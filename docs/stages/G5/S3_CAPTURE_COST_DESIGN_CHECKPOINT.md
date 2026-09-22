# S3 capture and cost gate — design checkpoint

> Historical gate comparison. The researcher subsequently [selected transparent joint scenario decomposition](../../decisions/S3_CAPTURE_COST_SCENARIO_DIRECTION_SELECTION.md) as design direction only; direct gross-payoff forecasting remains a documented alternative. Detailed choices remain proposals in the [scenario-model checkpoint](S3_CAPTURE_COST_SCENARIO_MODEL_DESIGN_CHECKPOINT.md). Statements below about an unselected direction describe the earlier gate. Original body preserved.

2026-09-22. DESIGN PROPOSALS ONLY / RESEARCHER DECISION REQUIRED.

The researcher has [preregistered alpha_ref=0.05 and z0=Q^w_0.95(|z^ref|)](../../decisions/S3_REFERENCE_TAIL_PROBABILITY_PREREGISTRATION.md). Numerical z0 remains unestimated. The [scale architecture](../../decisions/S3_SCALE_ARCHITECTURE_APPROVAL.md) is unchanged. This gate discusses how to estimate m_hat_u and c_hat_RT,u before entry; it does not select or fit a forecast, choose instruments, estimate costs, or authorize data access.

## 1. Economic question and common units

A rare current residual is not a forecast of subsequent capture. Keep three distinct objects:

- Remaining original basket displacement d_u, after overnight movement.
- Gross economic opportunity m_hat_u: an ex-ante forecast of signed basket gains/cash flows under a specified holding and liquidation policy, before separately counted costs.
- All-in cost c_hat_RT,u: an ex-ante forecast of the full entry-to-liquidation cost of that same basket/policy.

Both economic quantities must use the same proposed initial gross capital K_u and entry decision information set I_(u-), not unrelated return or currency denominators. The conceptual gate remains m_hat_u > c_hat_RT,u, alongside statistical abnormality, the original-gap no-reversal condition and complete executability. It is not evaluable until the forecast, reference prices and execution contract are frozen and qualified. No safety margin, confidence level or cost buffer is chosen here.

## 2. Remaining opportunity before committing capital

Retain the parent [fixed-origin basket proposal](TRADING_STRATEGY_ECONOMIC_REDESIGN_CHECKPOINT.md). For illustration of units, under its qualified-price/accounting assumptions:

Delta B_ON = sum_k w_kt*(P^0_ku/P_kt−1);
d_u = d_t−Delta B_ON;
L_u = sum_k |w_kt|*P^0_ku/P_kt;
g_u = |d_u|/L_u.

P^0_ku is a declared entry reference available at the admission decision; w_t is the original aligned basket. g_u is the gross-capital-normalized remaining target distance, not an expected return or guaranteed maximum gain. Full target capture at reference prices would correspond to that displacement; overshoot, non-resolution, reversal and delayed liquidation produce different outcomes.

Preserve d_t*d_u>0. Overnight target exhaustion does not reset the target or create an opposite trade. Corporate actions require entitlement-consistent prices/holdings; unqualified intervals do not become zero movement.

Timing must be explicit: a realized opening fill cannot be used to decide an order that had to be submitted before that fill was observable. A later execution contract must choose available pre-order quotes/auction information or a decision after an observable open with a subsequent executable fill. Do not assume exact fills at the observed open. Entry-price uncertainty belongs in the joint forecast/cost mapping. This document selects neither timing protocol.

## 3. Capture forecast alternatives

Let n_u be the candidate signed share vector and tau its future liquidation time under a separately frozen policy. Define a proposed reference-price gross payoff:

G_u(tau) = [sum_k n_ku*(P^0_k,tau−P^0_ku) + D_u(tau)]/K_u.

D includes qualified signed contractual security cash flows, including distributions owed on short legs if assigned here. Prices and cash flows must reconcile corporate actions. Financing, borrow and execution frictions are excluded from G and counted once in costs. The stopping policy, basket clock, treatment of suspension, recall and delayed exits remain unapproved dependencies; no ten-session default is adopted.

The forecast target is m_hat_u = estimated E[G_u(tau) | I_(u-), proposed basket and policy]. It must include adverse and unresolved economic outcomes, not only successful convergence cases.

| Construction | Meaning | Strength | Limitation |
|---|---|---|---|
| A: joint scenario decomposition | m_hat_u=sum_j p_hat_j*u_j, with u_j=estimated conditional mean gross payoff in mutually exclusive, exhaustive policy outcomes | Makes non-resolution, adverse movement, duration and forced-liquidation effects visible; can share scenarios with costs | Scenario partition, probabilities, payoff/duration estimators and evidence are not supplied by the relationship models |
| B: direct conditional gross-payoff forecast | Estimate the same E[G given pre-entry information] directly under one frozen model/specification | Targets the actual economic quantity without requiring separately estimated scenario probabilities | More opaque failure/duration behavior; can hide unsupported regions or excessive fitting freedom unless carefully constrained |

Possible scenario concepts include target-triggered liquidation, policy horizon without resolution, and forced/delayed liquidation. These are illustrations, not a selected partition. Ordering/overlap rules must be frozen before labels are created. A target touch is not necessarily successful economic capture after the execution delay.

