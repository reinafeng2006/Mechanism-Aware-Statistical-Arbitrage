# S3 pre-development numerical constants audit

2026-09-30. **STRUCTURAL APPROVAL RECORDED; PROPOSED NUMERICAL CONSTANTS NOT FROZEN.**
Source: [consolidated protocol](S3_CONSOLIDATED_PRE_DEVELOPMENT_PROTOCOL_CHECKPOINT.md) at GitHub main `81abaecb5a4ff3484e725a2441d93e4affe0e203`.
Authority: [partial structural approval](../../decisions/S3_PRE_DEVELOPMENT_STRUCTURAL_APPROVAL.md) and [authority ledger](../../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).

## Scope and approval boundary

This audit inventories the source protocol's explicit numerical policy constants, including counts written in words, dates/cadences, zero-tolerance rules, derived numbers and the single unselected EWLS alternative. Repeated occurrences with the same meaning are grouped; identical numbers with different functions have separate entries. Section/table numbering, model/state identifiers (R0, R1, R3, P0, P1, T1, C4, E1), version dates, commit hashes and equation indices are labels, not tuning constants. Inherited model H/U labels are not a newly proposed choice. The inherited MAD multiplier is included explicitly from its approval record even though the P0 text does not repeat its literal value.

The researcher approves the enumerated structural rules: qualified fund-share/deterministic-registry architecture; common auxiliary exposure architecture; M1 with strict unavailability; static-origin H-C/Target B; aligned H126 daily MAD and weighted 5% two-sided model-z discovery; mature F/P/N/A/X with separate censor/unavailable status; pooled low-dimensional P1/E1; intended K/E-A; deterministic partial-fill abort/unwind; strict missing-evidence handling; no fallback/outcome-selected rescue/flexible ML; and prospective post-freeze validation only. Previously exposed 2020–2025 remain non-pristine.

This is **not blanket P0 approval**. The oldest-fund tie-break details, specific OLS/NNLS methods, X_entry coding, censor shutdown implementation, exact lot policy, portfolio layout, detailed exception triggers and inferential procedure are not adopted merely because they accompany numeric rows. Only explicitly approved structure and earlier decisions are binding. Numerical alternatives below are bounded discussion choices, not authorized calibrations, grids, amendments or fallback strategies.

Previously approved H126 model scale/daily refresh, alpha=.05, the inverse-CDF .95 rule and reference-group architecture remain approved. Proposed T1 history 126 is a DIFFERENT object. Proposed confirmatory-test alpha=.05 is also a DIFFERENT decision. No numerical z0, tracking, cost or exposure has been estimated.

## Classification and how to read the inventory

Categories are the researcher's requested categories:
1. **Institutionally/contractually determined:** numbers supplied by qualified external terms. No actual rates, tick/lot sizes, loan availability or settlement periods are asserted here.
2. **Mathematically necessary:** algebraic identities/existence conditions conditional on the already-chosen formula. They do not make surrounding sampling horizons or tolerances necessary.
3. **Administrative/ex-ante policy choice:** risk, capacity, timing, resource, coverage or governance choices. Such choices can be stated without outcome data, but that alone does not validate the particular number.
4. **Statistically motivated design choice:** window, support, dependence, precision, estimator or inference design. A statistical motivation is not a supplied power/coverage proof. Several support values in P0 were called administrative minima; category 4 here describes their statistical purpose, not a newfound empirical justification.
5. **Future mechanically estimated quantity:** no fixed value exists now; the method must be approved and data access separately authorized.

Sensitivity statements are qualitative mathematical/design consequences, not estimated sensitivity results. The compact final table uses category numbers defined here; full justifications and alternatives are in the matching entry IDs.

Each entry gives value, source section, reason, effect on the estimand/economics versus operational/inferential robustness, outcome-free justification and bounded alternatives. Category 1 is externally determined; category 2 is definition/identity-bound; category 3/4 values are researcher design choices rather than facts imposed by mathematics or verified market structure. Category 5 outputs must not be chosen as policy constants.

“Can justify without outcomes” means a prospective rationale is possible, not that feasibility, risk or statistical precision has been demonstrated. None of this audit accesses market rules or scientific observations. No bounded alternatives are selected.

## Main findings

- **Most numerical values have no unique derivation.** P0 explicitly proposed administrative budgets and support thresholds. It contains no evidence that 93 days, 10,000 conditioning, 5 seconds, eta=.10, 20-session holding, 500 events or 504 validation sessions are uniquely required.
- **Operational rules can alter economics.** Quote age, dispatch and confirmation deadlines, lot comparisons, liquidity floors, T1 gates and reservation limits change the admitted/failed population, duration and costs. They cannot be dismissed as harmless engineering defaults.
- **Mathematics and implementation tolerance differ.** M1 equality/rank conditions are structural. A condition ceiling, floating-point tolerance and lot arithmetic comparison are numerical policies. A numerical check cannot authorize economic mismatch or broker-invalid fractions.
- **The same number has unrelated roles.** Separate model H126 from T1 126; daily model refresh from proposed daily auxiliary refresh; 20-session holding from 20-session embargo/support/blocks; pooled 500 events from 500 per validation group; abnormality .05 from familywise testing .05.
- **State boundaries and raw pooling interact subtly.** Changing eta can repartition states without changing the overall raw gross sample mean for the SAME complete event pool. But state-support gates, X labeling and cost/path assumptions can then change availability/economics. Holding cap or exit timeout changes the actual policy and paths directly.
- **Support is not proof of precision.** Kish weight support is not independent tail sample size; a fixed 20-session block does not establish independence; rare-state minima can make P1 unavailable. No observed shortage authorizes relaxing a constant.
- **Some constants are mechanically linked.** Six T1 blocks plus six leftovers follow 126 and 20; seven fitted snapshots follow six forward blocks plus one final fit; 10001 follows 10000 bootstrap replicates plus one. Linked numbers should not become separate micro-decisions.
- **Some engineering details remain underspecified even with numbers.** Condition-number norm/SVD rank precision, lot representation, and the method for any descriptive 95% interval must be specified before implementation. This audit identifies those dependencies rather than selecting hidden defaults.
- **No new constant is frozen here.** The next decision can approve a coherent bundle of policy/statistical values and their linked conventions, preserving all approved structure. Neither outcome-based numerical search nor automatic fallback is permitted.

## Detailed constant inventory

### A01. Model residual scale

**Source:** ancestry; §§3,11–12. **Exact source value:** 126 qualified prior observations; daily strictly-prior refresh. **Category 4. Decision status:** No—already approved.

**Why it exists / authority:** Approved dispersion/refresh design, not a mathematical minimum.

**Estimand and economics versus robustness:** Signal definition and historical ranking; economic admissions change if altered.

**Can it be justified without outcome data?** Already justified ex ante and explicitly approved; no new outcome justification is needed.

**Bounded alternatives, not selected:** None in this action; retain approved H126.

### A02. MAD multiplier

**Source:** scale approval (inherited). **Exact source value:** 1.4826. **Category 4. Decision status:** No—already approved.

**Why it exists / authority:** Inherited scale convention; not a Gaussian significance law or mathematical necessity.

**Estimand and economics versus robustness:** Changes z units; a consistently rescaled empirical reference may cancel a common multiplier, but inconsistent rescaling does not.

**Can it be justified without outcome data?** A convention can be fixed without outcomes; it does not establish predictive uncertainty.

**Bounded alternatives, not selected:** None; not reopened.

### A03. Model abnormality tail

**Source:** §§11–12. **Exact source value:** alpha=0.05; quantile=0.95; inclusive >=; two-sided absolute z. **Category 3. Decision status:** No—already approved.

**Why it exists / authority:** Approved rarity/materiality choice; 0.95=1−0.05 is derived, not an independent choice.

**Estimand and economics versus robustness:** Direct change to scientific discovery population if alpha/inequality changes.

**Can it be justified without outcome data?** Independent rarity rationale; no claim of 5% false positives or exactly 5% selected mass.

**Bounded alternatives, not selected:** None; no alternative alpha grid.

### A04. Reference estimator/direction balancing

