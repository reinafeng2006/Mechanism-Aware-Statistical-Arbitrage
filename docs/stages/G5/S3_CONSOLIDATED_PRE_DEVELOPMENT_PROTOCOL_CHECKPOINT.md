> Status update 2026-09-30: [enumerated structural rules are approved](../../decisions/S3_PRE_DEVELOPMENT_STRUCTURAL_APPROVAL.md), while new numerical constants remain unbound. See the [numerical constants audit](S3_PRE_DEVELOPMENT_NUMERICAL_CONSTANTS_AUDIT.md). The original proposal body below is preserved; its “proposed in full” wording describes its publication date, not the latest partial approval. No blanket P0 or execution approval follows.

# S3 consolidated pre-development protocol — researcher decision package

2026-09-27 · **PROPOSED IN FULL — NOT APPROVED, NOT EXECUTION AUTHORITY**.
Architecture base: bf95f790dfb1d4a65173a819c375b7063aa58bd2.
Authority: researcher request “S3 PRE-DEVELOPMENT PROTOCOL — CONSOLIDATED DESIGN”.
Read the [closed mathematical architecture](S3_CANONICAL_MATHEMATICAL_SPECIFICATION.md), [bindings audit](S3_PRE_DEVELOPMENT_BINDINGS_AUDIT.md), [Target B approval](../../decisions/S3_TARGET_B_CONVERGENCE_APPROVAL.md) and [authority ledger](../../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).

This is ONE recommended package for one researcher decision. Every newly specified number, estimator, time, support rule and execution policy below is a **proposal**, including wording such as “require” or “freeze”. None becomes active by publication. No actual instruments/providers are selected and no data are accessed. The closed architecture and its approval files are not edited.

Package P0 uses fixed ex-ante operating/measurement budgets and mechanical estimation, with **zero outcome-selected calibration parameters and no fallback**. The numbers are transparent policy choices for approval, not measured feasibility, statistical guarantees or recommendations to trade. Failure of P0 produces explicit unavailability; it does not launch another specification. This is especially material for exact lot-compatible geometry, historical borrow/fill evidence and sparse exceptional states.

Classification used below: **F** = rule that can be frozen now; **M** = numerical output later mechanically estimated; **C** = outcome-driven development calibration (none proposed); **U** = feasibility/support failure can make an event or whole exercise unavailable. F as a rule class is distinct from outcome state F.

## 1. Proxy universe and common exposure construction [F/M/U]

### 1.1 Qualified fund-share slots, not named funds

Use CNY-denominated, domestically exchange-traded, unleveraged, non-inverse ordinary fund shares with disclosed benchmark/mandate and physical equity holdings. No derivative overlay, currency transformation, foreign-hours exposure or synthetic fund substitutes in P0. This is a proposed evidence test; it does not assert which instruments currently satisfy it.

A market slot requires a broad domestic A-share equity benchmark, not a sector/style/thematic mandate. An industry slot requires an index/mandate mapped to the exact PIT industry dimension used by the research factors. Cross-industry baskets require both industry slots; same-industry coordinates are combined. A taxonomy crosswalk is admissible only if issuer/index definitions establish a deterministic one-to-one coverage identity at that vintage. A merely correlated sector, many-to-many crosswalk or narrative similarity fails; no estimated taxonomy mapping.

At each scheduled registry origin, require:
- Immutable exchange/instrument/share-class identifiers, first tradable date, delisting/merger lineage, currency, tick/lot/settlement rules and official calendar.
- Official mandate plus latest published holdings no older than 93 calendar days. For an industry slot, at least 95% of disclosed equity value must belong to that exact mapped industry; remaining non-equity cash is documented. The permitted 5% equity leakage is explicit and is subject to T1, not exact research-factor replication.
- At least 252 scheduled prior common sessions since inception, exposure and T1 history below, and all required splits/distributions/reorganizations qualified.
- In the latest 60 scheduled sessions: at least 57 with qualified positive turnover, median daily traded value at least CNY 20 million, and no unqualified price/action intervals. This is a fixed liquidity eligibility screen; order-size/depth limits below remain additional.
- Executable two-sided quotes and correct order access at entry; no admission during halt, limit condition preventing the required side, pending unresolved identity/action event or incompatible session/settlement state.
- Instrument-specific broker support for the relevant account. Every actual short, including a proxy or a pair stock, separately passes section 6; a fund passing long eligibility is not presumed borrowable.

**Deterministic selection:** within each slot, rank qualified candidates by earliest documented first tradable date, then ascending immutable exchange/instrument/share-class ID. Choose the first; no ranking on S3 events, PnL, tracking goodness within the admissible band, recent performance or cheapest realized borrow. Select at each semiannual development block origin using information available before that origin. Keep that slot identity for the block; if it later fails qualification, reject new affected baskets rather than trying the next candidate. Existing positions retain their original instruments and follow exceptional exits. For prospective validation, select once at T_freeze and lock identities throughout the validation horizon.

A new fund is not backfilled with its benchmark or a predecessor. History gaps cannot be filled with later knowledge, adjusted index proxies, synthetic pre-inception returns or another fund. No qualified required slot => **HEDGE UNAVAILABLE**. Physical replication, market-only substitution and H-A/H-B/M2 fallback remain inactive. No actual ID is chosen by this document; later application of this frozen ranking would produce an auditable registry, not another strategy-selection contest.

### 1.2 One common missing-exposure rule

For every candidate c use the same declared local factor basis: market plus the distinct PIT industries of i and j, in that order with industry IDs sorted and identical dimensions combined. The factor definitions/units remain those of the approved relationship design. Estimate stock and proxy loadings against the entire local basis, including cross-loadings unless the compatible approved model explicitly supplies a structural zero. Intercepts are fitted nuisance terms, not neutralization coefficients.

For stock k partition dimensions into compatible model-supplied S and missing U. Preserve supplied B_k,S exactly at its approved relationship vintage; do not overwrite it with a more favorable auxiliary estimate. Estimate missing dimensions by:
\[
y_{k,v}-(B_{k,S}^{model})'f_{S,v}=a_k+B_{k,U}'f_{U,v}+e_{k,v}.
\]
For R0/R3, S is empty; gamma_model=0 is not an actual-exposure assertion. For R1-M retain compatible market loadings and estimate missing industry dimensions through this constrained regression; for R1-MI retain all compatible supplied dimensions, filling only genuine omissions. Incompatible timestamps, return definitions or factors do not count as “supplied”; if compatibility cannot be established, declare unavailable rather than relabeling an incompatible estimate.

Compare only unweighted OLS and exponentially weighted least squares with a fixed 63-session half-life on the same history. **Recommend unweighted OLS**: fewer effective-window choices, direct diagnostics and no decay parameter. EWLS is an unselected design alternative, not a second development fit or fallback.

Proposed common auxiliary OLS: latest 252 scheduled common sessions ending t−1; at least 240 fully qualified aligned rows, no use of earlier observations to repair a short window; at least p+20 rows for p fitted regressors including the intercept; daily refresh before the signal session. Use available-as-of records, not today's revised history. Each proxy column of A uses the same OLS form/history/basis. For model-supplied coefficients retain their existing native update schedule; document their age, do not refit the relationship model.

Require finite inputs/coefficients, positive predictor variances, full column rank of the standardized design and condition number <=10,000; reject rather than ridge, truncate singular vectors or drop a factor. Solve the already-approved M1 inverse/minimum-norm map; require full row rank of A and condition number <=10,000 on a unit-column-normalized A, with original economic units restored for solving. These are numerical qualification criteria, not a new hedge algorithm. Require normalized algebraic error <=10^-10:
\[
\|Ah-\gamma^{neut}\|_\infty/(1+\|\gamma^{neut}\|_\infty)\le10^{-10}.
\]
No near-rank or gross-leverage repair. Retain all physical duplicate aggregation before computing w and L.

