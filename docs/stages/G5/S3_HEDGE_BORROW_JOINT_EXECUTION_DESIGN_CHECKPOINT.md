# S3 hedge, borrow and joint execution — design checkpoint

2026-09-22 — DESIGN ONLY / RESEARCHER DECISION REQUIRED.

The [minimal capture/cost architecture](../../decisions/S3_MINIMAL_SCENARIO_CAPTURE_COST_ARCHITECTURE_APPROVAL.md) is approved: F/P/N/A/X, pooled P1, joint duration/exposure, one all-leg cost ledger and E1. P3 remains inactive. This document proposes the execution contract those objects require. All detailed execution choices below remain proposals. No instrument, provider, borrow contract, numerical parameter or empirical feasibility finding is selected.

## 1. Common contract and model-to-instrument mapping

Use a versioned decision-origin mapping from model return coordinates to actual unique instrument coordinates. Freeze coefficient versions, identities, price/return definitions, factor vintages, corporate-action conventions and basket ancestry. An intercept is not a traded leg; it stays in the initial modeled discrepancy without assuming new daily alpha accrual.

### R0-D252, R0-C126, R0-L126

Their directional OLS bridge residual is epsilon=y_j−alpha−beta*y_i. Exact return-coordinate weights are (j,i)=(1,−beta). R0-D distance and R0-C correlation never become hedge ratios. R0-C/R0-L equality remains duplicate-equation evidence, not two independent confirmations.

### R3-252

Use alpha_p=alpha_G+conditional_pair_intercept and beta_p=beta_G+conditional_pair_slope, preserving the fitted conditional pair geometry. The residual basket is (1,−beta_p); do not substitute a population slope or refit it for hedge performance.

For R0/R3, direct shares can represent that origin return basket under matching qualified prices and cash-flow accounting. This establishes a mapping, not stable market neutrality, a cointegrating equilibrium or borrow feasibility. If beta<0, the two coefficients have the same sign; do not force a long/short pattern or flip beta. If beta=0 the counterpart coefficient is algebraically zero, not permission to drop any nonzero factor/hedge leg.

### R1-M126: full market expansion

With residual-bridge beta_u and leg factor regressions a_k+b_k*m:
gamma_M=b_j−beta_u*b_i;
a0=alpha_u+a_j−beta_u*a_i;
epsilon=y_j−beta_u*y_i−gamma_M*m−a0.

Model weights on (j,i,market) are (1,−beta_u,−gamma_M). Pair-only shares omit the market component and are not the approved residual object.

### R1-MI126: full industry and market expansion

Let gamma=(b_j−beta_u*b_i, delta_j, −beta_u*delta_i) on (market,industry-j,industry-i). Then:

epsilon=y_j−beta_u*y_i−gamma' f−a0,

with weights (1,−beta_u,−gamma_M,−delta_j,+beta_u*delta_i). Preserve the original PIT industry binding, constituent qualification and both-pair-member exclusions. Identical factor coordinates can be combined algebraically; distinct industries cannot be blended for convenience.

### Required replication identity

For tradable instrument return vector r_H and holdings h, exact replication requires h' r_H=gamma' f under the declared return/accounting convention on the relevant domain. If r_H=Gamma*f+e, Gamma' h=gamma is necessary for matching loadings but leaves h'e; it is not sufficient for exact replication.

The executable residual basket becomes y_j−beta_u*y_i−h' r_H−a0. Define tracking residual e_track=h'r_H−gamma'f; executable residual=model residual−e_track. Known loadings alone cannot set e_track to zero.

A future mapping manifest must specify the instruments, exposure/replication identity, all nonzero coefficients, history support, factor and instrument cash-flow conventions, and the scope of exactness. No instruments or estimates are supplied by this document.

## 2. Exact replication versus tracking-aware exposure

