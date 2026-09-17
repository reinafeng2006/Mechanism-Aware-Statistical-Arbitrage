"""Researcher-operated checkpointed V1 final held-out pipeline.

Status and progress contain integrity/runtime metadata only. The write-once access
event is atomically finalized before the first held-out byte is read.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EXT = Path(r"D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1")
CONTROL = EXT / "_control"
ACCESS = CONTROL / "heldout_access_event.json"
PROGRESS = CONTROL / "progress.json"
LOG_ROOT = EXT / "logs"
INPUT = EXT / "input/of4_input_v1.npz"
REL = EXT / "relationships"
LAYER = EXT / "a1_h126"
LAYER_MANIFEST = EXT / "_metadata/V1_FINAL_HELDOUT_A1_H126.json"
SYNTH_ROOT = EXT / "synthesis_checkpoint_v1"
SYNTH_UNITS = SYNTH_ROOT / "units"
FINAL = EXT / "_metadata/V1_FINAL_HELDOUT_A1_SYNTHESIS.json"
DECISION = ROOT / "docs/decisions/V1_FINAL_HELDOUT_CONFIRMATORY_FREEZE.md"
MATERIALIZER = ROOT / "tools/v1_of4_materialize.py"
CANDIDATES = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W", "V1-R3-252M", "V1-R4-63D"]
FOLDS = ["2024", "2025"]
FIELDS = ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba")
VERSION = "V1-FINAL-HELDOUT-CHECKPOINT-1.0"
CORE_FINGERPRINT = "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616"
ACCEPTED_COMMIT = "27be564a5fd24b5e10ba63e114cff3553f478d5a"


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
    os.replace(temp, path)


def access_event() -> dict:
    expected = {"access_id": "V1-FINAL-HELDOUT-ACCESS-1.0", "decision_id": "V1-FINAL-HELDOUT-CONFIRMATORY-1.0",
                "accepted_preheldout_commit": ACCEPTED_COMMIT, "core_fingerprint": CORE_FINGERPRINT,
                "runner_version": VERSION, "decision_sha256": sha(DECISION), "held_out_accessed": True,
                "irreversible": True, "region": "2024-01-01/2025-12-31"}
    if ACCESS.exists():
        current = json.loads(ACCESS.read_text(encoding="utf-8"))
        for key, value in expected.items():
            if current.get(key) != value:
                raise RuntimeError(f"existing held-out access event binding mismatch: {key}")
        return current
    CONTROL.mkdir(parents=True, exist_ok=True)
    event = dict(expected, opened_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                 process_id=os.getpid(), host=socket.gethostname())
    temp = ACCESS.with_name(ACCESS.name + f".{os.getpid()}.tmp")
    with temp.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(event, sort_keys=True, indent=2) + "\n")
        stream.flush(); os.fsync(stream.fileno())
    try:
        os.link(temp, ACCESS)
    except FileExistsError:
        temp.unlink()
        return access_event()
    temp.unlink()
    return event


def progress(load_only: bool = False) -> dict:
    if PROGRESS.exists():
        return json.loads(PROGRESS.read_text(encoding="utf-8"))
    obj = {"progress_id": VERSION, "state": "READY", "completed_stages": [], "held_out_accessed": False,
           "scientific_values_exposed": False, "stage_hashes": {}, "started_at": None, "updated_at": None}
    if not load_only:
        atomic_json(PROGRESS, obj)
    return obj


def save_progress(p: dict) -> None:
    p["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    atomic_json(PROGRESS, p)


def run_materializer(stage: str, candidate: str | None = None) -> None:
    env = os.environ.copy(); env["V1_MATERIALIZATION_ROLE"] = "FINAL_HELDOUT"
    cmd = [sys.executable, str(MATERIALIZER), stage]
    if candidate: cmd += ["--candidate", candidate]
    subprocess.run(cmd, cwd=ROOT, env=env, check=True)


def layer_partition(fold: str) -> dict:
    import v1_a1_h126_candidate_neutral as layer
    layer.EXT = LAYER; layer.OF4_REL = REL
    with np.load(INPUT, allow_pickle=False) as source:
        records = layer.build_partition("heldout", fold, source["response"])
    return {"fold": fold, "records": records}


def verify_records(records: list[dict]) -> None:
    for record in records:
        path = Path(record["physical_path"])
        if not path.is_file() or sha(path) != record["sha256"]:
            raise RuntimeError(f"completed payload hash mismatch: {path}")


def verify_finalized_relationship_stage() -> None:
    manifest_path = EXT / "_metadata/final_relationship_stage.json"
    if not manifest_path.is_file(): raise RuntimeError("completed relationship-stage manifest missing")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["manifest_id"] != "V1-FINAL-HELDOUT-RELATIONSHIP-STAGE-1.0" or len(manifest["payloads"]) != 56:
        raise RuntimeError("completed relationship-stage manifest structure mismatch")
    for record in manifest["payloads"]:
        path = EXT / record["physical_relative_path"]
        if not path.is_file() or sha(path) != record["sha256"]:
            raise RuntimeError(f"completed relationship-stage hash mismatch: {path}")


def finalize_layer(records: list[dict]) -> None:
    atomic_json(LAYER_MANIFEST, {"manifest_id": "V1-FINAL-HELDOUT-A1-H126-CN-SCALE-LOSS-1.0",
        "status": "IMMUTABLE_COMPLETE_CHECKSUMMED", "decision": "V1-A1-H126-CN-1.0",
        "confirmatory_decision": "V1-FINAL-HELDOUT-CONFIRMATORY-1.0", "physical_root": str(LAYER),
        "scale_source_candidate": "V1-R0C-126W", "ps0": "1.4826_MAD_H126_QUALIFIED_PIT",
        "ps1": "SAMPLE_SD_DDOF1_SAME_H126_GEOMETRY", "pit": "STRICTLY_BEFORE_EVALUATED_EVENT",
        "records": records, "relationship_recomputation": False, "held_out_accessed": True,
        "values_disclosed_during_construction": False})


def configure_synthesis():
    import v1_a1_h126_synthesis_batch as syn
    syn.LAYER_ROOT = LAYER; syn.WORK_ROOT = SYNTH_ROOT; syn.UNITS_ROOT = SYNTH_UNITS
    syn.PROGRESS = SYNTH_ROOT / "progress.json"; syn.FINAL = FINAL; syn.LAYER_MANIFEST = LAYER_MANIFEST
    syn.FOLDS = [("heldout", fold) for fold in FOLDS]
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
                "temporal_median_of_fold_equal_pair_median_differences": float(np.median([x["metrics"][field]["right_minus_left_equal_pair_median"] for x in items])),
                "fold_count": len(items)} for field in FIELDS}
    out = {"synthesis_id": "V1-FINAL-HELDOUT-A1-H126-SYNTHESIS-1.0", "scale_version": "V1-A1-H126-CN-SCALE-LOSS-1.0",
           "status": "FINAL_HELDOUT_EVIDENCE_AVAILABLE_FOR_VALIDATION", "results": summaries,
           "pairwise_common_support": comparisons, "temporal_median_vector": temporal,
           "confirmatory_bindings": {"C1": ["V1-R0L-126W", "V1-R1M-126W"], "C2": ["V1-R1M-126W", "V1-R1MI-126W"],
                                    "C3": ["V1-R0D-252M", "V1-R3-252M"], "C4": ["V1-R0L-126W", "V1-R4-63D"]},
           "uncertainty": "NOT_ESTIMATED_EXACT_COMPARATIVE_UNCERTAINTY_METHOD_UNFROZEN",
           "multiplicity": "NO_NUMERICAL_CORRECTION_EXACT_METHOD_AND_LEVEL_UNFROZEN",
           "severe_failure": "NOT_ACTIVATED_UNDERLYING_NUMERICAL_EVENT_UNFROZEN", "ranking": "NOT_FORCED",
           "a6_g5": "V1_NON_ESTIMABLE_NOT_EXECUTED", "held_out": "2024_2025_ACCESSED_AUTHORIZED"}
    atomic_json(FINAL, out); p["state"] = "COMPLETE"; p["final_sha256"] = sha(FINAL); syn.write_json_atomic(syn.PROGRESS, p)


def run_synthesis() -> None:
    syn = configure_synthesis(); p = syn.initialize(); syn.verify_completed(p)
    p["state"] = "RUNNING"; syn.write_json_atomic(syn.PROGRESS, p)
    for spec in syn.unit_specs():
        uid, dest = spec["id"], syn.unit_path(spec)
        if uid in p["units"]: continue
        started = time.perf_counter()
        if spec["kind"] == "support": syn.support_unit(spec, dest)
        elif spec["kind"] == "summary": syn.summary_unit(spec, dest)
        else: syn.comparison_unit(spec, dest)
        p["units"][uid] = {"kind": spec["kind"], "path": str(dest), "sha256": sha(dest),
                           "bytes": dest.stat().st_size, "runtime_seconds": time.perf_counter() - started}
        p["completed"] = len(p["units"]); syn.write_json_atomic(syn.PROGRESS, p)
    finalize_synthesis(syn, p)


def execute(resume: bool) -> None:
    p = progress()
    if not resume and p["completed_stages"]:
        raise RuntimeError("completed held-out checkpoints exist; use resume")
    event = access_event(); p["held_out_accessed"] = True
    if p["started_at"] is None: p["started_at"] = event["opened_at"]
    p["state"] = "RUNNING"; save_progress(p)
    stages = [("prepare", lambda: run_materializer("prepare"))]
    stages += [(f"relationships:{candidate}", lambda c=candidate: run_materializer("relationships", c)) for candidate in CANDIDATES]
    stages += [("state", lambda: run_materializer("state")), ("a3a5", lambda: run_materializer("a3a5")),
               ("compress", lambda: run_materializer("compress"))]
    layer_records = []
    compressed = "compress" in p["completed_stages"]
    if compressed:
        verify_finalized_relationship_stage()
    for name, fn in stages:
        if name in p["completed_stages"]:
            if not compressed: fn()  # underlying atomic markers rehash and skip valid payloads
            continue
        fn(); p["completed_stages"].append(name); save_progress(p)
    for fold in FOLDS:
        name = f"h126:{fold}"
        if name not in p["completed_stages"]:
            result = layer_partition(fold); atomic_json(CONTROL / f"{name.replace(':','_')}.json", result)
            p["completed_stages"].append(name); save_progress(p)
        records = json.loads((CONTROL / f"h126_{fold}.json").read_text(encoding="utf-8"))["records"]
        verify_records(records); layer_records.extend(records)
    finalize_layer(layer_records)
    if "synthesis" not in p["completed_stages"]:
        run_synthesis(); p["completed_stages"].append("synthesis")
    p["state"] = "COMPLETE"; p["final_sha256"] = sha(FINAL); save_progress(p)


def validate() -> None:
    p = progress(load_only=True)
    if not PROGRESS.exists(): raise RuntimeError("held-out progress does not exist")
    if ACCESS.exists() and not json.loads(ACCESS.read_text(encoding="utf-8"))["held_out_accessed"]: raise RuntimeError("invalid access event")
    if p["state"] == "COMPLETE":
        if not FINAL.exists() or sha(FINAL) != p["final_sha256"]: raise RuntimeError("final held-out synthesis hash mismatch")
        syn = configure_synthesis(); sp = json.loads(syn.PROGRESS.read_text(encoding="utf-8")); syn.verify_completed(sp)
        if sp["completed"] != 58: raise RuntimeError("held-out synthesis is not 58/58")
    print(json.dumps({"result": "PASS", "state": p["state"], "completed_stages": len(p["completed_stages"]),
                      "held_out_accessed": p["held_out_accessed"], "scientific_values_exposed": False}))


def status() -> None:
    p = progress(load_only=True)
    print(json.dumps({"state": p["state"], "completed_stages": len(p["completed_stages"]),
                      "held_out_accessed": ACCESS.exists(), "scientific_values_exposed": False}))


def dry_run() -> None:
    if not DECISION.is_file() or not MATERIALIZER.is_file(): raise RuntimeError("runner dependency missing")
    syn = configure_synthesis(); specs = syn.unit_specs()
    if len(specs) != 58 or sum(x["kind"] == "support" for x in specs) != 2 or sum(x["kind"] == "summary" for x in specs) != 14 or sum(x["kind"] == "comparison" for x in specs) != 42:
        raise RuntimeError("held-out synthesis unit registry mismatch")
    print(json.dumps({"dry_run": "PASS", "synthesis_units": 58, "units_executed": 0,
                      "access_event_created": False, "scientific_values_exposed": False}))


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("command", choices=("status", "run", "resume", "validate", "dry-run")); args = parser.parse_args()
    {"status": status, "run": lambda: execute(False), "resume": lambda: execute(True), "validate": validate, "dry-run": dry_run}[args.command]()


if __name__ == "__main__": main()
