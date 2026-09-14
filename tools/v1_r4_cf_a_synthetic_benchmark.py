"""Synthetic-only benchmark for frozen V1 R4 CF-A.

No repository research data is read. Structural workload counts are supplied from
the public feasibility manifest. The kernel implements the frozen scalar random-
walk-slope prediction-error likelihood and the single L-BFGS-B path.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import sys
import time
import tracemalloc
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DEPS = ROOT / "data/qa_work/v1/phase1/deps"
sys.path.insert(0, str(DEPS))
from scipy.optimize import minimize  # noqa: E402

STRUCTURE = ROOT / "data/qa_work/v1/phase1/structural_feasibility_v1.json"
OUT = ROOT / "data/qa_work/v1/phase1/r4_cf_a_synthetic_benchmark.json"


def nll(theta: np.ndarray, x: np.ndarray, y: np.ndarray, alpha: float, beta0: float, p0: float) -> float:
    q, r = float(theta[0]), float(theta[1])
    beta, p, loss = beta0, p0, 0.0
    for xt, yt in zip(x, y):
        pp = p + q
        innovation = yt - alpha - beta * xt
        variance = xt * xt * pp + r
        if not np.isfinite(variance) or variance <= 0:
            return np.inf
        loss += 0.5 * (np.log(2.0 * np.pi * variance) + innovation * innovation / variance)
        gain = pp * xt / variance
        beta += gain * innovation
        p = max(0.0, (1.0 - gain * xt) * pp)
    return float(loss)


def fit(seed: int) -> tuple[int, bool]:
    rng = np.random.default_rng(seed)
    x = rng.normal(0.0, 0.015, 63)
    beta = np.empty(63)
    beta[0] = 0.7
    for pos in range(1, 63):
        beta[pos] = beta[pos - 1] + rng.normal(0.0, 0.002)
    y = 0.0002 + beta * x + rng.normal(0.0, 0.008, 63)
    design = np.column_stack((np.ones(63), x))
    coef, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
    residual = y - design @ coef
    r0 = float(np.sum(residual * residual) / 61)
    xtx_inv = np.linalg.inv(design.T @ design)
    p0 = float(r0 * xtx_inv[1, 1])
    result = minimize(nll, np.array([0.01 * r0, r0]), args=(x, y, float(coef[0]), float(coef[1]), p0),
                      method="L-BFGS-B", bounds=((0.0, None), (0.0, None)),
                      options={"maxiter": 1000, "ftol": 1e-8})
    valid = bool(result.success and np.isfinite(result.fun) and np.all(np.isfinite(result.x)))
    return int(result.nfev), valid


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fits", type=int, default=1000)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    structure = json.loads(STRUCTURE.read_text(encoding="utf-8"))
    workload = int(structure["r4_cf_a_monthly_pair_direction_ml_fits"])
    tracemalloc.start()
    started = time.perf_counter()
    seeds = [90210 + pos for pos in range(args.fits)]
    if args.workers == 1:
        results = [fit(seed) for seed in seeds]
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
            results = list(pool.map(fit, seeds, chunksize=max(1, args.fits // (args.workers * 20))))
    elapsed = time.perf_counter() - started
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    nfev = [x[0] for x in results]
    fits_per_second = args.fits / elapsed
    projected_seconds_single_worker = workload / fits_per_second
    state_records = int(structure["r4_required_pair_direction_daily_ml_fits"])
    report = {
        "benchmark_id": "V1-R4-CF-A-SYNTHETIC-BENCHMARK-1.0",
        "inputs": "STRUCTURAL_COUNTS_PLUS_FIXED_SEED_SYNTHETIC_DATA_ONLY",
        "research_data_accessed": False,
        "synthetic_fits": args.fits,
        "elapsed_seconds": elapsed,
        "fits_per_second_single_process": fits_per_second,
        "benchmark_workers": args.workers,
        "optimizer_evaluations": {"median": float(np.median(nfev)), "mean": float(np.mean(nfev)), "max": int(max(nfev))},
        "valid_fit_fraction": float(np.mean([x[1] for x in results])),
        "monthly_pair_direction_ml_fits": workload,
        "projected_single_worker_seconds": projected_seconds_single_worker,
        "projected_single_worker_hours": projected_seconds_single_worker / 3600.0,
        "projected_ideal_parallel_hours": {str(n): projected_seconds_single_worker / 3600.0 / n for n in (2, 4, 8, 16)},
        "minimum_kalman_steps_per_likelihood_sweep": int(structure["r4_cf_a_minimum_kalman_state_steps_per_likelihood_sweep"]),
        "daily_pair_direction_state_records": state_records,
        "storage_projection_bytes": {
            "monthly_qr_at_64_bytes": workload * 64,
            "daily_state_at_64_bytes": state_records * 64,
            "checkpoint_overhead_not_included": True
        },
        "benchmark_peak_python_bytes": peak,
        "cpu_logical_count": os.cpu_count(),
        "restart_design": "MONTH_STRATUM_DIRECTION_PARTITIONS_WITH_CONTENT_HASH_AND_ATOMIC_COMPLETION_MARKER",
        "deadline_basis": "FIVE_CALENDAR_DAYS_FROM_2026_09_14_ACTIVATION; FULL_V1_PIPELINE_REQUIRES_MARGIN",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_hash = hashlib.sha256(OUT.read_bytes()).hexdigest().upper()
    print(json.dumps({"output": OUT.relative_to(ROOT).as_posix(), "sha256": report_hash,
                      "fits_per_second": fits_per_second, "median_nfev": report["optimizer_evaluations"]["median"],
                      "projected_single_worker_hours": report["projected_single_worker_hours"],
                      "cpu_logical_count": report["cpu_logical_count"]}))


if __name__ == "__main__":
    main()
