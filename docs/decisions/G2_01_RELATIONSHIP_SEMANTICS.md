# G2-01 — Economic / Signed Conditional Relationship Semantics Freeze

Status: **APPROVED / FROZEN — 2026-09-04**
Scope: semantic object and conceptual boundaries only. No statistical representation, formula, estimator, window, threshold, distribution or validation metric is selected.

## Frozen primary semantic object

A pair relationship is a **stable-enough, point-in-time estimable conditional joint/response relationship** between two securities, optionally conditioned on economically relevant market, industry and pair states. It describes the pair's currently expected joint behavior, directional responses and associated uncertainty using only information available by the decision time.

The primary semantic object is a **framework containing both**:

1. a **joint conditional distribution view**, which asks what combinations of contemporaneous or ordered responses are normal conditional on the current information state; and
2. **directional conditional response views**, which ask how security `j` is expected to respond conditional on information or movement in `i`, and separately how `i` is expected to respond conditional on information or movement in `j`.

These are complementary semantic views, not selected estimators. The joint view prevents the relationship from being reduced to a single direction; the directional views preserve economically meaningful lead–lag and asymmetric response questions. Neither view implies causality without separate identification evidence.

## Frozen semantics

The following are **FROZEN SEMANTICS**:

- Validity means sufficiently persistent and PIT-estimable conditional behavior for the intended research use; it does not mean permanent invariance.
- The semantic object permits positive, negative, asymmetric, state-dependent, pair-specific and gradually evolving relationships.
- Expected response includes explicit uncertainty; a point prediction alone is not the complete semantic object.
- `i → j` and `j → i` are distinct directional views and need not be symmetric.
- Conditioning information may include economically relevant market/industry states, but no conditioning variable is required or selected here.
- Relationship validity is not synonymous with positive correlation, similarity, cointegration, spread stationarity, OLS residual structure or trading predictability.
- `relationship validity ≠ trading predictability`.
- `economic relationship ≠ statistical dependence ≠ tradable opportunity`.
- The relationship object describes conditional behavior; it does not by itself identify an economic mechanism, causal effect or profitable intervention.

## Four distinct conceptual objects

| Object | Precise semantic definition | Boundary |
|---|---|---|
| Relationship state | The pair's current normal conditional joint behavior and directional response structure, indexed by the PIT information state. | A latent/conceptual target, not a chosen state-space model or discrete regime. |
| Relationship uncertainty | Uncertainty about the expected conditional behavior, including irreducible response variation and imperfect knowledge from finite/stale/noisy information. | Its decomposition, calibration and representation remain unselected. |
| Temporary abnormality | Degree to which a new joint observation is unusual relative to the current relationship state and its uncertainty, without yet concluding that the relationship itself changed. | Not automatically a mechanism, trade signal or binary trigger. |
| Relationship change / break | Accumulating evidence that the data-generating conditional relationship itself has evolved materially enough that the prior normal relationship is stale or invalid for the intended use. | Not equivalent to one extreme observation and not automatically M0 without positive rejection ancestry. |

## Conceptual mathematical representation

The following notation is **ILLUSTRATIVE / UNAUTHORIZED**, except for the semantic distinctions it labels:

`R_t := { JointLaw(Y_i,t, Y_j,t | I_t), Response(j | i, I_t), Response(i | j, I_t), Uncertainty_t }`

Here `I_t` means information lawfully available by decision time `t`; `R_t` denotes the conceptual relationship state, not a selected probability family or estimator. A conceptual abnormality comparison is:

`A_t := departure(observed joint response at t, expected response under R_t, uncertainty under R_t)`

This is not an authorized score, likelihood, residual, distance or threshold. Relationship change is conceptually evidence about movement in `R_t`, not merely a large `A_t`.

## Anti-circularity boundary

The normal relationship and the observation being judged must be temporally separated. A short-term abnormal observation must not be allowed to update the normal relationship so quickly or with such weight that it erases its own abnormality by construction.

If approved, G2 must later specify—before outcome inspection—how the reference relationship is estimated as of the decision time, when and how it may update, how candidate change/break evidence is accumulated, and how observations used for assessment are separated from information used to define their reference. The exact update rule, adaptation rate, window, embargo, change test and freeze/re-estimation policy remain deferred.

## Classification of decisions

### FROZEN SEMANTICS

- The combined joint-distribution/directional-response framework.
- The signed, asymmetric, state-dependent, pair-specific, gradually evolving and uncertainty-aware capabilities.
- The four-object distinction above.
- The non-equivalence and non-causality/non-profitability boundaries.
- PIT conditioning and the anti-circularity principle.

### G2 MEASUREMENT DECISION — DEFER

- Observable response variables, horizons and event clock.
- Conditioning information and state representation.
- Statistical representation: raw, residual, distance, correlation, regression, cointegration, factor or alternatives.
- Distributional form, estimator, parameterization, window/history, adaptation rate and uncertainty representation.
- Operational definitions of stable-enough, material change, break, abnormality and missing/stale evidence.
- Direction-specific versus joint measurement implementations and their reconciliation.
- Relationship-level comparison criteria and the timing protocol that enforces anti-circularity.

### EMPIRICAL VALIDATION — DEFER

- Whether any candidate is PIT-estimable, stable, calibrated and generalizable in A-share machinery stocks.
- Whether signed/asymmetric/state-dependent structure adds relationship-level value.
- Whether normal-response errors, false-abnormality behavior and break detection are acceptable OOS.
- Whether relationship validity contributes incremental resolution prediction or economic value; PnL cannot be the first validity criterion.

## Approval record

The researcher approved this proposal without modification on 2026-09-04. G2-01 is frozen. G2-02 remains unauthorized until a separate researcher instruction. Approval freezes only the semantics and boundaries listed above; every item under `G2 MEASUREMENT DECISION — DEFER` and `EMPIRICAL VALIDATION — DEFER` remains unresolved exactly as proposed.
