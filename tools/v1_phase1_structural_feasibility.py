"""Structural feasibility audit for frozen PAIR-A Phase 1.

Reads only C06 membership/availability, the structural eligibility sidecar, and the
official C04 exclusion calendar. It never reads a price, return, model output,
target, outcome, OF4 record, or held-out record.
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
C06 = ROOT / "data/qa_work/g3b_full/c06/20260909T081518Z/primary_membership.jsonl"
C06_REGISTER = ROOT / "data/amendments/c06/C06_AVAILABILITY_AMENDMENT_V1/snapshot_availability_register.jsonl"
SIDECAR = ROOT / "data/qa_work/g3b_f2/security_date_eligibility/v1/security_date_eligibility_sidecar_v1.csv.gz"
C04 = ROOT / "data/qa_work/v1/c04_a/official_calendar_v1/v1_exclusion_calendar.jsonl"
OUT = ROOT / "data/qa_work/v1/phase1/structural_feasibility_v1.json"


def iso(raw: str) -> str:
    raw = raw.replace("-", "")
    return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"


def ticker(code: str) -> str | None:
    if code.startswith("6"):
        return f"{code}.SH"
    if code.startswith(("0", "3")):
        return f"{code}.SZ"
    return None


def choose_snapshots() -> list[tuple[str, str, dict[str, str]]]:
    register = [json.loads(x) for x in C06_REGISTER.read_text(encoding="utf-8").splitlines() if x]
    by_title = {x["snapshot_title"]: x for x in register}
    membership: dict[str, dict[str, str]] = defaultdict(dict)
    for line in C06.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        code = ticker(str(row["security_code"]))
        industry = str(row["industry_code"])
        if code and industry in {"34", "35"}:
            membership[row["snapshot_title"]][code] = industry

    logical: dict[str, tuple[str, str, dict[str, str]]] = {}
    for title, members in membership.items():
        meta = by_title[title]
        if meta["qualification_state"] != "QUALIFIED_DATE_PRECISION_CONSERVATIVE_NEXT_DECISION_CLOCK":
            continue
        logical_id = meta["logical_snapshot_identifier"]
        candidate = (meta["corrected_publication_time"], title, members)
        if logical_id not in logical or title < logical[logical_id][1]:
            logical[logical_id] = candidate
    return sorted(logical.values())


def main() -> None:
    snapshots = choose_snapshots()
    normal_by_date: dict[str, set[str]] = defaultdict(set)
    with gzip.open(SIDECAR, "rt", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            day = iso(row["observation_date"])
            if day > "2019-12-31":
                continue
            if row["c05_structural_state"] == "NORMAL TRADING OBSERVED":
                normal_by_date[day].add(row["historical_ticker_code"])

    excluded = set()
    for line in C04.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        day = row["effective_ex_date"]
        if "2013-01-07" <= day <= "2019-12-31":
            excluded.add((row["historical_ticker"], day))

    dates = sorted(d for d in normal_by_date if "2013-01-07" <= d <= "2019-12-31")
    codes = sorted({c for values in normal_by_date.values() for c in values})
    ix = {code: pos for pos, code in enumerate(codes)}
    cumulative = np.zeros((len(codes), len(codes)), dtype=np.uint16)
    prior_normal: set[str] = set()
    rows = []
    yearly = defaultdict(lambda: {"sessions": 0, "candidate_pair_dates": 0, "h63_pair_dates": 0,
                                  "h126_pair_dates": 0, "h252_pair_dates": 0})
    origin_dates = {f"{year}-{month}-01" for year in range(2015, 2020) for month in ("01", "07")}
    origin_report = []

    snap_pos = -1
    current_members: dict[str, str] = {}
    for day in dates:
        while snap_pos + 1 < len(snapshots) and snapshots[snap_pos + 1][0] < day:
            snap_pos += 1
            current_members = snapshots[snap_pos][2]
        current = normal_by_date[day]
        response_eligible = {
            code for code in current_members
            if code in current and code in prior_normal and (code, day) not in excluded
        }
        positions = np.fromiter((ix[c] for c in response_eligible if c in ix), dtype=np.int64)
        n = len(positions)
        candidate_pairs = n * (n - 1) // 2
        if n:
            block = cumulative[np.ix_(positions, positions)]
            counts = {
                h: int(np.count_nonzero(np.triu(block >= h, 1)))
                for h in (63, 126, 252)
            }
            cumulative[np.ix_(positions, positions)] += 1
        else:
            counts = {63: 0, 126: 0, 252: 0}
        if day >= "2015-01-01":
            yr = day[:4]
            yearly[yr]["sessions"] += 1
            yearly[yr]["candidate_pair_dates"] += candidate_pairs
            for h in (63, 126, 252):
                yearly[yr][f"h{h}_pair_dates"] += counts[h]
            rows.append((day, n, candidate_pairs, counts[63], counts[126], counts[252]))
        if any(day >= origin and (not origin_report or origin_report[-1].get("requested_origin") != origin)
               for origin in sorted(origin_dates)):
            for origin in sorted(origin_dates):
                if day >= origin and not any(x["requested_origin"] == origin for x in origin_report):
                    origin_report.append({"requested_origin": origin, "first_exchange_session": day,
                                          "response_eligible_securities": n,
                                          "candidate_unordered_pairs": candidate_pairs})
        prior_normal = current

    totals = {key: sum(y[key] for y in yearly.values()) for key in next(iter(yearly.values()))}
    report = {
        "audit_id": "V1-PAIR-A-STRUCTURAL-FEASIBILITY-1.0",
        "scope": "C06/sidecar/C04 structural states only; no prices, returns, fits, outcomes, OF4, or held-out",
        "date_role": "2013-2014 formation reserve; 2015-2019 inner only",
        "universe_rule": "PAIR-A complete contemporaneous PIT all-pairs; no screening",
        "years": dict(yearly),
        "inner_totals": totals,
        "semiannual_origins": origin_report,
        "r4_required_pair_direction_daily_ml_fits": 2 * totals["h63_pair_dates"],
        "r4_minimum_kalman_state_steps_per_likelihood_sweep": 2 * totals["h63_pair_dates"] * 63,
        "r3_monthly_pair_direction_membership_fits_upper_geometry": 2 * sum(r[4] for r in rows if date.fromisoformat(r[0]).day <= 7),
        "interpretation": "Counts are structural computational geometry, not model performance or pair validity.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    OUT.write_text(payload, encoding="utf-8")
    print(json.dumps({"output": OUT.relative_to(ROOT).as_posix(),
                      "sha256": hashlib.sha256(OUT.read_bytes()).hexdigest().upper(),
                      "inner_sessions": totals["sessions"],
                      "candidate_pair_dates": totals["candidate_pair_dates"],
                      "r4_daily_ml_fits": report["r4_required_pair_direction_daily_ml_fits"]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
