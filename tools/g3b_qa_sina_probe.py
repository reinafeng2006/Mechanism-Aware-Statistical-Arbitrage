"""Bounded Sina A-share fallback QA; saves raw responses and structural metadata only."""
from __future__ import annotations
import ast, datetime as dt, hashlib, json, os
from pathlib import Path
import pandas as pd
import requests
import py_mini_racer
from akshare.stock.cons import hk_js_decode

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_ID = os.environ.get("SINA_QA_SNAPSHOT_ID", "sina_fallback_qa_v1")
OUT = ROOT / "data" / "raw" / "g3b_qa" / SNAPSHOT_ID
SYMBOLS = ("sz000157", "sz000404", "sh600031", "sh600055")
BENCHMARK = "sh000300"
SLICES = (("2013-01-07", "2013-01-11"), ("2025-12-29", "2025-12-31"))
URLS = {
    "raw_history": "https://finance.sina.com.cn/realstock/company/{symbol}/hisdata_klc2/klc_kl.js",
    "qfq_factor": "https://finance.sina.com.cn/realstock/company/{symbol}/qfq.js",
    "hfq_factor": "https://finance.sina.com.cn/realstock/company/{symbol}/hfq.js",
    "share_amount": "https://stock.finance.sina.com.cn/stock/api/jsonp.php/var%20KKE_ShareAmount_{symbol}=/StockService.getAmountBySymbol?_=20&symbol={symbol}",
}
HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://finance.sina.com.cn/"}

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest().upper()

def fetch(kind: str, symbol: str) -> tuple[bytes, dict]:
    url = URLS[kind].format(symbol=symbol)
    r = requests.get(url, headers=HEADERS, timeout=60)
    data = r.content
    path = OUT / f"{symbol}__{kind}.bin"
    path.write_bytes(data)
    return data, {"symbol": symbol, "kind": kind, "url": url, "http_status": r.status_code,
                  "content_type": r.headers.get("content-type"), "etag": r.headers.get("etag"),
                  "last_modified": r.headers.get("last-modified"), "bytes": len(data), "sha256": sha(data),
                  "file": str(path.relative_to(ROOT)).replace("\\", "/")}

def decode_history(data: bytes) -> pd.DataFrame:
    text = data.decode("utf-8", errors="replace")
    payload = text.split("=", 1)[1].split(";", 1)[0].replace('"', "")
    js = py_mini_racer.MiniRacer(); js.eval(hk_js_decode)
    rows = js.call("d", payload)
    frame = pd.DataFrame(rows)
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    return frame.sort_values("date")

def decode_factor(data: bytes) -> pd.DataFrame:
    text = data.decode("utf-8", errors="replace")
    obj = ast.literal_eval(text.split("=", 1)[1].splitlines()[0])
    frame = pd.DataFrame(obj.get("data", [])).rename(columns={"d": "date", "f": "factor"})
    frame = frame[["date", "factor"]]
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    return frame.sort_values("date")

def main() -> None:
    if OUT.exists():
        raise SystemExit(f"Immutable QA snapshot already exists: {OUT}")
    OUT.mkdir(parents=True, exist_ok=True)
    manifest, summaries = [], []
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    for symbol in (*SYMBOLS, BENCHMARK):
        raw, rec = fetch("raw_history", symbol); manifest.append(rec)
        hist = decode_history(raw)
        item = {"symbol": symbol, "history_fields": list(hist.columns), "history_rows": len(hist),
                "first_date": None if hist.empty else hist.date.min().date().isoformat(),
                "last_date": None if hist.empty else hist.date.max().date().isoformat(), "slices": []}
        for start, end in SLICES:
            part = hist[(hist.date >= start) & (hist.date <= end)]
            item["slices"].append({"start": start, "end": end, "rows": len(part),
                                    "dates": [x.date().isoformat() for x in part.date]})
        if symbol != BENCHMARK:
            for kind in ("qfq_factor", "hfq_factor", "share_amount"):
                data, extra = fetch(kind, symbol); manifest.append(extra)
                if kind.endswith("factor"):
                    factor = decode_factor(data)
                    item[kind] = {"fields": list(factor.columns), "rows": len(factor),
                                  "first_date": None if factor.empty else factor.date.min().date().isoformat(),
                                  "last_date": None if factor.empty else factor.date.max().date().isoformat()}
                else:
                    item[kind] = {"parse_status": "RAW_RESPONSE_PRESERVED; SEMANTICS REQUIRE SOURCE DICTIONARY",
                                  "contains_response_array": b"[" in data and b"]" in data}
        summaries.append(item)
    finished = dt.datetime.now(dt.timezone.utc).isoformat()
    body = {"manifest_id": SNAPSHOT_ID, "status": "AUDIT/QA — FALLBACK CANDIDATE — NON-EMPIRICAL",
            "canonical_status": "NOT APPROVED", "retrieval_start_utc": started, "retrieval_end_utc": finished,
            "deterministic_symbols": list(SYMBOLS), "benchmark": BENCHMARK, "date_slices": [list(x) for x in SLICES],
            "requests": manifest, "structural_summary": summaries,
            "prohibitions": ["NO RESEARCH MEASUREMENTS", "NO TARGETS", "NO OUTCOME INSPECTION", "NO PNL"]}
    path = OUT / "manifest.json"; path.write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"manifest": str(path.relative_to(ROOT)).replace("\\", "/"), "request_count": len(manifest),
                      "all_http_200": all(x["http_status"] == 200 for x in manifest),
                      "symbols": {x["symbol"]: {"rows": x["history_rows"], "first": x["first_date"], "last": x["last_date"]} for x in summaries}}))

if __name__ == "__main__": main()
