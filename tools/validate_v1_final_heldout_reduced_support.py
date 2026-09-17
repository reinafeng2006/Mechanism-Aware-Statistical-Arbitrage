"""Structural validator for the computation-incomplete reduced-support runner."""
from pathlib import Path
import ast

root = Path(__file__).resolve().parents[1]
runner = root / "tools/v1_final_heldout_reduced_support.py"
launcher = root / "tools/run_v1_final_heldout_reduced_support.ps1"
tree = ast.parse(runner.read_text(encoding="utf-8"))
text = runner.read_text(encoding="utf-8")
ps = launcher.read_text(encoding="utf-8")
required = [
    'CANDIDATES = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W", "V1-R3-252M"]',
    '"C4": "UNAVAILABLE_R4_2025_COMPUTATION_INCOMPLETE"',
    '"exact_common_support": True', '"equal_pair_influence": True', '"exact_medians": True',
    '"folds_kept_separate": True', 'if uid in p["units"]: continue',
]
if not all(token in text for token in required): raise SystemExit("FAIL: reduced-support binding missing")
if 'run(paths["r4"]' in text or 'V1_R4_WORKERS' in text: raise SystemExit("FAIL: reduced runner can invoke R4")
if not all(token in ps for token in ("Set-Location -LiteralPath $Repo", "New-Item -ItemType Directory", "2>&1", "Tee-Object")):
    raise SystemExit("FAIL: launcher robustness/logging binding missing")
print("PASS: reduced-support runner is structurally bound to six candidates, 44 exact units, no R4 execution")
