"""Checkpointable external batch runner for frozen V1 A1 H126 synthesis.

Progress output contains hashes, timings, sizes and states only. Scientific
values remain inside atomic unit payloads and the final synthesis artifact.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
LAYER_ROOT = Path(r"D:\MechanismAwareStatArbData\A1_H126")
WORK_ROOT = LAYER_ROOT / "synthesis_checkpoint_v1"
UNITS_ROOT = WORK_ROOT / "units"
PROGRESS = WORK_ROOT / "progress.json"
FINAL = ROOT / "data/manifests/V1_PRE_HELD_OUT_A1_SYNTHESIS.json"
LAYER_MANIFEST = ROOT / "data/manifests/V1_A1_H126_CANDIDATE_NEUTRAL.json"
CANDIDATES = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W", "V1-R3-252M", "V1-R4-63D"]
FOLDS = [("inner", f"{y}H{h}") for y in range(2015, 2020) for h in (1, 2)] + [("of4", str(y)) for y in range(2020, 2024)]
FIELDS = ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba")
VERSION = "V1-A1-H126-CN-SCALE-LOSS-1.0"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json_atomic(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(obj, sort_keys=True, indent=2) + "\n")
    os.replace(temp, path)


def layer_path(role: str, candidate: str, fold: str) -> Path:
    return LAYER_ROOT / role / candidate / f"{fold}.npy.gz"


def load_layer(role: str, candidate: str, fold: str) -> np.ndarray:
    source = layer_path(role, candidate, fold)
    manifest = json.loads(LAYER_MANIFEST.read_text(encoding='utf-8'))
    records = [x for x in manifest['records'] if x['role'] == role and x['candidate'] == candidate and x['partition'] == fold]
    if len(records) != 1: raise RuntimeError('layer identity binding mismatch')
    record = records[0]
    if sha(source) != record['sha256']: raise RuntimeError('immutable layer hash mismatch')
    cache = WORK_ROOT / '_input_cache' / role / candidate / f'{fold}.npy'
    if cache.exists():
        if sha(cache) != record['raw_sha256']: raise RuntimeError('noncanonical input cache hash mismatch')
    else:
        cache.parent.mkdir(parents=True, exist_ok=True)
        temp = cache.with_name(cache.name + '.tmp')
        with gzip.open(source, 'rb') as inp, temp.open('wb') as out:
            shutil.copyfileobj(inp, out, 8 << 20)
        if sha(temp) != record['raw_sha256']: raise RuntimeError('layer lossless cache validation failed')
        os.replace(temp, cache)
    return np.load(cache, mmap_mode='r', allow_pickle=False)


def keys(arr: np.ndarray) -> np.ndarray:
    return (arr["date_ix"].astype(np.uint64) << 20) | (arr["a"].astype(np.uint64) << 10) | arr["b"].astype(np.uint64)


def median_by_pair(values: np.ndarray, pairs: np.ndarray) -> np.ndarray:
    if not len(values):
        return np.empty(0, dtype=np.float64)
    order = np.lexsort((values, pairs))
    p, v = pairs[order], values[order]
    starts = np.r_[0, np.flatnonzero(np.diff(p)) + 1]
    ends = np.r_[starts[1:], len(p)]
    counts = ends - starts
    lo = starts + (counts - 1) // 2
    hi = starts + counts // 2
    return 0.5 * (v[lo] + v[hi])


def summarize(arr: np.ndarray, indexes: np.ndarray, field: str) -> dict:
    values = arr[field][indexes].astype(np.float64)
    good = np.isfinite(values)
    idx, values = indexes[good], values[good]
    pair = (arr["a"][idx].astype(np.uint32) << 10) | arr["b"][idx].astype(np.uint32)
    pp = median_by_pair(values, pair)
    center = float(np.median(pp)) if len(pp) else None
    return {"observation_count": int(len(values)), "pair_count": int(len(pp)), "equal_pair_median": center,
            "equal_pair_mad": float(np.median(np.abs(pp - center))) if len(pp) else None}


def unit_specs() -> list[dict]:
    specs = []
    for role, fold in FOLDS:
        specs.append({"id": f"support__{role}__{fold}", "kind": "support", "role": role, "fold": fold})
        for candidate in CANDIDATES:
            specs.append({"id": f"summary__{role}__{fold}__{candidate}", "kind": "summary", "role": role, "fold": fold, "candidate": candidate})
        for i, left in enumerate(CANDIDATES):
            for right in CANDIDATES[i + 1:]:
                specs.append({"id": f"compare__{role}__{fold}__{left}__{right}", "kind": "comparison", "role": role, "fold": fold, "left": left, "right": right})
    return specs


def unit_path(spec: dict) -> Path:
    suffix = ".npy.gz" if spec["kind"] == "support" else ".json"
    return UNITS_ROOT / (spec["id"] + suffix)


def initialize() -> dict:
    layer_hash = sha(LAYER_MANIFEST)
    specs = unit_specs()
    if PROGRESS.exists():
        progress = json.loads(PROGRESS.read_text(encoding="utf-8"))
        if progress["layer_manifest_sha256"] != layer_hash or progress["unit_count"] != len(specs):
            raise RuntimeError("existing progress manifest is bound to different inputs")
        return progress
    progress = {"progress_id": "V1-A1-H126-SYNTHESIS-CHECKPOINT-1.0", "state": "READY",
                "layer_manifest_sha256": layer_hash, "unit_count": len(specs), "completed": 0,
                "scientific_values_exposed": False, "held_out_accessed": False, "units": {}}
    write_json_atomic(PROGRESS, progress)
    return progress


def verify_completed(progress: dict) -> None:
    for uid, rec in progress["units"].items():
        path = Path(rec["path"])
        if not path.exists() or sha(path) != rec["sha256"]:
            raise RuntimeError(f"completed unit hash failure: {uid}")


def load_support(role: str, fold: str) -> np.ndarray:
    path = unit_path({"id": f"support__{role}__{fold}", "kind": "support"})
    with gzip.open(path, "rb") as stream:
        return np.load(stream, allow_pickle=False)


def support_unit(spec: dict, dest: Path) -> None:
    common = None
    for candidate in CANDIDATES:
        arr = load_layer(spec["role"], candidate, spec["fold"])
        valid = np.isfinite(arr["loss_abs_ab"]) & np.isfinite(arr["loss_abs_ba"])
        current = keys(arr)[valid]
        common = current if common is None else np.intersect1d(common, current, assume_unique=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    raw = dest.with_name(dest.name + ".tmp.npy")
    tmp = dest.with_name(dest.name + ".tmp.gz")
    for transient in (raw, tmp):
        if transient.exists():
            transient.unlink()
    try:
        # Passing a file handle prevents NumPy from altering the exact temp path.
        with raw.open("wb") as stream:
            np.save(stream, common, allow_pickle=False)
        with raw.open("rb") as inp, tmp.open("wb") as raw_out:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out, compresslevel=9, mtime=0) as out:
                shutil.copyfileobj(inp, out, 8 << 20)
        with gzip.open(tmp, "rb") as stream:
            check = np.load(stream, allow_pickle=False)
        if not np.array_equal(common, check):
            raise RuntimeError("support unit roundtrip failure")
        os.replace(tmp, dest)
    finally:
        for transient in (raw, tmp):
            if transient.exists():
                transient.unlink()


def align(arr: np.ndarray, common: np.ndarray) -> np.ndarray:
    k = keys(arr); order = np.argsort(k, kind="stable"); pos = np.searchsorted(k[order], common)
    if np.any(pos >= len(order)) or not np.array_equal(k[order[pos]], common):
        raise RuntimeError("exact common-support alignment failure")
    return order[pos]


def summary_unit(spec: dict, dest: Path) -> None:
    arr = load_layer(spec["role"], spec["candidate"], spec["fold"]); common = load_support(spec["role"], spec["fold"])
    common_ix = align(arr, common)
    native_ix = np.flatnonzero(np.isfinite(arr["loss_abs_ab"]) & np.isfinite(arr["loss_abs_ba"]))
    obj = {"kind": "candidate_fold_summary", "role": spec["role"], "fold": spec["fold"], "candidate": spec["candidate"],
           "support": {"native_rows": int(len(native_ix)), "common_rows": int(len(common_ix))},
           "common": {f: summarize(arr, common_ix, f) for f in FIELDS},
           "native": {f: summarize(arr, native_ix, f) for f in FIELDS}}
    write_json_atomic(dest, obj)


def comparison_unit(spec: dict, dest: Path) -> None:
    common = load_support(spec["role"], spec["fold"])
    left, right = load_layer(spec["role"], spec["left"], spec["fold"]), load_layer(spec["role"], spec["right"], spec["fold"])
    li, ri = align(left, common), align(right, common)
    pair = (left["a"][li].astype(np.uint32) << 10) | left["b"][li].astype(np.uint32)
    metrics = {}
    for field in FIELDS:
        delta = right[field][ri].astype(np.float64) - left[field][li].astype(np.float64)
        pp = median_by_pair(delta, pair)
        metrics[field] = {"right_minus_left_equal_pair_median": float(np.median(pp)) if len(pp) else None,
                          "pair_count": int(len(pp)), "observation_count": int(len(delta))}
    write_json_atomic(dest, {"kind": "candidate_comparison_fold", "role": spec["role"], "fold": spec["fold"],
                             "left": spec["left"], "right": spec["right"], "metrics": metrics})


def finalize(progress: dict) -> None:
    summaries, comparisons = [], []
    for spec in unit_specs():
        if spec["kind"] == "support": continue
        obj = json.loads(unit_path(spec).read_text(encoding="utf-8"))
        (summaries if spec["kind"] == "summary" else comparisons).append(obj)
    temporal = {"candidate": {}, "pairwise": {}, "roles_kept_separate": True}
    for candidate in CANDIDATES:
        temporal["candidate"][candidate] = {}
        for role in ("inner", "of4"):
            items = [x for x in summaries if x["candidate"] == candidate and x["role"] == role]
            temporal["candidate"][candidate][role] = {scope: {field: {
                "temporal_median_of_fold_equal_pair_medians": float(np.median([x[scope][field]["equal_pair_median"] for x in items])),
                "fold_count": len(items)} for field in FIELDS} for scope in ("common", "native")}
    for i, left in enumerate(CANDIDATES):
        for right in CANDIDATES[i + 1:]:
            temporal["pairwise"][f"{left}__{right}"] = {}
            for role in ("inner", "of4"):
                items = [x for x in comparisons if x["left"] == left and x["right"] == right and x["role"] == role]
                temporal["pairwise"][f"{left}__{right}"][role] = {field: {
                    "temporal_median_of_fold_equal_pair_median_differences": float(np.median([x["metrics"][field]["right_minus_left_equal_pair_median"] for x in items])),
                    "fold_count": len(items)} for field in FIELDS}
    out = {"synthesis_id": "V1-PRE-HELD-OUT-A1-H126-SYNTHESIS-1.0", "scale_version": VERSION,
           "status": "CORRECTED_EVIDENCE_AVAILABLE_FOR_RESEARCHER_INTERPRETATION", "results": summaries,
           "pairwise_common_support": comparisons, "temporal_median_vector": temporal,
           "uncertainty": "NOT_ESTIMATED_EXACT_COMPARATIVE_UNCERTAINTY_METHOD_UNFROZEN",
           "multiplicity": "NO_NUMERICAL_CORRECTION_EXACT_METHOD_AND_LEVEL_UNFROZEN",
           "severe_failure": "NOT_ACTIVATED_UNDERLYING_NUMERICAL_EVENT_UNFROZEN", "ranking": "NOT_FORCED",
           "a6_g5": "V1_NON_ESTIMABLE_NOT_EXECUTED", "held_out": "2024_2025_SEALED_NOT_ACCESSED"}
    write_json_atomic(FINAL, out)


def run(resume: bool, through_unit: str | None = None) -> None:
    progress = initialize(); verify_completed(progress)
    if not resume and progress["completed"]:
        raise RuntimeError("completed checkpoints exist; use resume")
    valid_ids = {spec["id"] for spec in unit_specs()}
    if through_unit is not None and through_unit not in valid_ids:
        raise RuntimeError(f"unknown bounded stop unit: {through_unit}")
    progress["state"] = "RUNNING"; write_json_atomic(PROGRESS, progress)
    for spec in unit_specs():
        uid, dest = spec["id"], unit_path(spec)
        if uid in progress["units"]:
            if uid == through_unit:
                break
            continue
        if dest.exists():
            raise RuntimeError(f"unregistered unit exists: {dest}")
        started = time.perf_counter()
        if spec["kind"] == "support": support_unit(spec, dest)
        elif spec["kind"] == "summary": summary_unit(spec, dest)
        else: comparison_unit(spec, dest)
        rec = {"kind": spec["kind"], "path": str(dest), "sha256": sha(dest), "bytes": dest.stat().st_size,
               "runtime_seconds": time.perf_counter() - started}
        progress["units"][uid] = rec; progress["completed"] = len(progress["units"])
        write_json_atomic(PROGRESS, progress)
        if uid == through_unit:
            break
    if through_unit is not None:
        progress["state"] = "PARTIAL_READY"
        write_json_atomic(PROGRESS, progress)
        return
    finalize(progress); progress["state"] = "COMPLETE"; progress["final_sha256"] = sha(FINAL)
    write_json_atomic(PROGRESS, progress)


def status() -> None:
    p = initialize()
    print(json.dumps({"state": p["state"], "completed": p["completed"], "unit_count": p["unit_count"],
                      "scientific_values_exposed": False, "held_out_accessed": False}))


def validate() -> None:
    p = initialize(); verify_completed(p)
    final_ok = p["state"] != "COMPLETE" or (FINAL.exists() and sha(FINAL) == p["final_sha256"])
    if not final_ok: raise RuntimeError("final synthesis hash failure")
    print(json.dumps({"result": "PASS", "state": p["state"], "completed": p["completed"], "unit_count": p["unit_count"],
                      "scientific_values_exposed": False, "held_out_accessed": False}))


def benchmark() -> None:
    # Structural fixed-prefix benchmark only; no scientific statistic is retained.
    started = time.perf_counter(); peak = 0; rows = 0
    for candidate in CANDIDATES:
        arr = load_layer("inner", candidate, "2015H1"); rows += min(len(arr), 100_000)
        sample = arr[:100_000]; _ = keys(sample); _ = np.isfinite(sample["loss_abs_ab"])
        peak = max(peak, arr.nbytes)
    elapsed = time.perf_counter() - started
    # Conservative I/O-dominated projection from fixed-prefix throughput and 406 units.
    per_unit = max(1.0, elapsed * 2.0)
    print(json.dumps({"benchmark": "FIXED_PREFIX_STRUCTURAL_NO_VALUES", "work_units": len(unit_specs()),
                      "sample_rows": rows, "elapsed_seconds": elapsed, "projected_seconds_per_unit": per_unit,
                      "projected_total_hours": per_unit * len(unit_specs()) / 3600.0,
                      "peak_array_bytes_observed": peak, "peak_temporary_storage_bytes": 2 * peak,
                      "scientific_values_exposed": False, "held_out_accessed": False}))


def dry_run() -> None:
    """Validate wiring and checkpoint contract without executing a unit."""
    progress = initialize()
    verify_completed(progress)
    specs = unit_specs()
    if len(specs) != 406 or sum(x["kind"] == "support" for x in specs) != 14 or sum(x["kind"] == "summary" for x in specs) != 98 or sum(x["kind"] == "comparison" for x in specs) != 294:
        raise RuntimeError("bounded unit registry mismatch")
    if FINAL.exists() and progress["state"] != "COMPLETE":
        raise RuntimeError("final artifact exists without COMPLETE checkpoint state")
    print(json.dumps({"dry_run": "PASS", "state": progress["state"], "completed": progress["completed"],
                      "unit_count": progress["unit_count"], "support_units": 14, "summary_units": 98,
                      "comparison_units": 294, "units_executed": 0, "scientific_values_exposed": False,
                      "held_out_accessed": False}))


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("command", choices=("status", "run", "resume", "validate", "benchmark", "dry-run", "smoke-one")); parser.add_argument("--through-unit"); args = parser.parse_args()
    first = "support__inner__2015H1"
    {"status": status, "run": lambda: run(False, args.through_unit), "resume": lambda: run(True, args.through_unit),
     "validate": validate, "benchmark": benchmark, "dry-run": dry_run,
     "smoke-one": lambda: run(False, first)}[args.command]()


if __name__ == "__main__": main()
