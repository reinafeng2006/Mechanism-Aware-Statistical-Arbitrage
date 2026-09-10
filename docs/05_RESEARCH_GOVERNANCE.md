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
| G2 Measurement & Timing | **G2-01 through G2-12 APPROVED / FROZEN** |
| G3 Point-in-Time Data & Database | **LOCKED** |
| G3A PIT Data / Provider Feasibility Audit | **APPROVED / COMPLETE / FEASIBILITY NOT DESIRABILITY** |
| G3B Formal PIT Data Acquisition Design | **APPROVED / FROZEN — 2026-09-08** |
| G3B Formal Data Acquisition Execution | **NOT AUTHORIZED / LOCKED** |
| G3B-01 Provider & Field Contract Resolution | **APPROVED / FROZEN — G3B-02 AUDIT AUTHORIZED** |
| G3B-02 Provider / Field / Schema / PIT Qualification Audit | **ACCEPTED / COMPLETE — AUDIT ONLY** |
| G3B-03 C06 Historical Industry Membership Qualification Closure | **ACCEPTED / FROZEN — FORMAL ACQUISITION LOCKED** |
| Final Formal Acquisition Proposal | **APPROVED / FROZEN — G3B-QA ONLY AUTHORIZED** |
| G3B-QA Bounded Acquisition & Structural Validation | **PARTIALLY COMPLETE / BLOCKED BY AUTHORIZED MARKET-DATA ACCESS — FULL-UNIVERSE EXPANSION LOCKED** |
| G3B-QA-R1 Authorized Market-Data Access Resolution | **COMPLETE / AWAITING RESEARCHER DECISION** |
| G3B-QA-R2 Priority Access Execution | **INSTITUTIONAL ENTITLEMENT NOT VERIFIED / TUSHARE QA BLOCKED PENDING RESEARCHER-CONFIGURED CREDENTIAL** |
| G3B-QA Sina bounded fallback | **COMPLETE — FALLBACK ONLY / AWAITING RESEARCHER REVIEW** |
| G3B-QA-R3 Governance Companion Data Qualification | **COMPLETE / AWAITING RESEARCHER REVIEW** |
| G3B-MV Minimum Viable PIT Acquisition Contract | **PROPOSED / AWAITING RESEARCHER APPROVAL — FORMAL ACQUISITION LOCKED** |
| G3B-R4 Paid / Institutional Source Value Comparison | **ACCEPTED — EXTERNAL ACCESS / QUOTATION PENDING — NO PURCHASE AUTHORIZED** |
| CSMAR / RESSET Access & Quotation Audit | **ACCEPTED — PUBLIC/NON-AUTHENTICATED LIMIT REACHED** |
| G3B External Access Pending | **PENDING RESEARCHER-CONTROLLED ENTITLEMENT OR QUOTATION — NO INTERNAL RESEARCH BLOCKER** |
| G3B-R5 Expanded Commercial Source Shortlist | **ACCEPTED / FROZEN — PUBLIC DISCOVERY CLOSED — NO PURCHASE AUTHORIZED** |
| G3B Source Consolidation / Minimum Source Count | **APPROVED / FROZEN — HARD PIT/LINEAGE REQUIREMENTS SUPERSEDE CONSOLIDATION** |
| Integrated Historical Research Platform Qualification | **DIRECT PURCHASE BRANCH PAUSED — LOW-COST RECONSIDERATION AWAITING REVIEW** |
| G3B-R6 Low-Cost Integrated Source Qualification | **ACCEPTED / FROZEN — JQDATA PROVISIONAL BEST LOW-COST INTEGRATED** |
| G3B-R7 JQData Authenticated Qualification | **PAUSED — ACCESS COST EXCEEDS RESEARCHER BUDGET** |
| G3B-R8 Tushare Authenticated Integrated QA | **ACCEPTED / COMPLETE — PROPOSED PRIMARY SUBJECT TO FINAL ACQUISITION CONTRACT** |
| G3B Tushare Final Acquisition Readiness | **APPROVED / FROZEN — G3B-FULL AUTHORIZED** |
| G3B-FULL Formal PIT Historical Acquisition | **COMPLETE / FROZEN — CORE-DATASET-FREEZE-V1** |
| G3B-C1 Structural Data Contract Amendment | **APPROVED / FROZEN — NO DATASET OR MEASUREMENT AUTHORIZATION** |
| G3B-F2 Core Dataset Freeze Readiness | **COMPLETE / PASS — CORE DATASET FREEZE APPROVED** |
| G3B-R9 Tushare Permission Delta / E02 Resolution Audit | **OPTION A SELECTED — 2000+ POINT TIER CONFIRMED / NO ADDITIONAL PURCHASE** |
| G3B-R9 Tushare Authenticated Permission Re-check | **PASS — C01/E02 ACCESS BLOCKER RESOLVED / PIT-VINTAGE LIMITATIONS PRESERVED** |
| G2B Implementable Measurement Specification Narrowing | **APPROVED / FROZEN — 2026-09-08** |
| G4 Statistical Protocol Freeze | **ACTIVE: INITIALIZATION / DESIGN ONLY — DECISION QUEUE AWAITING RESEARCHER REVIEW** |
| G4-01 Observation, Window & Pair Eligibility Protocol | **APPROVED / FROZEN — ALL NUMERICAL DECISIONS DEFERRED / NO COMPUTATION** |
| G4-02 Temporal Partition, Development/Held-Out & Information Boundary | **APPROVED / FROZEN — NUMERICAL AND STRUCTURAL PARTITIONS UNRESOLVED / NO COMPUTATION** |
| G4-03 Numerical Sample, Temporal Partition & Validation Architecture | **ACCEPTED AS THREE-BLOCK DECISION SCAFFOLD — NO CANDIDATE SELECTED** |
| G4-03A Sample & Estimation Geometry | **APPROVED / FROZEN — NUMERICAL TOLERANCES AND SUPPORT THRESHOLDS UNRESOLVED / NO COMPUTATION** |
| G4-03B Temporal Validation Architecture Selection | **PROPOSED / AWAITING RESEARCHER REVIEW — NO DATA ACCESS OR COMPUTATION** |
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

## Dataset freeze and measurement eligibility

`Core Dataset Structural Freeze ≠ Candidate Measurement Authorization`. Raw-data preservation does not make every observation eligible. `CORPORATE_ACTION STATUS UNRESOLVED` and `UNKNOWN MISSINGNESS` are durable downstream controls: freeze and transformation cannot clear or silently recode them. Candidate computation must enforce the approved C04/C05 eligibility rule with traceable rule/version lineage. `raw observation exists ≠ observation eligible for every measurement`.

## Observatory quarantine

Observatory observations, Measurement Gaps and provisional hypotheses are discovery context only. They may not become project evidence or bypass independent construct definition, literature review, measurement design or OOS validation.

## G1 reopening rule

G1 may reopen only if: (1) G2 encounters a decision-critical construct lacking adequate ancestry; (2) a previously inaccessible decision-relevant source becomes lawfully available and may change a permitted-use boundary; or (3) later internal work exposes a material identification problem absent from the frozen synthesis. Model underperformance, poor PnL or desire for additional factors is insufficient. Reopening requires a new recorded researcher decision.

## Historical governance records

The completed G1 hierarchy and Literature OS migration record are preserved in [G1 Stage Hierarchy](archive/G1/G1_STAGE_HIERARCHY.md) and [Literature OS Migration](archive/G1/LITERATURE_OS_MIGRATION.md). Pre-refactor governance snapshots are under `archive/GOVERNANCE/`; the canonical statements in this document are current authority.
