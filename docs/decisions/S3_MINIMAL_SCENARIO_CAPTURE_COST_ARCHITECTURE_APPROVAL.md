# Minimal S3 scenario capture/cost architecture — researcher approval

Decision ID: S3-MINIMAL-SCENARIO-CAPTURE-COST-2026-09-22.
Status: APPROVED ARCHITECTURE / NO ESTIMATION AUTHORIZED.
Authority: direct researcher instruction “RESEARCHER DECISION — APPROVE MINIMAL S3 SCENARIO CAPTURE/COST ARCHITECTURE”.
Ancestry: [scenario direction](S3_CAPTURE_COST_SCENARIO_DIRECTION_SELECTION.md), [detailed checkpoint](../stages/G5/S3_CAPTURE_COST_SCENARIO_MODEL_DESIGN_CHECKPOINT.md), [authority ledger](../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).

## 1. Approved states and prospective boundaries

Freeze R in {F,P,N,A,X}. F renames the checkpoint's H (target hit); this is a label change only.

Preserve the prospective classifier, with b(q)=s*Delta B_u(q)/abs(d_u), the first qualified target close theta_F, and the cap close theta_cap. X has priority for a forced/exceptional exit under the eventually frozen execution contract, including after a target trigger but before completed liquidation. Ordinary planned next-event exit is not itself exceptional.

For qualified fully observed paths not assigned X:
- F: theta_F<=theta_cap, including a tie.
- P: no target hit by cap and eta<b(theta_cap)<1.
- N: no target hit by cap and abs(b(theta_cap))<=eta.
- A: no target hit by cap and b(theta_cap)<−eta.

Eta remains UNSELECTED within its proposed domain 0<=eta<1. The holding cap, precise executable clock, X criterion, simultaneous-event precedence and censoring details remain unresolved until the execution contract is frozen. Record numerical boundaries in the future bounded development specification before access; do not invent or estimate them now. No unknown path is automatically N, A, X or zero payoff.

The target-monitoring state and actual executable liquidation payoff remain distinct. F can have overshoot or subsequent loss; no state-name guarantee overrides actual qualified cash flows.

## 2. Approved capture and pooled P1 architecture

G_u^target=abs(d_u)/L_u is full target displacement only: neither expected capture nor a hard bound on realized payoff.

mhat_u=sum_(r in {F,P,N,A,X}) pihat_r*Ghat_r.

The first primary model uses pooled chronologically prior qualified events:
pihat_r=N_r/N;
Ghat_r=(sum_(eta:R_eta=r) G_eta)/N_r.

These are pooled signed gross economic payoffs per a consistent initial gross-capital denominator and policy. This records the researcher's literal arithmetic-mean baseline, without introducing event-level conditioning. A normalized representation is permitted only when its definition and back-transformation preserve the approved estimand; simply multiplying a pooled historical ratio by a new event's g_u is not generally algebraically equal to the pooled raw-payoff mean and cannot be silently substituted.

When each required state mean is supported, the displayed baseline implies mhat=sum_eta G_eta/N. Scenario decomposition still exposes state-specific gains, losses and duration/cost dependence. It does not manufacture event-specific gross predictability: within a fixed pool/update, the raw pooled mhat is common, although basket costs and feasibility can differ.

No flexible functions of z, regime, volatility, estimator identity or other state variables; no six independently tuned second-stage models. Event-level conditioning is a future extension requiring a separately authorized design action, not automatic response to inadequate fit.

## 3. Pooling and support

One common primary capture architecture applies across all six estimators. Preserve estimator and signed-direction identities for diagnostics; no independently optimized state definitions, probabilities or payoff mappings.

The event unit, comparability universe, duplicate C/L handling for economic event counts, dependence/overlap treatment and any sparse-state pooling/shrinkage must be specified before development access. The already-approved reference-tail weighting is not automatically a weight system for these arithmetic economic-event counts. No weighted, estimator-conditioned or sign-conditioned replacement is silently adopted.

Sparse or unobserved required states do not establish zero risk. No pseudocount, smoothing strength, minimum support number or shrinkage estimator is approved now; unsupported required components mean the economic gate is unavailable until a separately approved specification exists.

## 4. Approved joint duration and non-overlapping costs

Preserve the scenario-conditional joint treatment of (R,G,T,exposure path). Duration remains unestimated. Costs must use the same duration/exposure law, not an inconsistent unconditional constant.

chat_RT,u=centry,u+E[cexit,u]+E[cborrow,u]+E[cfunding,u]+E[cother,u].

Approve the checkpoint's single non-overlapping all-leg ledger and anti-double-counting rules. Execution deviations already embedded in fills cannot also be charged as spread/slippage/impact. Signed distributions/manufactured payments are accounted once; collateral principal is not an expense; short-sale proceeds are not automatically free funding.

Capture and cost must refer to the same exact eventual basket, size, gross-capital denominator, duration assumptions, liquidation policy and execution feasibility. The exact reference/fill convention and instruments remain execution-contract dependencies.

Missing required cost evidence => ECONOMIC GATE UNAVAILABLE, never zero cost.

## 5. Approved economic rule and inactive alternatives

Select E1: mhat_u>chat_RT,u.

No delta safety margin, lambda_c cost multiple or performance-calibrated buffer is introduced. The z-gate retains statistical/material abnormality; E1 addresses expected economic value only.

P3 conservative joint bounds remain documented but INACTIVE. Any activation needs a separate pre-access researcher decision; sparse P1 support or unfavorable results do not activate it. P2 conditional modeling and direct conditional gross-payoff forecasting remain unselected future alternatives. The separate finite-grid threshold fallback is also inactive.

## 6. Remaining authority boundary

No probabilities, payoffs, durations, costs, numerical z0 or unresolved scenario boundaries are estimated. No historical data or borrow/market data acquisition, implementation, C04 repair, backtest or PnL inspection is authorized.

The exact hedge/borrow/joint-execution contract must be designed first. This instruction authorizes persistence and [design-only execution-contract work](../stages/G5/S3_HEDGE_BORROW_JOINT_EXECUTION_DESIGN_CHECKPOINT.md), not adoption of any proposed instruments or detailed execution rule. Future development requires its own bounded authorization after prerequisite contracts are frozen.

Scale and alpha=0.05 empirical reference-tail binding remain unchanged; numerical z0 is uncomputed; frozen V1 and exposure history are preserved. NEXT_ACTION remains NONE after documentation closeout.

**S3 HEDGE + BORROW + JOINT EXECUTION DESIGN / RESEARCHER DECISION REQUIRED**
