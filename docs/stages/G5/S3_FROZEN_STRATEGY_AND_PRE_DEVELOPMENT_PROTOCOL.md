# S3 frozen strategy and pre-development protocol

2026-09-30 · **S3 STRATEGY + PRE-DEVELOPMENT PROTOCOL FROZEN**

This is the single authoritative current S3 specification. The [final researcher decision](../../decisions/S3_FINAL_PROTOCOL_FREEZE.md) approves the consolidated structure and final 12-package numerical disposition, with the 0.5% T1 amendment and session-unit bootstrap amendment. Earlier checkpoints/audits remain historical evidence, not competing specifications. Frozen V1 and the six relationship estimators are unchanged.

**Design authority is not execution authority.** [NEXT_ACTION](../../../research/NEXT_ACTION.json) remains NONE. The sole proposed successor is the [bounded acquisition/development plan](S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md), NOT AUTHORIZED. No data, actual fund identities, estimates, costs, z0, implementation or economic results are produced by this freeze.

There are no further ordinary strategy-design or numerical-constant gates. Failure to satisfy a frozen requirement is a **FEASIBILITY / DATA AVAILABILITY RESULT**, not permission to change the requirement. A later technical release of qualified inputs, implementation, fitted outputs and fixed validation dates is not another strategy selection.

## 1. Claim, estimators and information set

The claim is: **Extreme pair-conditioned abnormality predicts subsequent convergence in a preregistered approximately factor-neutral tradable relative-value basket.** This is a hypothesis, not a demonstrated result. Model-space discovery is distinct from tradable-basket convergence. Exact model-residual replication is not universally claimed.

Use R0-D252, R0-C126, R0-L126, R1-M126, R1-MI126 and R3-252 under one common S3 architecture. Their approved prediction equations, native formation/update schedules and PIT eligibility remain unchanged. No R4, estimator winner, independently optimized second-stage system or new factor definition is introduced. For each approved pair equation write
\[
\varepsilon_t^{model}=y_{j,t}-\beta_ty_{i,t}-(\gamma_t^{model})'f_t-a_{0,t},
\quad d_t^{model}=-\varepsilon_t^{model}=\mu_{j|i,t}-y_{j,t}.
\]
R0/R3 have no explicit factor subtraction in this equation: gamma_model=0 is not a claim of actual factor neutrality. R3 uses its approved conditional pair coefficients. For R1,
\[
\mu_{j|i}=f_j+\alpha_u+\beta(y_i-f_i),\quad
f_k=a_k+b_kM+\delta_kI_k,
\]
so a0=alpha_u+a_j−beta a_i and the explicit factor term is
\[
(b_j-\beta b_i)M+\delta_jI_j-\beta\delta_iI_i.
\]
Omit industry terms for R1-M; combine identical industry coordinates for R1-MI. Research factors are not presumed tradable instruments.

Every input has event/effective, publication, receipt/available, computation and decision times, plus version and lineage. Availability is no earlier than publication and actual receipt. Never use revised future knowledge to change an earlier signal, target or admission. Preserve the original pair/model registry and native eligibility; no new universe from observed outcomes.

## 2. Model scale and discovery gate

At current origin t replay its residual basket over common qualified prior aligned observations:
\[
\varepsilon_{v;t}=y_{j,v}-\beta_ty_{i,v}-(\gamma_t^{model})'f_v-a_{0,t},
\quad
\sigma_t^{model}=1.4826\,\operatorname{median}_{v\in W_t}
|\varepsilon_{v;t}-\operatorname{median}_{r\in W_t}\varepsilon_{r;t}|.
\]
W_t contains H_sigma=126 qualified strictly-prior aligned observations, common across the six estimators; refresh daily before signal use. Zero/nonfinite/unsupported/insufficient scale gives SIGNAL UNAVAILABLE, never zero abnormality, a floor or a shortened-window rescue. Current-origin replay may understate genuine future prediction error because formation information overlaps coefficient fitting.

