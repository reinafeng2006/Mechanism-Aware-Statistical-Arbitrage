# G2 Design Requirement — Normal Pair Relationship and Abnormality

**Decision ID:** D-015  
**State:** APPROVED DESIGN REQUIREMENT  
**Authority:** Researcher approval, 2026-09-04  
**Scope:** downstream G2 design only; no model, data, empirical test or G1 evidence change.

## Governing principle

**Industry information determines what dimensions and relationship structure are economically meaningful; pair-specific historical data determine the actual normal relationship for each pair.**

This rejects both an assumed single industry-wide relationship and an unconstrained pair-specific model. It also preserves: `economic similarity ≠ statistical relationship ≠ normal relationship validity ≠ abnormality ≠ trading opportunity`.

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
