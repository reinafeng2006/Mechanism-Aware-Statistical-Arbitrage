# G4-04A1a PIT Scale & Aggregation Architecture Freeze

Status: **G4-04A1a APPROVED / FROZEN — 2026-09-10**
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

### PS0 — Primary: robust historical response scale

A pre-origin robust dispersion functional of the **same observed directional response quantity that the frozen expected conditional response predicts**. For `i -> j`, PS0 scales historical PIT realizations of the `j` response coordinate defined relative to the authorized `i` source/state and response interval; for `j -> i`, it separately scales the corresponding `i` response coordinate. It does not substitute source-stock volatility, an unrelated market-volatility series, or candidate forecast residuals.

The historical directional response may later use a preregistered candidate-neutral PIT location and robust dispersion functional, such as a median-absolute-deviation family. Exact location, dispersion, consistency factor, support history, and update rule remain unresolved. PS0 is proposed as primary because it is PIT, candidate-neutral, robust, interpretable, and operationally simple.

### PS1 — Preregistered robustness: quadratic historical response scale

A pre-origin standard-deviation/RMS family for exactly the same directional response quantity, response interval, candidate-neutral location convention, and PIT history contract used by PS0. It changes sensitivity to historical extremes rather than changing the economic scale object. Separate `i -> j` and `j -> i` construction remains mandatory where directional semantics differ.

### PS2 — Optional / not primary: candidate-neutral conditional response scale

A common pre-origin scale conditional on an already-authorized, preregistered market/industry information set, applied identically to all representations. The conditioning information set must be independent of the candidate representation being evaluated and frozen before outcomes. PS2 cannot become primary because conditioning improves realized rankings.

`normalization must not become a hidden second relationship model`.

All formulas and estimator details remain unresolved. The frozen roles are PS0 primary, PS1 preregistered robustness, and PS2 optional/non-primary. A fixed arbitrary constant, unrelated source-security volatility, or candidate-reported forecast uncertainty is not admissible as the cross-representation scale.

## Scale quality and zero/near-zero state

Create an explicit structural state:

`SCALE QUALITY / NEAR-ZERO SCALE`.

When the candidate-neutral PIT scale is undefined, weakly supported, unreliable, or near zero, scaled-loss eligibility must be resolved explicitly. An arbitrary fixed epsilon floor is prohibited as a computational convenience. Preserve a bounded later choice among:

- mark the directional observation undefined for scaled-loss comparison and retain the exclusion reason;
- apply a preregistered candidate-neutral floor derived without outcome inspection;
- route the record to a separate unscaled diagnostic stratum without allowing it into the primary scaled estimand.

Any numerical minimum-scale rule or candidate-neutral floor must be preregistered and frozen before computation. No floor or rule is selected.

## Four-level aggregation contract

### Level 1 — observations within direction

Choose a preregistered central-loss summary plus dispersion, severe-failure, and eligible-support reporting for each pair-direction-origin. A mean, median/quantile, or bounded robust functional may be considered; outcome-driven selection is prohibited.

### Level 2 — directions within pair

Retain `i -> j` and `j -> i` results, then apply an explicit symmetric, asymmetric, or non-compensatory pair rule. Severe failure in one direction cannot be hidden by automatic averaging. Missing directional capability and unequal directional support remain visible.

### Level 3 — pairs within support

Use a rule that prevents observation-rich pairs from receiving automatic row-count weight. Candidate families include equal pair weighting, a preregistered bounded support weight, or a hierarchical pair distribution summary. Common-support attribution and native-support deployability remain separate.

### Level 4 — temporal origins/folds

Aggregate semiannual inner origins and OF4 folds only through the frozen multidimensional evidence vector: central effect, direction consistency, dispersion, severe failure, and support. No compensatory scalar or result-selected fold weighting is permitted.

## Frozen aggregation architecture

- **AG1 — PRIMARY: robust hierarchical aggregation.** Preserve the order `observations -> direction -> pair -> temporal origin/fold`. Retain both directional summaries before pair aggregation. At the representation-comparison layer, equal-pair influence is preferred so longer histories do not create automatic row-count dominance; another weight requires preregistered structural justification.
- **AG2 — NON-COMPENSATORY GUARDRAIL.** Detect preregistered severe directional or pair failures that AG1's robust center cannot erase. AG2 is a guardrail applied alongside AG1, not an independent winner-selection score.
- **AG0 — SIMPLE SENSITIVITY / REFERENCE.** An equal-unit/simple hierarchy used only under the registered sensitivity budget, never chosen retrospectively to obtain a preferred ranking.

The primary path is `AG1 + AG2 guardrail`. AG1 must not erase directional asymmetry, and OF4 evidence remains the non-compensatory vector `{magnitude, directional consistency, dispersion, severe failure, support}` rather than one scalar. Equal-pair influence is the preferred representation-comparison principle unless a later preregistered structural justification authorizes another implementation. Any permitted sensitivity or hybrid must be enumerated explicitly in the Search Budget before access.

PS1, PS2, AG0, and any aggregation sensitivity remain outside opportunistic primary selection. The primary scale/aggregation architecture cannot be selected retrospectively according to which candidate ranking it produces.

## CS2 and dependency rules

- The scale is computed without candidate identity and then applied to the exact CS2 common pair-date-direction intersection for attribution.
- Native-support losses use the same scale semantics but are reported separately for coverage/deployability.
- Candidate-specific exclusions are never recoded to enlarge common support.
- Scale failure, directional failure, and support loss retain distinct reason codes.

## Decisions required

1. approve, revise, or reject PS0 primary / PS1 robustness / PS2 optional roles;
2. select PS0 robust location/dispersion estimator, consistency convention, support history, and update rule;
3. select PS1 quadratic estimator and confirm identical response/history/location semantics;
4. select `SCALE QUALITY / NEAR-ZERO SCALE` numerical rule and eligibility consequence;
5. choose AG1 Level 1 central, dispersion, failure, and support summaries;
6. choose AG1 Level 2 directional-to-pair rule without erasing asymmetry;
7. choose equal-pair influence or another structurally justified Level 3 rule;
8. choose Level 4 inner/outer vector summaries without scalar collapse;
9. define AG2 severe directional/pair failure conditions;
10. freeze scale, aggregation, sensitivity, and Search Budget versions before computation;
11. hand meaningful-effect, uncertainty, severe-failure, and multiplicity thresholds to later G4-04A decisions.

No scale estimator, floor, aggregation statistic, weighting rule, threshold, or computation is selected here.

`G4-04A1a APPROVED / FROZEN`
