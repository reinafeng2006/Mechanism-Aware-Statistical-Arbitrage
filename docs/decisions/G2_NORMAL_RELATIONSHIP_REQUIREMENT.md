# G2 Design Requirement — Normal Pair Relationship and Abnormality

**Decision ID:** D-015  
**State:** APPROVED DESIGN REQUIREMENT  
**Authority:** Researcher approval, 2026-09-04  
**Scope:** downstream G2 design only; no model, data, empirical test or G1 evidence change.

## Governing principle

**Industry information determines what dimensions and relationship structure are economically meaningful; pair-specific historical data determine the actual normal relationship for each pair.**

This rejects both an assumed single industry-wide relationship and an unconstrained pair-specific model. It also preserves: `economic similarity ≠ statistical relationship ≠ normal relationship validity ≠ abnormality ≠ trading opportunity`.

## Pair-formation evidence priority — D-016

**Observed point-in-time market relationship evidence is the primary basis for formal pair validity. Company/economic proximity is a secondary candidate prior/context variable whose inclusion requires demonstrated incremental value beyond market-relationship information.**

Formal pair formation must first consider reproducible market/statistical relationship information, including return co-movement, factor-adjusted/residual dependence, beta/exposure similarity, relationship stability/breakdown and other literature-supported relationship representations. No representation is selected by this requirement.

Company/economic proximity is **DEFINED; CANDIDATE SECONDARY PRIOR; NOT CORE; INCLUSION REQUIRES INCREMENTAL VALIDATION**. It may later be considered as a prior, regularizer, tie-breaker, contextual support, rejection/structural-change evidence or aid when relationship history is sparse. Higher company similarity does not imply a better tradable pair.

| Candidate | Meaning | Status |
|---|---|---|
| P0 — Market-Relationship-Only Pair Model | Formal pair validity uses prespecified PIT market/statistical relationship information. | **CANDIDATE / NOT SELECTED** |
| P1 — Market Relationship + Company/Economic Proximity | Same P0 basis plus proximity in a specified secondary role. | **CANDIDATE / NOT SELECTED** |

P1 may remain in a final design only if it demonstrates incremental **relationship-level** value beyond P0 under a prespecified OOS validation protocol. Pair validity, stability and generalization precede final strategy PnL; no metric is frozen here. PF-001 remains evidence only for economic/product-market proximity, not market relationship or trading validity.

## Signed conditional relationship requirement — D-017

A valid pair may exhibit a stable, estimable, signed and potentially state-dependent conditional response relationship. Validity does not require positive correlation or same-direction movement. `Observed Joint Response` versus `Expected Conditional Joint Response` gives candidate pair-specific abnormality. Opposite-direction movement is neither automatically abnormal nor M3.

G2 must allow positive, negative, asymmetric and state-dependent relationships where PIT data support them. Economic Relationship Representation may include competitor, supplier/customer, upstream/downstream, substitute-product and opposite shared-shock exposure, as well as similarity. Company proximity remains secondary. M1 means insufficient movement in expected signed direction; M2 means excessive movement relative to expected conditional response regardless of sign. No formula, factor, estimator or threshold is selected.

## Required normality candidates

| Candidate | Meaning | Status |
|---|---|---|
| N0 — Industry-Uniform Normality Baseline | Common industry-level feature schema and relationship semantics with stronger pooling/common structure across pairs. It is a deliberately simple benchmark, not an assumption that every pair shares one parameter value. | **CANDIDATE / NOT SELECTED** |
| N1 — Pair-Specific Normality Candidate | Uses the same frozen economic/statistical construct definition as N0, while estimating relationship and parameters from each pair's own PIT history. | **CANDIDATE / NOT SELECTED** |
| N2 — Hierarchical / Partial-Pooling Normality | Conceptually, `pair relationship = industry prior + pair-specific adjustment`. | **LATER COMPLEXITY CANDIDATE ONLY — NOT AUTHORIZED** |

N2 can be considered only if an authorized comparison of N0/N1 reveals a clear bias–variance or sample-efficiency problem that simpler specifications cannot resolve.

N0 and N1 must be compared under the **same prespecified construct definition, information set, timing rules and validation protocol**. Pair-specific modeling may not be introduced after inspecting N0 outcomes.

## Abnormality object

The object is **Continuous Pair-Specific Abnormality**: a degree of departure from the pair's estimated normal joint behavior and uncertainty. It is not an already-defined binary divergence trigger.

Possible dimensions to preserve—not select—are magnitude mismatch, directional mismatch, timing mismatch, factor-adjusted/residual deviation, and relationship-break evidence. Formula, dimensionality, normalization, uncertainty treatment and trigger/threshold/probability interpretation are all deferred.

## Explicit G2 question and complexity ladder

**Question:** Should abnormality remain a continuous score, be converted into a fixed/soft trigger, or eventually be represented probabilistically?

`fixed/simple baseline → continuous abnormality score → probabilistic abnormality only if justified`

Greater complexity is not presumed preferable.

## Evaluation boundary for later G2/G4

Normal-relationship specifications must first be evaluated with relationship-level criteria, not final strategy PnL. Candidate dimensions to design later include stability, calibration, OOS normal-response error, parameter instability, false-abnormality behavior, relationship-break behavior and cross-pair generalization. No metric is frozen here.

## Preserved boundaries

No literature claim selects N0, N1, N2 or an abnormality definition. No formula, factor, threshold, data acquisition, relationship model, empirical test or economic result is introduced. G1 remains in progress and G1 evidence records remain unchanged.
