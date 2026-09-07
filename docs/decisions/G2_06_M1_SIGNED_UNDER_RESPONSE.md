# G2-06 — M1 Signed Under-Response Measurement Freeze Decision

Status: **APPROVED / FROZEN**
Date: 2026-09-07
Boundary: candidate measurement design only. Every equation is **ILLUSTRATIVE / UNAUTHORIZED**. No final formula, estimator, threshold, window, factor model, clock, M1 probability or decision rule is selected.

## Decision objective

Operationalize the candidate M1 construct:

> The peer has moved insufficiently in its expected signed direction relative to the current valid conditional pair relationship.

Binding boundaries:

`response gap ≠ M1 identification`

`under-response measurement ≠ M1 probability`

`future catch-up ≠ event-time input`

Signed under-response is a candidate measurement of a response discrepancy. It becomes candidate M1 discriminator evidence only when assigned that role at a lawful decision time and interpreted with source/link/timing information and rival checks under G2-05.

## Construct decomposition

1. **Expected Signed Response** — the peer response implied by the current valid G2-01/G2-03 conditional relationship, given the PIT state and the authorized information architecture. It includes a direction, not merely a magnitude.
2. **Observed Response** — the peer response actually observable by the current decision time under a declared response definition and clock.
3. **Signed Response Gap** — the discrepancy between expected and observed response, oriented so positive values can represent movement that is insufficient in the expected direction.
4. **Response Uncertainty** — uncertainty in the expected response, normal variation and/or current relationship state. Its representation remains unresolved.
5. **Under-Response Evidence** — a role-specific interpretation of a gap as insufficient incorporation. It is not mechanically created by a large gap and may require source provenance, economic linkage, timing coherence and rival/rejection checks.

The decomposition preserves the distinction between a mathematical discrepancy and evidence about a mechanism.

## Frozen signed-orientation convention

The semantic orientation is fixed across positive and negative expected responses:

`positive oriented under-response = insufficient movement in the expected signed direction`

An overshoot in the expected signed direction has the opposite orientation. One illustrative implementation is:

**ILLUSTRATIVE / UNAUTHORIZED**

`sign(expected_response) × (expected_response − observed_response)`

This expression illustrates the orientation convention; it is not the selected formula. If the expected response is too close to zero, its direction is unstable, or Response Uncertainty is too large to establish a meaningful direction, under-response must not be mechanically assigned. The observation may remain an unoriented abnormality or `U = Unresolved / Abstain`. The definition of “too close,” direction reliability and uncertainty sufficiency remains deferred.

## Competing candidate measurement specifications

Notation for illustration only:

- `e_t`: expected signed peer response under the current PIT relationship reference;
- `o_t`: observed peer response by decision time;
- `d_t = sign(e_t)`: expected response direction when meaningfully defined;
- `u_t`: an unresolved measure of expected-response uncertainty or normal variation;
- `x_t`: already-authorized PIT market/industry/relationship context.

### UR0 — Raw Signed Response Gap

**ILLUSTRATIVE / UNAUTHORIZED**

`UR0_t = d_t × (e_t - o_t)`

A positive value represents an observed response falling short in the expected signed direction; zero represents matching the expected response under this illustration; a negative value may represent movement beyond the expected response. The meaning is conditional on how `e_t`, `o_t` and the response interval are later defined.

UR0 is not directionally defined when a meaningful expected sign cannot be established. A numerical sign function must not manufacture M1 under-response from a near-zero or highly uncertain expectation.

Strength: transparent and preserves sign. Limitation: does not make gaps comparable across pairs, states or uncertainty levels.

### UR1 — Uncertainty-Standardized Signed Response Gap

**ILLUSTRATIVE / UNAUTHORIZED**

`UR1_t = d_t × (e_t - o_t) / u_t`

This expresses the signed gap relative to a future authorized uncertainty/variation reference. It does not become a probability, significance test or M1 score merely because it is standardized.

Strength: potentially makes gap magnitude interpretable relative to relationship uncertainty. Limitation: inherits all assumptions, calibration error and instability in `u_t`, including undefined or poorly estimated uncertainty.

### UR2 — Conditional / Context-Adjusted Under-Response

**ILLUSTRATIVE / UNAUTHORIZED**

`e_t(x_t) = expected peer response conditional on PIT context x_t`

`UR2_t = signed_gap(e_t(x_t), o_t [, u_t(x_t)])`

UR2 permits authorized context not already represented in the Expected Signed Response architecture to affect the under-response interpretation. It is an architecture family, not a specific residualization, factor model or formula.

