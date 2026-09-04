# Active Strategy Architecture

Status: **APPROVED BY D-014 — 2026-09-04**. The original G0 pipeline remains preserved in `G0_FREEZE_DECISION.md`; this is the active operating architecture.

`Company Representation → Pair Relationship Prior → Abnormality Trigger → Sequential Mechanism Tracking + Dynamic Resolution Prediction → Trade / Update / Reject / Abstain`

| Element | Current responsibility | Status |
|---|---|---|
| Company Representation | PIT, reproducible company/business representation for formal data-driven procedure. | Philosophy frozen; measurement deferred. |
| Pair Relationship Prior | Evidence a pair should normally share a relationship; not a guarantee of later trading validity. | Literature partly reviewed; G2 measurement deferred. |
| Abnormality Trigger | Detect an unusual relative state against the relevant normal relationship. | Not operationalized. |
| Sequential Mechanism Tracking + Dynamic Resolution Prediction | Update competing M0–M3 and resolution beliefs jointly as PIT evidence arrives. | Conceptual architecture only; no model selected. |
| Trade / Update / Reject / Abstain | Act, wait and update, reject, or abstain according to a later frozen policy. | No policy selected. |

P/S/C/R use the meanings recorded in Amendment 001. `U = Unresolved / Abstain` is an epistemic state, not a mechanism. Any formula such as `belief_(t+1) = update(belief_t, evidence_(t+1))` is **ILLUSTRATIVE / UNAUTHORIZED** until G2 and later gates authorize a design.
