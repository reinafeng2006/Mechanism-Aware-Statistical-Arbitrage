# G4-03B Temporal Validation Architecture Freeze

Decision date: 2026-09-10
Status: **APPROVED / FROZEN**

## Selected architecture

- `TP2 — PRIMARY NESTED TEMPORAL VALIDATION ARCHITECTURE`;
- `TP3 — DIAGNOSTIC OVERLAY ONLY`;
- `TP1 — PREREGISTERED LOWER-COMPLEXITY WALK-FORWARD ROBUSTNESS COMPETITOR`;
- `TP0 — FIXED/BLOCKED SENSITIVITY BASELINE`.

`inner development != outer pseudo-OOS != final held-out`.

TP2 must separately preserve formation/estimation history, inner development/specification selection, outer pseudo-OOS evaluation, and one final sealed held-out region outside all inner/outer activity.

## Outer-loop governance

`outer pseudo-OOS evaluates the preregistered selection procedure; it is not an iterative manual retuning environment`.

After inspecting an outer fold, no manual change to candidate definitions, parameter grids, eligibility rules, target definitions, or selection criteria may occur while later outer folds retain uncontaminated status under the same protocol. A change requires protocol reopening, a contamination record, a new version, and reassessment of unconsumed outer regions. Aggregation and the decision rule for multiple outer folds must be frozen before their results are inspected.

## Robustness boundaries

`TP3 explains heterogeneity; TP3 does not tune the primary specification`.

TP3 cannot rescue, replace, tune, or select the primary specification after results. TP1 and TP0 cannot become opportunistic alternative tuning environments, and favorable results from them cannot override TP2 merely because they are preferred.

## Held-out and calendar boundary

The final held-out region remains sealed, separately authorized, and irreversibly consumed under G4-02. No calendar dates are selected here. G4-03B2 must reconcile the frozen geometry inputs before any development access.
