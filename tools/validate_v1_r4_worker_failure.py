"""Synthetic-only abrupt-worker propagation test for the R4 pool wrapper."""
from __future__ import annotations

import concurrent.futures
import time

import v1_phase1_inner_r4 as r4


def main() -> None:
    started = time.monotonic()
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
            r4.run_fit_tasks(pool, [None, None], "synthetic/non-scientific", r4.synthetic_abrupt_worker_exit)
    except RuntimeError as exc:
        elapsed = time.monotonic() - started
        if "R4 worker failure" not in str(exc) or elapsed > 30:
            raise RuntimeError("abrupt-worker failure was not propagated promptly") from exc
        print(f"PASS: synthetic abrupt worker exit propagated explicitly in {elapsed:.2f}s; scientific units executed=0.")
        return
    raise RuntimeError("synthetic abrupt worker exit did not fail")


if __name__ == "__main__":
    main()
