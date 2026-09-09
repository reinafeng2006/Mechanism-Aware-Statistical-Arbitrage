"""Bounded authenticated Tushare permission re-check; never persists or prints credentials."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "g3b_qa" / "tushare_permission_recheck_r9_v1"
API = "https://api.tushare.pro"

REQUESTS = (
    ("stock_basic", {"exchange": "SSE", "list_status": "L"}, "ts_code,symbol,name,exchange,list_status,list_date,delist_date"),
    ("stock_basic", {"exchange": "SZSE", "list_status": "L"}, "ts_code,symbol,name,exchange,list_status,list_date,delist_date"),
    ("daily_basic", {"ts_code": "600031.SH", "start_date": "20250102", "end_date": "20250103"}, "ts_code,trade_date,turnover_rate,turnover_rate_f,total_share,float_share,free_share"),
    ("daily_basic", {"ts_code": "000157.SZ", "start_date": "20250102", "end_date": "20250103"}, "ts_code,trade_date,turnover_rate,turnover_rate_f,total_share,float_share,free_share"),
)


def credential() -> str:
    value = os.environ.get("TUSHARE_TOKEN") or os.environ.get("TUSHARE_API_TOKEN")
    if not value:
        raise SystemExit("Tushare credential is not configured in this process environment.")
    return value


def request_id(api_name: str, params: dict, fields: str) -> str:
    clean = json.dumps({"api_name": api_name, "params": params, "fields": fields}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(clean.encode()).hexdigest()[:20]


def call(api_name: str, params: dict, fields: str, token: str) -> dict:
    payload = json.dumps({"api_name": api_name, "token": token, "params": params, "fields": fields}).encode()
    req = Request(API, data=payload, headers={"Content-Type": "application/json"})
    with urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode())


def main() -> None:
    token = credential()
    if OUT.exists():
        raise SystemExit("Immutable QA output already exists; refusing overwrite.")
    OUT.mkdir(parents=True)
    records = []
    for api_name, params, fields in REQUESTS:
        requested_at = dt.datetime.now(dt.timezone.utc).isoformat()
        result = call(api_name, params, fields, token)
        encoded = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        rid = request_id(api_name, params, fields)
        filename = f"{api_name}__{rid}.json"
        (OUT / filename).write_bytes(encoded)
        data = result.get("data") or {}
        records.append({
            "api_name": api_name,
            "request_id": rid,
            "params_without_credential": params,
            "requested_at_utc": requested_at,
            "response_code": result.get("code"),
            "response_message": result.get("msg"),
            "returned_fields": data.get("fields") or [],
            "row_count": len(data.get("items") or []),
            "file": filename,
            "sha256": hashlib.sha256(encoded).hexdigest().upper(),
        })
    manifest = {
        "manifest_id": "G3B-R9-TUSHARE-2000-POINT-PERMISSION-RECHECK-V1",
        "status": "AUDIT/QA — NON-EMPIRICAL",
        "scope": ["stock_basic", "daily_basic"],
        "credential_recorded": False,
        "credential_hashed": False,
        "request_count": len(records),
        "requests": records,
        "interpretation_boundary": "Endpoint success demonstrates effective token permission, not PIT/vintage qualification.",
    }
    manifest_bytes = json.dumps(manifest, ensure_ascii=False, indent=2).encode()
    (OUT / "manifest.json").write_bytes(manifest_bytes)
    summary = {
        "request_count": len(records),
        "success_count": sum(r["response_code"] == 0 for r in records),
        "codes": [{"api": r["api_name"], "code": r["response_code"], "rows": r["row_count"]} for r in records],
        "credential_recorded": False,
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
