# C04/C05 Measurement Eligibility Matrix

Status: **APPROVED / FROZEN UNDER G3B-C1 — NO MEASUREMENT AUTHORIZED**

These classifications describe structural eligibility only. They do not alter the frozen G2B candidate classes, select specifications, or permit empirical computation.

| G2B candidate family | Proposed structural eligibility | C04/C05 dependency and required later rule |
|---|---|---|
| P0-RAW, RR-DIST, RR-CORR | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Raw paths exist, but action-contaminated observations and unknown missing sessions require explicit exclusion/uncertainty treatment; distance/correlation remain baselines only. |
| P0-EXP, RR-EXPOSURE | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Exposure inputs do not remove price/action or missing-session contamination in the security response path. |
| P0-RES, RR-RESID, A-RES | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Conditioning lineage plus C04/C05 observation eligibility must be declared; residualization cannot cleanse unknown corporate actions by assertion. |
| P0-STAB, A-BREAK, R0 | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Missing sessions or corporate actions may mimic instability/breaks; positive break evidence requires explicit rival handling. |
| P0-SIGN, RR-SIGNED, N0, N1 | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Estimable in principle from core histories, but signed normal-response estimation requires eligible observations and continuity rules. N0/N1 remain mandatory fair-comparison candidates. |
| N2 | **BLOCKED** | Already unauthorized unless escalation conditions are met; C04/C05 availability does not change that status. |
| GOV-FDR, GOV-MATCH | **ELIGIBLE IN PRINCIPLE WITH CORE DATA** | Construction governance can be designed from the preserved universe/metadata, but any tested relationship statistic inherits its own C04/C05 eligibility. |
| A-MAG, A-SIGN, A-TIME | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Corporate actions and unknown sessions may manufacture magnitude, direction, or timing mismatch. |
| A-SUM | **CONSTRAINED** | Optional subordinate summary inherits every included morphology's unresolved eligibility. |
| ROLE-TRIG, ROLE-DISC, ROLE-UPD, ROLE-RIVAL | **ELIGIBLE IN PRINCIPLE WITH CORE DATA** | Information-role architecture remains usable; a concrete signal inherits the eligibility of its upstream measurements. |
| UR0, UR1, UR2 | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Expected and observed responses must use eligible histories; UR1/UR2 additionally inherit uncertainty/conditioning burdens. Response gap remains non-identifying. |
| MP0 | **ELIGIBLE ONLY AFTER C04/C05 RULE** | A corporate action or unexplained missing interval may resemble an excess move. MP0 remains an abnormality diagnostic, not M2 identification. |
| MP1 | **ELIGIBLE ONLY AFTER C04/C05 RULE** | Raw volume/amount context is retained, but session eligibility and denominator-dependent E02-B limitations remain explicit. |
| MP2 | **CONSTRAINED** | Pressure-source and contamination lineage remain incomplete; C04/C05 rules alone cannot supply exogeneity. |
| MP3 | **BLOCKED** | Remains research-only/blocked; lack of MP3 does not block M2. |
| R1 | **CONSTRAINED** | Positive event rejection also requires qualified event-time public/available-time evidence; C04 disclosures alone are incomplete. |
| R2 | **CONSTRAINED** | Structural-link histories remain sparse and identifier continuity cannot establish economic continuity. |
| R3 | **ELIGIBLE IN PRINCIPLE WITH CORE DATA** | Explicit C04/C05 gaps, provenance, and unknown missingness may inform ambiguity/data-quality handling, normally supporting U rather than M0. |
| M3-DISC | **BLOCKED** | M3 production identification remains absent; outcome-side discovery remains separately quarantined. |
| U0, U4 | **ELIGIBLE IN PRINCIPLE WITH CORE DATA** | Core quality/provenance states can support an unresolved-state representation; no uncertainty formula or policy is selected. |
| U1, U2 | **CONSTRAINED** | These inherit an as-yet-unselected belief/uncertainty model and all upstream observation eligibility. |
| U3 | **BLOCKED** | Decision-policy representation remains outside current measurement scope. |

Cross-cutting rule: a candidate marked `ELIGIBLE IN PRINCIPLE WITH CORE DATA` still requires its previously frozen G2 authorization and implementation protocol. It is not empirically authorized by this matrix.

Propagation rule: computation must reject or explicitly route observations whose durable C04/C05 states do not satisfy the candidate's approved rule. Dataset freeze or transformation never promotes an unresolved state to eligible, and every eligibility decision must retain rule/version lineage.
