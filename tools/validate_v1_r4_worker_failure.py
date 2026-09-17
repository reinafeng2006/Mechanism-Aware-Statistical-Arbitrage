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
        pass
    else:
        raise RuntimeError("synthetic abrupt worker exit did not fail")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
            one = pool.submit(r4.synthetic_abrupt_worker_exit, None)
            two = pool.submit(r4.synthetic_abrupt_worker_exit, None)
            r4.await_block_futures(pool, [(0, None, None, None, one, None, None), (1, None, None, None, two, None, None)], "synthetic/checkpointed")
    except RuntimeError as exc:
        total = time.monotonic() - started
        if not any(token in str(exc) for token in ("R4 worker failure", "R4 worker terminated")) or total > 30:
            raise RuntimeError("checkpointed abrupt-worker failure was not propagated promptly") from exc
        print(f"PASS: legacy and checkpointed abrupt worker exits propagated explicitly in {total:.2f}s; scientific units executed=0.")
        return
    raise RuntimeError("synthetic abrupt worker exit did not fail")


if __name__ == "__main__":
    main()