| Path | What must hold | Design consequence |
|---|---|---|
| Exact residual replication | Model and instrument response/cash-flow definitions reconcile, not just fitted factor loadings; fixed-origin holding mapping also valid | Retains the approved statistical object if proved; current feasibility UNKNOWN |
| Tracking-aware proxy | Explicit tracking process remains between factor model and executable basket | Requires an approved amended signal/scale/target or separately justified tracking treatment and capture/cost implications; no implicit approval |

Recommend exact alignment as the first-version requirement. Do not declare R1 feasible without proof, and do not admit approximate instruments merely because their correlation is high. Tracking-error exposure is NOT approved in this task; it remains a researcher alternative requiring an explicit amendment and pre-access specification.

A daily rebalanced factor-return series is not generally reproduced by fixed origin shares over a multi-session holding period. Exact one-session factor replication is not sufficient to establish exact holding-period target replication. A self-financing rebalanced replica would add trades/costs and change the fixed-share execution protocol; a static substitute can change the factor/target object. Neither is adopted here.

If exact fixed-origin replication cannot be demonstrated for a candidate, mark HEDGE MAPPING UNRESOLVED / S3 SIGNAL UNAVAILABLE under the existing alignment rule, retaining any descriptive model residual separately. Do not manufacture an executable S3 signal, omit factor legs, or silently remove the candidate from common-support threshold estimation. No scientific estimator is declared a winner or loser.

## 3. Signed shares and gross capital

After an exact mapping, let a_l,t be coefficients on unique tradable instruments l at signal close, including j, i and all factor-replicating legs. Aggregate identical physical instruments algebraically within the same basket before computing actual instrument gross exposure. This does not grant cross-episode netting or borrow/collateral offsets.

For positive reference entry marks O^0_l,u and qualified signal marks P_l,t:

Delta B_ON=sum_l a_l,t*(O^0_l,u/P_l,t−1);
d_u=d_t−Delta B_ON;
s=sign(d_u), require d_t*d_u>0;
L_u=sum_l abs(a_l,t)*O^0_l,u/P_l,t;
n_l=s*K_ref*a_l,t/(P_l,t*L_u).

Then sum_l abs(n_l)*O^0_l,u=K_ref and gross reference price movement/K_ref=s*Delta B_u/L_u. g_u=abs(d_u)/L_u is full target price displacement per the SAME capital denominator. A response beta is a notional coefficient; n_i/n_j=−beta*P_j,t/P_i,t under this fixed-origin share construction, not generally −beta.

Expanding factor coordinates into instruments can change gross capital even with identical net factor return. Compute L on actual unique instrument legs, not a synthetic model-factor notional sum. Costs, target and pooled payoff labels must all use that denominator.

An execution contract must distinguish K_ref from actual entry gross K_fill=sum_l abs(n_l)*F_entry,l. If actual-fill normalization is chosen, convert all reference-normalized target, capture and cost terms by K_ref/K_fill. No changing only the cost denominator. Collateral/equity committed capital is a separate resource measure, not an unannounced replacement for initial gross notional.

Lot/tick constraints may prevent exact n. Proposed response: select a feasible common basket scale only if exact ratios are preserved, or report unavailable. Independent rounding is a tracking change requiring explicit approval. No tolerance, minimum size, rebalance, derivative multiplier or margin treatment is invented; derivatives would need their own units/exposure/cash-flow mapping and cannot be inserted into the cash-share formula by ticker substitution.

## 4. Pre-entry timing and admission snapshot

Define t=signal close, u_dec=admission/commitment time, and actual fills thereafter. F_entry contains only information genuinely available by u_dec. Quotes/auction information, costs, borrow availability and collateral checks need binding timestamps and validity conditions. Reading an actual opening fill to decide an order submitted before that open is forbidden.

Recommend an observable pre-order all-leg snapshot and predeclared executable price limits, with revalidation immediately before commitment. This is a design proposal, not selection of a particular order type, feed, validity interval or limit offset.

Check the approved statistical gate, overnight persistence, E1 and feasibility using the SAME proposed size/mapping. Unknown capture/cost evidence already implies ECONOMIC GATE UNAVAILABLE. A stale snapshot requires revalidation or no entry; a fill after the target has vanished cannot be treated as the original valid hypothetical entry by resetting the target.

