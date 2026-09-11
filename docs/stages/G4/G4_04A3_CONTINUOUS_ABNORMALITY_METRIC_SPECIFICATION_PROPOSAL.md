# G4-04A3 Continuous Abnormality Metric Specification Proposal

Status: **PROPOSED / AWAITING RESEARCHER REVIEW**
Boundary: pre-empirical abnormality-metric design only. No frozen-data inspection, relationship fitting, abnormality computation, thresholding, mechanism inference, target construction, or outcome access.

## Objective and estimand

Specify how the frozen Multidimensional Abnormality State may be measured as the departure of the current Observed Joint Response from the pair's PIT Expected Conditional Joint Response, conceptually accounting for Relationship Uncertainty.

The estimand is the magnitude and morphology of current conditional departure—not a mechanism label, resolution probability, trade trigger, or trading opportunity.

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

Retain separate candidate-neutral PIT-scaled departures for `i -> j` and `j -> i`, using the frozen A1 scale-quality rules. Signed and absolute forms have different roles: signed departure preserves morphology; absolute departure expresses size. Neither direction is silently averaged.

### A3-L1 — Multidimensional morphology vector

Preserve separately, where a representation supports them:

- magnitude mismatch;
- signed-direction mismatch;
- timing mismatch;
- conditional/residual deviation;
- parallel Relationship Change/Break Evidence.

Relationship-break evidence is a diagnostic channel, not automatically a component to be added into temporary-abnormality magnitude.

### A3-L2 — Optional continuous summary

A scalar or low-dimensional summary may later support ranking or attention allocation, but remains subordinate to the morphology vector. It cannot erase direction, uncertainty, break evidence, scale-quality state, or provenance.

### A3-L3 — Trigger/probability interpretation

Fixed trigger, soft trigger, ranking, resource-budget, or probabilistic interpretation remains deferred. No A3 measurement is itself a trigger or mechanism belief.

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

1. exact signed directional departure definition and orientation;
2. treatment of expected response near zero or directionally unreliable;
3. definitions for magnitude, direction, timing, and conditional/residual morphology;
4. representation of relationship uncertainty alongside point departure;
5. whether and how a subordinate continuous summary is constructed;
6. morphology-specific missing/undefined handling;
7. common/native-support comparison estimands;
8. temporal aggregation and independently justified severe-failure semantics;
9. A-family multiplicity and claim roles;
10. trigger/probability interpretation, deferred beyond A3 metric specification.

No abnormality formula, normalization beyond the frozen scale architecture, weight, threshold, probability, trigger, or model is selected here.

`G4-04A3 CONTINUOUS ABNORMALITY METRIC SPECIFICATION PROPOSED / AWAITING RESEARCHER REVIEW`
