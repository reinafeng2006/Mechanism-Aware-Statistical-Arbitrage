"""Acquire the bounded official C04-A calendar for V1.

The script retrieves only official SSE action tables and official SZSE monthly
"dividend, bonus and rights issues" tables covering the V1 warm-up and inner
development period. It creates immutable raw payloads plus a normalized,
universe-filtered descendant calendar. It never constructs adjusted prices and
never asserts that absence from the calendar proves an action-clean history.
"""
from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import html
import json
import re
import sys
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
VERSION = "C04-A-OFFICIAL-CALENDAR-V1"
RAW_DIR = ROOT / "data" / "raw" / "v1" / "c04_a" / "official_calendar_v1"
DERIVED_DIR = ROOT / "data" / "qa_work" / "v1" / "c04_a" / "official_calendar_v1"
PUBLIC_MANIFEST = ROOT / "data" / "manifests" / "C04_A_OFFICIAL_CALENDAR_V1.json"
ACQUISITION_MANIFEST = ROOT / "data" / "raw" / "g3b_full" / "tushare" / "full_2013_2025_v1" / "manifest.json"
UA = "MechanismAwareStatArb/1.0 bounded-official-C04-acquisition"
SSE_QUERY = "https://query.sse.com.cn/commonQuery.do"
SSE_REFERERS = {
    "dividend": "https://www.sse.com.cn/market/stockdata/dividends/dividend/index_his.shtml",
    "bonus": "https://www.sse.com.cn/market/stockdata/dividends/bonus/index_his.shtml",
    "rights": "https://www.sse.com.cn/market/stockdata/raise/overview/index_his.shtml",
}
SZSE_INDEX = "https://www.szse.cn/market/periodical/month/index.html"
SZSE_MONTH_BASE = "https://www.szse.cn/market/periodical/month/"
START_PERIOD = "2012-12"  # boundary guard for actions effective after 2013-01-07
END_PERIOD = "2019-12"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def fetch(url: str, referer: str, attempts: int = 4) -> tuple[bytes, dict[str, str]]:
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            request = Request(url, headers={"User-Agent": UA, "Referer": referer, "Accept": "application/json,text/html,*/*"})
            with urlopen(request, timeout=45) as response:
                return response.read(), {str(k): str(v) for k, v in response.headers.items()}
        except Exception as exc:  # bounded retry; the manifest records terminal failures
            last = exc
            time.sleep(min(8.0, 0.75 * (2**attempt)))
    assert last is not None
    raise last


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href is not None:
            label = re.sub(r"\s+", " ", html.unescape("".join(self._text))).strip()
            self.links.append((self._href, label))
            self._href = None
            self._text = []


class RowParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []
        elif tag == "br" and self._cell is not None:
            self._cell.append(" ")

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"td", "th"} and self._cell is not None and self._row is not None:
            self._row.append(re.sub(r"\s+", " ", html.unescape("".join(self._cell))).strip())
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None
            self._cell = None


def decode_html(data: bytes, headers: dict[str, str]) -> str:
    content_type = headers.get("Content-Type", "")
    match = re.search(r"charset=([\w-]+)", content_type, re.I)
    encodings = [match.group(1)] if match else []
    encodings += ["utf-8", "gb18030"]
    for encoding in encodings:
        try:
            return data.decode(encoding)
        except (UnicodeDecodeError, LookupError):
            continue
    return data.decode("utf-8", errors="replace")


def normalized_date(value: object) -> str | None:
    text = str(value or "").strip().replace("/", "-").replace(".", "-")
    match = re.fullmatch(r"(20\d{2})-?(\d{2})-?(\d{2})", text)
    if not match:
        return None
    try:
        return dt.date(int(match.group(1)), int(match.group(2)), int(match.group(3))).isoformat()
    except ValueError:
        return None


def nonzero(value: object) -> bool:
    text = str(value or "").strip().replace(",", "")
    if not text or text in {"-", "—", "–"}:
        return False
    try:
        return float(text) != 0.0
    except ValueError:
        return True


