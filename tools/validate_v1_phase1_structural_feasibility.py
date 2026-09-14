"""Validate the public structural-feasibility manifest against its ignored report."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/manifests/V1_PHASE1_STRUCTURAL_FEASIBILITY.json"
REPORT = ROOT / "data/qa_work/v1/phase1/structural_feasibility_v1.json"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    actual_hash = hashlib.sha256(REPORT.read_bytes()).hexdigest().upper()
    checks = [
        actual_hash == manifest["source_report_sha256"],
        report["inner_totals"]["candidate_pair_dates"] == manifest["inner_geometry"]["candidate_pair_dates"],
        report["r4_required_pair_direction_daily_ml_fits"] == manifest["r4_geometry"]["required_pair_direction_daily_ml_fits"],
        report["r4_minimum_kalman_state_steps_per_likelihood_sweep"] == manifest["r4_geometry"]["minimum_kalman_state_steps_per_single_likelihood_sweep"],
        report["scope"].endswith("no prices, returns, fits, outcomes, OF4, or held-out"),
        manifest["pair_screening_performed"] is False,
    ]
    if not all(checks):
        raise SystemExit("V1 structural-feasibility manifest mismatch")
    print(json.dumps({"manifest_id": manifest["manifest_id"], "sha256": actual_hash,
                      "candidate_pair_dates": report["inner_totals"]["candidate_pair_dates"],
                      "r4_daily_ml_fits": report["r4_required_pair_direction_daily_ml_fits"],
                      "result": "PASS"}))


if __name__ == "__main__":
    main()
