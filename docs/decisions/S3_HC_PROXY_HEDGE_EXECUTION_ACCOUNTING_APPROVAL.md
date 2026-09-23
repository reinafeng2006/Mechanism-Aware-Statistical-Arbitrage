# H-C proxy-hedged S3 and execution/accounting — researcher approval

Decision ID: S3-HC-PROXY-HEDGE-EXECUTION-ACCOUNTING-2026-09-23.
Status: APPROVED ARCHITECTURE AND ENUMERATED EXECUTION/ACCOUNTING BINDINGS; NO EXECUTION.
Authority: direct researcher decision “RESEARCHER DECISION — SELECT H-C PRACTICAL PROXY-HEDGED S3 ARCHITECTURE”.
Ancestry: [execution design checkpoint](../stages/G5/S3_HEDGE_BORROW_JOINT_EXECUTION_DESIGN_CHECKPOINT.md), [minimal capture/cost approval](S3_MINIMAL_SCENARIO_CAPTURE_COST_ARCHITECTURE_APPROVAL.md), [authority ledger](../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).

## 1. Selected estimand and hedge architecture

Select H-C — practical factor-neutral / proxy-hedged relative-value convergence as primary S3.

Frozen prospective claim: “Extreme pair-conditioned abnormality predicts subsequent convergence in a preregistered approximately factor-neutral tradable relative-value basket.”

This is a research hypothesis, not an empirical finding. It does not replace frozen V1 or any relationship estimator. Exact modeled-residual replication may be claimed only when its identity is separately demonstrated.

Preserve:
epsilon_model=y_j−beta*y_i−gamma_model' f−a0;
epsilon_trade=y_j−beta*y_i−h'H−a0;
xi=epsilon_model−epsilon_trade=h'H−gamma_model'f.

Tracking/replication error is explicit. No proxy, tolerance or feasibility verdict is selected.

Use one common declared proxy universe and one common hedge-construction rule across all six estimators. Candidate-specific signal coefficients may differ, but proxy universes/algorithms cannot be independently optimized by estimator. R0/R3 retain the (1,−beta) pair component; R1-M/R1-MI retain their model-implied market/industry exposure information in proxy-neutralization targets.

H-B exact replication is a diagnostic/benchmark architecture only, not a universal execution prerequisite. H-A pair-only remains documented and inactive as primary. Neither activates automatically because H-C evidence is unavailable or results unfavorable. Earlier exact-first/universal-replication proposals are superseded by this explicit decision; missing H-C qualification still blocks economic execution.

## 2. Capital and share normalization

For actual unique tradable instruments:
L_u=sum_k abs(w_k)*O_(k,u)/P_(k,t);
n_k=s*K*w_k/(P_(k,t)*L_u).

Intended gross capital K is fixed before order submission and is the common event denominator for G_r, c_RT, mhat and failed attempts. Actual deployed peak gross is diagnostic; portfolio NAV is the aggregate portfolio-return denominator.

The identity sum_k abs(n_k)*O_(k,u)=K holds at the declared marks. Different actual fills do not retroactively change intended K or submitted shares. All costs/execution deviations must reconcile under the eventually frozen reference/fill convention; do not silently renormalize failed attempts to their realized deployed gross.

## 3. Approved entry: partial fill -> deterministic abort/unwind

Economic exposure starts at the first actual fill. Admit an S3 episode only when the complete qualified basket exists.

At the frozen completion/failure condition, an incomplete basket latches abort. Cancel remaining orders; unwind all actual fills deterministically. Late fills join the unwind obligations. No completion chase after abort. “Unwind” is an obligation/process, not an assertion that immediate execution is possible.

Timing, timeouts, fill qualification and deterministic unwind ordering remain unresolved fields for the later consolidated execution contract. Basket-level all-or-none availability is not assumed or selected as the primary entry architecture.

## 4. E-A failed-attempt accounting

Select E-A. Failed partial entries are economically real strategy attempts despite no admitted S3 episode. Their market gains/losses, execution deviations, commissions/fees, borrow/funding, entitlements and unwind costs enter executable-strategy economics without double counting.

E[R_attempt]=p_admit*E[R|admitted]+(1−p_admit)*E[R|failed].

No outcome is calculated now. The eventual event schema must reconcile the entry branch with F/P/N/A/X and the pooled P1 count universe. E-A fixes inclusion, not an unrecorded change to count units, censoring, duplicate handling or a separately estimated admission model. No failed-entry loss may be excluded merely because no episode was admitted.

## 5. Approved exit precedence

1. Binding contractual/legal obligations.
2. Feasible risk reduction.
3. Preservation of hedge geometry.

Recall/buy-in/margin obligations can break the ideal hedge. No discretionary replacement trade or unspecified risk-reduction algorithm is authorized. Detailed exceptional-exit, partial-liquidation and persistent-obligation handling remains to be consolidated and frozen.

## 6. Preserved approvals and remaining scope

Approved model-based scale/alpha=0.05 reference-tail gate, pooled P1 capture architecture, joint duration/exposure, all-leg cost ledger and E1 remain. H-C does not automatically substitute a proxy-residual z-score or silently equate the model gap with an exact tradable target. The signal-to-proxy-target bridge remains an explicit tracking-contract dependency.

P3 and the finite-grid threshold fallback remain inactive. No probabilities, payoffs, durations, costs, tracking error, feasibility or numerical z0 are estimated.

Current authority permits persistence and [proxy-universe/tracking design comparison](../stages/G5/S3_PROXY_HEDGE_TRACKING_CONTRACT_DESIGN_CHECKPOINT.md). No data acquisition, implementation, backtest, PnL inspection, C04 repair or parameter estimation. NEXT_ACTION remains NONE after documentation closeout.

**S3 PROXY HEDGE + TRACKING CONTRACT / RESEARCHER DECISION REQUIRED**
