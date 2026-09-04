# G2-04 — Pair-Specific Continuous Abnormality Construct Freeze

Status: **APPROVED / FROZEN — 2026-09-04**

Scope: semantic design only. No formula, estimator, window, normalization, combination, weight, threshold, probability, update rule or model is selected.

## Frozen governing principle

**Pair-specific abnormality is the state of departure of the current Observed Joint Response from the pair's current Expected Conditional Joint Response, accounting conceptually for Relationship Uncertainty.**

Abnormality is conditional on the frozen G2-01 semantic relationship and the current N0 or N1 reference allowed by G2-03. It is a common pre-mechanism state: it may feed sequential belief updates for M0/M1/M2/M3/U, but it does not identify any mechanism or trading opportunity.

Preserved directional boundaries:

- `opposite-direction movement ≠ automatically abnormal`
- `same-direction movement ≠ automatically normal`

Observed direction is judged only relative to the pair's expected signed and potentially state-dependent conditional response.

## 1. Multidimensional Abnormality State

The primary semantic object is a potentially multidimensional description of how the current joint response departs from its current normal reference. Candidate morphology dimensions remain separate:

| Candidate dimension | Semantic question | What it cannot establish |
|---|---|---|
| Magnitude mismatch | Is the size of one or both observed responses unusual conditional on the current relationship and uncertainty? | Mechanism, direction of resolution or tradability. |
| Signed direction mismatch | Is the observed signed joint/directional response inconsistent with the expected signed response? | Opposite sign is not inherently abnormal; same sign is not inherently normal. |
| Timing mismatch | Is the ordering or response timing unusual relative to expected conditional behavior? | Lead–lag alone does not identify M1. |
| Conditional/residual deviation | What part of the observation is unusual after a later-specified conditioning representation? | A residual is model-dependent and does not identify M3. |
| Relationship-change / break evidence | Does accumulated evidence suggest the normal reference itself may be moving or invalid? | One large deviation does not establish a break or M0. |

Relationship-change/break evidence is retained as a **parallel diagnostic channel** within the broader abnormal-state assessment. It must not be mechanically combined with temporary-departure dimensions in a way that erases the distinction between an unusual observation under a valid relationship and evidence that the relationship itself changed.

No listed dimension is mandatory in a final measurement, and the list does not authorize a factor inventory.

## 2. Continuous Abnormality Summary

A later G2 design may consider a scalar or low-dimensional continuous summary derived from the multidimensional state for ranking, attention allocation or comparison. Such a summary would be a lossy representation and must preserve access to morphology, uncertainty and break diagnostics rather than silently becoming a mechanism label or Pair Score.

No summary formula, dimension reduction, aggregation, weighting, scale or ranking procedure is authorized here. A single summary is optional, not presumed necessary or superior.

## 3. Trigger / Probability Interpretation

Deferred alternatives remain:

- retain the abnormality representation as a continuous state/summary;
- define a later fixed or soft trigger for attention or processing; or
- represent abnormality probabilistically if justified.

No binary trigger, probability, distribution, cutoff, alert rule or decision threshold is frozen. A trigger would control attention/processing, not automatically classify a mechanism or authorize a trade.

## Temporary abnormality versus relationship change/break

| Concept | Semantic meaning | Required separation |
|---|---|---|
| Temporary Abnormality | Current observation is unusual conditional on a relationship still treated as the operative reference. | May motivate continued mechanism/resolution updating; does not imply later normalization. |
| Relationship Change/Break Evidence | Accumulating PIT evidence suggests the operative normal relationship may itself be stale or altered. | Supports uncertainty, rejection or M0/U updating; must not be inferred solely from absence of normalization. |

A large deviation may be compatible with either concept, both under uncertainty, or neither after measurement error. Abnormality magnitude cannot adjudicate the interpretation by itself.

## Anti-circularity implications

- The observation being evaluated must be compared with a reference determined without immediately absorbing that same observation unrestrictedly.
- A flexible N1 reference cannot adapt after seeing the anomaly so as to remove it by construction.
- A fast abnormality observation may update mechanism/resolution beliefs while normal-relationship updating follows separately prespecified eligibility and timing.
- Evidence accumulated for relationship change must remain distinguishable from evidence of a temporary observation.
- Re-estimation timing, buffers, embargoes, update weights and change rules remain unresolved.

## Proposed information flow

`P0/P1 Relationship Information → N0/N1 Relationship State + Relationship Uncertainty → Observed vs Expected Conditional Joint Response → Multidimensional Abnormality State → optional Continuous Summary → Sequential M0/M1/M2/M3/U + Resolution Belief Updates`

This is a semantic flow, not a formula, hard gate, classifier or trade rule. Mechanism and resolution beliefs may update jointly.

## FROZEN SEMANTICS

- Pair-specific abnormality is conditional departure of observed from expected joint/directional response, conceptually accounting for relationship uncertainty.
- The multidimensional abnormality state is primary; candidate morphologies remain conceptually distinct.
- A continuous scalar/low-dimensional summary is optional and subordinate, not the definition itself.
- Trigger/probability interpretation remains a later choice and cannot imply mechanism or trade.
- Temporary abnormality and relationship-change/break evidence remain distinct interpretations/channels.
- Abnormality is a common pre-mechanism state feeding sequential M0–M3/U and resolution-belief updates.
- Signed/state-dependent direction and anti-circularity boundaries above.

## G2 MEASUREMENT DECISION — DEFER

- Observable response variables, event clock, horizons and synchronization.
- Which morphology dimensions become operational candidates.
- Representation, estimator, normalization, uncertainty treatment and missing/stale handling for each dimension.
- Whether/how dimensions are combined, weighted or reduced.
- Whether a continuous summary is needed and its scale/ranking interpretation.
- Fixed/soft/probabilistic trigger alternatives, distributions and thresholds.
- Normal-reference update timing versus abnormality evaluation timing.
- Break/change accumulation and separation from temporary abnormality.
- PIT latency/frequency and data-lineage requirements.

## EMPIRICAL VALIDATION — DEFER

- Calibration and stability of candidate abnormality representations.
- False-abnormality behavior under valid relationships.
- Sensitivity to relationship uncertainty, state changes, sign/asymmetry and synchronization.
- Ability to distinguish temporary departure from relationship change without outcome leakage.
- Cross-pair/industry generalization and A-share machinery transferability.
- Incremental downstream prediction and economic value only after relationship-level validity; PnL cannot define abnormality.

## Approval record

The researcher approved G2-04 as proposed on 2026-09-04. The governing principle, multidimensional primary object, candidate morphology families, optional subordinate continuous summary, deferred trigger/probability interpretation, temporary-versus-break separation, common pre-mechanism role, signed/state-dependent boundary and anti-circularity implications are frozen. All measurement, normalization, weighting, dimensionality-reduction, probability, threshold, estimator, window and update choices remain unresolved exactly as proposed. G2-05 remains unauthorized.