## 2. T1 absolute tracking qualification [F/M/U]

Keep the meanings:
\[
\ell_t=\gamma_t^{neut}-A_th_t,\quad
\tau_{v;t}=h_t'H_v-(\gamma_t^{neut})'f_v,\quad
\xi_t=(\gamma_t^{neut}-\gamma_t^{model})'f_t+\tau_{t;t}.
\]
The semicolon denotes current-origin coefficients replayed on prior observations. Neither low ell nor low replay tracking proves out-of-sample neutrality. This fit-overlap limitation is reported alongside the already-approved model-scale limitation.

Use exactly the latest 126 scheduled common sessions ending t−1, all 126 qualified; no missing-date compression or earlier-date rescue. Put \(g_t=\sum_k|w_{k,t}|\), the signal-mark gross basket size after physical aggregation; g_t>0. Define \(x_v=\tau_{v;t}/g_t\). This is absolute tracking per unit signal gross, not tracking divided by the target and not a replacement for L_u. Define:
- Exposure residual: \(E_\ell=\|\ell_t\|_\infty/g_t\).
- Signed tracking mean \(\bar x=126^{-1}\sum_vx_v\).
- RMS \(R_x=(126^{-1}\sum_vx_v^2)^{1/2}\).
- Tail: empirical inverse-CDF Q_.95(|x|); maximum \(M_x=\max_v|x_v|\).
- Holding discrepancy for historical start a and h sessions:
\[
J_{a,h;t}=\{h_t'C_H(a,h)-(\gamma_t^{neut})'C_f(a,h)\}/g_t,
\]
where C_H and C_f are each component's qualified cash-flow-consistent buy-and-hold return from a, with cash distributions retained as cash (no assumed reinvestment), under the same origin convention. Research factors require an explicitly reconstructible corresponding accumulation; absent that lineage, this diagnostic/qualification is unavailable. It is not the sum of daily portfolio-rebalanced tau. Evaluate h=1,...,20 wherever complete; use six non-overlapping 20-session blocks, anchored backward from t−1, for primary 20-session support, with six sessions left over.
- Exposure drift: \(d_{v;t}=B_{j,v}-\beta_tB_{i,v}-A_vh_t\), using each historical v's strictly-prior qualified daily exposure fits; \(E_d=\max_v\|d_{v;t}\|_\infty/g_t\). Actual held-share dollar drift is separately reported at current prices using fixed n; no rebalancing is permitted.

**Proposed hard pre-entry budgets:** M1 numerical residual as above; E_ell<=0.02; |mean x|<=0.0002 (2 bp/day); RMS<=0.001 (10 bp/day); max |x|<=0.005 (50 bp/day); max over the six non-overlapping |J_20|<=0.01 (100 bp over 20 sessions); E_d<=0.05. All required histories, positive units and finite outputs must exist. Absolute signed-mean/RMS/maximum/holding/drift budgets must all pass. They are ex-ante administrative risk budgets, not estimated optimums, forecast intervals or guarantees.

