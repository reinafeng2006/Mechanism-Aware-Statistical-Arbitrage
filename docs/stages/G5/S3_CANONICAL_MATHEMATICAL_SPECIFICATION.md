# Canonical S3 mathematical architecture

2026-09-27. Current S3 architecture consolidation; not an executable protocol or empirical result.
Authority: [Target B approval](../../decisions/S3_TARGET_B_CONVERGENCE_APPROVAL.md) and [post-V1 ledger](../../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).
Earlier V1/V1.1 specifications remain historical and unchanged. This document controls the redesigned S3 chain together with its approved decisions; unresolved executable bindings are exhaustively grouped in the [pre-development audit](S3_PRE_DEVELOPMENT_BINDINGS_AUDIT.md).

## 1. Claim and common architecture

Prospective H-C hypothesis: extreme pair-conditioned abnormality predicts subsequent convergence in a preregistered approximately factor-neutral tradable relative-value basket. This is not a demonstrated equilibrium, stationarity or profitability claim.

One architecture applies to R0-D252, R0-C126, R0-L126, R1-M126, R1-MI126 and R3-252. Relationship estimator definitions, windows and refresh rules are not changed. Candidate-specific coefficients do not permit six optimized execution or second-stage forecasting systems.

The complete chain is:

**model abnormality → model z-gate → H-C proxy mapping → tradable target → overnight persistence → capture/cost gate → execution → C4 tradable-basket convergence → PnL accounting.**

The final arrow specifies economic accounting only; no PnL is computed or inspected.

## 2. Model abnormality and scale

Suppress candidate c when unambiguous. In compatible return coordinates:
\[
\epsilon_t^{model}=y_{j,t}-\beta_t y_{i,t}-(\gamma_t^{model})'f_t-a_{0,t},
\qquad d_t^{model}=-\epsilon_t^{model}.
\]

R0-D/C/L and R3 use their already-approved pair-response slope/intercept bridges; their explicit gamma_model is zero, not a claim of zero actual factor exposure. R3 retains conditional pair effects. For R1,
\[
\mu_{j|i}=f_j+\alpha_u+\beta(y_i-f_i).
\]
Writing each stock factor fit as \(f_k=a_k+b_k M+\delta_k I_k\) gives
\[
a_0=\alpha_u+a_j-\beta a_i,\qquad
\gamma_{model}'f=(b_j-\beta b_i)M+\delta_jI_j-\beta\delta_iI_i.
\]
R1-M omits industry terms; R1-MI includes them, combining identical industry coordinates. Stock fitted component f_k and vector factor f are distinguished by their indices; neither implies a tradable research factor.

Replay the CURRENT origin model on prior qualified aligned observations:
\[
\epsilon^{model}_{v;t}=y_{j,v}-\beta_t y_{i,v}-(\gamma_t^{model})'f_v-a_{0,t},
\]
\[
\sigma_t^{model}=1.4826\operatorname{median}_{v\in W_t}
\left|\epsilon^{model}_{v;t}-\operatorname{median}_{r\in W_t}\epsilon^{model}_{r;t}\right|.
\]
W_t contains 126 qualified prior aligned observations on common dates across six estimators for common attribution/reference work. Daily strictly-prior scale refresh excludes the evaluated response. Underlying relationship H/U is unchanged. Invalid, zero, nonfinite, unsupported or insufficient scale gives **SIGNAL UNAVAILABLE**, not zero abnormality or a shortened/floored rescue. MAD centering does not recenter the numerator's model-zero target.

Current-origin formation overlap can understate true future prediction error; this is descriptive dispersion, not full predictive uncertainty. H252 MAD and H126 SD are non-selecting robustness only.

## 3. Frozen discovery gate

\[
z_t^{model}=d_t^{model}/\sigma_t^{model},\quad
z_0=Q^w_{0.95}(|z^{ref}|),\quad |z_t^{model}|\ge z_0.
\]
Alpha is fixed at 0.05. The empirical inverse CDF is
\[
F_w(x)=\sum_l\omega_l1\{|z_l^{ref}|\le x\},\qquad
Q^w_{0.95}=\inf\{x:F_w(x)\ge0.95\}.
\]
Preserve equal chronological-block influence, equal unordered-pair influence within block, equal supported-direction influence within pair, and equal estimator-group influence. Groups: R0-D; joint R0-C/R0-L with equal within-group shares; R1-M; R1-MI; R3. No silent missing-group reweighting. Numerical reference formation/support/refresh details remain unbound; numerical z0 is NOT ESTIMATED.

This is rarity/materiality, not Gaussian significance, p-value, 5% false-positive control, convergence probability or economic profitability. Inclusive ties can admit more than 5% reference mass. No parametric 1.96 substitution, signed-tail equalization, adaptive alpha, occurrence-driven threshold selection or finite-grid fallback. Model z remains discovery; no trade-residual threshold is introduced.