**Source:** §11. **Exact source value:** 6 estimators; 5 groups; 2 ordered directions; factors 1/5, 1/2 and 1/2 inside C/L; weights sum 1. **Category 3. Decision status:** No—approved hierarchy.

**Why it exists / authority:** Approved equal-influence policy; factors follow group counts, not a universal statistical optimum.

**Estimand and economics versus robustness:** Changes reference distribution/threshold if weighting changes; ordered direction is not z sign.

**Can it be justified without outcome data?** Equal influence/duplicate treatment are defensible prospectively; approval predates P0.

**Bounded alternatives, not selected:** None to approved hierarchy; cell support and within-date weights remain separate.

### A05. Non-selecting scale robustness

**Source:** §12. **Exact source value:** 2 specifications: H252 MAD and H126 SD. **Category 4. Decision status:** No—already approved specifications.

**Why it exists / authority:** Previously approved diagnostic horizons/estimators.

**Estimand and economics versus robustness:** Reporting only if genuinely non-selecting; replacing the primary would change discovery.

**Can it be justified without outcome data?** Fixed independent diagnostic contrast; no outcomes required to specify it.

**Bounded alternatives, not selected:** No new robustness specs or primary substitution.

### A06. Mature outcome count

**Source:** §§4,10. **Exact source value:** 5: F/P/N/A/X; separate censor/unavailable status. **Category 3. Decision status:** No—structural approval.

**Why it exists / authority:** Approved scenario taxonomy, not a theorem selecting five states.

**Estimand and economics versus robustness:** Structural payoff decomposition; detailed boundaries can change labels and estimates.

**Can it be justified without outcome data?** Researcher approved; boundaries remain audited below.

**Bounded alternatives, not selected:** No additional state or forced assignment of unknown outcomes.

### A07. Algebraic target/sign/probability boundaries

**Source:** §§3–4,7,10. **Exact source value:** sign ±1; finite sign products >0; target b=1 / signed remainder<=0; positive K,L,scale; probabilities in [0,1], sum 1; N_r>0 to form a raw state mean. **Category 2. Decision status:** No—identities/approved semantics.

**Why it exists / authority:** Units, orientation, full-target definition and denominators require these identities/inequalities conditional on approved architecture.

**Estimand and economics versus robustness:** Changing them changes definitions, not operational robustness; 20 state observations is NOT implied by N_r>0.

**Can it be justified without outcome data?** Pure algebra and approved semantics; no observations needed.

**Bounded alternatives, not selected:** None; no numerical floor or invented mean for empty states.

### A08. No rescue/search additions

**Source:** §§7,10,12,15. **Exact source value:** 0 strategy fallbacks, outcome-selected rescues or flexible-ML extensions; 0 entry-completion chase. **Category 3. Decision status:** No—approved restrictions.

**Why it exists / authority:** Researcher governance and execution restrictions, not mathematical impossibility.

**Estimand and economics versus robustness:** Protects the scientific/execution procedure from adaptive changes.

**Can it be justified without outcome data?** Explicit present/prior approval; no outcome rationale needed.

**Bounded alternatives, not selected:** None; zero fallback is not permission to set missing risks/costs to zero.

### B01. Holdings publication age

**Source:** §1.1. **Exact source value:** <=93 calendar days. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Proxy disclosure freshness budget; no institutional mandate of 93 was evidenced.

**Estimand and economics versus robustness:** Changes proxy eligibility and opportunity population, not merely software robustness.

**Can it be justified without outcome data?** Can be proposed without outcomes; cannot call it an exchange/publication requirement without evidence.

**Bounded alternatives, not selected:** Keep 93 or tie eligibility to the verified disclosure cycle plus a fixed preregistered delay.

### B02. Industry holdings purity

**Source:** §1.1. **Exact source value:** >=95% of disclosed equity; <=5% equity leakage. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Approximation budget for a taxonomy-compatible fund.

**Estimand and economics versus robustness:** Changes tradable exposure/basis risk and eligible proxies; cash is outside this equity denominator.

**Can it be justified without outcome data?** Ex-ante tolerance is possible; no proof 95% gives acceptable tracking.

**Bounded alternatives, not selected:** 95% or 100%; neither selected, and strict industry qualification remains.

### B03. Proxy age floor

**Source:** §1.1. **Exact source value:** 252 prior scheduled common sessions. **Category 3. Decision status:** Yes.

**Why it exists / authority:** History availability floor, not an institutional fund-age rule.

**Estimand and economics versus robustness:** Changes proxy universe and early coverage; may bind differently from exposure/T1 history.

**Can it be justified without outcome data?** Can set a minimum prospectively; sufficiency must reflect nested histories, not just age.

**Bounded alternatives, not selected:** 252 or a deterministic minimum derived from the ultimately approved nested exposure/tracking histories.

### B04. Turnover history/support

**Source:** §1.1. **Exact source value:** 60 scheduled sessions; >=57 positive-turnover qualified sessions. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Administrative tradability screen (57/60 implies 95% count coverage).

**Estimand and economics versus robustness:** Changes eligible funds and economics; not proof of IOC fillability.

**Can it be justified without outcome data?** Can define without outcomes; counts are not justified by a formal precision calculation.

**Bounded alternatives, not selected:** 60/57 or 60/60; do not silently compress missing dates.

### B05. Liquidity value floor

**Source:** §1.1. **Exact source value:** Median traded value >=CNY 20,000,000/day. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Fixed value screen intended to avoid illiquid proxy slots.

**Estimand and economics versus robustness:** Currency/size-sensitive universe restriction; does not establish depth at entry.

**Can it be justified without outcome data?** Can be a capacity policy but no market-mandated floor or measured sufficiency is shown.

**Bounded alternatives, not selected:** Fixed CNY 20m or a preregistered size-linked participation rule; latter needs explicit rule approval.

### B06. Registry/learned-component refresh

**Source:** §§1,9–12. **Exact source value:** Every 6 months in development; 1 registry lock/final learned-parameter freeze during validation. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Administrative update/no-learning schedule.

**Estimand and economics versus robustness:** Changes available hedge identities, forecasts, threshold vintages and economic decisions.

**Can it be justified without outcome data?** PIT and non-adaptation justify a schedule, not uniquely six months.

**Bounded alternatives, not selected:** Semiannual or annual; select before access, not via fit/PnL.

### B07. Auxiliary history and aligned support

**Source:** §1.2. **Exact source value:** 252 scheduled sessions; >=240 aligned rows; end t−1. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Bias/stability/recency design with missing-row allowance; exact counts not mathematically forced.

**Estimand and economics versus robustness:** Changes B,A,h,xi,Target B, T1 and executable basket; high economic sensitivity.

**Can it be justified without outcome data?** The trade-off can be reasoned about ex ante; no validated optimality/precision claim.

**Bounded alternatives, not selected:** 252/240 or 126/120; one common rule only, not a two-model development search.

### B08. Regression support margin

**Source:** §1.2. **Exact source value:** N>=p+20, p includes intercept. **Category 4. Decision status:** Yes.

**Why it exists / authority:** An additional degrees-of-freedom margin; full-rank estimation alone does not require +20.

**Estimand and economics versus robustness:** Changes eligibility; no guarantee of stable estimates or prediction quality.

**Can it be justified without outcome data?** Can be preregistered under stated precision assumptions; none derives the value 20 here.

**Bounded alternatives, not selected:** p+20 or a specified ex-ante error/precision rule; no outcome-selected minimum.

### B09. Auxiliary/T1/drift refresh

**Source:** §§1–2. **Exact source value:** Daily; prior data through t−1; daily ongoing hard-budget monitoring. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Proposed freshness/operational frequency; strict PIT is mandatory but daily auxiliary refresh is not.

**Estimand and economics versus robustness:** New hedge targets and qualification-driven X exits; can alter strategy economics.

**Can it be justified without outcome data?** Can fix a cadence without outcomes; unlike model sigma daily refresh this is not automatically approved.

**Bounded alternatives, not selected:** Daily or weekly auxiliary refresh; retain strict PIT and separately specify monitoring.