**Reporting only:** signed mean, Q_.95, all overlapping J_h paths, signed bias, maximum dates, separate market/industry components, actual-share drift, 95% descriptive cluster intervals when support permits, and target-relative tracking ratios (T2 remains inactive). For descriptive uncertainty use 20-session non-overlapping blocks; with only six blocks, report their individual values and range, not a purported precise asymptotic confidence result. Current-origin replay versus genuinely PIT one-step innovations \(H_v-A_{v-1}'f_v\) is a fixed diagnostic, not a second acceptance rule or fitted hedge.

No tolerance search is proposed. These numbers require researcher approval now; none may be loosened because qualification is rare. Daily ongoing monitoring reports drift; a breached hard budget on an admitted basket is the deterministic qualification-loss exceptional trigger in section 8, not permission to rebalance or re-evaluate the original target using future tau.

## 3. Exact PIT event timeline and cash-flow coordinate [F/U]

All clock times below are **relative to the instrument's verified exchange session**, not claims about present exchange rules. Eligible baskets must share the same continuous-session opening time u and scheduled close. Different calendars/opens => no new attempt. All data carry event, publication, receipt/available and decision timestamps; use the latest of publication/receipt for availability.

1. **Relationship refresh:** retain candidate-native approved H/U and coefficient availability; no coefficient may use information later than the approved signal information set. Auxiliary exposures, A and T1 use data ending t−1 and must be available before signal evaluation.
2. **Signal close t:** consume qualified close/entitlement/factor/response observations only after actual publication/receipt. Compute approved current-origin MAD from strictly-prior observations, model d and model z. A cutoff/scale formed later cannot classify this event retrospectively.
3. **Proxy mapping and Target B:** use prequalified block registry and PIT coefficients plus signal-observed H_t,f_t for xi. Require d_model*D_t_trade>0. Freeze w, D_t_trade and transformation lineage. All signal computations must finish before u; otherwise skip that event.
4. **Entry-open precheck:** use the first synchronized executable quote snapshot at or after u+60 seconds, no later than u+120 seconds. Snapshot spread across leg timestamps <=1 second; each quote age <=1 second at receipt; both sides positive and noncrossed. O_k,u is the midpoint of that observed bid/ask snapshot. Thus “entry-open” means this declared post-open reference, not the unknowable auction fill or a fictional fill at the first print.
5. **D_u, sizing and economics:** subtract actual-basket signal-to-snapshot movement, test D_t_trade*D_u>0, compute L_u, preliminary allocations and E1 using parameters published before u and quotes/contracts available by the snapshot. Compute exact planned shares, reserve resources and recheck all guards. Submit within 1 second of the snapshot. If computation/reservation exceeds that age, skip; do not refresh to hunt a favorable sign/E1. The one snapshot and target stay fixed for that attempt.
6. **Orders and holding:** opening prices/fills occurring after submission never justify the earlier decision. First actual fill starts exposure; only a complete qualified basket admits an episode.
7. **C4:** use the first qualified synchronized end-of-session marks after admission; no synthetic intraday target hits. Monitor the fixed tradable coordinate through the cap. Trigger launches liquidation at the next joint continuous-session opening window defined above; contractual emergency processing is immediate subject to lawful tradability.
8. **Liquidation and accounting:** actual fill/settlement receipts may arrive later and belong to their real times. Never mark a target touch as a fill. Financial closure requires quantities, borrow and cash/entitlement obligations reconciled.

Prices for share construction are unadjusted executable currency prices with explicit origin multipliers and entitlement accounts. For a split by ratio a, transform n→a n and coordinate prices by 1/a; origin price and weight coordinates transform coherently so value and D remain invariant. Do not apply future split factors to data available earlier.

Use a cash-flow-consistent value coordinate for basket movement: for each original share, current transformed-share market value plus vested signed cash/receivables attributable since origin, less mandatory entitlement subscriptions if lawfully automatic. Hence price drops on ex-distribution dates alone are not convergence. Cash distributions are not reinvested. When a distribution is included in that coordinate, the gross-payoff ledger adds no second copy. Short manufactured amounts offset the corresponding signed entitlement exactly once; extra contractual service charges belong to other cost. Withholding/reclaim eligibility uses actual account terms, not assumed gross recovery. No elective rights subscription, security replacement or reinvestment.

An action requiring discretion or not representable by a verified entitlement-preserving transformation blocks entry if known before submission; if encountered while holding, enter X/action-pending and apply section 8. Missing action evidence is unknown, not clean. Publication revisions discovered later create explicit availability/lineage records, not retrospective admission changes.

The qualified value-coordinate transformation supplies the P symbols in the canonical movement equation; execution-price P/O and entitlement ledgers are retained separately for reconciliation. Do not include a distribution both in this transformed movement and as an additional increment to that same movement.

At each common close value all outstanding actual positions/receivables using qualified marks and disclose stale/unknown components. If any material required mark is missing, label NAV/return unavailable for that interval; do not use the last price as a clean observed return. End-of-session monitoring gaps enter X operational handling if they occur during an admitted basket; an unobserved historical gap remains censored and cannot be assigned an invented X payoff. Funding accrues on actual calendar time including closures.

## 4. Common cap and exhaustive outcome coding [F/U]

Propose one **20 common scheduled-session cap**, counting entry session as 1, regardless of missing quotes or suspensions. The calendar counter never pauses to make convergence look better. Trigger cap liquidation at the close of session 20, with execution at the next lawful scheduled liquidation window. Legal settlement delays may outlast the cap; do not call the cap an execution guarantee.

Set eta=0.10 ex ante: ±10% of the fixed remaining displacement is approximately unchanged. No boundary calibration. With
\[
b(q)=s\Delta B_u^{trade}(q)/|D_u|,\quad
\theta_F=\inf\{q:s(D_u-\Delta B_u^{trade}(q))\le0\},
\]
and cap close theta_cap, classify **qualified mature attempts** by this priority:
1. **X:** abort/failed entry, or any exceptional trigger in section 8 before financial closure. Tag X_entry (no episode), X_hold or X_exit; none creates a fictitious target hit. A target hit followed by recall/exception during liquidation is X.
2. **F:** admitted, not X, and theta_F<=theta_cap; target/cap tie is F.
3. **P:** admitted, not X, no hit by cap, and 0.10<b(theta_cap)<1.
4. **N:** admitted, not X, no hit by cap, and |b(theta_cap)|<=0.10.
5. **A:** admitted, not X, no hit by cap, and b(theta_cap)<−0.10.

These five states are exhaustive for **observed mature outcomes**, not for missing data. Pending/right-censored/unobservable is a data-status field, not a sixth economic state and not N or a guessed X payoff. A failed no-fill submitted attempt also belongs to X_entry, even if realized cost is known to be zero; a rejected pre-submission proposal is coverage, not an attempt. This proposed X subcoding reconciles the approved forced/exceptional class and E-A without pretending failed entries were S3 episodes.

A hit does not guarantee a positive realized payoff; overshoot and liquidation delay remain in actual cash flows. Early ordinary exit uses the same first-target rule; the remaining hypothetical cap path is not needed. No performance-dependent recoding, alternative cap or state grid is permitted.

## 5. Sizing and capital reservation [F/M/U]

Propose six equal, segregated research sleeves, one per estimator, with sleeve NAV V_c=one-sixth of allocated portfolio NAV at inception. Return and holdings records remain separate; do not select an estimator winner. Reinvest/update each sleeve's actual reconciled NAV daily, without cross-sleeve performance reallocations. Known costs/receivables and unavailable NAV states carry through; unknown NAV blocks new orders.

Raw desired gross per proposal is K_raw=0.01 V_c at the prior qualified close. Within each sleeve permit at most one admitted or pending attempt per unordered pair, regardless of direction; simultaneous opposing ordered-pair signals mean ENTRY CONFLICT / NO TRADE for that pair. Repeated signals do not reset an existing episode. Exact duplicate C/L proposals are mechanically linked in research reporting, not independent evidence; sleeve commitments still count if both sleeves would trade.

At the synchronized snapshot define physical gross fractions a_e,k=|w_e,k|O_k/(P_k,t L_e), summing to 1. Batch all same-window proposals, ordered by ascending unordered-pair IDs, direction ID and estimator ID only for audit—not discretionary priority. Choose the largest common rho in [0,1] such that K_e=rho K_raw,e obeys all below together with existing commitments:
- Sleeve total gross commitment <=100% of V_c; portfolio total gross <=100% of total NAV.
- Each physical security's gross commitment <=10% of sleeve NAV and <=10% of portfolio NAV.
- Absolute signed net currency exposure <=10% of each sleeve NAV and of portfolio NAV, on aggregate signed positions; diagnostic market/industry exposures reported separately. Compute this as linear inequalities in rho; existing breaches allow no new entry.
- Planned leg value <=0.1% of its prior-20-qualified-session median daily traded value, all 20 observations required; order quantity <=10% of displayed executable depth at its permitted limit. Funding/borrow/cash constraints below also bound rho.

Commitments are measured **gross before execution netting**, including outstanding orders, actual holdings, pending abort/unwind and reserved collateral. Opposing obligations across baskets do not release locate/margin or capital unless the actual contract legally releases them and the ledger records release. P0 sends segregated child orders and does not cross/net baskets internally; model-level long/short offsets remain separate economic obligations. Aggregate NAV counts actual cash once.

Reserve long purchase cash plus entry charges, lender-required short collateral and margin, 20-session/calendar-equivalent contractual carry at known maximum rates, and quoted liquidation charges. Restricted short proceeds are not available cash. Credit facilities count only with committed limits/rates and broker-recognized collateral; principal is reserved, not expensed. If no contractual cap on a required reservable liability exists, mark resource/economic qualification unavailable rather than invent a safety multiplier. Longer exceptional carry draws from the same reserved/free-capital ledger; insufficiency invokes margin handling.

Apply E1 at the resulting K, with nonlinear minima/fees recomputed once. Candidates failing E1 are dropped with their unused allocation left idle; no redistribution or second size search. Candidates whose exact shares violate lawful lot rules are dropped, again without redistributing. Minimum K is the smallest feasible instrument-lot allocation, not a new discretionary currency threshold. **No rounding of the approved basket weights**: only representable exact shares under the instrument/account rules qualify (arithmetic comparison tolerance 10^-10 relative, not an economic mismatch allowance). General regression ratios may have no executable lot-compatible basket at the proposed K. This can make the strategy unavailable; the package does not silently authorize a rounded approximation or assert universal executability.

Once a qualified order batch is submitted, K_e is immutable as the denominator through success/failure. Peak deployed gross and reserved capital are diagnostics, never replacement denominators. Scheduled caps constrain new entry; price drift can cause a later breach, handled deterministically in section 8 rather than resized/rebalanced.

## 6. Borrow, settlement and funding evidence [F/U]

For **every actually short physical leg after within-basket duplicate aggregation**, require an account/instrument-specific timestamped evidence record available at the precheck and reconfirmed before order release:
- Broker/lender identity and account eligibility; valid locate/reservation ID, exact instrument/share class, permitted short quantity, already-consumed quantity and non-reused remaining allocation.
- Locate receipt time, contractual valid-from/to, reservation through the entry completion deadline, rejection/revocation conditions and whether locate means a binding loan commitment or only indicative availability. Indicative availability alone fails.
- Borrow rate or deterministic contracted rate schedule/reset formula, valuation base, calendar/day-count, minima, upfront/locate charges, rate caps if used for reservation, accrued-fee settlement and rebates.
- Required initial/maintenance collateral and margin, haircut/currency/eligible collateral, restricted proceeds and legal right to use any cash credit; funding facility, committed available balance, rates/reset/day-count and liquidation priority.
- Recall notice delivery channel/timestamp, deadline, partial recall mechanics, buy-in agent/price responsibility and costs, lender substitution rights (P0 does not elect substitutions), corporate-action allocation and manufactured distributions/withholding.
- Effective instrument/account-specific short-sale restrictions, permissible order prices/types, settlement, sale/cover availability, failed settlement and inability to same-day liquidate bought stock. “Immediate unwind” means immediate cancellation and submission/queueing of the earliest lawful liquidation obligations, not an assumption that every leg is sellable immediately.
- Qualified historical evidence of the same contractual exposure/exit possibilities for the cost/joint-path model; a 20-session expected cap is not a guaranteed loan term.

**BORROW UNAVAILABLE** means a required short has no binding eligible locate/quantity/validity or a legally usable short/settlement route, or mandatory terms needed to determine the obligation are unknown. Record the scientific signal and block order submission. A known later recall does not retrospectively invalidate the earlier scientific signal.

**ECONOMIC GATE UNAVAILABLE** means required P1 support, payable-fee/rate/basis/funding/entitlement evidence or a qualified expected cost path is missing/nonfinite/incompatible. A valid locate with missing borrow price fails economics; missing permission fails borrow. Record all applicable reasons rather than letting one mask another. Verified contractual zero is allowed; absent evidence is not zero. Known valid estimates with mhat<=chat give ECONOMIC GATE REJECTED, not unavailable.

Terms effective after entry may be used prospectively only if announced and available before the decision. Unannounced future changes are scenario risk, never substituted into a historical admission calculation. On-term updates during holding are recorded at actual receipt and may invoke contractual exit; they do not revise the frozen admission estimate.

## 7. Joint entry and failed-attempt state machine [F/U]

One event is a frozen candidate/pair/direction/signal-origin proposal with a single intended K, registry version, exact vector n and parent attempt ID. All child orders and replacements **for liquidation only** carry that ID. All six sleeve batches share a single resource-reservation ledger.

Proposed entry state machine:
1. **PREPARED:** signal, target, hedge, quotes, costs, resources and legally permitted routes qualified. No attempted execution economics yet; pre-entry rejection is a coverage record.
2. **RESERVED:** exact K and all locate/cash/margin/quantity allocations atomically reserved. If any reservation fails, release unused reservations, no orders.
3. **SUBMITTED:** dispatch the full basket's permissible immediate-or-cancel marketable limit orders within 1 second as one parent batch. Limit for buys is the snapshot best ask, for sells the snapshot best bid, rounded only to a lawful executable tick on the non-more-aggressive side. No resting-order queue fill assumption; no entry repricing/retry. If IOC or equivalent immediate cancel semantics are unavailable for a required leg/account, the event is EXECUTION UNAVAILABLE.
4. **EXPOSED/ENTRY_PENDING:** first actual fill starts economic exposure. IOC fills may be partial; unfilled quantity is canceled. **Complete** means confirmed exact full planned quantities on every leg, valid reservations and no abort already latched. Only then create an admitted S3 episode.
5. **ABORT_LATCHED:** immediately upon explicit rejection, canceled/unfilled IOC remainder, locate revocation, qualification/resource failure, dispatch overrun, or failure to confirm full completion by **5 seconds after the first child submission**, whichever occurs first. No waiting for favorable completion after a known failure. Send cancel-all, quarantine duplicate/out-of-order messages and reconcile exchange/broker IDs.
6. **UNWIND_PENDING:** all actual and subsequent late entry fills join mandatory liquidation. A late full basket does not create an episode after abort. No completion chase or new hedge instrument. Lock the attempt's capital/borrow obligations until reconciliation.
7. **CLOSED:** all actual quantities flat, borrowed inventory returned and fees/cash/entitlements settled or represented by fully specified, finally reconciled receivables/payables. Settlement pending is not closed.

Immediately on abort, choose lawful liquidations by: mandatory contractual deadline first (earliest timestamp); then largest current absolute currency exposure; then ascending instrument ID. Send reducible legs in that deterministic order in the same dispatch cycle. Use fresh executable quotes, never stale original limits. For ordinary abort/unwind use IOC at best bid/ask, no discretionary limit chasing; retry at the first fresh quote at least **1 second** later while trading is permitted. Each retry may only reduce actual outstanding exposure and uses current lawful quotes. No price-percentage stop that would leave an avoidable contractual default; an imposed broker/exchange restriction remains binding. Untradeable or settlement-locked inventory is queued until the earliest lawful opportunity and valued as outstanding risk. This continuation is liquidation, not an entry retry.

All submitted attempts, including zero-fill rejects and partially filled failures, retain intended K and their full actual economics. Never pretend an order-book quote is a fill. Development reconstruction requires certified complete order-event evidence or qualified replay of this exact crossing-order protocol with matching/latency/market-response assumptions disclosed; ordinary daily bars cannot identify IOC completion. Ambiguous fills cannot be assumed successful or zero-cost. Synthetic replay is an executable-policy estimate, not proof of live fills, and must be separately authorized before use.

## 8. Deterministic exceptional exit state machine [F/U]

For admitted baskets maintain NORMAL_HOLD → NORMAL_EXIT_TRIGGERED → LIQUIDATING → SETTLEMENT_PENDING → CLOSED. Any exceptional event before CLOSED latches **X** and changes the route to OBLIGATION_EXIT / RISK_EXIT / BLOCKED_LIQUIDATION; the latch never clears to F after recovery. Original target and static holdings are not reset.

**Trigger precedence at a timestamp:**
1. Binding recall/buy-in, margin/settlement default or contractual/legal liquidation instruction.
2. Known current position/portfolio capital-cap breach, loss of hard hedge/T1 qualification, inability to obtain a required scheduled valuation, suspension/untradeable leg, unexpected session/calendar mismatch or unsupported corporate action.
3. Normal target/cap trigger.
Within a level use earliest legal deadline, then actual receipt timestamp, then instrument ID. A qualified entitlement-preserving split/cash distribution is processed before value-based trigger evaluation; an unknown action cannot be processed as a clean price move.

Actions:
- **Recall / buy-in:** cancel new entry, obey specified returned quantity/deadline; cover recalled leg at first lawful quote and start whole-basket liquidation. Forced external buy-ins are recorded at actual terms. Never short a replacement to restore geometry.
- **Margin / funding breach:** honor mandated transfers from already available committed resources; if contractual demand remains unmet or a cap breach is detected, cancel all new entries and liquidate affected basket(s). For portfolio-wide deficits, process earliest obligation, then largest gross basket, then attempt ID until compliant; no discretionary “best trade” ranking.
- **Suspension / one-leg untradeability / calendar mismatch:** latch X, cancel outstanding increases, liquidate every lawfully tradable remaining leg in the fixed order. Keep the blocked leg as a recorded obligation; retry on verified reopening/settlement release. Hedge preservation never prevents feasible risk reduction.
- **Corporate action:** apply a verified entitlement-preserving transformation without discretionary trade; if impossible or terms unknown, latch X, seek lawful liquidation of executable holdings, record the surviving entitlement/claim with unknown status until qualified. No voluntary elections or replacement instruments.
- **Partial liquidation / late fill:** reduce actual net position of that parent only; continually reconcile child order IDs so cancellation acknowledgements do not erase fills. Uncertain quantity stops orders that could increase/reverse exposure; obligated known reducible quantities may still be liquidated.
- **Settlement pending:** no new episode on the same unordered pair; keep reservations while legally encumbered. Outstanding manufactured payments, fees and recall claims remain in the attempt. An unresolved claim cannot be erased at the cap or validation end.

Scheduled ordinary liquidation begins in the next common opening window and follows the same deterministic best-quote IOC/retry process. An explicit rejection/canceled remainder or failure to confirm complete normal liquidation within 5 seconds of its first child submission latches X; subsequent retry is exceptional liquidation. Pending acknowledgements never imply a flat position. If the common window fails or any leg cannot execute, latch X immediately and use the available-leg rule, rather than wait indefinitely for hedge symmetry. Funding/borrow accrue until their actual contractual release. The proposal allows legal settlement delays but does not replace “earliest lawful” with a fixed assumed duration.

## 9. All-leg cost and gross-payoff estimation contract [F/M/U]

### 9.1 One accounting identity

For each fill l, let signed executed quantity q_l be positive for a buy and negative for a sale; p_l its actual fill price; m_l its declared pre-order benchmark midpoint. Entry children retain the section-3 O benchmark; each liquidation submission uses its synchronized or exceptional fresh pre-order midpoint. Partial/late fills keep their parent's benchmark. Define cash entitlement total D_e, assigned once:
\[
G_e=\{-\sum_l q_l m_l+D_e\}/K_e,\qquad
C_{exec,e}=\sum_l q_l(p_l-m_l)/K_e.
\]
For a financially closed attempt,
\[
R_e^{net}=G_e-C_{exec,e}-C_{fees,e}-C_{borrow,e}
-C_{funding,e}-C_{other,e}.
\]
If terminal noncash claims exist, qualified marked entitlement value and subsequent settlement reconciliation enter D, never fabricated cash. G is signed benchmark gross economic capture, including actual exposure timing, not a clipped target. At ideal complete reference fills it reconciles to static-basket movement and entitlements; failed attempts use their actual changing inventory.

This convention puts arrival-to-fill spread/latency/impact in execution costs. Do not also charge them inside G. Benchmark changes between entry and liquidation remain market capture; mid-price movement from a given order's benchmark to its fill belongs to that order's execution deviation. Market-maker price improvement may make realized deviation negative; retain it in accounting.

### 9.2 Cost components

All components are currency amounts divided by the same attempt K; scenario expectations use the **same joint event paths** as section 10.

- **Commission:** sum the applicable side/instrument tariff \(F_{broker}(q_l,p_l,\text{order/day aggregation})/K\), including minima, tiers and verified rebates. Source: account-specific signed broker tariff; available before entry and effective at the charge time. Recheck each entry and each announced effective change. No guessed constant if schedule/minimum aggregation is missing.
- **Exchange/regulatory fees/taxes:** sum applicable instrument/side/value/quantity schedule functions /K. Source: effective official rules plus account applicability. Do not assert any present tax or fee rate here. Announced future schedules may enter an entry forecast; otherwise use the current qualified schedule under the joint-path forecast. Unknown applicability => unavailable.
- **Spread:** expected signed crossing cost at order arrival, \(\sum_l |q_l|(\text{ask}-\text{bid})_l/2K\), using contemporaneous quotes for entry; future exit/unwind quotes come from the qualified joint path library described below. Exact realized accounting uses total C_exec, not this component added again.
- **Slippage plus impact beyond quoted spread:** estimate one common nonnegative two-coefficient execution model
\[
E[\delta_l-\text{halfspread}_l/m_l]=a+b\sqrt{v_l/ADV20_l},\quad a,b\ge0,
\]
where \(\delta_l=q_l(p_l-m_l)/(|q_l|m_l)\), v_l=|q_l|m_l and ADV20 is prior-20-session median traded value. Fit nonnegative least squares on prior qualified distinct parent-order records; no instrument/estimator/state-specific tuning. This combines latency and residual impact because they are not independently identifiable from a fill deviation. Report them jointly; do not add another standalone slippage/impact charge. Require full-rank design, at least 200 parent orders across 20 distinct sessions, and at least 20 for each current physical instrument and side. Proposed participation must lie within the observed min/max supported range for that instrument/side and obey the ex-ante depth/participation caps. Outside support => ECONOMIC GATE UNAVAILABLE, no extrapolated zero.
- **Borrow:** \(\sum_k\int \rho_k(v)\,V^{borrow}_k(v)\,dv/d_k\), plus unique locate/minimum/return fees, all /K. Rates/bases/day counts come from binding lender terms; exposure duration comes from the joint path. Reconfirm current terms at entry. Unknown rate-reset/recall fee mechanics fail, rather than assuming flat zero. Forecast applies known current/announced schedule to resampled paths; report unannounced-rate-change uncertainty.
- **Funding:** \(\int r(v)B^{debit}(v)dv/d-\int r^{credit}(v)B^{eligible\,credit}(v)dv/d\), /K, with contractual tiers/restrictions. B is the cash/collateral/settlement ledger path, not gross notional by default. Only legally available credit offsets borrowing. A blanket borrow-plus-funding charge on the same economic debit is prohibited.
- **Collateral:** posted principal is a reserved asset, not a cost. Only its actual financing debit, contractual custody/service charges and permitted interest enter the corresponding unique ledger account. No arbitrary capital-opportunity-cost premium.
- **Distributions/manufactured payments:** signed cash entitlements enter D once. Extra lender/broker administration charges enter other cost; do not add the manufactured payment again after including the short signed entitlement.
- **Failed entry, unwind and exceptional exit:** same fill/fee/carry functions on actual attempt path, including no-fill charges, delayed legal unwind, recall/buy-in and settlement. No separate “failure penalty” on top of those costs.
- **Other:** only enumerated contractual charges with effective schedule and unique allocation. No residual plug. If a charged component lacks evidence, the gate is unavailable.

### 9.3 PIT forecast and estimation frequency

Tariffs, rates, quotes, available balance and reserved capacity update at every actual precheck from then-available evidence. Numerical execution coefficients a,b and the event/path library are fitted once per scheduled half-year development origin from mature prior records with a 20-session embargo; keep them fixed within that block. At final freeze keep learned coefficients/library fixed throughout prospective validation. Mechanical contemporaneous contract/quote changes remain permitted; validation outcomes do not refit the model.

For a new attempt, evaluate each prior qualified joint scenario path under the current basket, intended K and current known contracts, preserving that path's linked admission branch, holding duration, partial exposure, liquidation timing and exit liquidity state. Transfer *dimensionless leg-role inventory fractions, price multipliers, spread fractions and participation* to the current actual instrument mapping; never average raw currency costs of differently sized baskets. Roles are j, i, market and the two industry slots before physical aggregation; same-industry duplicates are then combined. A required current role absent/undefined in a source path cannot be guessed or dropped; if the common library cannot support all required path components, economic qualification fails. This explicit transferability assumption is stronger than an observed cost identity and must be reported.

Compute each scenario's expected unique costs by averaging its full paired paths; then weight by the same pooled state frequencies, including X_entry. Known current entry costs may be evaluated directly; unknown future duration/exit conditions use the joint library, never one unconditional holding time. Do not choose whichever of a path forecast and a quote bound makes E1 pass. Normalized transfer is for **cost mechanics**, not a replacement of the approved raw arithmetic G forecast by event-target-scaled capture.

The proposed coefficients are mechanical component estimates, not cost parameters calibrated to strategy profits. Entry/exit execution evidence and future payoff-path access still require separate authorization; the present document estimates nothing.

## 10. Pooled P1, attempts and support [F/M/U]

### Population and bootstrap

Use one common low-dimensional pool across all six estimators and both signs. A scientific opportunity satisfying z, Target B, sign, hedge and operational qualification generates a **shadow candidate attempt** under the fixed resource/execution contract **before E1 selection**. Construct this prospective estimation ledger only under later explicit event-path access authority. It includes would-be unfavorable attempts and cannot be selected by the very capture forecast being fitted. Real executed attempts are a separately marked subset; do not count both shadow and realized records for the same event.

The training ledger must have qualified observed execution records or an explicitly authorized, auditable reconstruction of the proposed IOC/unwind policy. Daily prices do not establish fills, queue state, borrow or counterfactual market impact. If required data cannot identify a path, retain it as unobservable and fail the affected pool; do not use theoretical full-fill outcomes as executable evidence. This package does not promise that the exposed 2015–2019 archive can supply such a library.

Bootstrap fixed-policy shadow opportunities without E1, but with evidence for all primitive contractual costs, legality, resources and fills; P1/E1 availability is not itself a prerequisite to create a shadow event. Do not use the estimated future cost or P1 gate to select these seed events. Development shadow sleeves start at a declared **CNY 1 million per estimator** on the first eligible simulation session; their balances/constraints then follow the same accounting rule. This is an ex-ante reference scale, not a statement of available investment capital. No portfolio return curve need be exposed to researchers to compute the prescribed event labels; such calculations are nevertheless empirical economic work and need explicit authorization.

One attempt is one parent submission batch. Retain all five distinct equation groups. R0-C/R0-L exact duplicates (same origin, pair, direction, coefficients, w, K, order contract and path) count once, with both identities attached; use C as deterministic representative. If the supposedly duplicate equations disagree materially, stop that equivalence check rather than count twice or average. Coincident nonduplicate estimators remain separate attempts and dependent observations; no artificial independence claim.

### Pooled estimator and failure branch

Let R_e denote the outcome-state label, distinct from net return R_e^net. Assign outcome states by section 4; X_entry explicitly tags submitted failures with no admitted episode. Let N count mature qualified unique attempts:
\[
\widehat\pi_r=N_r/N,\qquad
\widehat G_r=N_r^{-1}\sum_{e:R_e=r}G_e,\qquad
\widehat m=\sum_r\widehat\pi_r\widehat G_r.
\]
No pseudocounts, shrinkage, winsorization, removal of adverse states or new probability model. Preserve raw arithmetic G/K normalization, not average G divided by each event's target. Within a fixed pool mhat is common; variable current costs/feasibility can still differ. This is not claimed to estimate a flexible event-conditional mean.

Record A_e=1 if admitted, else 0, and p_admit=N_admitted/N **as a descriptive frequency of the same pool**, not a separate learned admission model. The all-attempt sample mean satisfies
\[
\bar R=\widehat p_{admit}\bar R_{admitted}
+(1-\widehat p_{admit})\bar R_{failed}.
\]
Thus E-A failures enter P1 and cost expectations through X_entry, while the F/P/N/A classifier remains an admitted-episode classifier. Also report conditional admitted-only scenario diagnostics, without substituting them for primary economics.

Per event retain exact fill inventory path, gross G, each cost component, admission/abort/trigger times, target remainder, settlement closure, duration in calendar and common sessions, recall/action codes, signal model, pair, direction and original K.

### Maturity, censoring, support

At block origin b use only attempts whose submission is at least **60 common sessions before b**, whose complete outcome/settlement was available at least **20 common sessions before b**, and whose inputs are in the permitted 2015–2019 region. These are fixed lag/embargo rules, not selecting fast winners.

Consider the entire predeclared eligible age-60 cohort. If any of its attempts remains unobservable/unsettled/right-censored, mark the pooled economic estimator unavailable for that origin. Do not silently estimate only complete cases. Recent (<60-session) attempts are intentionally not yet cohort members, regardless of their outcomes. Actual long-lived obligations persist until resolved; no numerical truncation payoff.

Require at least **500 unique mature attempts**, **20 unordered pairs**, **20 non-overlapping 20-session origin clusters**, at least **50 attempts in each of the five distinct equation groups**, and **20 observations in each F/P/N/A and each of X_entry and admitted-X**. Require at least 20 in each signed orientation overall; no pair may contribute >20% and no 20-session time cluster >20% of N. These are fixed administrative support minima, not proof of effective independence or finite tail risk. Every required cost-path role also needs full support. A missing rare X state is unavailable, not zero probability; no P3 activation. There is no bounded fallback.

Use all eligible earlier development history (expanding pool), not whichever trailing subwindow scores best. Fit at each six-month origin, embargo as above, and freeze until the next origin. Descriptive clustered uncertainty uses the common 20-session calendar blocks across estimators/pairs, keeping cross-sectional dependence together; identify concentration beyond those blocks as a limitation. Candidate-specific/signed calibration and exchangeability diagnostics do not select six different fits. A poor pooled model is reported as poor/inadequate; it is not automatically replaced.

## 11. Reference population and numerical z0 [F/M/U]

Keep the approved model-space MAD, alpha=.05 and weighted empirical inverse CDF. No absolute-value trade residual enters this reference.

Propose 2015 as input-only warm-up; reference blocks begin **2016H1**, then 2016H2, 2017H1,...,2019H2. At a forward six-month block origin use only completely ended reference blocks strictly before that origin, with all input records available by the cutoff. First potential publication is before 2017H1 using the two 2016 blocks; if unsupported, z0 is unavailable. A cutoff calculated later never creates retroactive 2016 S3 events. No 2013–2014 or 2020+ lookup is assumed or authorized by this package.

Within each completed reference block:
- Start from the PIT unordered-pair registry obtained from the unchanged relationship/pair eligibility protocol at that block origin. Later inception/membership does not backfill it.
- Include only dates on which both ordered prediction directions and all six model z objects are simultaneously qualified on their approved common aligned scale support. One missing required object excludes that whole pair-date reference tuple, not just the inconvenient estimator.
- A pair requires at least **60** such common dates. Both ordered directions are retained regardless of positive/negative z; ordered direction is not the sign of z. No support check uses future convergence labels, proxy qualification, E1, fills or profits.
- Require at least **10** complete pairs and at least **80%** of that block's PIT registered pairs to meet the fixed complete-pair test. Unsupported pairs are explicitly excluded under this proposed population rule and listed in coverage; no missing estimator/direction group is reweighted into another group. If block coverage fails, the **whole reference is unavailable**, not formed by dropping that block.
- Require at least **two complete blocks** and Kish weight support \(1/\sum_l\omega_l^2\ge1000\). This is weight concentration support, not a claim of independent sample size. Report pair/time clustering.

For complete pair p, direction d, group g, candidate c and qualified date v:
\[
\omega_{b,p,d,g,c,v}
=\frac1B\frac1{P_b}\frac12\frac15
\frac1{|g|}\frac1{n_{b,p}},
\]
where groups are {R0-D}, {R0-C,R0-L}, {R1-M}, {R1-MI}, {R3}; |g| is 2 only for C/L. Equal common dates within a pair give n_b,p. Sum weights to 1 mechanically; do not renormalize missing required groups. A broken C/L duplicate-equation consistency check is reported as integrity failure, not two independent groups.

\[
z_0=\inf\{x:\sum_l\omega_l1(|z_l^{ref}|\le x)\ge.95\}.
\]
Sort finite absolute values ascending, aggregate equal values and choose the first cumulative weight >=.95. Keep inclusive |z|>=z0; report tie mass. Store exact input/weight lineage and deterministic arithmetic convention (rational cell weights until final comparison, no random tie-breaking). No Gaussian replacement, alternative alpha, occurrence calibration or outcome-dependent reference subset.

During development expand reference blocks and publish one new common cutoff at each half-year origin. Final estimate uses all complete 2016–2019 blocks under the same tests, once. Hold the final numerical z0 fixed through prospective validation; current model coefficients and MAD still update under their approved PIT rules. Unsupported final reference means no validation activation, not a different alpha or sample.

## 12. Development region, folds and finite budget [F/M/U]

2015–2019 is proposed development only. 2020–2025 is already exposed and cannot support pristine final-validation claims. No assertion is made that pre-freeze 2026 is untouched.

**Fixed chronology:** 2015 input warm-up; 2016 reference formation and remaining input qualification; six forward assessment blocks 2017H1, 2017H2, 2018H1, 2018H2, 2019H1, 2019H2. No new access is authorized here. If the 2015 start cannot support required native relationship histories, exposures, T1 or scale, early origins are unavailable; no unauthorized earlier-year extension.

At each block origin:
1. Freeze the qualified proxy registry using strictly earlier evidence and the deterministic rule.
2. Form model z0 from completed reference blocks; never use the forward block.
3. Fit pooled capture/path and execution-component estimates from older mature records using the 60-session cohort lag and 20-session availability embargo. Their labels/settlement must end before the cutoff. Overlapping outcome intervals crossing the cutoff are excluded from fit by the same predeclared cohort rule; if an old cohort record remains unresolved, fail support rather than silently censor it.
4. Process the forward block chronologically with frozen learned components and authorized PIT model/exposure/quote/contract updates. All six estimators receive the same policy; native missing support is reported.
5. Forward outcomes may inform only the next scheduled origin after maturity/embargo, not a within-block refit or parameter search.

The first forward blocks may supply shadow events without a supported P1 forecast; those forecasts remain unavailable, and there are **no economically admitted trades** until every gate is supported. Do not seed the initial pool with a retrospectively computed threshold or hypothetical already-profitable sample.

At 2019 end make one final fit using only permitted region records mature/available by that cutoff and the same embargo. A late-2019 cohort without observed final obligations is reported pending; no 2020 lookup. The final model may therefore have less than all 2019 event history. Do not shorten settlement or extrapolate missing outcomes. Current pre-validation auxiliary histories must later be qualified separately; this historical development boundary does not magically provide future signals.

**Budget:** ONE complete economic specification, six scheduled forward blocks and one final production fit. This permits at most seven scheduled fits of each learned P1/cost/reference component, plus deterministic daily model/auxiliary refresh required by the protocol; it is not seven tunable variants. Zero cap/eta/tolerance/alpha/sizing/execution grids; zero flexible conditional ML; no P3, EWLS or alternative proxy-selection runs.

Only the two already-approved H252 MAD and H126 SD scale specifications may receive diagnostic-only replay: same model origins/reference weighting/.05 rule and support policy, separate diagnostic threshold values, no replacement of the primary H126 MAD, no secondary economic portfolio runs. Thus one economic protocol plus two non-selecting scale diagnostics, no factorial combination. T1 reporting variants and sign/estimator/X-cause tables are summaries, not fitted strategies.

**Objectives, not selection criteria:** mechanical OLS/NNLS fitting objectives; multiclass Brier score \(\sum_r(\hat\pi_r-1\{R=r\})^2\); signed gross-payoff prediction error and MAE; duration MAE; execution-component error; coverage, censoring, concentration and accounting reconciliation. Keep pair/time dependence visible. No Sharpe, cumulative PnL, winner ranking or economic-return target is an optimization objective. Event G/cost/duration access is still economic outcome access, and must be explicitly authorized even if portfolio PnL is not displayed.

**Stop:** one prescribed pass; report support failures and model inadequacy. Missing evidence stops the affected forecast/event; a protocol contradiction, unqualified reconstruction, corrupted accounting or sample-boundary breach stops the run. No rerun with relaxed support/tolerances, later dates, another hedge or more favorable costs. Pure implementation-defect corrections require a logged bounded repair authority and cannot change these semantics. There are no C-class calibration choices in P0: only F rules and M outputs.

## 13. Prospective validation protocol [F/M/U]

**T_freeze** is the timestamp of an immutable signed protocol/input-manifest/model-output release after researcher approval, authorized development completion (or explicitly recorded unavailable disposition), all prerequisite integrity/qualification checks, proxy-ID registry lock, and hash lock of code, model parameters, z0, state/accounting rules and execution/cost contracts. No S3 validation may begin if the required model is unavailable. The present design commit is not T_freeze.

Use a timestamped **future no-access boundary**: the first full common scheduled trading session strictly after T_freeze whose opening occurs after that timestamp is session 1. No partially observed same-day session is validation. Register the start calendar before receiving that session's market/outcome data. Later unavailable signals count as coverage failures; they do not shift the start to a convenient date.

Propose a **calendar/session-fixed horizon of 504 common scheduled sessions** for new candidate attempts; 252 sessions is the minimum interpretable interim exposure horizon, **not an early-success stopping rule**. At session 252 permit only an operational completeness/censoring audit, no unblinded strategy-effect test or model selection. No event-count extension. At session 504 stop new attempts and permit a preregistered 60-common-session settlement follow-up with no new entries. Unresolved obligations after follow-up remain censored/unavailable; do not declare them zero or extend research inspection until a desired outcome appears. Any continuing real legal obligations would remain obligations under separately authorized operations, not extra scientific observations silently added to the test.

For final inferential reporting require at least 500 mature unique attempts per distinct equation group, at least 20 pairs and 20 time clusters per group; otherwise report insufficient precision/support. Count requirements do not extend the fixed calendar. Any unresolved included attempt prevents a fully identified all-attempt mean for its group; report censored coverage, not success-only inference.

Primary economic estimand: mean all-attempt net return per intended K, including E-A failures, for each estimator group under the preregistered E1 policy. Report six estimator books and both signs, but treat C/L duplicate-equation results as one linked hypothesis group, with equal C/L-book influence if distinct execution realizations exist; exact duplicate records count once. This is five hypothesis groups, not an independence assumption.

For the single final confirmatory family testing positive mean versus <=0, when support is qualified, preregister a paired calendar moving-block bootstrap with **20-session blocks, 10,000 replicates and fixed seed 20260927**, resampling the same origin blocks for all candidates and keeping all cross-sectional attempts/linked records in a block together. Resample centered returns for the null distribution, recompute attempt-weighted means with their actual block counts, use one-sided \((1+\#\{T^*\ge T_{obs}\})/(10001)\), and Holm-adjust the five p-values at familywise .05. Censored or unsupported groups get “not testable”, not significance; the family still has five slots (not-testable slots cannot be declared discoveries). Temporal bootstrap validity requires adequate weak dependence; report raw block paths and that limitation, with no theorem claiming arbitrary long-memory control.

Also report frozen P1 probability/gross/duration calibration, actual target-resolution distribution, qualification losses, borrow coverage, tracking and attempted-versus-admitted economics. These are descriptive secondary diagnostics, not additional confirmatory discoveries or reasons to select a winner. Positive returns alone do not establish that model extremeness adds predictive value relative to a non-extreme control; no new control-strategy experiment is smuggled into this package.

Freeze throughout validation: estimator set/definitions, primary scale/alpha/reference cutoff, Target B/sign/C4 rules, proxy identities/algorithm, auxiliary estimator settings, T1 budgets, cap/eta, event units, execution/risk/cost methods, P1 learned parameters, support rules, sizing, inference and stopping. Allow only already-specified PIT relationship/scale/exposure refresh, contemporaneous quotes/contractual rates and mechanically updated NAV/reservations, entitlement transformations and mandatory exits. No learning from validation labels.

Structural/contractual integrity failure pauses new entries immediately and is reported; do not restart the validation clock or discard its adverse prefix. Any scientific amendment terminates the original confirmatory protocol and requires a separately registered future study. A later authorization must state whether validation uses observed actual execution or a qualified prospective shadow reconstruction. Neither mode may be presented as the other; unverifiable fills/economic outcomes make the corresponding claim unavailable. No live trading authority is implied by a researcher-approved paper protocol. No data access, live orders or validation execution is authorized by this design package.

## 14. Minimal future acquisition and qualification scope [F/U]

This classification comes from canonical metadata/design records, not new payload inspection. “Existing” is not equivalent to “qualified for S3”. Dataset versions, account contracts and provider identifiers must be listed in the later bounded acquisition manifest; procurement/access choices do not reopen strategy rules and are not permission to license/download anything now.

**Already existing, potentially reusable after immutable integrity/PIT qualification:** frozen security identifiers/calendars, stock response/price and research factor definitions, PIT pair/model registry lineage, historical membership records and recorded model/scale ancestry. Reuse only qualified versions/fields with exact available timestamps. The V1 core fingerprint is preserved, not recomputed here. Previously fitted outputs cannot replace S3's prescribed chronology/geometry without conformance verification.

**Existing but requiring correction or requalification before economic use:** known C04/entitlement-response eligibility inconsistencies; factor/stock return-to-price/cash-flow unit mapping; membership publication-time lineage; current versus historical adjustment factors; later mask/action coverage; any daily quote field asserted executable without event-time evidence. Corrections require immutable descendant versions and explicit authority; do not repair C04 or overwrite V1 in this task. Unresolved intervals stay unavailable.

**Genuinely new required evidence unless a later inventory proves a qualified existing copy:**
- Full PIT candidate fund universe (including dead/merged funds), IDs, inception, mandate/index taxonomy, published holdings vintages, share/price/turnover series and actions; avoid present-survivor selection.
- Synchronized stock AND fund quote/depth/trade/order-event records at required timestamps, exchange sequence/receipt times, tick/lot/order/settlement eligibility and halt/limit calendars, sufficient to qualify entry, IOC completion, liquidation and T1 cash-flow paths.
- Account-specific historical and prospective binding locates, quantities/reservations, loan contracts/rates/recalls/buy-ins, collateral/margin/funding/restricted-cash records, effective fee/tax schedules and manufactured-entitlement obligations.
- Qualified fills/cancellations/late fills/settlement logs or specifically authorized counterfactual replay evidence for the fixed execution contract and independently supported market-response assumptions; matched primitive execution evidence for cost fitting.
- PIT cash/position/receivable accounting and resource reservations, plus future sealed-feed custody/access logs needed to demonstrate the post-T_freeze boundary.

If historical borrower/quote/execution evidence does not exist, a 2015–2019 executable P1 model may be **non-estimable**. A provider price series alone cannot cure that gap. No automatic daily-bar backtest, invented loan availability, synthetic fill success, P3 or alternative architecture replaces it.

**Optional diagnostics only:** fund NAV/premium attribution, holdings-based look-through exposure, H-B exact-replication attribution where independently defined, and the two approved scale robustness views. Optional sources cannot rescue a mandatory gate or expand the primary factor universe. No optional acquisition/benchmark calculation is authorized.

Minimal schema includes instrument/account/event identifiers, economic and receipt timestamps, provider/vintage/version, raw-document hash, units/denominator, effective-time interval, quality/unknown flags, original and transformed coordinates and parent-attempt linkage. Acquire only the fields/periods needed by the approved equations and stage; avoid bulk unrelated data. A later action must explicitly name permitted economic labels/output visibility, not disguise acquisition or payoff reconstruction as a metadata check.

## 15. One complete recommended package and decision boundary

**Recommend P0 in full**, subject to researcher approval: deterministic eligible fund-share registry; constrained common OLS252/daily; explicit absolute T1 budgets; observed synchronized post-open midpoint reference; static exact shares; 20-session cap/eta=.10; equal sleeves and fixed gross/resource caps; binding borrow evidence; IOC partial-fill abort with 5-second deadline and earliest-lawful deterministic unwind; X-priority exceptions; unique cash-flow cost ledger; raw pooled all-attempt P1 with strict support; expanding 2016+ reference/.05 inverse CDF; one 2015–2019 chronological development specification; and strictly post-final-freeze calendar-fixed validation.

No fallback is proposed. In particular, no rounded-share hedge, proxy substitution, sparse-state smoothing, P3, flexible ML, threshold grid or exposure-window rescue is bundled into approval. Exact lot geometry, missing historical execution evidence, strict support and fixed T1 budgets can make P0 sparse or wholly unavailable. That is an honest feasibility result, not permission to infer an optimized replacement.

**Freeze now if approved:** the proposed policy numbers, estimators, time rules, support/unknown handling, event/accounting semantics, registry ranking, research budget and future-validation contract. **Mechanical future outputs:** actual eligible IDs, exposure/A/h estimates, qualified tracking diagnostics, contractual fee/rate schedules, execution a/b, P1 frequencies/raw means/joint paths and empirical z0. **Bounded development calibration:** none; no scientific parameter is selected by maximizing a score or profitability. **Feasibility conditions:** every mandatory evidence, rank, exact-share, borrow, cost, path and support requirement; failures retain their declared unavailable states.

Approval would freeze these rules in one decision. It would not authorize acquisition, implementation, fitting, backtesting, live execution or PnL access. Those require separately bounded action contracts specifying data/outputs/paths; they are authority steps, not a proposed series of new strategy micro-decisions. No recommendations are adopted by this checkpoint.

Documentation-only validation: architecture/approval files remain unchanged; check links, exact changed-path scope, numerical/control consistency, historical log preservation and NEXT_ACTION=NONE. Full PowerShell validators are unavailable in this client, and empirical/core validators are deliberately not run under the no-data scope.

**S3 CONSOLIDATED PRE-DEVELOPMENT PROTOCOL / RESEARCHER DECISION REQUIRED**

| Binding | Proposed primary rule | Alternative if any | Why it matters | Requires data? |
|---|---|---|---|---|
| Proxy eligibility/selection | Common qualified market/industry fund shares; exact taxonomy identity; oldest inception then ID; semiannual registry, validation IDs locked | None | Deterministic, PIT, no outcome-selected proxies; missing slot unavailable | Rule no; registry/evidence yes |
| Auxiliary exposures | Preserve compatible R1 coefficients; constrained OLS252, >=240 rows, daily t−1, full rank/finite and condition <=10,000 | Fixed-63-half-life EWLS compared only, not selected/run | One missing-dimension rule across all six estimators | Rule no; coefficients yes |
| M1 and exact instruments | Approved inverse/minimum-norm; duplicate aggregation; numerical residual <=10^-10; no economic rounding | None | Does not silently change approved basket geometry | Rules no; mathematical/lot feasibility yes |
| T1 | 126/126 prior sessions; fixed exposure/mean/RMS/max/20-session-path/drift budgets in section 2 | No tolerance calibration; T2 reporting only | Explicit absolute tracking contract, independent of S3 performance | Budgets no; metrics/support yes |
| Timeline/target | One u+60 to u+120 synchronized midpoint snapshot, <=1s age/skew; submit <=1s; both frozen sign gates | None | Avoids opening-price lookahead and target reset | Rule no; timestamped observations yes |
| Corporate actions/valuation | Entitlement-preserving static coordinate; signed distributions once; unknowns unavailable | None | Prevents fake convergence and duplicated cash flows | Rule no; qualified entitlements yes |
| Cap/states | Common 20 scheduled sessions; eta=.10; X priority incl failed-attempt subtype; F cap tie; explicit censor status | No state/cap search | Exhaustive qualified mature outcomes without hiding failures | Boundaries no; labels later yes |
| Sizing/capital | Six equal sleeves; 1% raw attempt gross; common rho; 100% total gross, 10% security/net caps; no netting credit; exact lots | None | Reconciles portfolio resources with immutable attempt K | Policy no; NAV/quotes/capacity yes |
| Borrow/funding | Binding per-leg locate/quantity/validity, full rates/recall/margin/settlement evidence | None | Scientific signal cannot imply executable short inventory | Contract schema no; evidence yes |
| Entry | IOC basket batch; 5s completion; immediate abort on failure; late fills unwind; no chase | None | Defines admission, actual exposure and failed attempts | Rules no; lawful route/fills yes |
| Exceptional exits | Obligations, feasible reduction, geometry; fixed liquidation order and earliest-lawful retry; no replacement | None | Deterministic handling of broken hedges and pending obligations | Rules no; event evidence yes |
| Costs | Unique benchmark-fill identity; dated tariffs; two-coefficient NNLS execution deviation; joint scenario carry/exit paths | No arbitrary zero/buffer | Makes expected costs auditable and non-overlapping | Formulas no; schedules/fits/path evidence yes |
| P1 | All-attempt raw arithmetic pool; exact C/L dedup; 60-session cohort/20-session embargo; fixed support incl X_entry/admitted-X; no smoothing | None; P3 inactive | Avoids E1 training selection, omitted failures and sparse-state optimism | Rules no; empirical counts/G/T yes |
| Numerical z0 | Completed 2016+ half-years, complete tuple support, prescribed block/pair/direction/group/date weights; .95 inverse CDF | None | Future numerical cutoff is deterministic, alpha unchanged | Rules no; quantile yes |
| Development | 2015 warm-up/2016 formation; six 2017–2019 blocks + final fit; one economic specification, two scale-only diagnostics | No calibration grid or rerun rescue | Finite budget and honest exposed-history use | Protocol no; later authorized estimation yes |
| Validation | Immutable final T_freeze; next full future session; fixed 504-session horizon +60 settlement; no outcome refit; five-group Holm family | None | No reused “pristine” history or optional stopping | Protocol no; future evidence yes |
| Acquisition/authority | Minimal field/period manifest, existing vs requalify vs new vs optional; separate bounded access | None | Evidence availability is not presumed and approval is not execution | Inventory design no; later qualification/acquisition yes |
