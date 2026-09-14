"""Validate the immutable RT3-A relationship-state augmentation without interpretation."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "data/qa_work/v1/phase1/rt3_state_v1"
REL = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/relationships"
MANIFEST = ROOT / "data/manifests/V1_RT3_RELATIONSHIP_STATE_AUGMENTATION.json"
CANDIDATES = [
    "V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W",
    "V1-R1MI-126W", "V1-R3-252M", "V1-R4-63D",
]
PARTS = [f"{year}H{half}" for year in range(2015, 2020) for half in (1, 2)]
INPUT_SHA = "360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"
REL_MANIFEST_SHA = "BF78CDD6B55694FAECF36FF743B3C7206930FC4189A26271B57AEB7712D820D0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def expected_state_schema(candidate: str) -> str:
    if candidate == "V1-R3-252M":
        return "RT3-STATE-R3-1.0"
    if candidate == "V1-R4-63D":
        return "RT3-STATE-R4-1.0"
    return "RT3-STATE-STATIC-1.0"


def build() -> tuple[dict, list[str]]:
    failures: list[str] = []
    entries: list[dict] = []
    for candidate in CANDIDATES:
        summary_path = STATE / ("static_summary.json" if candidate.startswith(("V1-R0", "V1-R1")) else f"{candidate}/summary.json")
        if not summary_path.exists():
            failures.append(f"missing_summary:{candidate}")
            continue
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        if summary.get("schema") != expected_state_schema(candidate):
            failures.append(f"summary_schema:{candidate}")
        by_key = {(p["candidate"], p["partition"]): p for p in summary.get("partitions", [])}
        for part in PARTS:
            state_path = STATE / candidate / f"{part}.npy"
            marker_path = STATE / candidate / f"{part}.complete.json"
            ancestor_path = REL / candidate / f"{part}.npy"
            if not all(path.exists() for path in (state_path, marker_path, ancestor_path)):
                failures.append(f"missing:{candidate}:{part}")
                continue
            marker = json.loads(marker_path.read_text(encoding="utf-8"))
            state_hash = sha256(state_path)
            ancestor_hash = sha256(ancestor_path)
            summary_item = by_key.get((candidate, part))
            if summary_item is None:
                failures.append(f"summary_partition:{candidate}:{part}")
            for source_name, source in (("marker", marker), ("summary", summary_item or {})):
                if source.get("sha256") != state_hash:
                    failures.append(f"{source_name}_state_hash:{candidate}:{part}")
                if source.get("ancestor_sha256") != ancestor_hash:
                    failures.append(f"{source_name}_ancestor_hash:{candidate}:{part}")
                if source.get("equivalence") != "PASS_EXACT" or source.get("shared_field_mismatches") != 0:
                    failures.append(f"{source_name}_equivalence:{candidate}:{part}")
                if source.get("of4_accessed") is not False or source.get("held_out_accessed") is not False:
                    failures.append(f"{source_name}_role_boundary:{candidate}:{part}")
            array = np.load(state_path, mmap_mode="r", allow_pickle=False)
            if int(marker.get("rows", -1)) != len(array):
                failures.append(f"row_count:{candidate}:{part}")
            entries.append({
                "candidate": candidate,
                "partition": part,
                "artifact": state_path.relative_to(ROOT).as_posix(),
                "schema": expected_state_schema(candidate),
                "rows": int(len(array)),
                "sha256": state_hash,
                "ancestor_artifact": ancestor_path.relative_to(ROOT).as_posix(),
                "ancestor_sha256": ancestor_hash,
                "shared_rows_verified": int(marker.get("shared_rows_verified", -1)),
                "shared_field_mismatches": 0,
                "equivalence": "PASS_EXACT",
                "of4_accessed": False,
                "held_out_accessed": False,
            })
    relationship_manifest = ROOT / "data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json"
    if sha256(relationship_manifest) != REL_MANIFEST_SHA:
        failures.append("ancestor_relationship_manifest_hash")
    manifest = {
        "manifest_id": "V1-RT3-RELATIONSHIP-STATE-AUGMENTATION-1.0",
        "status": "IMMUTABLE_QUALIFIED" if not failures else "FAIL",
        "scope": "2015-2019_INNER_ONLY",
        "purpose": "MINIMAL_EVENT_TIME_STATE_FOR_FROZEN_A5_RT3",
        "input_manifest": "V1-PHASE1-INNER-INPUT-1.0",
        "input_sha256": INPUT_SHA,
        "ancestor_relationship_manifest": "V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0",
        "ancestor_relationship_manifest_sha256": REL_MANIFEST_SHA,
        "candidate_count": len(CANDIDATES),
        "partition_count": len(entries),
        "common_output_equivalence": "PASS_EXACT" if not failures else "FAIL",
        "total_shared_field_mismatches": 0 if not failures else None,
        "original_relationship_outputs": "IMMUTABLE_UNCHANGED",
        "empirical_interpretation": "NONE",
        "of4_accessed": False,
        "held_out_accessed": False,
        "partitions": entries,
    }
    return manifest, failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    manifest, failures = build()
    if args.write_manifest:
        if MANIFEST.exists():
            raise SystemExit("no-overwrite: RT3 augmentation manifest already exists")
        if failures:
            raise SystemExit(json.dumps({"result": "FAIL", "failures": failures}))
        MANIFEST.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    else:
        if not MANIFEST.exists():
            failures.append("missing_frozen_manifest")
        elif json.loads(MANIFEST.read_text(encoding="utf-8")) != manifest:
            failures.append("frozen_manifest_mismatch")
    if failures:
        raise SystemExit(json.dumps({"result": "FAIL", "failures": failures}))
    print(json.dumps({
        "manifest_id": manifest["manifest_id"],
        "candidate_count": manifest["candidate_count"],
        "partition_count": manifest["partition_count"],
        "common_output_equivalence": manifest["common_output_equivalence"],
        "result": "PASS",
        "values_disclosed": False,
    }))


if __name__ == "__main__":
    main()
