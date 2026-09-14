#!/usr/bin/env python3
"""Build the non-overwriting V1 C06 publication/availability amendment.

The builder reads only frozen C06 membership structure and immutable first-party
CSRC/CAPCO page captures. It never reads market observations, pair counts, model
outputs, outcomes, OF4, or held-out data. Period labels are identifiers only and
are never converted into availability dates.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CORE_MANIFEST = REPO / "data/manifests/CORE_DATASET_FREEZE_V1.json"
BASE_MEMBERSHIP = REPO / "data/qa_work/g3b_full/c06/20260909T081518Z/primary_membership.jsonl"
RAW_RUN = REPO / "data/raw/g3b_full/c06/20260909T081518Z"
RAW_MANIFEST = RAW_RUN / "manifest.json"
OUT_DIR = REPO / "data/amendments/c06/C06_AVAILABILITY_AMENDMENT_V1"
REGISTER = OUT_DIR / "snapshot_availability_register.jsonl"
ORIGINS = OUT_DIR / "pit_origin_validation.json"
AMENDMENT_MANIFEST = REPO / "data/manifests/C06_AVAILABILITY_AMENDMENT_V1.json"

EXPECTED_CORE_ROOT = "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616"
EXPECTED_BASE_SHA256 = "288C5BBB457439B88E4D23A6E821D864A4F53A4AF401241C642B48EEBBECBBE4"
ARCHIVE_MIGRATION_DATE = "2019-09-04"
INNER_ORIGINS = [f"{year}-{month:02d}-01" for year in range(2015, 2020) for month in (1, 7)]


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def stable_json(value: object, *, indent: int | None = None) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=indent) + "\n"


def write_immutable(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise RuntimeError(f"immutable output differs: {path.relative_to(REPO)}")
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def normalized_title(title: str) -> str:
    return re.sub(r"[\s.。·]", "", title).replace("第", "")


def reference_period(title: str) -> str:
    compact = normalized_title(title)
    quarter = re.search(r"(20\d{2})年([1-4])季度", compact)
    if quarter:
        return f"{quarter.group(1)}Q{quarter.group(2)}"
    half = re.search(r"(20\d{2})年(上|下)半年", compact)
    if half:
        return f"{half.group(1)}H{1 if half.group(2) == '上' else 2}"
    raise RuntimeError(f"unrecognized frozen snapshot title: {title}")


def taxonomy_version(period: str) -> str:
    year = int(period[:4])
    if "Q" in period and (year < 2021 or period <= "2021Q3"):
        return "CSRC_LISTED_COMPANY_INDUSTRY_CLASSIFICATION_2012_REGIME"
    return "CAPCO_2023_GUIDELINE_JR_T_0020_2024_FROZEN_VERSION_LABEL"


def visible_publication_date(page: str) -> tuple[str | None, str | None]:
    decoded = html.unescape(page)
    csrc = re.search(r"日期[：:]\s*(20\d{2}-\d{2}-\d{2})", decoded)
    if csrc:
        return csrc.group(1), "OFFICIAL_CSRC_VISIBLE_PAGE_DATE"
    capco = re.search(r"发布时间[：:]\s*(20\d{2}-\d{2}-\d{2})", decoded)
    if capco:
        return capco.group(1), "OFFICIAL_CAPCO_VISIBLE_PUBLICATION_DATE"
    return None, None


def main() -> int:
    core = json.loads(CORE_MANIFEST.read_text(encoding="utf-8"))
    if core["root_fingerprint"]["value"] != EXPECTED_CORE_ROOT:
        raise RuntimeError("CORE-DATASET-FREEZE-V1 fingerprint mismatch")
    if sha256_file(BASE_MEMBERSHIP) != EXPECTED_BASE_SHA256:
        raise RuntimeError("frozen C06 membership hash mismatch")

    title_rows: dict[str, list[dict]] = defaultdict(list)
    with BASE_MEMBERSHIP.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            title_rows[row["snapshot_title"]].append(row)
    if len(title_rows) != 45:
        raise RuntimeError(f"expected 45 frozen snapshot titles, found {len(title_rows)}")

    raw_manifest = json.loads(RAW_MANIFEST.read_text(encoding="utf-8"))
    evidence_by_title: dict[str, list[dict]] = defaultdict(list)
    for item in raw_manifest["records"]:
        if item.get("kind") != "detail" or item.get("status") != "OK":
            continue
        source_path = RAW_RUN / item["file"]
        if sha256_file(source_path) != item["sha256"]:
            raise RuntimeError(f"raw evidence hash mismatch: {item['file']}")
        page = source_path.read_text(encoding="utf-8", errors="replace")
        date, evidence_type = visible_publication_date(page)
        if date is None:
            continue
        evidence_by_title[normalized_title(item["title"])].append(
            {
                "authoritative_source": "CSRC" if "csrc.gov.cn" in item["url"] else "CAPCO",
                "source_url": item["url"],
                "captured_artifact": str(source_path.relative_to(REPO)).replace("\\", "/"),
                "captured_artifact_sha256": item["sha256"],
                "evidence_type": evidence_type,
                "visible_publication_date": date,
                "archive_or_current_page_date_used_as_availability": False,
            }
        )

    content_hash_by_title: dict[str, str] = {}
    logical_contents: dict[str, set[str]] = defaultdict(set)
    for title, rows in title_rows.items():
        members = sorted(f"{row['security_code']}|{row['industry_code']}" for row in rows)
        digest = sha256_bytes(("\n".join(members) + "\n").encode("utf-8"))
        content_hash_by_title[title] = digest
        logical_contents[reference_period(title)].add(digest)
    conflicting_duplicates = {period: hashes for period, hashes in logical_contents.items() if len(hashes) != 1}
    if conflicting_duplicates:
        raise RuntimeError(f"duplicate-title membership disagreement: {sorted(conflicting_duplicates)}")

    records = []
    unresolved = []
    null_rows_accounted = 0
    archive_rows_corrected = 0
    period_occurrence: dict[str, int] = defaultdict(int)
    for title in sorted(title_rows, key=lambda value: (reference_period(value), value)):
        rows = title_rows[title]
        period = reference_period(title)
        period_occurrence[period] += 1
        evidence = sorted(
            evidence_by_title.get(normalized_title(title), []),
            key=lambda item: (item["visible_publication_date"], item["authoritative_source"], item["source_url"]),
        )
        old_values = sorted({"NULL" if row.get("publication_date") is None else row["publication_date"] for row in rows})
        null_count = sum(row.get("publication_date") is None for row in rows)
        archive_count = sum(row.get("publication_date") == ARCHIVE_MIGRATION_DATE for row in rows)
        null_rows_accounted += null_count
        archive_rows_corrected += archive_count
        corrected = min((item["visible_publication_date"] for item in evidence), default=None)
        qualified = corrected is not None
        title_id = f"C06-{period}-TITLE-{period_occurrence[period]}"
        record = {
            "snapshot_identifier": title_id,
            "logical_snapshot_identifier": f"C06-{period}",
            "snapshot_title": title,
            "reference_period": period,
            "taxonomy_id": "CSRC_CAPCO_LISTED_COMPANY_INDUSTRY_CLASSIFICATION",
            "taxonomy_version": taxonomy_version(period),
            "old_metadata_values": old_values,
            "old_null_publication_rows": null_count,
            "old_archive_migration_date_rows": archive_count,
            "corrected_publication_time": corrected,
            "publication_time_precision": "DATE" if qualified else None,
            "corrected_available_time": (
                {
                    "rule": "FIRST_PROJECT_DECISION_CLOCK_STRICTLY_AFTER_PUBLICATION_DATE",
                    "exclusive_date_lower_bound": corrected,
                    "intraday_time_known": False,
                }
                if qualified
                else None
            ),
            "qualification_state": (
                "QUALIFIED_DATE_PRECISION_CONSERVATIVE_NEXT_DECISION_CLOCK"
                if qualified
                else "C06 AVAILABILITY UNRESOLVED"
            ),
            "amendment_reason": (
                "replace null or archive-migration metadata with independently preserved first-party visible publication date"
                if qualified
                else "no independently verifiable first-party publication/availability evidence found"
            ),
            "authoritative_source_evidence": evidence,
            "base_membership_rows": len(rows),
            "base_membership_normalized_content_sha256": content_hash_by_title[title],
            "duplicate_title_group_size": sum(reference_period(other) == period for other in title_rows),
            "duplicate_membership_content_equivalent": len(logical_contents[period]) == 1,
            "membership_content_amended": False,
            "anti_contamination": "AUTHORIZED_BEFORE_EMPIRICAL_RELATIONSHIP_PAIR_COUNT_RETURN_OUTCOME_OR_PNL_INSPECTION",
        }
        if not qualified:
            unresolved.append(title_id)
        records.append(record)

    if null_rows_accounted != 1125:
        raise RuntimeError(f"expected to account for 1125 null-date rows, found {null_rows_accounted}")

    register_content = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in records)
    write_immutable(REGISTER, register_content)

    qualified_logical: dict[str, dict] = {}
    for row in records:
        if not row["corrected_publication_time"]:
            continue
        period = row["reference_period"]
        candidate = {
            "logical_snapshot_identifier": row["logical_snapshot_identifier"],
            "reference_period": period,
            "publication_date": row["corrected_publication_time"],
            "taxonomy_version": row["taxonomy_version"],
        }
        current = qualified_logical.get(period)
        if current is None or candidate["publication_date"] < current["publication_date"]:
            qualified_logical[period] = candidate

    origin_results = []
    for origin in INNER_ORIGINS:
        usable = [row for row in qualified_logical.values() if row["publication_date"] < origin]
        chosen = max(usable, key=lambda row: row["publication_date"], default=None)
        origin_results.append(
            {
                "origin": origin,
                "constructible": chosen is not None,
                "selection_rule": "latest qualified snapshot whose publication date is strictly before the origin",
                "selected_logical_snapshot_identifier": chosen["logical_snapshot_identifier"] if chosen else None,
                "selected_reference_period": chosen["reference_period"] if chosen else None,
                "selected_publication_date": chosen["publication_date"] if chosen else None,
                "available_time_rule": "FIRST_PROJECT_DECISION_CLOCK_STRICTLY_AFTER_PUBLICATION_DATE",
                "carry_forward": True if chosen else None,
                "classification_age_days": None,
                "classification_age_computation": "DEFERRED_TO_DECISION_DATE_MATERIALIZATION_NO_THRESHOLD",
                "membership_or_pair_count_inspected": False,
            }
        )
    origin_report = {
        "validation_id": "C06-AVAILABILITY-AMENDMENT-V1-PIT-ORIGINS",
        "scope": "C06_METADATA_AND_MEMBERSHIP_STRUCTURE_ONLY",
        "origins": origin_results,
        "all_required_origins_constructible": all(item["constructible"] for item in origin_results),
        "of4_accessed": False,
        "held_out_accessed": False,
        "empirical_values_accessed": False,
    }
    write_immutable(ORIGINS, stable_json(origin_report, indent=2))

    generator_hash = sha256_file(Path(__file__))
    register_hash = sha256_file(REGISTER)
    origins_hash = sha256_file(ORIGINS)
    binding = {
        "amendment_id": "C06-AVAILABILITY-AMENDMENT-V1",
        "ancestor_dataset": "CORE-DATASET-FREEZE-V1",
        "ancestor_root_fingerprint": EXPECTED_CORE_ROOT,
        "base_membership_sha256": EXPECTED_BASE_SHA256,
        "snapshot_register_sha256": register_hash,
        "pit_origin_validation_sha256": origins_hash,
        "generator_sha256": generator_hash,
    }
    amendment_root = sha256_bytes(stable_json(binding).encode("utf-8"))
    amendment_manifest = {
        **binding,
        "amendment_root_fingerprint": amendment_root,
        "status": (
            "QUALIFIED_ALL_REQUIRED_INNER_ORIGINS"
            if origin_report["all_required_origins_constructible"] and not unresolved
            else "C06-FIX-A INTEGRITY BLOCKER"
        ),
        "scope": "PUBLICATION_AND_AVAILABLE_TIME_METADATA_ONLY",
        "frozen_base_membership_unchanged": True,
        "snapshot_titles_accounted": len(records),
        "logical_snapshots_accounted": len(qualified_logical),
        "old_null_publication_rows_accounted": null_rows_accounted,
        "old_archive_migration_date_rows_corrected": archive_rows_corrected,
        "old_archive_migration_date_retained_as_availability": 0,
        "unresolved_snapshot_identifiers": unresolved,
        "required_inner_origins": len(INNER_ORIGINS),
        "constructible_inner_origins": sum(item["constructible"] for item in origin_results),
        "source_standard": "IMMUTABLE_FIRST_PARTY_CSRC_CAPCO_VISIBLE_PAGE_PUBLICATION_RECORDS",
        "time_precision_rule": "date-only evidence becomes usable at the first project decision clock strictly after the date",
        "prohibitions": [
            "no period-label or period-end backdating",
            "no archive/current-page modification date used as publication time",
            "no inferred neighboring dates",
            "no membership, taxonomy, identity, scope, PAIR-A, or scientific-semantic change",
            "no empirical, OF4, or held-out access",
        ],
        "artifacts": {
            "snapshot_register": str(REGISTER.relative_to(REPO)).replace("\\", "/"),
            "pit_origin_validation": str(ORIGINS.relative_to(REPO)).replace("\\", "/"),
            "generator": str(Path(__file__).relative_to(REPO)).replace("\\", "/"),
        },
    }
    write_immutable(AMENDMENT_MANIFEST, stable_json(amendment_manifest, indent=2))

    print(
        json.dumps(
            {
                "amendment_id": amendment_manifest["amendment_id"],
                "status": amendment_manifest["status"],
                "snapshot_titles": len(records),
                "logical_snapshots": len(qualified_logical),
                "null_rows_accounted": null_rows_accounted,
                "unresolved_snapshots": len(unresolved),
                "constructible_inner_origins": amendment_manifest["constructible_inner_origins"],
                "amendment_root_fingerprint": amendment_root,
            },
            ensure_ascii=False,
        )
    )
    return 0 if amendment_manifest["status"] == "QUALIFIED_ALL_REQUIRED_INNER_ORIGINS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
