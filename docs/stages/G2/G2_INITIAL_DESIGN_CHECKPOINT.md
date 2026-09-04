# G2 — Initial Measurement & Timing Design Checkpoint

Status: **ACTIVE — INITIALIZATION / DESIGN ONLY; DECISIONS UNRESOLVED**  
Authority: approved G1-04 Evidence Freeze and frozen `../../decisions/G2_HANDOFF_CONTRACT.md`, 2026-09-04.
Boundary: this checkpoint structures decisions. It selects no formula, factor, model, estimator, threshold, window, classifier, filter, provider, dataset or trading rule.

## Governing design objective

G2 designs measurements for a sequential belief-updating system, not a mandatory M0–M3 classifier. Abnormality, mechanism evidence and resolution evidence may remain continuous and uncertain. Sequential updating, ambiguity, positive rejection evidence and `U = Unresolved / Abstain` must remain representable without forced discrete assignment.

## Dependency-ordered researcher decisions

All rows are **UNRESOLVED — RESEARCHER DECISION REQUIRED BEFORE MEASUREMENT FREEZE**. Candidate families are preserved for comparison, not selected.

| Order | Decision group | Researcher decision to be resolved | Required boundary / dependency | Frozen ancestry |
|---:|---|---|---|---|
| 1 | Economic / signed conditional relationship semantics | Define the common economic/statistical construct vocabulary and what constitutes an expected signed, negative, asymmetric or state-dependent conditional response. | Must precede pair validity and normality measurement; positive co-movement is not required. | D-017; CL-PF-001–007/009/010 |
| 2 | P0/P1 pair-information architecture | Define a fair, prespecified P0 market-relationship-only design and P1 secondary company/economic-prior addition, including the permitted role of proximity. | P1 must show incremental relationship-level value beyond P0; no PnL-first retention. | D-016; CL-PF-001–007/009/010 |
| 3 | N0/N1 normal-relationship specifications; N2 escalation | Specify comparable N0 and N1 design candidates under the same construct, information set, timing and validation protocol; prespecify the condition that could later authorize N2 consideration. | Depends on 1–2; N2 remains later complexity only and cannot be introduced after outcome inspection. | D-015; CL-PF-002–007/009 |
| 4 | Pair-specific continuous abnormality | Decide which departure dimensions and uncertainty representation deserve operational candidates and how normality validity is separated from abnormality. | Depends on 3; preserve magnitude, direction, timing, residual and break as unselected possibilities. | D-015/D-017; CL-PF-002–007/009 |
| 5 | Trigger / discriminator / sequential-updating families | Define non-overlapping measurement roles, update clocks and how continuous/uncertain evidence enters ongoing mechanism and resolution beliefs. | Depends on 4; no mandatory classifier or hard M1/M2 gates. | D-014; G1-04 clarification; CL-M1-001/003, CL-M2-001–004, CL-B4-002 |
| 6 | M1 under-response | Define candidate PIT under-response relative to the expected signed response, source/link/timing inputs, and rival-information checks. | Depends on 1, 3 and 5; future follower catch-up is validation-only. | CL-M1-001/003 |
| 7 | M2 pressure and proxy contamination | Define candidate PIT pressure-source, liquidity-state, abnormal response and rival checks, plus controls for endogenous/return-contaminated proxies. | Depends on 4–5; reversal is validation-only; volume/flow/illiquidity alone is non-identifying. | CL-M2-001–004; CL-B4-002 |
| 8 | M0 positive rejection evidence | Define operational candidates for structural/fundamental/link-break/funding invalidation and distinguish persistent break from temporary abnormality. | Depends on 3–5; M0 cannot be assigned by elimination. | CL-M0-001; CL-PF-001/004/005 |
| 9 | M3 non-identification constraint | Encode that unexplained residual movement cannot produce a positive M3 label and specify what, if anything, may remain descriptive context. | Depends on 6–8; absence of M1/M2/M0 evidence is not M3. | CL-M3-001; CL-PF-007; CL-B4-001 |
| 10 | U / abstention representation | Define how ambiguity, insufficient evidence, rival explanations and measurement failure lead to continuing update, rejection or abstention without inventing a fifth mechanism. | Depends on 5–9; forced state assignment is prohibited. | Competing-mechanism Claim block in `../../decisions/G2_HANDOFF_CONTRACT.md` |
| 11 | PIT timing, frequency, latency and lineage | Define decision timestamps, availability/vintage rules, update latency classes, required histories, missing/stale handling and lineage fields for every retained measurement candidate. | Cross-cuts 1–10 and must be fixed before handoff to G3; providers and acquisition remain unauthorized. | `../../archive/G1/G1_03_DATA_REQUIREMENT_MAP.md`; all linked Claim IDs except excluded DR-008 |

## Later G2 freeze obligations

Before G2 can be frozen, the approved decisions must collectively specify construct definitions, comparable candidates, PIT timing and causal availability, trigger/discriminator/update roles, rejection/abstention handling, evidence/data lineage, and relationship-level validation design. They must preserve all alternatives and prohibitions in the G2 Handoff Contract.

This checkpoint does not authorize answering these decisions through assumption. It does not activate G3 or authorize data acquisition, implementation, outcome inspection or empirical analysis.
