# Trading strategy economic redesign checkpoint

Date: 2026-09-18. **DESIGN PROPOSALS ONLY / RESEARCHER SELECTION REQUIRED.**

Economic hypothesis → mathematical strategy → data requirements → development → validation.

All data correction, C04 repair, acquisition, backtesting, trading execution and PnL access remain paused. This document does not amend the frozen V1 release, adopt any proposed strategy, or implement anything. Its reference baseline is `V1_1_COMPLETE_TRADING_STRATEGY_MATHEMATICAL_SPECIFICATION.md`; that document, the six relationship estimators and immutable research artifacts remain intact. Existing code-conformance and input-qualification findings are not repaired here.

No empirical performance informs these recommendations. Prior repository execution/access history is not erased: absence of a valid complete trading return series is not equivalent to absence of prior data exposure. This redesign is a prospective new design record, not a retroactive preregistration of V1.

## 1. Economic hypothesis: the missing forward implication

Start from the intended relationship object

`mu_(j|i,t) = E[y_jt | F_t, relationship with i]`,

`a_(i→j,t)=y_jt−mu_(j|i,t); g_(i→j,t)=−a_(i→j,t)`.

For this notation to be meaningful, the conditioning information for mu excludes the dependent response y_jt itself: write it more precisely as `I_t={prior formation information, current observable source/factors}`. If F_t already contains y_jt, its conditional expectation given all F_t is y_jt; the implemented model is a restricted conditional projection, not that tautology. At signal formation the full close information, including the measured error, becomes observable.

Let u be the first executable open after signal t, tau a predeclared liquidation rule, R_j(u,tau) the actually capturable security return including qualified distributions, and C_j(u,tau) its all-in costs per initial long notional. A positive gap supports a **single-leg** trade only under the additional hypothesis

`E[R_j(u,tau)−C_j(u,tau) | information available at u, g_t>0, admission conditions] > 0`.

For a signed hedge basket with share vector n and initial gross capital K, the hypothesis is instead

`E[(sum_k n_k*(P_k,tau−O_ku) + qualified cash flows − financing − borrow − execution costs)/K | entry information, residual gap] > 0`.

Neither inequality follows from low contemporaneous relationship loss. An economic story that could make it true is temporary, delayed incorporation of shared information: a valid stable relation identifies an under-responsive leg, the discrepancy persists until execution, and subsequent price adjustment closes the discrepancy rather than a permanent change in the relation. For a long-only source-normalization trade the separate story is that a negative source departure is temporary and rebounds. Both stories require forward evidence; no mechanism is identified merely by naming the error.

| Concept | Exact distinction |
|---|---|
| Contemporaneous error | y_jt−mu_(j given i,t) describes the current observation relative to a conditional model. |
| Future expected return | A conditional expectation of executable future price/cash-flow change; it requires a forward mapping not supplied by the current regression. |
| Mean reversion | A dynamic tendency of a specified state toward a target, e.g. E[X_next−X_now given X_now]=−lambda*X_now with lambda>0; no lambda is estimated or adopted here. |
| Relative-value convergence | Movement of a defined tradable basket toward a declared relative target; the long security need not rise if the hedge falls faster. |
| Mechanism identification | Evidence distinguishing economic causes from alternatives; neither a profitable trade nor a reverting residual supplies this on its own. |

