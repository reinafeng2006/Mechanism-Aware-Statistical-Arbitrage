"""Bounded Tushare integrated-candidate QA. Never persists or prints credentials."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "g3b_qa" / "tushare_integrated_qa_r8_v1"
API = "https://api.tushare.pro"
SECURITIES = ("000157.SZ", "000404.SZ", "600031.SH", "600055.SH")
DATE_SLICES = (("20130107", "20130111"), ("20251229", "20251231"))

def token() -> str:
    value = os.environ.get("TUSHARE_TOKEN") or os.environ.get("TUSHARE_API_TOKEN")
    if not value:
        raise SystemExit("Tushare credential is not configured in this process environment.")
    return value

def call(api_name: str, params: dict, fields: str) -> dict:
    payload = json.dumps({"api_name": api_name, "token": token(), "params": params, "fields": fields}).encode()
    req = Request(API, data=payload, headers={"Content-Type": "application/json"})
    with urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode())

def request_id(api_name: str, params: dict, fields: str) -> str:
    clean = json.dumps({"api_name": api_name, "params": params, "fields": fields}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(clean.encode()).hexdigest()[:16]

def write_raw(api_name: str, params: dict, fields: str, result: dict) -> dict:
    rid = request_id(api_name, params, fields)
    path = OUT / f"{api_name}__{rid}.json"
    encoded = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    path.write_bytes(encoded)
    data = result.get("data") or {}
    return {"api_name": api_name, "request_id": rid, "params_without_credential": params,
            "requested_fields": fields.split(","), "response_code": result.get("code"),
            "response_message": result.get("msg"), "returned_fields": data.get("fields") or [],
            "row_count": len(data.get("items") or []), "file": str(path.relative_to(ROOT)).replace("\\", "/"),
            "bytes": len(encoded), "sha256": hashlib.sha256(encoded).hexdigest().upper()}

def main() -> None:
    token()
    OUT.mkdir(parents=True, exist_ok=True)
    requests = []
    for security in SECURITIES:
        requests.append(("stock_basic", {"ts_code": security}, "ts_code,symbol,name,area,industry,market,exchange,curr_type,list_status,list_date,delist_date,is_hs"))
        requests.append(("suspend_d", {"ts_code": security, "start_date": "20130107", "end_date": "20251231"}, "ts_code,trade_date,suspend_timing,suspend_type"))
        for start_date, end_date in DATE_SLICES:
            p = {"ts_code": security, "start_date": start_date, "end_date": end_date}
            requests.extend([
                ("daily", p, "ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount"),
                ("daily_basic", p, "ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,total_share,float_share,free_share,total_mv,circ_mv")])
    for start_date, end_date in DATE_SLICES:
        p = {"ts_code": "000300.SH", "start_date": start_date, "end_date": end_date}
        requests.extend([
            ("index_daily", p, "ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount"),
            ("index_weight", {"index_code": "000300.SH", "start_date": start_date, "end_date": end_date}, "index_code,con_code,trade_date,weight")])
    records = []
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    for api_name, params, fields in requests:
        try:
            records.append(write_raw(api_name, params, fields, call(api_name, params, fields)))
        except Exception as exc:
            records.append({"api_name": api_name, "request_id": request_id(api_name, params, fields),
                            "params_without_credential": params, "requested_fields": fields.split(","),
                            "transport_error_type": type(exc).__name__, "status": "REQUEST_FAILED"})
    manifest = {"manifest_id": "G3B-R8-TUSHARE-INTEGRATED-QA-V1", "status": "AUDIT/QA — NON-EMPIRICAL",
                "provider": "Tushare Pro", "source_role": "PRIMARY INTEGRATED CANDIDATE — NOT CANONICAL / NOT FORMALLY SELECTED",
                "credential_recorded": False, "retrieval_start_utc": started,
                "retrieval_end_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "deterministic_securities": list(SECURITIES), "date_slices": [list(x) for x in DATE_SLICES],
                "benchmark": "000300.SH", "requests": records}
    path = OUT / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"manifest": str(path.relative_to(ROOT)).replace("\\", "/"), "request_count": len(records),
                      "success_count": sum(r.get("response_code") == 0 for r in records),
                      "api_error_count": sum(r.get("response_code") not in (None, 0) for r in records),
                      "transport_error_count": sum(r.get("status") == "REQUEST_FAILED" for r in records)}))

if __name__ == "__main__":
    main()
