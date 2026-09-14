# V1 RT3-A Relationship-State Augmentation Freeze

Decision date: 2026-09-14

Decision ID: `V1-RT3-A-1.0`

Status: **RESEARCHER APPROVED / FROZEN**

RT3-A authorizes deterministic replay of the seven frozen V1 relationship tuples solely to create an immutable, model-specific event-time relationship-state companion required by frozen A5 RT3. `V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0` remains immutable and authoritative for its existing fields.

Replay must use the exact frozen equations, estimators, PIT inputs, eligibility, H/U tuples, initialization, hyperparameter rules, convergence/boundary states, update cadence, and numerical implementation. It may not add a retry, estimator, floor, feature, model, or Search-Budget branch.

The companion stores only state sufficient to evaluate future authorized inputs under the event-time-frozen relationship function. Future inputs may evaluate `mu^t(x_(t+h),q_(t+h),f_(t+h))`; parameters or states estimated after `t` may not replace the event-time state.

Every replayed common field must be checked against the immutable partition at deterministic equality or the strictest implementation-justified tolerance. Any scientifically material mismatch stops before downstream use at `RT3 RELATIONSHIP REPLAY EQUIVALENCE BLOCKER`.

No performance, ranking, abnormality, target, A6, trading, PnL, OF4, or held-out inspection is authorized during augmentation.

`V1-RT3-A-1.0 — APPROVED / FROZEN`
