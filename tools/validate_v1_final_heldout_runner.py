"""Non-empirical structural validator for the final held-out external runner."""
from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "tools/v1_final_heldout_batch.py"
LAUNCHER = ROOT / "tools/run_v1_final_heldout.ps1"
MATERIALIZER = ROOT / "tools/v1_of4_materialize.py"
DECISION = ROOT / "docs/decisions/V1_FINAL_HELDOUT_CONFIRMATORY_FREEZE.md"

for path in (BATCH, LAUNCHER, MATERIALIZER, DECISION):
    if not path.is_file():
        raise RuntimeError(f"missing held-out runner component: {path}")
ast.parse(BATCH.read_text(encoding="utf-8"))
ast.parse(MATERIALIZER.read_text(encoding="utf-8"))
batch = BATCH.read_text(encoding="utf-8")
launcher = LAUNCHER.read_text(encoding="utf-8")
decision = DECISION.read_text(encoding="utf-8")
required_batch = (
    'choices=("status", "run", "resume", "validate", "dry-run")',
    'access_event()', 'held_out_accessed": True', 'os.link(temp, ACCESS)',
    'FOLDS = ["2024", "2025"]', 'len(specs) != 58',
    'V1-R0L-126W", "V1-R1M-126W', 'V1-R1M-126W", "V1-R1MI-126W',
    'V1-R0D-252M", "V1-R3-252M', 'V1-R0L-126W", "V1-R4-63D',
    'V1_NON_ESTIMABLE_NOT_EXECUTED', 'NOT_FORCED',
)
for token in required_batch:
    if token not in batch:
        raise RuntimeError(f"held-out runner contract token missing: {token}")
for token in ("status","run","resume","validate","FINAL_HELDOUT_V1","RedirectStandardError","Exception.ToString()"):
    if token not in launcher:
        raise RuntimeError(f"launcher contract token missing: {token}")
for token in ("C1 market-adjustment", "C2 industry-adjustment", "C3 hierarchical-pooling", "C4 dynamic-adaptation",
              "No p-value", "A6/G5 = V1 NON-ESTIMABLE / NOT EXECUTED"):
    if token not in decision:
        raise RuntimeError(f"confirmatory freeze token missing: {token}")
print("PASS: final held-out access guard, frozen bindings, 58-unit synthesis, launcher, and no-ranking boundary are structurally valid.")
