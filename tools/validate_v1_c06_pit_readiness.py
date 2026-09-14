#!/usr/bin/env python3
"""Audit the frozen C06 artifact's availability-time readiness for V1 inner origins.

This validator is structural only. It never reads market observations or outcomes and
never repairs, infers, or backfills a publication date.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CORE = REPO / "data/manifests/CORE_DATASET_FREEZE_V1.json"
C06 = REPO / "data/qa_work/g3b_full/c06/20260909T081518Z/primary_membership.jsonl"
OUTPUT = REPO / "data/manifests/V1_C06_PIT_READINESS_BLOCKER.json"
EXPECTED_C06_SHA256 = "288C5BBB457439B88E4D23A6E821D864A4F53A4AF401241C642B48EEBBECBBE4"
EXPECTED_ROOT = "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def labelled_period(title: str) -> tuple[int, int] | None:
    match = re.search(r"(20\d{2}).*?([1-4]).*?(?:季度|����)", title)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def main() -> int:
    core = json.loads(CORE.read_text(encoding="utf-8"))
    actual_hash = sha256(C06)
    if core["root_fingerprint"]["value"] != EXPECTED_ROOT:
        raise SystemExit("Frozen core fingerprint mismatch")
    if actual_hash != EXPECTED_C06_SHA256:
        raise SystemExit("Frozen C06 artifact hash mismatch")

    snapshots: dict[str, dict[str, object]] = defaultdict(
        lambda: {"publication_dates": set(), "rows": 0, "period": None}
    )
    total_rows = 0
    null_publication_rows = 0
    with C06.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            total_rows += 1
            title = row["snapshot_title"]
            publication = row.get("publication_date")
            if publication is None:
                null_publication_rows += 1
            snapshots[title]["publication_dates"].add(publication)
            snapshots[title]["rows"] += 1
            snapshots[title]["period"] = labelled_period(title)

    through_2019q2 = []
    for title, state in snapshots.items():
        period = state["period"]
        if period and period <= (2019, 2):
            through_2019q2.append(
                {
                    "snapshot_title": title,
                    "labelled_period": f"{period[0]}Q{period[1]}",
                    "publication_dates": sorted(
                        "NULL" if value is None else value
                        for value in state["publication_dates"]
                    ),
                    "rows": state["rows"],
                }
            )
    through_2019q2.sort(key=lambda item: (item["labelled_period"], item["snapshot_title"]))

    dated_publications = sorted(
        {
            value
            for state in snapshots.values()
            for value in state["publication_dates"]
            if value is not None
        }
    )
    inner_calendar_boundaries = [
        f"{year}-{month:02d}-01" for year in range(2015, 2020) for month in (1, 7)
    ]
    usable_at_origin = {
        origin: [date for date in dated_publications if date < origin]
        for origin in inner_calendar_boundaries
    }

    report = {
        "audit_id": "V1-C06-PIT-READINESS-BLOCKER-1.0",
        "status": "FAIL_MATERIAL_C06_AVAILABILITY_TIME_CONTRACT_MISMATCH",
        "scope": "STRUCTURAL_ONLY_NO_MARKET_OR_OUTCOME_ACCESS",
        "ancestry": {
            "dataset": "CORE-DATASET-FREEZE-V1",
            "root_fingerprint": EXPECTED_ROOT,
            "c06_artifact": str(C06.relative_to(REPO)).replace("\\", "/"),
            "c06_sha256": actual_hash,
        },
        "frozen_contract_expectation": {
            "earliest_qualified_boundary": "2013-01-07",
            "rule": "use each historical snapshot only from its true publication/available time",
            "prohibition": "period labels and current/archive-page dates may not backfill publication time",
        },
        "observed_artifact": {
            "rows": total_rows,
            "snapshot_titles": len(snapshots),
            "null_publication_rows": null_publication_rows,
            "dated_publications_min": dated_publications[0] if dated_publications else None,
            "snapshots_2012q4_through_2019q2": len(through_2019q2),
            "historical_snapshot_publication_records": through_2019q2,
        },
        "inner_origin_check": [
            {
                "calendar_boundary": origin,
                "any_captured_snapshot_available_strictly_before_origin": bool(usable_at_origin[origin]),
                "latest_captured_publication_before_origin": (
                    usable_at_origin[origin][-1] if usable_at_origin[origin] else None
                ),
            }
            for origin in inner_calendar_boundaries
        ],
        "finding": (
            "The frozen C06 normalized artifact does not preserve true historical "
            "publication/available dates for the pre-2019 snapshot sequence. Under its "
            "own captured dates, none of the 2015-2019 semiannual inner boundaries has "
            "an available C06 snapshot. PAIR-A therefore cannot be constructed without "
            "an explicit versioned C06 availability-time correction/amendment."
        ),
        "non_actions": [
            "no publication date inferred from period label",
            "no archive-page date treated as original availability",
            "no current membership backfill",
            "no pair counts or market values computed",
            "no frozen artifact mutated",
        ],
    }
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text(encoding="utf-8") != serialized:
            raise SystemExit("Existing immutable C06 blocker report differs from deterministic regeneration")
    else:
        OUTPUT.write_text(serialized, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "audit_id": report["audit_id"],
                "status": report["status"],
                "rows": total_rows,
                "snapshot_titles": len(snapshots),
                "null_publication_rows": null_publication_rows,
                "inner_boundaries_without_available_snapshot": sum(
                    not item["any_captured_snapshot_available_strictly_before_origin"]
                    for item in report["inner_origin_check"]
                ),
            },
            ensure_ascii=False,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
