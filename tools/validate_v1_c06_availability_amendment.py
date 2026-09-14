#!/usr/bin/env python3
"""Read-only validation for C06-AVAILABILITY-AMENDMENT-V1."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "data/manifests/C06_AVAILABILITY_AMENDMENT_V1.json"
CORE = REPO / "data/manifests/CORE_DATASET_FREEZE_V1.json"
BASE = REPO / "data/qa_work/g3b_full/c06/20260909T081518Z/primary_membership.jsonl"
EXPECTED_CORE_ROOT = "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616"
EXPECTED_BASE_HASH = "288C5BBB457439B88E4D23A6E821D864A4F53A4AF401241C642B48EEBBECBBE4"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def stable_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    failures: list[str] = []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    core = json.loads(CORE.read_text(encoding="utf-8"))
    register_path = REPO / manifest["artifacts"]["snapshot_register"]
    origins_path = REPO / manifest["artifacts"]["pit_origin_validation"]
    generator_path = REPO / manifest["artifacts"]["generator"]

    if core["root_fingerprint"]["value"] != EXPECTED_CORE_ROOT:
        failures.append("core fingerprint changed")
    if sha256_file(BASE) != EXPECTED_BASE_HASH:
        failures.append("base membership changed")
    expected_hashes = {
        "snapshot_register_sha256": sha256_file(register_path),
        "pit_origin_validation_sha256": sha256_file(origins_path),
        "generator_sha256": sha256_file(generator_path),
    }
    for field, actual in expected_hashes.items():
        if manifest[field] != actual:
            failures.append(f"{field} mismatch")

    binding = {
        "amendment_id": manifest["amendment_id"],
        "ancestor_dataset": manifest["ancestor_dataset"],
        "ancestor_root_fingerprint": manifest["ancestor_root_fingerprint"],
        "base_membership_sha256": manifest["base_membership_sha256"],
        **expected_hashes,
    }
    root = hashlib.sha256(stable_json(binding).encode("utf-8")).hexdigest().upper()
    if manifest["amendment_root_fingerprint"] != root:
        failures.append("amendment root fingerprint mismatch")

    records = [json.loads(line) for line in register_path.read_text(encoding="utf-8").splitlines()]
    if len(records) != 45:
        failures.append("snapshot-title count is not 45")
    if len({row["logical_snapshot_identifier"] for row in records}) != 42:
        failures.append("logical-snapshot count is not 42")
    if sum(row["old_null_publication_rows"] for row in records) != 1125:
        failures.append("1125 null-date rows are not fully accounted")
    if any(row["qualification_state"] == "C06 AVAILABILITY UNRESOLVED" for row in records):
        failures.append("unresolved snapshot remains")
    if any(row["membership_content_amended"] for row in records):
        failures.append("membership content was marked amended")
    if any(not row["duplicate_membership_content_equivalent"] for row in records):
        failures.append("duplicate-title membership mismatch")
    if any(not row["authoritative_source_evidence"] for row in records):
        failures.append("snapshot lacks authoritative evidence")
    if any(
        row["corrected_available_time"]["rule"]
        != "FIRST_PROJECT_DECISION_CLOCK_STRICTLY_AFTER_PUBLICATION_DATE"
        for row in records
    ):
        failures.append("availability-time rule mismatch")
    if any(
        item["archive_or_current_page_date_used_as_availability"]
        for row in records
        for item in row["authoritative_source_evidence"]
    ):
        failures.append("archive/current-page date treated as availability")
    for row in records:
        for evidence in row["authoritative_source_evidence"]:
            path = REPO / evidence["captured_artifact"]
            if sha256_file(path) != evidence["captured_artifact_sha256"]:
                failures.append(f"source evidence hash mismatch: {path.name}")

    duplicate_sizes = Counter(row["reference_period"] for row in records)
    if sorted(period for period, count in duplicate_sizes.items() if count > 1) != ["2015Q4", "2020Q4", "2021Q3"]:
        failures.append("unexpected duplicate-title groups")

    origins = json.loads(origins_path.read_text(encoding="utf-8"))
    if len(origins["origins"]) != 10 or not origins["all_required_origins_constructible"]:
        failures.append("not all ten inner origins are constructible")
    if any(not row["constructible"] for row in origins["origins"]):
        failures.append("blocked inner origin remains")
    if any(row["membership_or_pair_count_inspected"] for row in origins["origins"]):
        failures.append("pair count inspection recorded")
    if origins["of4_accessed"] or origins["held_out_accessed"] or origins["empirical_values_accessed"]:
        failures.append("prohibited data access recorded")

    manifest_checks = {
        "status": manifest["status"] == "QUALIFIED_ALL_REQUIRED_INNER_ORIGINS",
        "titles": manifest["snapshot_titles_accounted"] == 45,
        "null_rows": manifest["old_null_publication_rows_accounted"] == 1125,
        "archive_date_not_retained": manifest["old_archive_migration_date_retained_as_availability"] == 0,
        "origins": manifest["constructible_inner_origins"] == 10,
        "base_unchanged": manifest["frozen_base_membership_unchanged"] is True,
    }
    failures.extend(f"manifest invariant failed: {key}" for key, value in manifest_checks.items() if not value)

    result = {
        "amendment_id": manifest["amendment_id"],
        "amendment_root_fingerprint": root,
        "snapshot_titles": len(records),
        "logical_snapshots": len({row["logical_snapshot_identifier"] for row in records}),
        "null_rows_accounted": sum(row["old_null_publication_rows"] for row in records),
        "constructible_inner_origins": sum(row["constructible"] for row in origins["origins"]),
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
