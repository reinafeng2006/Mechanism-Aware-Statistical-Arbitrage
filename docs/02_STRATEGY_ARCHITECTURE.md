# Strategy Architecture — Current Active State

Status: **APPROVED BY D-014 — 2026-09-04**. The original G0 pipeline remains preserved in `archive/G0/G0_FREEZE_DECISION.md`; this is the active operating architecture.

`Company Representation → Industry-Specific Relationship Prior → Pair-Specific Normal Relationship → Continuous Pair-Specific Abnormality → Sequential Mechanism & Resolution Updating → Trade / Update / Reject / Abstain`

| Element | Current responsibility | Status |
|---|---|---|
| Company Representation | PIT, reproducible company/business representation for formal data-driven procedure. | Philosophy frozen; measurement deferred. |
| Industry-Specific Relationship Prior | Industry information defines economically meaningful dimensions and relationship semantics; observed PIT market relationship evidence remains primary for formal pair validity. | D-015/D-016; company proximity is secondary candidate context, measurement deferred. |
| Pair-Specific Normal Relationship | Pair PIT history determines each pair's actual signed, potentially asymmetric/state-dependent conditional joint behavior using the same construct definition as N0. | N0/N1 candidates only; no model selected. |
| Continuous Pair-Specific Abnormality | Degree of departure from pair-specific normal behavior and uncertainty; not a pre-defined binary trigger. | Construct/score/trigger interpretation deferred to G2. |
| Sequential Mechanism & Resolution Updating | Update competing M0–M3 and resolution beliefs jointly as PIT information arrives. | Conceptual architecture only; no model selected. |
| Trade / Update / Reject / Abstain | Act, wait and update, reject, or abstain according to a later frozen policy. | No policy selected. |

P/S/C/R use the meanings frozen by [Amendment 001](decisions/ARCHITECTURE_AMENDMENT_001.md): **P — Relationship Prior**, **S — Abnormality Trigger**, **C — Mechanism Discriminator / Updating Evidence**, and **R — Rejection / Rival Evidence**. M0–M3 remain competing economic hypotheses rather than mandatory mutually exclusive instantaneous labels. `U = Unresolved / Abstain` is an epistemic state, not a fifth mechanism. Any formula such as `belief_(t+1) = update(belief_t, evidence_(t+1))` is **ILLUSTRATIVE / UNAUTHORIZED** until G2 and later gates authorize a design.

The N0/N1/N2 ladder and continuous-abnormality requirement are recorded in [G2 Normal Relationship Requirement](decisions/G2_NORMAL_RELATIONSHIP_REQUIREMENT.md). No normality or abnormality model is selected.

Company/economic proximity is not a default core pair-formation input. P0 (market relationship only) and P1 (market relationship plus proximity) are later comparison candidates; P1 requires incremental relationship-level validation.

Opposite-direction movement is not automatically abnormal or M3. The G2 abstraction is observed joint response versus expected conditional joint response; only their departure is candidate abnormality. See D-017 in `decisions/G2_NORMAL_RELATIONSHIP_REQUIREMENT.md`.

Relationship validity is distinct from trading predictability. Economic relationship, statistical dependence, normal-relationship validity, abnormality and tradable opportunity remain separate constructs. Market/statistical relationship evidence is primary for formal pair validity; company/economic proximity is a secondary candidate prior or context variable and requires incremental relationship-level validation through P1 versus P0.