Policy must specify when the basket becomes an admitted episode, how delayed entry affects the remaining target and what information may trigger cancellation. No numerical deadline is chosen here.

## 5. Short obligations, availability and fees

For each negative n_l, require qualified, instrument- and time-specific evidence that the required quantity may be borrowed and sold under applicable account/contract rules. Model-level direction is not enough. Positive legs require deliverable cash/instrument capacity; all legs need legal/operational qualification.

Separate:
- Locate or indicative availability from an enforceable reservation/borrow commitment.
- Borrowed quantity, contractual fee base/day count, rate-reset terms and fee minima.
- Recall rights, notice deadlines, mandatory return/buy-in rules and settlement obligations.
- Restriction of proceeds, collateral requirements, manufactured entitlements and other short-related charges.

Recommend reserved/confirmed capacity for every short leg before entry rather than presumed availability. Whether a reservation suffices is contract-dependent and unverified. A high fee cannot substitute for absent availability. Failure on one required leg blocks the whole new basket; no drop-leg, unhedged or direction-flip substitute.

Fees accrue on the actual outstanding obligations until contractually discharged, not merely until a modeled exit trigger. Return/settlement delays can extend borrowing beyond a sale/buy execution; that distinction belongs in the joint duration/exposure law. Do not assume constant rates or free short proceeds.

## 6. Recall, margin and funding

Recommend any qualified recall or binding risk/contract constraint that interrupts ordinary policy liquidation invoke X and initiate coordinated basket closure under a frozen priority procedure. A recall of one leg is not permission to replace it with a new instrument or continue an altered hedge indefinitely. If immediate legal return and simultaneous basket closure conflict, the contract's mandatory obligation controls actual action; preserve the residual exposure and X history rather than claim a joint fill.

Before entry demonstrate cash for purchases, fees and required reserves; borrow collateral/margin; settlement timing; restricted proceeds; currency treatment if applicable; and funding sources under the qualified account contract. Freeze collateral valuation/haircuts, rate changes and cash-flow ordering before any future estimation. None is supplied now.

Collateral principal is not an expense; its funding cost and contractual charges are. No cross-basket netting credit, reinvestment of restricted short proceeds, perpetual refinancing or automatic margin top-up is assumed.

Margin calls, funding withdrawal or exhausted qualified capacity invoke the contract's X/closure process. A numerical gross-exposure cap alone does not prove solvency or collateral feasibility. Margin buffers, stress limits and risk reserves are unresolved design fields, not optimized here.

## 7. Coordinated entry and partial fills

Atomic simultaneous execution must not be presumed for independent instruments. Compare:

| Entry design | Benefit | Limitation |
|---|---|---|
| Verified atomic multi-leg facility | No unmatched basket fill if contractual guarantee holds | Availability/applicability unverified; cannot be assumed for these instruments |
| Coordinated orders with explicit completion/abort contract | Represents practical non-atomic fills honestly | Creates temporary exposures and possible unwind losses; needs timestamp, quantity, limit and contingency rules |

Recommend atomic entry where actually qualified; otherwise only a separately approved coordinated transaction with predeclared completion deadline, permitted legging exposure and price limits. These numerical fields remain UNSELECTED. If the necessary guarantees/contingency controls cannot be defined, execution is unavailable.

For partial entry propose:
1. Preserve every actual fill, signed obligation, reserved borrow, cash flow and outstanding order.
2. Complete only the original approved share vector within the frozen limits; no chasing indefinitely, increasing risk or reoptimizing ratios.
3. If completion fails, cancel remaining orders, confirm cancellation and unwind filled obligations as qualification permits; record X and real residual exposure until fully closed.
4. No “never entered” deletion of fees/losses, no fictitious simultaneous full basket, and no assumption a suspended leg can be flattened immediately.

