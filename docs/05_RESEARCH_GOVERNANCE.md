# Research Governance — Current Authoritative State

## Documentation architecture

`Canonical docs = current truth`

`Stage docs = active working state`

`Archive = completed historical process`

Future checkpoints belong under `docs/stages/<stage>/`. No new top-level document may be created unless it is a new canonical current-state document. Formal amendments and freeze records belong under `docs/decisions/`. Moving a record never changes its authority or substantive meaning.

## Current gates

| Gate | Status |
|---|---|
| G0 Economic Thesis | **PASS / FROZEN — 2026-09-03** |
| G1 Literature & Mechanism Evidence | **PASS / FROZEN — 2026-09-04** |
| G2 Measurement & Timing | **G2-01 APPROVED / FROZEN; G2-02 PROPOSED / AWAITING RESEARCHER APPROVAL; DESIGN ONLY; G2-03 NOT AUTHORIZED** |
| G3 Point-in-Time Data & Database | **LOCKED** |
| G4 Statistical Protocol Freeze | **LOCKED** |
| G5 Implementation Readiness | **LOCKED** |
| G6 Development Evidence | **LOCKED** |
| G7 Held-Out Authorization | **LOCKED** |
| G8 Predictive Validation | **LOCKED** |
| G9 Intervention & Economic Validation | **LOCKED** |
| G10 Release / Stop | **LOCKED** |

No gate passes through repository activity alone. Every gate requires an explicit recorded researcher decision. Empirical work, data acquisition, implementation and outcome inspection remain unauthorized.

## Evidence and research-decision discipline

Description, prediction, intervention and economic validation are separate claims. Full-text literature admission, claim-level provenance, evidence ancestry, contradictions, missing links, validation tests, project testability and permitted-use controls remain governed by the Literature OS in `../literature/` and registers in `../registers/`. Learning artifacts explain evidence and decisions but are never evidence sources.

## Point-in-time and causal discipline

Only information lawfully available by the decision time may enter an event-time design. Future catch-up, reversal, convergence or normalization is outcome-only validation. Material artifacts must be deterministic; development and held-out evidence remain separated; stopping rules must be frozen before their relevant empirical inspection.

## Observatory quarantine

Observatory observations, Measurement Gaps and provisional hypotheses are discovery context only. They may not become project evidence or bypass independent construct definition, literature review, measurement design or OOS validation.

## G1 reopening rule

G1 may reopen only if: (1) G2 encounters a decision-critical construct lacking adequate ancestry; (2) a previously inaccessible decision-relevant source becomes lawfully available and may change a permitted-use boundary; or (3) later internal work exposes a material identification problem absent from the frozen synthesis. Model underperformance, poor PnL or desire for additional factors is insufficient. Reopening requires a new recorded researcher decision.

## Historical governance records

The completed G1 hierarchy and Literature OS migration record are preserved in [G1 Stage Hierarchy](archive/G1/G1_STAGE_HIERARCHY.md) and [Literature OS Migration](archive/G1/LITERATURE_OS_MIGRATION.md). Pre-refactor governance snapshots are under `archive/GOVERNANCE/`; the canonical statements in this document are current authority.
