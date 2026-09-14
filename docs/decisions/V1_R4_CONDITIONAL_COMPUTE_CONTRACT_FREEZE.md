# V1 R4 Conditional Compute Contract Freeze

Decision date: 2026-09-14
Contract ID: `V1-R4-CF-A-CF-B-1.0`
Status: **APPROVED / FROZEN BEFORE BENCHMARK OR EMPIRICAL ACCESS**

## CF-A primary path

Preserve complete PIT PAIR-A and `R4-RW`. Latent-state filtering uses U1D: predict before the response, evaluate, then update only for the next decision. Pair-direction-specific `Q/R` prediction-error PIT-ML is re-estimated only on the first candidate-eligible exchange session of each calendar month using H63 information available strictly before that monthly origin. The resulting `Q/R` version is carried forward deterministically until the next authorized monthly origin.

`state-update cadence != hyperparameter-estimation cadence`.

Matched-static initialization, eligible-session state time, explicit converged boundary states, single optimizer path, no smoothing, and every EXEC-A numerical-integrity rule remain frozen. No Top-K, sampling, PAIR-A reduction, lower-frequency state updates, result-driven pair removal, performance-driven Q/R change, or alternative dynamic family is authorized.

## Synthetic engineering benchmark gate

Before any full R4 execution, use only structural pair/origin counts and synthetic kernels to record monthly pair-direction fit count, optimization evaluations, state steps, projected wall time, peak memory, output storage, and checkpoint geometry. Test semantics-preserving vectorization, batching, shared operations, available compiled kernels, deterministic caching, safe parallelism, and restart.

CF-A passes only if the measured conservative projection fits within the remaining V1 deadline on the available environment with restart margin. Runtime/resource feasibility alone controls this decision; model results are prohibited inputs.

## Pre-authorized CF-B fallback

If CF-A fails the benchmark, set R4 to `V1 COMPUTATION-DEFERRED / V2`, preserve its scientific registration and frozen contracts, and execute V1 with R0/R1/R3. Deferral is not evidence against dynamic relationships. No further researcher approval is required for this computational fallback.

`computational infeasibility may reduce the executed V1 model set, but may not silently alter the scientific definition of an executed model`.

OF4 2020–2023 and held-out 2024–2025 remain inaccessible.

`V1-R4-CF-A-CF-B-1.0 — APPROVED / FROZEN`