A stationary one-period return residual can have no serial predictability at all. Its next value can return to zero without cumulative future returns reversing today's error. Likewise a return regression does not establish cointegration of prices. The distinction between a stationary level combination and an error-correction dynamic is substantive, not terminology; see Granger's [Nobel lecture](https://www.nobelprize.org/uploads/2018/06/granger-lecture.pdf). No cointegration estimator or new relationship family is proposed for execution here.

### Notation used below

t: signal close; u: executable entry open; q: later observation; tau: liquidation; P_kt/O_ku: raw close/open with explicitly accounted corporate actions; y_kt: simple close response; K: allocated initial gross capital; w: signed notional coefficients; L=sum|w|; n: signed shares; s in {−1,+1}: chosen trade orientation; beta: directional response slope; b_k,d_k: market/industry factor loadings; f: vector of factor responses; Gamma: loadings of tradable hedge instruments on those factors; g/e: peer gap/source excess; sigma_t: strictly-prior scale; z0: unselected normalized threshold; c_hat: ex-ante all-in round-trip hurdle per gross capital; m_hat: pre-entry forecast of capturable gross basket return; h: predeclared holding cap, not calibrated here. All costs/targets are explicitly distinguished by their denominator. Empty/unknown required inputs mean unavailable, not zero.

## 2. A — what position tests the hypothesis?

### A1. Single-leg morphology trade

For the existing long-only peer channel, `g>0 → n_j=K/O_ju, n_i=0`. For source, `e<0 → n_i=K/O_iu, n_j=0`. Exit sells the purchased security. The negative theoretical orientations are not executed under existing V1.1.

If `R_j=b_j R_market+d_j R_industry+R_idiosyncratic`, then the long position earns all three components. Conditioning a signal on a factor-residualized relationship does **not** subtract factor exposure from the purchased security. Even a perfect signal attribution cannot make the position market-neutral.

### A2. Relationship-hedged pair trade

For `y_j=alpha+beta*y_i+epsilon`, the same-period response innovation is `y_j−beta*y_i−alpha`. A return-unit basket has coefficients `w_j=1, w_i=−beta`. At entry a precisely specified implementation is

`L=1+|beta|; n_j=s*K/(L*O_ju); n_i=−s*K*beta/(L*O_iu)`.

Ignoring distributions/costs, its fixed-share PnL over an open-to-price holding interval is exactly

`PnL/K = s*[R_j(u,q)−beta*R_i(u,q)]/(1+|beta|)`.

Thus beta is a **return-notional coefficient under this particular normalization**, not a shares ratio. The share hedge is `n_i/n_j=−beta*O_ju/O_iu`. For a regression in price levels or logs, this mapping would be different. Re-estimating beta daily and maintaining constant dollar weights would be a rebalanced strategy; it is not implied here.

An OLS slope minimizes in-sample one-period residual variance against i under its estimation geometry. That does not prove the same coefficient is a stable open-to-exit risk hedge, a structural equilibrium ratio, a minimum-cost hedge, a market-neutral hedge, or a source of future reversion. Alpha is not a tradable asset and cannot be shorted: basket return still contains any alpha drift. For beta<0 this construction is two legs of the same sign for s=+1, not the usual long/short pair. Dollar neutrality holds only in special cases (beta=1 in this normalization).

With market loadings b and industry loadings d, residual exposures per gross capital are `s*(b_j−beta*b_i)/L` and `s*(d_j−beta*d_i)/L`. They need not vanish. A separate neutralization mapping would be a new explicit hedge layer, not a reinterpretation of beta.

For R1, expanding the two-stage equation gives

`mu_j|i = alpha_u + beta*y_i + (a_j−beta*a_i) + (b_j−beta*b_i)*m + d_j*q_j−beta*d_i*q_i`.

Consequently **pair-only** hedging leaves the factor terms; a basket that matches the modeled residual must also hedge their tradable equivalents. With factor coefficient vector gamma (market and the appropriate industry terms), choose hedge notionals h satisfying

`Gamma' h = gamma`,

and positions proportional to `(1, −beta, −h')`. Gamma maps available hedge-instrument returns to the model factors. Exact replication, unique identification, stable exposures and executability must be demonstrated; otherwise there is tracking risk or a missing mapping. There is no authorized minimum-norm/optimized fallback. Industry baskets exclude the evaluated pair, as in the signal, if claimed to be exact replication. Market/industry indices themselves are not assumed purchasable assets.

A daily equal-weight industry-return series may require rebalancing to replicate across several days; a frozen constituent share basket generally will not reproduce it exactly. S3's fixed-origin position therefore needs an explicit static replication/target definition or disclosed tracking error. Adding ongoing factor-basket rebalancing would change turnover, costs and the position equations and requires an explicit design binding, not an unnoticed implementation step.

R3 supplies the pair-specific slope `beta_G,slope+b_p,slope` for this candidate mapping; statistical shrinkage is not an economic guarantee about the hedge. R0-D/C use their OLS bridges, not distance/correlation as hedge ratios.

### A3. Factor-hedged single security

Let gamma_j collect the held security's factor loadings and choose executable instrument notionals h with `Gamma' h=gamma_j`. Set

`L=1+sum_l|h_l|; n_j=s*K/(L*O_ju); n_Hl=−s*K*h_l/(L*O_Hl,u)`.

This isolates factor-relative security movement to the extent the hedge mapping holds. It tests idiosyncratic normalization more directly than A1, but does **not** hedge the conditioning security's residual. In R1, the conditional target includes `beta*u_i`; factor hedging j alone does not replicate the full pair residual. R0/R3 do not independently supply all the factor coefficients needed for this construction; a separately approved exposure-estimation layer would be necessary.

### Required construction comparison

| Aspect | A1 single leg | A2 relationship hedge | A3 factor hedge |
|---|---|---|---|
| Position | K/O in held security | K/L times (1,−beta), converted to shares; R1 residual replication additionally needs factor legs | K/L times (1,−h) with Gamma'h=gamma_j |
| Hypothesis / PnL source | Held security rises after entry | Signed residual basket earns after-entry correction | Held security outperforms/normalizes relative to its factors |
| Market exposure | Full held-security loading | Difference b_j−beta*b_i; zero only if demonstrated or additionally hedged | Ideally canceled; replication/tracking risk remains |
| Industry exposure | Full held-security loading | Difference of leg loadings, often material for cross-industry pairs | Ideally canceled for modeled industries |
| Pair-relative exposure | Signal-conditioned only; no traded pair difference | Explicit traded relative exposure | Not directly pair-hedged |
| Financing / shorts | Existing long-only cash-funded semantics | Borrow/collateral/recall for negative legs; long-long possible with negative beta | Short hedge instruments or other separately qualified hedge mechanics |
| Turnover | One entry/exit leg | At least two; drift means fixed shares do not maintain fixed notional hedge | Security plus factor instruments; proxy/basket turnover potentially large |
| Interpretability | Directional economic probe, not neutral arbitrage | Most direct pair-convergence test when hedge and target match | Cleaner idiosyncratic test, different from pair-residual convergence |
| R0/R1/R3 compatibility | All six signals usable | R0 bridges/R3 slopes usable as proposed mappings; R1 needs expanded factors for full residual match | R1 provides formation factor coefficients; R0/R3 need additional hedge-layer estimates |
| Data | Long execution, accounting and valuation | Both legs plus borrow/funding; factor instruments if expanded | Factor-instrument replication, exposures, borrow/funding and prices |
| Principal failure | Common-factor rally mistaken for anomaly capture | Predictive coefficient or one-period innovation mistaken for stable convergent tradable spread | Proxy basis / time-varying factor loadings mistaken for idiosyncratic alpha |

**Ex-ante recommendation:** for the stated statistical-arbitrage/convergence question, prefer A2 with a declared tradable-residual mapping; use factor expansion when the signal itself is factor-adjusted. A3 is appropriate only if the intended estimand is explicitly factor-relative single-security normalization. Do not silently fall back to A1 when a required short/hedge is unavailable. The recommendation is conditional on hedge feasibility and does not claim that convergence exists.

## 3. B — threshold architectures

Let d_t denote the signed hypothesized correction in the chosen object's units: peer g, source −e, or a corresponding mapped basket gap. Let `z_t=d_t/sigma_t`, with sigma positive finite and formed strictly before signal from the **same economically aligned object**. The scale estimator/window must be separately bound for the redesign. Reusing H126 MAD is a possible inheritance decision, not a license to call a security-response scale a hedge-residual scale. No current outcome enters the scale.

| Architecture | Gate and units | PIT construction / interpretation | Volatility and cost behavior | Numerical decisions |
|---|---|---|---|---|
| B1 none | abs(d_t)>0, response units | Exact nonzero modeled discrepancy | Arbitrarily small discrepancies admitted; no volatility or cost protection | No magnitude parameter; still requires nondegenerate data/scale gates where used |
| B2 normalized | abs(d_t)/sigma_t ≥ z0, dimensionless | Distance relative to prior aligned variability | Adjusts to scale, not monetary profitability; same z can imply different costs | z0 and scale history must be justified ex ante or calibrated in development, never final validation |
| B3 economic | m_hat_u > c_hat_RT,u, both per initial gross capital | Forward expected executable correction versus observable/modelled all-in costs | Handles costs directly; volatility enters only through forecast/risk model | Forecast mapping/horizon/cost model must be declared and development-qualified; no inference m_hat=gap by default |
| B4 combined | abs(z_t)≥z0 AND m_hat_u>c_hat_RT,u | Requires statistical materiality and economic capturability | Rejects both small standardized noise and uneconomic gross opportunities | Requires all B2/B3 bindings; no arbitrary universal z or cost buffer supplied here |

A cost estimate in currency is, schematically,

`Cost_hat = sum_k [c_in,k*|n_k|*O_ku + c_out,k*|n_k|*P_hat_exit,k] + spread/slippage/impact allowances + expected borrow/financing + mandatory charges`.

Divide by initial gross capital K for c_hat_RT. Terms must not be double-counted (e.g. spreads already embedded in execution prices). Exit prices/duration/borrow costs require a predeclared estimation or conservative bounding method, not future realized inputs. The old 5/10/20 bps assumptions alone do not establish executable short-basket costs.

If one explicitly posits `m_hat_u=rho_hat_u*|d_u|/L_u`, then B3 implies `|d_u|>L_u*c_hat_RT/rho_hat_u`, where rho_hat>0 is the expected captured correction fraction (including failure/delay possibilities in its forecasting definition), and L_u converts gap units into gross capital. Neither rho=1 nor positive rho is supplied by the relationship regression. B4's shorthand `|g|≥h_cost` is economically meaningful only after this conversion and entry adjustment; otherwise it is a cost-scaled heuristic, not expected profitability. Directional eligibility remains necessary; absolute-value thresholds do not authorize forbidden shorts.

**Recommendation:** B4 as a design architecture, with thresholds/forecast mapping unresolved until authorized ex-ante binding or development-only calibration. A positive safety margin, if desired, is another declared parameter—not invented now. No numerical z0, rho, cost multiplier or optimized horizon is selected.

## 4. C — resolution and executable convergence

All proposed exits distinguish a close-time trigger theta from an executable liquidation time `tau=first jointly qualified required-leg execution event after theta`. A target hit at close does not guarantee a fill at that price. Known unavailable execution keeps an obligation pending under a predeclared contract; unknown valuation cannot be silently carried as valid. Entry/exit feasibility, fold boundary, maximum holding/risk controls and financing must be bound before development for a selected redesign.

### C1. Existing signal-origin morphology

For peer `r(q)=g_t−sum_(s=t+1..q)y_js`; source `r(q)=e_t+sum_(s=t+1..q)y_is`. With original anchor b=g or e, held-security eligible count L(q), and entry-inclusive clock,

`theta_C1=inf{close q after entry: required variables qualified AND [b*r(q)≤0 OR L(q)≥10]}`.

This tests whether subsequent raw-response accumulation offsets an original morphology component. The sum includes overnight movement before entry, and is not compounded entry return. It does not establish that the position captured that convergence. Origin remains fixed. Data/complexity are lowest, but corporate-action and unknown-interval requirements remain binding.

### C2. Entry-based single-security target

This requires an **explicit proposed bridge** from a response gap to a price target; it is not an identity implied by mu. For a positive long correction d_t (peer g_t; source −e_t), consider

`P*_k=P_kt*(1+d_t)`.

Let `r_ON=O_ku/P_kt−1`. The economically remaining target return at entry is exactly

`d_u=(P*_k−O_ku)/O_ku=(d_t−r_ON)/(1+r_ON)`.

If r_ON≥d_t, the target has already been reached/passed; there is no positive long target left and this proposed convergence trade is not admitted. If costs absorb the remaining opportunity, B3/B4 also blocks it. Setting the target instead to O_ku*(1+d_t) would reset the anomaly and manufacture an extra gap; it is not this proposal.

For qualified observations after u,

`r_C2(q)=d_u−(P_kq/O_ku−1)=(P*_k−P_kq)/O_ku`,

`theta_C2=inf{close q≥u: r_C2(q)≤0 OR eligible holding count≥h}`.

The original target is fixed; only its remaining distance is measured from execution. Actual PnL is evaluated at subsequent exit fills and includes costs/distributions. Corporate actions require an entitlement-consistent transformation of target and holdings, not an unadjusted-price target across a split. h and the eligibility rule are pre-execution bindings; retaining ten held-security sessions is a proposed inheritance, not a performance choice.

### C3. Current-model fair-response exit

Let `a_new(q)=y_jq−mu_j|i,q` under current PIT model state and sigma_q its declared scale. A possible target-region stopping time is

`theta_C3=inf{close q≥u: |a_new(q)|/sigma_q≤z_exit OR holding count≥h}`.

z_exit is unselected. The origin is no longer fixed: model updates, source movement and scale changes can move the target even without profitable position movement. A fresh one-period error near zero is **not necessarily a fair-price level or cumulative correction**. This is a dynamic-control strategy requiring all contemporaneous pair/factor inputs, refresh rules, invalid-state exits and substantially more interpretation; not the recommendation for a first clean convergence test.

### C4. Fixed-origin, tradable relative-basket convergence

To avoid mixing close-return and entry-return denominators, define at signal t a basket vector w_t in close-notional units: R0/R3 `(1,−beta_t)`; expanded R1 `(1,−beta_t,−h_t')` if exact tradable factor mapping exists. Hold these origin share proportions fixed. Define

`B_t(q)=sum_k w_kt*(P_kq/P_kt)`;
`Delta B_ON=sum_k w_kt*(O_ku/P_kt−1)`;
`d_u=d_t−Delta B_ON`;
`L_u=sum_k |w_kt|*O_ku/P_kt`.

Here d_t is the **proposed** event-basket correction target (peer g for an exactly matched response residual); translating today's residual into a future level displacement is an economic hypothesis to validate, not a proven equilibrium. For trade orientation s=sign(d_u), proposed shares are

`n_k=s*K*w_kt/(P_kt*L_u)`.

Actual entry dollar weights are `s*w_kt*O_ku/(P_kt*L_u)`, not automatically `(1,−beta)/(1+|beta|)` after an overnight move. This explicitly chooses fixed-origin share geometry instead of silently switching hedge mappings. For peer continuation require original and remaining directions agree, `d_t*d_u>0`; target overshoot is not a new reverse signal.

Post-entry basket movement and residual are

`Delta B_u(q)=sum_k w_kt*(P_kq−O_ku)/P_kt`,
`r_C4(q)=d_u−Delta B_u(q)`,
`theta_C4=inf{jointly qualified close q≥u: s*r_C4(q)≤0 OR declared basket holding count≥h}`.

Before costs/distributions, `PnL(q)/K=s*Delta B_u(q)/L_u`, so a correctly executed target displacement has gross magnitude `|d_u|/L_u`. Borrow, funding, corporate actions, delayed/partial fills and drift remain real constraints. Intercept drift is not hedged; signal alpha is included in the initial target, and no additional alpha accrual is silently assumed. This event target is **not a claim that B_t is a stationary cointegrating spread**.

| Exit | Executable PnL link | Overnight sensitivity | Anchor / reversion interpretation | Data / complexity |
|---|---|---|---|---|
| C1 morphology | Indirect; can resolve on pre-entry movement | Counts overnight toward original sum | Fixed event response, not entry-price reversion | Existing security responses; low, but qualification strict |
| C2 entry-based | Direct to entry-to-target price change, before actual fill costs | Explicitly deducts overnight movement; skip exhausted target | Fixed proposed security price target | Qualified open/close/accounting; moderate |
| C3 updated model | No automatic mapping from current error to accumulated PnL | Target can move after entry | Moving conditional-response target, not fixed-anchor reversion | Current pair/factors/model refresh; high |
| C4 basket | Exact fixed-share basket price-change mapping | Deducts all legs' overnight displacement in common units | Fixed event-basket target; convergence hypothesis still unproven | Synchronized multi-leg execution/valuation, hedge, borrow; high |

**Recommendation:** C2 with A1, or C4 with A2; prefer C4 for a relative-value hypothesis. Retain C1 only as the explicitly named morphology probe. Do not mix single-security C1 exits with a new hedged position and call the result a test of basket convergence.

## 5. Three coherent architectures — no implementation or selection

Common accounting notation: executed order cost is a specified function of actual signed security trades; episode PnL is `sum_k n_k*(exit_fill_k−entry_fill_k) + qualified distributions − execution/borrow/funding costs`. Short sale proceeds are not assumed freely deployable cash; collateral and equity/gross exposure must be modeled explicitly. No package inherits long-only cash feasibility unchanged when it introduces short legs.

### S1 — existing morphology probe (A1/B1/C1)

`mu → g/e/UR0/MP0/MP1 → existing validity/EP-A/DECA-A and long-only gates → next-open admission → Option-A sizing → fixed single-security shares → C1 trigger → qualified exit → actual-price PnL`.

Core peer gate: valid pair/directional state, `NZ(mu), NZ(g), UR0>0`, no positive rejection/break/data-invalidity/conflict, no active same pair/channel, no opposite raw-eligible collision, and `g>0` for long executability. Source uses `NZ(e), NZ(MP0), qualified MP1>0`, no positive leakage or other blocking evidence, collision/episode constraints, and `e<0`. No extra magnitude threshold. Missing required data blocks; unavailable mechanism evidence is not fabricated as absent.

At an open, `A=surviving episodes`, `B=qualified proposals before funding`, `x_raw=V_pre/(A+B)`. Aggregate new requests by security k: `d_k=B_k*x_raw`, `z_k=min(d_k,max(0,0.1V_pre−H_k))`, where H_k is surviving security notional. Set Z=sum z_k and `lambda_G=min(1,max(0,V_pre−sum H_k)/Z)` for Z>0. With executing exit notionals X_k and cash `C0=C_before+sum X_k`, choose

`lambda*=max{lambda in [0,lambda_G]: C0−lambda Z−kappa sum|lambda z_k−X_k|≥0}`,

`x_eta=lambda*z_k/B_k; n_eta=x_eta/O_ku`.

Zero Z means no admissions. Survivors never resize; zero allocations remain funding-unavailable. Exit is C1 with ten held-security eligible sessions, preserved anchors, held-security-only post-entry qualification, next-qualified-open liquidation, no fold-crossing or fabricated terminal sale. PnL is the accounting identity, not the raw-response sum. All six estimators, two channels and 5/10/20 bps remain as the historical package. S1 is only a directional morphology probe, not a clean test of hedged arbitrage. Its old data/code limitations do not disappear by choosing its label.

### S2 — executable single-leg convergence (A1/B4/C2)

Proposed primary scope: peer only, positive mu and positive gap under the same relationship-validity gates; source is not silently pooled. Let `P*=P_jt*(1+g_t)`, `d_u=(P*−O_ju)/O_ju`. Proposed admission is

`I_S2 = required signal/execution validity AND g_t>0 AND |g_t|/sigma_t≥z0 AND d_u>0 AND m_hat_u>c_hat_RT,u`.

This is an entry-time reevaluation, not use of later data. Preserve the existing simultaneous Option-A long-only capital rule above as a proposed inheritance: `n_j=x_eta/O_ju`. Keep the price target fixed, trigger C2 at the first target-crossing qualified close or ten held-security eligible sessions if that inheritance is approved; execute the next qualified open. Net PnL is `n_j*(P_exit−O_ju)+qualified cash entitlements−costs`. No requirement that the original sum-of-returns anchor also crosses.

`signal gap → standardized gate → remaining open-to-target opportunity → economic hurdle → long admission → entry-based target exit → directional net return`.

This removes pre-entry convergence from the claimed capture but retains market/industry exposure. The price-target bridge and forward m_hat mapping are proposed hypotheses, not established facts. z0, scale choice and expected-capture/cost calibration remain preregistration/development items; no values selected here.

### S3 — hedged relative-value convergence (A2/B4/C4; conditional factor expansion)

Proposed primary scope: peer only, same positive-origin signal orientation; short **hedge** legs require new explicit authority and feasibility, not a relabeling of V1.1's no-short rule. For each estimator construct w_t matching the residual as in A2/C4, not a candidate-specific performance-selected hedge. Apply

`I_S3 = required pair/model validity AND exact declared hedge mapping available AND |d_t|/sigma_t≥z0 AND d_t*d_u>0 AND m_hat_u>c_hat_RT,u AND all-leg executable/borrow/collateral feasibility`.

Here `d_t=g_t`, sigma is an aligned residual-basket scale, `d_u=d_t−Delta B_ON`, and the expected gross correction per capital is forecast in units `s*Delta B_u/L_u`. No unhedged substitute if one leg fails. Set `n_k=s*K_eta*w_kt/(P_kt*L_u)`; keep origin share proportions fixed; exit jointly by C4. Net return is `s*Delta B_u(exit)/L_u + distributions/K_eta − all-in costs/K_eta`.

`signal residual → common normalized/cost gate → borrowable residual-replicating basket → fixed-origin shares → basket correction target → multi-leg liquidation → net relative-basket return`.

For a coherent proposed portfolio extension, define equal raw **gross** admission targets `K_raw=V_pre/(A+B)` for same-open baskets. Existing episode shares retain priority. With normalized signed entry weights v_eta,k=n_k/K_eta, enforce conservative absolute episode-leg commitments `sum_existing |n_eta,k|O_k + sum_new K_eta|v_eta,k|O_k ≤ 0.10V_pre` per security and ≤V_pre in aggregate, plus the explicitly contracted collateral/cash/borrow constraints. A deterministic non-redistributing proposal is: per security compute the available-capacity/request ratio clipped to [0,1]; each new basket takes the minimum ratio across its legs, preserving its hedge; then use a common maximal feasible factor for the simultaneous batch's remaining gross/collateral/cash constraints. Count opposing obligations for borrow and commitment purposes even if net orders reduce execution turnover; do not invent financing relief from netting.

Those short-basket capacity/accounting conventions are **proposals requiring approval**, not existing frozen V1.1 rules. If cash/collateral feasibility cannot be expressed and verified from broker/instrument contracts, S3 cannot yet be an executable protocol. Partial fills, borrow recall, joint exit eligibility and market-calendar mismatches need a consolidated pre-development execution contract; no software default may decide them. This document defines a coherent economic architecture, not a ready-to-run backtest masquerading as one.

### Recommendation among packages

S3 is the most direct match to the stated relative-value/convergence objective, conditional on a defensible hedge and forward correction hypothesis. S2 is an interpretable directional-convergence alternative, not a neutral approximation to S3. S1 remains useful only if the researcher consciously wants the existing morphology probe. Select an estimand first; inability to obtain a short or factor instrument must not select a different hypothesis automatically. No fourth architecture or post-performance fallback is proposed.

## 6. Peer and source are not independent merely because they have different labels

Exactly,

`e_(i→j)=a_(j→i)=−g_(j→i)`.

Therefore the long-source condition `e_(i→j)<0` is the positive peer-gap condition in the reverse direction. Both buy security i. They differ in **gates**, not in the algebraic residual: reverse-peer eligibility additionally requires an expected direction giving UR0>0 (for positive g, mu_i|j>0); source uses MP1>0 and its source-specific evidence conditions instead. MP0 has the same sign as e when its scale is positive. These facts do not make the two fitted directional regressions inverses or make their errors perfectly dependent.

For the same i→j direction, a peer long j and source long i can coexist if their distinct gates pass and neither channel's raw reverse direction causes a DECA collision. Across reversed labels, a peer episode and source episode can instead buy the **same security from the same numerical residual**. Channel-specific episode keys permit this coexistence in S1; it is duplicated economic exposure unless separately accounted for, not independent hypothesis confirmation. Both directional raw gates within one channel still invoke that channel's collision rule.

MP1 here is `log[(amount/volume)/prior_median(amount/volume)]`. Subject to field units, amount/volume is an average transacted price proxy, not a signed order-flow measure or a turnover-intensity measure. It may add a price-level/location condition not algebraically determined by the one-session residual, but this is not demonstrated incremental information, and price trends, corporate actions and units can affect it. Above-reference average price does not identify overbuying, liquidity demand, investor motive or future normalization. No empirical incremental-value claim is made.

**Recommendation:** peer-only core for a selected S2/S3; retain source/MP1 as a separately preregistered exploratory hypothesis or defer its execution until an economic rationale for that price-context interaction is accepted. Do not preserve it in the core solely because the field exists. This recommendation changes nothing in immutable S1 records. If later included, specify overlap/deduplication and hypothesis accounting before data use, not after results.

## 7. Role of the six models

Treat R0-D252, R0-C126, R0-L126, R1-M126, R1-MI126 and R3-252 as **six estimators/conditional representations under one common strategy architecture**, not six separately optimized trading systems. They do not all condition on identical factors or histories, so 'same latent normality' is a research organizing concept, not proof that their estimands coincide.

| Estimator | Signal contribution | Proposed hedge consequence / comparison meaning |
|---|---|---|
| R0-D252 | H252 monthly OLS bridge; distance remains representation-only | Pair response slope; compare longer-history bridge, not distance-selected pairs |
| R0-C126 | H126 weekly OLS bridge; correlation representation | Same mapped hedge as matched R0-L; equality need not be independent evidence |
| R0-L126 | H126 weekly OLS directional reference | Baseline response-conditioned correction hypothesis |
| R1-M126 | Market residualization then residual bridge | Full residual hedge includes pair and remaining market coefficient |
| R1-MI126 | Own-industry and market residualization | Full residual hedge includes pair and distinct industry/market terms |
| R3-252 | Shrunk stratum/pair intercept and slope | Pair-specific pooled/shrunk slope; no automatic factor neutrality |

For S2, a common held-security position rule makes differences primarily signal/support differences. For S3, residual-consistent hedges also differ by estimator: net PnL differences combine signal quality, hedge composition and implementation cost. Report this distinction rather than attributing every return difference to 'better relationship estimation'. Use a common declared threshold/calibration procedure, sizing and evaluation protocol, with matched-support attribution and native deployability separately. Do not tune each candidate until it wins or collapse R0-C/R0-L duplicates into extra corroboration. No candidate is selected from prior relationship or trading performance here.

## 8. Data contracts derived after the equations

This is a schema/lineage inventory, not an empirical sufficiency audit. Existing code/specifications indicate field types and intended artifacts; no raw payload or result is opened now. Presence never proves qualification. In particular existing C04 mismatch/unavailable accounting findings remain unresolved and no existing complete economic dataset is certified.

| Layer | S1 minimum | S2 increment | S3 increment | Existing versus genuinely new requirement |
|---|---|---|---|---|
| Relationship estimation | PIT raw responses, stable IDs, C04/C05/C06, fixed market/industry inputs, H/U histories, six model artifacts | Same unless separately chosen scale/forecast mapping needs prior calibration samples | Same plus explicit signal-to-tradable-hedge coefficient mapping | Existing model/input schemas cover research fields; code/input conformance remains unproven |
| Signal | Both directional predictions, preserved A3, evidence flags, episode state; source amount/volume/reference | Qualified signal-close price, remaining open target, aligned PIT scale, pre-entry capture forecast | Aligned residual-basket scale and origin leg prices/coefficient lineage | A1 H126 and A3 artifacts are not interchangeable by field name; new derived layers need separate specification, not necessarily a new provider |
| Hedge | None | None | Tradable hedge instrument IDs, contracts, constituent weights/rebalance schedules, exposures/Gamma and tracking definitions | Market/industry response series do not establish executable replication; new qualification/possibly new data required |
| Execution prices | Qualified next raw open, tradability/suspension status | Same with explicit overnight target adjustment; actual feasible fill assumptions | Synchronized executable quotes/opens across legs, joint/partial-fill policy, calendars, lot/tick constraints if implemented | Existing open field is only a price observation, not proof of executable capacity |
| Corporate actions | Effective dates, publication/availability, entitlements, identity continuity, qualification coverage | Same; target adjusted consistently with holdings | All legs including manufactured distributions on shorts and hedge instruments | Existing bounded calendar is not authoritative no-action proof; accounting/data gaps remain; no repair now |
| Short/borrow | None for long-only | None for long-only | Security/date PIT availability, locate, rates, recalls/buy-ins, collateral/margin and short-sale constraints | Not established by existing long-only contracts; mandatory new qualified contract/data before S3 execution |
| Costs | Frozen scenario fees; not claimed market-calibrated | PIT spread/slippage/fees/impact or justified conservative bounds for economic hurdle | Each leg plus funding, borrow, collateral and liquidation costs | Existing 5/10/20 bps scenarios alone insufficient to validate a cost-aware/short strategy |
| Valuation | Qualified prices, shares, cash/distributions, unavailable intervals | Same with fixed target lineage | All legs, short liabilities, funding/collateral, distributions, cash reconciliation | Requires economic qualification, not just complete numerical arrays |

For S1, existing **field architecture** is largely sufficient, but not demonstrated qualified coverage. S2 mainly requires explicitly derived entry-gap/forecast/scale layers plus defensible execution costs; additional market data depend on whether current official lineage can meet the approved contract. S3 necessarily requires evidence of tradability/borrow/funding and hedge replication that the six relationship files alone cannot provide. No provider, mirror, instrument or acquisition is selected here. Missing evidence is not filled by a generic constant without researcher approval.

## 9. Future development versus validation — proposed, not authorized

### Exposure ledger first

2015–2019 inner research, 2020–2023 OF4 and 2024–2025 final research inputs/results have already been used/opened. The repository also records prior trading computation and unavailable economic dispositions. No valid complete trading PnL is inspected in this task; that does not reset the knowledge state or make these intervals pristine. The frozen V1 claims and their limitations remain historical. A redesigned trading hypothesis cannot be retroactively described as preregistered against the opened 2024–2025 region.

### Development proposal

Prefer 2015–2019 as the explicit initial development region because it was designated for development and is already exposed. Use chronological expanding/rolling training within it, with no future information; keep 2020–2023 and 2024–2025 out of calibration under this proposal. This restriction preserves a smaller design budget, not an assertion that the later periods are untouched. Warm-up data stay separated from scored periods.

Within a **future separately authorized** development action:

1. Verify executability/accounting with synthetic cases and metadata first, then qualified historical inputs; no performance-dependent eligibility fixes.
2. Select an economically declared scale/cost/capture mapping and a finite calibration budget before opening development outcomes. If z0 cannot be justified economically, calibrate its predefined objective within training folds, not by unconstrained best-Sharpe search.
3. Estimate execution/borrow/impact assumptions from appropriate independent quotes/contracts/transaction evidence with PIT timestamps. Historical price series alone do not identify fills or borrow availability.
4. Validate hedge mapping by units, residual replication, exposure stability and accounting, not merely by improved PnL. Freeze any added exposure estimator and its data before evaluating it.
5. Use purging/embargo sufficient for the actual maximum label/position overlap and input availability. Because suspended exits can outlive a nominal ten-session clock, a fixed ten-day embargo is not automatically sufficient. Unclosed/unknown episodes need predeclared handling.
6. Freeze one selected architecture, source scope, six-model comparison role, scales, threshold calibration outputs, cost/borrow model, clock, joint-leg failure policy and economic estimand before validation. No adaptation after validation reveal.

Development-sample trading PnL, if later authorized, is explicitly exploratory; it is not inspected now. Threshold selection and forward-capture estimation consume research degrees of freedom even if no unique winning model is declared.

### Valid evaluation after redesign

**Preferred:** prospective forward observation beginning only after a dated final strategy/protocol freeze and a verified no-access boundary. Let T_freeze be that future timestamp; validation starts at the first qualified session strictly after T_freeze and after all operational prerequisites. Do not call the whole calendar year 2026 untouched: some of it has already occurred and its exposure status is not established. Fix the calendar/end-information budget and permissible stopping conditions in advance, independent of realized returns.

An alternative is an independently custodially sealed historical sample, but only if a documented access audit demonstrates it was never used in project decisions and selection was not conditioned on outcomes. No such sample is verified here, so no exact historical dates are claimed available.

Previously opened 2020–2025 may later serve as explicitly retrospective robustness/stress analysis, not final untouched confirmation. Nested/purged chronological resampling of exposed data can estimate a declared development procedure more honestly than in-sample fitting, but it does not erase human adaptive exposure. A new holdout/prospective protocol must also predeclare six-model/multiple-channel claim handling; no fresh p-values, multiplicity procedure or winner rule is adopted in this document.

## 10. Consolidated researcher decision

The following are proposals for one integrated selection, not sequential engineering defaults. Numerical calibration and executable-short contracts remain future bounded protocol fields; this design checkpoint is intentionally not an execution authorization.

| Decision | Options | Key equation | Economic meaning | Pros | Cons | Data needs | Recommendation |
|---|---|---|---|---|---|---|---|
| A: position | A1 single leg; A2 relationship hedge; A3 factor hedge | n proportional to 1; (1,−beta); or (1,−h), respectively | Directional rise; pair-relative correction; factor-relative normalization | Increasing isolation when hedge matches estimand | Short/replication costs; beta not automatically an equilibrium hedge | Long prices versus joint hedge/borrow/exposure data | A2 for pair convergence, including R1 factor expansion if needed; A3 only for an explicitly different factor-relative estimand |
| B: threshold | B1 none; B2 normalized; B3 economic; B4 combined | abs(d)/sigma≥z0 AND m_hat>c_hat_RT | Material, capturable discrepancy rather than any nonzero error | B4 connects statistical scale and economics | Requires forecast/cost mapping and predeclared calibration | PIT aligned scales, independent execution-cost evidence | B4; no numerical z0/rho/cost buffer selected |
| C: resolution | C1 signal sum; C2 entry target; C3 updated model; C4 basket | r=d_u−post-entry movement; theta=first qualified target hit or cap | What the position is supposed to capture after entry | C2/C4 align target and holdings | Target bridge still a hypothesis; fill gaps/financing matter | Qualified entry/exit and all relevant legs | C4 with A2; C2 with A1; not C3 by default |
| Peer/source | Both as S1; peer core with separate source exploration; source deferred | e_i→j=−g_j→i | Distinct gates can trade the same underlying reverse gap | Separation avoids double-counted confirmation | Source MP1 lacks demonstrated mechanism meaning | Ratio units/lineage; distinct preregistered channel accounting | Peer core; defer source core inclusion pending economic rationale |
| Six models | Separate optimized strategies; common rule with six relationship representations | signal_c → same architecture/calibration protocol | Signal/representation comparison rather than six searches | Cleaner attribution and preserved research | S3 hedge composition still changes across models | Candidate lineage, support and hedge diagnostics | Common architecture; retain all six without performance selection |
| Development/validation | Exposed-data development; prospective holdout; verified sealed independent sample | train before freeze; validate strictly after T_freeze | Honest post-redesign assessment | Prospective boundary avoids relabeling old data | Delays confirmation; sealed historical alternative unverified | Access ledger, final protocol and qualified future feed | 2015–2019 development proposal; prospective untouched validation; 2020–2025 retrospective only |

### At most three complete architecture packages for selection

| Package | Coherent construction | What selecting it means | Remaining pre-development bindings |
|---|---|---|---|
| **S1 — morphology probe** | Existing single leg + existing no-magnitude gates + signal-origin C1 | Accept directional morphology economics explicitly; no claim of clean hedged convergence | Existing implementation/data conformity must still pass; no automatic rerun |
| **S2 — executable directional convergence** | Peer single leg + B4 + fixed entry-adjusted price target C2 + proposed existing long-only capital discipline | Test capturable directional correction, acknowledging factor exposure | Target bridge, aligned scale/z0, capture forecast/cost calibration and validation plan |
| **S3 — hedged relative-value convergence (recommended conditionally)** | Peer residual-matched hedge + B4 + fixed-origin entry-adjusted basket target C4 + explicit joint-leg funding | Test relative correction with economics closest to statistical arbitrage | Tradable hedge mapping, short/borrow/collateral/joint-fill contract, scale/calibration budget, basket capacity/clock and prospective validation |

Recommendation is economic and ex ante, not a claim that S3 is feasible or profitable. Researcher selection authorizes neither data acquisition nor execution by itself; the selected package must first become a complete versioned protocol with the listed bindings. Do not use unavailable hedge data to silently change the package. No V2 implementation is initiated, no V1 artifact is overwritten, and no trading PnL has been computed or inspected for this task.

**TRADING STRATEGY ECONOMIC REDESIGN / RESEARCHER DECISION REQUIRED**
