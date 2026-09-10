# G4-04A1a PIT Scale & Aggregation Specification Proposal

Status: **PROPOSED / AWAITING RESEARCHER REVIEW**
Boundary: numerical-protocol design only. No frozen-data inspection, statistic, candidate loss computation, or outcome access.

## Objective

Select one candidate-neutral PIT scale contract and one deterministic hierarchical aggregation contract for the frozen A1 absolute/squared losses. The same scale and aggregation rule must apply to named competing representations on CS2 common support.

## Candidate-neutral PIT scale requirements

Every candidate scale must:

- measure the pre-origin scale of the frozen directional response target, not candidate forecast uncertainty;
- use only information available before the evaluation origin;
- use a history rule already inside the representation-aware Search Budget or a separately frozen common scaling history;
- be identical across competing representations at the same direction/pair/origin;
- define zero, near-zero, undefined, sparse-history, and structural-break states;
- remain reproducible and versioned;
- avoid future/outcome normalization.

## Bounded scale candidates

### PS0 — Robust historical response scale

A pre-origin robust dispersion functional of the observed directional response target, such as a later-specified median-absolute-deviation family. It limits domination by historical extremes but requires a frozen consistency factor and minimum-support rule.

### PS1 — Quadratic historical response scale

A pre-origin standard-deviation/RMS family for the same directional target. It aligns naturally with squared loss but is more sensitive to extremes and relationship breaks.

### PS2 — Candidate-neutral conditional response scale

A common pre-origin scale conditional on an already-authorized market/industry state, applied identically to all representations. It may better respect state dependence but adds a conditioning specification and must not repeat candidate-specific modeling.

All formulas and estimator details are **ILLUSTRATIVE / UNAUTHORIZED**. No scale candidate is preferred here. A fixed arbitrary constant or candidate-reported forecast uncertainty is not admissible as the cross-representation scale.

## Zero/near-zero scale candidates

Preserve a bounded choice among:

- mark the directional observation undefined for scaled-loss comparison and retain the exclusion reason;
- apply a preregistered candidate-neutral floor derived without outcome inspection;
- route the record to a separate unscaled diagnostic stratum without allowing it into the primary scaled estimand.

No floor or rule is selected.

## Four-level aggregation contract

### Level 1 — observations within direction

Choose a preregistered central-loss summary plus dispersion, severe-failure, and eligible-support reporting for each pair-direction-origin. A mean, median/quantile, or bounded robust functional may be considered; outcome-driven selection is prohibited.

### Level 2 — directions within pair

Retain `i -> j` and `j -> i` results, then apply an explicit symmetric, asymmetric, or non-compensatory pair rule. Severe failure in one direction cannot be hidden by automatic averaging. Missing directional capability and unequal directional support remain visible.

### Level 3 — pairs within support

Use a rule that prevents observation-rich pairs from receiving automatic row-count weight. Candidate families include equal pair weighting, a preregistered bounded support weight, or a hierarchical pair distribution summary. Common-support attribution and native-support deployability remain separate.

### Level 4 — temporal origins/folds

Aggregate semiannual inner origins and OF4 folds only through the frozen multidimensional evidence vector: central effect, direction consistency, dispersion, severe failure, and support. No compensatory scalar or result-selected fold weighting is permitted.

## Bounded aggregation architectures

- **AG0 — equal-unit hierarchy:** equal weight at each applicable direction/pair level, with separate dispersion/failure/support reporting;
- **AG1 — robust hierarchical summary:** robust central functional at observation and pair levels, without discarding the separate evidence vector;
- **AG2 — non-compensatory directional/pair hierarchy:** advancement requires both directional and pair-level adequacy conditions before temporal aggregation.

These are candidate architectures, not a Cartesian menu of independently selectable choices. Any permitted hybrid must be enumerated explicitly in the Search Budget before access.

## CS2 and dependency rules

- The scale is computed without candidate identity and then applied to the exact CS2 common pair-date-direction intersection for attribution.
- Native-support losses use the same scale semantics but are reported separately for coverage/deployability.
- Candidate-specific exclusions are never recoded to enlarge common support.
- Scale failure, directional failure, and support loss retain distinct reason codes.

## Decisions required

1. select PS0, PS1, or PS2 and define its exact estimator/history contract;
2. select zero/near-zero/undefined-scale handling;
3. choose Level 1 central, dispersion, failure, and support summaries;
4. choose the Level 2 directional-to-pair rule;
5. choose Level 3 pair weighting/distribution rule;
6. choose Level 4 inner/outer aggregation semantics;
7. select AG0, AG1, AG2, or one explicitly enumerated bounded hybrid;
8. freeze candidate-neutral scale and aggregation versions before computation;
9. hand numerical meaningful-effect, uncertainty, severe-failure, and multiplicity thresholds to later G4-04A decisions.

No scale estimator, floor, aggregation statistic, weighting rule, threshold, or computation is selected here.

`G4-04A1a PIT SCALE & AGGREGATION SPECIFICATION PROPOSED / AWAITING RESEARCHER REVIEW`