## 4. Proxy map and difference decomposition

Common qualified fund-share market/industry slots, actual instruments still unselected:
\[
\gamma_t^{neut}=B_{j,t}-\beta_t B_{i,t},\quad H_t=A_t'f_t+e_t,\quad A_th_t=\gamma_t^{neut}.
\]
Preserve compatible model coefficients; fill missing exposure dimensions only through one common auxiliary rule yet to be fully bound. R0/R3 may require nonzero neutralization despite gamma_model=0.

M1:
\[
h_t=A_t^{-1}\gamma_t^{neut}
\]
for square nonsingular A; for full-row-rank underdetermined A:
\[
h_t=A_t'(A_tA_t')^{-1}\gamma_t^{neut}.
\]
No M2 rescue. Required industry proxy missing or exact declared matching mathematically/qualification infeasible gives **HEDGE UNAVAILABLE**. Cross-industry pairs require each required industry dimension; combine common dimensions before mapping. No market-only substitution.

On actual physical instruments, combine duplicates in
\[
w_t=(1,-\beta_t,-h_t').
\]
A fund and its constituents are not duplicates. Define
\[
\epsilon_t^{trade}=y_{j,t}-\beta_ty_{i,t}-h_t'H_t-a_{0,t},
\quad \xi_t=\epsilon_t^{model}-\epsilon_t^{trade}
=h_t'H_t-(\gamma_t^{model})'f_t,
\]
\[
\ell_t=\gamma_t^{neut}-A_th_t,\quad
\tau_t=h_t'H_t-(\gamma_t^{neut})'f_t,
\quad \xi_t=(\gamma_t^{neut}-\gamma_t^{model})'f_t+\tau_t.
\]
Xi is total model-to-trade difference, including intentional neutralization. Tau is unwanted implementation/proxy tracking. M1 does not establish exact return replication. T1 uses residual exposure, signed mean/RMS tau, tail/max path discrepancy, cash-flow-consistent holding discrepancy and drift; its numerical qualification remains unbound. No universal-small-xi requirement.

## 5. Target B and PIT orientation

\[
D_t^{trade}=d_t^{model}+\xi_t=-\epsilon_t^{trade}.
\]
The intercept defines the origin departure; it is not a purchased asset or future stream of intercept payments. This prospective target does not prove that an observed return residual must mean revert.

Every input to origin xi must be available at signal t. Freeze the qualified origin transformation and target. Subsequent realized tau, changed coefficients/exposures or new residuals cannot reset it.

Require \(d_t^{model}D_t^{trade}>0\). A defined product <=0 gives **TARGET-MAPPING UNAVAILABLE / NO TRADE**. Missing/nonfinite required inputs remain unavailable. No direction reversal, Target A, second z-gate or new target floor.

For qualified signal prices P and declared entry reference marks O in a consistent origin coordinate:
\[
\Delta B_{ON}^{trade}=\sum_k w_{k,t}(O_{k,u}/P_{k,t}-1),\quad
D_u=D_t^{trade}-\Delta B_{ON}^{trade}.
\]
Require \(D_t^{trade}D_u>0\). A defined product <=0 gives **OPPORTUNITY EXHAUSTED / NO TRADE**; missing references remain unavailable. Thus
\[
\operatorname{sgn}d_t^{model}=\operatorname{sgn}D_t^{trade}
=\operatorname{sgn}D_u=s.
\]
No resetting at the open. Reference marks are not guaranteed fills; a future opening price cannot be used to justify earlier orders. Exact executable timestamp/mark binding remains a pre-development requirement.

## 6. Capital and static shares

For finite positive qualified prices, nonzero qualified basket, K>0 and L_u>0:
\[
L_u=\sum_k|w_{k,t}|O_{k,u}/P_{k,t},\quad
n_k=\frac{sKw_{k,t}}{P_{k,t}L_u},
\]
\[
\sum_k|n_k|O_{k,u}=\frac{K}{L_u}\sum_k|w_{k,t}|O_{k,u}/P_{k,t}=K.
\]
This identity holds for the ideal submitted share construction at declared marks. Lot rounding, partial fills and fill deviations require a separately bound qualification/accounting policy; they cannot silently redefine K or exact geometry.

Shares remain static except qualified entitlement-preserving transformations, authorized contractual exceptional actions and liquidation. No drift-driven rebalancing.
\[
G_u^{target}=|D_u|/L_u
\]
is full remaining target displacement per intended K, neither expected capture nor payoff ceiling. Intended K is fixed before submission and is also the failed-attempt denominator; peak deployed gross is diagnostic and NAV is the portfolio denominator.

## 7. C4 and scenario coordinate

For the static-origin actual basket:
\[
\Delta B_u^{trade}(q)=\sum_k w_{k,t}(P_{k,q}-O_{k,u})/P_{k,t},\quad
R^{trade}(q)=D_u-\Delta B_u^{trade}(q).
\]
Apply qualified entitlement/accounting transformations; raw corporate-action jumps are not convergence. The primary normal target trigger is
\[
sR^{trade}(q)\le0\iff s\Delta B_u^{trade}(q)\ge|D_u|.
\]
The qualified monitoring clock, holding cap and risk/exception contract remain to be frozen. A trigger launches joint liquidation; no fill at the trigger is assumed. Exceptional actual holdings/obligations must be tracked even when ideal geometry is broken.

Define progress \(b(q)=s\Delta B_u^{trade}(q)/|D_u|\). Preserve the existing disjoint classifier for qualified fully observed paths: X priority under the eventual exceptional contract, otherwise F for target hit by cap (tie included), P for no hit and eta<b_cap<1, N for no hit and |b_cap|<=eta, A for no hit and b_cap<-eta. Eta in [0,1), cap, X boundaries/precedence and censoring remain unresolved. Unknown paths are never silently zero, N or X. Target hit and executable payoff differ; F may have overshoot or loss during liquidation.

## 8. Capture, costs and admission

Pooled chronologically prior qualified events, with one common fixed pooling architecture:
\[
\widehat\pi_r=N_r/N,\quad
\widehat G_r=N_r^{-1}\sum_{\eta:R_\eta=r}G_\eta,\quad
\widehat m_u=\sum_{r\in\{F,P,N,A,X\}}\widehat\pi_r\widehat G_r.
\]
Here eta as event index is distinct from the unresolved non-resolution tolerance. Payoffs, labels and the joint (R,G,T,exposure path) law use Target B and intended K. Supported raw arithmetic P1 implies the overall pooled mean within its fixed pool. No flexible event-level model, six independently tuned systems or non-equivalent multiplication by an event's target magnitude.

\[
\widehat c_{RT,u}=c_{entry,u}+E[c_{exit,u}]+E[c_{borrow,u}]
+E[c_{funding,u}]+E[c_{other,u}],\qquad
\widehat m_u>\widehat c_{RT,u}.
\]
Same actual basket, size, K, duration/exposure law, liquidation and feasibility throughout. Use one non-overlapping ledger: fill-embedded execution deviations cannot also be charged as spread/slippage/impact; entitlements/manufactured payments once; collateral principal is not a cost; short proceeds are not assumed free funding. Missing required capture support or cost evidence gives **ECONOMIC GATE UNAVAILABLE**. No safety margin or cost multiple; P3 inactive.

Economic admission requires scientific discovery, qualified hedge/target, both sign tests, supported E1 and complete execution/borrow feasibility. Scientific validity does not imply executability.

## 9. Entry, exits and attempt accounting

Approved entry branch:
prepared/qualified → submitted → first fill (economic exposure) → complete qualified basket (admitted episode).
At the frozen incomplete/failure condition: abort latched → cancel outstanding orders → deterministic unwind of actual and late fills → close only after obligations reconcile. No completion chase. Exact deadlines, lot/fill conditions and unwind order remain unbound.

Normal C4/cap or contractual trigger → liquidation pending → partial liquidation/outstanding obligations → reconciled closed. Exact transitions for suspension, mismatch, recall/buy-in/margin, corporate actions and partial liquidation remain to be frozen. Exit precedence is binding legal/contractual obligations, feasible risk reduction, then hedge geometry. No discretionary replacement or unspecified risk algorithm.

E-A includes every failed partial attempt's market results, execution deviations, fees, borrow/funding, entitlements and unwind obligations even without an admitted episode:
\[
E[R_{attempt}]=p_{admit}E[R\mid admitted]+(1-p_{admit})E[R\mid failed].
\]
Net attempt return is reconciled signed cash-flow gains/losses less uniquely assigned costs, divided by intended K. Full fills reconcile to the basket price component \(s\Delta B_u/L_u\) plus qualified entitlements/execution accounting; failed attempts use actual fill/exposure paths. This is an accounting identity, not an authorized new admission forecaster. Event-branch reconciliation with P1 remains a binding requirement.

## 10. Closure boundary

Target B closes the mathematical architecture, not numerical specification, empirical qualification or executable readiness. All unbound fields are consolidated in one [pre-development protocol gate](S3_PRE_DEVELOPMENT_BINDINGS_AUDIT.md). No actual funds or numerical tolerances selected; no data, fitting, quantile computation, implementation, C04 repair, backtest or PnL inspection. Inactive alternatives cannot rescue missing evidence. NEXT_ACTION = NONE; frozen V1 unchanged.

**S3 MATHEMATICAL ARCHITECTURE CLOSED / PRE-DEVELOPMENT BINDINGS REQUIRED**
