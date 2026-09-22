# S3 capture/cost scenario model — design checkpoint

2026-09-22 — DESIGN PROPOSALS ONLY / RESEARCHER DECISION REQUIRED.

The [researcher selected transparent joint scenario decomposition](../../decisions/S3_CAPTURE_COST_SCENARIO_DIRECTION_SELECTION.md) as the preferred design direction. Every detailed choice below is a proposal. No numerical parameters are selected or estimated. Direct conditional gross-payoff forecasting remains a documented alternative in the [parent checkpoint](S3_CAPTURE_COST_DESIGN_CHECKPOINT.md), not the primary design or an automatic rescue.

## 1. Economic object and verified target mapping

Use the parent fixed-origin geometry, with s=sign(d_u), fixed original w_(k,t), and positive initial gross capital K_u:

d_u=d_t−Delta B_ON;
Delta B_ON=sum_k w_(k,t)*(O_(k,u)/P_(k,t)−1);
L_u=sum_k abs(w_(k,t))*O_(k,u)/P_(k,t);
n_(k,u)=s*K_u*w_(k,t)/(P_(k,t)*L_u).

Then sum_k abs(n_(k,u))*O_(k,u)=K_u, and for a later qualified price observation q:

sum_k n_(k,u)*(P_(k,q)−O_(k,u))/K_u
= s*sum_k w_(k,t)*(P_(k,q)−O_(k,u))/P_(k,t)/L_u
= s*Delta B_u(q)/L_u.

At exact full price-displacement capture, s*Delta B_u(q)=abs(d_u), so:

G_u^target = g_u = abs(d_u)/L_u.

This verifies the target-displacement mapping; it does not establish expected capture. It is the full proposed target component, not a hard maximum on realized gross payoff: overshoot, delayed exits, losses, entitlements and fill deviations may produce values above or below it. No truncation to [0,g_u] is justified by this identity. A target touch at a close is not an executed liquidation.

The identity assumes qualified consistent prices/holdings; corporate actions require entitlement-consistent transformations and signed cash-flow accounting. The intercept is not a traded leg. The original-gap condition d_t*d_u>0 remains; an exhausted gap cannot be reset.

### Pre-entry timing and price convention

F_u^entry must mean the information available before the admission commitment, even though the displayed equations describe the eventual executable entry. A future fill cannot be used to justify an earlier order. The later execution contract must freeze the observation/order/fill timing, and quantify entry-price uncertainty.

Recommended accounting proposal below: use O and subsequent P as a declared reference-price path for the candidate executable basket, with execution deviations charged explicitly. If O instead denotes an actual fill, that entry deviation is already embedded and cannot also be added as a spread/slippage cost. The choice of reference mark and capital/size timing remains unresolved; do not switch conventions between capture and cost. For the same predetermined shares, distinguish K_ref=sum_k abs(n_k)*O^0_k from K_fill=sum_k abs(n_k)*F_entry,k. If the protocol normalizes by actual initial gross fill capital, convert every reference-normalized target, gross payoff and cost by the same K_ref/K_fill factor; do not keep the idealized target denominator while changing only costs. Actual fills cannot retroactively determine an order's submitted size.

## 2. Minimal prospective outcome-state space

Propose five terminal states R in {H,P,N,A,X}. Freeze the classifier before any outcomes are accessed; observing an outcome assigns it to the frozen classifier, not to a retrospectively invented state.

Let theta_H be the first qualified monitored target close, theta_cap the close at the predeclared holding cap, theta=min(theta_H,theta_cap) for ordinary liquidation, and tau the actual executable liquidation time under the same later-frozen policy. The cap and executable-clock semantics are not selected here.

Let b(q)=s*Delta B_u(q)/abs(d_u) describe reference-price progress from entry toward the original target. Introduce a proposed non-resolution tolerance eta with 0<=eta<1, to be researcher-bound before access. No value is selected, no precision floor is smuggled into the signal scale, and eta never changes the approved z-gate. It gives “approximately unchanged” an explicit meaning; exact equality alone would be a brittle economic category.

