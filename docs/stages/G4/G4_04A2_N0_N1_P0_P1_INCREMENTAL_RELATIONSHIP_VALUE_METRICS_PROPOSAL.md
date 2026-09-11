# G4-04A2 N0/N1 & P0/P1 Incremental Relationship-Value Metrics Freeze

Status: **G4-04A2 APPROVED / FROZEN — 2026-09-11**
Boundary: relationship-level metric design only. No frozen-data inspection, statistic, model fitting, candidate selection, outcome access, or downstream mechanism/economic evaluation.

## Objective

Prespecify how N0 versus N1 and P0 versus P1 will be evaluated for incremental normal-relationship value under the frozen G2 semantics, G4 temporal architecture, CS2 support, and SR0-to-SR1 selection rules.

The estimand is improvement in PIT OOS adequacy of the same signed conditional normal-relationship object—not strategy profitability.

## Primary paired incremental estimand

At the finest valid matched comparison unit `m`:

`DeltaLoss_m = ChallengerLoss_m - BaselineLoss_m`.

`DeltaLoss_m < 0` means the challenger has lower PIT-scaled absolute OOS conditional-response loss at that matched unit. The primary loss, candidate-neutral PIT scale, separate directional components, MAD normalization, and frozen AG1/AG2 hierarchy come directly from G4-04A1/A1a/A1b; no new performance metric is introduced.

The matched unit preserves, wherever applicable:

`m = {pair, direction, decision/evaluation origin, response target, candidate-neutral PIT scale, temporal role, common-support eligibility, relationship representation, authorized estimation geometry}`.

Baseline and challenger must share every named dimension. A dimension that necessarily differs must be declared as part of the incremental estimand before evaluation; it cannot change silently.

## Non-negotiable fair-comparison boundary

N0/N1 comparisons must hold constant:

- the G2-01 semantic target;
- P0/P1 information architecture within a named comparison;
- PIT information boundary and decision origins;
- evaluation periods and OF4 folds;
- candidate-neutral loss scale and A1 aggregation architecture;
- outcome-exclusion discipline;
- anti-circularity rule;
- CS2 common/native-support reporting.

P0/P1 comparisons must hold constant the normal-relationship specification, target, estimator family where applicable, temporal geometry, PIT boundary, and validation protocol. P1 differs only through the separately lineage-tracked economic/company information layer.

## N0 versus N1 estimands

### Exact N0 -> N1 estimand

`DeltaLoss_N(m) = Loss_N1(m) - Loss_N0(m)`.

This estimates the incremental relationship-level value of allowing greater pair-specific heterogeneity/adaptation relative to stronger pooling, conditional on the same semantic target, P0/P1 information architecture, relationship representation, response target, PIT scale, temporal origin, common support, and authorized estimation geometry except for the preregistered pooling/parameter-sharing dimension that defines N0 versus N1.

N1 cannot claim incremental value by also changing representation, target, scale, information set, or another unrelated dimension. N1 remains the mandatory challenger; challenger status does not imply selection.

Evaluate the pooling trade-off through separate relationship-level evidence dimensions:

- common-support change in primary absolute OOS response loss;
- squared-loss robustness;
- calibration/uncertainty evidence where jointly available;
- temporal stability and severe-failure evidence;
- native coverage and sparse-history deployability;
- parameter/state instability diagnostics where representation permits;
- approximation and complexity burden.

N0 is the simpler strongly pooled baseline; N1 is the mandatory pair-specific challenger. Neither is selected by status. N1 cannot be demoted to optional merely for greater complexity, and N0 cannot win merely for simplicity.

## P0 versus P1 estimands

### Exact P0 -> P1 estimand

`DeltaLoss_P(m) = Loss_P1(m) - Loss_P0(m)`.

P1 is strictly `complete P0 information + secondary Economic/Company Relationship information`. The estimand attributes incremental normal-relationship value only to that separately lineage-tracked secondary layer while holding fixed the semantic target, normality specification, relationship representation, scale, temporal origin, common support, and authorized estimation geometry.

P1 may not remove, replace, suppress, or differently transform inconvenient P0 information and still claim P0-to-P1 incremental value. Any unavoidable difference must define a separate estimand rather than masquerade as the incremental-information comparison.

Evaluate whether the secondary economic/company layer adds relationship-level value beyond market information through:

- common-support incremental primary loss;
- calibration/stability improvement where applicable;
- relationship-break or stale-linkage discrimination at the relationship level;
- sparse-history support and generalization;
- native coverage and deployability;
- added PIT, lineage, latency, and production burden.

P1 must not receive credit merely because it contains more information. Superior downstream return prediction or PnL alone cannot establish improved pair validity.

`downstream return prediction or strategy PnL alone cannot establish P1 incremental relationship value`.

## Proposed metric roles

