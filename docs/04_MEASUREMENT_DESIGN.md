# Measurement Design — Current G2 State

Status: **G2-01 through G2-12 APPROVED / FROZEN — 2026-09-07**. **G3A ACTIVE / AUDIT ONLY / FEASIBILITY NOT DESIRABILITY**; G3B remains locked. No formula, factor, estimator, model, distribution, metric, threshold, window, frequency, update rate, provider, dataset or trading rule is selected.

## Governing authorization

G2 may design measurements for a continuous and uncertain sequential belief-updating system, not a mandatory M0–M3 classifier. It must preserve sequential updating, ambiguity, positive rejection evidence and `U = Unresolved / Abstain`. See the frozen [G2 Handoff Contract](decisions/G2_HANDOFF_CONTRACT.md).

## Dependency-ordered unresolved decisions

1. Economic / signed conditional relationship semantics — **APPROVED / FROZEN**.
2. P0/P1 pair-information architecture — **APPROVED / FROZEN**.
3. N0/N1 normal-relationship candidates and N2 escalation condition — **APPROVED / FROZEN**.
4. Pair-specific continuous abnormality — **APPROVED / FROZEN**.
5. Trigger/discriminator/sequential-updating measurement families — **APPROVED / FROZEN**.
6. M1 signed under-response measurement — **APPROVED / FROZEN SEMANTICS; CANDIDATES UNSELECTED**.
7. M2 pressure and proxy-contamination measurement — **APPROVED / FROZEN SEMANTICS; CANDIDATES UNSELECTED**.
8. M0 positive rejection evidence — **APPROVED / FROZEN SEMANTICS; CANDIDATES UNSELECTED**.
9. M3 non-identification constraint — **APPROVED / FROZEN; PRODUCTION USE BLOCKED**.
10. U/abstention representation — **APPROVED / FROZEN; REPRESENTATIONS UNSELECTED**.
11. PIT timing, frequency, latency and data lineage — **APPROVED / FROZEN; IMPLEMENTATION UNSELECTED**.

The detailed active queue is in [G2 Initial Design Checkpoint](stages/G2/G2_INITIAL_DESIGN_CHECKPOINT.md).

## Existing approved design requirements

P0/P1, N0/N1, later-only N2, signed/negative/asymmetric/state-dependent relationships and continuous pair-specific abnormality retain exactly the statuses and boundaries recorded in [G2 Normal Relationship Requirement](decisions/G2_NORMAL_RELATIONSHIP_REQUIREMENT.md). These requirements do not select raw versus residual representation or any other statistical implementation.

## Frozen G2-01 semantics

The semantic object is a unified framework containing a joint conditional distribution view and distinct directional `i → j` and `j → i` response views, with explicit uncertainty. It permits signed, asymmetric, pair-specific and state-dependent relationships. It separates relationship state, relationship uncertainty, temporary abnormality and relationship change/break, and freezes PIT discipline plus the anti-circularity boundary preventing a current abnormal observation from being immediately absorbed into normality. `relationship validity ≠ trading predictability`. See the formal [G2-01 Freeze Decision](decisions/G2_01_RELATIONSHIP_SEMANTICS.md).

Distributions, estimators, factors, windows, update rates, thresholds, clocks, uncertainty representations and statistical models remain unresolved. No later G2 decision may be answered automatically.

## Frozen G2-02 architecture

P0 is the primary, simpler PIT Market-Relationship-Only architecture, preserving raw joint/co-movement, factor/exposure, conditional/residual, dynamic stability/breakdown and signed/asymmetric/state-dependent information as distinct, non-equivalent families rather than a Pair Score. P1 is unchanged P0 plus a separately identifiable, secondary Economic/Company Relationship layer. Slow P1 information normally remains precomputed/cached relationship context rather than entering latency-critical abnormality/mechanism paths. A newly arriving company event may only become separate timestamped discriminator/rejection evidence if later authorized.

P1 survives only through incremental **normal-relationship-level** value over P0 under the same prespecified PIT information, timing and validation protocol. Superior downstream return prediction or strategy PnL alone cannot establish improved pair validity. No P2 may be introduced without a genuinely distinct, later-justified information architecture. No representation, metric or winner is selected. See the formal [G2-02 Freeze Decision](decisions/G2_02_PAIR_INFORMATION_ARCHITECTURE.md).

## Frozen G2-03 specifications

N0 is the Industry-Structured / Strongly Pooled normality specification, without requiring identical parameters across pairs. N1 targets the same frozen G2-01 semantic relationship object while permitting substantially greater pair-specific PIT parameterization. Differences are limited to pooling strength, parameter sharing, heterogeneity accommodation, information borrowing, sparse-history behavior and adaptation scope. Semantic target, P0/P1 information architecture, PIT boundary, evaluation period, relationship-level objective, outcome-exclusion discipline and anti-circularity remain constant.