Define X first: a forced/constraint-driven exit or a failure of the policy's prescribed ordinary liquidation opportunity before completion. Ordinary planned next-event execution is not itself an exceptional delay. The execution contract must define that opportunity and resolve simultaneous-event precedence; this proposal assigns X priority whenever its criterion occurs, including after a target trigger but before liquidation.

For paths not in X:

| State | Proposed prospective classifier | Economic meaning |
|---|---|---|
| H — target trigger | theta_H<=theta_cap, including a tie | Target reached at a qualified monitored close, followed by ordinary policy liquidation |
| P — partial | No target hit by cap and eta<b(theta_cap)<1 | Positive progress without target convergence |
| N — non-resolution | No target hit by cap and abs(b(theta_cap))<=eta | Basket approximately unchanged at cap |
| A — adverse | No target hit by cap and b(theta_cap)<−eta | Movement away from the original target |
| X — constrained/exceptional exit | Priority criterion above | Forced liquidation or execution delay outside the ordinary policy; payoff may have either sign |

This partition is mutually exclusive and exhaustive for fully observed, qualified paths under the declared policy: a qualified cap close with b>=1 is a target hit and belongs to H unless X applies. An absent/unqualified monitoring path is not automatically “no hit”, N, A or X. Missing or right-censored economic observations remain unclassified until resolved under an approved observation/censoring contract. Do not renormalize probabilities over observed successes or impute unknown outcomes as zero.

No state proliferation for every constraint cause: keep X as one economic state, recording non-selecting reason tags. If X cannot support a defensible payoff/duration description, report the economic gate unavailable rather than dropping it.

For every r:

pi_(r,u)=P(R=r | F_u^entry, candidate basket and policy);
sum_r pi_(r,u)=1.

Let the random gross reference-basket payoff be:

G_u=[sum_k n_(k,u)*(P^0_(k,tau)−O^0_(k,u)) + D_u]/K_u,

where D_u is signed qualified security cash flow, including manufactured distributions owed on short legs. G_(r,u) denotes this random payoff conditional on R=r; its forecast is Ghat_(r,u)=estimated E[G_u | R=r,F_u^entry]. State names concern monitored progress, not a guarantee about the sign or amount received at tau.

## 3. Prospective payoff magnitudes

The decomposition cannot assign “H=g_u, P=a positive constant, N=0, A=a fixed loss” by assertion. Separate monitored progress, movement until actual liquidation and entitlements:

B_r=b(theta_r);
J_r=s*(Delta B_u(tau)−Delta B_u(theta_r))/abs(d_u);
Dbar_r=D_u/K_u;
G_(r,u)=g_u*(B_r+J_r)+Dbar_r.

For ordinary states theta_r is their trigger/cap close. For X, use the last qualified decision/constraint reference defined by the policy; missing such a reference makes the decomposition unavailable. The total gross-payoff identity above remains the target; this decomposition must reconcile to it.

- H: B_H>=1, with overshoot possible; J_H may be negative or positive before the executable exit. Full target component g_u does not replace the whole payoff.
- P: eta<B_P<1 at the cap; J_P and entitlements still matter.
- N: abs(B_N)<=eta, not necessarily zero; do not zero out subsequent exit movement.
- A: B_A<−eta, with no imposed finite lower bound from the residual target alone; exit movement can aggravate or reverse the loss.
- X: no fixed sign or fraction restriction. Conditional payoff and duration reflect its constraint path.

These are prospective mathematical definitions. Forecast magnitudes must be determined solely from entry-available information and, if separately authorized, chronologically prior qualified training outcomes. No current event's eventual path enters its own forecast.

| Magnitude architecture | Benefit | Limitation |
|---|---|---|
| Fixed fractions of g_u | Few interpretable parameters | Fractions need justification; imposing [0,1] or a capped loss discards overshoot/tails; a success-only formula omits losses |
| Residual-scale-based magnitudes | Could describe movement in standardized units | One-session sigma_t is not holding-period volatility; sqrt(T) scaling or a new horizon scale requires additional assumptions/approval |
| Prior development conditional means of normalized components | Estimates state-specific progress, exit movement and cash-flow contribution under the exact policy | Needs qualified outcomes, full state support and tail/censoring treatment; small g_u can create unstable ratios |
| Conservative bounded payoff set | Transparent robust alternative without pretending a bound is a mean | Bounds must be independently defensible and joint; finite adverse-loss bounds cannot be invented for short legs |

