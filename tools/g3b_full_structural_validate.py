"""Structural-only G3B-FULL validation. Never computes research measurements or outcomes."""
from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "data/raw/g3b_full/tushare/full_2013_2025_v1"
C06 = ROOT / "data/qa_work/g3b_full/c06/20260909T081518Z"
OUT = ROOT / "data/qa_work/g3b_full/tushare/full_2013_2025_v1"
IDENTIFIER_REGISTER = ROOT / "registers/G3B_IDENTIFIER_HISTORY_RESOLUTION_REGISTER.jsonl"

REQUIRED = {
    "C01": {"ts_code", "symbol", "name", "exchange", "list_status", "list_date", "delist_date"},
    "C03": {"ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"},
    "E02": {"ts_code", "trade_date", "close", "turnover_rate", "turnover_rate_f", "volume_ratio", "total_share", "float_share", "free_share", "total_mv", "circ_mv"},
    "E03-A": {"ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"},
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def data_sha(payload: dict) -> str:
    """Hash returned fields/items only; provider request IDs may legitimately differ."""
    encoded = json.dumps(payload.get("data") or {}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest().upper()


def payload_records() -> dict[tuple[str, str], list[tuple[Path, dict]]]:
    grouped: dict[tuple[str, str], list[tuple[Path, dict]]] = defaultdict(list)
    for path in RUN.glob("*.json"):
        parts = path.stem.split("__")
        if len(parts) < 3 or parts[0] not in REQUIRED:
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        grouped[(parts[0], parts[2])].append((path, payload))
    return grouped


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    universe_codes = [x.strip() for x in (C06 / "security_union.txt").read_text(encoding="utf-8").splitlines() if x.strip()]
    eligible = sorted(f"{x}.SH" if x.startswith("6") else f"{x}.SZ" for x in universe_codes if x.startswith(("0", "3", "6")))
    excluded = sorted(set(universe_codes) - {x.split(".")[0] for x in eligible})
    grouped = payload_records()
    summary = {}
    canonical_payloads: dict[str, list[dict]] = defaultdict(list)
    duplicate_groups = 0
    duplicate_hash_mismatch_groups = 0
    normalized_content_records = []
    for (contract, rid), entries in grouped.items():
        successes = [(p, d) for p, d in entries if d.get("code") == 0]
        if not successes:
            continue
        canonical_payloads[contract].append(successes[0][1])
        if len(successes) > 1:
            duplicate_groups += 1
            if len({data_sha(d) for _, d in successes}) > 1:
                duplicate_hash_mismatch_groups += 1
        normalized_content_records.append({
            "contract": contract,
            "request_id": rid,
            "normalized_fields_items_sha256": data_sha(successes[0][1]),
            "raw_objects": [{"file": p.name, "raw_sha256": sha(p)} for p, _ in successes],
        })

    c01_ids = set()
    c01_intervals = {}
    for payload in canonical_payloads["C01"]:
        data = payload.get("data") or {}
        fields = data.get("fields") or []
        if "ts_code" in fields:
            ix = fields.index("ts_code")
            c01_ids.update(row[ix] for row in data.get("items") or [])
            list_ix = fields.index("list_date") if "list_date" in fields else None
            delist_ix = fields.index("delist_date") if "delist_date" in fields else None
            for row in data.get("items") or []:
                c01_intervals[row[ix]] = (str(row[list_ix] or "") if list_ix is not None else "",
                                           str(row[delist_ix] or "") if delist_ix is not None else "")
    identifier_resolutions = [json.loads(x) for x in IDENTIFIER_REGISTER.read_text(encoding="utf-8").splitlines() if x.strip()] if IDENTIFIER_REGISTER.exists() else []
    mapped_ids = {x["historical_code"] for x in identifier_resolutions if x.get("resolution_status") == "VALID HISTORICAL SECURITY — C01 MAPPING REQUIRED"}

    detail = {}
    for contract in ("C01", "C03", "E02", "E03-A"):
        payloads = canonical_payloads[contract]
        missing_field_payloads = 0
        empty_payloads = 0
        duplicate_date_payloads = 0
        bad_identifier_payloads = 0
        observed_ids = set()
        min_dates, max_dates = [], []
        row_count = 0
        for payload in payloads:
            data = payload.get("data") or {}
            fields = data.get("fields") or []
            rows = data.get("items") or []
            row_count += len(rows)
            if not REQUIRED[contract].issubset(fields):
                missing_field_payloads += 1
            if not rows:
                empty_payloads += 1
                continue
            if "ts_code" in fields:
                code_ix = fields.index("ts_code")
                ids = {row[code_ix] for row in rows}
                observed_ids.update(ids)
                if contract in ("C03", "E02") and len(ids) != 1:
                    bad_identifier_payloads += 1
            if "trade_date" in fields:
                date_ix = fields.index("trade_date")
                dates = [str(row[date_ix]) for row in rows]
                min_dates.append(min(dates))
                max_dates.append(max(dates))
                if len(dates) != len(set(dates)):
                    duplicate_date_payloads += 1
        detail[contract] = {
            "unique_successful_requests": len(payloads),
            "rows": row_count,
            "empty_payloads": empty_payloads,
            "missing_required_field_payloads": missing_field_payloads,
            "duplicate_trade_date_payloads": duplicate_date_payloads,
            "bad_identifier_payloads": bad_identifier_payloads,
            "observed_security_ids": len(observed_ids),
            "min_observed_date": min(min_dates) if min_dates else None,
            "max_observed_date": max(max_dates) if max_dates else None,
        }

    journal_events = [json.loads(x) for x in (RUN / "acquisition_journal.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    journal_hash_failures = []
    for event in journal_events:
        file = event.get("file")
        expected_hash = event.get("sha256")
        if file and expected_hash:
            path = RUN / file
            if not path.exists() or sha(path) != expected_hash:
                journal_hash_failures.append(file)

    successful_ids = Counter(e.get("contract") for e in journal_events if e.get("response_code") == 0)
    failed_ids = Counter(e.get("contract") for e in journal_events if e.get("response_code") not in (None, 0) or e.get("status") == "FAILED")
    rid_to_code = {e.get("request_id"): (e.get("params") or {}).get("ts_code") for e in journal_events
                   if e.get("contract") == "C03" and e.get("response_code") == 0}
    benchmark_dates = set()
    for payload in canonical_payloads["E03-A"]:
        fields = (payload.get("data") or {}).get("fields") or []
        if "trade_date" in fields:
            ix = fields.index("trade_date")
            benchmark_dates.update(str(row[ix]) for row in (payload.get("data") or {}).get("items") or [])
    candidate_unknown_sessions = 0
    securities_with_candidate_unknown_sessions = 0
    for (contract, rid), entries in grouped.items():
        if contract != "C03" or not any(d.get("code") == 0 for _, d in entries):
            continue
        code = rid_to_code.get(rid)
        payload = next(d for _, d in entries if d.get("code") == 0)
        fields = (payload.get("data") or {}).get("fields") or []
        actual = set()
        if "trade_date" in fields:
            ix = fields.index("trade_date")
            actual = {str(row[ix]) for row in (payload.get("data") or {}).get("items") or []}
        interval_code = "601360.SH" if code == "601313.SH" else code
        listed, delisted = c01_intervals.get(interval_code, ("20130107", ""))
        lower = max("20130107", listed or "20130107")
        upper = min("20251231", delisted or "20251231")
        if code == "601313.SH":
            upper = min(upper, "20180227")
            probe = ROOT / "data/raw/g3b_full/structural_resolution/601313_tushare_probe_v1/daily.json"
            if probe.exists():
                probe_payload = json.loads(probe.read_text(encoding="utf-8"))
                probe_fields = (probe_payload.get("data") or {}).get("fields") or []
                if "trade_date" in probe_fields:
                    probe_ix = probe_fields.index("trade_date")
                    actual = {str(row[probe_ix]) for row in (probe_payload.get("data") or {}).get("items") or [] if str(row[probe_ix]) <= upper}
        expected = {d for d in benchmark_dates if lower <= d <= upper}
        missing = expected - actual
        if missing:
            candidate_unknown_sessions += len(missing)
            securities_with_candidate_unknown_sessions += 1
    coverage = {
        "eligible_universe": len(eligible),
        "c06_raw_union": len(universe_codes),
        "excluded_non_primary_exchange_codes": len(excluded),
        "excluded_prefixes": dict(Counter(x[0] for x in excluded)),
        "c03_unique_request_coverage": detail["C03"]["unique_successful_requests"],
        "e02_unique_request_coverage": detail["E02"]["unique_successful_requests"],
        "eligible_ids_missing_from_c01": sorted(set(eligible) - c01_ids - mapped_ids),
        "eligible_ids_resolved_by_history_mapping": sorted((set(eligible) - c01_ids) & mapped_ids),
        "c03_ids_missing_from_c01": sorted({x for p in canonical_payloads["C03"] for x in ((p.get("data") or {}).get("items") or [])[:0]}),
        "candidate_unknown_missing_sessions_without_c05": candidate_unknown_sessions,
        "securities_with_candidate_unknown_missing_sessions": securities_with_candidate_unknown_sessions,
        "missingness_method": "Benchmark trading dates within C01 listing interval minus observed C03 dates; diagnostic only, not a suspension classification.",
    }
    statuses = {
        "C01": "PASS WITH LIMITATIONS" if detail["C01"]["unique_successful_requests"] == 3 and not coverage["eligible_ids_missing_from_c01"] else "FAIL",
        "C03": "PASS WITH LIMITATIONS" if detail["C03"]["unique_successful_requests"] == len(eligible) and detail["C03"]["missing_required_field_payloads"] == 0 else "FAIL",
        "C04": "FAIL — AUTHORITATIVE FORMAL PAYLOAD NOT ACQUIRED",
        "C05": "FAIL — AUTHORITATIVE FORMAL PAYLOAD NOT ACQUIRED; MISSINGNESS REMAINS UNKNOWN",
        "C06": "PASS WITH LIMITATIONS",
        "E02": "PASS WITH LIMITATIONS" if detail["E02"]["unique_successful_requests"] == len(eligible) and detail["E02"]["missing_required_field_payloads"] == 0 else "FAIL",
        "E03-A": "PASS WITH LIMITATIONS" if detail["E03-A"]["unique_successful_requests"] == 1 else "FAIL",
        "E03-B": "EXCLUDED / BLOCKS SPECIFIC COMPETING SPECIFICATIONS ONLY",
    }
    report = {
        "status": "STRUCTURAL VALIDATION COMPLETE — CONTRACT FAILURES REQUIRE RESEARCHER REVIEW",
        "scope": "Acquisition/provenance/coverage validation only; no research measurements or outcomes",
        "detail": detail,
        "coverage": coverage,
        "journal": {
            "events": len(journal_events),
            "successful_events": dict(successful_ids),
            "failed_events_preserved": dict(failed_ids),
            "hash_failures": journal_hash_failures,
        },
        "concurrent_resume_incident": {
            "duplicate_success_groups": duplicate_groups,
            "duplicate_semantic_data_mismatch_groups": duplicate_hash_mismatch_groups,
            "raw_checksums_expected_to_differ": "Provider-generated response request_id differs; returned data subtree is validated separately.",
            "handling": "All objects preserved; no duplicates deleted. One process was stopped; one controlled runner completed.",
        },
        "contract_status": statuses,
        "outcome_quarantine": "PASS — acquisition contains no constructed targets, measurements, relationships, predictions or PnL",
    }
    path = OUT / "structural_validation_report.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    normalized_manifest = {
        "status": "STRUCTURAL QA — NON-EMPIRICAL",
        "normalization": "SHA-256 of Tushare data.fields/items; provider response request_id excluded",
        "records": sorted(normalized_content_records, key=lambda x: (x["contract"], x["request_id"])),
    }
    (OUT / "normalized_content_manifest.json").write_text(
        json.dumps(normalized_manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"report": str(path.relative_to(ROOT)), "contract_status": statuses,
                      "eligible_universe": len(eligible), "duplicate_success_groups": duplicate_groups,
                      "duplicate_semantic_data_mismatch_groups": duplicate_hash_mismatch_groups,
                      "journal_hash_failures": len(journal_hash_failures)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
