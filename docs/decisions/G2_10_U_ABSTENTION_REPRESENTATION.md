# G2-10 — U / Abstention Representation Freeze Decision

Status: **APPROVED / FROZEN**
Date: 2026-09-07
Boundary: uncertainty semantics and decision separation only. No probability threshold, classifier, numerical uncertainty measure, transition model, trade rule or empirical specification is selected.

## Decision objective

Formalize how the sequential system represents cases in which mechanism inference is insufficient, conflicting, unreliable or not yet mature enough for responsible assignment.

Frozen distinctions:

`U = epistemic state`

`Abstain = decision/action`

`No Trade = possible downstream trading outcome`

These are separate objects. Neither Abstain nor No Trade is a mechanism, and neither is synonymous with U.

## Positive U semantics

U is the legitimate epistemic state in which mechanism belief remains insufficiently resolved under the PIT information available at a declared decision time. It records what the system responsibly does not know; it is not merely the mechanical remainder after M0/M1/M2 fail thresholds.

U does not assert that no mechanism exists, that M3 exists, that the pair is invalid, or that trading must cease. It may coexist with partial evidence for several mechanisms and may be revised as new PIT information arrives.

## Candidate sources of U

1. **Measurement Uncertainty** — relationship state, Expected Response, abnormality or another measurement is too uncertain, unstable or unreliable for responsible mechanism use.
2. **Information Insufficiency** — relevant discriminator or rejection evidence is missing, stale, unavailable or not yet public.
3. **Mechanism Ambiguity** — multiple M0/M1/M2 interpretations remain materially plausible under current evidence.
4. **Evidence Conflict** — available evidence points in materially inconsistent directions.
5. **Data / Provenance Uncertainty** — PIT validity, timestamps, data quality, lineage, coverage or production feasibility are inadequate.

These are overlapping diagnostic sources, not mutually exclusive classes, scores or a taxonomy. No aggregation, weighting or threshold is authorized.

## U, M0 and M3 boundaries

| Object | Positive meaning | Required boundary |
|---|---|---|
| U | current PIT evidence does not support responsible mechanism resolution | no economic mechanism claim |
| M0 | positive structural, fundamental or relationship-invalidating evidence weakens temporary arbitrage | cannot arise from mere insufficiency |
| M3 | preserved but currently non-identified economic research hypothesis | no event-time discriminator or production label |

Therefore: `unexplained live abnormality → U`, never automatically M3; `insufficient mechanism evidence ≠ M0`; `U ≠ M0` and `U ≠ M3`.

## Epistemic state versus action

U describes knowledge at time `t`; Abstain describes a decision response; No Trade is one possible downstream trading outcome. A future Decision Model may react to U through continued tracking, delayed action, awaiting information, reduced confidence or exposure, abstention, or eventual No Trade. None is selected here.

`U → No Trade` is not frozen as an immediate or permanent rule. `Abstain ≠ U`; `No Trade ≠ U`.

Abstention may also occur when a mechanism is relatively resolved but costs, weak expected payoff, risk constraints, capacity or implementation limits make action unattractive. Conversely, a U case may remain under active tracking rather than immediately entering No Trade.

## Sequential transition semantics

U is dynamic and revisable. The architecture permits, without defining a transition model: `U(t0) → M1(t1)`, `U(t0) → M2(t1)`, `U(t0) → M0(t1)`, and `U(t0) → U(t1)`.

Transitions require genuinely new information available by `t1`, or a properly authorized update to a measurement using information available by `t1`. Earlier records and their PIT information sets remain immutable. U neither permanently absorbs unexplained cases nor forces eventual assignment.

## Not yet known versus currently non-identifiable

- **Not yet known** — specified information may plausibly arrive or mature later. This can support waiting or continued tracking.
- **Currently non-identifiable** — available information and authorized constructs do not presently distinguish the competing interpretations, even after current inputs are processed. This may support continued U, research escalation or downstream abstention.

The distinction must be recorded at each decision time. It is not a numerical horizon, permanence declaration or action rule. A later arrival may change either assessment, but it cannot rewrite the earlier state.

## Candidate future representation families

All remain competing **ILLUSTRATIVE / UNAUTHORIZED** candidates:

1. **U0 — Explicit Epistemic State**: a declared unresolved state alongside mechanism beliefs, without asserting a fifth mechanism.
2. **U1 — Unresolved Belief Mass**: a model-specific representation reserving mass for unresolved explanations.
3. **U2 — Uncertainty over M0/M1/M2**: U emerges from insufficient precision or unresolved dispersion over supported hypotheses.
4. **U3 — Abstention Region in Belief Space**: a future decision layer defines a region where assignment/action is withheld.
5. **U4 — Structured Diagnostic Vector**: retain the five U-source diagnostics without reducing them to one state or score.

These candidates need not be mutually exclusive at different semantic layers. No formula or normalization is authorized. In particular, the project does not require `P(M0) + P(M1) + P(M2) + P(U) = 1` unless a later model architecture independently justifies that probability space. U3 concerns a future decision policy and must not collapse epistemic U into Abstain.

## PIT and timing requirements

Every U assessment must record at minimum:

- decision time and frozen PIT information set;
- measurement and relationship-state vintages;
- observation and public/PIT availability times of relevant evidence;
- missing, stale, revised or conflicting input status;
- current evidence maturity and authorization status;
- whether the case is `not yet known` or `currently non-identifiable`;
- what genuinely new information, if any, could support a later update;
- immutable linkage to earlier and later sequential decision records.

Future outcomes, later data corrections or later-arriving evidence cannot be leaked backward to erase or relabel an earlier U assessment. They may inform only a later sequential decision or outcome validation.

## Production feasibility

U should preferentially reuse uncertainty, quality, timing, lineage, relationship, abnormality, discriminator and rejection metadata already produced by the frozen G2 architecture. A separate expensive U data stack is neither required nor authorized.

U0/U4 may be operationally simpler at the representation layer, but end-to-end feasibility inherits every underlying input. U1/U2/U3 inherit the eventual belief or decision model and therefore remain unresolved. Any dedicated U measurement must receive the full G2-05 Production Feasibility record. Easy representation does not imply reliable inference.

## Unresolved decisions

- which candidate representation or layered combination is appropriate;
- whether U is explicit, emergent from uncertainty, represented as unresolved mass or handled partly in the decision layer;
- how the five diagnostic sources are measured, stored or combined;
- how evidence sufficiency, ambiguity, conflict, staleness and reliability are operationalized;
- whether and how mechanism beliefs use probabilities at all;
- transition/update logic, clocks, persistence and reevaluation cadence;
- boundaries between continued tracking, escalation, abstention and No Trade;
- decision-policy treatment of U and non-U abstention;
- production feasibility, calibration, generalization and false-resolution behavior;
- providers, data implementation and empirical validation.

## Frozen classification

### FROZEN SEMANTICS

- U is a positive epistemic state, not a residual threshold bucket or fifth mechanism;
- U, Abstain and No Trade are separate objects;
- five candidate sources of U remain non-exclusive diagnostics;
- U is dynamic, revisable and tied to current PIT information;
- `not yet known` and `currently non-identifiable` are distinct;
- U does not default to M0 or M3 and does not mechanically imply No Trade;
- sequential updates preserve earlier decision records and prohibit outcome leakage.

### CANDIDATE REPRESENTATION

U0 explicit state, U1 unresolved mass, U2 uncertainty over mechanisms, U3 abstention region and U4 diagnostic vector remain **ILLUSTRATIVE / UNAUTHORIZED**. No candidate is selected or ranked.

### G2-DEFER

Representation choice, uncertainty/sufficiency/conflict measurements, belief architecture, update/transition logic, clocks, reevaluation cadence and all numerical definitions.

### DECISION-DEFER

How U and resolved beliefs map to continued tracking, delayed action, reduced exposure, abstention or No Trade; how costs, payoff, risk and implementation can cause Abstain independently of U.

### EMPIRICAL-DEFER

Calibration, coverage, persistence, false resolution, transition behavior, incremental value, production feasibility, A-share transferability and held-out validation.

G2-11 remains unauthorized. No data acquisition, implementation or empirical testing is performed.

## Approval record

Researcher approval on 2026-09-07 freezes U as a dynamic PIT epistemic state, the five potentially overlapping uncertainty sources, the U/M0/M3 and U/Abstain/No Trade boundaries, live unexplained-case routing, positive-evidence requirement for M0, new-information-only revision rule, prior-state preservation, `not yet known` versus `currently non-identifiable`, and U0–U4 as competing candidates exactly as documented above.

No probability space, uncertainty metric, threshold, transition model, abstention policy, waiting policy or trade-decision rule is selected. Mechanism/U probabilities are not required to sum to one absent a later specifically authorized model architecture.
