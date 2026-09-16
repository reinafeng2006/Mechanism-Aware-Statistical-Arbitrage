"""Integrity-only validator for the H126 A1 layer; prints no scientific values."""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/manifests/V1_A1_H126_CANDIDATE_NEUTRAL.json"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> None:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    rows = 0
    for rec in m["records"]:
        path = Path(rec["physical_path"])
        if not path.exists() or sha(path) != rec["sha256"]:
            failures.append(str(path)); continue
        check = hashlib.sha256()
        with gzip.open(path, "rb") as stream:
            for chunk in iter(lambda: stream.read(8 << 20), b""):
                check.update(chunk)
        if check.hexdigest().upper() != rec["raw_sha256"]:
            failures.append(str(path)); continue
        rows += rec["rows"]
    if len(m["records"]) != 98 or failures or m["held_out"] != "2024_2025_SEALED_NOT_ACCESSED":
        raise SystemExit(json.dumps({"result": "FAIL", "failures": failures, "record_count": len(m["records"])}))
    print(json.dumps({"manifest_id": m["manifest_id"], "record_count": len(m["records"]), "rows": rows,
                      "result": "PASS", "values_disclosed": False, "held_out_accessed": False}))


if __name__ == "__main__":
    main()