def write_raw(name: str, data: bytes) -> dict[str, object]:
    path = RAW_DIR / name
    if path.exists():
        raise FileExistsError(f"immutable raw artifact already exists: {path}")
    path.write_bytes(data)
    return {"file": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": sha256(data)}


def sse_url(kind: str, year: int) -> str:
    base = {
        "isPagination": "true",
        "pageHelp.pageSize": "5000",
        "pageHelp.pageNo": "1",
        "pageHelp.beginPage": "1",
        "pageHelp.endPage": "1",
        "pageHelp.cacheSize": "1",
    }
    if kind == "dividend":
        base.update(sqlId="COMMON_SSE_GP_SJTJ_FHSG_AGFH_L_NEW", record_date_a=str(year), security_code_a="")
    elif kind == "bonus":
        base.update(sqlId="COMMON_SSE_GP_SJTJ_FHSG_SG_L_NEW", year1=str(year), year2=str(year), company_code="")
    elif kind == "rights":
        base.update(sqlId="COMMON_SSE_GP_SJTJ_MJZJ_PG_AGPG_L", searchyear=str(year))
    else:
        raise ValueError(kind)
    return SSE_QUERY + "?" + urlencode(sorted(base.items()))


def acquire_sse(universe: set[str]) -> tuple[list[dict], list[dict], list[dict]]:
    raw_records: list[dict] = []
    actions: list[dict] = []
    failures: list[dict] = []
    for year in range(2012, 2020):
        for kind in ("dividend", "bonus", "rights"):
            url = sse_url(kind, year)
            try:
                body, headers = fetch(url, SSE_REFERERS[kind])
                artifact = write_raw(f"sse_{kind}_{year}.json", body)
                payload = json.loads(body.decode("utf-8"))
                rows = ((payload.get("pageHelp") or {}).get("data") or [])
                raw_records.append({"source": "SSE_OFFICIAL", "kind": kind, "year": year, "url": url, "status": "OK", "rows": len(rows), **artifact})
                for row in rows:
                    code = str(row.get("SECURITY_CODE_A") or row.get("COMPANY_CODE") or "").strip()
                    if code not in universe:
                        continue
                    if kind == "dividend":
                        effective = normalized_date(row.get("EX_DIVIDEND_DATE_A"))
                        action_types = ["CASH_DIVIDEND"]
                        terms = {"pre_tax_per_share": str(row.get("DIVIDEND_PER_SHARE2_A") or "").strip(), "after_tax_per_share": str(row.get("DIVIDEND_PER_SHARE1_A") or "").strip()}
                        publication = None
                    elif kind == "bonus":
                        effective = normalized_date(row.get("EX_RIGHT_DATE_A"))
                        action_types = ["BONUS_OR_CAPITALIZATION"]
                        terms = {"bonus_rate_per_10": str(row.get("BONUS_RATE") or "").strip()}
                        publication = normalized_date(row.get("ANNOUNCE_DATE"))
                    else:
                        effective = normalized_date(row.get("EX_RIGHTS_DATE_A"))
                        action_types = ["RIGHTS_ISSUE"]
                        terms = {"rights_price": str(row.get("PRICE_OF_RIGHTS_ISSUE_A") or "").strip(), "rights_ratio_per_10": str(row.get("RATIO_OF_RIGHTS_ISSUE_A") or "").strip()}
                        publication = None
                    actions.append({
                        "calendar_version": VERSION,
                        "source": "SSE_OFFICIAL",
                        "source_url": url,
                        "source_artifact": artifact["file"],
                        "source_artifact_sha256": artifact["sha256"],
                        "security_code": code,
                        "historical_ticker": f"{code}.SH",
                        "action_types": action_types,
                        "record_date": normalized_date(row.get("RECORD_DATE_A")),
                        "effective_ex_date": effective,
                        "action_publication_date": publication,
                        "action_publication_time_quality": "OFFICIAL_FIELD" if publication else "NOT_PRESENT_IN_OFFICIAL_TABLE",
                        "terms": terms,
                        "eligibility_effect": "IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED" if effective else "EFFECTIVE DATE UNRESOLVED — NO CLEAN INTERVAL INFERENCE",
                    })
            except Exception as exc:
                failures.append({"source": "SSE_OFFICIAL", "kind": kind, "year": year, "url": url, "error_type": type(exc).__name__})
    return raw_records, actions, failures


def month_in_scope(period: str) -> bool:
    return START_PERIOD <= period <= END_PERIOD


def acquire_szse(universe: set[str]) -> tuple[list[dict], list[dict], list[dict]]:
    raw_records: list[dict] = []
    actions: list[dict] = []
    failures: list[dict] = []
    index_body, index_headers = fetch(SZSE_INDEX, "https://www.szse.cn/")
    index_artifact = write_raw("szse_month_index.html", index_body)
    raw_records.append({"source": "SZSE_OFFICIAL", "kind": "month_index", "url": SZSE_INDEX, "status": "OK", **index_artifact})
    text = decode_html(index_body, index_headers)
    entries = [(period, urljoin(SZSE_MONTH_BASE, path)) for path, period in re.findall(r"value:'([^']+)'\s*,\s*text:'(\d{4}-\d{2})'", text) if month_in_scope(period)]
    entries = sorted(set(entries))

    def one_month(item: tuple[str, str]) -> tuple[list[dict], list[dict], list[dict]]:
        period, parent_url = item
        local_raw: list[dict] = []
        local_actions: list[dict] = []
        local_failures: list[dict] = []
        try:
            parent_body, parent_headers = fetch(parent_url, SZSE_INDEX)
            parent_artifact = write_raw(f"szse_{period}_parent.html", parent_body)
            local_raw.append({"source": "SZSE_OFFICIAL", "kind": "monthly_report_parent", "period": period, "url": parent_url, "status": "OK", **parent_artifact})
            parser = LinkParser()
            parser.feed(decode_html(parent_body, parent_headers))
            matches = [urljoin(parent_url, href.replace("http://", "https://", 1)) for href, label in parser.links if "分红派息配股" in label]
            if len(matches) != 1:
                raise ValueError(f"expected exactly one action-table link, found {len(matches)}")
            action_url = matches[0]
            action_body, action_headers = fetch(action_url, parent_url)
            action_artifact = write_raw(f"szse_{period}_actions.html", action_body)
            table = RowParser()
            table.feed(decode_html(action_body, action_headers))
            data_rows = [row for row in table.rows if row and re.fullmatch(r"\d{6}", row[0].strip())]
            local_raw.append({"source": "SZSE_OFFICIAL", "kind": "monthly_action_table", "period": period, "url": action_url, "status": "OK", "rows": len(data_rows), **action_artifact})
            for row in data_rows:
                if len(row) < 12:
                    local_failures.append({"source": "SZSE_OFFICIAL", "period": period, "url": action_url, "error_type": "SHORT_DATA_ROW", "columns": len(row), "security_code": row[0]})
                    continue
                code = row[0].strip()
                if code not in universe:
                    continue
                padded = row + [""] * (14 - len(row))
                types: list[str] = []
                if nonzero(padded[2]) or nonzero(padded[3]):
                    types.append("BONUS_OR_CAPITALIZATION")
                if nonzero(padded[4]) or nonzero(padded[5]):
                    types.append("CASH_DIVIDEND")
                if nonzero(padded[6]) or nonzero(padded[7]) or nonzero(padded[8]):
                    types.append("RIGHTS_ISSUE")
                if not types:
                    types.append("OFFICIAL_ACTION_ROW_UNCLASSIFIED")
                local_actions.append({
                    "calendar_version": VERSION,
                    "source": "SZSE_OFFICIAL",
                    "source_url": action_url,
                    "source_artifact": action_artifact["file"],
                    "source_artifact_sha256": action_artifact["sha256"],
                    "source_archive_period": period,
                    "security_code": code,
                    "historical_ticker": f"{code}.SZ",
                    "security_name": padded[1],
                    "action_types": types,
                    "record_date": normalized_date(padded[11]),
                    "effective_ex_date": normalized_date(padded[10]),
                    "action_publication_date": None,
                    "action_publication_time_quality": "NOT_PRESENT_IN_OFFICIAL_MONTHLY_TABLE",
                    "terms": {
                        "bonus_shares": padded[2], "bonus_rate": padded[3],
                        "cash_dividend_amount": padded[4], "dividend_per_share": padded[5],
                        "rights_shares": padded[6], "rights_rate": padded[7], "rights_price": padded[8],
                    },
                    "eligibility_effect": "IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED" if normalized_date(padded[10]) else "EFFECTIVE DATE UNRESOLVED — NO CLEAN INTERVAL INFERENCE",
                })
        except Exception as exc:
            local_failures.append({"source": "SZSE_OFFICIAL", "period": period, "url": parent_url, "error_type": type(exc).__name__, "error_detail": str(exc)[:240]})
        return local_raw, local_actions, local_failures

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for local_raw, local_actions, local_failures in pool.map(one_month, entries):
            raw_records.extend(local_raw)
            actions.extend(local_actions)
            failures.extend(local_failures)
    expected_periods = 85  # 2012-12 plus 2013-01 through 2019-12
    if len(entries) != expected_periods:
        failures.append({"source": "SZSE_OFFICIAL", "error_type": "ARCHIVE_PERIOD_COUNT", "expected": expected_periods, "observed": len(entries)})
    return raw_records, actions, failures


def main() -> None:
    for path in (RAW_DIR, DERIVED_DIR, PUBLIC_MANIFEST):
        if path.exists():
            raise SystemExit(f"immutable V1 target already exists; no overwrite permitted: {path}")
    acquisition = json.loads(ACQUISITION_MANIFEST.read_text(encoding="utf-8"))
    acquired_tickers = {
        str(event.get("params", {}).get("ts_code", ""))
        for event in acquisition.get("events", [])
        if event.get("contract") == "C03" and re.fullmatch(r"\d{6}\.(?:SH|SZ)", str(event.get("params", {}).get("ts_code", "")))
    }
    universe = {ticker[:6] for ticker in acquired_tickers}
    if len(universe) != 751:
        raise SystemExit(f"frozen acquired C03 universe mismatch: expected 751, observed {len(universe)}")
    RAW_DIR.mkdir(parents=True, exist_ok=False)
    DERIVED_DIR.mkdir(parents=True, exist_ok=False)
    retrieval_time = dt.datetime.now(dt.timezone.utc).isoformat()

    sse_raw, sse_actions, sse_failures = acquire_sse(universe)
    szse_raw, szse_actions, szse_failures = acquire_szse(universe)
    raw_records = sorted(sse_raw + szse_raw, key=lambda item: (str(item.get("source")), str(item.get("kind")), str(item.get("year", item.get("period", "")))))
    failures = sse_failures + szse_failures
    actions = sse_actions + szse_actions
    # Retain source-row duplicates in raw, but normalize the action calendar by
    # exact semantic content so dynamic page duplication cannot change eligibility.
    unique: dict[str, dict] = {}
    for action in actions:
        key = sha256(canonical_json_bytes(action))
        unique[key] = action
    actions = sorted(unique.values(), key=lambda item: (str(item.get("historical_ticker")), str(item.get("effective_ex_date")), "+".join(item.get("action_types", [])), str(item.get("source"))))

    exclusions: list[dict] = []
    unresolved_effective = 0
    for action in actions:
        if not action.get("effective_ex_date"):
            unresolved_effective += 1
            continue
        exclusions.append({
            "calendar_version": VERSION,
            "historical_ticker": action["historical_ticker"],
            "effective_ex_date": action["effective_ex_date"],
            "action_types": action["action_types"],
            "interval_rule": "EXCLUDE_CLOSE_TO_CLOSE_INTERVAL_(PREVIOUS_ELIGIBLE_SESSION,CURRENT_SESSION]_CONTAINING_EFFECTIVE_EX_DATE",
            "state": "IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED",
            "source": action["source"],
            "source_artifact": action["source_artifact"],
            "source_artifact_sha256": action["source_artifact_sha256"],
        })
    exclusions = sorted(exclusions, key=lambda item: (item["historical_ticker"], item["effective_ex_date"], "+".join(item["action_types"]), item["source"]))

    action_bytes = b"".join(canonical_json_bytes(row) for row in actions)
    exclusion_bytes = b"".join(canonical_json_bytes(row) for row in exclusions)
    action_path = DERIVED_DIR / "official_action_calendar.jsonl"
    exclusion_path = DERIVED_DIR / "v1_exclusion_calendar.jsonl"
    action_path.write_bytes(action_bytes)
    exclusion_path.write_bytes(exclusion_bytes)

    raw_root_material = "".join(f"{record['file']}\t{record['sha256']}\n" for record in sorted(raw_records, key=lambda item: str(item["file"]))).encode("utf-8")
    manifest = {
        "manifest_id": VERSION,
        "status": "IMMUTABLE C04-A DESCENDANT — V1 INNER DEVELOPMENT ONLY",
        "ancestry": {"dataset": "CORE-DATASET-FREEZE-V1", "root_fingerprint": "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616"},
        "retrieval_time_utc": retrieval_time,
        "source_contract": ["SSE_OFFICIAL_HISTORICAL_ACTION_TABLES", "SZSE_OFFICIAL_MONTHLY_ACTION_TABLES"],
        "calendar_scope": {"first_archive_period": START_PERIOD, "last_archive_period": END_PERIOD, "empirical_role": "2013-2014 formation reserve plus 2015-2019 inner development only"},
        "universe_security_count": len(universe),
        "raw_artifact_count": len(raw_records),
        "raw_artifact_root_sha256": sha256(raw_root_material),
        "raw_artifacts": raw_records,
        "normalized_action_rows": len(actions),
        "normalized_action_calendar": {"file": action_path.relative_to(ROOT).as_posix(), "bytes": len(action_bytes), "sha256": sha256(action_bytes)},
        "exclusion_rows": len(exclusions),
        "exclusion_calendar": {"file": exclusion_path.relative_to(ROOT).as_posix(), "bytes": len(exclusion_bytes), "sha256": sha256(exclusion_bytes)},
        "unresolved_effective_date_rows": unresolved_effective,
        "failures": failures,
        "semantic_states": ["IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED", "NO IDENTIFIED ACTION UNDER V1 CALENDAR"],
        "nonclaim": "NO IDENTIFIED ACTION UNDER V1 CALENDAR != AUTHORITATIVELY ACTION-CLEAN",
        "core_c04_state_mutated": False,
        "adjusted_price_constructed": False,
        "validated": not failures and len(exclusions) > 0,
    }
    manifest_bytes = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    (RAW_DIR / "manifest.json").write_bytes(manifest_bytes)
    (DERIVED_DIR / "manifest.json").write_bytes(manifest_bytes)
    PUBLIC_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC_MANIFEST.write_bytes(manifest_bytes)
    print(json.dumps({
        "manifest_id": VERSION,
        "validated": manifest["validated"],
        "raw_artifacts": len(raw_records),
        "actions": len(actions),
        "exclusions": len(exclusions),
        "unresolved_effective_dates": unresolved_effective,
        "failures": len(failures),
        "manifest_sha256": sha256(manifest_bytes),
    }, ensure_ascii=False))
    if not manifest["validated"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
