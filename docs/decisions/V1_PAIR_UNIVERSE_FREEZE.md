# V1 Candidate Pair Universe Freeze

Decision date: 2026-09-14

Status: **APPROVED / FROZEN — PAIR-A COMPLETE PIT ALL-PAIRS**

## Candidate-universe semantics

`membership in the candidate-pair universe != evidence that a valid economic/statistical relationship exists`.

PAIR-A determines only which contemporaneously PIT-eligible securities may be evaluated. Relationship existence, quality, admissibility, and advancement remain governed by the frozen R0/R1/R3/R4, CS2, and SR0-to-SR1 protocols.

## PIT construction

At every authorized origin, construct the security set using only the C06 snapshot genuinely available at that origin, its taxonomy/version and staleness state, the frozen machinery scope codes `34 + 35`, SSE/SZSE identity lineage, and candidate-specific structural eligibility. Current membership may never backfill a historical origin.

Form every unordered pair `{i,j}` from that contemporaneously eligible security set. Code `34` and code `35` may pair across codes; identical C06 code is structural context only, not an eligibility condition.

For every eligible unordered pair, preserve two separate directional response channels, `i -> j` and `j -> i`. Directions are not independent pair identities. The frozen directional-vector and equal-pair aggregation semantics remain binding.

## No screening

`candidate-universe construction != relationship screening`.

No correlation, distance, Top-K, cointegration, model-performance, pair-availability, or outcome-dependent screen may precede relationship evaluation. Realized pair counts may be recorded only after this freeze and may not be used to revise it.

## Engineering boundary

Vectorization, batching, caching, shared sufficient statistics, safe parallel computation, and deterministic checkpointing are authorized only when they preserve exact PAIR-A membership and numerical semantics. Computational burden does not authorize pair reduction. If exact execution is infeasible despite engineering optimization, stop before approximation or screening.

Dependency-ordered multiplicity and CS2 common/native-support rules are unchanged. Candidate-universe size is not a winner-selection criterion.

## Alternatives

- `PAIR-B — NOT SELECTED FOR V1`; future/V2 only.
- `PAIR-C — NOT SELECTED FOR V1`; future/V2 only.

Neither alternative may rescue V1 outcomes or computational burden without explicit protocol reopening and contamination governance.

## Execution boundary

This freeze resolves the pair-universe blocker and authorizes resumption of the already-frozen Phase 1 pipeline using only 2013–2014 formation reserve and 2015–2019 inner-development roles. OF4 2020–2023 and held-out 2024–2025 remain denied.

`PAIR-A COMPLETE PIT ALL-PAIRS — APPROVED / FROZEN FOR V1`
