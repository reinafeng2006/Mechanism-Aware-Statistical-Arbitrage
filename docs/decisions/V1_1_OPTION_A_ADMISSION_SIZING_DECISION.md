# Trading V1.1 Option A admission-sizing decision

Decision date: 2026-09-18.
Status: **RESEARCHER APPROVED — OPTION A; EXECUTION PAUSED BEFORE PNL FOR SIMULTANEOUS-ADMISSION BINDING**.

Ancestry: [single policy inventory](../stages/G5/V1_1_FINAL_SINGLE_POLICY_CHECKPOINT.md), the researcher's morphology-only/both-channel approval, and the subsequent explicit Option A decision. This is a descendant record; no prior frozen artifact is rewritten.

## Approved and not reopened

- Trading V1.1 is an exploratory morphology-based economic probe, not mechanism identification or a continuously rebalanced equal-weight portfolio.
- Six independent candidate books: V1-R0D-252M, V1-R0C-126W, V1-R0L-126W, V1-R1M-126W, V1-R1MI-126W and V1-R3-252M. Both peer/source channels and coexistence remain in scope. Original A6/G5 stays non-estimable/not executed; R4-2025 remains prohibited.
- Observable rejection, invalidity, conflict, PIT and data exclusions remain. Unavailable mechanism evidence stays unavailable. The source channel retains the frozen MP1 ratio requirement. Negative-direction opportunities are execution-unavailable, never reversed.
- Preserve surviving executed episode shares. New entries, unrelated exits, active-count changes, NAV changes and price drift do not resize survivors. Only authorized exits, qualified accounting adjustments and other explicitly frozen mandatory semantics can change those holdings.
- Equal admission sizing means the new episode's raw notional is `V_pre / N`, where N is the active admitted episode count including the proposed new episode. It does not reset surviving positions to 1/N.
- New entry is the largest nonnegative notional no larger than its raw target satisfying remaining 10% security capacity, gross cap 1.0, cash and cost funding. No redistribution of unused capacity or liquidation of survivors to create capacity.
- No positive feasible allocation means FUNDING UNAVAILABLE: no position, turnover, exposure or fabricated fill. Preserve opportunity diagnostics. No retrospective funding or carried failed FD-A entry.
- Passive cap drift is reported, not mechanically corrected to admit another episode. Exit cash is available only after executed exits.
- Retain FD-A next-open entry and the original EP-A/DECA-A identities/conflicts. Peer exit residual is g minus cumulative peer response; source exit residual is e plus cumulative source response. Trigger at nonpositive product with the original anchor, or ten eligible holding sessions counting entry. Evaluate at close, execute no earlier than the next qualified open; known exit suspension delays to the first qualified observed open.
- Normalized fractional book V0=1; zero-return cash; no invented lot, settlement, financing or borrowing contract. Corporate-action/price/identity failures make affected economics unavailable, not zero or survivor-renormalized.
- No fabricated fold-end sale; report qualified terminal marks and open positions. NAV equals cash plus marked shares; daily return is the NAV ratio minus one after actual costs. Preserve approved 252-session reporting, sample-SD volatility, Sharpe, drawdown, turnover, exposure and unavailable states.
- Cost rates are 10 bps primary and mandatory 5/20 bps non-selection sensitivities on executed net security notional. Freeze and validate before first PnL; execute once; no optimization, retuning, filter/holding/direction change, winning-book selection or V2.

## Pre-PnL executable completeness finding

The single-proposal sizing equation does not explicitly bind the episode count for several distinct qualifying proposals at the same execution timestamp. The earlier all-active target-set equation was superseded by Option A; its count cannot silently be carried over to resolve the new admission rule.

Invented example, not an empirical observation: NAV=1, twenty surviving admitted episodes with total holdings=0.4, cash=0.6, and two new long proposals on separate unused securities. All relevant price, quality and eligibility conditions are valid. Costs=10 bps. Security and gross caps and cash are nonbinding for these sizes.

- A batch counting both proposals uses N=22 and raw targets (1/22, 1/22).
- Separate evaluations against the same survivor snapshot each use N=21 and targets (1/21, 1/21).
- Sequential admissions use N=21 then N=22, assigning different shares according to processing order.

These alternatives preserve survivor shares and satisfy the numerical capacity/funding constraints, yet differ in holdings and turnover before any returns occur. The inherited common cash-scaling rule does not resolve this example because cash is not binding. Security-level netting/proportional cap scaling does not resolve it because the securities differ and caps do not bind. EP-A and DECA-A do not select an order across distinct episode identities.

This is an accounting-rule binding, not a runtime optimization. No empirical frequency or impact has been inspected. No alternative is selected in software. Recommended decision: a single simultaneous proposal batch with one pre-execution snapshot and explicit N for that batch; confirm whether N counts all eligible executable proposals before capacity/funding, and retain the already-approved common funding scaling and no survivor resizing. This recommendation is not execution authority.

## State

No trading data, PnL or outcome inspection occurred. No trading runner was launched. NEXT_ACTION remains NONE pending this binding. Publication of this approval/audit record does not claim an executable final policy or a final V1 release.