Primary proposal: prior conditional means of the normalized price-capture components (B+J), with separately accounted signed entitlements, using the same scenario model across candidates. In an unconditional P1 stratum this posits transferability of the conditional normalized-payoff distribution; disclose it as a model assumption, not an identity. Size-dependent effects and conditional dependence not captured by that stratum remain limitations.

At entry, Ghat_(r,u)=g_u*kappahat_(r,u)+Dhatbar_(r,u). Kappahat may exceed one or be negative; no clipping or arbitrary fraction is selected. No epsilon floor for small g_u is introduced: diagnose ratio concentration and declare unsupported application unavailable. No new bins, winsorization, sign/model-specific rescue, or selected magnitude values.

## 4. Expected capturable gross payoff

By total expectation under the same scenario partition:

mhat_u=sum_r pihat_(r,u)*Ghat_(r,u).

g_u is remaining target distance per initial gross capital. mhat_u is the forecast expected executable gross economic payoff, allowing failed convergence, adverse paths, delayed liquidation and entitlements. Neither the 5% rarity nor a hit probability alone determines it.

A shorthand mhat=rhohat*g_u is only equivalent if rhohat includes the entire signed conditional payoff distribution (and consistently allocated cash flows). Rhohat is not automatically a probability, positive, or bounded by one.

## 5. Duration: one joint scenario/path law

T_u is the random elapsed executable holding duration from entry to complete liquidation, including policy delays/constraints. A basket-session holding cap and calendar-time borrow accrual are distinct clocks. For leg k retain T_(k,u) or its outstanding-notional path if legs can close at different times; basket completion occurs only after the last required obligation is closed.

Recommend the scenario-conditional joint law of payoff, duration, exposure path and liquidation conditions. Report That_(r,u)=estimated E[T_u | R=r,F_u^entry] as a summary, not as a sufficient input for all costs.

The mixture is P(T in A | F_entry)=sum_r pi_r*P(T in A | R=r,F_entry). Borrow, funding, expected exit friction and recall/delay treatment must use this same law. A separate independently fitted duration law would risk incompatible success probabilities and holding times.

For example expected integrated borrow depends on E[integral_0^T rate_k(v)*borrow_base_k(v) dv], not generally E[rate]*E[base]*E[T]. Daily tariff calendars, cash settlement, nonlinear impact, rate changes and correlated liquidity require path integration or a separately justified approximation. No duration distribution, cap value, rate law, discretization or tail cutoff is selected here.

## 6. Exact non-overlapping cost ledger

Under the proposed reference-price convention, define signed trade Delta n_(k,l), execution reference M_(k,l) and fill F_(k,l). The signed execution deviation is Delta n_(k,l)*(F_(k,l)−M_(k,l)): positive adverse execution for buys above or sells below the benchmark; improvement may be negative.

Cost per K_u is:

chat_RT,u=centry,u + E[cexit,u] + E[cborrow,u] + E[cfunding,u] + E[cother,u],

all conditional on F_u^entry and the same candidate basket/policy. Before entry fills exist, centry,u is an ex-ante estimate, not a known realized charge. Random or nonlinear terms remain inside the expectation. The scenario mixture provides the conditional expectations of each future component.

| Ledger bucket | Included exactly once | Excluded / double-count control |
|---|---|---|
| Entry | Entry signed execution deviations and entry commissions/exchange/clearing/taxes or other mandatory transaction charges | Do not add spread/slippage/impact again if jointly represented in the fill model |
| Exit | Same definitions for every liquidation leg, including forced liquidation transaction charges and executed unwinds | Adverse benchmark price movement is gross payoff movement, not another fee |
| Borrow | Locate/reservation charges if payable; stock-loan fees and explicitly contracted borrow-related charges, net of only evidenced applicable credits | Borrow availability itself is a feasibility condition, not a numerical fee; manufactured distributions allocated to D, not here |
| Funding/collateral | Financing cash flows for debit balances, collateral/margin funding and qualified rebates under the declared contract and day count | Posted collateral principal is not an expense; restricted short proceeds are not free financing; no duplicated loan fees |
| Other | Only a pre-enumerated residual list of contractual charges not in the four buckets | No generic unexplained plug; each charge must have one owner or be marked not applicable with evidence |

