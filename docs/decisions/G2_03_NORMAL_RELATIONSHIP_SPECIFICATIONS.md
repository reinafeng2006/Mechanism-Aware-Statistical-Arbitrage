# G2-03 — N0/N1 Normal-Relationship Specifications and N2 Escalation Freeze

Status: **APPROVED / FROZEN — 2026-09-04**

Scope: semantics of pooling, pair specificity and complexity escalation only. No estimator, factor model, distribution, window, threshold, metric, update rate or empirical winner is selected.

## Governing identity

`N0 and N1 must measure the same semantic object.`

That object is the G2-01 frozen, uncertainty-aware joint-conditional plus bidirectional-response relationship. N0/N1 differences concern where relationship structure is shared and how much is pair-specific—not what “normal relationship” means.

## 1. N0 semantics

**N0 — Industry-Structured / Strongly Pooled Normality** is the hypothesis that securities within an economically coherent industry share enough normal-relationship structure to justify stronger pooling or common structure.

N0 does not require every pair to share an identical coefficient, correlation, spread, distribution or parameter value. “Strongly pooled” describes the architecture's greater reliance on industry-level structure relative to N1. N0 may still permit pair indexing or limited pair variation where a later statistical specification requires it; no such implementation is selected here.

N0 is the simpler pooling benchmark. It tests whether shared structure can represent normal pair behavior without prematurely granting each pair extensive flexibility.

## 2. N1 semantics

**N1 — Pair-Specific Normality** targets exactly the same G2-01 relationship object but allows substantially more of its characteristics to be determined from each pair's own PIT historical relationship.

N1 does not authorize an unconstrained or post-hoc pair model. Pair-specific flexibility must remain prespecified, PIT, reproducible and subject to the same information and evaluation discipline as N0. N1 is a competing candidate, not a presumed improvement.

## 3. Dimensions along which N0/N1 may differ

The following are permitted architectural axes of difference; their implementation remains unresolved:

| Difference axis | N0 orientation | N1 orientation |
|---|---|---|
| Pooling strength | Stronger reliance on industry/common structure | Weaker pooling; greater pair-history influence |
| Parameter sharing | More shared/common constraints or regularities | More pair-specific characteristics/parameters |
| Pair heterogeneity | Represented more parsimoniously | Represented more flexibly |
| Information borrowing | Greater cross-pair/industry borrowing | Greater reliance on the pair's own PIT history |
| Sparse-history behavior | Shared structure may provide support | Pair-specific estimation may carry greater uncertainty |
| Adaptation scope | Common structure may constrain evolution | Pair-specific components may adapt more independently |

These axes do not select a parameterization, shrinkage method, model family or estimator.

## 4. Dimensions N0/N1 must hold constant

N0 and N1 must share:

- the G2-01 semantic normal-relationship target;
- the signed, asymmetric and state-dependent capability being evaluated;
- the declared P0 or P1 pair-information architecture within a comparison;
- the PIT availability and causal-timing boundary;
- the evaluation period and prediction/assessment origin;
- the relationship-level validation objective and outcome-exclusion discipline;
- the universe, eligibility and missing-data treatment for a fair comparison;
- the definition separating relationship state, uncertainty, temporary abnormality and change/break;
- the anti-circularity rule;
- the rule that final strategy PnL is not the first selection criterion.

A comparison may not call different economic/statistical objects “N0 versus N1” merely because both produce a pair score.

## Shared, pair-specific, state-dependent and dynamic dimensions

| Dimension | Conceptual role | Status |
|---|---|---|
| Industry-shared | Common semantic schema, economically meaningful conditioning dimensions, or constrained relationship structure | Permitted; exact content/strength G2-DEFER |
| Pair-specific | Pair identity, pair history, signed directional characteristics, uncertainty or deviations from shared structure | Permitted; exact content/strength G2-DEFER |
| State-dependent | Conditional behavior associated with PIT market/industry/pair state | Required capability, not required complexity; state definition G2-DEFER |
| Dynamically updated | Evolution of relationship state/uncertainty as new PIT information arrives | Permitted under anti-circularity; update rule/rate G2-DEFER |

Nothing here requires each dimension to appear in a final model.

## 5. N2 escalation rationale