This exposes a capture-model population dependency: approved formulas describe a fixed-origin entered basket, whereas entry aborts can occur before that basket exists. Before development the researcher must explicitly bind the event unit and denominator for attempted entries and X. Proposed extension is an attempted-commitment event with fixed planned capital and actual partial-fill exposure/cash-flow paths; an alternative is a separately accounted entry-failure branch whose expected costs enter admission. Neither population/accounting choice is frozen here. Failed attempts cannot simply disappear from the economic expectation or use a newly shrunken denominator after losses.

No partial-fill implementation or hypothetical execution simulation is authorized.

## 8. Joint liquidation, suspension and calendar mismatch

Preserve the origin target; do not reestimate the hedge or reset the gap after admission. Proposed normal trigger is the earliest qualified target close or the eventually frozen holding cap. F/P/N/A classification uses the approved prospective monitored-progress boundaries; actual liquidation occurs under this joint execution contract afterward.

A target touch is an exit instruction, not a guaranteed fill. Recommend coordinated full-basket liquidation at the first policy-qualified joint opportunity, subject to binding recall/margin obligations. Track actual leg-specific fill and borrow-discharge times, keeping exposure/costs open until all obligations are discharged.

An ordinary planned next opportunity is not automatically X. Missed ordinary execution due to a qualified exception, forced exit, or delay beyond the contract's definition invokes X priority. The exact ordinary/exceptional boundary, cap value and monitoring tolerance eta remain unresolved.

Suspension or non-overlapping trading calendars:
- No new entry without a qualified common entry opportunity and a defensible joint-exit policy.
- During a holding, absence of a tradable mark/fill does not imply a stale price is executable, a zero return, a paused financing clock or automatic risk cancellation.
- Freeze how qualified basket monitoring sessions are counted. Calendar-time borrow/funding continues according to contract even when a basket-session clock cannot advance.
- If a leg cannot close, retain its liability/exposure and follow the approved emergency procedure; no invented terminal fill or silent completion at a fold boundary.

Unknown future exit time can leave a path right-censored. Preserve censoring and the unresolved obligation; do not convert it into an observed N/A or completed X payoff. Duration-tail and support treatment must return to the bounded development contract before estimation.

## 9. Corporate actions on both sides

Require qualified effective/record/payment/publication times, instrument identity continuity, entitlements and account/loan terms for every long and short leg. No new C04 repair or acquisition is performed.

Maintain a holdings/cash ledger that reconciles splits/consolidations, distributions, rights, mergers, conversions, delistings and loan-specific manufactured obligations where applicable. Split share changes and price transformations must preserve economic exposure and the original target coordinate; raw price jumps are not convergence.

Long receivables and short manufactured payments enter the approved signed cash-flow allocation exactly once. Related fee/tax costs have unique ledger owners. Recall or instrument conversion triggered by an action follows the contract's X rules, not an ad hoc replacement security. Elective actions need predeclared instructions; no discretionary economic choice is made by the agent.

Unqualified action accounting makes valuation/payoff unavailable. An open position still has real obligations: inability to calculate a valid research return does not close it or erase previously observed data. Freeze/mask lineage remains immutable; unknown no-action status is not “clean”.

## 10. Failure and unavailable states

| Condition | Required proposed disposition |
|---|---|
| Factor/model mapping unresolved or unsupported | HEDGE MAPPING UNRESOLVED / S3 SIGNAL UNAVAILABLE for executable alignment; retain descriptive residual separately |
| Required cost/capture evidence absent | ECONOMIC GATE UNAVAILABLE; no zero-cost/certain-capture assumption |
| Borrow, cash, collateral, common session or instrument qualification absent before entry | EXECUTION UNAVAILABLE; retain qualified scientific signal, no order |
| Price/borrow snapshot invalid before commitment | Revalidate under frozen policy or no entry; no retrospective repair |
| Entry partial/abort, recall, forced exit, exceptional delay | X path with actual fills/exposure; event-unit and denominator binding required before model estimation |
| Corporate-action/accounting or valuation unknown | Accounting/payoff unavailable with persistent obligations; no fabricated return |
| Open/unresolved path at data boundary | Censored/unavailable, no terminal sale or lookup outside authorization |
| Residual leg remains after attempted closure | Episode/obligation not closed; financing and risk remain per contract |

