# G4-04A1 Relationship Representation & Validity Metric Architecture Freeze

Status: **G4-04A1 APPROVED / FROZEN — 2026-09-10**
Boundary: G4-04A Block 1 only. No frozen-data inspection, computation, outcome access, or N0/N1/P0/P1 metric design.

## Exact stage estimand

`OOS adequacy of a PIT-estimated representation of the pair's normal joint/conditional relationship, including predictive adequacy, uncertainty/calibration adequacy where applicable, and temporal robustness.`

Pair validity is not defined by correlation strength, cointegration significance, residual stationarity, in-sample fit, or strategy profitability alone. Those objects may be representation-specific diagnostics or later-stage evidence, but are not universal relationship-quality estimands.

## Proposed bounded metric architecture

| Metric role | Proposed family | Estimand/use | Support role |
|---|---|---|---|
| **PRIMARY COMPARISON METRIC** | Candidate-neutral-PIT-scaled OOS absolute conditional-response error | Cross-representation point-predictive adequacy for the same frozen observed-response target, direction, and decision origin | Primary attribution on CS2 common support; separately report native-support value |
| **SUPPORTING DIAGNOSTIC** | Candidate-neutral-PIT-scaled OOS squared conditional-response error | Tail-sensitive robustness using the same economic normalization; exposes conclusions dependent on extreme errors | Same common/native split; cannot replace the primary metric after inspection |
| **SUPPORTING DIAGNOSTIC** | calibration/uncertainty vector, where available | Calibration of predictive intervals/distributions separately from point error | Common support where representations are jointly capable; native support for coverage |
| **SUPPORTING DIAGNOSTIC** | temporal robustness vector | Central effect, direction consistency, dispersion, severe failure, and support across semiannual inner origins and OF4 folds | Origin- and fold-level evidence retained |
| **COVERAGE / DEPLOYABILITY METRIC** | eligible pair-date coverage and loss from common-support intersection | Practical usable scope, exclusion burden, and representativeness | Native support mandatory; common-support attrition reported |
| **REPRESENTATION-SPECIFIC ADMISSIBILITY DIAGNOSTIC** | contract-required diagnostics | Tests whether a representation satisfies its own stated mathematical/semantic assumptions | Never a universal winner metric |

## OOS loss candidates

### Candidate-neutral PIT scaling semantics

`point-prediction scaling != candidate-specific uncertainty calibration`.

The cross-representation point-loss denominator must be a **candidate-neutral PIT scale** that:

- uses only information available before the decision/evaluation origin;
- is defined identically across named competing representations on common support;
- does not depend on any candidate's reported forecast uncertainty or distribution width;
- uses no future or outcome information;
- has a preregistered state for zero, near-zero, undefined, or unreliable scale values.

The exact scale estimator and its zero/near-zero rule remain unresolved for a bounded numerical decision. A candidate cannot improve point-error performance by reporting wider uncertainty.

### Primary — scaled absolute error

Illustrative only:

`L_abs(i->j,t) = |observed_response(i->j,t) - PIT_expected_response(i->j,t)| / candidate_neutral_PIT_scale(i->j,t)`

The exact scale definition, zero/near-zero handling, and common response functional remain unresolved. Scale semantics are shared across candidates; candidate-reported uncertainty is excluded from this denominator.

Absolute loss is proposed as primary because it measures response error in a cross-representation form and is less dominated by a small number of extreme observations than squared loss.

### Preregistered robustness — scaled squared error

Illustrative only:

`L_sq(i->j,t) = ((observed_response(i->j,t) - PIT_expected_response(i->j,t)) / candidate_neutral_PIT_scale(i->j,t))^2`

Squared loss is deliberately tail-sensitive and asks whether the result changes when large misses receive disproportionate weight. It uses the same candidate-neutral PIT scale as absolute loss, so only sensitivity to large errors changes—not the economic normalization. It is a single preregistered robustness loss, not an outcome-selected alternative.

No additional point-loss menu is proposed. Absolute and squared losses must use the same target, PIT scale, temporal origins, eligibility rules, and comparison family. If a representation does not naturally produce the frozen common point-response functional, the approximation and semantic gap must be registered before evaluation.

## Calibration and uncertainty adequacy

Representations that produce predictive uncertainty or a distribution must be evaluated separately for:

- empirical coverage versus stated predictive coverage, where interval semantics exist;
- calibration across prespecified probability/quantile levels, where distributional semantics exist;
- sharpness/concentration conditional on adequate calibration;
- undefined, degenerate, or numerically invalid uncertainty outputs;
- temporal stability of calibration and native/common eligible support.

Candidate diagnostics include a finite interval-coverage vector and, where a full predictive distribution is genuinely supplied, a proper scoring diagnostic such as CRPS or another later-authorized proper score. Log-likelihood-specific fit is not universal and cannot compare representations lacking identical density semantics.

A representation receives no credit merely for emitting uncertainty; the uncertainty must be calibratable. A non-probabilistic representation is not automatically SR0-inadmissible. Its status is **UNCERTAINTY CAPABILITY ABSENT**, and comparison must report that capability gap without fabricating calibration evidence.

Candidate-specific uncertainty/distribution outputs remain wholly outside the point-loss denominator. They are assessed only through calibration and proper-uncertainty diagnostics.

## Directional-loss handling

The frozen relationship semantics permit asymmetric `i -> j` and `j -> i` responses. Therefore compute and retain conceptual loss components separately:

- `L(i -> j, t)`;
- `L(j -> i, t)`.

