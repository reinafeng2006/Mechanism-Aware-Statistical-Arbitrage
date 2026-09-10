# G4-01 Candidate Eligibility Rule Matrix

Status: **APPROVED / FROZEN — NO MASK OR MEASUREMENT AUTHORIZED**

This matrix translates the frozen G3B-C1 eligibility classes into protocol obligations. It does not change any G2B candidate classification.

| Frozen G2B family | Frozen structural class | Candidate-specific rule obligation before computation | Decision class |
|---|---|---|---|
| P0-RAW, RR-DIST, RR-CORR | ELIGIBLE ONLY AFTER C04/C05 RULE | Declare raw-record, unresolved-C04, unknown-session, window-support, and pair-synchronization treatment; retain baseline-only meaning | **CANDIDATE-SPECIFIC** |
| P0-EXP, RR-EXPOSURE | ELIGIBLE ONLY AFTER C04/C05 RULE | Apply underlying price-history rule plus PIT exposure availability and membership lineage | **CANDIDATE-SPECIFIC** |
| P0-RES, RR-RESID, A-RES | ELIGIBLE ONLY AFTER C04/C05 RULE | Apply underlying observation rule; bind conditioning information/availability; prohibit residualization from silently cleansing C04/C05 states | **CANDIDATE-SPECIFIC** |
| P0-STAB, A-BREAK, R0 | ELIGIBLE ONLY AFTER C04/C05 RULE | Separate missing/action/identifier changes from candidate relationship-change evidence; no future-confirmed break input | **CANDIDATE-SPECIFIC** |
| P0-SIGN, RR-SIGNED, N0, N1 | ELIGIBLE ONLY AFTER C04/C05 RULE | Preserve signed/asymmetric support, C04/C05 states, identity transitions, and common N0/N1 eligibility comparison | **CANDIDATE-SPECIFIC** |
| N2 | BLOCKED | No mask until the frozen escalation condition and separate authorization are satisfied | **FREEZE SEMANTICS NOW** |
| GOV-FDR, GOV-MATCH | ELIGIBLE IN PRINCIPLE WITH CORE DATA | Governance universe may be defined structurally; each tested statistic/pair inherits its own candidate rule and support | **CANDIDATE-SPECIFIC** |
| A-MAG, A-SIGN, A-TIME | ELIGIBLE ONLY AFTER C04/C05 RULE | Prevent action/missing-session artifacts from silently becoming morphology; preserve ordered/synchronized support | **CANDIDATE-SPECIFIC** |
| A-SUM | CONSTRAINED | Inherit every included morphology's mask and disclose support loss; no summary-specific override | **CANDIDATE-SPECIFIC** |
| ROLE-TRIG, ROLE-DISC, ROLE-UPD, ROLE-RIVAL | ELIGIBLE IN PRINCIPLE WITH CORE DATA | Role metadata may be instantiated, but concrete signals inherit every upstream candidate mask/version | **CANDIDATE-SPECIFIC** |
| UR0, UR1, UR2 | ELIGIBLE ONLY AFTER C04/C05 RULE | Expected/observed response histories must pass their candidate masks; retain weak-direction/U and conditioning lineage | **CANDIDATE-SPECIFIC** |
| MP0 | ELIGIBLE ONLY AFTER C04/C05 RULE | Prevent actions/unknown gaps from becoming apparent excess moves; retain `excess move ≠ M2 identification` | **CANDIDATE-SPECIFIC** |
| MP1 | ELIGIBLE ONLY AFTER C04/C05 RULE | Bind raw activity/session eligibility and distinguish E02-A from denominator-dependent E02-B limitations | **CANDIDATE-SPECIFIC** |
| MP2 | CONSTRAINED | Require separately qualified pressure-source, contamination, rival, and upstream observation eligibility | **CANDIDATE-SPECIFIC** |
| MP3 | BLOCKED | No production mask; research-only status unchanged | **FREEZE SEMANTICS NOW** |
| R1 | CONSTRAINED | Require qualified event public/available time in addition to eligible response history | **CANDIDATE-SPECIFIC** |
| R2 | CONSTRAINED | Require dated structural-link lineage; identifier continuity is insufficient | **CANDIDATE-SPECIFIC** |
| R3 | ELIGIBLE IN PRINCIPLE WITH CORE DATA | May preserve unresolved structural states as quality/ambiguity evidence, normally routing to U; cannot convert unknowns into M0 | **CANDIDATE-SPECIFIC** |
| M3-DISC | BLOCKED | No event-time/production mask; outcome discovery remains separately quarantined | **FREEZE SEMANTICS NOW** |
| U0, U4 | ELIGIBLE IN PRINCIPLE WITH CORE DATA | May propagate structural uncertainty/quality states without a probability or action rule | **CANDIDATE-SPECIFIC** |
| U1, U2 | CONSTRAINED | Inherit future belief/uncertainty representation and all upstream masks | **CANDIDATE-SPECIFIC** |
| U3 | BLOCKED | Decision-policy representation remains outside measurement scope | **FREEZE SEMANTICS NOW** |

Cross-family numerical choices—including minimum support, allowed gap burden, C04 treatment, transition buffer, staleness tolerance, and common support—remain **NUMERICAL PROTOCOL DECISION LATER**. Statistical adequacy and sensitivity remain **EMPIRICAL VALIDATION LATER**.