**N2 — Hierarchical / Partial-Pooling Normality** remains **ILLUSTRATIVE / UNAUTHORIZED**.

Conceptually only:

`pair-specific relationship = shared industry structure + pair-specific deviation`

N2 may be proposed for separate authorization only after a prespecified N0/N1 comparison reveals a concrete problem that simpler candidates cannot adequately handle. Qualifying evidence may include:

- systematic material pair heterogeneity that N0 fails to represent;
- excessive estimation uncertainty or instability under N1;
- sparse-history pairs making substantially pair-specific estimation unreliable; or
- relationship-level evidence that partial pooling may improve calibration/generalization rather than merely downstream prediction or PnL.

The escalation record must name the observed problem, show why N0/N1 remedies are inadequate, define the additional complexity, and receive researcher approval before N2 design. No numerical threshold is frozen here.

## 6. Industry-heterogeneity principle

**Pooling strength must not be assumed identical across industries.** Industry coherence and heterogeneity may later affect how much shared structure is defensible. This does not authorize an Industry Homogeneity Score, industry-specific model, clustering rule or pooling estimator. Those remain G2 measurement questions followed by empirical validation.

## 7. Anti-circularity implications

- The observation being assessed as abnormal cannot immediately or with unrestricted weight redefine its own N1 normal reference.
- Greater N1 flexibility cannot be used to absorb anomalies after they are observed.
- Dynamic updating must distinguish evidence about a temporary observation from accumulated evidence about relationship change.
- N0 and N1 update eligibility, timing origin and outcome quarantine must be prespecified comparably.
- N2 cannot be introduced after observing which pairs or outcomes make it look favorable.

The update window, cadence, weight, freeze interval, embargo and change-detection method remain unselected.

## 8. Unresolved measurement/model decisions

- The statistical representation of the frozen relationship object.
- Which components or parameters, if any, are shared versus pair-specific.
- Pooling strength and whether it varies by industry.
- Industry definition, coherence/heterogeneity construct and any permissible measurement.
- State variables, state dependence and transition/update representation.
- History length, windows, refresh cadence, adaptation rate and uncertainty representation.
- Sparse-history definition and treatment.
- Stability, calibration, generalization, false-abnormality and break objectives/metrics.
- Materiality thresholds and the evidence required to trigger N2 authorization.
- Interaction of P0/P1 with N0/N1 comparisons and the sequence of comparisons.

## 9. Frozen classification

### FROZEN SEMANTICS

- N0 is the industry-structured/strongly pooled simpler benchmark; identical pair parameters are not required.
- N1 targets the same semantic object with substantially greater pair-specific PIT-history influence.
- The allowed difference axes and required constant dimensions above.
- Pooling strength is not assumed identical across industries.
- N2 remains unauthorized and requires a separately approved, problem-specific escalation.
- N0/N1 relationship-level fair comparison, outcome exclusion and anti-circularity requirements.

### G2 MEASUREMENT DECISION — DEFER

Every representation, parameterization, sharing rule, industry/state construct, estimator, distribution, history/window, update rule/rate, uncertainty treatment, objective, metric and threshold in Section 8.

### EMPIRICAL VALIDATION — DEFER

Whether N0 underfits pair heterogeneity; whether N1 is unstable or too uncertain; sparse-history behavior; industry differences; relationship-level calibration/generalization; false-abnormality and break behavior; and whether evidence justifies proposing N2. Downstream prediction/PnL alone cannot decide normal-relationship validity.

## 10. Learning Layer interpretation

The Learning Layer teaches N0/N1 as the same semantic target under different pooling strengths, shows shared versus pair-specific versus state-dependent versus dynamically updated dimensions, and marks N2 and its formula **ILLUSTRATIVE / UNAUTHORIZED**. It does not display a selected model or imply that greater flexibility is better.

## Approval record

The researcher approved G2-03 as proposed on 2026-09-04. N0/N1 semantics, allowed difference axes, held-constant dimensions, industry-heterogeneity principle, anti-circularity implications, N2 escalation boundary and PnL restriction are frozen. All estimator, representation, factor, window, distribution, threshold, update-rate and validation-metric choices remain unresolved exactly as proposed. G2-04 remains unauthorized.