| Evidence | Role |
|---|---|
| Candidate-neutral scaled absolute OOS loss difference on common support | **PRIMARY INCREMENTAL RELATIONSHIP-VALUE METRIC** |
| Squared-loss difference | **PREREGISTERED TAIL-SENSITIVE ROBUSTNESS** |
| Calibration/uncertainty difference | **SUPPORTING EVIDENCE WHERE JOINTLY AVAILABLE** |
| Temporal median-vector and AG2 failures | **TEMPORAL ROBUSTNESS EVIDENCE** |
| Native pair/date support and exclusion burden | **COVERAGE / DEPLOYABILITY EVIDENCE** |
| Pooling/parameter diagnostics | **N0/N1-SPECIFIC DIAGNOSTIC** |
| Economic-layer lineage, staleness, and approximation gap | **P0/P1-SPECIFIC ADMISSIBILITY / FEASIBILITY EVIDENCE** |

No universal scalar or weighted score is proposed.

## SR0 mapping

SR0 may reject a named candidate use only for genuine failures such as semantic mismatch, PIT/lineage violation, inability to reproduce required inputs, mathematically unsupported estimation, prohibited leakage, or failure of its frozen candidate-specific support contract.

Poor incremental loss, absence of improvement, weak temporal stability, low common-support attribution, or added complexity normally belongs to SR1/claim scope—not structural invalidity.

Structural inability to construct the declared matched unit may be an SR0 failure only where it violates a candidate's frozen semantics, PIT lineage, estimation contract, or required comparison identity. Otherwise it is an explicit support/estimand limitation. An ordinary positive `DeltaLoss` is unfavorable SR1 evidence, never an SR0 failure by itself.

## SR1 partial-order mapping

For each named comparison:

1. evaluate primary incremental relationship loss and uncertainty on common support;
2. examine squared-loss and calibration robustness;
3. preserve OF4 magnitude, directional consistency, dispersion, severe failure, and support;
4. report native coverage/deployability;
5. use complexity/feasibility only as a later discriminator.

The protocol may advance the challenger, retain the baseline, retain both as non-dominated, find insufficient differentiation, or advance neither where applicable. No improvement threshold is invented to force selection.

## CS2 paired support handling

- **Common support:** the primary attribution estimand uses only matched pair-direction-origin-target units eligible for both baseline and challenger under frozen candidate-specific and temporal rules.
- **Native support:** separately report coverage gained/lost, pair/dates on which the challenger or baseline is unavailable, exclusion reasons, and deployability implications.
- No structural state is recoded and no temporal origin is moved to enlarge the intersection.
- Better native coverage cannot compensate for worse common-support relationship evidence; better common-support evidence does not itself establish adequate deployability.

## Paired aggregation hierarchy

Preserve paired `DeltaLoss` evidence through:

`observation within direction -> equal-status directional vector within pair -> equal-influence common-support pairs -> semiannual origins / OF4 folds`.

Pair the baseline/challenger losses before aggregation; do not subtract two independently aggregated samples with different support. Consistent with AG1, each eligible pair has equal representation-level influence rather than row-count influence.

Do not form an incremental-value scalar. Preserve separately:

- central magnitude of paired loss difference;
- direction consistency across `i -> j` and `j -> i`;
- pair/origin/fold dispersion;
- independently justified severe failure or material reversal evidence;
- common and native support.

AG2 remains a guardrail and cannot create a weighted incremental score.

## Multiplicity family structure

- Each preregistered N0-versus-N1 comparison within a fixed representation/information architecture is an **N incremental-comparison family**.
- Each preregistered P0-versus-P1 comparison within a fixed normality/representation architecture is a distinct **P incremental-comparison family**.
- N and P families share the frozen loss architecture but cannot be pooled into one opportunistic tournament.
- Dependency gates must prevent unrestricted crossing of every representation, history, normality, and information variant.
- Primary loss defines the comparison claim; squared loss, calibration, temporal vectors, and native support are supporting evidence rather than extra winner-picking tests.
- Exact family membership and correction method remain unresolved.

## Unresolved decisions

1. define the exact finite matched N-family and P-family tuples in the Search Budget;
2. define the uncertainty procedure for paired `DeltaLoss` at pair, origin, and fold levels;
3. define continuous dominance, baseline-retention, non-dominance, insufficient-differentiation, and neither-advances rules without arbitrary thresholds;
4. define N0/N1 sparse-history and parameter-instability diagnostics;
5. define P0/P1 economic-layer staleness, lineage, and relationship-break diagnostics;
6. define common-support claim-scope reporting and native coverage gained/lost/deployability summaries;
7. define handling for unmatched dimensions and when they require a separate estimand;
8. define N-family and P-family multiplicity/claim roles separately;
9. preserve N2 escalation as separately conditional and unauthorized.

No numerical threshold, candidate tuple, estimator, winner, or computation is selected here.

`G4-04A2 APPROVED / FROZEN`