### B10. Unselected EWLS half-life

**Source:** §1.2. **Exact source value:** 63 sessions. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Recency weighting parameter in the sole compared alternative, not the selected common estimator.

**Estimand and economics versus robustness:** Would change exposure geometry/target if adopted; no effect while inactive.

**Can it be justified without outcome data?** A design comparison can be made without fitting; value is not mathematically preferred.

**Bounded alternatives, not selected:** Leave EWLS inactive; no alternative-fit authority created.

### B11. Rank/finite-state conditions

**Source:** §1.2. **Exact source value:** Finite inputs; positive predictor variance; full column rank of OLS design and full row rank of A for approved M1 formula. **Category 2. Decision status:** No—mathematical/approved M1 prerequisite.

**Why it exists / authority:** Conditional algebraic existence/identification requirements; the approved inverse formula requires its rank conditions.

**Estimand and economics versus robustness:** Determines existence; rank deficiency cannot be fixed by declaring zero coefficients.

**Can it be justified without outcome data?** Algebraic justification; no empirical rank assessed.

**Bounded alternatives, not selected:** No ridge/drop-factor rescue; numerical rank detection still needs engineering specification.

### B12. Condition-number ceiling

**Source:** §1.2. **Exact source value:** <=10,000 for standardized design; <=10,000 for unit-column-normalized A. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Numerical stability acceptance policy, distinct from exact rank.

**Estimand and economics versus robustness:** May screen many events and alter economic coverage; below-bound changes in a well-conditioned solve are operational.

**Can it be justified without outcome data?** Can motivate error budgets before outcome data, but 10,000 is not universal or guaranteed; norm/SVD convention must be explicit.

**Bounded alternatives, not selected:** 10^4 or 10^6, with the same declared scaling and precision-error rationale; no auto-relaxation.

### B13. M1 residual check and offset

**Source:** §1.2. **Exact source value:** ||Ah−gamma||inf/(1+||gamma||inf)<=10^-10; offset 1. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Floating-point acceptance/scale convention for exact declared matching; neither 1 nor 10^-10 is mathematically forced.

**Estimand and economics versus robustness:** Operational if just arithmetic error; economic if used to admit materially unmatched baskets.

**Can it be justified without outcome data?** Can use forward/backward error analysis without outcomes; exact M1 identity remains mandatory.

**Bounded alternatives, not selected:** 10^-10 or a machine-precision/dimension-based error bound fixed before use.

### B14. Exact-share arithmetic comparison

**Source:** §5. **Exact source value:** 10^-10 relative; no economic rounding allowance. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Proposed numerical equality test, not an exchange lot size or T1 tolerance.

**Estimand and economics versus robustness:** Changing a numerical comparison may change feasibility; permitting actual rounding would change the basket.

**Can it be justified without outcome data?** Can justify arithmetic tolerance from representations; broker lot rules must be evidenced separately.

**Bounded alternatives, not selected:** Strict rational/lot representability or documented machine-error comparison; do not convert to economic rounding tolerance.

### C01. T1 lookback and completeness

**Source:** §2. **Exact source value:** 126 scheduled sessions; all 126 qualified. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Tracking-history/support design; NOT the approved 126 qualified residual-scale observations.

**Estimand and economics versus robustness:** Filters hedges, hence economic population; scheduled-window completeness differs from model-scale qualified-date history.

**Can it be justified without outcome data?** Can be chosen prospectively; matching the model number does not supply justification.

**Bounded alternatives, not selected:** 126/126 or 252/252; reject missing support rather than backfill.

### C02. Holding tracking horizons/block geometry

**Source:** §2. **Exact source value:** h=1,...,20; 6 non-overlapping 20-session blocks; 6 leftover sessions. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Path-risk horizon choice; block/remainder counts are arithmetic once 126 and 20 are fixed.

**Estimand and economics versus robustness:** Hard 20-session path test affects qualification; reporting shorter h alone does not change trades.

**Can it be justified without outcome data?** Geometry is derivable; statistical adequacy of six blocks is not guaranteed.

**Bounded alternatives, not selected:** Tie h to the eventual holding cap; recompute floor(H/h) and remainder, do not independently tune counts.

### C03. Residual-exposure budget

**Source:** §2. **Exact source value:** E_ell<=0.02. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Absolute exposure tolerance per signal gross; separate from M1 equation error.

**Estimand and economics versus robustness:** Can filter execution and trigger X; under valid exact M1 it may be redundant, not authority for 2% matching slack.

**Can it be justified without outcome data?** Risk preference can be stated without outcomes; no measured neutrality guarantee.

**Bounded alternatives, not selected:** Retain 0.02 as a separate guard or treat it as a reported diagnostic while preserving exact M1; requires decision.

### C04. Signed tracking-bias budget

**Source:** §2. **Exact source value:** abs(mean x)<=0.0002 =2 bp/day. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Tolerance for systematic implementation tracking per signal gross.

**Estimand and economics versus robustness:** Changes hedge admission and qualification-loss exits.

**Can it be justified without outcome data?** Risk-budget justification possible; the exact 2 bp is not data-derived or mandatory.

**Bounded alternatives, not selected:** 2 bp or 1 bp, chosen ex ante; no support-driven relaxation.

### C05. RMS tracking budget

**Source:** §2. **Exact source value:** RMS x<=0.001 =10 bp/day. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Absolute variability tolerance.

**Estimand and economics versus robustness:** Changes tradable sample and X exits, not just reporting precision.

**Can it be justified without outcome data?** Can set a risk budget without S3 outcomes; no empirical feasibility asserted.

**Bounded alternatives, not selected:** 10 bp or 5 bp prospectively.

### C06. Maximum daily tracking budget

**Source:** §2. **Exact source value:** max abs(x)<=0.005 =50 bp/day. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Historical extreme-error screen, not a bound on future maxima.

**Estimand and economics versus robustness:** Admission sensitive to sample length/extreme observation; changes economics.

**Can it be justified without outcome data?** Can state a loss/error budget; realized maximum frequency cannot be guaranteed.

**Bounded alternatives, not selected:** 50 bp or 25 bp ex ante; do not tune after seeing path maxima.

### C07. Maximum 20-session tracking budget

**Source:** §2. **Exact source value:** max abs(J_20)<=0.01 =100 bp over 20 sessions. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Cumulative cash-flow tracking budget.

**Estimand and economics versus robustness:** Changes qualified baskets/exits; not equivalent to daily RMS times sqrt(20).

**Can it be justified without outcome data?** Risk-based statement possible without outcomes; horizon dependence must be acknowledged.

**Bounded alternatives, not selected:** 100 bp or 50 bp at the same horizon; changing the cap requires explicit alignment.

### C08. Exposure-drift budget

**Source:** §2. **Exact source value:** E_d<=0.05. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Maximum replayed residual exposure per signal gross.

**Estimand and economics versus robustness:** Changes admission and exceptional exits; not permission to rebalance.

**Can it be justified without outcome data?** Can set ex ante, not a theorem about exposure uncertainty.

**Bounded alternatives, not selected:** 0.05 or 0.025; both remain proposed.

### C09. Tracking tail diagnostic

**Source:** §2. **Exact source value:** Q_0.95(abs(x)). **Category 4. Decision status:** Yes.

**Why it exists / authority:** Descriptive tail summary, not the approved model-z quantile.

**Estimand and economics versus robustness:** Reporting only while not a hard gate.

**Can it be justified without outcome data?** Conventional quantile can be specified without outcomes.

**Bounded alternatives, not selected:** 0.95 or 0.99 for reporting only; not a strategy threshold.

### C10. Tracking confidence/cluster reporting

**Source:** §2. **Exact source value:** 95% descriptive intervals; 20-session blocks, only 6 blocks in current history. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Uncertainty/reporting convention; six blocks do not establish reliable asymptotic coverage.

**Estimand and economics versus robustness:** Inference/reporting only unless misused for qualification.

**Can it be justified without outcome data?** Confidence level can be preregistered; coverage depends on method/dependence, not just 95%.