Component audit:

- Explicit commissions/fees/taxes and side-specific short-sale transaction charges belong to entry/exit. Loan-specific short charges belong to borrow. Assign each by contract, never both.
- Bid-ask spread, residual slippage and market impact may be reported as a diagnostic decomposition of the single signed execution deviation. If modeled separately, freeze distinct benchmarks: spread versus a simultaneous midpoint; incremental size impact relative to the relevant executable quote; remaining modeled deviation with an explicit non-overlap rule. Aggregate fill-deviation modeling is the preferred simple accounting, with no extra half-spread.
- Delayed execution moves the reference basket and can add funding/borrow time; those are different consequences, not permission to duplicate price movement as slippage under an inconsistent benchmark.
- Cash dividends, manufactured payments and corporate-action entitlements enter signed D in gross payoff under this proposal. Their tax/processing charges must have an explicit ledger assignment. No double counting as borrow expense.
- Multi-leg legging, partial fills and forced unwinds require the same executed holdings and timing in both G and C. Fees/deviations for every actual order are included. A path that never establishes the intended basket needs a later partial-fill/unwind contract; do not silently evaluate it as a full S3 basket. Until defined, such cases prevent an evaluable gate.
- Unknown required costs are not zero; a zero/not-applicable item needs affirmative contractual/accounting support.

The reconciliation target is gross reference-basket payoff minus all signed execution deviations and contractual costs equals net economic cash gain per the same initial capital. This is an accounting identity for a future specification, not a computed portfolio result.

## 7. Basket/size/policy consistency

Before any gate evaluation require identical:

basket mapping/version and signed share vector; reference/actual price convention; initial capital denominator; size assumption; origin target and corporate-action treatment; entry-information cutoff; monitored holding clock and liquidation policy; scenario classifier; conditional duration/exposure law; cash-flow ledger.

Formally, basket_m=basket_c, n_m=n_c, K_m=K_c, policy_m=policy_c, F_m=F_c and law_(R,T,exposure)_m=law_(R,T,exposure)_c. Any price-convention conversion must preserve the net reconciliation.

All legs receive the same realism standard. A realistic held-leg cost with a frictionless hedge, single-leg cost for a multi-leg forecast, or full target capture paired with an inconsistent horizon is invalid. A resized proposed order requires reevaluation because impact and funding may be nonlinear. No sizing or hedge/borrow implementation is selected in this document.

## 8. Economic admission: bounded comparison

| Rule | Meaning | Trade-off |
|---|---|---|
| E1: mhat>chat_RT | Strict positive estimated expected net value | Minimal extra parameterization; susceptible to estimation error |
| E2: mhat−chat_RT>=delta | An additive gross-capital return margin | Delta needs independent economic justification and units; zero/equality is not exactly E1 |
| E3: mhat>=lambda_c*chat_RT | Cost-proportional margin | Requires a meaningful positive cost base; may behave poorly with rebates/near-zero cost; lambda_c is another research choice |

Recommend E1 for the primary first-version specification, conditional on qualified components and explicit uncertainty/support reporting. It is a proposal, not an approval or claim of robustness to estimation error. Do not append a hidden positive haircut, confidence level or multiplier. If a defensible economic margin is required, researcher approval must bind its purpose/value before development; no performance-based delta/lambda_c selection.

## 9. Scenario probability architecture

