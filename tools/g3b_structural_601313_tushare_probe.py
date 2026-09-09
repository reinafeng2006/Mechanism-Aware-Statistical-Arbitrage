"""Bounded provider-behavior probe for the official 601313 -> 601360 code mapping."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/raw/g3b_full/structural_resolution/601313_tushare_probe_v1"
API = "https://api.tushare.pro"

def main() -> None:
    token = os.environ.get("TUSHARE_TOKEN") or os.environ.get("TUSHARE_API_TOKEN")
    if not token:
        raise SystemExit("Tushare credential unavailable")
    if OUT.exists():
        raise SystemExit("Immutable probe output exists; refusing overwrite")
    OUT.mkdir(parents=True)
    records = []
    for api_name, fields in (
        ("daily", "ts_code,trade_date,open,high,low,close,vol,amount"),
        ("daily_basic", "ts_code,trade_date,turnover_rate,total_share,float_share,free_share"),
    ):
        params = {"ts_code": "601360.SH", "start_date": "20130107", "end_date": "20180301"}
        body = json.dumps({"api_name": api_name, "token": token, "params": params, "fields": fields}).encode()
        with urlopen(Request(API, data=body, headers={"Content-Type": "application/json"}), timeout=60) as response:
            result = json.loads(response.read().decode())
        encoded = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        file = f"{api_name}.json"
        (OUT / file).write_bytes(encoded)
        data = result.get("data") or {}
        records.append({"api_name": api_name, "params_without_credential": params, "response_code": result.get("code"),
                        "response_message": result.get("msg"), "returned_fields": data.get("fields") or [],
                        "row_count": len(data.get("items") or []), "file": file,
                        "retrieval_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                        "sha256": hashlib.sha256(encoded).hexdigest().upper()})
    manifest = {"status": "AUDIT/QA — NON-EMPIRICAL", "scope": "601313 successor-code provider behavior only",
                "credential_recorded": False, "records": records}
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"credential_recorded": False, "results": [{"api": x["api_name"], "code": x["response_code"], "rows": x["row_count"]} for x in records]}))

if __name__ == "__main__":
    main()
