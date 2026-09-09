"""Acquire official C06 classification archive documents only.

Creates a new immutable run directory. It does not parse market outcomes or overwrite prior runs.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import html
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data" / "raw" / "g3b_full" / "c06"
INDEXES = [
    "https://www.csrc.gov.cn/csrc/c100103/common_list.shtml",
    "https://www.csrc.gov.cn/csrc/c100103/common_list_2.shtml",
    *[f"https://www.capco.org.cn/xhgg/hyfl/hyfljg/index{suffix}.html" for suffix in ("", "_1", "_2", "_3", "_4")],
]
UA = "MechanismAwareStatArb/1.0 research-data-acquisition"


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as response:
        return response.read()


def links(body: bytes, base: str) -> list[tuple[str, str]]:
    text = body.decode("utf-8", errors="replace")
    found = []
    for href, label in re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', text, re.I | re.S):
        label = html.unescape(re.sub(r"<[^>]+>", " ", label))
        label = re.sub(r"\s+", " ", label).strip()
        found.append((urljoin(base, html.unescape(href.strip())), label))
    return found


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def safe_name(url: str, prefix: str, data: bytes) -> str:
    name = Path(urlparse(url).path).name or "payload"
    if "." not in name:
        kind = data[:8]
        ext = ".pdf" if kind.startswith(b"%PDF") else ".zip" if kind.startswith(b"PK") else ".bin"
        name += ext
    return f"{prefix}__{hashlib.sha256(url.encode()).hexdigest()[:12]}__{name}"


def main() -> None:
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = BASE / run_id
    out.mkdir(parents=True, exist_ok=False)
    records: list[dict] = []
    detail_urls: dict[str, str] = {}

    for index_url in INDEXES:
        try:
            body = fetch(index_url)
            path = out / safe_name(index_url, "index", body)
            path.write_bytes(body)
            records.append({"kind": "index", "url": index_url, "file": path.name, "bytes": len(body), "sha256": sha(body), "status": "OK"})
            for url, label in links(body, index_url):
                year_match = re.search(r"20(?:1[2-9]|2[0-5])", label)
                if year_match and ("行业分类" in label or "classification" in label.lower()) and url.startswith("http"):
                    detail_urls[url] = label
        except Exception as exc:
            records.append({"kind": "index", "url": index_url, "status": "FAILED", "error_type": type(exc).__name__})

    attachment_urls: dict[str, dict] = {}
    def acquire_detail(detail_url: str) -> tuple[dict, list[tuple[str, str]]]:
        label = detail_urls[detail_url]
        try:
            body = fetch(detail_url)
            path = out / safe_name(detail_url, "detail", body)
            path.write_bytes(body)
            record = {"kind": "detail", "title": label, "url": detail_url, "file": path.name, "bytes": len(body), "sha256": sha(body), "status": "OK"}
            found = []
            for url, attachment_label in links(body, detail_url):
                if url.startswith("http") and not any(host in url for host in ("weibo.com", "gov.cn/english", "beian")):
                    low = url.lower()
                    if any(x in low for x in ("/files/", "sp.capco.org.cn", ".xls", ".xlsx", ".doc", ".docx", ".pdf", ".zip")):
                        found.append((url, attachment_label))
            return record, found
        except Exception as exc:
            return {"kind": "detail", "title": label, "url": detail_url, "status": "FAILED", "error_type": type(exc).__name__}, []

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(acquire_detail, url): url for url in sorted(detail_urls)}
        for future in as_completed(futures):
            record, found = future.result()
            records.append(record)
            for url, attachment_label in found:
                attachment_urls[url] = {"parent": record["url"], "parent_title": record["title"], "label": attachment_label}

    def acquire_attachment(item: tuple[int, str]) -> dict:
        i, url = item
        meta = attachment_urls[url]
        try:
            body = fetch(url)
            path = out / safe_name(url, f"attachment_{i:03d}", body)
            path.write_bytes(body)
            return {"kind": "attachment", **meta, "url": url, "file": path.name, "bytes": len(body), "sha256": sha(body), "status": "OK"}
        except Exception as exc:
            return {"kind": "attachment", **meta, "url": url, "status": "FAILED", "error_type": type(exc).__name__}

    with ThreadPoolExecutor(max_workers=6) as pool:
        records.extend(pool.map(acquire_attachment, enumerate(sorted(attachment_urls), 1)))

    records.sort(key=lambda r: (r.get("kind", ""), r.get("url", "")))

    manifest = {
        "manifest_id": "G3B-FULL-C06-OFFICIAL-ARCHIVE-V1",
        "status": "FORMAL RAW ACQUISITION — NON-EMPIRICAL",
        "run_id": run_id,
        "retrieval_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_classes": ["CSRC official", "CAPCO official"],
        "scope": "C06 official historical classification snapshots, 2012Q4–2025H2; primary codes parsed later as 34/35",
        "records": records,
    }
    manifest_path = out / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "run_id": run_id,
        "manifest": str(manifest_path.relative_to(ROOT)).replace("\\", "/"),
        "details_found": len(detail_urls),
        "attachments_found": len(attachment_urls),
        "successful_attachments": sum(r.get("kind") == "attachment" and r.get("status") == "OK" for r in records),
        "failures": sum(r.get("status") == "FAILED" for r in records),
    }))


if __name__ == "__main__":
    main()