**Bounded alternatives, not selected:** 95% with explicitly justified method/support, or block values/range only (already cautioned in P0).

### D01. Opening observation window

**Source:** §3. **Exact source value:** First synchronized snapshot in [u+60s,u+120s]. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Defines the actionable origin reference; not a market-mandated auction rule.

**Estimand and economics versus robustness:** Directly changes D_u, sign survival, fills and economic estimand.

**Can it be justified without outcome data?** Can choose a deterministic observation delay, but 60–120s is only policy absent latency/session evidence.

**Bounded alternatives, not selected:** 60–120s or 30–60s; choose once prospectively.

### D02. Quote age and cross-leg skew

**Source:** §3. **Exact source value:** Each age<=1s; cross-leg timestamp skew<=1s. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Proposed synchronization/staleness budget, not mathematical simultaneity.

**Estimand and economics versus robustness:** Operational risk control that changes admitted population and measured entry target.

**Can it be justified without outcome data?** Can be tied to timestamp resolution/latency contracts without strategy outcomes; no such contract verified.

**Bounded alternatives, not selected:** 1s or a tighter 0.5s subject to evidenced feed capability.

### D03. Snapshot-to-submit and batch dispatch

**Source:** §§3,7. **Exact source value:** <=1s snapshot-to-submit; <=1s basket dispatch. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Computational/order synchronization deadline; distinct two tests.

**Estimand and economics versus robustness:** Changes feasibility, latency and partial-entry exposure; not merely software speed.

**Can it be justified without outcome data?** Can be an engineering service-level policy without PnL; capability unverified.

**Bounded alternatives, not selected:** 1s or a verified contractual latency bound chosen before access.

### D04. IOC confirmation deadlines

**Source:** §§7–8. **Exact source value:** 5s from first child submission for entry and normal liquidation. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Local confirmation/failure timeout, NOT time an IOC order rests at venue.

**Estimand and economics versus robustness:** Entry failures and X exit labels/carry can change; economic sensitivity.

**Can it be justified without outcome data?** Could be set from broker acknowledgement guarantees independent of outcomes; no universal 5s rule.

**Bounded alternatives, not selected:** 5s or an evidence-bound acknowledgement deadline; distinguish it from immediate IOC cancellation.

### D05. Liquidation retry spacing

**Source:** §7. **Exact source value:** >=1s until first fresh lawful quote. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Deterministic throttle between risk-reducing attempts.

**Estimand and economics versus robustness:** May change liquidation duration, fees and exposure; operational AND economic.

**Can it be justified without outcome data?** Can reflect API/rate limits without outcomes; must not supersede a binding deadline.

**Bounded alternatives, not selected:** 1s or a qualified broker throttle rule; no discretionary waiting.

### D06. Monitoring/count convention

**Source:** §§3–4. **Exact source value:** 1 close per common session; entry session counts as 1; next lawful joint opening for normal liquidation. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Temporal event definition; neither daily monitoring nor count origin is forced by Target B.

**Estimand and economics versus robustness:** Changes hit/cap labels and liquidation delay/payoffs.

**Can it be justified without outcome data?** Can be fixed without outcomes; it is strategy policy, not just documentation.

**Bounded alternatives, not selected:** Retain close-only/entry-as-1 or change count convention explicitly before access; no retrospective intraday hits.

### D07. Holding cap

**Source:** §4. **Exact source value:** 20 common scheduled sessions. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Maximum ordinary holding-trigger horizon, not guaranteed settlement duration.

**Estimand and economics versus robustness:** High: changes payoff, borrow/funding, states and economic hypothesis horizon.

**Can it be justified without outcome data?** Economic horizon rationale possible ex ante; mathematics does not select 20.

**Bounded alternatives, not selected:** 10 or 20 sessions; no empirical horizon optimization.

### D08. Non-resolution boundary

**Source:** §4. **Exact source value:** eta=0.10; ±10% of remaining target; P eta<b<1, N abs(b)<=eta, A b<−eta. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Defines approximately unchanged; mathematical domain 0<=eta<1 does not select 0.10.

**Estimand and economics versus robustness:** Changes labels and state cost/duration estimates. For same complete fixed raw P1 pool, repartition alone leaves overall gross sample mean unchanged; support gates can still change economics.

**Can it be justified without outcome data?** Can be a materiality convention without outcomes, not a uniquely statistical value.

**Bounded alternatives, not selected:** eta=0.05 or 0.10 ex ante; no optimized labeling.

### E01. Equal capital sleeves

**Source:** §5. **Exact source value:** 6 sleeves; each 1/6 initial NAV; daily NAV updates. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Six models do not mathematically require six equally funded trading books.

**Estimand and economics versus robustness:** Capital/fill competition, costs and comparability change; more than reporting.

**Can it be justified without outcome data?** Equal treatment can justify policy without performance data.

**Bounded alternatives, not selected:** Equal sleeves or a preregistered common-capital comparison design; latter changes portfolio policy and requires explicit approval.

### E02. Raw attempt gross

**Source:** §5. **Exact source value:** K_raw=0.01 V_c =1% sleeve NAV. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Risk/capacity allocation choice.

**Estimand and economics versus robustness:** High through size-dependent fees, lots, impact, borrowing and resource competition.

**Can it be justified without outcome data?** Can express risk budget without PnL; not scale-invariant economics.

**Bounded alternatives, not selected:** 0.5% or 1%; no optimized sizing.

### E03. Total gross cap

**Source:** §5. **Exact source value:** 100% sleeve NAV and 100% portfolio NAV. **Category 3. Decision status:** Yes.

**Why it exists / authority:** No-leverage gross budget as proposed; not evidence of legal margin constraints.

**Estimand and economics versus robustness:** Changes admission/resources and cap-trigger exits.

**Can it be justified without outcome data?** Can be an ex-ante risk policy; contract limits may be stricter.

**Bounded alternatives, not selected:** 50% or 100% total gross; never override binding broker limits.

### E04. Physical-security gross cap

**Source:** §5. **Exact source value:** 10% sleeve NAV and 10% total portfolio NAV. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Concentration control on gross commitments.

**Estimand and economics versus robustness:** Changes overlapping-basket eligibility/exit behavior.

**Can it be justified without outcome data?** Risk preference can be set without outcomes; legal limits separately evidenced.

**Bounded alternatives, not selected:** 5% or 10%.

### E05. Absolute net currency cap

**Source:** §5. **Exact source value:** 10% sleeve NAV and 10% portfolio NAV. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Net-notional budget; not factor neutrality.

**Estimand and economics versus robustness:** Changes eligible basket combinations; dollar neutrality is not guaranteed by M1.

**Can it be justified without outcome data?** Can be chosen ex ante; not an algebraic consequence of hedge matching.

**Bounded alternatives, not selected:** 5% or 10%; do not call either market-neutral by definition.

### E06. Turnover measure for sizing/impact

**Source:** §§5,9. **Exact source value:** Prior 20 qualified sessions; all 20 required; median traded value. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Liquidity estimator/history convention, distinct from 60-session fund eligibility.

**Estimand and economics versus robustness:** Changes feasible order size and cost estimates.

**Can it be justified without outcome data?** Recency/robustness argument possible, not mandatory 20-day liquidity law.

**Bounded alternatives, not selected:** 20/20 or 60/60; one common declared method.

### E07. Participation cap

**Source:** §5. **Exact source value:** Leg value<=0.1% of prior ADV20 median value. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Capacity/impact risk budget.

**Estimand and economics versus robustness:** Direct size/economic feasibility effect.

**Can it be justified without outcome data?** Can be set from risk mandate without PnL; no measured safe-impact guarantee.

**Bounded alternatives, not selected:** 0.05% or 0.1%.

### E08. Displayed-depth cap

**Source:** §5. **Exact source value:** Order quantity<=10% executable displayed depth. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Liquidity consumption budget; displayed depth is not a guaranteed fill.

**Estimand and economics versus robustness:** Changes execution eligibility and failed attempts.

**Can it be justified without outcome data?** Can be conservative policy; cannot establish counterfactual fill/impact from rule alone.

**Bounded alternatives, not selected:** 5% or 10%.

