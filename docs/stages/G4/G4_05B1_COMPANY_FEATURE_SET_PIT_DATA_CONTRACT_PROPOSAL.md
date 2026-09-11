# G4-05B1 Company Feature Set & PIT Data Contract Freeze

Status: **APPROVED / FROZEN — 2026-09-11**
Boundary: construct and data-contract preregistration only. No frozen-data inspection, acquisition, feature computation, fitting, or outcome access.

## Objective

Define a small economic information set that R2 may later use before selecting or fitting its equations. The registry proceeds from construct to raw variable to authorized pair transformation to model role; none of these layers implies the next.

`construct != raw variable != pair transformation != model role`.

`variable availability != automatic model inclusion`.

## Bounded construct and raw-variable shortlist

Each construct has one proposed primary raw variable and at most one robustness alternative. “Raw variable” means the logical source field before pair transformation; exact physical field names remain source-contract work.

| ID / construct | Primary raw variable | One robustness alternative | Economic rationale | Expected R2 relationship role | P0/P1 | Core-data readiness |
|---|---|---|---|---|---|---|
| `FS-SCALE` Scale | PIT total market capitalization | PIT total assets | firm scale may condition transmission strength, common exposure, and response level | company state; pair difference/similarity; slope conditioner | P1 when used to claim company-state increment | market-cap input: `AVAILABLE WITH DOCUMENTED LIMITATION` through E02-B lineage; total assets: `REQUIRES VERSIONED P1 ENHANCEMENT DATA` |
| `FS-PROF` Profitability / quality | return on assets derived from PIT profit and asset fields | operating margin derived from PIT operating profit and revenue | operating quality may modify how shared news maps across economically linked firms | company state; pair difference/similarity; intercept or slope conditioner; rival context | P1 | `REQUIRES VERSIONED P1 ENHANCEMENT DATA` |
| `FS-LEV` Leverage / capital structure | total liabilities / total assets | debt / equity | balance-sheet leverage may change exposure amplification and asymmetry | company state; signed/absolute pair difference; slope conditioner; rival context | P1 | `REQUIRES VERSIONED P1 ENHANCEMENT DATA` |
| `FS-GROW` Growth | PIT year-over-year operating revenue growth | PIT year-over-year operating profit growth | differing operating trajectories may weaken or strengthen expected pair transmission | company state; pair difference/similarity; intercept or slope conditioner | P1 | `REQUIRES VERSIONED P1 ENHANCEMENT DATA` |
| `FS-VAL` Valuation | book-to-market from PIT book equity and market capitalization | earnings yield from PIT earnings and market capitalization | relative valuation state may condition response level or sensitivity but is not pair validity | company state; signed/absolute pair difference; similarity; bounded slope conditioner | P1 | `REQUIRES VERSIONED P1 ENHANCEMENT DATA`; market numerator alone is available only with E02-B limitations |
| `FS-LIQ` Liquidity / trading structure | daily transaction amount | daily share volume | observable activity may condition response transmission and trading-friction state | P0 company/market state; pair difference/similarity; slope conditioner; rival context | P0 for existing qualified E02 information; no incremental P1 claim from re-expression | `AVAILABLE IN FROZEN CORE` for raw E02-A observations, subject to candidate eligibility and later state-construction rule |
| `FS-STRUCT` Business / subindustry structural information | dated C06 industry/subindustry code | separately qualified directed business/exposure linkage | common structure may define shared context or explain heterogeneous pair response | pair similarity; pooling prior; slope conditioner; rival/rejection context | C06 shared industry context is P0; additional company/economic linkage is P1 | C06 code: `AVAILABLE WITH DOCUMENTED LIMITATION`; directed business linkage: `NOT CURRENTLY QUALIFIED` |

The readiness classifications rely only on the frozen dataset contract: `CORE-DATASET-FREEZE-V1` binds C01/C03/C06/E02/E03-A and documented limitations, not a PIT-vintaged fundamentals layer. No row-level availability or distribution has been inspected.

## Authorized pair-transformation registry

Only transformations marked below enter the bounded proposal. Blank cells are not authorized; adding one requires protocol amendment before outcomes.

| Construct | i level | j level | Signed `i-j` difference | Absolute difference | Similarity | Interaction with source response | Intended role boundary |
|---|---:|---:|---:|---:|---:|---:|---|
| Scale | yes | yes | yes | no | yes | yes, source-scale only | levels/intercept; signed difference/similarity for heterogeneity; interaction for transmission |
| Profitability / quality | yes | yes | yes | no | yes | no | state/intercept and directed difference; no automatic slope interaction |
| Leverage / capital structure | yes | yes | yes | yes | no | yes, source leverage only | amplification/asymmetry and mismatch |
| Growth | yes | yes | yes | no | yes | no | state/intercept and trajectory alignment |
| Valuation | no | no | yes | yes | yes | no | relative state only; standalone valuation-level return prediction is outside the R2 estimand |
| Liquidity / trading structure | yes | yes | yes | yes | no | yes, source-liquidity state only | activity/friction state and response conditioning; no exogenous-pressure interpretation |
| Business / subindustry structure | no | no | no | no | yes, taxonomy/version aware | yes only for separately justified linkage strength | shared-context/similarity or directed transmission; code arithmetic prohibited |

“Similarity” requires a construct-specific formula; it is not automatically the negative absolute difference. Levels and differences must retain direction. A feature interaction means only `registered state x source response`; arbitrary feature-feature interactions are not authorized.

`raw variable != automatically authorized transformation`.

## Per-feature PIT and vintage contract

Every realized feature record must contain:

- stable security identity and historical code linkage;
- logical/physical field and transformation version;
- observation or fiscal period;
- true first-public time and system available time;
- source, source vintage, retrieval artifact, and upstream IDs;
- original and, if later revised, superseding vintage values without overwrite;
- update event/cadence and last genuine information-arrival time;
- carry-forward basis, feature age, and explicit staleness state;
- missingness reason/state and mathematical-quality state;
- permitted P0/P1 and Feature Role bindings.

Fiscal-period end never substitutes for first-public or available time. A restatement becomes a new later vintage and cannot rewrite earlier decision states. Retrieval time is provenance, not historical availability.

## Slow-state update and carry-forward

At decision time `t`, a slow company state may use only the latest qualifying vintage whose `available_time <= t`. Between genuine releases it may be carried forward with unchanged vintage ID and increasing age. Carry-forward is not a new observation, evidence event, or daily update:

`PIT carry-forward != daily information update`.

The state must remain accompanied by feature age and staleness metadata. No numerical staleness cutoff is proposed. Missing or nonqualified state is explicit; future reports, later-restated values, silent cross-sectional fills, and retrieval-time substitution are prohibited.

## Frozen-core and P1 enhancement architecture

`CORE-DATASET-FREEZE-V1` is immutable. New fundamental/company records must form a separately versioned P1 enhancement layer with:

`core freeze ID -> P1 enhancement version -> immutable raw manifests -> PIT-aligned feature records -> authorized R2 feature-set version`.

The enhancement layer records ancestry to the core but does not mutate, overwrite, or re-freeze it. C04/C05/C06, identifier, source, and outcome-quarantine controls continue to propagate.

Company-feature missingness may reduce R2-P1 native support, but it must not silently alter the complete P0 baseline sample. CS2 requires P0/P1 attribution on their common eligible pair/date support and separate reporting of P0 native support, P1 native support, and support lost because P1 is unavailable.

`P1 = complete matched P0 + separately tracked company/economic information`.

## Construct-level Search Budget registry

This registry stops before estimator and H/U multiplication. Each line is one authorized construct/variable/transformation/role bundle; robustness variables do not execute unless separately approved.

| Bundle ID | Construct and primary variable | Authorized transformation bundle | Authorized R2 role |
|---|---|---|---|
| `B1-SCALE` | total market capitalization | i level, j level, signed difference, similarity, source-level interaction | state/intercept and slope conditioning |
| `B1-PROF` | ROA | i level, j level, signed difference, similarity | state/intercept conditioning |
| `B1-LEV` | liabilities/assets | i level, j level, signed difference, absolute difference, source-level interaction | state, mismatch, and slope conditioning |
| `B1-GROW` | revenue growth | i level, j level, signed difference, similarity | state/intercept conditioning |
| `B1-VAL` | book-to-market | signed difference, absolute difference, similarity | relative-state conditioning only |
| `B1-LIQ-P0` | transaction amount | i level, j level, signed difference, absolute difference, source-state interaction | P0 activity/friction context only; not an incremental P1 bundle |
| `B1-STRUCT-P0` | C06 dated code | taxonomy-aware similarity | shared context / pooling only; not P1 increment |
| `B1-STRUCT-P1-DEFERRED` | directed business/exposure linkage | similarity and linkage-by-source-response only | P1 economic linkage; not qualified and excluded from the initial R2 computation Search Budget |

The initial P1 fundamental Search Budget is bounded to `B1-SCALE`, `B1-PROF`, `B1-LEV`, `B1-GROW`, and `B1-VAL`. It retains their documented authorized transformations, one primary raw variable, and at most one robustness alternative. Robustness alternatives cannot enter the primary vector beside their primary variable without separate authorization. `B1-LIQ-P0` and `B1-STRUCT-P0` are context bundles, not P1 increments. `B1-STRUCT-P1-DEFERRED` is outside the initial computation Search Budget.

The registry does not authorize every line in one model, all subsets, or any combination with R2-L/R/N, estimator, H, U, or N0/N1. The final feature-set decision must name a small bundle set before those later axes are attached. New constructs after outcome inspection require explicit protocol reopening and contamination recording.

## Required P1 enhancement-data gaps

1. PIT-vintaged balance-sheet fields for assets, liabilities, equity, and applicable debt definitions;
2. PIT-vintaged income/cash-flow fields for profitability, margins, earnings quality, revenue, and operating profit;
3. defensible first-public/available timestamps and revision/restatement lineage for every filing value;
4. validated derived-ratio denominator and non-finite-state rules;
5. market-cap/share-capital vintage limitations needed for scale and valuation;
6. any business/exposure linkage source with dated availability and version lineage.

These are data contracts only. No acquisition is authorized.

## Unresolved decisions

1. choose the minimal subset/composition of the five frozen P1 construct bundles for the final primary R2 vector;
2. define exact logical fields, units, accounting basis, and derived-ratio formulas;
3. define each similarity function and directional sign convention;
4. decide whether documented authorized interactions have sufficient economic ancestry for a concrete R2 equation;
5. specify feature-age reporting and whether any later staleness boundary has independent justification;
6. qualify and separately authorize the P1 fundamentals source/vintage contract and acquisition amendment;
7. define missing-feature eligibility without changing the P0 baseline sample;
8. bind frozen bundles to R2 complexity levels, equations, and finite estimator/H/U tuples;
9. decide which robustness alternatives, if any, enter a later sensitivity budget.

The five core P1 fundamental constructs require a separately versioned `P1 FUNDAMENTALS ENHANCEMENT LAYER` before R2 computation. This layer must preserve ancestry to immutable `CORE-DATASET-FREEZE-V1` and satisfy the frozen PIT/vintage/restatement/staleness contracts. B1 freezing does not authorize acquisition or computation; R2 remains unfrozen.

`G4-05B1 COMPANY FEATURE & PIT DATA CONTRACT APPROVED / FROZEN`