\[
z_t^{model}=d_t^{model}/\sigma_t^{model},\quad
z_0=\inf\{x:\sum_e\omega_e1(|z_e^{ref}|\le x)\ge .95\},
\quad |z_t^{model}|\ge z_0.
\]
Alpha=.05 is directly preregistered; the threshold is the weighted empirical inverse CDF of absolute model z. No Gaussian 1.96 substitution. Inclusive ties can admit more than exactly 5%. This is reference rarity/materiality, not a p-value, false-positive probability, convergence probability or profitability threshold.

The reference hierarchy is equal completed chronological blocks, equal qualified pairs within block, equal two ordered prediction directions, and equal five equation groups. R0-C/R0-L share one group's weight equally, avoiding duplicate-equation overcounting. Within a complete pair/block/direction/group cell use equal qualified dates; identical C/L observations together retain one group contribution. Weights sum to one. The predeclared population and missing cells remain visible; do not drop a missing required group then renormalize a more favorable population.

Reference support is governed by a dependence-aware 95% probability-precision requirement of ±.01 (one percentile point), not the old fixed counts/coverage/Kish screens. It concerns reference tail probability precision, not ±.01 in z units or a 5% false-positive guarantee. Quantile and support certification are future outputs. Insufficient support makes the cutoff unavailable; alpha and the reference population do not adapt.

H252 MAD and H126 SD are the only non-selecting scale robustness specifications. They cannot replace the primary scale. No alternative tail sensitivities, finite-grid fallback or occurrence/PnL-driven alpha selection is authorized.

## 3. Fund-share registry and common auxiliary exposures

Use one PIT common universe of CNY domestic exchange-traded, unleveraged, non-inverse ordinary fund shares with disclosed benchmark/mandate and physical equity holdings. No derivative, synthetic, foreign-hours or currency substitute. Market slot: broad domestic A-share equity mandate. Industry slots: exact PIT industry dimensions of the research factors. Cross-industry pairs require both slots; same-industry and duplicate physical coordinates are combined. A taxonomy crosswalk requires documentary one-to-one identity at that vintage, not empirical correlation.

Qualification requires official identifiers/share class, first tradable date, dead/merged/delisted lineage, official mandate, holdings disclosures due under the applicable disclosure contract, calendar, tick/lot/order/settlement rules, qualified required history/actions, broker/account access and current lawful executable quotes. Remove generic 93-day holdings age, 95% holdings purity, 252-session inception floor, 57-of-60 turnover and CNY20m screens. Required history follows the actual exposure/tracking windows; liquidity/quantity follows binding executable evidence. Missing required evidence is unavailable, not a relaxed screen.

At each semiannual development registry origin rank qualified candidates by earliest documented first tradable date, then immutable exchange/instrument/share-class ID. Take the first qualified candidate, keep it for the block. Later failure blocks affected new baskets, not selection of a runner-up. Lock IDs once for prospective validation. No historical PnL, tracking minimization inside the acceptance band or cheapest realized borrow ranking. No synthetic pre-inception backfill.

Use the common local basis: market, then distinct PIT industries of i and j in sorted ID order. Include cross-loadings unless a compatible approved model explicitly supplies a structural zero. Preserve compatible model-supplied stock loadings; fill only missing dimensions with daily unweighted constrained OLS on **one calendar year of strictly-prior aligned information**, ending before signal use:
\[
y_{k,v}-(B_{k,S}^{model})'f_{S,v}
=a_k+B_{k,U}'f_{U,v}+e_{k,v}.
\]
For R0/R3 S is empty; R1-M retains compatible market coefficients; R1-MI retains compatible supplied dimensions. Incompatible units/vintages cannot be relabeled compatible. Each proxy loading column uses the same history, basis and OLS rule. Intercepts are nuisance terms. No EWLS, ridge, factor dropping, 240-row or p+20 screen, or history extension to rescue support.

Require finite valid inputs, necessary nonzero variances, identification/full required rank, estimable uncertainty and scale-aware numerical certification. Numerical error bounds must respect units, conditioning, arithmetic precision and input accuracy. Do not hard-code condition<=10,000 or equality tolerance 1e-10. An uncertifiable rank, sign, equality or lawful exact-share claim is unavailable; numerical tolerance is not economic hedge slack.

## 4. H-C mapping and T1 qualification