### E09. Carry reserve horizon

**Source:** §§5–6. **Exact source value:** 20-session/calendar-equivalent carry at known contractual maxima. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Resource-reservation horizon tied by proposal to cap, not lender-guaranteed duration.

**Estimand and economics versus robustness:** May block entries or cause margin exits; exceptional obligations can outlast it.

**Can it be justified without outcome data?** Can tie to a chosen risk horizon; quoted rate ceilings themselves are category 1.

**Bounded alternatives, not selected:** Cap-linked reserve or cap plus a preregistered settlement-delay allowance; not a bounded-loss promise.

### E10. Collision and sizing-pass counts

**Source:** §§5,7–8. **Exact source value:** Max 1 active/pending attempt per unordered pair per sleeve; 1 common-rho sizing pass; 0 redistribution/retry after rejection. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Anti-stacking/collision/allocation convention beyond immutable K.

**Estimand and economics versus robustness:** Changes event population and unused capital; not merely bookkeeping.

**Can it be justified without outcome data?** Can avoid endogenous prioritization prospectively; no unique mathematical rule.

**Bounded alternatives, not selected:** Retain one-pass nonstacking or specify a different collision/allocation rule before access; no automatic alternative.

### E11. Allocation shrinkage range

**Source:** §5. **Exact source value:** rho in [0,1], largest feasible common rho. **Category 3. Decision status:** Yes.

**Why it exists / authority:** No increase above raw allocation is a sizing policy; rho's realized value is a future mechanical output.

**Estimand and economics versus robustness:** Economic sizing/admission sensitivity.

**Can it be justified without outcome data?** Can define before outcomes; math solves constraints conditional on this chosen policy.

**Bounded alternatives, not selected:** Retain common shrinkage; a different allocation objective requires a policy decision, not numeric tuning.

### E12. Development reference capital

**Source:** §10. **Exact source value:** CNY 1,000,000 per estimator; CNY 6,000,000 total implied. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Nominal simulation scale, not a mathematical unit cancellation under nonlinear costs/lots.

**Estimand and economics versus robustness:** Economic/support sensitivity through fees, impact and exact-share feasibility.

**Can it be justified without outcome data?** Can choose operational scale before data; not a claim capital is available.

**Bounded alternatives, not selected:** CNY 0.5m or 1m per estimator, bound prospectively.

### F01. Execution cost functional constants

**Source:** §9.2. **Exact source value:** 2 coefficients (a,b); exponent 1/2 on participation; a,b>=0. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Low-dimensional NNLS model specification; neither square-root impact nor nonnegative intercept is mathematically required.

**Estimand and economics versus robustness:** Changes costs/E1 and executable economic estimand; realized negative price improvements remain recorded.

**Can it be justified without outcome data?** A parsimonious hypothesis can be stated ex ante; predictive adequacy is unverified.

**Bounded alternatives, not selected:** Keep proposed form or defer it pending independent execution-model rationale; no alternate fits authorized.

### F02. Execution-fit support

**Source:** §9.2. **Exact source value:** 200 parent orders; 20 distinct sessions; 20 orders per current instrument/side. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Coverage/stability minima, not a power or error guarantee.

**Estimand and economics versus robustness:** Cost availability and admissions change.

**Can it be justified without outcome data?** Can set under stated precision/dependence assumptions; no derivation of these counts was supplied.

**Bounded alternatives, not selected:** Fixed proposed minima or a preregistered precision criterion; not lower-until-estimable.

### F03. Cost extrapolation boundary

**Source:** §9.2. **Exact source value:** 0 extrapolation beyond observed instrument/side participation min/max. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Domain-of-support policy; endpoints are future measured quantities.

**Estimand and economics versus robustness:** Can make costs/economics unavailable; observed min/max do not prove dense support.

**Can it be justified without outcome data?** Can prohibit extrapolation prospectively; does not validate interpolation.

**Bounded alternatives, not selected:** Keep no extrapolation; any extra neighborhood support rule requires explicit pre-access binding.

### F04. P1 cohort age

**Source:** §10. **Exact source value:** Submission at least 60 common sessions before fit origin. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Age/maturity eligibility convention, distinct from 20-session holding cap.

**Estimand and economics versus robustness:** Changes training population and forecast availability; not guaranteed censor elimination.

**Can it be justified without outcome data?** Can align to anticipated information/settlement delays without outcomes; actual maturity still required.

**Bounded alternatives, not selected:** 60 sessions or a fully preregistered event-maturity inclusion scheme that handles censoring without survivor selection.

### F05. P1/cost availability embargo

**Source:** §§9.3,10,12. **Exact source value:** Outcome/settlement available at least 20 common sessions before fit. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Leakage/dependence buffer; actual non-overlap and timestamp restrictions are distinct.

**Estimand and economics versus robustness:** Training sample and E1 forecasts change.

**Can it be justified without outcome data?** PIT ordering is necessary; a universal 20-session buffer is not.

**Bounded alternatives, not selected:** 20 sessions or a deterministic information/overlap-derived embargo; no retrospective leakage rescue.

### F06. Old-cohort censor tolerance

**Source:** §10. **Exact source value:** 0 unresolved/unobservable/unsettled old-cohort records before primary raw mean is qualified. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Conservative identification guard; raw all-attempt mean cannot assign unknown values, but global shutdown is a chosen policy.

**Estimand and economics versus robustness:** Potential whole-pool unavailability; very high support sensitivity.

**Can it be justified without outcome data?** Can justify avoidance of complete-case bias without outcomes; zero-tolerance is not the only possible inferential architecture.

**Bounded alternatives, not selected:** Retain guard; alternative censor estimators/bounds are outside this audit, not approved fallbacks.

### F07. P1 total/pair minima

**Source:** §10. **Exact source value:** N>=500 unique mature attempts; >=20 unordered pairs. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Amount/diversity design criteria; not effective sample size guarantees.

**Estimand and economics versus robustness:** Forecast availability/economic sample change.

**Can it be justified without outcome data?** Requires ex-ante precision/heterogeneity rationale to claim adequacy; no such derivation exists.

**Bounded alternatives, not selected:** Proposed fixed minima or an explicitly specified precision criterion before access.

### F08. P1 cluster support/length

**Source:** §10. **Exact source value:** >=20 non-overlapping origin clusters, each 20 sessions. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Dependence/diversity design; cluster count and length are separate choices.

**Estimand and economics versus robustness:** Qualification and uncertainty change; dependence may extend beyond block.

**Can it be justified without outcome data?** Can posit dependence scale prospectively; cannot claim independence from 20 sessions.

**Bounded alternatives, not selected:** Length 20 or 40 with separately justified minimum cluster count; no outcome-based selection.

### F09. P1 estimator-group support

**Source:** §10. **Exact source value:** >=50 attempts in each of 5 equation groups. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Comparability/coverage minimum, not equal-count weighting.

**Estimand and economics versus robustness:** Changes pool availability; does not make raw counts group-balanced.

**Can it be justified without outcome data?** Can define coverage prospectively; 50 has no demonstrated precision justification.

**Bounded alternatives, not selected:** 50 or 100 per group; no independently tuned per-model minima.

### F10. P1 state/substate support

**Source:** §10. **Exact source value:** >=20 each F/P/N/A, X_entry and admitted-X. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Six support cells within five mature states; rare-risk means are not set to zero.

**Estimand and economics versus robustness:** May prohibit most estimation if exceptional states sparse; labels/means unchanged but gate availability changes.

**Can it be justified without outcome data?** Rarity does not justify zero risk; exact 20 needs an independent precision rationale.

**Bounded alternatives, not selected:** 20 or a prespecified precision rule; no automatic smoothing/P3 or collapsing exceptional risks.

### F11. P1 signed support

**Source:** §10. **Exact source value:** >=20 attempts per signed orientation overall. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Coverage across long/short orientation; not equal-tail probability.

**Estimand and economics versus robustness:** Economic-support filter; raw pooled forecast remains common.

**Can it be justified without outcome data?** Can require prospective sign coverage; count alone not precision.