| Choice | Interpretability / sample efficiency | Model risk / adaptability / freedom | Six-estimator compatibility |
|---|---|---|---|
| P1 frequency model | Weighted frequencies of chronologically prior comparable qualified S3 events; transparent, few fitted quantities | Weak adaptation and comparability assumptions; sparse rare states remain problematic; few model choices if event universe/strata/weights frozen | One common procedure with declared sign/estimator treatment; never six independently tuned classifiers |
| P2 low-dimensional conditional model | A single multinomial probability model on a preregistered small vector, e.g. abs(z), g_u and approved regime variables | More adaptive but more parameters, functional-form risk and regularization choices; no automatic feature discovery | Same features/form and fitting rule across candidates; new model interactions/bins require approval |
| P3 fixed conservative bounds | A jointly coherent probability/payoff/duration uncertainty set, avoiding spurious fitted precision | Validity of bounds is the main risk; may be too conservative or unbounded; probabilities and adverse loss cannot be wished into existence | Common structural rule; differing basket liabilities must remain explicit |

Primary recommendation: P1 under a frozen common event definition and no fitted conditional-feature search. Probabilities are nonnegative weighted counts normalized over the full defined state space, including X. Report each estimator and sign separately; do not interpret equal weights as equal event risks.

At most one fallback: P3, only if separately chosen before empirical access, with independently defensible joint bounds. It is not an automatic reaction to poor P1 results. If no credible bound exists (particularly adverse shorts or exit duration), the economic gate remains unavailable. P2 is retained as a documented alternative, not a scored primary/fallback configuration.

For P3 use a coherent joint set A_u. A lower bound inf_(P in A_u) E_P[G−C] can provide a robust admission interpretation if the researcher chooses it; do not relabel that bound as an estimated expected value. Separately minimizing G and maximizing C may be conservative but must not imply mutually impossible scenarios. No uncertainty set, bound or robust-admission rule is adopted now.

## 10. Four separate gates

1. Statistical/material abnormality: abs(z_t)>=Q^w_0.95(abs(z_ref)), with alpha=0.05 and approved scale/support/weights; numerical z0 remains uncomputed.
2. Overnight persistence: d_t*d_u>0; the original opportunity has not vanished or reversed before entry.
3. Economic value: the approved future capture/cost rule on the same basket, size and policy; no currently computable value.
4. Execution: qualified hedge mapping, borrow, collateral and joint-leg implementation feasibility.

The capture model may use approved signal variables in a later frozen specification, but it must not redefine abnormality or retune alpha. A scientific signal with unavailable economics or execution remains recorded as such, not erased or turned into zero abnormality.

## 11. Proposed bounded development protocol — NOT AUTHORIZED

Only the already-proposed 2015–2019 development region is considered. Reuse, as a proposal only, the prior 2015–2016 formation interval and six forward assessment blocks: 2017H1, 2017H2, 2018H1, 2018H2, 2019H1, 2019H2. No 2020+ lookup to complete an exit or label; no claim that exposed data become an untouched holdout. No numerical z0 calculation is part of this task.

Before any data action the researcher must freeze eta, holding/exit policy, qualified event population, reference quantile formation/schedule, cost/price accounting, candidate comparability/pooling and all support criteria below. These unresolved numerical/specification fields are explicit blockers, not defaults.

### Event set, information cutoff and estimation

Use the complete preregistered scientific opportunity set satisfying statistical and overnight gates, with declared economic/execution qualification. Do not select training examples on the economic gate's own predictions. If only executable opportunities form the forecast population, retain unavailable opportunities in a separate coverage ledger and state the conditioning explicitly. Overlapping pair/time episodes are not independent replications; freeze episode construction before labels.

At each assessment block start use only permitted earlier information and outcomes fully knowable at that cutoff. Freeze estimated scenario parameters for the block; current pre-entry costs/inputs can update only under the separately frozen PIT evidence rule. Do not use validation labels to revise them mid-block.

Future data authority must explicitly permit the necessary forward basket payoff components and durations: “no-PnL selection” does not make economic outcome access non-empirical. No realized portfolio PnL/Sharpe optimization or performance-based choice is proposed.

Estimate only the five-state probability vector (four independent probability degrees of freedom per approved stratum), state-conditional normalized payoff components and the joint empirical duration/exposure/exit-condition distribution; separately qualify contracted costs and any approved component estimators. No horizon, eta, model features, cost multiplier or threshold search.