N2 partial pooling remains **ILLUSTRATIVE / UNAUTHORIZED** and may be proposed later only if relationship-level evidence establishes a specific bias–variance, instability, sparse-history, calibration or generalization problem that N0/N1 cannot adequately address. Pooling strength is not assumed identical across industries. Final strategy PnL is not the primary selection criterion. See the formal [G2-03 Freeze Decision](decisions/G2_03_NORMAL_RELATIONSHIP_SPECIFICATIONS.md).

## Frozen G2-04 abnormality semantics

Pair-specific abnormality is the potentially multidimensional state of departure of the current Observed Joint Response from the current Expected Conditional Joint Response, conceptually accounting for Relationship Uncertainty. Multidimensional Abnormality State is the primary semantic object. Magnitude, signed direction, timing and conditional/residual deviation are candidate morphology families, not frozen measurements. Relationship-change/break evidence is a parallel diagnostic channel, not a temporary-abnormality synonym.

A scalar or low-dimensional Continuous Abnormality Summary is optional and subordinate rather than the definition itself. Trigger/probability interpretation remains deferred. Abnormality is a common pre-mechanism state feeding sequential M0–M3/U and resolution-belief updates; it identifies neither mechanism nor trade. Signed/state-dependent and anti-circularity principles remain binding. See the formal [G2-04 Freeze Decision](decisions/G2_04_CONTINUOUS_ABNORMALITY.md).

## Frozen G2-05 information-role and feasibility architecture

Four non-equivalent information roles govern information use after abnormality exists: Trigger Evidence, Mechanism Discriminator Evidence, Sequential-Updating Evidence and Rejection/Rival Evidence. `variable identity ≠ signal role`: role depends on construct, hypothesis, context, decision time and PIT availability. The same information type may change role across decision times only when a genuinely new timestamped observation becomes available.

Every future candidate requires construct, role, affected mechanism, theoretically supported effect direction, observation and PIT-availability timestamps, frequency, latency class, cached/critical status, rival interpretation, input/update/outcome status, evidence or Observatory ancestry and authorization metadata. Slow prior/context, medium relationship state, fast abnormality/market evidence and fast sequential updates remain distinct. No activation method, factor, formula, update rule or model is selected. See the formal [G2-05 Freeze Decision](decisions/G2_05_INFORMATION_ROLE_TIMING_ARCHITECTURE.md).

Production / Data Feasibility is a separate design dimension. Every candidate must carry distinct `Research Status` and `Production Feasibility Status` records covering availability, PIT reliability, historical/universe coverage, frequency, acquisition and computation, latency, reproducibility, source stability, proprietary/reconstruction dependency, cacheability and critical-path position. The operational ladder is `EASY / CORE-CANDIDATE → MODERATE → HARD / OPTIONAL → UNAVAILABLE / RESEARCH-ONLY`; it is not an evidence or predictive-value ranking. Harder candidates require later material incremental value at their intended relationship/discrimination/prediction/economic level, and final PnL cannot first justify a difficult relationship-level variable. No candidate is rated or selected here.

## Frozen G2-06 M1 under-response semantics and candidate set

M1 signed under-response is insufficient peer movement in the expected signed direction relative to the current valid PIT conditional relationship. The design separates Expected Signed Response, Observed Response, Signed Response Gap, Response Uncertainty and Under-Response Evidence. A response gap is neither M1 identification nor M1 probability; future catch-up remains validation-only.

UR0 raw signed gap, UR1 uncertainty-standardized gap and UR2 conditional/context-adjusted gap remain competing **ILLUSTRATIVE / UNAUTHORIZED** candidates. Signed gap may be a general abnormality morphology and, separately, an M1-specific transformation after source/link/timing and rival evidence; it cannot redefine the normal relationship. All estimators, clocks, windows, thresholds and models remain unresolved. See the formal [G2-06 Freeze Decision](decisions/G2_06_M1_SIGNED_UNDER_RESPONSE.md).

The frozen semantic orientation defines positive as insufficient movement in the expected signed direction and overshoot as the opposite orientation. Near-zero or too-uncertain expected direction cannot mechanically generate M1 under-response and may remain U. UR2 must separate information already used for Normal/Expected Response, information used to measure the gap and additional discriminator/rival context; repeated conditioning is prohibited. UR0's orientation/subtraction step may be operationally easy, but its end-to-end feasibility inherits the underlying Expected Signed Response specification.

## Frozen G2-07 M2 pressure and contamination architecture

M2 measurement is a nine-part architecture separating Expected Signed Conditional Response, Observed Source Response, Oriented Excess-Move Gap, uncertainty, pressure-source evidence, liquidity/flow-state evidence, proxy-contamination audit, rival evidence and downstream M2 Evidence. Excess movement, volume, turnover, flow and later reversal do not identify temporary pressure or M2.

