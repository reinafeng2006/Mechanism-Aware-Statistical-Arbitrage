# S3 convergence target bridge — researcher comparison

2026-09-23 — DESIGN ONLY / TARGET A AND TARGET B UNSELECTED.

[Fund-share/M1/static-origin/T1 construction is approved](../../decisions/S3_PROXY_CONSTRUCTION_APPROVAL.md). This checkpoint compares only the two requested convergence targets. It neither changes the model-based z-gate nor selects a target, direction rule, new magnitude gate or parameter. No observations or estimates are used.

## 1. Signal, tradable coordinate and exact algebra

At the signal origin t, freeze the applicable relationship coefficients and proxy construction. In consistent return units:

epsilon_model,t=y_j,t−beta_t*y_i,t−gamma_model,t'f_t−a0_t;
epsilon_trade,t=y_j,t−beta_t*y_i,t−h_t'H_t−a0_t;
xi_t=epsilon_model,t−epsilon_trade,t=h_t'H_t−gamma_model,t'f_t.

Therefore:
d_model,t=−epsilon_model,t;
d_trade,t=−epsilon_trade,t=d_model,t+xi_t.

The actual unique-instrument vector is w_t=(1,−beta_t,−h_t') after physical duplicate aggregation. Its contemporaneous return combination equals epsilon_trade,t+a0_t. The intercept is not a traded asset; subtracting it defines the origin model-zero departure, not a stream of future intercept payments.

M1 matches declared exposures A_t*h_t=gamma_neut,t. It does not imply xi_t=0:
xi_t=(gamma_neut,t−gamma_model,t)'f_t+tau_t.
Even acceptable unwanted tracking tau does not make the intentional term small. Consequently Target B is not generally a small perturbation of Target A.

Algebraic error measurement in either coordinate does not establish future mean reversion, equilibrium or a profitable forward correction. Both targets impose a prospective economic displacement hypothesis.

## 2. Common fixed-origin price/cash-flow convention

For derivation, let P_k,t and O_k,u be qualified signal and declared entry reference prices in the same origin coordinate. All transformations/entitlements must reconcile to the eventual accounting convention; raw action jumps cannot count as convergence. Reference marks are not guaranteed fills.

Delta B_ON=sum_k w_k,t*(O_k,u/P_k,t−1);
Delta B_u(q)=sum_k w_k,t*(P_k,q−O_k,u)/P_k,t;
L_u=sum_k abs(w_k,t)*O_k,u/P_k,t.

For target choice J in {A,B}, define D_t^J and D_u^J=D_t^J−Delta B_ON. The analogous persistence condition is D_t^J*D_u^J>0. If it fails, the original target has vanished or reversed; do not reset it or turn the episode into a new reverse opportunity.

For the proposed target-oriented direction s_J=sign(D_u^J):
n_k^J=s_J*K*w_k,t/(P_k,t*L_u),
sum_k abs(n_k^J)*O_k,u=K.

Under the reference-price convention:
gross price movement(q)/K=s_J*Delta B_u(q)/L_u.
Signed entitlements and unique costs are accounted separately as already required. At an exact target displacement s_J*Delta B_u=abs(D_u^J):
G_target,u^J=abs(D_u^J)/L_u.

Intended K remains the approved denominator even for incomplete or failed attempts. Actual fills and price limits remain a later execution contract; future fills cannot justify earlier orders. The target formulas do not override that timing boundary.

## 3. Only two target definitions

| Quantity | Target A — model-gap displacement | Target B — actual-basket displacement |
|---|---|---|
| Origin target D_t^C | D_t^A=d_model,t | D_t^B=d_trade,t=d_model,t+xi_t |
| Remaining target D_u^C | d_model,t−Delta B_ON | d_model,t+xi_t−Delta B_ON |
| Full target price displacement | abs(d_model,t−Delta B_ON)/L_u | abs(d_model,t+xi_t−Delta B_ON)/L_u |
| Interpretation | The model departure is a hypothesized correction amount for the proxy basket | The actual proxy basket's origin departure from the retained a0 target is hypothesized to correct |
| Coordinate alignment | Target magnitude comes from model; accumulated movement comes from actual basket | Origin departure and accumulated movement use the same basket coordinate |
| Principal limitation | Transports magnitude across different coordinates without an identity guaranteeing capture | Model-extreme selection can coexist with small, zero or oppositely signed trade departure |

With identical w and entry references:
D_t^B−D_t^A=xi_t;
D_u^B−D_u^A=xi_t.

No new xi at q is used to update either target. Static-origin means both keep their origin target fixed; future exposures, coefficients, residuals or tracking diagnostics do not reset it. Same gap magnitudes are obtained if xi_t=0, but nonzero xi can affect magnitude, sign, persistence, shares, costs and exits.

Target A is not algebraically wrong: it is a stronger cross-coordinate economic hypothesis. It must not be described as the measured trade-residual gap. Target B has a direct origin-coordinate interpretation, but it still does not turn a one-period return error into a proven stationary price spread.

## 4. Direction and no-reversal consequences must be explicit

For A, proposed target-oriented direction follows d_model at origin and the surviving same-sign D_u^A at entry. This matches the directional interpretation of the historical model-gap construction.

For B, target-oriented convergence follows sign(d_model+xi) at origin and the surviving same-sign D_u^B at entry. It can oppose sign(d_model). The approved absolute model z-gate is two-sided, but that alone is not authority to silently approve this directional remapping.

A B decision therefore must explicitly acknowledge whether trades may follow the actual-basket target when its sign differs from the model gap. Requiring extra model/trade sign concordance would be an additional admission predicate, not implied by B or by the existing absolute z threshold; none is adopted here.

D_t=0 or failed D_t*D_u>0 supplies no surviving directional convergence target. Tiny nonzero targets are not automatically excluded by any approved new floor; no target-relative magnitude threshold is invented. Exceptional contractual exits can still override ideal hedge direction as already approved.

## 5. Model z-gate alignment

The approved gate is:
z_model,t=d_model,t/sigma_model,t;
abs(z_model,t)>=Q^w_0.95(abs(z_model,ref)).

Sigma remains the approved current-origin aligned MODEL residual MAD, common H126/daily with qualified support. The reference weighting/alpha=0.05 remain unchanged. Numerical z0 has NOT been estimated.

For A: model z measures the standardized size of the very gap used as the origin target, but not the standardized risk of the proxy portfolio. H-C's proxy risks/costs still require independent qualification.

For B: model z is signal discovery/selection. The approved proxy map and xi identity then give D_t^B in the trade coordinate. The claim becomes: model-extreme pair-conditioned events predict convergence of the contemporaneous actual-basket departure. This is compatible with the approved H-C economic estimand without algebraically redefining z.

Thus selecting a tradable-basket target does NOT logically require changing the threshold object. It requires clearly separating the model event-selection rule from the trade-coordinate target/orientation.

If instead the intended claim were “the TRADE residual itself lies in its extreme 5% reference tail”, a trade-residual scale, qualified history and its own reference distribution would be needed. That would be a separate researcher amendment, not a mechanical consequence of B. Dividing d_trade by the existing model sigma would not produce the already-approved standardized object. No such threshold redefinition or extra trigger is proposed in this two-target comparison.

B can therefore pass the model z-gate while its trade target is small or opposite in sign. Report this design property; do not silently add a second z-gate, shrink xi, relax T1 or change alpha.

## 6. C4 exit under each target

For a selected J, define the surviving fixed-origin remainder:
r_J(q)=D_u^J−Delta B_u(q).

The proposed normal target trigger is the first qualified close q satisfying:
s_J*r_J(q)<=0,
equivalently s_J*Delta B_u(q)>=abs(D_u^J).

The ordinary C4 trigger is the earlier of that target trigger and the eventually frozen qualified basket holding cap. Actual liquidation follows the approved joint-exit/exception contract, not a fictional fill at the trigger close. Cap, qualification clock, eta and exact exception timing remain unresolved.

For the same realized unsigned basket path:
r_B(q)=r_A(q)+xi_t.

If A and B share direction, their trigger levels differ by the origin tracking difference; if directions differ, they seek opposite signed corrections. The same path can be F under one and P/N/A under the other. A target touch can be followed by loss before execution, and realized payoff can exceed the target through overshoot.

Apply approved X priority for forced/exceptional exits and the E-A abort/unwind accounting. A failed entry has no completed basket episode and cannot be assigned a fictitious C4 target hit. Its economic costs/results still enter the attempted-trade population under the later-frozen event schema.

## 7. Capture/cost consequences without estimation

The approved model remains:
mhat_u^J=sum_(r in {F,P,N,A,X}) pihat_r^J*Ghat_r^J,
with pooled prior-event P1 counts and state-conditional arithmetic means under one common architecture, not flexible event-level conditioning.

The superscript J describes the prospective label/policy definition, not two authorized fits or a request to select the more profitable result. Select the target before future outcomes are used to estimate its model.

Changing A to B can change:
- Origin and remaining target, orientation and no-entry population.
- F/P/N/A classification through b_J(q)=s_J*Delta B_u(q)/abs(D_u^J).
- Target-hit and executable holding durations.
- Actual entry/exit prices and signed entitlements.
- Borrow direction, duration, funding and exit friction.
- Failed-attempt composition and X paths.

Consequently pi_r, G_r, the joint (R,G,T,exposure path) law and expected costs must all be defined under the SAME selected target and execution policy. One cannot reuse A's capture forecast with B's exit/duration assumptions. No such quantities exist as approved estimates now.

For either J, G_target=abs(D_u^J)/L_u is full target price displacement only. It is not mhat, a realized payoff ceiling, or probability times target by default. Under the raw pooled P1 baseline, mhat equals the pooled mean gross payoff within its fixed training population. It does not automatically shrink with a particular event's small D_u. E1 is not a substitute for an unapproved target-magnitude gate or an event-specific forecasting model.

All attempt gains/losses/costs retain intended K. A direction change affects actual short legs and therefore can change feasibility and costs; no sign-symmetric borrow/cost assumption is justified.

## 8. Researcher comparison and ex-ante assessment

| Decision dimension | A | B |
|---|---|---|
| Model signal and target magnitude linked directly | Yes | No: model discovery precedes trade-coordinate mapping |
| Target and held basket share a coordinate | Not guaranteed | Yes, under qualified return/price/cash-flow mapping |
| Meaning of xi | Cross-coordinate gap between transported target and trade departure | Explicit adjustment to origin target; never updated to reset it |
| Model-direction consistency | Direct under target-oriented entry | Possible sign disagreement requiring explicit acceptance |
| Need to redefine approved z? | No | No, if model z is retained as discovery; trade-tail claim would require separate amendment |
| Main scientific risk | Treating a model-coordinate gap as a capture promise for another basket | Mistaking model extremeness for trade extremeness, or assuming measured trade error predicts correction |
| Before estimation | Freeze A's cross-coordinate hypothesis and execution semantics | Freeze B's target/orientation mapping and discovery interpretation |
| Remaining numerical prerequisites | Same unselected cap/eta/support/T1/auxiliary-exposure details | Same; no extra numeric gate silently added |

Ex-ante recommendation for consideration, NOT selection: B more directly matches the approved claim of convergence in the actual approximately factor-neutral tradable basket, provided model z is explicitly retained only as discovery and any model/trade direction disagreement is expressly resolved. A remains a coherent alternative if the researcher intends the stronger hypothesis that the original model gap forecasts the proxy basket's correction amount.

Neither recommendation is based on feasibility measurements or performance. Choosing B would not itself demonstrate convergence; choosing A would not eliminate tracking risk. No target or orientation amendment is approved by this document.

## 9. Stop

Approved fund-share/M1/static/T1 construction is recorded separately. Actual funds, auxiliary exposures, T1 numbers and detailed execution conditions remain unresolved. This checkpoint compares ONLY A and B; no empirical comparison, new threshold, third target, automatic fallback or numerical parameter is introduced.

No funds named/selected, data acquired, exposures/tracking/capture/cost or numerical z0 estimated, implementation, backtest or PnL inspection. NEXT_ACTION remains NONE.

**S3 CONVERGENCE TARGET BRIDGE / RESEARCHER DECISION REQUIRED**
