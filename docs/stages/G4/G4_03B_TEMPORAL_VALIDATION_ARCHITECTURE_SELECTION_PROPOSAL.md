# G4-03B Temporal Validation Architecture Selection Proposal

Status: **G4-03B PROPOSED / AWAITING RESEARCHER REVIEW**  
Boundary: architecture selection proposal only. No frozen-data inspection, statistic, measurement, target construction, or development access.

## Objective

Select the temporal-validation structure that will govern later development while preserving chronological information boundaries, dynamic-relationship assessment, selection separation, and a sealed final held-out evaluation. Exact dates, origin spacing, purge/embargo lengths, aggregation rules, and access authorization remain unresolved.

## TP0-TP3 comparison

| Candidate | Dynamic relationship stability | OOS robustness and selection control | Complexity/history burden | Proposed disposition |
|---|---|---|---|---|
| TP0 — single chronological development / sealed held-out | Weak: one development split gives limited evidence across relationship states | Weak-to-moderate: preserves a holdout but is sensitive to one development period | Lowest | Do not select as the primary architecture; retain only as a transparent sensitivity baseline |
| TP1 — rolling-origin development validation / sealed held-out | Strong: repeated chronological origins expose temporal variation | Strong if candidate menus, overlap controls, and aggregation are frozen | Moderate | Retain as the lower-complexity competing architecture |
| TP2 — nested temporal development / sealed held-out | Strongest selection separation: outer temporal evaluation tests stability while inner temporal development contains parameter choice | Strongest protection against reusing the same development evidence for tuning and comparison | Highest and consumes more history | **Proposed primary architecture**, subject to researcher approval and later numerical feasibility within the frozen date envelope |
| TP3 — prespecified regime/calendar strata / sealed held-out | Useful diagnostic view of known dated environments | Complementary only; strata do not replace chronological pseudo-OOS selection | Adds multiplicity and reporting burden | Use only as a prespecified diagnostic overlay on TP2, not as a standalone partition architecture |

## Proposed architecture selection

Select **TP2 with a TP3 diagnostic overlay**:

1. an inner time-ordered development loop may choose only among preregistered Search-Budget tuples;
2. an outer time-ordered development-validation loop evaluates fixed inner-loop choices across later origins;
3. one final held-out region remains sealed until separate authorization;
4. TP3 strata, if authorized, are dated ex ante and used only to report stability, not to redefine folds or add candidates;
5. TP1 remains the preregistered lower-complexity comparator for determining whether nesting adds necessary protocol value;
6. TP0 remains a sensitivity baseline and may not govern final candidate selection.

The proposal selects an architecture class, not numerical partitions. If later numerical design shows that TP2 cannot provide minimally adequate candidate-specific estimation, outer-validation, and sealed-held-out support within the frozen date envelope, the protocol must return for researcher decision; it must not silently collapse to TP1.

## Information-boundary and access rules

- Every origin uses only information with `available_time <= decision_time`.
- Inner-loop outputs cannot inspect outer-loop future observations; neither loop can inspect final held-out evidence.
- Outcome records are quarantined relative to their decision origins.
- Overlapping estimation windows or outcome horizons activate the structurally triggered purge/embargo analysis frozen in G4-03A.
- Eligibility, partition, candidate, and Search-Budget versions must be bound before development computation.
- Any development inspection, outer-validation inspection, or future held-out access must be logged under G4-02.

## Decisions preserved for later numerical protocol

- exact development, outer-validation, and held-out dates;
- rolling versus expanding history within each permitted representation contract;
- number and spacing of inner and outer origins;
- exact purge and embargo rules/lengths;
- target censoring at fold and partition boundaries;
- aggregation and stability summaries across origins;
- whether every candidate uses identical origins or candidate-specific eligible origins with explicit support reporting;
- the finite TP3 strata, if any;
- TP2-versus-TP1 adequacy decision rule;
- all development and held-out access authorizations.

## Classification

| Item | Proposed classification |
|---|---|
| Chronological nested development with sealed final held-out | **PROPOSED ARCHITECTURE SELECTION — TP2** |
| Prespecified regime/calendar reporting | **PROPOSED DIAGNOSTIC OVERLAY — TP3** |
| Rolling-origin non-nested structure | **COMPETING LOWER-COMPLEXITY ARCHITECTURE — TP1** |
| Single split | **SENSITIVITY BASELINE ONLY — TP0** |
| Dates, origins, purge/embargo, aggregation, strata | **G4 NUMERICAL DECISION — DEFER** |
| Development access | **NOT AUTHORIZED** |
| Held-out access | **SEPARATE LATER AUTHORIZATION** |

## Researcher decision requested

Approve, revise, or reject the proposed TP2 primary architecture with TP3 diagnostic overlay, while retaining TP1 as the lower-complexity comparator and TP0 as a sensitivity baseline. No development access follows automatically from approval; numerical partitions and access controls must be frozen first.

`G4-03B TEMPORAL VALIDATION ARCHITECTURE PROPOSED / AWAITING RESEARCHER REVIEW`