**Bounded alternatives, not selected:** 20 or 40, fixed across models.

### F12. Pool concentration ceilings

**Source:** §10. **Exact source value:** Each pair<=20% of N; each 20-session cluster<=20% of N. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Administrative concentration budget with statistical motivation.

**Estimand and economics versus robustness:** Changes which origins qualify, not the raw count formula.

**Can it be justified without outcome data?** Can be an ex-ante diversity preference; no guarantee of effective independence.

**Bounded alternatives, not selected:** 10% or 20%; no after-the-fact pair pruning.

### F13. Raw-pool numerical exclusions

**Source:** §10. **Exact source value:** 0 pseudocounts, shrinkage or winsorization; 1 common raw pool; C/L exact duplicate counted once. **Category 3. Decision status:** No new smoothing; detailed policy still pending.

**Why it exists / authority:** Raw arithmetic P1 and duplicate treatment; structural counts differ from support minima.

**Estimand and economics versus robustness:** Smoothing/trimming would change expected capture/risk; exact duplicate removal changes evidence count.

**Can it be justified without outcome data?** Approved raw P1 supports no silent smoothing; detailed dedup/event coding still needs conformance.

**Bounded alternatives, not selected:** No numerical rescue; detailed economic pooling rules not approved wholesale.

### G01. Reference complete-date support

**Source:** §11. **Exact source value:** >=60 complete pair-dates per block, both ordered directions/all 6 models. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Reference sampling/coverage threshold, not quantile mathematical existence.

**Estimand and economics versus robustness:** Changes reference population/z0/discovery while alpha stays fixed.

**Can it be justified without outcome data?** Can prescribe before outcomes; value 60 not derived from quantile precision.

**Bounded alternatives, not selected:** 60 or a preregistered quantile-precision/support requirement.

### G02. Reference pair count

**Source:** §11. **Exact source value:** >=10 complete pairs per block. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Cross-pair diversity minimum.

**Estimand and economics versus robustness:** Threshold/support/discovery changes.

**Can it be justified without outcome data?** Can be a diversity rule; no precision proof at 10.

**Bounded alternatives, not selected:** 10 or 20 complete pairs, selected prospectively.

### G03. Reference pair coverage

**Source:** §11. **Exact source value:** >=80% of PIT registered pairs qualify. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Administrative completeness threshold; not required by weighted quantile mathematics.

**Estimand and economics versus robustness:** Changes reference availability and potentially selected reference sample.

**Can it be justified without outcome data?** Can define coverage mandate without outcomes; not proof missingness is ignorable.

**Bounded alternatives, not selected:** 80% or 100%, with no silent group substitution.

### G04. Reference block count

**Source:** §11. **Exact source value:** >=2 completed half-year blocks. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Temporal coverage criterion, not necessary for algebraic quantile existence.

**Estimand and economics versus robustness:** Delays/changes available threshold; economic discovery affected.

**Can it be justified without outcome data?** Can require multiple periods ex ante; two periods do not establish stability.

**Bounded alternatives, not selected:** 2 or 4 completed blocks.

### G05. Kish weight-support floor

**Source:** §11. **Exact source value:** 1/sum(omega^2)>=1000. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Weight concentration diagnostic threshold, not independent observations or tail precision.

**Estimand and economics versus robustness:** Can block reference/strategy; no guarantee of 50 independent tail events.

**Can it be justified without outcome data?** Can justify a concentration rule; 1000 has no supplied power/error derivation.

**Bounded alternatives, not selected:** 1000 or a formal preregistered weighted-quantile precision criterion, no observed-support retuning.

### G06. Within-date reference weight

**Source:** §11. **Exact source value:** 1/n_b,p per qualified date; rational cell weights; 1/B and 1/P_b. **Category 3. Decision status:** Yes—date/support details; hierarchy already approved.

**Why it exists / authority:** Equal dates proposed; block/pair balance inherited. Denominators are mechanically counted.

**Estimand and economics versus robustness:** Date weighting can change z0; exact arithmetic representation mainly reproducibility.

**Can it be justified without outcome data?** Uniform dates can be stated ex ante; not forced by inverse CDF.

**Bounded alternatives, not selected:** Retain equal qualified dates or explicitly bind another measure before access; hierarchy unchanged.

### G07. Development dates and reference chronology

**Source:** §§11–12. **Exact source value:** 2015–2019 development proposed; 2015 warm-up; 2016 formation; reference 2016H1–2019H2; first possible cutoff before 2017H1. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Chosen temporal design, not authority to access or proof adequate warm-up.

**Estimand and economics versus robustness:** Changes fitted reference/forecasts and assessed development population.

**Can it be justified without outcome data?** Can respect known contamination and fix dates without outcomes; sufficiency still unknown.

**Bounded alternatives, not selected:** Retain calendar plan or defer access until a preregistered warm-up/support plan is approved; no automatic earlier/later access.

### G08. Fold/fit/search budget

**Source:** §12. **Exact source value:** 6 forward half-years 2017H1–2019H2; 1 final fit; <=7 component fits; 1 economic specification/pass; 2 existing scale-only diagnostics. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Finite research budget; 7 is derived from 6+1, not seven free model searches.

**Estimand and economics versus robustness:** Refit frequency changes predictions; budget controls adaptation and inference.

**Can it be justified without outcome data?** Finite budget can be fixed without outcomes; not a proof six blocks suffice.

**Bounded alternatives, not selected:** Retain six half-years or three annual blocks plus one final fit; neither executed.

### G09. Previously exposed calendar boundary

**Source:** §§12–13. **Exact source value:** 2020–2025 non-pristine; no automatic 2020+ completion; pre-freeze 2026 not presumed untouched; no 2013–2014 extension. **Category 3. Decision status:** No—history/authority constraint.

**Why it exists / authority:** Recorded access history and scope restriction, not an optimizable parameter.

**Estimand and economics versus robustness:** Changes permissible claims/data scope; cannot erase contamination by changing a date label.

**Can it be justified without outcome data?** Canonical ledger, not an outcome-based choice; no new access checked.

**Bounded alternatives, not selected:** No alternative making exposed data pristine; any future access remains separately authorized.

### H01. Future start boundary

**Source:** §13. **Exact source value:** First full common session strictly after T_freeze; session index 1; 0 partially observed pre-start validation sessions. **Category 3. Decision status:** No—prospective principle approved.

**Why it exists / authority:** Prospective no-access requirement, now structurally approved; exact operational start record must be immutable.

**Estimand and economics versus robustness:** Prevents contaminated validation; changing start after outcomes biases claims.

**Can it be justified without outcome data?** Can preregister before future data; T_freeze is a future recorded timestamp, not today's approval.

**Bounded alternatives, not selected:** No retroactive earlier start or outcome-selected restart.

### H02. Validation horizon/interim

**Source:** §13. **Exact source value:** 504 common sessions; 252-session operational-only interim/minimum interpretable horizon. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Duration/precision design; 252 is not inherently one market year or a statistical adequacy theorem.

**Estimand and economics versus robustness:** Observation horizon/inference change; stopping new entries at end also changes program economics.

**Can it be justified without outcome data?** Can set calendar budget ex ante; precision needs assumptions; no event counts observed.

**Bounded alternatives, not selected:** 504 or 252 total sessions, chosen before freeze; retain no outcome-dependent early stop.

### H03. Validation settlement follow-up

**Source:** §13. **Exact source value:** 60 common sessions after 504; no new entries. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Research observation budget, NOT a settlement deadline or legal release.

**Estimand and economics versus robustness:** Changes censoring/economic identifiability, not actual outstanding obligations.

**Can it be justified without outcome data?** Can fix follow-up budget without outcomes; legal obligations may outlast it.

**Bounded alternatives, not selected:** 60 or 120 sessions prospectively; no wait-until-favorable extension.

### H04. Validation inferential support

**Source:** §13. **Exact source value:** >=500 mature attempts, >=20 pairs and >=20 time clusters PER equation group. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Per-group inference threshold, distinct from pooled P1's 500 total.

**Estimand and economics versus robustness:** Reporting/testability; calendar unchanged even if counts fail.

