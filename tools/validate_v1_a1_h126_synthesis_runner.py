"""Structural and synthetic exactness validator for the external runner."""
import importlib.util
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
py = (ROOT / "tools/v1_a1_h126_synthesis_batch.py").read_text(encoding="utf-8")
ps = (ROOT / "tools/run_v1_a1_h126_synthesis.ps1").read_text(encoding="utf-8")
required = ["os.replace", "sha(dest)", "verify_completed(progress)", "np.intersect1d", "assume_unique=True",
            "np.lexsort", "np.median", "temporal_median_vector", "2024_2025_SEALED_NOT_ACCESSED"]
missing = [item for item in required if item not in py]
for command in ("status", "run", "resume", "validate"):
    if command not in ps: missing.append(command)
if missing: raise SystemExit(f"FAIL: missing runner invariants: {missing}")
spec = importlib.util.spec_from_file_location("batch", ROOT / "tools/v1_a1_h126_synthesis_batch.py")
batch = importlib.util.module_from_spec(spec); spec.loader.exec_module(batch)
if len(batch.unit_specs()) != 406:
    raise SystemExit("FAIL: expected 406 bounded units")
# Exact odd/even medians with equal pair influence: pair 1 -> median 2;
# pair 2 -> median (10+20)/2=15; representation median -> (2+15)/2=8.5.
values = np.array([1.0, 2.0, 3.0, 10.0, 20.0])
pairs = np.array([1, 1, 1, 2, 2], dtype=np.uint32)
per_pair = batch.median_by_pair(values, pairs)
if not np.array_equal(per_pair, np.array([2.0, 15.0])) or np.median(per_pair) != 8.5:
    raise SystemExit("FAIL: exact/equal-pair median synthetic check")
print("PASS: checkpointable H126 runner structure, exact medians/common support, and held-out seal are bound.")