Strength: can distinguish peer shortfall from response explained by separately authorized PIT context. Limitation: greater data/model dependence, context misspecification risk and potential overlap with the normal-relationship estimator.

### Information-set lineage and no-double-conditioning rule

UR2 must preserve three separately declared information sets:

1. **Normal / Expected Response Information Set** — information already used to estimate the normal relationship and Expected Signed Response;
2. **Response-Gap Measurement Information Set** — source/peer observations and timing required to compare expected with observed response;
3. **Additional M1 Discriminator / Rival Information Set** — PIT context used to interpret the gap but not already incorporated into the expected-response object.

`normal-relationship conditioning ≠ repeated under-response conditioning`

UR2 may not re-adjust, residualize or condition on information already embedded in Expected Signed Response unless a later design explicitly defines a non-duplicative transformation and proves its lineage. Overlapping information must be declared and resolved rather than counted twice. Context already in the normal reference remains ancestry of the expectation; it does not become new M1 evidence merely by being reused.

UR0, UR1 and UR2 remain competing candidates. UR1 may standardize either UR0 or a conditional gap; UR2 may remain multidimensional. Their partial nesting does not authorize a complexity ladder winner.

## Signed, asymmetric and state-dependent semantic checks

These are hypothetical unit-free examples, not market observations or thresholds.

| Case | Expected peer response | Observed response | Signed-gap interpretation |
|---|---:|---:|---|
| Positive relationship | `+4` | `+1` | Positive shortfall of `3`: candidate under-response morphology |
| Negative relationship | `-4` | `-1` | Positive signed shortfall of `3`: peer did not move far enough in the expected negative direction |
| Expected negative, overshoot | `-4` | `-6` | Negative gap of `-2`: not under-response under UR0 semantics |
| Wrong direction | `+4` | `-1` | Positive gap of `5`, but could indicate break, own-news or misspecified state; not automatically M1 |
| Directional asymmetry | `i→j: +4`; `j→i: +1` | peer response `+1` after shock to `i` | Evaluate against `i→j`, not the reverse relationship |
| State dependence | state A expects `+4`; state B expects `-2` | observed `-1` in state B | Compare with `-2`; do not reuse state A's positive expectation |

Thus under-response never means merely “peer moved less than source.” It refers to the relevant directed conditional expectation.

## Timing architecture

Every candidate measurement must preserve distinct timestamps:

1. **Source/shock observation time** — when the source response or candidate shock is observed.
2. **Expected-response reference time** — the PIT cutoff at which the normal relationship and context used to form `e_t` are frozen.
3. **Peer observation time** — the end of the peer-response information included in `o_t`.
4. **Decision time** — when UR and accompanying discriminator/rival evidence may legally enter the sequential system.
5. **Later validation horizon** — the prespecified future interval used to test catch-up or another outcome.

The reference must precede or be causally valid for the observation being judged. The decision record must preserve all five times and applicable data vintages. Daily close is not presumed. Still unresolved are event versus calendar clock, synchronization, intraday/daily frequency, response interval, source-event duration, non-synchronous trading treatment, update cadence, staleness and validation horizon.

## Relationship to the frozen abnormality state

Signed response gap can occupy both layers without collapsing them:

- At the **general abnormality layer**, signed-direction or magnitude mismatch may be one morphology of the Multidimensional Abnormality State, independent of any M1 claim.
- At the **M1-specific interpretation layer**, a directed gap can be transformed into candidate under-response evidence only after binding it to source/link/timing context and rival checks.

The M1 transformation consumes the frozen normal-relationship reference; it cannot refit, redefine or rapidly update that reference to make the gap appear or disappear. Relationship-change/break evidence remains a parallel rejection/update channel under the G2-01/G2-04 anti-circularity boundary.

## Rival and rejection boundaries

A large UR candidate cannot alone distinguish delayed incorporation from:

- peer own-news;
- relationship change/break;
- common, continuing or mis-timed shock;
- liquidity or pressure effects;
- stale, invalid or directionally misspecified economic link;
- market or industry context already explaining the response;
- measurement error, non-synchronous observation or ordinary uncertainty.

Each rival must be represented through the G2-05 role/timing architecture. Some information may lower M1 belief without establishing M0; positive pair-invalidating evidence is still required for M0. Conflicting or insufficient evidence may preserve `U = Unresolved / Abstain`.

## Production-feasibility comparison

These are preliminary architecture-level assessments, not provider claims or empirical rankings. Final status requires G3 data feasibility and later validation.