**Can it be justified without outcome data?** Requires prospective precision/dependence rationale; counts alone no power guarantee.

**Bounded alternatives, not selected:** Fixed minima or a specified precision criterion; no event-count stopping/extension.

### H05. Bootstrap block length

**Source:** §13. **Exact source value:** 20 common-session moving blocks; paired resampling across candidates. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Dependence approximation, not forced by holding cap=20.

**Estimand and economics versus robustness:** Inference only if no selection/feedback; invalid choice can distort error rates.

**Can it be justified without outcome data?** Can posit a dependence horizon before outcomes; no claim arbitrary-memory validity.

**Bounded alternatives, not selected:** 20 or 40 sessions preregistered, or a fully specified independent dependence-based rule; none selected.

### H06. Bootstrap replication budget

**Source:** §13. **Exact source value:** 10,000 replicates. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Monte Carlo resolution/computational budget, not economic parameter.

**Estimand and economics versus robustness:** Inference numerical variability only; not underlying payoff estimand.

**Can it be justified without outcome data?** Computational precision can be justified without strategy outcomes.

**Bounded alternatives, not selected:** 10,000 or 50,000; no rerun until significance.

### H07. Bootstrap seed

**Source:** §13. **Exact source value:** 20260927. **Category 3. Decision status:** Yes.

**Why it exists / authority:** Reproducibility label, not a date-dependent scientific parameter.

**Estimand and economics versus robustness:** Only finite-simulation randomness; seed shopping would change inference.

**Can it be justified without outcome data?** Any preregistered seed is defensible without outcomes.

**Bounded alternatives, not selected:** Keep seed or a deterministic hash-derived seed fixed before validation; no multiple-seed selection.

### H08. Monte Carlo correction constants

**Source:** §13. **Exact source value:** (1+exceedances)/10001; denominator B+1 for B=10,000. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Plus-one p-value convention; 10001 is derived, not independently tunable.

**Estimand and economics versus robustness:** Inference discreteness only; no payoff change.

**Can it be justified without outcome data?** Can specify convention without outcomes; it does not establish bootstrap validity.

**Bounded alternatives, not selected:** Retain convention; if B is changed, denominator changes mechanically.

### H09. Confirmatory family/error level

**Source:** §13. **Exact source value:** 5 Holm hypothesis groups; equal 1/2 C/L-book influence if executions differ; familywise alpha=0.05; 1 one-sided final family. **Category 4. Decision status:** Yes.

**Why it exists / authority:** Inference/multiplicity policy; independent of approved reference-tail alpha=0.05.

**Estimand and economics versus robustness:** Claim sensitivity, not trade economics if strictly reporting-only.

**Can it be justified without outcome data?** Can preregister family/error budget; five groups reflect equation grouping but inferential target still needs approval.

**Bounded alternatives, not selected:** 5-group family at 0.05 or 0.01; no extra unadjusted discoveries or group dropping.

### I01. Institutional numeric inputs

**Source:** §§1,5–9,14. **Exact source value:** No literal values specified: tick/lot sizes, fees/taxes/minima, loan quantities/rates/day counts, margin/haircuts, credit, validity/recall/settlement deadlines, session times, distributions/split ratios. **Category 1. Decision status:** Evidence required; do not invent policy values.

**Why it exists / authority:** Actual instrument/account/venue terms must supply numbers; not designer-selected defaults.

**Estimand and economics versus robustness:** Directly affects executable basket/costs/obligations.

**Can it be justified without outcome data?** Needs qualified authoritative contractual evidence, not S3 outcome optimization; none accessed here.

**Bounded alternatives, not selected:** No substitute arbitrary values; missing mandatory evidence remains unavailable.

### I02. Future model/data outputs

**Source:** §§1–2,5,9–11. **Exact source value:** No selected numbers: B,A,h,xi,ell,tau; K/rho after allocation; a,b; pi_r,G_r,mhat,costs,durations; reference counts/weights and numerical z0. **Category 5. Decision status:** Authorize methods/access separately; values not selected.

**Why it exists / authority:** Mechanical outputs conditional on approved methods and qualified PIT data.

**Estimand and economics versus robustness:** Direct forecast/basket/economic sensitivity; not free policy knobs.

**Can it be justified without outcome data?** Methods may be justified ex ante; output values require separately authorized data and cannot be supplied now.

**Bounded alternatives, not selected:** No parametric z0, chosen exposures, zero missing costs or manually fitted probabilities.

### I03. Definition constants, not tuning knobs

**Source:** §§1–4,9–12. **Exact source value:** Midpoint/halfspread divisor 2; RMS power 2 and root 1/2; Brier power 2; accounting signs ±1; split reciprocal 1/a; indicator 0/1; t−1 lag notation. **Category 2. Decision status:** No—identities, subject to method approval.

**Why it exists / authority:** Arithmetic conditional on chosen definitions; square-root participation model is separately F01, not this row.

**Estimand and economics versus robustness:** Changing arithmetic breaks those definitions; choosing a different metric/benchmark is a separate policy change.

**Can it be justified without outcome data?** Algebraic justification; no empirical numerical estimate.

**Bounded alternatives, not selected:** No independent numeric alternatives within the same definition.

## Completeness and stop

The inventory covers all explicit numerical policy occurrences in source sections 1–15 and its repeated final table. Duplicate literals are not silently treated as one scientific binding. Category-1 fields have no supplied numeric values; category-5 outputs remain unestimated. Source labels/identifiers and algebraic notation are accounted for above rather than misclassified as free parameters.

No acquisition, scientific-data access, exposure/tracking/capture/cost estimation, numerical z0, implementation, calibration, backtest or PnL inspection. Frozen V1 and canonical mathematical architecture are unchanged. NEXT_ACTION remains NONE. Documentation checks are structural only; full PowerShell validators are unavailable, and data/core/result-reading validators are not run.

**S3 NUMERICAL PROTOCOL CONSTANTS / RESEARCHER DECISION REQUIRED**

