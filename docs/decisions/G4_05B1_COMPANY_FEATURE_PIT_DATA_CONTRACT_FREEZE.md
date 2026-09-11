# G4-05B1 Company Feature and PIT Data Contract Freeze

Decision date: 2026-09-11
Status: **APPROVED / FROZEN**

## Frozen construct set

The bounded primary P1 fundamental-information set contains exactly:

- Scale;
- Profitability / Quality;
- Leverage / Capital Structure;
- Growth;
- Valuation.

Each retains exactly one documented primary raw variable and at most one preregistered robustness alternative. Shared denominators, mechanical relationships, and conceptual overlaps remain explicit. A robustness alternative cannot enter the primary R2 feature vector beside its primary variable without separate authorization.

## P0 and deferred information

- existing qualified E02 liquidity/trading information remains P0 context; its re-expression or pair transformation is not incremental P1 information;
- C06 industry/subindustry information is frozen as `P0 — STRUCTURAL RELATIONSHIP CONTEXT`, including potential relationship-conditioning and hierarchical/pooling roles;
- directed business/supply-chain/structural linkage is `P1 — ECONOMICALLY RELEVANT / NOT CURRENTLY QUALIFIED`;
- directed linkage is excluded from the initial R2 computation Search Budget and cannot be approximated by C06; later admission requires separately qualified PIT linkage data.

## Data architecture and integrity

The five core fundamental constructs require a separately versioned `P1 FUNDAMENTALS ENHANCEMENT LAYER`. It must preserve explicit ancestry to immutable `CORE-DATASET-FREEZE-V1` and comply with all frozen PIT, vintage, restatement, carry-forward, staleness, missingness, identifier, and outcome-quarantine contracts.

`re-expression of existing P0 information != incremental P1 information`.

`P1 = complete matched P0 + separately tracked incremental company/economic information`.

The construct-level bundles and authorized transformations documented in B1 are frozen. New constructs after outcome inspection require protocol reopening and contamination recording.

This decision authorizes no acquisition, feature computation, R2 fitting, or R3 work.