MP0 excess-move diagnostic, MP1 accessible liquidity/flow context, MP2 pressure-source/contamination-audited diagnostic and MP3 difficult high-frequency permanent/transitory extension remain competing **ILLUSTRATIVE / UNAUTHORIZED** candidates. They form a complexity/information-requirement ladder, not an evidence-strength, identification-quality or model-maturity ranking; greater complexity does not imply better M2 identification. Every proxy requires a Contamination Record and seven-time PIT lineage. Transformation complexity remains separate from inherited end-to-end feasibility. See the formal [G2-07 Freeze Decision](decisions/G2_07_M2_PRESSURE_CONTAMINATION.md).

## Frozen G2-08 M0 rejection architecture

M0 requires positive rejection evidence and cannot be inferred from weak M1/M2/M3 support. Pair Rejection targets the normal relationship; Event/Mechanism Rejection targets the current episode; Decision Rejection/Abstention handles evidence insufficiency without creating M0. `No Trade ≠ M0`, `U ≠ M0`, U does not default to M0, and No Trade may later result from M0, U or economic/decision criteria.

Relationship-break, fundamental/event, structural-linkage, persistent-versus-temporary, data-quality, conflict/ambiguity and downstream M0 evidence remain distinct. R0 relationship warning, R1 event rejection, R2 structural-linkage diagnostic and R3 ambiguity/quality rejection are competing **ILLUSTRATIVE / UNAUTHORIZED** candidates and are not combined into a score. See the formal [G2-08 Freeze Decision](decisions/G2_08_M0_POSITIVE_REJECTION.md).

## Frozen G2-09 M3 non-identification constraint

M3 is preserved as an economic research hypothesis but positive contemporaneous identification is absent. Event-time discriminator and production signal/model use are therefore `BLOCKED — NO POSITIVE IDENTIFICATION BASIS`. Residual/unexplained abnormality, exclusion of M1/M2/M0, opposite direction, apparent temporariness and future normalization cannot generate M3.

Unexplained live cases route to U. A future outcome-defined discovery sample may support research under strict PIT reconstruction, development/held-out separation and G1 reopening governance, but `M3 discovery target ≠ M3 event-time signal ≠ M3 production label`. Future evidence may either upgrade M3 into an identifiable candidate or reject it as unnecessary/non-distinct. See the [G2-09 Freeze Decision](decisions/G2_09_M3_NON_IDENTIFICATION_CONSTRAINT.md).

## Frozen G2-10 U / Abstention representation

U is proposed as a positive, time-indexed epistemic state for insufficiently resolved mechanism belief—not merely a residual threshold bucket. Measurement uncertainty, information insufficiency, mechanism ambiguity, evidence conflict and data/provenance uncertainty remain overlapping diagnostic sources. U is dynamic and may update with genuinely new PIT information without rewriting earlier records.

`U = epistemic state`, `Abstain = decision/action`, and `No Trade = possible downstream outcome` remain separate. U neither defaults to M0/M3 nor mechanically implies Abstain or No Trade. Explicit state, unresolved mass, uncertainty-over-mechanisms, abstention-region and diagnostic-vector representations remain **ILLUSTRATIVE / UNAUTHORIZED** candidates. Mechanism/U probabilities need not sum to one absent a later authorized model. See the [G2-10 Freeze Decision](decisions/G2_10_U_ABSTENTION_REPRESENTATION.md).

## Frozen G2-11 PIT Timing & Data Lineage contract

The frozen common timing vocabulary separates `observation_time`, `public_time`, `available_time`, `compute_time`, `decision_time` and `outcome_time`. Every event-time input requires `available_time ≤ decision_time`; a derived input must also be computed after all upstream inputs are available and before the decision origin. Frequency, observation granularity, publication latency, computation latency and total decision-path latency remain distinct.

The semantic lineage chain is `raw source → source vintage → availability time → transformation/version → derived measurement → downstream use`. It freezes vintage/non-overwrite discipline, genuinely-new-information requirements for sequential updates and timing extensions to Production Feasibility while leaving clocks, frequencies, tolerances, providers and physical database design unresolved. See the [G2-11 Freeze Decision](decisions/G2_11_PIT_TIMING_DATA_LINEAGE.md).

## Active Pre-G3 readiness checkpoint

The approved synthesis conclusion found G2 not ready for data acquisition. G2-12 resolved the five linked pre-audit blockers through versioned candidate envelopes, universe/clock frames, an inheritance graph and data tiers. G3A is authorized audit-only under `G3A evaluates feasibility, not desirability`; G3B acquisition remains locked. See the [G2-12 Freeze Decision](decisions/G2_12_CANDIDATE_MEASUREMENT_REQUIREMENTS_FEASIBILITY_CONTRACT.md) and [Pre-G3 Readiness Checkpoint](stages/G2/G2_MEASUREMENT_DESIGN_SYNTHESIS_PRE_G3_READINESS_CHECKPOINT.md).
