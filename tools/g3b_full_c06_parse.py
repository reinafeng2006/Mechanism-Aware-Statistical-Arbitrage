"""Parse only frozen C06 codes 34/35 from an acquired official archive run."""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data" / "qa_work" / "python_packages"))


def normalized_code(value: object) -> str | None:
    text = str(value).strip()
    match = re.fullmatch(r"(\d{6})(?:\.0)?", text)
    return match.group(1) if match else None


def parse_excel(path: Path) -> set[tuple[str, str]]:
    import pandas as pd
    rows: set[tuple[str, str]] = set()
    engine = "xlrd" if path.suffix.lower() == ".xls" else "openpyxl"
    for sheet in pd.ExcelFile(path, engine=engine).sheet_names:
        frame = pd.read_excel(path, sheet_name=sheet, header=None, dtype=object, engine=engine)
        inherited: str | None = None
        for values in frame.itertuples(index=False, name=None):
            strings = [str(v).strip() for v in values if str(v) != "nan"]
            for value in strings:
                if re.fullmatch(r"(?:C)?\d{2}(?:\.0)?", value, re.I):
                    inherited = re.sub(r"\D", "", value)[:2]
                    break
            codes = [normalized_code(v) for v in values]
            security = next((c for c in codes if c), None)
            if security and inherited in {"34", "35"}:
                rows.add((security, inherited))
    return rows


def parse_pdf(path: Path, label: str) -> set[tuple[str, str]]:
    from pypdf import PdfReader
    rows: set[tuple[str, str]] = set()
    text = "\n".join((page.extract_text() or "") for page in PdfReader(path).pages)
    if "股票代码" in label:
        blocks = re.split(r"(?=^\s*\d{6}\b)", text, flags=re.M)
        for block in blocks:
            match = re.match(r"\s*(\d{6})\b", block)
            if not match:
                continue
            industry = re.findall(r"(?:^|\s)(34|35)(?:\s|$)", block)
            if industry:
                rows.add((match.group(1), industry[-1]))
        return rows
    # Older industry-sorted PDFs print an industry code once, followed by many
    # security-only continuation rows. Preserve that table state explicitly.
    current_industry: str | None = None
    for line in text.splitlines():
        if not re.match(r"\s*\d{6}\b", line):
            industry_only = re.findall(r"(?:^|\s)(\d{2})(?:\s|$)", line)
            if industry_only:
                current_industry = industry_only[-1]
        header = re.search(r"(?:^|\s)(\d{2})\s+.*?\b(\d{6})\b", line)
        if header:
            current_industry = header.group(1)
            if current_industry in {"34", "35"}:
                rows.add((header.group(2), current_industry))
            continue
        continuation = re.match(r"\s*(\d{6})\b", line)
        if continuation and current_industry in {"34", "35"}:
            rows.add((continuation.group(1), current_industry))
    return rows


def parse_word_text(path: Path) -> set[tuple[str, str]]:
    rows: set[tuple[str, str]] = set()
    current_industry: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = raw.replace("\x07", "").strip()
        if re.fullmatch(r"\d{2}", value):
            current_industry = value
        elif re.fullmatch(r"\d{6}", value) and current_industry in {"34", "35"}:
            rows.add((value, current_industry))
    return rows


def parse_docx(path: Path) -> set[tuple[str, str]]:
    rows: set[tuple[str, str]] = set()
    with zipfile.ZipFile(path) as archive:
        text = archive.read("word/document.xml").decode("utf-8", errors="replace")
    text = re.sub(r"<[^>]+>", " ", text)
    for match in re.finditer(r"\b(\d{6})\b(.{0,250}?)(?:\bC?(34|35)\b)", text, re.S | re.I):
        rows.add((match.group(1), match.group(3)))
    return rows


def publication_date(url: str) -> str | None:
    match = re.search(r"/(20\d{2})(\d{2})/(?:20\d{6}/)?j_(20\d{6})", url)
    if match:
        d = match.group(3)
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}"
    match = re.search(r"/(20\d{2})(\d{2})/(20\d{2})(\d{2})(\d{2})", url)
    if match:
        return f"{match.group(3)}-{match.group(4)}-{match.group(5)}"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id")
    args = parser.parse_args()
    run_dir = ROOT / "data" / "raw" / "g3b_full" / "c06" / args.run_id
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    grouped: dict[str, set[tuple[str, str]]] = defaultdict(set)
    evidence: dict[str, list[dict]] = defaultdict(list)
    failures: list[dict] = []
    for record in manifest["records"]:
        if record.get("kind") != "attachment" or record.get("status") != "OK":
            continue
        path = run_dir / record["file"]
        try:
            if path.suffix.lower() in {".xls", ".xlsx"}:
                parsed = parse_excel(path)
            elif path.suffix.lower() == ".pdf":
                parsed = parse_pdf(path, record.get("label") or "")
            elif path.suffix.lower() == ".docx":
                parsed = parse_docx(path)
            else:
                continue
            title = record.get("parent_title") or record.get("label") or path.name
            grouped[title].update(parsed)
            evidence[title].append({"file": record["file"], "sha256": record["sha256"], "rows_34_35": len(parsed), "source_url": record["url"]})
        except Exception as exc:
            failures.append({"file": record["file"], "error_type": type(exc).__name__})

    word_text = ROOT / "data" / "qa_work" / "g3b_full" / "c06" / args.run_id / "2012q4_word_text.txt"
    if word_text.exists():
        parsed = parse_word_text(word_text)
        grouped["2012年4季度上市公司行业分类结果"].update(parsed)
        evidence["2012年4季度上市公司行业分类结果"].append({"file": str(word_text.relative_to(ROOT)).replace("\\", "/"), "rows_34_35": len(parsed), "source_evidence": "read-only extraction from immutable official DOC attachment"})

    out_dir = ROOT / "data" / "qa_work" / "g3b_full" / "c06" / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for title in sorted(grouped):
        parent = next((r.get("parent") for r in manifest["records"] if r.get("kind") == "attachment" and r.get("parent_title") == title), "")
        for security, industry in sorted(grouped[title]):
            rows.append({"snapshot_title": title, "publication_date": publication_date(parent), "security_code": security, "industry_code": industry, "source_evidence": evidence[title]})
    (out_dir / "primary_membership.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows), encoding="utf-8")
    union = sorted({r["security_code"] for r in rows})
    (out_dir / "security_union.txt").write_text("\n".join(union), encoding="utf-8")
    report = {"run_id": args.run_id, "snapshot_titles_with_primary_rows": len(grouped), "membership_rows": len(rows), "union_securities": len(union), "parse_failures": failures, "snapshots": {k: len(v) for k, v in sorted(grouped.items())}}
    (out_dir / "parse_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
