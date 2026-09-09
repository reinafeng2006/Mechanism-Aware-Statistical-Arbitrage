"""Acquire the bounded authoritative identity evidence for historical code 601313."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/raw/g3b_full/structural_resolution/601313_v1"
SOURCES = (
    ("CSRC_2013Q3_INDUSTRY_CLASSIFICATION", "https://www.csrc.gov.cn/csrc/c100103/c1452021/1452021/files/1616066710130_27835.pdf"),
    ("CNINFO_2018_CODE_CHANGE_ANNOUNCEMENT", "https://static.cninfo.com.cn/finalpage/2018-02-02/1204386750.PDF"),
)


def main() -> None:
    if OUT.exists():
        raise SystemExit("Immutable 601313 evidence directory already exists; refusing overwrite.")
    OUT.mkdir(parents=True)
    records = []
    for source_id, url in SOURCES:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0 G3B structural audit"})
        with urlopen(request, timeout=90) as response:
            body = response.read()
            content_type = response.headers.get("Content-Type")
        filename = f"{source_id}.pdf"
        (OUT / filename).write_bytes(body)
        records.append({"source_id": source_id, "url": url, "file": filename,
                        "retrieval_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                        "content_type": content_type, "bytes": len(body),
                        "sha256": hashlib.sha256(body).hexdigest().upper()})
    manifest = {"status": "FORMAL RAW STRUCTURAL-RESOLUTION EVIDENCE", "scope": "601313.SH only",
                "credential_recorded": False, "records": records}
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"records": len(records), "credential_recorded": False}))


if __name__ == "__main__":
    main()
