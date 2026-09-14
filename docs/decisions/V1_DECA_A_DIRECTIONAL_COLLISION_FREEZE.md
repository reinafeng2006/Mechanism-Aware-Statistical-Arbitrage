# V1 DECA-A Directional Collision Freeze

Date: 2026-09-14
Status: **APPROVED / FROZEN / PENDING PUBLICATION**
Contract: `V1-DECA-A-1.0`

## Frozen rule

`SIMULTANEOUS BIDIRECTIONAL ENTRY ELIGIBILITY WITHIN THE SAME UNORDERED PAIR × POLICY CHANNEL -> DIRECTIONAL ENTRY CONFLICT / NO NEW POSITION`.

For an unordered pair and frozen policy channel:

- exactly one entry-eligible direction opens the corresponding episode under EP-A;
- simultaneous eligibility of `i -> j` and `j -> i` creates no position and records `DIRECTIONAL ENTRY CONFLICT`;
- both underlying directional scientific records remain unchanged.

`DIRECTIONAL ENTRY CONFLICT` is neither M0, U by definition, nor model failure. It is a trading-eligibility state: the frozen evidence does not identify one executable direction for that pair/channel at that decision event.

No directional ranking, stronger-signal selection, magnitude tie-break, first-observed priority, random tie-break, or bidirectional/two-leg replacement is permitted in V1. DECA-B and DECA-C are V2/future-only registrations.

If an EP-A episode is already active, its existing `BLOCKED RE-ENTRY` semantics control. A collision cannot reset, replace, stack onto, alter, or add PnL/exposure to the active episode.

Conflict events remain diagnostic metadata. Their count/rate may be reported when the governing result-inspection contract permits, but cannot be used to redesign this rule after inspection.

This decision was frozen before model fitting, abnormality, target, trade/PnL, OF4, or held-out inspection.