### Pooling proposal

Use one P1 estimation architecture with separate signed orientations. Within a sign propose common estimator-group-balanced pooling of dimensionless state probabilities/normalized payoff components only under an explicitly approved exchangeability assumption. R0-C/R0-L share a group so duplicate equations do not double the evidence. Preserve all six estimator reports and native qualified support.

Reference-tail weights are already approved for that reference distribution; extending them to economic event pooling is a NEW PROPOSAL, not an inherited approval. Block/pair/estimator influence, missing groups and episode overlap must be explicitly bound for the economic population. Candidate-specific entry g_u, actual legs, entitlements and costs remain candidate-specific. No averaging raw currency costs across incompatible baskets.

If normalized distributions are not supportable as exchangeable, report the limitation and stop for amendment; do not automatically split into six fitted strategies. No per-model winner selection.

### Minimum support and censoring

Structural minimum: nonempty qualified common groups/strata and positive observed support for every state whose mean/duration must be estimated, or a separately approved justified bound. An unobserved X/adverse state is not proof of zero probability. No success-only renormalization.

Statistical minimum must be a preregistered precision/effective-support criterion with per-state, independent-pair/time-cluster and concentration requirements. Denote the still-unselected requirements N_min,r, N_eff,min and the allowed uncertainty/concentration bounds. Algebra cannot choose these numerical values; access stays blocked until the researcher binds them. Mere existence of a mean is insufficient.

Primary P1 proposes no fitted shrinkage/smoothing hyperparameter or pseudocount search. If sparse support prevents an estimate, report unavailable. A future smoothing prior would itself require an amendment, not silently turn missing states into supported means.

Purging/label maturity must follow actual policy liquidation and information availability, not a fixed cap expressed as calendar days. A complete observation contract must handle right censoring and invalid paths without conditioning the sample on quick/successful liquidation. No ad hoc complete-case selection. If censoring prevents identifying the proposed means/joint law, stop; do not manufacture a tail completion.

### Objective, diagnostics, budget and stopping

Use predeclared forward probability calibration (a multiclass proper score such as Brier as the proposed single probability diagnostic), payoff-component prediction error, duration prediction/calibration, coverage and concentration reporting. These assess a fixed procedure; they do not optimize profitability or choose a winner. No new numerical acceptance cutoff is supplied.

Robustness is diagnostic: separate signs, estimator groups, chronological blocks, X causes, censoring and cluster concentration; report component forecast errors and exposure to extreme ratios. No re-fitting after deleting inconvenient states. Existing H252 MAD/H126 SD remain non-selecting scale specifications; they are not a new factorial capture-model search. No new tail probabilities are introduced.

Budget proposal: ONE primary scenario/P1/payoff-duration specification, evaluated in six chronological blocks; all six estimators and both signs are reporting strata, not model-search candidates. P3 is at most ONE mutually exclusive pre-access alternative if explicitly selected, not an additional run after seeing results. No P2 fit, state-count search, payoff mapping grid, margin search or automatic second pass. Evidence-based cost components implement that same specification, not alternative profitable cost scenarios.

Stop after the one prescribed pass and report all diagnostic/unavailable states. Sparse support, non-identifiable censoring, missing mandatory costs, inconsistent accounting or failed comparability stops the affected gate; no search expansion, per-model rescue, threshold relaxation or later-year access.

## 12. Cost evidence hierarchy before acquisition

No source/provider, contract or dataset is selected or accessed here. The hierarchy specifies evidence types needed, not current market rules or prices.