No silent averaging, pooling, minimum/maximum selection, or direction choice is permitted. A later preregistered rule must state how directional evidence becomes pair-level evidence, including how asymmetry, missing directional capability, unequal directional support, and severe one-direction failure are treated.

## Observation, direction, pair, and origin aggregation

The later protocol must specify a deterministic aggregation hierarchy across four distinct grains:

1. security-date/response observations within one direction;
2. the two directional responses for a pair;
3. pairs within a comparison family and CS2 support view;
4. semiannual inner origins and annual OF4 folds.

Pairs with longer eligible histories or more observations must not automatically dominate the representation-level comparison merely through row count. Candidate aggregation options must later address pair weighting, unequal observation counts, directional weighting, cluster/dependence structure, common-support intersection, and native-support coverage without collapsing those questions into one scalar.

## Representation-specific diagnostics

Correlation magnitude/sign, ADF or other stationarity diagnostics, cointegration diagnostics, residual diagnostics, likelihood-specific fit, and model-specific convergence/identification checks remain tied to the representation that requires them.

They may establish that a candidate failed its own preregistered representation contract. They cannot rank all relationship representations or redefine the frozen normal-relationship semantics.

## Temporal aggregation semantics

At each frozen semiannual inner origin and each OF4 outer fold, retain a relationship-evidence vector:

`{central loss/effect, direction consistency, dispersion, severe failure, common support, native support}`.

- Central loss/effect summarizes the prespecified comparison without becoming the whole decision.
- Direction consistency records whether relative improvement has the same sign across authorized origins/folds.
- Dispersion records time variation in the comparative effect.
- Severe failure records preregistered material breakdown rather than allowing averaging to conceal it.
- Support records common pair-date attribution support and native deployable coverage separately.

No weighted aggregate is permitted. Exact central-tendency, dispersion, uncertainty, consistency, and severe-failure statistics remain unresolved. One exceptional fold cannot compensate automatically for severe instability elsewhere.

## SR0 / SR1 mapping

### Legitimate SR0 non-compensatory conditions

- PIT or lineage violation;
- failure to produce the frozen relationship object or required point-response functional under the registered approximation contract;
- invalid/undefined output beyond a later-frozen structural tolerance;
- failure of candidate-specific minimum history, eligibility, or support contract;
- violation of a mathematical diagnostic explicitly constitutive of that representation's preregistered definition;
- prohibited outcome leakage or inability to reproduce the candidate under its frozen version.

Poor comparative OOS loss, weak calibration, low relative improvement, or temporal instability are not automatically structural failures. They normally enter SR1 unless a later-frozen use-specific adequacy floor genuinely makes the candidate invalid for that use.

### SR1 comparative evidence

For SR0-admissible candidates, SR1 uses:

1. common-support primary absolute-loss difference and its uncertainty;
2. squared-loss robustness evidence;
3. calibration evidence where jointly applicable, with missing uncertainty capability explicitly reported;
4. temporal consistency, dispersion, and severe-failure evidence;
5. native-support coverage/deployability;
6. production/data complexity only as the frozen later discriminator/tie-break.

The rule may return dominant/advances, non-dominated/both survive, insufficient differentiation, or no candidate advances. It need not force a unique winner.

## CS2 use

- **Common support:** freeze the named candidate set first, then intersect candidate-eligible pair-date origins inside each authorized temporal layer. Use this view for attribution of loss/calibration differences.
- **Native support:** report each candidate on its own frozen eligibility mask for coverage, deployability, failure burden, and practical usefulness.
- Report the number/share and reasons for pair-date loss caused by the common-support intersection.
- Never recode C04/C05/C06, missingness, identifier, temporal, or candidate-specific exclusions to enlarge the intersection.

`better native-support result != specification superiority when support differs materially`.

`better common-support result != sufficient deployability`.

## Relationship-representation multiplicity family

All preregistered representations competing for the same frozen relationship estimand constitute one upstream **Relationship Representation Comparison Family**. The primary family is defined by one primary loss on common support. The squared loss, calibration vector, representation-specific diagnostics, native support, and temporal vector are declared supporting/robustness evidence rather than additional opportunities to select the most favorable result.

This family is evaluated before normal-relationship, abnormality, mechanism, and resolution families. A representation failing SR0 cannot spawn unrestricted downstream testing. The exact within-family correction, confirmatory claim count, and alpha/q level remain unresolved; no global all-project tournament is created.

## Unresolved numerical and formal decisions

1. exact common observed-response target and directional functional used across representations;
2. candidate-neutral PIT scale estimator and zero/near-zero/undefined-scale treatment;
3. aggregation of security-date observations within a direction;
4. pair-level aggregation of `i -> j` and `j -> i` evidence;
5. pair weighting and protection against longer-support pairs dominating;
6. aggregation across pairs, semiannual origins, and annual OF4 folds;
7. exact absolute- and squared-loss fold/origin summaries;
8. uncertainty estimator for comparative loss differences;
9. calibration levels, coverage diagnostic, sharpness rule, and any proper score;
10. minimum common/native support and invalid-output tolerances;
11. meaningful improvement and insufficient-differentiation thresholds;
12. direction-consistency, dispersion, and severe-failure rules;
13. representation-contract diagnostics and their SR0 boundaries;
14. within-family multiplicity method and any alpha/q level;
15. inner aggregation and OF4 confirmation rule.

The formulas remain illustrative specifications pending G4-04A1a choices. The loss architecture, candidate-neutral scaling semantics, separate calibration channel, directional decomposition, four aggregation levels, and SR1 role are frozen; exact estimators, aggregation rules, and thresholds remain unauthorized.

`G4-04A1 APPROVED / FROZEN`
