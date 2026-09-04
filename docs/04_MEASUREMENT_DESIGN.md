# Measurement Design — Current G2 State

Status: **G2 ACTIVE — DESIGN ONLY**. **G2-01 and G2-02 APPROVED / FROZEN — 2026-09-04**. **G2-03 PROPOSED / AWAITING RESEARCHER APPROVAL**; G2-04 is not authorized. No formula, factor, estimator, model, distribution, metric, threshold, window, frequency, classifier, filter, provider, dataset or trading rule is selected.

## Governing authorization

G2 may design measurements for a continuous and uncertain sequential belief-updating system, not a mandatory M0–M3 classifier. It must preserve sequential updating, ambiguity, positive rejection evidence and `U = Unresolved / Abstain`. See the frozen [G2 Handoff Contract](decisions/G2_HANDOFF_CONTRACT.md).

## Dependency-ordered unresolved decisions

1. Economic / signed conditional relationship semantics — **APPROVED / FROZEN**.
2. P0/P1 pair-information architecture — **APPROVED / FROZEN**.
3. N0/N1 normal-relationship candidates and N2 escalation condition — **PROPOSED / AWAITING RESEARCHER APPROVAL**.
4. Pair-specific continuous abnormality — **UNRESOLVED**.
5. Trigger/discriminator/sequential-updating measurement families — **UNRESOLVED**.
6. M1 signed under-response measurement — **UNRESOLVED**.
7. M2 pressure and proxy-contamination measurement — **UNRESOLVED**.
8. M0 positive rejection evidence — **UNRESOLVED**.
9. M3 non-identification constraint — **UNRESOLVED**.
10. U/abstention representation — **UNRESOLVED**.
11. PIT timing, frequency, latency and data lineage — **UNRESOLVED**.

The detailed active queue is in [G2 Initial Design Checkpoint](stages/G2/G2_INITIAL_DESIGN_CHECKPOINT.md).

## Existing approved design requirements

P0/P1, N0/N1, later-only N2, signed/negative/asymmetric/state-dependent relationships and continuous pair-specific abnormality retain exactly the statuses and boundaries recorded in [G2 Normal Relationship Requirement](decisions/G2_NORMAL_RELATIONSHIP_REQUIREMENT.md). These requirements do not select raw versus residual representation or any other statistical implementation.

## Frozen G2-01 semantics

The semantic object is a unified framework containing a joint conditional distribution view and distinct directional `i → j` and `j → i` response views, with explicit uncertainty. It permits signed, asymmetric, pair-specific and state-dependent relationships. It separates relationship state, relationship uncertainty, temporary abnormality and relationship change/break, and freezes PIT discipline plus the anti-circularity boundary preventing a current abnormal observation from being immediately absorbed into normality. `relationship validity ≠ trading predictability`. See the formal [G2-01 Freeze Decision](decisions/G2_01_RELATIONSHIP_SEMANTICS.md).

Distributions, estimators, factors, windows, update rates, thresholds, clocks, uncertainty representations and statistical models remain unresolved. No later G2 decision may be answered automatically.

## Frozen G2-02 architecture

P0 is the primary, simpler PIT Market-Relationship-Only architecture, preserving raw joint/co-movement, factor/exposure, conditional/residual, dynamic stability/breakdown and signed/asymmetric/state-dependent information as distinct, non-equivalent families rather than a Pair Score. P1 is unchanged P0 plus a separately identifiable, secondary Economic/Company Relationship layer. Slow P1 information normally remains precomputed/cached relationship context rather than entering latency-critical abnormality/mechanism paths. A newly arriving company event may only become separate timestamped discriminator/rejection evidence if later authorized.

P1 survives only through incremental **normal-relationship-level** value over P0 under the same prespecified PIT information, timing and validation protocol. Superior downstream return prediction or strategy PnL alone cannot establish improved pair validity. No P2 may be introduced without a genuinely distinct, later-justified information architecture. No representation, metric or winner is selected. See the formal [G2-02 Freeze Decision](decisions/G2_02_PAIR_INFORMATION_ARCHITECTURE.md).

## Active G2-03 proposal

N0 is proposed as the industry-structured/strongly pooled simpler normality benchmark, without requiring identical parameters across pairs. N1 targets the same frozen G2-01 semantic relationship object while permitting substantially greater influence from pair-specific PIT history. Allowed differences concern pooling, parameter sharing, heterogeneity, information borrowing, sparse-history behavior and adaptation scope; semantic target, information architecture, PIT/evaluation boundary, relationship-level objective, outcome exclusion and anti-circularity must remain constant.

N2 partial pooling remains **ILLUSTRATIVE / UNAUTHORIZED** and may be proposed later only if a specific N0 underfit, N1 uncertainty/instability, sparse-history or relationship-level calibration/generalization problem cannot be adequately handled by N0/N1. Pooling strength must not be assumed identical across industries. See [G2-03 Working Proposal](stages/G2/G2_03_NORMAL_RELATIONSHIP_SPECIFICATIONS_PROPOSAL.md).
