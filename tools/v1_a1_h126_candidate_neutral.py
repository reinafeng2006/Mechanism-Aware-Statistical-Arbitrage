"""Build the versioned candidate-neutral H126 A1 scale/loss layer.

The H126 R0-C relationship artifact is the immutable scale-input lineage source:
its PS0/PS1 fields were computed from the exact frozen H126 qualified-PIT
response geometry.  Predictions and all ancestor payloads are read-only.
Scientific values are written to checksummed artifacts and are never printed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EXT = Path(r"D:\MechanismAwareStatArbData\A1_H126")
OF4 = Path(r"D:\MechanismAwareStatArbData\OF4")
INNER_INPUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"
OF4_INPUT = OF4 / "input/of4_input_v1.npz"
INNER_REL = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/relationships"
OF4_REL = OF4 / "relationships"
MANIFEST = ROOT / "data/manifests/V1_A1_H126_CANDIDATE_NEUTRAL.json"
SYNTHESIS = ROOT / "data/manifests/V1_PRE_HELD_OUT_A1_SYNTHESIS.json"
CANDIDATES = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W", "V1-R3-252M", "V1-R4-63D"]
INNER_PARTS = [f"{year}H{half}" for year in range(2015, 2020) for half in (1, 2)]
OF4_PARTS = [str(year) for year in range(2020, 2024)]
VERSION = "V1-A1-H126-CN-SCALE-LOSS-1.0"
ELIGIBILITY = "PAIR-A+C04-A+C05+C06-AVAILABILITY-AMENDMENT-V1+V1-EXECUTABLE-SEMANTICS-A1"

DT = np.dtype([
    ("date_ix", "<u2"), ("a", "<u2"), ("b", "<u2"), ("ancestor_row", "<u4"),
    ("scale_state_ab", "u1"), ("scale_state_ba", "u1"),
    ("ps0_a", "<f4"), ("ps0_b", "<f4"), ("ps1_a", "<f4"), ("ps1_b", "<f4"),
    ("loss_abs_ab", "<f4"), ("loss_abs_ba", "<f4"),
    ("loss_sq_ab", "<f4"), ("loss_sq_ba", "<f4"),
])


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def key(arr: np.ndarray) -> np.ndarray:
    return (arr["date_ix"].astype(np.uint64) << 20) | (arr["a"].astype(np.uint64) << 10) | arr["b"].astype(np.uint64)


def load_array(path: Path) -> np.ndarray:
    if path.suffix == ".gz":
        with gzip.open(path, "rb") as stream:
            return np.load(stream, allow_pickle=False)
    return np.load(path, mmap_mode="r", allow_pickle=False)


def relationship_path(role: str, candidate: str, part: str) -> Path:
    base = INNER_REL if role == "inner" else OF4_REL
    raw = base / candidate / f"{part}.npy"
    return raw if raw.exists() else raw.with_suffix(".npy.gz")


def atomic_compress(array: np.ndarray, final: Path) -> dict:
    final.parent.mkdir(parents=True, exist_ok=True)
    raw = final.with_suffix(".tmp.npy")
    gztemp = final.with_suffix(".tmp.gz")
    np.save(raw, array, allow_pickle=False)
    raw_hash = sha(raw)
    with raw.open("rb") as inp, gztemp.open("wb") as raw_out:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out, compresslevel=9, mtime=0) as out:
            shutil.copyfileobj(inp, out, 8 << 20)
    check = hashlib.sha256()
    with gzip.open(gztemp, "rb") as inp:
        for chunk in iter(lambda: inp.read(8 << 20), b""):
            check.update(chunk)
    if check.hexdigest().upper() != raw_hash:
        raise RuntimeError(f"lossless roundtrip failed: {final}")
    compressed_hash = sha(gztemp)
    os.replace(gztemp, final)
    record = {"physical_path": str(final), "sha256": compressed_hash, "raw_sha256": raw_hash,
              "rows": int(len(array)), "logical_direction_rows": int(2 * len(array)),
              "raw_bytes": raw.stat().st_size, "compressed_bytes": final.stat().st_size,
              "compression": "GZIP_DEFLATE_LEVEL9_MTIME0_FILENAME_EMPTY", "validation": "LOSSLESS_ROUNDTRIP_PASS"}
    raw.unlink()
    return record


def build_partition(role: str, part: str, response: np.ndarray) -> list[dict]:
    scale_path = relationship_path(role, "V1-R0C-126W", part)
    scales = load_array(scale_path)
    skey = key(scales)
    order = np.argsort(skey, kind="stable")
    skey = skey[order]
    records = []
    for candidate in CANDIDATES:
        ancestor = relationship_path(role, candidate, part)
        arr = load_array(ancestor)
        akey = key(arr)
        pos = np.searchsorted(skey, akey)
        matched = pos < len(skey)
        matched[matched] &= skey[pos[matched]] == akey[matched]
        out = np.empty(len(arr), DT)
        out["date_ix"], out["a"], out["b"] = arr["date_ix"], arr["a"], arr["b"]
        out["ancestor_row"] = np.arange(len(arr), dtype=np.uint32)
        for name in ("ps0_a", "ps0_b", "ps1_a", "ps1_b", "loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba"):
            out[name] = np.nan
        if np.any(matched):
            ix = np.flatnonzero(matched)
            src = scales[order[pos[ix]]]
            for name in ("ps0_a", "ps0_b", "ps1_a", "ps1_b"):
                out[name][ix] = src[name]
            mu_ab = arr["mu_n1_ab"] if "mu_n1_ab" in arr.dtype.names else arr["mu_ab"]
            mu_ba = arr["mu_n1_ba"] if "mu_n1_ba" in arr.dtype.names else arr["mu_ba"]
            observed_b = response[arr["date_ix"][ix], arr["b"][ix]]
            observed_a = response[arr["date_ix"][ix], arr["a"][ix]]
            ps0a, ps0b, ps1a, ps1b = (out[n][ix].astype(np.float64) for n in ("ps0_a", "ps0_b", "ps1_a", "ps1_b"))
            eab = observed_b - mu_ab[ix].astype(np.float64)
            eba = observed_a - mu_ba[ix].astype(np.float64)
            valid_ab = np.isfinite(eab) & np.isfinite(ps0b) & np.isfinite(ps1b) & (ps0b != 0) & (ps1b != 0)
            valid_ba = np.isfinite(eba) & np.isfinite(ps0a) & np.isfinite(ps1a) & (ps0a != 0) & (ps1a != 0)
            j = ix[valid_ab]
            out["loss_abs_ab"][j] = np.abs(eab[valid_ab]) / ps0b[valid_ab]
            out["loss_sq_ab"][j] = (eab[valid_ab] / ps1b[valid_ab]) ** 2
            j = ix[valid_ba]
            out["loss_abs_ba"][j] = np.abs(eba[valid_ba]) / ps0a[valid_ba]
            out["loss_sq_ba"][j] = (eba[valid_ba] / ps1a[valid_ba]) ** 2
        out["scale_state_ab"] = np.isfinite(out["loss_abs_ab"])
        out["scale_state_ba"] = np.isfinite(out["loss_abs_ba"])
        final = EXT / role / candidate / f"{part}.npy.gz"
        rec = atomic_compress(out, final)
        rec.update({"role": role, "candidate": candidate, "partition": part,
                    "ancestor_artifact": str(ancestor), "ancestor_sha256": sha(ancestor),
                    "scale_lineage_artifact": str(scale_path), "scale_lineage_sha256": sha(scale_path),
                    "scale_version": VERSION, "eligibility_version": ELIGIBILITY,
                    "candidate_native_scale_status": "NOT_CANONICAL_FOR_CROSS_CANDIDATE_A1_LOSS_COMPARISON"})
        records.append(rec)
    return records


def write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(obj, sort_keys=True, indent=2) + "\n")
    os.replace(temp, path)


def build() -> None:
    records = []
    with np.load(INNER_INPUT, allow_pickle=False) as z:
        response = z["response"]
        for part in INNER_PARTS:
            records.extend(build_partition("inner", part, response))
    with np.load(OF4_INPUT, allow_pickle=False) as z:
        response = z["response"]
        for part in OF4_PARTS:
            records.extend(build_partition("of4", part, response))
    manifest = {"manifest_id": VERSION, "status": "IMMUTABLE_COMPLETE_CHECKSUMMED", "decision": "V1-A1-H126-CN-1.0",
                "publication_commit": "938a43a", "physical_root": str(EXT), "scale_source_candidate": "V1-R0C-126W",
                "scale_source_role": "IMMUTABLE_H126_GEOMETRY_LINEAGE_ONLY_NOT_COMPARISON_PRIVILEGE",
                "ps0": "1.4826_MAD_H126_QUALIFIED_PIT", "ps1": "SAMPLE_SD_DDOF1_SAME_H126_GEOMETRY",
                "point_loss": "ABS_ERROR_DIV_PS0", "robustness_loss": "SQUARED_ERROR_DIV_PS1_SQUARED",
                "pit": "STRICTLY_BEFORE_EVALUATED_EVENT", "records": records,
                "ancestor_mutation": False, "relationship_recomputation": False, "held_out": "2024_2025_SEALED_NOT_ACCESSED",
                "values_disclosed_during_construction": False}
    write_json(MANIFEST, manifest)


def median_by_pair(values: np.ndarray, pairs: np.ndarray) -> np.ndarray:
    if not len(values):
        return np.empty(0, dtype=np.float64)
    # Lexicographic pair/value sort makes each group's two middle order
    # statistics directly addressable without a Python group loop.
    order = np.lexsort((values, pairs))
    p, v = pairs[order], values[order]
    starts = np.r_[0, np.flatnonzero(np.diff(p)) + 1]
    ends = np.r_[starts[1:], len(p)]
    counts = ends - starts
    lo = starts + (counts - 1) // 2
    hi = starts + counts // 2
    return 0.5 * (v[lo] + v[hi])


def summarize_values(arr: np.ndarray, indexes: np.ndarray, field: str) -> dict:
    vals = arr[field][indexes].astype(np.float64)
    good = np.isfinite(vals)
    idx = indexes[good]
    vals = vals[good]
    pair = (arr["a"][idx].astype(np.uint32) << 10) | arr["b"][idx].astype(np.uint32)
    per_pair = median_by_pair(vals, pair) if len(vals) else np.empty(0)
    return {"observation_count": int(len(vals)), "pair_count": int(len(per_pair)),
            "equal_pair_median": float(np.median(per_pair)) if len(per_pair) else None,
            "equal_pair_mad": float(np.median(np.abs(per_pair - np.median(per_pair)))) if len(per_pair) else None}


def synthesize() -> None:
    raise RuntimeError("monolithic synthesis is disabled; use v1_a1_h126_synthesis_batch.py")
    if not MANIFEST.exists():
        raise RuntimeError("validated H126 manifest required")
    output = {"synthesis_id": "V1-PRE-HELD-OUT-A1-H126-SYNTHESIS-1.0", "scale_version": VERSION,
              "status": "CORRECTED_EVIDENCE_AVAILABLE_FOR_RESEARCHER_INTERPRETATION", "results": [],
              "uncertainty": "NOT_ESTIMATED_EXACT_COMPARATIVE_UNCERTAINTY_METHOD_UNFROZEN",
              "multiplicity": "NO_NUMERICAL_CORRECTION_EXACT_METHOD_AND_LEVEL_UNFROZEN",
              "severe_failure": "NOT_ACTIVATED_UNDERLYING_NUMERICAL_EVENT_UNFROZEN",
              "ranking": "NOT_FORCED", "a6_g5": "V1_NON_ESTIMABLE_NOT_EXECUTED", "held_out": "2024_2025_SEALED_NOT_ACCESSED"}
    for role, parts in (("inner", INNER_PARTS), ("of4", OF4_PARTS)):
        for part in parts:
            arrays = {c: load_array(EXT / role / c / f"{part}.npy.gz") for c in CANDIDATES}
            keys = {c: key(a) for c, a in arrays.items()}
            common = keys[CANDIDATES[0]][np.isfinite(arrays[CANDIDATES[0]]["loss_abs_ab"]) & np.isfinite(arrays[CANDIDATES[0]]["loss_abs_ba"])]
            for candidate in CANDIDATES[1:]:
                valid = np.isfinite(arrays[candidate]["loss_abs_ab"]) & np.isfinite(arrays[candidate]["loss_abs_ba"])
                common = np.intersect1d(common, keys[candidate][valid], assume_unique=True)
            aligned = {}
            for candidate in CANDIDATES:
                order = np.argsort(keys[candidate], kind="stable")
                pos = np.searchsorted(keys[candidate][order], common)
                aligned[candidate] = order[pos]
                native = np.flatnonzero(np.isfinite(arrays[candidate]["loss_abs_ab"]) & np.isfinite(arrays[candidate]["loss_abs_ba"]))
                output["results"].append({"role": role, "partition": part, "candidate": candidate,
                    "support": {"native_rows": int(len(native)), "common_rows": int(len(common))},
                    "common": {f: summarize_values(arrays[candidate], aligned[candidate], f) for f in ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba")},
                    "native": {f: summarize_values(arrays[candidate], native, f) for f in ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba")}})
            comparisons = []
            for i, left in enumerate(CANDIDATES):
                for right in CANDIDATES[i + 1:]:
                    row = {"left": left, "right": right}
                    for field in ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba"):
                        delta = arrays[right][field][aligned[right]].astype(np.float64) - arrays[left][field][aligned[left]].astype(np.float64)
                        pair = (arrays[left]["a"][aligned[left]].astype(np.uint32) << 10) | arrays[left]["b"][aligned[left]].astype(np.uint32)
                        pp = median_by_pair(delta, pair) if len(delta) else np.empty(0)
                        row[field] = {"right_minus_left_equal_pair_median": float(np.median(pp)) if len(pp) else None,
                                      "pair_count": int(len(pp)), "observation_count": int(len(delta))}
                    comparisons.append(row)
            output.setdefault("pairwise_common_support", []).append({"role": role, "partition": part, "comparisons": comparisons})
    write_json(SYNTHESIS, output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("build",))
    args = parser.parse_args()
    build()
    print(json.dumps({"stage": args.stage, "result": "PASS", "values_disclosed": False, "held_out_accessed": False}))


if __name__ == "__main__":
    main()