\[
\gamma_t^{neut}=B_{j,t}-\beta_tB_{i,t},\quad
H=A_t'f+e,\quad A_th_t=\gamma_t^{neut}.
\]
Square nonsingular A: h=A^{-1}gamma_neut. Full-row-rank underdetermined A: h=A'(AA')^{-1}gamma_neut. Retain the deterministic minimum-norm rule; no M2 mismatch optimization.
\[
w_t=(1,-\beta_t,-h_t'),\quad
\varepsilon_t^{trade}=y_{j,t}-\beta_ty_{i,t}-h_t'H_t-a_{0,t}.
\]
Combine duplicate physical instruments before any gross normalization. Exact declared exposure matching or required qualified industry proxy unavailable => HEDGE UNAVAILABLE. Physical constituents, market-only substitution, H-A, H-B execution and tolerance relaxation are inactive. H-B remains diagnostic only.

\[
\xi_t=\varepsilon_t^{model}-\varepsilon_t^{trade}
=h_t'H_t-(\gamma_t^{model})'f_t,
\quad \ell_t=\gamma_t^{neut}-A_th_t,
\quad \tau_{v;t}=h_t'H_v-(\gamma_t^{neut})'f_v.
\]
Thus xi=(gamma_neut−gamma_model)'f+tau: intentional model-to-trade estimand difference is distinct from unwanted implementation tracking. Universally small xi is not required.

Use the same strictly-prior one-calendar-year history as auxiliary OLS. Set g_t=sum_k|w_k,t| after physical aggregation. Define x_v=tau_v;t/g_t and cash-flow-consistent static-holding discrepancy
\[
J_{a,h;t}=\{h_t'C_H(a,h)-(\gamma_t^{neut})'C_f(a,h)\}/g_t.
\]
C_H and C_f require qualified buy-and-hold accumulation with cash distributions retained as cash, not reinvested, and consistent factor reconstruction. A sum of daily rebalanced tau is not a substitute. Missing accumulation lineage means unavailable.

**Primary T1 budget: max |J_H|<=0.005, H=20 common scheduled sessions**, per unit signal-origin gross. Use complete non-overlapping H-session paths anchored backward from the prior-history endpoint; their number and leftover sessions derive from the fixed annual calendar/history, not a hard-coded six-block rule. Retain all qualified required path evidence and report missingness; no compressed-date or earlier-year rescue. This is at most 0.5% measured qualified holding-period discrepancy, an explicit ex-ante hedge-quality/risk budget, not a statistical confidence bound, optimum, profitability threshold or future guarantee. No outcome-based relaxation.

Residual exposure ell, signed mean, RMS, daily max/tail, all overlapping holding paths, drift, target-relative tracking and available descriptive uncertainty are diagnostics, not additional hard acceptance gates. Exact M1 remains mathematically required. Remove former .02 residual, 2bp mean, 10bp RMS, 50bp daily-max and .05 drift acceptance cutoffs; .01 holding discrepancy is not the primary threshold. Daily monitoring cannot rebalance holdings or retarget using future tau. Loss of actual hard qualification invokes exceptional handling; a diagnostic drift change alone is not a new gate.

## 5. Target B, entry reference, shares and capital

At signal close compute only with then-available qualified information:
\[
D_t^{trade}=d_t^{model}+\xi_t,\qquad d_t^{model}D_t^{trade}>0.
\]
Failure gives TARGET-MAPPING UNAVAILABLE / NO TRADE; do not reverse or substitute Target A. Future realized tau cannot change origin target, admission or orientation.

Use the **first qualified synchronized post-open snapshot** at the next compatible common continuous session. O_k,u is its observed two-sided midpoint, not an assumed auction fill. All legs require compatible opening/closing calendars. Quote age/skew, computation/dispatch validity, acknowledgement deadline and lawful retry timing derive from verified feed/exchange/broker contracts. No generic 60–120 seconds, one second or five seconds defaults. Missing certified timing bounds means unavailable. Do not refresh snapshots to hunt a passing signal.
\[
\Delta B_{ON}^{trade}=\sum_kw_{k,t}(O_{k,u}/P_{k,t}-1),\quad
D_u=D_t^{trade}-\Delta B_{ON}^{trade}.
\]
Require D_t_trade D_u>0, else OPPORTUNITY EXHAUSTED / NO TRADE. Never reset at the open. All signs agree; s=sgn(D_u).
\[
L_u=\sum_k|w_{k,t}|O_{k,u}/P_{k,t},\quad
n_k=\frac{sK w_{k,t}}{P_{k,t}L_u},\quad
\sum_k|n_k|O_{k,u}=K,\quad G_u^{target}=|D_u|/L_u.
\]
Use actual tradable unadjusted price coordinates with qualified entitlement transformations. G_target is full remaining target displacement, not expected capture or a realized-payoff bound.

Raw intended gross is .01 of the declared book's prior qualified NAV. Remove forced equal one-sixth sleeves and CNY1m starting capital: capital/account allocation is a declared resource input, not fabricated evidence or a performance reallocation. Six estimator records cannot each spend the same capital six times. Actual shared commitments must reconcile to portfolio NAV.

Within a book permit one pending/admitted attempt per unordered pair. Opposing same-window directions conflict => no trade; repeated signals do not reset. Batch proposals and take the largest common rho in [0,1] such that K_e=rho K_raw,e respects total gross<=100% book/portfolio NAV, physical-security gross<=10% book/portfolio NAV, and actual borrow/collateral/funding/liquidity constraints. Gross is before cross-basket netting; outstanding orders, positions, aborts and encumbered resources remain recorded. Cash principal and gross position exposure are distinct constraints, not duplicate cost charges. Net currency exposure is diagnostic; remove the generic 10% net, .1% ADV and 10% depth caps.

Reserve legally required purchase cash, fees, collateral, carry and liquidation liabilities under actual contracts. Restricted short proceeds are not free capital. No contractual liability cap/evidence => unavailable, not an invented multiplier. Apply E1 once at resulting K with nonlinear costs recomputed; discard failed E1/lot candidates without redistribution or size search. Exact lot-compatible shares are required; no hedge rounding rescue. Intended K freezes before submission and remains the denominator even for zero/partial fill. Peak deployed gross is diagnostic; portfolio NAV is the aggregate-return denominator.

## 6. Borrow, entry, holding and joint exit

Every actual short physical leg requires binding account-specific borrowability/locate, receipt and validity times, committed remaining quantity/reservation, rates/reset/day-count/minima, collateral/margin/restricted proceeds, recall/buy-in deadlines and costs, manufactured distributions, account eligibility and lawful short-sale/order/settlement restrictions. Indicative availability is not a commitment. Long eligibility does not imply short availability. Unknown legal route => BORROW UNAVAILABLE; missing cost evidence => ECONOMIC GATE UNAVAILABLE. Both can apply while the scientific signal remains valid.

Entry states:
PREPARED -> RESERVED -> SUBMITTED -> EXPOSED/ENTRY_PENDING -> ADMITTED, or ABORT_LATCHED -> UNWIND_PENDING -> SETTLEMENT_PENDING -> CLOSED.
Release a batch of lawful IOC marketable limits at snapshot best ask for buys/bid for sells, rounded only to a lawful non-more-aggressive tick. No entry repricing, retry or assumed all-or-none facility. Missing IOC/equivalent immediate-cancel semantics means unavailable. Economic exposure begins at first fill; admission requires confirmed exact complete basket and valid reservations before abort.

Explicit rejection, canceled/unfilled IOC remainder, revocation, resource/qualification failure, dispatch overrun or contractual completion timeout immediately latches abort. Cancel remaining orders; all actual and late fills must unwind. A later complete basket does not undo abort. No completion chase. Reconcile IDs and out-of-order acknowledgements; unknown quantity cannot authorize exposure-increasing/reversing orders.

Static-origin shares remain fixed except entitlement-preserving transformations, mandatory contractual actions and liquidation. Monitor qualified common close marks. Entry session is session 1 of **20 common scheduled sessions**; missing quotes/suspensions do not pause the counter.
\[
\Delta B_u^{trade}(q)=\sum_kw_{k,t}(P_{k,q}-O_{k,u})/P_{k,t},\quad
R^{trade}(q)=D_u-\Delta B_u^{trade}(q).
\]
P in this movement is the qualified original-share value coordinate including attributable cash/claims once. First close with sR<=0 triggers C4. Target/cap close launches liquidation at the next lawful joint opening window, not a fictional target-price fill. No synthetic intraday target hit.

Normal states: NORMAL_HOLD -> NORMAL_EXIT_TRIGGERED -> LIQUIDATING -> SETTLEMENT_PENDING -> CLOSED. Any exception before closure latches X, never later relabeled F. Precedence: binding legal/contractual obligations; feasible risk reduction; hedge geometry. At equal priority use earliest legal deadline, receipt time and instrument ID. Liquidation sends legally reducible legs by earliest deadline, then largest current gross, then ID, using fresh lawful best-quote IOC and contract-derived retry timing. No discretionary replacement or optimization.

Recall/buy-in covers required inventory and starts joint liquidation; actual forced terms remain recorded. Margin/capital breaches cancel new entries and use committed resources/required liquidation; portfolio-wide liquidation orders earliest obligation, largest gross basket, then attempt ID. Suspension/calendar mismatch/blocked leg: liquidate feasible legs, retain blocked obligations until lawful release. Partial exit or contractual timeout latches X; late fills join outstanding obligations. A qualified split transforms shares/prices preserving value; signed distributions and short manufactured payments are booked once. Unknown/elective actions invoke X/pending; no voluntary replacement/reinvestment. Missing material valuation means NAV/return unavailable, never stale-price zero.

Holding cap does not erase settlement, recalls, carry or entitlements. Financial closure requires flat actual quantities, returned loans and reconciled cash/receivables/payables. Legal same-day resale restrictions can prevent instant unwind; immediate abort means immediate cancellation and earliest-lawful liquidation obligations, not assumed instant flatness.

## 7. States, capture, unique costs and E1

For mature qualified attempts define b(q)=s DeltaB_u_trade(q)/|D_u| and eta=.10. Apply priority:
- X: failed entry or exceptional trigger before financial closure; subtypes X_entry, X_hold, X_exit.
- F: admitted, no X, first target hit by cap; target/cap tie is F.
- P: no X/hit, .10<b(cap)<1.
- N: no X/hit, |b(cap)|<=.10.
- A: no X/hit, b(cap)<−.10.

Pending/censored/unobservable is a separate data status, never an invented sixth payoff or zero. Submitted no-fill attempts are X_entry even if known costs are zero; pre-submission rejection is coverage, not an attempt.

Use one pooled prior-event P1 model across six estimators/signs:
\[
\widehat\pi_r=N_r/N,\quad
\widehat G_r=N_r^{-1}\sum_{e:R_e=r}G_e,\quad
\widehat m=\sum_r\widehat\pi_r\widehat G_r.
\]
Use raw arithmetic payoff per K; do not rescale it by each new event's target. Preserve joint (R,G,T,inventory/exposure path); no unconditional-duration shortcut, flexible state conditioning, smoothing, shrinkage, trimming or independent estimator optimization. Exact C/L duplicates count once with both identities, C representative. Other correlated records remain dependent observations. Reference-tail balancing is not a new weighting of this raw economic pool.

The pre-E1 shadow opportunity ledger includes all otherwise qualified opportunities under this fixed resource/execution policy, not only profitable/admitted examples. Actual versus qualified reconstructed paths are distinctly marked; never duplicate both for one event or assume daily bars establish fills/borrow. No observation of a required state cannot silently establish its probability/payoff as zero. Unsupported states/paths or unresolved members of the fixed eligible cohort make affected forecasts unavailable.

Maturity uses actual input/outcome/settlement availability and purges information paths crossing fit cutoffs. No generic 60-session cohort or 20-session embargo, no dropping slow failures to obtain support. Support must certify a dependence-aware **95% joint net-mean precision halfwidth<=.0005 (5bp per K)** for the relevant P1 economic estimate, with state/path/cost identifiability. Replace fixed 500/50/20 and 200-order floors, not missing-evidence requirements. No concentration ceilings as selection; report concentration. This precision condition is not an economic safety buffer, lower-confidence-bound admission rule or positivity test.

\[
\widehat c_{RT}=c_{entry}+E[c_{exit}]+E[c_{borrow}]
+E[c_{funding}]+E[c_{other}],\qquad \widehat m>\widehat c_{RT}.
\]
Costs, G, duration, size, liquidation, feasibility and denominator must coincide. Missing required evidence => ECONOMIC GATE UNAVAILABLE, not zero. Qualified mhat<=chat => rejected. No delta, cost multiple, P3 or performance buffer.

For signed fill quantity q_l (buy positive), actual price p_l and pre-order benchmark m_l:
\[
G_e=(-\sum_lq_lm_l+D_e)/K_e,\quad
C_{exec,e}=\sum_lq_l(p_l-m_l)/K_e,
\]
\[
R_e^{net}=G_e-C_{exec,e}-C_{fees,e}-C_{borrow,e}-C_{funding,e}-C_{other,e}.
\]
Entry benchmark is original O; liquidation uses its own fresh pre-order midpoint; late fills retain parent benchmark. D contains each signed entitlement/qualified terminal claim once. Do not charge spread/slippage/impact twice, or manufactured distributions both in G and costs. Collateral principal is not expense; only actual financing/service charges are costs.

Use binding dated broker/official fees, taxes and minima; borrow integrates contractual rate times borrowed-value base over actual calendar duration; funding uses actual legally available debit/credit ledger, not an automatic gross-notional charge. Other costs must be enumerated unique contractual charges. Remove the proposed two-coefficient square-root impact model and arbitrary order-support defaults. Execution deviation needs qualified direct execution/reconstruction evidence; do not invent a replacement cost function or extrapolate outside identified instrument/side/size support.

Evaluate qualified joint paths against current actual basket/K/known contracts using common leg-role inventory fractions, price multipliers and liquidity states, retaining admission, duration and liquidation dependence. Missing required role cannot be guessed/dropped. This cost-path transferability assumption must be qualified and reported; it does not authorize target-scaled G. If direct evidence cannot identify required costs, stop affected economics.

E-A includes all attempted-entry market gain/loss, deviations, fees, borrow/funding, entitlements and unwind:
\[
E[R_{attempt}]=p_{admit}E[R|admitted]+(1-p_{admit})E[R|failed].
\]
Admission frequency is a diagnostic of the same pool, not a new conditional forecasting model.

## 8. Single chronological development specification

Permitted future historical scope is **2015-01-01 through 2019-12-31 only**, contingent on separate authorization. 2015 warms inputs, 2016 forms reference/history, six half-year forward blocks span 2017–2019; one final fit at 2019 end uses only then-mature information. No earlier warm-up extension or 2020 label completion.

At each scheduled origin freeze registry/reference/P1/cost components using strictly earlier qualified completed records; process forward chronologically; labels can enter only a later scheduled fit after information maturity/purging. First blocks may supply supported shadow events without supported P1/E1; no economic admission until every gate passes. Never backfill an earlier threshold or seed from retrospectively favorable outcomes.

Budget: one economic specification, six forward blocks plus one final production fit (at most seven scheduled fits of learned components), with approved deterministic daily native/auxiliary/scale refresh. Only H252 MAD and H126 SD receive diagnostic-only scale replay, not secondary economic portfolios. Zero parameter/hedge/threshold/cap/sizing grids; no failed-support rescue.

Mechanical outputs include proxy registry, exposures/A/h, tracking qualification, contract schedules, z0, raw P1 frequencies/state means/joint paths and qualified direct execution-cost evidence. Development-derived outputs under fixed rules include dependence/support/precision certification and validation power/horizon, not profit-maximizing constants.

Permitted later research reports, only if separately authorized: support/coverage, censoring, concentration, accounting reconciliation, Brier score, signed payoff prediction error/MAE, duration and execution-component error, and fixed-rule precision/power qualification. Such event G/cost/duration work is economic-outcome access even without a portfolio PnL chart. No Sharpe/PnL ranking, winner selection or repeated fitting for favorable support. Unresolved 2019 obligations remain pending, without 2020 access.

## 9. Prospective validation, technical release and inference

Historical 2020–2025 are non-pristine; do not relabel other already seen data pristine. T_freeze is the later immutable protocol/input/code/model-output release following authorized development, qualification and conformance checks. It locks actual proxy IDs, fitted parameters/z0, contracts, capital/account basis, full calendar, inference details, hashes and seed before any validation observations. The current design freeze is not that release and grants no future data access or live orders.

Plan for a **10bp (.001/K) minimum material mean all-attempt net effect**, **80% power**, conservative planning level .05/5. Using development variance/dependence/occurrence, not estimated profitability, mechanically choose the shortest qualifying **1-, 2-, or 3-calendar-year** horizon. If none qualifies, record inadequate design feasibility; no horizon expansion. Fix the complete scheduled-session sample before validation. Begin the first full common scheduled session strictly after T_freeze; no partial already-observed session. No optional stopping, count-driven extension or arbitrary 504/252-session defaults.

Stop new attempts at fixed horizon end; settlement follow-up is derived before validation from qualified contractual obligations, not a generic 60-session extension. Unresolved attempts remain censored/unavailable. Continuing legal obligations do not expand the scientific sample. No successful-attempt-only inference. Actual versus prospective qualified shadow execution must be explicitly labeled/authorized; neither substitutes for the other.

Primary estimand: mean all-attempt net return/K for each of five equation groups; report six model books/signs but link C/L, exact duplicates once and equal influence if distinct C/L realizations exist. Single final one-sided positive-mean family versus <=0, five-group Holm at .05. Not-testable slots remain in the five-slot family and cannot become discoveries.

Paired calendar moving-block bootstrap retains all cross-sectional linked attempts at common origin dates and resamples the same blocks across groups. Recompute attempt-weighted means using actual resampled counts; center returns for null samples:
\[
b=\max(H,L_{\mathrm{information}},\lceil n^{1/3}\rceil),
\quad H=20,
\]
**n is the number of common scheduled validation sessions in the fixed validation sample.** It is never attempt/pair/security/raw-row count. L_information is the qualified longest development event-information span, measured in common scheduled sessions, locked before validation. Every term has session units. Missing observations do not shrink the scheduled n.

Freeze **50,000 replicates** and deterministic **protocol-hash-derived seed**, with the hash/seed conversion and random-generator implementation recorded in the technical release before validation. For the null statistic:
\[
p=(1+\#\{T^*\ge T_{obs}\})/50001.
\]
Apply the five-group Holm family at .05; 95% descriptive intervals do not create new tests. No fixed standalone 20-block default or old 10,000-replicate/20260927 seed. If b/data do not support defensible resampling, report inference unavailable; do not truncate memory or change units to force a result. Weak-dependence assumptions/precision limitations remain explicit, not guaranteed by the formula.

Keep validation labels sealed from model updating. Allowed updates are only prescribed PIT relationship/scale/exposure refresh, actual quotes/contract changes, NAV/reservations, entitlements and mandatory exits. Freeze learned P1/cost/reference components, hedge identities, semantics and statistical rules. Structural failure pauses new entries without restarting the clock or discarding its prefix. Positive returns alone do not identify incremental model-extremeness predictive value relative to an unregistered control strategy.

## 10. Complete numerical disposition and failure semantics

The [final decision](../../decisions/S3_FINAL_PROTOCOL_FREEZE.md) maps all 86 audit IDs exactly once to the six approved disposition classes. Classification applies to each control's final replacement rule, not preservation of obsolete literals. In particular, reporting classification of H09 limits confirmatory interpretation; it does not unfreeze the approved five-group Holm family.

Actual provider/account terms, registry IDs, numerical z0 and all estimates remain unproduced. Numerical certification and dependence/precision procedures must be documented before their authorized calculations; they may demonstrate conformance or unavailability, not invent policy relaxation. This protocol does not assert that historical evidence, exact lots, all-state support, power or reliable inference will exist.

Signal -> model z gate -> qualified proxy hedge -> Target B/sign persistence -> economic gate -> partial-fill execution -> C4/exceptional joint exit -> all-attempt accounting -> bounded development -> separately authorized prospective validation is now fixed. No further ordinary strategy-design gates are authorized. Missing evidence, unidentified quantities or inability to certify requirements yields **FEASIBILITY / DATA AVAILABILITY RESULT**, retaining specific unavailable flags and no fallback.

**S3 PROTOCOL FROZEN / DATA ACQUISITION + DEVELOPMENT AUTHORIZATION REQUIRED**
