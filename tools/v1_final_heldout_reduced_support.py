"""Checkpointed reduced-support completion of the frozen V1 final held-out run.

R4/H4 is terminal computation-incomplete for V1.  This runner never invokes
R4 and never treats its engineering blocks as scientific held-out evidence.
It completes only the six-candidate H1/H2/H3/H5 execution set authorized by
the plan frozen at 2df48ef.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EXT = Path(r"D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1")
CONTROL = EXT / "_control"
PROGRESS = CONTROL / "progress_reduced_support.json"
ACCESS = CONTROL / "heldout_access_event.json"
INPUT = EXT / "input/of4_input_v1.npz"
REL, STATE, A3A5 = EXT / "relationships", EXT / "rt3_state", EXT / "a3_a5"
LAYER = EXT / "a1_h126_reduced_support"
LAYER_MANIFEST = EXT / "_metadata/V1_FINAL_HELDOUT_A1_H126_REDUCED_SUPPORT.json"
STAGE_MANIFEST = EXT / "_metadata/final_relationship_stage_reduced_support.json"
SYNTH_ROOT = EXT / "synthesis_checkpoint_reduced_support_v1"
FINAL = EXT / "_metadata/V1_FINAL_HELDOUT_A1_SYNTHESIS_REDUCED_SUPPORT.json"
MATERIALIZER = ROOT / "tools/v1_of4_materialize.py"
PLAN = ROOT / "docs/stages/G4/V1_FINAL_HELDOUT_COMPUTATION_INCOMPLETE_PLAN.md"
CANDIDATES = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W", "V1-R3-252M"]
FOLDS = ["2024", "2025"]
FIELDS = ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba")
VERSION = "V1-FINAL-HELDOUT-REDUCED-SUPPORT-1.0"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def atomic_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(obj, sort_keys=True, indent=2) + "\n")
        stream.flush(); os.fsync(stream.fileno())
    os.replace(temp, path)


def load_progress(create: bool = False) -> dict:
    if PROGRESS.exists():
        p = json.loads(PROGRESS.read_text(encoding="utf-8"))
        if p.get("progress_id") != VERSION: raise RuntimeError("reduced-support progress identity mismatch")
        return p
    p = {"progress_id": VERSION, "state": "READY", "completed_stages": [], "stage_hashes": {},
         "held_out_accessed": ACCESS.exists(), "scientific_values_exposed": False,
         "excluded_candidate": "V1-R4-63D", "h4": "COMPUTATION-INCOMPLETE / NO FINAL HELD-OUT DISPOSITION"}
    if create: atomic_json(PROGRESS, p)
    return p


def save(p: dict) -> None:
    p["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    atomic_json(PROGRESS, p)


def artifact(root: Path, candidate: str, fold: str, suffix: str = ".npy") -> Path:
    raw = root / candidate / f"{fold}{suffix}"
    gz = raw.with_suffix(raw.suffix + ".gz")
    return gz if gz.exists() else raw


def verify_checkpoint(root: Path, candidate: str, fold: str, kind: str) -> None:
    if kind == "a3a5":
        marker = root / candidate / f"{fold}.complete.json"
        meta = json.loads(marker.read_text(encoding="utf-8"))
        for tag in ("a3", "a5"):
            item = artifact(root, candidate, fold, f".{tag}.npy")
            expected = meta[f"{tag}_sha256"]
            if item.suffix == ".gz":
                compressed = json.loads(item.with_suffix(item.suffix + ".complete.json").read_text(encoding="utf-8"))
                if sha(item) != compressed["sha256"] or compressed["raw_sha256"] != expected:
                    raise RuntimeError(f"{tag} compressed lineage mismatch: {candidate}/{fold}")
            actual = sha(item) if item.suffix != ".gz" else compressed_raw_sha(item)
            if actual != expected: raise RuntimeError(f"{tag} hash mismatch: {candidate}/{fold}")
        return
    path = artifact(root, candidate, fold)
    if not path.is_file(): raise RuntimeError(f"missing {kind} checkpoint: {candidate}/{fold}")
    marker = path.with_suffix(path.suffix + ".complete.json") if path.suffix == ".gz" else root / candidate / f"{fold}.complete.json"
    key = "sha256"
    if not marker.is_file(): raise RuntimeError(f"missing {kind} marker: {candidate}/{fold}")
    meta = json.loads(marker.read_text(encoding="utf-8"))
    actual = sha(path)
    if actual != meta[key]: raise RuntimeError(f"{kind} hash mismatch: {candidate}/{fold}")


def compressed_raw_sha(path: Path) -> str:
    h = hashlib.sha256()
    with gzip.open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def preflight() -> None:
    if not ACCESS.is_file() or not json.loads(ACCESS.read_text(encoding="utf-8")).get("held_out_accessed"):
        raise RuntimeError("irreversible held-out access event missing")
    if not PLAN.is_file() or not INPUT.is_file(): raise RuntimeError("reduced-support plan or held-out input missing")
    for candidate in CANDIDATES:
        for fold in FOLDS:
            verify_checkpoint(REL, candidate, fold, "relationship")
            verify_checkpoint(STATE, candidate, fold, "state")


def run_a3a5(candidate: str, fold: str) -> None:
    env = os.environ.copy(); env["V1_MATERIALIZATION_ROLE"] = "FINAL_HELDOUT"
    subprocess.run([sys.executable, str(MATERIALIZER), "a3a5", "--candidate", candidate, "--partition", fold],
                   cwd=ROOT, env=env, check=True)
    verify_checkpoint(A3A5, candidate, fold, "a3a5")


def compress_one(source: Path) -> dict:
    final = source.with_suffix(source.suffix + ".gz")
    marker = final.with_suffix(final.suffix + ".complete.json")
    if final.exists() or marker.exists():
        if not (final.exists() and marker.exists()): raise RuntimeError(f"incomplete compressed checkpoint: {final}")
        rec = json.loads(marker.read_text(encoding="utf-8"))
        if sha(final) != rec["sha256"] or compressed_raw_sha(final) != rec["raw_sha256"]:
            raise RuntimeError(f"compressed checkpoint validation failed: {final}")
        return rec
    if not source.is_file(): raise RuntimeError(f"missing compression source: {source}")
    raw_hash, raw_bytes = sha(source), source.stat().st_size
    temp = final.with_name(final.name + ".tmp")
    with source.open("rb") as inp, temp.open("wb") as raw_out:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out, compresslevel=9, mtime=0) as out:
            shutil.copyfileobj(inp, out, 8 << 20)
    if compressed_raw_sha(temp) != raw_hash: raise RuntimeError(f"lossless compression failure: {source}")
    os.replace(temp, final)
    rec = {"logical_path": source.relative_to(EXT).as_posix(), "physical_relative_path": final.relative_to(EXT).as_posix(),
           "raw_sha256": raw_hash, "sha256": sha(final), "raw_bytes": raw_bytes,
           "compressed_bytes": final.stat().st_size, "compression": "GZIP_DEFLATE_LEVEL9_MTIME0_FILENAME_EMPTY",
           "validation": "LOSSLESS_ROUNDTRIP_PASS"}
    atomic_json(marker, rec); return rec


def compress_all() -> None:
    records = []
    for candidate in CANDIDATES:
        for fold in FOLDS:
            for root, suffix in ((REL, ".npy"), (STATE, ".npy"), (A3A5, ".a3.npy"), (A3A5, ".a5.npy")):
                raw = root / candidate / f"{fold}{suffix}"
                records.append(compress_one(raw))
    atomic_json(STAGE_MANIFEST, {"manifest_id": VERSION + "-PAYLOADS", "status": "IMMUTABLE_COMPLETE_CHECKSUMMED",
        "candidate_count": 6, "annual_folds": FOLDS, "payload_count": 48, "payloads": records,
        "excluded_candidate": "V1-R4-63D", "h4": "COMPUTATION-INCOMPLETE / NO FINAL HELD-OUT DISPOSITION",
        "r4_engineering_checkpoints_are_not_scientific_evidence": True, "held_out_accessed": True})


def layer_fold(fold: str) -> list[dict]:
    import v1_a1_h126_candidate_neutral as layer
    layer.EXT, layer.OF4_REL, layer.CANDIDATES = LAYER, REL, CANDIDATES
    records = []
    with np.load(INPUT, allow_pickle=False) as source:
        response = source["response"]
        for candidate in CANDIDATES:
            checkpoint = CONTROL / f"reduced_h126_{fold}_{candidate}.json"
            if checkpoint.exists():
                rec = json.loads(checkpoint.read_text(encoding="utf-8"))
                if sha(Path(rec["physical_path"])) != rec["sha256"]:
                    raise RuntimeError("completed H126 candidate hash mismatch")
            else:
                final = LAYER / "heldout" / candidate / f"{fold}.npy.gz"
                if final.exists(): raise RuntimeError(f"unverified H126 artifact requires recovery: {final}")
                layer.CANDIDATES = [candidate]
                rec = layer.build_partition("heldout", fold, response)[0]
                atomic_json(checkpoint, rec)
            records.append(rec)
    return records


def configure_synthesis():
    import v1_a1_h126_synthesis_batch as syn
    syn.CANDIDATES = CANDIDATES; syn.FOLDS = [("heldout", x) for x in FOLDS]
    syn.LAYER_ROOT = LAYER; syn.WORK_ROOT = SYNTH_ROOT; syn.UNITS_ROOT = SYNTH_ROOT / "units"
    syn.PROGRESS = SYNTH_ROOT / "progress.json"; syn.FINAL = FINAL; syn.LAYER_MANIFEST = LAYER_MANIFEST
    return syn


def finalize_synthesis(syn, p: dict) -> None:
    summaries, comparisons = [], []
    for spec in syn.unit_specs():
        if spec["kind"] == "support": continue
        obj = json.loads(syn.unit_path(spec).read_text(encoding="utf-8"))
        (summaries if spec["kind"] == "summary" else comparisons).append(obj)
    temporal = {"candidate": {}, "pairwise": {}, "roles_kept_separate": True}
    for candidate in CANDIDATES:
        items = [x for x in summaries if x["candidate"] == candidate]
        temporal["candidate"][candidate] = {scope: {field: {
            "temporal_median_of_fold_equal_pair_medians": float(np.median([x[scope][field]["equal_pair_median"] for x in items])),
            "fold_count": len(items)} for field in FIELDS} for scope in ("common", "native")}
    for i, left in enumerate(CANDIDATES):
        for right in CANDIDATES[i + 1:]:
            items = [x for x in comparisons if x["left"] == left and x["right"] == right]
            temporal["pairwise"][f"{left}__{right}"] = {field: {
                "temporal_median_of_fold_equal_pair_median_differences": float(np.median(
                    [x["metrics"][field]["right_minus_left_equal_pair_median"] for x in items])),
                "fold_count": len(items)} for field in FIELDS}
    out = {"synthesis_id": VERSION + "-A1-CS2", "status": "FINAL_HELDOUT_REDUCED_SUPPORT_EVIDENCE_AVAILABLE_FOR_VALIDATION",
           "candidates": CANDIDATES, "results": summaries, "pairwise_common_support": comparisons,
           "temporal_median_vector": temporal,
           "confirmatory_bindings": {"C1": ["V1-R0L-126W", "V1-R1M-126W"], "C2": ["V1-R1M-126W", "V1-R1MI-126W"], "C3": ["V1-R0D-252M", "V1-R3-252M"], "C4": "UNAVAILABLE_R4_2025_COMPUTATION_INCOMPLETE"},
           "exact_common_support": True, "equal_pair_influence": True, "exact_medians": True,
           "folds_kept_separate": True, "ranking": "NOT_FORCED", "held_out_accessed": True}
    atomic_json(FINAL, out); p["state"] = "COMPLETE"; p["final_sha256"] = sha(FINAL); syn.write_json_atomic(syn.PROGRESS, p)


def run_synthesis() -> None:
    syn = configure_synthesis(); p = syn.initialize(); syn.verify_completed(p); p["state"] = "RUNNING"; syn.write_json_atomic(syn.PROGRESS, p)
    for spec in syn.unit_specs():
        uid, dest = spec["id"], syn.unit_path(spec)
        if uid in p["units"]: continue
        started = time.perf_counter()
        {"support": syn.support_unit, "summary": syn.summary_unit, "comparison": syn.comparison_unit}[spec["kind"]](spec, dest)
        p["units"][uid] = {"kind": spec["kind"], "path": str(dest), "sha256": sha(dest), "bytes": dest.stat().st_size,
                           "runtime_seconds": time.perf_counter() - started}
        p["completed"] = len(p["units"]); syn.write_json_atomic(syn.PROGRESS, p)
    finalize_synthesis(syn, p)


def execute(resume: bool) -> None:
    preflight(); p = load_progress(True)
    if not resume and p["completed_stages"]: raise RuntimeError("checkpoints exist; use resume")
    p["state"] = "RUNNING"; save(p)
    for candidate in CANDIDATES:
        for fold in FOLDS:
            name = f"a3a5:{candidate}:{fold}"
            if name not in p["completed_stages"]:
                if (A3A5 / candidate / f"{fold}.complete.json").exists():
                    verify_checkpoint(A3A5, candidate, fold, "a3a5")
                else:
                    run_a3a5(candidate, fold)
                p["completed_stages"].append(name); save(p)
            else: verify_checkpoint(A3A5, candidate, fold, "a3a5")
    if "compress" not in p["completed_stages"]: compress_all(); p["completed_stages"].append("compress"); save(p)
    records = []
    for fold in FOLDS:
        name, cp = f"h126:{fold}", CONTROL / f"reduced_h126_{fold}.json"
        if name not in p["completed_stages"]: atomic_json(cp, {"records": layer_fold(fold)}); p["completed_stages"].append(name); save(p)
        records.extend(json.loads(cp.read_text(encoding="utf-8"))["records"])
    for rec in records:
        if sha(Path(rec["physical_path"])) != rec["sha256"]: raise RuntimeError("H126 payload hash mismatch")
    atomic_json(LAYER_MANIFEST, {"manifest_id": VERSION + "-H126", "status": "IMMUTABLE_COMPLETE_CHECKSUMMED",
        "records": records, "candidate_count": 6, "candidate_neutral_h126": True, "held_out_accessed": True})
    if "synthesis" not in p["completed_stages"]: run_synthesis(); p["completed_stages"].append("synthesis")
    p["state"] = "COMPLETE"; p["final_sha256"] = sha(FINAL); save(p)


def validate() -> None:
    preflight(); p = load_progress(False)
    if p["state"] == "COMPLETE":
        if sha(FINAL) != p["final_sha256"]: raise RuntimeError("final hash mismatch")
        syn = configure_synthesis(); sp = json.loads(syn.PROGRESS.read_text(encoding="utf-8")); syn.verify_completed(sp)
        if sp["completed"] != 44: raise RuntimeError("reduced synthesis is not 44/44")
    print(json.dumps({"result": "PASS", "state": p["state"], "completed_stages": len(p["completed_stages"]),
                      "synthesis_completed": json.loads((SYNTH_ROOT / "progress.json").read_text())["completed"] if (SYNTH_ROOT / "progress.json").exists() else 0,
                      "scientific_values_exposed": False}))


def status() -> None:
    p = load_progress(False)
    print(json.dumps({"state": p["state"], "completed_stages": len(p["completed_stages"]), "total_pipeline_stages": 16,
                      "h4": p["h4"], "scientific_values_exposed": False}))


def dry_run() -> None:
    preflight(); syn = configure_synthesis(); specs = syn.unit_specs()
    counts = {k: sum(x["kind"] == k for x in specs) for k in ("support", "summary", "comparison")}
    if len(specs) != 44 or counts != {"support": 2, "summary": 12, "comparison": 30}: raise RuntimeError("44-unit registry mismatch")
    print(json.dumps({"dry_run": "PASS", "synthesis_units": 44, "counts": counts, "units_executed": 0,
                      "excluded_candidate": "V1-R4-63D", "scientific_values_exposed": False}))


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("command", choices=("status", "run", "resume", "validate", "dry-run")); args = parser.parse_args()
    {"status": status, "run": lambda: execute(False), "resume": lambda: execute(True), "validate": validate, "dry-run": dry_run}[args.command]()


if __name__ == "__main__": main()
