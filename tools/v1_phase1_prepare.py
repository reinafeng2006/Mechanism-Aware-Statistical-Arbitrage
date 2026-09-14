"""Prepare a deterministic 2013-2019 matrix for authorized V1 inner computation.

The script reads only frozen CORE-V1 inputs plus the frozen C04-A and C06
availability amendments. It does not screen pairs, fit models, inspect OF4, or
read the sealed held-out region. The derived NPZ stays in ignored QA work; a
public manifest contains hashes and structural counts only.
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/g3b_full/tushare/full_2013_2025_v1"
SIDECAR = ROOT / "data/qa_work/g3b_f2/security_date_eligibility/v1/security_date_eligibility_sidecar_v1.csv.gz"
C04 = ROOT / "data/qa_work/v1/c04_a/official_calendar_v1/v1_exclusion_calendar.jsonl"
C06_BASE = ROOT / "data/qa_work/g3b_full/c06/20260909T081518Z/primary_membership.jsonl"
C06_AMEND = ROOT / "data/amendments/c06/C06_AVAILABILITY_AMENDMENT_V1/snapshot_availability_register.jsonl"
OUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"
MANIFEST = ROOT / "data/manifests/V1_PHASE1_INNER_INPUT.json"
LOWER, UPPER = "20130107", "20191231"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def payload_data_hash(payload: dict) -> str:
    b = json.dumps(payload.get("data") or {}, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")).encode()
    return hashlib.sha256(b).hexdigest().upper()


def canonical_payloads() -> dict[str, list[dict]]:
    grouped: dict[tuple[str, str], list[tuple[Path, dict]]] = defaultdict(list)
    for path in RAW.glob("*.json"):
        parts = path.stem.split("__")
        if len(parts) < 3 or parts[0] not in {"C03", "E02", "E03-A"}:
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if payload.get("code") == 0:
            grouped[(parts[0], parts[2])].append((path, payload))
    result: dict[str, list[dict]] = defaultdict(list)
    for (contract, _), entries in sorted(grouped.items()):
        hashes = {payload_data_hash(p) for _, p in entries}
        if len(hashes) != 1:
            raise RuntimeError(f"normalized duplicate mismatch for {contract}")
        result[contract].append(sorted(entries, key=lambda x: x[0].name)[0][1])
    return result


def rows(payload: dict) -> list[dict]:
    data = payload.get("data") or {}
    fields = data.get("fields") or []
    return [dict(zip(fields, item)) for item in data.get("items") or []]


def ymd(s: str) -> date:
    return date(int(s[:4]), int(s[4:6]), int(s[6:8]))


def main() -> None:
    deps = ROOT / "data/qa_work/v1/phase1/deps"
    if str(deps) not in sys.path:
        sys.path.insert(0, str(deps))
    import numpy as np

    payloads = canonical_payloads()
    if len(payloads["E03-A"]) != 1:
        raise RuntimeError("exactly one canonical E03-A payload required")
    benchmark = {str(r["trade_date"]): r for r in rows(payloads["E03-A"][0])
                 if LOWER <= str(r["trade_date"]) <= UPPER}
    dates = sorted(benchmark)
    date_ix = {d: i for i, d in enumerate(dates)}

    by_code: dict[str, dict[str, dict]] = {}
    for payload in payloads["C03"]:
        rr = rows(payload)
        if not rr:
            continue
        code = str(rr[0]["ts_code"])
        by_code[code] = {str(x["trade_date"]): x for x in rr
                         if LOWER <= str(x["trade_date"]) <= UPPER}
    codes = sorted(by_code)
    code_ix = {c: i for i, c in enumerate(codes)}
    n_t, n_s = len(dates), len(codes)

    observed_normal = np.zeros((n_t, n_s), dtype=np.bool_)
    sidecar_ticker: dict[tuple[str, str], str] = {}
    with gzip.open(SIDECAR, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            d = r["observation_date"]
            c = r["historical_ticker_code"]
            if d in date_ix and c in code_ix:
                sidecar_ticker[(c, d)] = r["stable_security_id"]
                observed_normal[date_ix[d], code_ix[c]] = r["c05_structural_state"] == "NORMAL TRADING OBSERVED"

    close = np.full((n_t, n_s), np.nan, dtype=np.float64)
    open_ = np.full_like(close, np.nan)
    volume = np.full_like(close, np.nan)
    amount = np.full_like(close, np.nan)
    for c, day_rows in by_code.items():
        j = code_ix[c]
        for d, r in day_rows.items():
            i = date_ix.get(d)
            if i is None:
                continue
            close[i, j] = float(r["close"])
            open_[i, j] = float(r["open"])
            volume[i, j] = float(r["vol"])
            amount[i, j] = float(r["amount"])

    action_dates: set[tuple[str, str]] = set()
    for line in C04.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        action_dates.add((r["historical_ticker"], r["effective_ex_date"].replace("-", "")))

    response = np.full_like(close, np.nan)
    response_ok = np.zeros_like(observed_normal)
    exclusion_count = 0
    for t in range(1, n_t):
        for s, c in enumerate(codes):
            if not (observed_normal[t - 1, s] and observed_normal[t, s]):
                continue
            if (c, dates[t]) in action_dates:
                exclusion_count += 1
                continue
            p0, p1 = close[t - 1, s], close[t, s]
            if np.isfinite(p0) and np.isfinite(p1) and p0 > 0 and p1 > 0:
                response[t, s] = p1 / p0 - 1.0
                response_ok[t, s] = True

    bclose = np.array([float(benchmark[d]["close"]) for d in dates], dtype=np.float64)
    bret = np.full(n_t, np.nan, dtype=np.float64)
    good = np.isfinite(bclose[1:]) & np.isfinite(bclose[:-1]) & (bclose[:-1] > 0)
    bret[1:][good] = bclose[1:][good] / bclose[:-1][good] - 1.0

    amendment = [json.loads(x) for x in C06_AMEND.read_text(encoding="utf-8").splitlines() if x.strip()]
    qualified = sorted((x["corrected_publication_time"].replace("-", ""), x["snapshot_title"],
                        x["logical_snapshot_identifier"], x["taxonomy_version"])
                       for x in amendment if x["qualification_state"].startswith("QUALIFIED"))
    membership_by_title: dict[str, dict[str, int]] = defaultdict(dict)
    for line in C06_BASE.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        c = f"{r['security_code']}.SH" if str(r["security_code"]).startswith("6") else f"{r['security_code']}.SZ"
        if c in code_ix:
            membership_by_title[r["snapshot_title"]][c] = int(r["industry_code"])

    industry = np.zeros((n_t, n_s), dtype=np.int8)
    snapshot_index = np.full(n_t, -1, dtype=np.int16)
    snapshot_ids: list[str] = []
    taxonomy_versions: list[str] = []
    for t, d in enumerate(dates):
        candidates = [x for x in qualified if x[0] < d]
        if not candidates:
            continue
        pub, title, sid, tax = candidates[-1]
        key = (sid, tax)
        if sid not in snapshot_ids:
            snapshot_ids.append(sid)
            taxonomy_versions.append(tax)
        snapshot_index[t] = snapshot_ids.index(sid)
        for c, g in membership_by_title[title].items():
            industry[t, code_ix[c]] = g

    pair_member = response_ok & np.isin(industry, np.array([34, 35], dtype=np.int8))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        raise RuntimeError(f"no silent overwrite: {OUT}")
    np.savez_compressed(OUT, dates=np.array(dates, dtype="S8"), codes=np.array(codes, dtype="S9"),
                        close=close, open=open_, volume=volume, amount=amount, response=response,
                        response_ok=response_ok, industry=industry, pair_member=pair_member,
                        benchmark_response=bret, snapshot_index=snapshot_index,
                        snapshot_ids=np.array(snapshot_ids), taxonomy_versions=np.array(taxonomy_versions))
    manifest = {
        "manifest_id": "V1-PHASE1-INNER-INPUT-1.0",
        "status": "IMMUTABLE DERIVED INNER INPUT — NO MODEL OUTPUT",
        "artifact": OUT.relative_to(ROOT).as_posix(),
        "artifact_sha256": sha(OUT),
        "dates": {"first": dates[0], "last": dates[-1], "count": n_t},
        "securities": n_s,
        "response_state_counts": {"qualified": int(response_ok.sum()), "c04_excluded": exclusion_count},
        "c06_snapshot_ids": snapshot_ids,
        "core_freeze": "CORE-DATASET-FREEZE-V1",
        "core_fingerprint": "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616",
        "c04_manifest": "C04-A-OFFICIAL-CALENDAR-V1",
        "c06_amendment": "C06-AVAILABILITY-AMENDMENT-V1",
        "value_disclosure": "NONE; structural counts and hashes only",
        "of4_accessed": False,
        "held_out_accessed": False,
        "pair_screening": False,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"manifest_id": manifest["manifest_id"], "artifact_sha256": manifest["artifact_sha256"],
                      "date_count": n_t, "security_count": n_s, "result": "PASS"}))


if __name__ == "__main__":
    main()
