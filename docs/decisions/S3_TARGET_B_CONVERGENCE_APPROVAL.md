# S3 Target B — researcher approval

Decision ID: S3-TARGET-B-2026-09-27.
Status: APPROVED MATHEMATICAL ARCHITECTURE / PRE-DEVELOPMENT BINDINGS REQUIRED.
Authority: direct researcher instruction “RESEARCHER DECISION — SELECT TARGET B: TRADABLE-BASKET CONVERGENCE TARGET”.
Ancestry: [target comparison](../stages/G5/S3_CONVERGENCE_TARGET_BRIDGE_DESIGN_CHECKPOINT.md), [proxy construction](S3_PROXY_CONSTRUCTION_APPROVAL.md), [authority ledger](../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).

## Approved target and signal separation

Select Target B. Model-space abnormality discovery is distinct from tradable-basket convergence and economic realization.

\[
d_t^{model}=\mu_{j|i,t}-y_{j,t},\quad
z_t^{model}=d_t^{model}/\sigma_t^{model},\quad
|z_t^{model}|\ge Q^w_{0.95}(|z^{ref}|).
\]

The previously approved model scale, alpha=0.05, weighting and inclusive inequality are unchanged. No proxy/trade-coordinate scale or threshold is substituted.

\[
D_t^{trade}=d_t^{model}+\xi_t.
\]

All quantities entering the origin transformation xi must be available by the signal timestamp under the qualified PIT mapping. Future realized tau cannot alter admission, orientation, target or exit retrospectively; it is a tracking/attribution diagnostic. Model d itself is not the amount the proxy basket must capture.

Require \(d_t^{model}D_t^{trade}>0\). Otherwise, for a finite defined product <=0, record **TARGET-MAPPING UNAVAILABLE / NO TRADE**. Missing/nonfinite required target inputs are also unavailable, never permission to trade. No reversal and no Target A substitution.

For the approved actual basket:
\[
D_u=D_t^{trade}-\Delta B_{ON}^{trade},\qquad D_t^{trade}D_u>0.
\]
A finite product <=0 gives **OPPORTUNITY EXHAUSTED / NO TRADE**. Missing entry inputs remain unavailable rather than being assigned an observed exhaustion. Never reset the target at the entry open.

Thus a valid entry requires
\[
\operatorname{sgn}(d_t^{model})=\operatorname{sgn}(D_t^{trade})
=\operatorname{sgn}(D_u),\qquad s=\operatorname{sgn}(D_u).
\]

## Approved remaining target and C4

With unique physical instruments and static-origin weights:
\[
L_u=\sum_k |w_{k,t}|O_{k,u}/P_{k,t},\quad
n_k=\frac{sKw_{k,t}}{P_{k,t}L_u},\quad
G_u^{target}=|D_u|/L_u.
\]
Intended K is fixed before order submission; full remaining target displacement is neither expected capture nor a realized-payoff bound.

\[
\Delta B_u^{trade}(q)=\sum_k w_{k,t}\frac{P_{k,q}-O_{k,u}}{P_{k,t}},
\quad R^{trade}(q)=D_u-\Delta B_u^{trade}(q).
\]
Qualified entitlement/accounting transformations apply. Primary normal C4 target convergence is \(sR^{trade}(q)\le0\), subject to the separately frozen holding/risk/exceptional-exit contract. A trigger is not a guaranteed liquidation fill.

## Approved economic alignment and scope

F/P/N/A/X, pooled P1, the joint payoff/duration/exposure law and costs must use this same Target-B coordinate, actual H-C basket and intended K. Preserve \(\widehat m_u=\sum_r\widehat\pi_r\widehat G_r\) and E1 \(\widehat m_u>\widehat c_{RT,u}\), including E-A failed-attempt economics.

The [canonical S3 mathematical specification](../stages/G5/S3_CANONICAL_MATHEMATICAL_SPECIFICATION.md) consolidates the chain. The [single consolidated pre-development audit](../stages/G5/S3_PRE_DEVELOPMENT_BINDINGS_AUDIT.md) identifies remaining choices without selecting them.

Target A remains historical/unselected and cannot activate automatically. All previously inactive alternatives remain inactive. No actual funds, numerical parameters, data access, quantile estimation, exposure/tracking/capture/cost estimation, implementation, C04 repair, backtesting or PnL inspection is authorized. Frozen V1 and relationship estimators are unchanged.

This instruction authorizes one documentation/control publication to GitHub main, not continuing execution/publication authority. NEXT_ACTION remains NONE.

**S3 MATHEMATICAL ARCHITECTURE CLOSED / PRE-DEVELOPMENT BINDINGS REQUIRED**
