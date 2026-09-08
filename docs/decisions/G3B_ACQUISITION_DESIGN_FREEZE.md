# G3B Acquisition Design — Freeze Decision

Decision ID: **G3B-DESIGN-01**  
Date: **2026-09-08**  
Status: **APPROVED / FROZEN**

The four acquisition-design blocks in the [canonical stage artifact](../stages/G3B/G3B_ACQUISITION_DESIGN_PROPOSAL.md) are approved and frozen:

- G3B-A — Acquisition Scope & PIT Universe;
- G3B-B — Provider, Source & Clock Contract;
- G3B-C — Security Master & PIT Integrity;
- G3B-D — Immutable Storage, Provenance & Outcome Quarantine.

## Frozen clarifications

### Fallback substitution

`Canonical Source + documented Fallback Source` does not authorize silent gap patching. A fallback substitution must be explicit, reason-coded, field/date/security scoped, provenance-preserving, separately versioned where needed and auditable downstream. Missing canonical observations do not automatically trigger fallback use, and provider mixing must remain visible to all downstream code.

### Storage versus information availability

`acquisition breadth ≠ model-use authorization`

`stored data ≠ decision-time available data`

Outcome-side information may later be stored for validation only under physical/logical quarantine. Storage does not make it event-time available and does not permit access by feature-generation or mechanism-inference paths.

## Unresolved by design

All items classified `PROVIDER-AUDIT INFORMED`, `FIELD/SCHEMA AUDIT INFORMED`, or `DEFER UNTIL FORMAL ACQUISITION` remain unresolved. No provider, field contract, clock, numerical acceptance threshold, database technology, measurement, model or acquisition execution is selected or authorized by this freeze.
