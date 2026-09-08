# G3B-QA — Bounded Formal Acquisition & Structural Validation Slice

Status: **AUTHORIZED / ACTIVE — BOUNDED STRUCTURAL QA ONLY**

## Deterministic slice rule

Build the slice without prices, returns or sample-count optimization:

1. From the frozen C06 primary codes 34/35, take the lexicographically first two resolvable securities per venue in the earliest qualified snapshot and the latest approved complete-period snapshot.
2. Add the lexicographically first primary-universe security per venue exhibiting each metadata-only technical condition available in source contracts: listing/delisting, suspension, corporate action and identifier change.
3. Add one approved benchmark/index identity required by E03 and its documented membership/weight records.
4. Deduplicate by stable C01 security ID. Preserve the selection manifest and reason code for every row.

If a condition cannot be established without unapproved data or outcome inspection, mark it `NOT TESTABLE IN CURRENT QA` rather than substituting another rule.

## Permitted validations

Physical fields, schema/row semantics, timestamps, PIT/vintage behavior, identifiers, adjustment lineage, C06 joins, missingness, explicit fallback behavior, immutable snapshots/checksums/manifests, deterministic regeneration and input/outcome quarantine.

## Prohibited computations

No pair selection/rank/validity; correlation, distance or cointegration research outputs; abnormality; UR/MP/R measurements; mechanism beliefs; resolution targets; predictions; portfolio metrics or PnL.

## Required checkpoint

Return contract-by-contract PASS/FAIL, exact source/field maps, PIT validation, identifier/universe validation, action/adjustment validation, coverage/missingness, immutable hash validation, blockers/amendments and structural readiness. Stop before full-universe expansion.
