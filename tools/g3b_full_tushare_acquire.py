"""Resumable G3B-FULL Tushare acquisition for C01/C03/E02/E03-A only.

Credentials are read from the process environment and never logged or persisted.
No research measurements or outcomes are computed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import time
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.tushare.pro"
START = "20130107"
END = "20251231"


def credential() -> str:
    value = os.environ.get("TUSHARE_TOKEN") or os.environ.get("TUSHARE_API_TOKEN")
    if not value:
        raise SystemExit("Tushare credential unavailable in process environment")
    return value


def call(api_name: str, params: dict, fields: str) -> dict:
    payload = json.dumps({"api_name": api_name, "token": credential(), "params": params, "fields": fields}).encode()
    with urlopen(Request(API, data=payload, headers={"Content-Type": "application/json"}), timeout=60) as response:
        return json.loads(response.read().decode())


def request_id(api_name: str, params: dict, fields: str) -> str:
    clean = json.dumps({"api_name": api_name, "params": params, "fields": fields}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(clean.encode()).hexdigest()[:20]


def exchange_code(code: str) -> str | None:
    if code.startswith("6"):
        return f"{code}.SH"
    if code.startswith(("0", "3")):
        return f"{code}.SZ"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--c06-run", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    credential()
    universe_file = ROOT / "data" / "qa_work" / "g3b_full" / "c06" / args.c06_run / "security_union.txt"
    universe = sorted(filter(None, (exchange_code(x.strip()) for x in universe_file.read_text(encoding="utf-8").splitlines())))
    out = ROOT / "data" / "raw" / "g3b_full" / "tushare" / args.run_id
    out.mkdir(parents=True, exist_ok=True)
    journal = out / "acquisition_journal.jsonl"

    requests: list[tuple[str, str, dict, str, float]] = []
    basic_fields = "ts_code,symbol,name,area,industry,market,exchange,curr_type,list_status,list_date,delist_date,is_hs"
    for status in ("L", "D", "P"):
        requests.append(("C01", "stock_basic", {"exchange": "", "list_status": status}, basic_fields, 61.0))
    daily_fields = "ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount"
    e02_fields = "ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,total_share,float_share,free_share,total_mv,circ_mv"
    for ts_code in universe:
        params = {"ts_code": ts_code, "start_date": START, "end_date": END}
        requests.append(("C03", "daily", params, daily_fields, 1.3))
        requests.append(("E02", "daily_basic", params, e02_fields, 61.0))
    requests.append(("E03-A", "index_daily", {"ts_code": "000300.SH", "start_date": START, "end_date": END}, daily_fields, 61.0))

    existing = {p.stem.split("__")[-1] for p in out.glob("*.json") if "__" in p.stem}
    completed = 0
    for contract, api_name, params, fields, delay in requests:
        rid = request_id(api_name, params, fields)
        if rid in existing:
            completed += 1
            continue
        attempt = 0
        while True:
            attempt += 1
            started = dt.datetime.now(dt.timezone.utc).isoformat()
            try:
                result = call(api_name, params, fields)
                code = result.get("code")
                message = result.get("msg") or ""
                if code != 0 and ("频率" in message or "超限" in message) and attempt < 6:
                    time.sleep(max(delay, 61.0))
                    continue
                encoded = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
                path = out / f"{contract}__{api_name}__{rid}.json"
                path.write_bytes(encoded)
                data = result.get("data") or {}
                event = {"contract": contract, "api_name": api_name, "request_id": rid, "params": params,
                         "requested_fields": fields.split(","), "response_code": code, "response_message": message,
                         "returned_fields": data.get("fields") or [], "row_count": len(data.get("items") or []),
                         "retrieval_time_utc": started, "bytes": len(encoded), "sha256": hashlib.sha256(encoded).hexdigest().upper(),
                         "file": path.name, "attempts": attempt, "credential_recorded": False}
                with journal.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps(event, ensure_ascii=False) + "\n")
                completed += 1
                print(json.dumps({"completed": completed, "total": len(requests), "contract": contract, "api": api_name, "code": code, "rows": event["row_count"]}), flush=True)
                break
            except Exception as exc:
                if attempt >= 6:
                    event = {"contract": contract, "api_name": api_name, "request_id": rid, "params": params,
                             "retrieval_time_utc": started, "transport_error_type": type(exc).__name__, "attempts": attempt,
                             "credential_recorded": False, "status": "FAILED"}
                    with journal.open("a", encoding="utf-8") as handle:
                        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
                    break
                time.sleep(min(300.0, 5.0 * (2 ** (attempt - 1))))
        time.sleep(delay)

    events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines() if line.strip()]
    manifest = {"manifest_id": "G3B-FULL-TUSHARE-C01-C03-E02-E03A-V1", "status": "FORMAL RAW ACQUISITION — NON-EMPIRICAL",
                "run_id": args.run_id, "c06_run": args.c06_run, "date_range": [START, END], "universe_security_count": len(universe),
                "provider": "Tushare Pro", "credential_recorded": False, "formal_contracts": ["C01", "C03", "E02", "E03-A"],
                "excluded": ["C04", "C05", "C06 payloads stored separately", "E03-B", "measurements", "outcomes"],
                "completed_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "events": events}
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": "COMPLETE", "run_id": args.run_id, "events": len(events), "universe": len(universe)}), flush=True)


if __name__ == "__main__":
    main()