X is an economic outcome on a qualified observed path, not a garbage class for missing evidence. No failure automatically activates P3, a tracking proxy, alternative alpha or unhedged fallback.

## 11. Evidence contracts and pre-estimation prerequisites

No feasibility verdict can be established from design algebra alone. The eventual contract must bind:
- Instrument identities and exact response/path replication, including fixed-origin versus rebalanced factor construction.
- Lot/tick and account eligibility, short reservations/loan terms, fee/rate/day-count evidence.
- Cash, margin/collateral, settlement and recall/buy-in rules.
- Entry mark/order/fill chronology, limits, completion/abort procedure, joint exit and emergency priority.
- Price/corporate-action/entitlement conventions, signed cash-flow ownership, censored-path treatment.
- Attempt/episode universe, gross-capital normalization and pooling/count units for approved P1.

These are requested future evidence types, not claims about current exchange law, broker offerings or instrument availability. The record does not acquire or inspect them. Missing authority/evidence blocks the relevant gate.

The previously proposed 2015–2019 development plan remains inactive. Only after the execution contract, unresolved scenario boundaries, pooling/sparse-state support, reference quantile specification and a bounded access action are frozen may any numerical estimation be considered. No flexible event-level conditional capture model is added to overcome these gaps.

## 12. Preferred contract proposal and decision table

Preferred first-version proposal: exact residual-to-instrument alignment; fixed-origin signed shares and consistent gross normalization; confirmed short capacity and funded collateral; verified atomic execution where available or explicitly bounded coordinated completion/abort; joint normal exit with X-priority contractual emergency handling; full long/short entitlement accounting; unavailable whenever qualification fails. This is not a claim that an eligible implementation exists.

Tracking-aware factor proxies are a separately amendable alternative, not an approved fallback. No instruments, deadlines, tolerances, margin values or order types are selected.

| Decision | Recommended proposal | Researcher/evidence binding still required |
|---|---|---|
| R0/R3 hedge | Exact OLS/conditional-pair (1,−beta) origin coordinate | Identity/accounting, feasible share quantities and actual borrow |
| R1 hedge | Full market/industry expansion and exact instrument response identity | Instruments, factor constituents, path replication and no hidden tracking term |
| Tracking | Exact first; fail unavailable if unproved | Any acceptable tracking exposure needs explicit amended object/protocol |
| Shares/capital | Fixed-origin shares; actual instrument gross; one denominator | Mark/fill convention, lots/rounding, capital conversion and sizing |
| Borrow | Confirmed all-leg capacity with contractual fee/recall terms | Reservation meaning, applicable account rules, liability/settlement details |
| Collateral/funding | Qualified cash/margin ledger with restricted proceeds | Haircuts, reserves, stress/funding and mandatory liquidation priorities |
| Entry | Qualified atomic facility or bounded coordinated transaction | Timing, limits, completion deadline and permitted transient exposure |
| Partial fills | Complete original vector within bounds or cancel/unwind, preserving X | Attempt-level event unit/capital versus separate failure branch |
| Exit/calendars | Joint ordinary liquidation; explicit forced/delayed X | Cap/clock, exception boundary, recall conflict and suspension procedures |
| Corporate actions | Entitlement-consistent long/short ledger and target transformation | Qualified action/loan data and election policy, without C04 repair |
| Failure | Distinct alignment/economic/execution/accounting unavailability | No silent proxy, zero, drop-leg, terminal fill or fallback |

Approved capture/cost architecture is preserved; this table's execution choices remain proposals. No probabilities, payoffs, duration, costs or numerical z0 were estimated. No data acquisition, implementation, backtest or PnL inspection occurred. NEXT_ACTION remains NONE.

**S3 HEDGE + BORROW + JOINT EXECUTION DESIGN / RESEARCHER DECISION REQUIRED**