| Constant | Proposed value | Category | Justification | Strategy sensitivity | Needs researcher decision? |
|---|---|---|---|---|---|
| A01 Model residual scale | 126 qualified prior observations; daily strictly-prior refresh | 4 | Statistical rationale; not validated | Discovery/population | No—already approved |
| A02 MAD multiplier | 1.4826 | 4 | Statistical rationale; not validated | Discovery/population | No—already approved |
| A03 Model abnormality tail | alpha=0.05; quantile=0.95; inclusive >=; two-sided absolute z | 3 | Ex-ante policy, not compelled | Discovery/population | No—already approved |
| A04 Reference estimator/direction balancing | 6 estimators; 5 groups; 2 ordered directions; factors 1/5, 1/2 and 1/2 inside C/L; weights sum 1 | 3 | Ex-ante policy, not compelled | Discovery/population | No—approved hierarchy |
| A05 Non-selecting scale robustness | 2 specifications: H252 MAD and H126 SD | 4 | Statistical rationale; not validated | Reporting/claims | No—already approved specifications |
| A06 Mature outcome count | 5: F/P/N/A/X; separate censor/unavailable status | 3 | Ex-ante policy, not compelled | Labels + support | No—structural approval |
| A07 Algebraic target/sign/probability boundaries | 0, ±1, 1; positive denominators; probability simplex | 2 | Conditional algebra/identity | Existence/definition | No—identities/approved semantics |
| A08 No rescue/search additions | 0 fallback/rescue/ML/completion chase | 3 | Ex-ante policy, not compelled | Eligibility/economics | No—approved restrictions |
| B01 Holdings publication age | <=93 calendar days | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B02 Industry holdings purity | >=95% of disclosed equity; <=5% equity leakage | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B03 Proxy age floor | 252 prior scheduled common sessions | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B04 Turnover history/support | 60 scheduled sessions; >=57 positive-turnover qualified sessions | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B05 Liquidity value floor | Median traded value >=CNY 20,000,000/day | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B06 Registry/learned-component refresh | Every 6 months in development; 1 registry lock/final learned-parameter freeze during validation | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B07 Auxiliary history and aligned support | 252 sessions; >=240 rows; t−1 | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| B08 Regression support margin | N>=p+20, p includes intercept | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| B09 Auxiliary/T1/drift refresh | Daily; prior data through t−1; daily ongoing hard-budget monitoring | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| B10 Unselected EWLS half-life | 63 sessions | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| B11 Rank/finite-state conditions | Finite; positive variance; required full rank | 2 | Conditional algebra/identity | Existence/definition | No—mathematical/approved M1 prerequisite |
| B12 Condition-number ceiling | 10,000 (two matrix checks) | 3 | Ex-ante policy, not compelled | Numerics + eligibility | Yes—unfrozen |
| B13 M1 residual check and offset | 10^-10; normalization offset 1 | 3 | Ex-ante policy, not compelled | Numerics + eligibility | Yes—unfrozen |
| B14 Exact-share arithmetic comparison | 10^-10 relative; no economic rounding allowance | 3 | Ex-ante policy, not compelled | Numerics + eligibility | Yes—unfrozen |
| C01 T1 lookback and completeness | 126 scheduled sessions; all 126 qualified | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| C02 Holding tracking horizons/block geometry | h=1…20; 6×20 blocks; 6 leftovers | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| C03 Residual-exposure budget | E_ell<=0.02 | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| C04 Signed tracking-bias budget | abs(mean x)<=0.0002 =2 bp/day | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| C05 RMS tracking budget | RMS x<=0.001 =10 bp/day | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| C06 Maximum daily tracking budget | max abs(x)<=0.005 =50 bp/day | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| C07 Maximum 20-session tracking budget | max abs(J_20)<=0.01 =100 bp over 20 sessions | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| C08 Exposure-drift budget | E_d<=0.05 | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| C09 Tracking tail diagnostic | Q_0.95(abs(x)) | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| C10 Tracking confidence/cluster reporting | 95% descriptive intervals; 20-session blocks, only 6 blocks in current history | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| D01 Opening observation window | First synchronized snapshot in [u+60s,u+120s] | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D02 Quote age and cross-leg skew | Age 1s; skew 1s | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D03 Snapshot-to-submit and batch dispatch | Submit 1s; batch dispatch 1s | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D04 IOC confirmation deadlines | 5s from first child submission for entry and normal liquidation | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D05 Liquidation retry spacing | >=1s until first fresh lawful quote | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D06 Monitoring/count convention | 1 close per common session; entry session counts as 1; next lawful joint opening for normal liquidation | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D07 Holding cap | 20 common scheduled sessions | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| D08 Non-resolution boundary | eta=.10; target boundary 1 | 3 | Ex-ante policy, not compelled | Labels + support | Yes—unfrozen |
| E01 Equal capital sleeves | 6 sleeves; each 1/6 initial NAV; daily NAV updates | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E02 Raw attempt gross | K_raw=0.01 V_c =1% sleeve NAV | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E03 Total gross cap | 100% sleeve NAV and 100% portfolio NAV | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E04 Physical-security gross cap | 10% sleeve NAV and 10% total portfolio NAV | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E05 Absolute net currency cap | 10% sleeve NAV and 10% portfolio NAV | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E06 Turnover measure for sizing/impact | Prior 20 qualified sessions; all 20 required; median traded value | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| E07 Participation cap | Leg value<=0.1% of prior ADV20 median value | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E08 Displayed-depth cap | Order quantity<=10% executable displayed depth | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E09 Carry reserve horizon | 20-session carry reservation | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E10 Collision and sizing-pass counts | 1 pair attempt; 1 sizing pass; 0 redistribution | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E11 Allocation shrinkage range | rho in [0,1], largest feasible common rho | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| E12 Development reference capital | CNY 1,000,000 per estimator; CNY 6,000,000 total implied | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| F01 Execution cost functional constants | 2 coefficients; sqrt exponent 1/2; a,b>=0 | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F02 Execution-fit support | 200 orders; 20 sessions; 20/instrument/side | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F03 Cost extrapolation boundary | 0 extrapolation beyond observed instrument/side participation min/max | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| F04 P1 cohort age | Submission at least 60 common sessions before fit origin | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F05 P1/cost availability embargo | Outcome/settlement available at least 20 common sessions before fit | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F06 Old-cohort censor tolerance | 0 unresolved old-cohort records | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| F07 P1 total/pair minima | 500 total; 20 pairs | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F08 P1 cluster support/length | 20 clusters × 20 sessions | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F09 P1 estimator-group support | 50/group × 5 groups | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F10 P1 state/substate support | 20 in each F/P/N/A/X_entry/admitted-X | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F11 P1 signed support | 20 per signed orientation | 4 | Statistical rationale; not validated | Eligibility/economics | Yes—unfrozen |
| F12 Pool concentration ceilings | 20% per pair; 20% per time cluster | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| F13 Raw-pool numerical exclusions | 0 smoothing/trimming; 1 pool; dedup once | 3 | Ex-ante policy, not compelled | Eligibility/economics | No new smoothing; detailed policy still pending |
| G01 Reference complete-date support | 60 common pair-dates; 2 directions; 6 models | 4 | Statistical rationale; not validated | Discovery/population | Yes—unfrozen |
| G02 Reference pair count | >=10 complete pairs per block | 4 | Statistical rationale; not validated | Discovery/population | Yes—unfrozen |
| G03 Reference pair coverage | 80% pairs | 3 | Ex-ante policy, not compelled | Discovery/population | Yes—unfrozen |
| G04 Reference block count | 2 half-year blocks | 4 | Statistical rationale; not validated | Discovery/population | Yes—unfrozen |
| G05 Kish weight-support floor | Kish >=1000 | 4 | Statistical rationale; not validated | Discovery/population | Yes—unfrozen |
| G06 Within-date reference weight | 1/n; 1/B; 1/P; rational weights | 3 | Ex-ante policy, not compelled | Discovery/population | Yes—date/support details; hierarchy already approved |
| G07 Development dates and reference chronology | 2015 warm-up; 2016 reference; 2017–19 forward | 3 | Ex-ante policy, not compelled | Discovery/population | Yes—unfrozen |
| G08 Fold/fit/search budget | 6 blocks +1 final=7; 1 economic +2 diagnostics | 3 | Ex-ante policy, not compelled | Eligibility/economics | Yes—unfrozen |
| G09 Previously exposed calendar boundary | 2020–25 exposed; no later/earlier access | 3 | Ex-ante policy, not compelled | Reporting/claims | No—history/authority constraint |
| H01 Future start boundary | First full future session; no pre-start overlap | 3 | Ex-ante policy, not compelled | Reporting/claims | No—prospective principle approved |
| H02 Validation horizon/interim | 504 total; 252 operational interim | 4 | Statistical rationale; not validated | Observation + economics | Yes—unfrozen |
| H03 Validation settlement follow-up | 60 follow-up sessions | 3 | Ex-ante policy, not compelled | Observation + economics | Yes—unfrozen |
| H04 Validation inferential support | 500 attempts/20 pairs/20 clusters per group | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| H05 Bootstrap block length | 20 common-session moving blocks; paired resampling across candidates | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| H06 Bootstrap replication budget | 10,000 replicates | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| H07 Bootstrap seed | 20260927 | 3 | Ex-ante policy, not compelled | Reporting/claims | Yes—unfrozen |
| H08 Monte Carlo correction constants | Plus 1; B+1=10001 | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| H09 Confirmatory family/error level | 5 groups; .05 FWER; C/L 1/2; 1-sided final test | 4 | Statistical rationale; not validated | Reporting/claims | Yes—unfrozen |
| I01 Institutional numeric inputs | Unspecified—must come from qualified terms | 1 | Qualified external terms | Eligibility/economics | Evidence required; do not invent policy values |
| I02 Future model/data outputs | Unestimated—no fixed values | 5 | Output of approved method | Eligibility/economics | Authorize methods/access separately; values not selected |
| I03 Definition constants, not tuning knobs | 0/1, ±1, 2, 1/2, 1/a, t−1 | 2 | Conditional algebra/identity | Definition/implementation | No—identities, subject to method approval |
