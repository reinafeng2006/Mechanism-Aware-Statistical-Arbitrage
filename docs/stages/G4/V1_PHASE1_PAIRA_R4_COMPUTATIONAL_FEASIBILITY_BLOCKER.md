# V1 Phase 1 PAIR-A / R4 Computational Feasibility Blocker

Status: **PHASE 1 SAFELY PAUSED / RESEARCHER DECISION REQUIRED**
Date: 2026-09-14

## Completed

- `V1-EXECUTABLE-SEMANTICS-A1` was frozen, validated, committed as `6ea7a6b`, and pushed before empirical access.
- The EXEC-A-bound 2013–2019 access guard was committed as `dcee301` and pushed before the structural feasibility audit.
- A deterministic audit used only C06 membership/availability, C04 exclusion dates, and sidecar structural states. It read no price, return, relationship, outcome, PnL, OF4, or held-out value.
- PAIR-A was kept complete. No correlation/distance/Top-K/same-code/performance screen or sample approximation was applied.

## Exact blocker

The 2015–2019 inner region contains 1,219 exchange sessions and 46,463,558 contemporaneous unordered candidate pair-dates under complete PIT PAIR-A. Of these, 43,703,661 pair-dates have the prior H63 structural support required by `V1-R4-63D`.

R4-A is frozen as pair-direction-specific `Q/R` prediction-error PIT maximum likelihood inside each H63 formation set with U1D. Therefore it requires:

- **87,407,322 independent pair-direction daily ML fits**;
- at least **5,506,661,286 Kalman state steps for one likelihood sweep**;
- multiple sweeps per L-BFGS-B fit in actual optimization, plus prediction/output work.

This is a lower bound, not a runtime extrapolation from model outcomes. Even perfect batching cannot eliminate the pair-specific objective and daily re-estimation without changing frozen R4 semantics. The current project runtime also lacks an installed scientific optimizer/compiled estimation stack; adding one would improve constants but not remove the orders-of-magnitude workload.

The active action requires an explicit computational-feasibility stop before any approximation or screening. Full Phase 1 therefore did not start.

## Bounded alternatives

### `CF-A — Amend R4 variance-refresh semantics` (recommended)

Keep U1D Kalman predict/evaluate/update, but estimate `Q/R` only at a preregistered sparse calendar refresh (for example U1M) and carry the fitted variance parameters between refreshes. All PAIR-A pair states still update daily. This retains the dynamic model and complete pair universe while cutting ML optimizations by roughly the daily-to-monthly refresh ratio.

Trade-off: changes the frozen R4-A estimation clock and requires a versioned protocol amendment before computation. It is not an engineering-only optimization.

### `CF-B — Defer R4 from V1`

Execute complete PAIR-A for the frozen R0/R1/R3 candidates and move R4-RW to V2 without inspecting results first.

Trade-off: fastest integrity-preserving V1 path, but narrows the already approved seven-tuple MODEL-A scope.

### `CF-C — Supply material dedicated compute`

Retain exact pair-specific daily PIT-ML R4 semantics and execute using a separately provisioned compiled/distributed compute environment with deterministic partitioning and a demonstrated completion budget.

Trade-off: no scientific amendment, but materially higher operational cost and still requires a bounded benchmark before the deadline can be claimed feasible.

### `CF-STOP — Keep V1 paused`

Make no protocol or infrastructure change. No empirical access occurs.

PAIR screening, Top-K, sampling, same-code restriction, shared `Q/R`, or silent U1D-to-U1M substitution are not authorized alternatives.

## Recommendation

Select `CF-A`: preserve complete PAIR-A and daily filtered-state adaptation, but freeze monthly `Q/R` PIT-ML refresh with deterministic carry-forward between refreshes. This isolates the computational relief to variance-hyperparameter re-estimation rather than changing the candidate universe or using results to screen pairs.

Exact next action after approval: publish the R4 clock amendment before empirical access, rerun the structural feasibility estimate under the amended clock, and resume Phase 1 only if the bounded estimate is operationally feasible.

No files are intended to remain uncommitted except the unrelated `.venv/`.

`GENUINE COMPUTATIONAL BLOCKER / RESEARCHER DECISION REQUIRED`
