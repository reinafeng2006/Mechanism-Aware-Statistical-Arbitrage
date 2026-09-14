"""Validate the immutable, ignored V1 inner-input artifact without revealing values."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/manifests/V1_PHASE1_INNER_INPUT.json"


def main() -> None:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    artifact = ROOT / m["artifact"]
    actual = hashlib.sha256(artifact.read_bytes()).hexdigest().upper()
    checks = [
        m["manifest_id"] == "V1-PHASE1-INNER-INPUT-1.0",
        actual == m["artifact_sha256"],
        m["dates"]["first"] == "20130107",
        m["dates"]["last"] == "20191231",
        m["core_fingerprint"] == "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616",
        m["of4_accessed"] is False,
        m["held_out_accessed"] is False,
        m["pair_screening"] is False,
    ]
    if not all(checks):
        raise SystemExit("V1 inner-input manifest mismatch")
    print(json.dumps({"manifest_id": m["manifest_id"], "artifact_sha256": actual,
                      "result": "PASS", "values_disclosed": False}))


if __name__ == "__main__":
    main()