A shorthand m_hat_u=rho_hat_u*g_u is valid only if rho_hat is explicitly defined as the signed expected capture ratio of this whole payoff distribution. It is not automatically 1, a probability, or restricted to [0,1]. A hit-probability-times-gap formula omitting payoffs on misses and losses is insufficient. Neither residual z nor its 5% reference rarity supplies p_hat, rho_hat or m_hat.

Recommendation for consideration: use A as the first transparent specification path, with one finite, preregistered scenario/payoff/duration construction; retain B only as a design alternative if the researcher prefers a direct forecast. Do not run both and select on profitability. No scenario model, features, estimator family, training window, probability, payoff or capture fraction is approved here.

## 4. All-in round-trip cost construction

Proposed accounting form:

C_RT = C_entry + C_exit(tau) + C_borrow(tau) + C_funding/collateral(tau) + C_other;
c_hat_RT,u = estimated E[C_RT/K_u | I_(u-), same basket, size and liquidation policy].

| Component | What a future pre-entry specification must bind |
|---|---|
| Entry and exit execution | Signed quantities for every leg; commissions, exchange/clearing/mandatory charges; spread, slippage, impact and any qualified order-related charges; side/instrument-specific treatment |
| Borrow | Availability/locate qualification as a feasibility prerequisite; rates, rate changes and duration of short obligations; recall/buy-in effects under the declared policy |
| Funding and collateral | Cash borrowing, collateral/margin funding, contractual rebates/credits where qualified, settlement timing and netting rules; short-sale proceeds are not automatically free cash |
| Holding and liquidation | Expected duration distribution, delayed/suspended exits and forced liquidation; forecasts of exit notional and liquidity using entry-available information, not realized future values |
| Cash-flow allocation | Every dividend, manufactured distribution or other entitlement allocated exactly once between G and C; no double counting or hidden omission |

Use reference-price gross returns plus explicit execution frictions consistently, or an explicitly approved fill-price convention that omits already-embedded frictions. The table follows the former proposal. The spread cannot appear both in assumed adverse fills and as an added fee; adverse reference-price movement during delay is not itself a fee.

A scenario-consistent cost estimate is c_hat_RT,u=sum_j p_hat_j*c_hat_j using the same outcome/duration distribution as capture. Within a scenario, costs must account for joint rate, notional, duration and liquidity behavior; multiplying unrelated averages need not equal expected accumulated cost. A cost that depends on size requires the gate to be reevaluated at the eventual proposed size under a separately frozen sizing protocol. This gate does not choose that protocol.

Do not substitute old 5/10/20-bps scenarios as demonstrated all-in hedged-basket costs. Do not assume zero borrow, zero impact, constant exit liquidity or a nominal holding cap that guarantees an executable exit. No provider, instrument, fee schedule, rate, impact model or numerical cost is selected or inspected.

## 5. Uncertainty, feasibility and missingness

Recommendation for consideration: begin with the explicit expected-gross-versus-expected-all-in-cost contract, accompanied by separate uncertainty/support diagnostics. A stricter rule using a lower capture bound and upper cost bound is a possible later researcher choice, but needs specified confidence/robustness meaning; no quantile, multiplier or arbitrary haircut is adopted here.

Neither a positive estimated difference nor an exact residual hedge proves profitable execution. Borrow availability, exact model-to-instrument mapping, collateral sufficiency and joint-leg fills are hard feasibility prerequisites to the later execution gate; making a cost larger cannot substitute for absent feasibility.

If capture evidence, required rates, accounting, geometry or policy-conditioned support is missing, the economic gate is UNAVAILABLE. Do not assign zero cost, certainty of capture, zero return on an unknown path, or an unhedged substitute. Scientific abnormality remains a separate record. Qualified adverse outcomes belong in the forecast; unobserved paths need an approved missingness/censoring treatment, not success-only deletion or zero imputation.

The common six-estimator comparison keeps one forecast/cost procedure, units and permitted complexity. Candidate-specific basket composition and costs may differ; this is not permission for six separately optimized trading systems. Signs require separate diagnostics without threshold retuning.

## 6. What must be decided before any estimation

The researcher must bind the economic target and liquidation policy, forecast path A or B, permissible predictors/model complexity, temporal training/validation boundaries, support/missingness treatment, and whether an uncertainty-based margin is required. These are open design questions, not defaults supplied here.

The cost side additionally needs an approved reference-price accounting convention, leg-level component definitions, policy-consistent duration/size treatment, and evidence requirements. Exact instruments, borrow/funding contracts and joint execution mechanics remain later execution prerequisites. Dependencies may require returning to this design gate; they do not justify inventing a forecast now.

Any later capture-model development would need separate authorization for qualified forward outcomes. The fixed primary alpha=0.05 must not be tuned using that work. Numerical reference-quantile estimation also remains a separate bounded action after the reference specification is complete. No empirical task is activated by this checkpoint.

## 7. Stop record

Completed: persisted direct probability preregistration and prepared the design comparison above from canonical design records only. No historical data, reference quantile, capture forecast, costs, forward labels, backtest or PnL accessed/computed. No S3 implementation, C04 repair, acquisition or hedge-execution contract selected.

Recommended next researcher action: resolve the capture forecast target/path and cost accounting/uncertainty specification at this gate, then authorize only a specifically bounded subsequent task. NEXT_ACTION remains NONE.

**S3 CAPTURE + COST GATE DESIGN / RESEARCHER DECISION REQUIRED**
