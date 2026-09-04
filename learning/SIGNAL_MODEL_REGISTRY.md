# Cross-Mechanism Signal Model Registry

Status: **LEARNING / TRACEABILITY ONLY**. Entries are concepts or candidate measurements, never frozen factors or trade rules. All formulas/model families below are **ILLUSTRATIVE / UNAUTHORIZED**.

| Name | Role | Mechanisms | Intuition / attempted construct | Candidate inputs | Illustrative form | Rival / PIT / latency | Ancestry | Status / unresolved work |
|---|---|---|---|---|---|---|---|---|
| P0 market relationship layer | Relationship | all | Describe PIT signed conditional dependence while keeping raw joint, exposure, conditional/residual, stability/break and signed/state families distinct | returns, exposures, residuals, stability history | `R_t=relationship(PIT history)` | representation-dependent; fast observations + medium relationship state | CL-PF-002–007/009; G2-02 | FROZEN ARCHITECTURE; measurement unresolved |
| P1 economic/company layer | Relationship/Rejection | all, M0 | Secondary economic relationship prior, sparse-history support or stale-link context added separately to unchanged P0 | dated company/product/exposure representations | `P1 = P0 + declared economic layer` | does not imply price validity; slow prior, normally cached | CL-PF-001; D-016; G2-02 | FROZEN SECONDARY LAYER; normal-relationship-level incremental validation required |
| Relationship stability/break evidence | Relationship/Rejection | M0/U | Test whether the normal reference remains credible | rolling PIT relationship history | `break_evidence_t` | extreme observation is not itself break; medium state | CL-PF-004/005 | CANDIDATE; method and materiality unresolved |
| Continuous pair abnormality | Detection | all | Departure of observed from expected conditional joint response | observed response, relationship state, uncertainty | `A_t=departure(Y_t,R_t,U_t)` | may reflect noise, break or mechanisms; fast trigger | D-015/D-017; G2-01 | CANDIDATE; formula/dimensions unresolved |
| M1 source-link-timing evidence | Discriminator/Updating | M1/U | Linked public source moves while peer under-responds in expected signed direction | PIT link vintage, source event/time, source and peer response | `b_M1,t=h(link,event,underresponse,rivals)` | common shock/private news/stale link; fast update | CL-M1-001/003 | SUPPORTED FOR G2 DESIGN; not hard gate |
| M1 rival-information checks | Rejection/Updating | M1/M0/U | Weaken clean delayed-incorporation attribution | peer own-news, market/industry news, pre-event move | no formula selected | first-public timestamps required; fast update | CL-M1-001/003 | SUPPORTED candidate R/C; measurement unresolved |
| M2 pressure-source evidence | Discriminator/Updating | M2/U | A plausibly temporary pressure source strengthens over-movement interpretation | lawful flow context, lagged overlap, calendar/settlement context | `b_M2,t=h(source,liquidity,response,rivals)` | motives/endogeneity and release lag; slow prior + fast update | CL-M2-001/003 | SUPPORTED FOR G2 DESIGN; not exogenous label |
| M2 contamination/liquidity checks | Rejection/Updating | M2/M1/M0/U | Separate pressure from information and contaminated proxies | flow construction, returns, volume, turnover, quotes, liquidity | no formula selected | flow can contain returns; illiquidity ≠ oversupply; fast update | CL-M2-002/004; CL-B4-002 | SUPPORTED candidate checks; measurement unresolved |
| M0 positive rejection evidence | Rejection | M0/U | Evidence that relationship or arbitrage interpretation is invalid | structural/link change, fundamentals/news, persistent break, funding constraints | `reject_evidence_t` | absence of M1/M2/M3 is insufficient; mixed latency | CL-M0-001; CL-PF-001/004/005 | SUPPORTED FOR G2 DESIGN; no M0-by-elimination |
| M3 residual context | Discriminator/Rejection | M3/U | Record unexplained abnormality without promoting it to mechanism | fundamental/news controls, residual abnormal move | no positive score authorized | omitted information/model error; fast/medium | CL-M3-001; CL-PF-007; CL-B4-001 | DESCRIPTIVE ONLY; WEAK/NON-IDENTIFIED |
| Resolution outputs | Resolution | all | Eventually estimate direction, magnitude, timing, persistence, catch-up, reversal, normalization and break persistence | frozen PIT history only | `Q_t(outcome|F_t)` | realized future path is target, never event input | D-014; CL-M1-001/003; CL-M2-001–004 | G2/G4 PENDING; no model selected |
| Decision output | Decision | all/U | Eventually map beliefs and uncertainty to action | relationship, abnormality, mechanism/resolution beliefs, uncertainty | `policy(inputs)→Trade/Update/Exit/Reject/Abstain` | costs/constraints and OOS required | D-014; G1-04 | NOT STARTED; no decision rule authorized |

Registry taxonomy: **signal concept ≠ candidate measurement ≠ frozen factor ≠ model output ≠ trade rule**. Candidate inputs are inventory fields, not selected providers or database specifications.

## G2-03 normality specifications — frozen semantics

| Candidate | Relationship role | What differs | What stays fixed | Status |
|---|---|---|---|---|
| N0 | Industry-structured / strongly pooled reference | Greater shared/common structure | G2-01 semantic target, P0/P1 layer within comparison, PIT/evaluation and outcome exclusion | FROZEN SEMANTICS; no identical-pair-parameter requirement |
| N1 | Pair-specific reference | Greater pair PIT parameterization and flexibility | Same target and fair-comparison boundary as N0 | FROZEN SEMANTICS; not presumed superior |
| N2 | Hierarchical / partial pooling | Conceptually shared structure + pair deviation | Requires specific relationship-level evidence and separate approval | **ILLUSTRATIVE / UNAUTHORIZED** |

Pooling strength may differ by industry. No pooling estimator, Industry Homogeneity Score, update rate, window, metric or model is selected.
