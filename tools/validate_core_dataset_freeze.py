"""Verify CORE-DATASET-FREEZE-V1 without computing any research statistic."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/manifests/CORE_DATASET_FREEZE_V1.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    freeze = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    lines = []
    for item in sorted(freeze["bound_artifacts"], key=lambda x: x["path"]):
        path = ROOT / item["path"]
        actual = sha(path) if path.exists() else None
        if actual != item["sha256"] or (path.exists() and path.stat().st_size != item["bytes"]):
            failures.append(item["path"])
        lines.append(f"{item['path']}\t{item['sha256']}\n")
    root_hash = hashlib.sha256("".join(lines).encode("utf-8")).hexdigest().upper()
    if root_hash != freeze["root_fingerprint"]["value"]:
        failures.append("root_fingerprint")
    sidecar_manifest = json.loads(
        (ROOT / "data/qa_work/g3b_f2/security_date_eligibility/v1/manifest.json").read_text(encoding="utf-8")
    )
    expected = freeze["sidecar"]
    checks = {
        "rows": sidecar_manifest["row_count"] == expected["rows"],
        "normal": sidecar_manifest["c05_state_counts"]["NORMAL TRADING OBSERVED"] == expected["normal_trading_observed"],
        "unknown": sidecar_manifest["c05_state_counts"]["UNKNOWN MISSINGNESS"] == expected["unknown_missingness"],
        "c04": sidecar_manifest["c04_state"] == expected["c04_state"],
        "no_universal_eligible": sidecar_manifest["universal_eligible_field"] is False,
    }
    failures.extend(name for name, passed in checks.items() if not passed)
    print(json.dumps({
        "freeze_id": freeze["freeze_id"],
        "bound_artifacts": len(freeze["bound_artifacts"]),
        "root_fingerprint": root_hash,
        "sidecar_checks": checks,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }, ensure_ascii=False))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
