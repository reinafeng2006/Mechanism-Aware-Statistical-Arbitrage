# G4-04A3 Continuous Abnormality Metric Specification Freeze

Status: **G4-04A3 APPROVED / FROZEN — 2026-09-11**
Boundary: pre-empirical abnormality-metric design only. No frozen-data inspection, relationship fitting, abnormality computation, thresholding, mechanism inference, target construction, or outcome access.

## Objective and estimand

Specify how the frozen Multidimensional Abnormality State may be measured as the departure of the current Observed Joint Response from the pair's PIT Expected Conditional Joint Response, conceptually accounting for Relationship Uncertainty.

The exact estimand is the current observation-level signed directional departure and its multidimensional qualification state relative to the PIT expected directional response under one authorized relationship representation—not a mechanism label, resolution probability, trade trigger, or trading opportunity.

## Frozen semantic boundaries inherited

- opposite-direction movement is not automatically abnormal;
- same-direction movement is not automatically normal;
- abnormality is relative to the expected signed, asymmetric, potentially state-dependent relationship;
- temporary abnormality remains distinct from Relationship Change/Break Evidence;
- current abnormal observations cannot be immediately absorbed into normality;
- abnormality precedes and does not identify M0/M1/M2/M3/U;
- no binary trigger or scalar summary is required.

## Proposed measurement layers

### A3-L0 — Directional response-departure components

The fundamental primitives are:

`departure_(i->j,t) = observed_response_(i->j,t) - PIT_expected_response_(i->j,t)`

`departure_(j->i,t) = observed_response_(j->i,t) - PIT_expected_response_(j->i,t)`

Positive and negative values retain their raw response-coordinate meaning. A3 does not orient signs toward M1 under-response, M2 excess-response, or another mechanism. Mechanism-specific orientation belongs only to a later authorized layer. Retain both directions separately before higher aggregation.

### A3-L0S — Candidate-neutral scaled departure

`scaled_departure_(d,t) = departure_(d,t) / candidate_neutral_PIT_scale_(d,t)`.

The scale inherits the frozen A1/A1a/A1b MAD architecture, separate directional construction, and A1c hard-failure/continuous-quality rules.

`abnormality scaling != candidate-specific forecast uncertainty`.

Candidate uncertainty cannot enter the denominator or mechanically shrink point abnormality. An unavailable, non-finite, exactly zero, or mathematically unsupported scale makes the scaled component unavailable. Near-zero but nondegenerate scale remains continuous `SCALE QUALITY` evidence with no epsilon replacement.

### A3-L1 — Primary multidimensional abnormality state

Preserve separate channels containing at minimum:

- raw signed directional departure for both directions;
- candidate-neutral scaled departure and magnitude for both directions;
- measurement/relationship uncertainty state;
- structural/relationship-validity state, including parallel Relationship Change/Break Evidence;
- timing/PIT and version metadata sufficient to reconstruct the observation.

Candidate morphology extensions may additionally retain timing mismatch and representation-specific conditional/residual deviation. No channel is combined into a weighted score.

Relationship-break evidence is a diagnostic channel, not automatically a component to be added into temporary-abnormality magnitude.

### A3-L2 — Optional continuous summary

A scalar or low-dimensional Continuous Abnormality Summary may later support attention, ranking, or monitoring only. It remains subordinate to the multidimensional state and cannot define abnormality, identify M0/M1/M2/M3, become a probability, create a trade decision, erase direction/uncertainty/validity/scale quality, or introduce a threshold in A3. Formula and weights remain unresolved.

### A3-L3 — Trigger/probability interpretation

Fixed trigger, soft trigger, ranking, resource-budget, or probabilistic interpretation remains deferred. No A3 measurement is itself a trigger or mechanism belief.

`abnormality != mechanism identification`.

The same state may later support competing M1, M2, M0, or U updates. M3 remains non-identified and receives no abnormality-to-M3 mapping.

## Candidate metric roles

| Evidence object | Proposed role |
|---|---|
| Signed directional scaled departure | **PRIMARY MORPHOLOGY COMPONENT** |
| Absolute directional scaled departure | **MAGNITUDE COMPONENT** |
| Directional mismatch state | **SUPPORTING MORPHOLOGY DIAGNOSTIC** |
| Timing mismatch | **CANDIDATE MORPHOLOGY / MEASUREMENT-DEFER** |
| Conditional/residual deviation | **REPRESENTATION-CONDITIONAL COMPONENT** |
| Relationship Change/Break Evidence | **PARALLEL RIVAL/REJECTION DIAGNOSTIC** |
| Continuous summary | **OPTIONAL SUBORDINATE DERIVATION** |