| Component | Preferred authority / evidence | Role of bounds or development |
|---|---|---|
| Statutory exchange/regulatory fees and taxes | Applicable dated exchange/regulatory schedule with instrument, side, effective-time and legal applicability | A generic rate cannot replace missing applicable authority |
| Broker commissions and contractual short charges | Executable broker agreement/tariff and its minima, caps, rebates and settlement terms | Only verified applicable terms; no inferred zero |
| Borrow/locate fee and availability | Security/time-specific broker/lender terms, locate/availability evidence, fee basis, recall rights and rate changes | Availability is hard feasibility; defensible future-rate/duration bounds may supplement qualified contract evidence |
| Spread and execution deviation | PIT quotes/order-book or appropriate executable reference evidence at the declared decision time | A preregistered bound needs independent support; spread is not inferred from daily closes |
| Impact/size/legging | Qualified trade/order/execution evidence at relevant size and liquidity plus the future execution policy | A separately approved simple estimator or defensible conservative bound; no unsupported zero impact |
| Funding/collateral | Applicable broker/funding agreement, margin/settlement and short-proceeds treatment | Costs depend on the approved joint balance/duration paths; posted principal is not expensed |
| Exit friction and recall/delay | Same quote/contract hierarchy plus qualified chronologically prior exit-condition evidence | Joint scenario development may forecast duration/liquidity; no future realized values at entry |
| Entitlements/manufactured distributions | Qualified corporate-action/entitlement records and contract allocation | Included once in D; unresolved C04/accounting remains unavailable, not repaired in this task |
| Other contractual charges | Explicit applicable fee/contract evidence and unique ledger assignment | No residual cost plug; unjustified components remain missing |

Distinguish a missing quote from a known zero fee. A conservative bound is admissible only if separately preregistered with a defensible evidence basis; it is not a license to substitute an arbitrary constant. Missing required evidence produces ECONOMIC GATE UNAVAILABLE. This evidence design is not acquisition authorization.

## 13. Preferred complete proposal and at most one fallback

Preferred proposal: five-state X-priority partition with prospective eta/holding rules still to be bound; P1 common-procedure frequency probabilities with proposed sign separation and justified normalized pooling; state-conditional prior normalized payoff means and a joint duration/exposure law; one non-overlapping reference-price all-leg cost ledger; E1 strict positive estimated expected net value with support/uncertainty reporting. Stop unavailable when required support or cost evidence is absent. Every detail remains proposed.

Only fallback: P3 independently justified joint conservative bounds for the same basket, states, accounting and policy, with explicitly researcher-approved robust admission semantics. It must be selected before access and cannot rescue inconvenient P1 outcomes. No defensible bounds means unavailable.

## 14. Researcher decision table

| Decision | Preferred proposal | What still needs approval |
|---|---|---|
| Outcome-state space | H/P/N/A/X, X priority, qualified monitored closes distinct from executable payoff | eta, cap/clock, ordinary-delay versus X criterion, simultaneous-event and censoring rules |
| Expected gross capture | sum_r pihat_r*Ghat_r; g_u=abs(d_u)/L_u only the full target component | Exact reference/capital/cash-flow target and permissible estimation |
| Duration | Joint scenario-conditional payoff/duration/exposure law; conditional mean duration only a summary | Tail/censoring support, leg completion, day-count and integration conventions |
| Probability architecture | P1 fixed frequency procedure; P2 documented only; P3 sole possible pre-access fallback | Comparability, strata, support precision and choice of primary or bounded fallback |
| Payoff architecture | Prior conditional normalized capture/exit-movement means plus signed entitlements | Transferability, small-gap ratio support and exact component estimator |
| Costs | Full basket reference-price deviation plus uniquely assigned contractual costs | Benchmark, all evidence/contract mappings and nonlinear path/size treatment |
| Admission | E1 mhat>chat; E2/E3 compared only | Researcher selection; any justified margin would require a separate explicit binding |
| Pooling | Common procedure, separate signs, proposed balanced normalized pooling without duplicate C/L evidence | Economic-population weights/exchangeability; no automatic inheritance from reference-tail weights |
| Development | Proposed 2015–2016 formation, six 2017–2019 forward blocks; one primary specification | All prerequisite values/policies, minimum effective support, maturity rules and separate bounded access authority |

No detailed choice in this table is frozen by writing it. No data, numerical z0, probability, duration, payoff or cost was accessed/estimated. No implementation, hedge/borrow execution, C04 repair, backtest or PnL inspection occurred. NEXT_ACTION remains NONE.

**S3 CAPTURE + COST SCENARIO MODEL / RESEARCHER DECISION REQUIRED**
