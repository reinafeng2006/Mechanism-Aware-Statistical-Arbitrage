# Measurement Design — Current G2 State

Status: **G2 ACTIVE — DESIGN ONLY**. Current checkpoint: **G2-01 PROPOSED / AWAITING RESEARCHER APPROVAL**; G2-02 is not authorized. No formula, factor, estimator, model, distribution, threshold, window, classifier, filter, provider, dataset or trading rule is selected.

## Governing authorization

G2 may design measurements for a continuous and uncertain sequential belief-updating system, not a mandatory M0–M3 classifier. It must preserve sequential updating, ambiguity, positive rejection evidence and `U = Unresolved / Abstain`. See the frozen [G2 Handoff Contract](decisions/G2_HANDOFF_CONTRACT.md).

## Dependency-ordered unresolved decisions

1. Economic / signed conditional relationship semantics — **PROPOSED; AWAITING APPROVAL**.
2. P0/P1 pair-information architecture — **UNRESOLVED**.
3. N0/N1 normal-relationship candidates and N2 escalation condition — **UNRESOLVED**.
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

## Active G2-01 proposal

The proposal defines the semantic object as a framework containing a joint conditional distribution view and distinct directional `i → j` and `j → i` response views, with explicit uncertainty. It separates relationship state, relationship uncertainty, temporary abnormality and relationship change/break, and proposes a PIT anti-circularity boundary. All mathematical notation remains illustrative. See [G2-01 Working Proposal](stages/G2/G2_01_RELATIONSHIP_SEMANTICS_PROPOSAL.md).

Until approved, these semantics are proposed rather than frozen. No later G2 decision may be answered automatically.