All formulas and combination rules remain unresolved.

## Uncertainty and scale quality

Point-departure scaling uses the candidate-neutral PIT MAD architecture. Candidate-specific relationship uncertainty is a separate evidence channel and cannot widen the denominator to make the point departure appear smaller.

Unavailable, non-finite, zero, or mathematically unsupported scale makes the scaled component unavailable. Near-zero nondegenerate scale remains a continuous quality diagnostic. Missing uncertainty output does not automatically invalidate a point-departure candidate.

Uncertainty describes precision or knowledge about the expected response/measurement; it does not redefine the observed-minus-expected departure. Structural validity describes whether temporary-abnormality inference remains legitimate; it does not add to abnormality magnitude.

## Structural eligibility propagation

`raw observation eligibility != abnormality-computation eligibility`.

Every abnormality computation must derive a versioned candidate-specific eligibility decision from the frozen Security-Date Eligibility Sidecar plus the frozen candidate rule. Dataset freeze and raw observation presence do not clear structural states.

- `CORPORATE_ACTION STATUS UNRESOLVED` cannot automatically become extreme economic abnormality evidence; the C04 rule must mark the component unavailable, constrained, or separately qualified.
- `UNKNOWN MISSINGNESS` cannot become zero movement, a forward-filled response, a synthetic observation, or a synthetic departure.
- Relationship Change/Break Evidence remains a parallel validity/rejection diagnostic and cannot be added mechanically to temporary-abnormality magnitude.
- C05, C06, identifier lineage, provenance, scale state, and exclusion reasons remain attached downstream.

## Anti-circularity ordering

For decision time `t`:

`pre-response PIT information -> frozen normal-relationship state/version -> PIT expected directional response -> current observed response -> directional departure -> abnormality state -> any later relationship update under its frozen rule`.

The current observation cannot first enter the same-decision normal-relationship estimate in a way that erases its own departure. This order holds under U1D refresh: daily refresh does not imply contemporaneous absorption of the observation being evaluated.

## Representation-aware, mechanism-neutral states

Each surviving relationship representation may produce its own authorized abnormality state under the same semantics, timing, scaling, eligibility, and metadata contract. Representation identity/version remains attached. Representation-specific abnormality states cannot be pooled, averaged, selected, or combined before the representation-selection protocol permits it.

## Temporal and PIT contract

Every component must bind observation time, available time, compute time, decision time, relationship-state version, expected-response version, scale version, directional target, eligibility-rule version, and candidate role. Later normalization, reversal, catch-up, persistence, break, or PnL cannot enter the event-time abnormality object.

## Aggregation and CS2

- preserve observation-level directional components before pair-level representation;
- retain an equal-status directional vector;
- prevent observation-rich pairs from dominating later representation comparison;
- report common support for comparing abnormality specifications and native support for coverage/deployability;
- preserve temporal magnitude, consistency, dispersion, severe failure, and support separately;
- prohibit a compensatory weighted abnormality score unless separately justified and authorized.

## SR0 / SR1 boundary

SR0 may cover unavailable/invalid inputs, PIT leakage, mathematically unsupported scale, violated representation contract, or unreproducible computation. Large or small abnormality, poor ranking behavior, unstable morphology, or weak later validation are SR1/continuous evidence—not structural invalidity.

## Proposed comparison family

Competing abnormality representations serving the same frozen morphology/summary estimand form an A-family comparison downstream of an admissible frozen normal-relationship representation. Point-departure, uncertainty, break diagnostics, and optional summaries retain separate claim roles; they do not form an unrestricted tournament.

## Unresolved decisions

1. exact observed/expected directional response interval and units;
2. treatment of expected response near zero or directionally unreliable without mechanism orientation;
3. exact magnitude mapping from signed scaled departure;
4. definitions for timing and representation-specific conditional/residual morphology;
5. representation of relationship/measurement uncertainty alongside point departure;
6. candidate-specific C04/C05 and missing/undefined computation rules;
7. whether and how a subordinate continuous summary is constructed;
8. common/native-support comparison estimands and aggregation;
9. temporal aggregation and independently justified severe-failure semantics;
10. A-family multiplicity and claim roles;
11. trigger/probability interpretation, deferred beyond A3 metric specification.

No abnormality threshold, probability, trigger, weighted score, trading interpretation, or model is authorized here.

`G4-04A3 APPROVED / FROZEN`