| Candidate | Required raw data | PIT/frequency/coverage | Acquisition, latency, compute, reproducibility | Cacheability / critical path | Preliminary feasibility status |
|---|---|---|---|---|---|
| UR0 | PIT source/peer market response plus a precomputed expected-response reference | Reliability and coverage inherit the Expected Signed Response specification and timestamp alignment | The subtraction/orientation transformation itself is `EASY`; end-to-end acquisition, compute and reproducibility inherit the normal-response architecture | Expected response may be cached if its specification allows; current observed response is latency-critical | Transformation: `EASY`; end-to-end status: `UNRESOLVED / INHERITED`, not globally easy |
| UR1 | UR0 inputs plus PIT relationship uncertainty/normal-variation estimate and history | Requires adequate pair/state history and calibrated uncertainty coverage | Moderate derivation and validation burden; sensitive to unstable/zero uncertainty estimates | uncertainty may be cached/medium-state; current numerator is latency-critical | `MODERATE` preliminary |
| UR2 | UR0/UR1 inputs plus authorized PIT market/industry/relationship context | Coverage and PIT reliability depend on chosen context and frequency | Moderate by default; may become hard if specialized/intraday/proprietary context is introduced | slow/medium context should be cached; fast contextual observations may be critical | `MODERATE`, potentially `HARD / OPTIONAL`; component-dependent |

The labels assess operational feasibility, not evidence strength or expected alpha. UR0's arithmetic simplicity does not make its underlying Expected Signed Response easy to produce. A harder UR1/UR2 implementation may supplement or displace a simpler transformation only if later validation shows material incremental M1 discrimination or resolution-prediction value. No provider or dataset is selected or acquired.

## Unresolved decisions

- construction and estimator of expected signed response;
- response definition, scale, units and aggregation;
- representation and calibration of response uncertainty;
- operational rule for when expected direction is too near zero or too uncertain to orient, while preserving U rather than mechanical assignment;
- candidate normalization and cross-pair comparability;
- raw versus conditional/context-adjusted representation;
- exact information-set partitions, overlap audit and no-double-conditioning implementation for UR2;
- state definition and asymmetric directional parameterization;
- clock, frequency, synchronization, response interval, window and update cadence;
- source/shock identification and event-time provenance;
- role assignment, rival measurements and missing/stale-data handling;
- threshold, ranking, trigger, probability or attention use;
- M1 belief/update model and interaction with resolution prediction;
- final Production Feasibility classifications and incremental-value protocol;
- validation targets, horizons, metrics and A-share transferability.

## Frozen classification

### FROZEN SEMANTICS

- M1 under-response means insufficient movement in the expected signed direction relative to a current valid PIT conditional relationship;
- the five-part construct decomposition;
- signed, asymmetric and state-dependent capability;
- positive orientation for insufficient movement and opposite orientation for overshoot, with no mechanical assignment under weak/uncertain expected direction;
- response-gap, M1-identification, probability and outcome separation;
- the five-time timing lineage;
- general-abnormality morphology versus M1-specific interpretation layers;
- no redefinition of normality by the M1 measurement;
- explicit separation of normal/expected-response inputs, gap-measurement inputs and additional discriminator/rival inputs, prohibiting repeated conditioning;
- rival, M0-positive-rejection and U boundaries.

### CANDIDATE MEASUREMENT

- UR0 raw signed gap;
- UR1 uncertainty-standardized signed gap;
- UR2 conditional/context-adjusted under-response.

All are **ILLUSTRATIVE / UNAUTHORIZED** and none is preferred or frozen as a formula.

### G2-DEFER

All estimator, response, uncertainty, contextual adjustment, clock, frequency, window, normalization, role, threshold, update and model choices; final feasibility ratings; M1 decision use.

### EMPIRICAL-DEFER

Measurement calibration, reliability, stability, rival sensitivity, incremental discrimination and prediction value, production feasibility, cross-pair/state generalization, A-share transferability and future catch-up validation without leakage.

## Approval record

Researcher approval on 2026-09-07 freezes the five-object decomposition, signed-orientation convention, weak-direction/U handling, three information-set separation, no-double-conditioning rule, UR0/UR1/UR2 as competing candidates only, UR0 transformation/end-to-end feasibility distinction, and all rival, PIT and outcome-leakage boundaries exactly as documented above.

No candidate, Expected Response or uncertainty estimator, threshold, window, model, provider or factor is selected. G2-07 remains unauthorized. No data acquisition, implementation or empirical testing is performed.
