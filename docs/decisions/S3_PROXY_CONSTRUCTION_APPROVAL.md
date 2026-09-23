# S3 proxy construction — researcher approval

Decision ID: S3-PROXY-CONSTRUCTION-2026-09-23.
Status: APPROVED CONSTRUCTION / TARGET BRIDGE UNRESOLVED / NO ESTIMATION.
Authority: direct researcher instruction “RESEARCHER DECISION — APPROVE S3 PROXY-HEDGE CONSTRUCTION; TARGET BRIDGE REMAINS UNRESOLVED”.
Ancestry: [H-C approval](S3_HC_PROXY_HEDGE_EXECUTION_ACCOUNTING_APPROVAL.md), [proxy/tracking checkpoint](../stages/G5/S3_PROXY_HEDGE_TRACKING_CONTRACT_DESIGN_CHECKPOINT.md), [authority ledger](../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).

## 1. Approved proxy and exposure architecture

Select Package 1: fund-share proxies. Use one preregistered common universe of qualified tradable market fund-share slot(s) and industry fund-share slots across all six estimators. Actual funds remain UNSELECTED.

Physical constituent replication remains documented but INACTIVE. Qualification failure or unfavorable outcomes do not activate it.

Preserve gamma_neut,c,t=B_j,c,t−beta_c,t*B_i,c,t. Preserve compatible model-supplied coefficients. Fill missing exposure dimensions only through one common auxiliary exposure rule across six estimators. Its unspecified estimation form/history/refresh details remain unbound; no coefficients or numerical parameters are selected/estimated.

## 2. Approved M1 mapping and actual instrument basket

Require A_t*h_c,t=gamma_neut,c,t.

For square nonsingular A: h=A^(-1)*gamma_neut.
For full-row-rank underdetermined A: h=A'*(A*A')^(-1)*gamma_neut, the deterministic minimum-norm solution.

No M2 bounded-mismatch fallback. If exact declared exposure matching is mathematically or qualification infeasible: HEDGE UNAVAILABLE. Rank/conditioning/gross qualification criteria that are not uniquely specified remain pre-access bindings; no numerical tolerance or regularizer is invented. A feasible coefficient identity does not establish exact return replication.

Freeze w_c,t=(1,−beta_c,t,−h_c,t') on actual tradable instruments. Combine duplicate physical instrument coordinates before normalization. Fund shares and their underlying securities are not identical physical instruments.

## 3. Approved static-origin shares

L_u=sum_k abs(w_k,t)*O_k,u/P_k,t;
n_k=s*K*w_k,t/(P_k,t*L_u).

Preserve shares through the episode except qualified entitlement-preserving transformations, already-authorized exceptional contractual actions and liquidation. Do not rebalance because prices/exposures drift. Rebalanced architecture is INACTIVE.

Intended K remains fixed before submission and the common event denominator. Actual-fill deviations do not retroactively change K or submitted positions. Direction s and the origin convergence target must be consistent with the still-unresolved target bridge; approving this share formula does not select Target A or B.

## 4. Approved tracking notation and T1 architecture

xi=epsilon_model−epsilon_trade=h'H−gamma_model'f is TOTAL model-to-trade difference.

ell=gamma_neut−A*h is residual target exposure.
tau=h'H−gamma_neut'f is unwanted implementation/proxy tracking.

Preserve xi=(gamma_neut−gamma_model)'f+tau. Do not require universally small xi: intentional neutralization can create a model-to-trade difference.

Select T1 absolute exposure/implementation-tracking qualification. Primary diagnostics: ell; signed mean tau; RMS tau; tail/max path discrepancy; cash-flow-consistent holding-period discrepancy; exposure drift.

Numerical tolerances, history, confidence levels and minimum support remain UNSELECTED. Model/exposure identities do not eliminate estimation uncertainty or holding-period drift. T2 target-relative acceptance remains INACTIVE; target-relative reporting is diagnostic only.

## 5. Strict missing-industry qualification

A required qualified industry proxy unavailable => HEDGE UNAVAILABLE.

No automatic market-only substitution, H-A, H-B, physical constituent fallback or tolerance relaxation. H-B remains diagnostic/benchmark only, not a required executable primary. No benchmark computations authorized.

## 6. Target bridge explicitly not approved

Compare only:
- Target A: retain d_model as the hypothesized displacement the proxy basket should capture.
- Target B: use the origin displacement in the actual approved H-C basket coordinate.

Both must be derived from d_trade=d_model+xi. No convergence target, orientation amendment, C4 target rule or payoff-label bridge is selected by this construction decision. The already-approved model-based z-gate remains abs(z_model)>=Q^w_0.95(abs(z_ref)); numerical z0 is uncomputed. No trade-residual restandardization or threshold change is authorized.

The [target-bridge checkpoint](../stages/G5/S3_CONVERGENCE_TARGET_BRIDGE_DESIGN_CHECKPOINT.md) records equations and consequences as proposals.

## 7. Scope

Earlier approved pooled P1/E1, joint duration/exposure, all-leg cost ledger, E-A, deterministic abort/unwind, intended K and obligation-first exits remain. Actual funds, auxiliary exposure specification, T1 values, target bridge and detailed timing/exception mechanics require further binding.

No proxy/borrow data acquisition, exposure/tracking/tolerance/capture/cost estimation, numerical z0, implementation, backtest or PnL inspection. Frozen V1 and relationship estimators unchanged. Current authority permits only documentation persistence and target-bridge design comparison. NEXT_ACTION remains NONE after closeout.

**S3 CONVERGENCE TARGET BRIDGE / RESEARCHER DECISION REQUIRED**
