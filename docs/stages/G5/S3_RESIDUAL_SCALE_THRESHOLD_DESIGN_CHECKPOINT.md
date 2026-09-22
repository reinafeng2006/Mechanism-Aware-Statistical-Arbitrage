# S3 residual scale and threshold design checkpoint

> Historical proposal record, dated 2026-09-18. The [2026-09-22 researcher decision](../../decisions/S3_SCALE_ARCHITECTURE_APPROVAL.md) now approves the specified scale, orientation and weighting architecture. Statements below that all choices remain proposals describe the original checkpoint, not current authority. The [subsequent preregistration](../../decisions/S3_REFERENCE_TAIL_PROBABILITY_PREREGISTRATION.md) freezes alpha=0.05 and the weighted empirical 95th-percentile rule; numerical z0 remains unestimated and fallback inactive. Current gate: [capture/cost design](S3_CAPTURE_COST_DESIGN_CHECKPOINT.md). The original proposal body is preserved below.

2026-09-18 — **S3 DEVELOPMENT DESIGN GATE 01 / DESIGN ONLY**.

## Authority and scope

The researcher selects **S3 — PEER-ONLY HEDGED RELATIVE-VALUE CONVERGENCE** as the architectural direction. The six relationship candidates remain six estimators under one common architecture. This records the architectural selection, not approval of the scale, window, threshold, orientation or development proposals below.

No implementation, historical data access, calibration, acquisition, C04 repair, backtest, trading execution or PnL inspection is authorized. No frozen V1 artifact, prior specification, relationship estimator or historical claim is changed. The parent design is `TRADING_STRATEGY_ECONOMIC_REDESIGN_CHECKPOINT.md`. The old V1.1 security-response scales and A1 H126 loss layer remain intact; neither is silently reused as an S3 residual scale. No cost forecast or expected-capture model is defined in this gate.

All numerical design-budget values below are **proposals for researcher approval**, not calibrated values or selected thresholds. No empirical quantity has been computed or inspected for this document.

## 1. Signal object, units and the two PIT clocks

For candidate c, pair p={i,j}, direction i→j and signal close t,

`d_t^c=mu_(j|i,t)^c−y_jt = −epsilon_(t;t)^c`.

y is a simple return in decimal response units. The semicolon in epsilon_(s;t) means: evaluate historical observation s using the relationship/hedge geometry legitimately frozen for decision t. Let theta_(t−)^c contain all coefficients fitted before the evaluated response, including R1 leg regressions and bridge, or R3 fixed effects and conditional pair deviations. Let w_t^c be the declared tradable residual-basket coefficients, with dependent-security coefficient normalized to +1.

| Quantity | Units / meaning |
|---|---|
| d_t | Decimal response discrepancy in the dependent-security-normalized basket coordinate, not currency and not expected net return |
| epsilon_(s;t) | Historical residual response in that same coordinate under theta_(t−), factor/identifier geometry and w_t |
| sigma_t | Positive dispersion of those residual responses; same units as d_t |
| z_t=d_t/sigma_t | Dimensionless deviation from the model's zero-error target, not automatically a Normal z-score, probability or p-value |

Multiplying a basket coordinate by a nonzero constant a requires multiplying d and sigma by a and abs(a), respectively; abs(z) is unchanged. Changing the mix of legs is not a scalar rescaling and requires reconstruction of residual history. If a gross-capital normalization L is applied, both d/L and sigma/L must use the same L. Entry-time L_u, overnight correction and expected economic return belong to the subsequent admission geometry; do not divide a signal gap by an unrelated security volatility or by cross-sectional pair dispersion.

Two clocks must not be conflated:

1. **PIT at decision t:** every coefficient, historical response, factor vintage and qualification used in sigma_t is available before t; the evaluated y_jt never enters its own denominator.
2. **Prequential PIT at historical s:** a prediction for s uses theta_(s−), not today's theta_(t−). This yields a different residual stream.

Current-geometry replay is PIT at t but is not an out-of-sample prediction made at s. It must never be labeled as such. Replay can use only original defensible PIT observations/vintages; later corrections or retrospectively invented clean intervals do not acquire historical eligibility by being known today.

## 2. Exact residuals for all six candidates

All coefficients in this section are frozen at the applicable relationship refresh for t. Their original H/U are unchanged: R0-D252 and R3-252 monthly; R0-C126/R0-L126/R1-M126/R1-MI126 H126 weekly. No relationship refitting to optimize scale is proposed.

### R0-D252, R0-C126, R0-L126

For each of the three OLS bridges,

`epsilon_(s;t)^c=y_js−alpha_(ji,t−)^c−beta_(ji,t−)^c*y_is`,
`w_t=(1,−beta_(ji,t−))`, `a0_t=alpha_(ji,t−)`.

At s=t, `d_t=−epsilon_(t;t)` exactly in the specified algebra. R0-D distance and R0-C correlation are not residuals or hedge ratios; their OLS bridges supply the object. R0-C and R0-L with identical input histories share the same equation and should not supply two independent corroborating observations.

### R1-M126

For each leg k, define with t-frozen OLS coefficients

`f_(k,s;t)=a_(k,t−)+b_(k,t−)*m_s`, `u_(k,s;t)=y_ks−f_(k,s;t)`.

Then

`epsilon_(s;t)=u_(j,s;t)−alpha_(u,t−)−beta_(u,t−)*u_(i,s;t)`
`=y_js−beta_u*y_is−(b_j−beta_u*b_i)*m_s−[alpha_u+a_j−beta_u*a_i]`.

The residual-consistent factor-coordinate basket is

`w_t=(1,−beta_u,−(b_j−beta_u*b_i))`,
`a0_t=alpha_u+a_j−beta_u*a_i`.

These are coordinates for (j,i,market). Replacing this innovation with `y_j−alpha−beta*y_i` drops a modeled risk component and is not S3 residual alignment.

### R1-MI126

Use each leg's own industry factor under the declared decision-origin PIT industry binding:

`f_(k,s;t)=a_k+b_k*m_s+delta_k*q_(k,p,s;t)`.

q uses contemporaneously qualified constituents for historical s in the industry bound at the decision origin; it excludes both pair members and retains taxonomy/identifier lineage. The residual is

`epsilon_(s;t)=y_js−beta_u*y_is−(b_j−beta_u*b_i)*m_s`
`                 −delta_j*q_(j,p,s;t)+beta_u*delta_i*q_(i,p,s;t)`
`                 −[alpha_u+a_j−beta_u*a_i]`.

The basket coordinates on (j,i,market,industry-j,industry-i) are

`w_t=(1,−beta_u,−(b_j−beta_u*b_i),−delta_j,+beta_u*delta_i)`.

Identical industry instruments are aggregated algebraically; different industries are not blended. Full prior factor support is mandatory. At s=t this is exactly the model error, so d_t=−epsilon_(t;t), not a new R0 surrogate.

### R3-252

Let `(alpha_p,t−,beta_p,t−)=beta_G,t−+bhat_p,t−`, the fitted stratum fixed-effect vector plus the pair's conditional random intercept/slope. Then

`epsilon_(s;t)=y_js−alpha_p,t−−beta_p,t−*y_is`,
`w_t=(1,−beta_p,t−)`, `a0_t=alpha_p,t−`.

Use the pair's conditional innovation, not a pooled population residual that removes its fitted deviation. Shrinkage affects the fitted geometry and residual dispersion; it does not make the residual a different physical unit. At s=t, d_t=−epsilon_(t;t).

### Tradable mapping and exactness boundary

For every candidate, the common form is `epsilon_(s;t)=w_t' r_s−a0_t`, where r_s contains the securities/factors just declared. An intercept is not a traded leg. MAD/SD center the history and hence ignore an additive constant a0_t; **the numerator remains d_t=−epsilon_(t;t)**, not minus a median-recentered innovation. A persistent nonzero residual median must be reported as model bias, not silently removed from the signal.

R1 factor coordinates are not automatically executable instrument coordinates. If factor coefficients gamma are replicated by instruments with exposure matrix Gamma, the declared hedge must establish `Gamma' h=gamma` and the corresponding realized response mapping. If instrument-basket return equals the model factor combination only approximately, a tracking residual appears: the model d_t is not the exact tradable-basket gap. Do not pretend scaling fixes that mismatch. Gate status is **HEDGE MAPPING UNRESOLVED / S3 SIGNAL UNAVAILABLE** until exact alignment or an explicitly approved new tracking-aware object is defined. No proxy or instrument is chosen here.

Likewise current-geometry replay is a one-session return basket under today's coefficients; it is not automatically the multi-session PnL of fixed shares. The declared origin-share hedge and its drift remain in the parent S3 geometry. sigma_t is a signal innovation scale, not holding-period portfolio volatility. Floating stored predictions/coefficients may differ by rounding: algebraic equality is not a promise of bitwise equality. Future lineage validation must bind the same coefficient version/precision and account for that distinction without rewriting immutable inputs.

## 3. Which historical geometry?

| Geometry | History | Advantage | Limitation / recommendation |
|---|---|---|---|
| Current-origin replay | epsilon_(s;t) for s in W_t, all using theta_(t−) | Exact alignment with the currently declared residual basket | May overlap coefficient estimation and understate out-of-sample error; recommended as **descriptive basket dispersion**, not predictive uncertainty |
| Prequential errors | epsilon_(s;s) using each historical theta_(s−) | Honest past forecast-error stream, includes changing-estimator behavior | Mixes changing hedge geometries; useful separate diagnostic, not silently substituted for current-basket scale |
| Disjoint historical replay | Current theta_(t−), but only s outside all observations used to fit it | Reduces direct in-sample fit overlap without refitting models | Often much older/less representative and lower support; no automatic shift to this architecture |

**Proposed primary:** current-origin replay, with one common history/refresh policy across candidates. Explicitly disclose fit-overlap counts and in-sample optimism, especially for R1's multistage fits and R3's conditional effects. It does not prove equal false-positive rates or remove overfitting. A candidate can have small fitted residual dispersion and poor future performance; a larger z is not evidence it is better. If the researcher instead requires a calibrated prediction-error probability, current replay is insufficient and this gate must choose a different object, not rebrand it.

This choice does not alter any relationship estimator. It defines a new, separately versioned S3 scale layer if later authorized. No residual replay is performed now.

## 4. Bounded scale architectures

For n=abs(W_t), median m_t=median_(s in W_t) epsilon_(s;t), mean ebar_t=mean epsilon_(s;t):

`sigma_MAD,t=1.4826*median_(s in W_t) abs(epsilon_(s;t)−m_t)`;

`sigma_SD,t=sqrt[sum_(s in W_t)(epsilon_(s;t)−ebar_t)^2/(n−1)]`.

The factor 1.4826 is the normal-consistency convention, not evidence of normality, finite-sample unbiasedness, or an exact tail probability. MAD is less sensitive to extremes than SD; its robustness does not protect an incorrectly estimated hedge or missing data. See the primary [NIST scale discussion](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm) and [MAD definition](https://itl.nist.gov/div898/software/dataplot/refman2/auxillar/mad.htm).

| Property | sigma-A: trailing MAD | sigma-B: trailing SD | sigma-C: model-implied predictive SD |
|---|---|---|---|
| Object | Robust spread of aligned residual history | Quadratic spread of same history | Declared conditional future observation/prediction-error uncertainty |
| Units | Residual-response units | Same | Same only when prediction target matches |
| Outliers | Bounded central sensitivity; can be zero with many ties | An extreme residual can dominate | Depends on likelihood/covariance assumptions; not automatically robust |
| Responsiveness | Window-driven; may respond slowly to a minority of large shocks | Reacts strongly to large recent deviations | Reacts to model state, leverage and uncertainty as supplied |
| Interpretation | Typical historical basket dispersion | Historical root-mean-square centered dispersion | Uncertainty includes declared parameter/state components; different estimand |
| Cross-model compatibility | Same formula for all six | Same formula for all six | Existing uncertainty outputs are not equivalent across the six |
| PIT | Prior valid history, current-origin coefficients/factors | Identical geometry | All parameters/covariances prior; current explanatory values only if legitimately observable |
| Minimum | Entire H_sigma; positive finite resulting MAD; n≥2 under proposal | Entire H_sigma≥2; denominator n−1, not model residual df | Supported fit/rank/df and finite positive relevant covariance, per model |
| Work per pair/direction/refresh | O(H_sigma*legs) replay plus exact median selection/sort | O(H_sigma*legs) replay and moments | Potentially cheap if already supplied; producing missing full uncertainty would require new work/semantics |
| Failures | Missing support, invalid residual, zero/nonfinite scale | Same, including unsupported n | Missing/partial uncertainty, invalid covariance, nonpositive/nonfinite result, target mismatch |

For R0, the existing OLS predictive output has the form `s_pred^2=R*[1+1/n+(y_it−mean(y_i))^2/Sxx]`, where R=SSE/(n−2). R1's corresponding bridge formula uses residual x but does not by itself propagate all first-stage factor uncertainty. R3's documented conditional output has `R+x_t' C_p x_t`, with x_t=(1,y_it), C_p the conditional random-effect covariance; omitted fixed-effect/hyperparameter uncertainty is not added by assertion. These supplied outputs can be labeled diagnostics. They cannot be described as one fully equivalent uncertainty-aware threshold scale across all six. No new sigma-C is invented for an unsupported model.

**Primary recommendation: sigma-A.** Keep sigma-B as a predeclared diagnostic robustness calculation; do not switch to whichever produces better convergence. Exclude sigma-C from the primary common threshold until comparable uncertainty targets exist. No epsilon floor, winsorization, tail trimming or scale clipping is proposed.

## 5. H_sigma, U_sigma and candidate fairness

Relationship estimation history and trading threshold-scale history are separate objects. Common architecture means the same residual construction, scale formula, support definition, refresh and threshold rule—not equal numerical sigma across candidates.

| Architecture | Comparability | Candidate geometry | Assessment |
|---|---|---|---|
| Native H/U | Different smoothness and staleness confound signal counts | Follows H126-weekly/H252-monthly fits | Do not inherit automatically |
| Common H_sigma and daily U_sigma | Same trailing length and scale decision cadence | Replays each current candidate geometry; no model refresh added | Recommended; isolates scale design from relationship H/U |
| Common weekly scale refresh | Lower work / more stable denominator | Geometry changes require immediate reconstruction or invalidation | Reasonable alternative, but introduces an additional staleness convention |
| Fixed dated calibration window | Stable external yardstick | Can become stale after regime/geometry change | Not proposed as primary |

Define native W_(c,p,t) as the most recent H_sigma qualified synchronized residual observations with s<t and all inputs available before t. No calendar-day replacement or shortened window. For the fairness/calibration panel use W_common,p,t: the same last H_sigma dates on which **all six** residual objects can be legitimately constructed. Then evaluate each candidate's distinct epsilon on these dates. If common history is insufficient, the matched observation is unavailable; separately report native-support coverage/scales without using that fallback for common attribution or calibration. Both directions remain separate, with pair-level weighting later. Selection of common support changes the reference population and must be disclosed.

Propose daily U_sigma: at each signal close, use a scale calculated exclusively from s<t with coefficients frozen before the current response. Relationship coefficients still change only at their original U. After any coefficient, factor-leg, industry-stratum, taxonomy, identifier or hedge-map change, reconstruct the **whole prior window** under the new declared geometry, not a concatenation of old-geometry residuals. If reconstruction fails, signal unavailable until a complete supported history exists. Do not retain stale sigma or reset already-admitted episode origins. A common weekly alternative must have the same mandatory invalidation rule.

H_sigma has no uniquely optimal value implied by algebra. Proposed bounded lengths are **126 qualified observations primary, 252 diagnostic robustness**, familiar shorter/longer trading-history scales rather than proven optimal economic horizons. This is a design proposal, not automatic inheritance from A1 or a fitted optimum. No other H or U enters the proposed budget. Daily U is chosen to avoid stale/geometry-mismatched scaling, not for observed performance.

## 6. z and unavailable states

`z_t^c=d_t^c/sigma_t^c` only if d finite, full aligned support exists, geometry/lineage are valid, and `0<sigma_t^c<infinity`.

| State | Required behavior |
|---|---|
| sigma=0 | SIGNAL UNAVAILABLE; never infinity, epsilon replacement or zero abnormality |
| sigma nonfinite/negative | SIGNAL UNAVAILABLE with diagnostic cause |
| Fewer than full H_sigma qualified observations | SIGNAL UNAVAILABLE; no shorter-window fallback |
| Invalid historical row | Exclude only by predefined PIT eligibility, seek preceding qualified rows; no response bridging or outcome-conditioned deletion |
| Row claimed valid but internally inconsistent | Integrity failure; no silent NaN-dropping to rescue the scale |
| Nonzero but tiny scale | Retain value and quality diagnostics; no new near-zero threshold |
| Geometry refreshed | Replay all H_sigma under the new origin mapping before a new signal; preserve previously entered episode state |
| Hedge/model basket mismatch | S3 signal unavailable; a numerical residual scale does not repair economic misalignment |

Missingness masks and support dates are part of lineage. Large residuals are not invalid merely because they are large. MAD center m_t is used for scale estimation only; z remains d/sigma. Nonzero historical bias is reported separately.

## 7. What z0 means, without choosing it

`abs(z_t)≥z0` means the current model-zero departure exceeds a declared multiple of the residual's prior typical dispersion. It is not automatically a significance test, evidence of convergence, or a transaction-cost test.

| Binding method | Definition | Advantage | Limitation |
|---|---|---|---|
| Z-A conventional | Fix one z0 before data/outcomes, with a stated interpretation | Least data adaptation | A familiar multiple is a convention unless a reference law is justified; MAD scaling does not imply Gaussian tails |
| Z-B tail/occurrence design | z0=inf{x:F_ref(x)≥1−alpha_ref} for X=abs(z) | Directly answers intended rarity without future convergence/PnL optimization | Requires a declared reference population; empirical rarity is not a false-positive rate under an unverified null |
| Z-C finite development grid | Choose one common z0 from a finite predeclared Z by one objective | Can ask whether thresholded events better discriminate future convergence | Uses outcomes, requires honest temporal separation and consumes selection freedom |

For a genuinely justified standard-Normal reference, the mathematical two-sided relation would be `z0=Phi^−1(1−alpha_ref/2)` (one-sided: `Phi^−1(1−alpha_ref)`), where Phi is the standard-Normal CDF. This is an illustration of the needed assumption, **not** an assumption adopted here. Non-Gaussian, biased, heteroskedastic, dependent residuals and fitted scales invalidate a casual 'two sigma means 5%' statement.

**Preferred binding method: Z-B, descriptive reference rarity, not false-signal control.** A proposed occurrence design parameter is alpha_ref=0.05 for the absolute tail, subject to researcher approval; this is a conventional rarity budget, not an economically optimal value or a selected z0. Do not split it into equal signed tails unless symmetry is demonstrated or separately imposed. Empirical quantile atoms can make the ≥ threshold occurrence exceed alpha; disclose the actual count rather than introduce randomized ties or change the inequality.

Use only the prospective-in-development stream of z values formed without each evaluated observation entering its own scale. Pool with predetermined weights: equal chronological calibration-block influence, equal unordered-pair influence within a block, equal supported directions within pair, and equal estimator-family influence. To avoid duplicate R0-C/R0-L equations determining the tail twice, propose five fixed groups {R0-D}, {R0-C,R0-L}, {R1-M}, {R1-MI}, {R3}, with equal group weights and equal C/L shares inside their group. Still report all six books. This weighting is a proposed reference-distribution definition, not a performance ranking. If the matched panel lacks a group, the common calibration is unavailable rather than silently reweighted.

Formally `F_ref(x)=sum_l omega_l*1{abs(z_l)≤x}`, sum omega_l=1, with omega_l determined by that hierarchy, not by scale size, signal profitability or row volume. This pools **dimensionless** temporal innovations to bind a common threshold; it is not cross-sectional dispersion used as sigma. It cannot guarantee the same tail frequency for each candidate or sign. Historical fit overlap remains a limitation even when subsequent z calibration is chronological.

No quantile, reference distribution or z0 is computed now.

## 8. Calibration objectives — no default to Sharpe

Z-B's primary objective is reference occurrence, not a forward performance objective: estimate the declared weighted reference quantile and evaluate its out-of-block occurrence stability without changing the objective. O1–O3 below are alternatives **only if the researcher chooses outcome-dependent Z-C**.

Let u denote the first eligible hypothetical entry event, d_u the remaining original basket gap, s=sign(d_u), and Delta B_u(q) the parent S3 fixed-origin basket movement after u. For an eventual separately frozen ten-eligible-basket-session diagnostic horizon, define

`Y=1{there exists a qualified close q by that horizon with s*Delta B_u(q)≥abs(d_u)}`.

This is a resolution label, not an executed portfolio return or a cost-adjusted outcome. Require d_t*d_u>0 and a qualified original basket mapping. Missing forward paths are censored/unavailable, never coded as failed resolution. The diagnostic's multi-leg clock, overnight mapping and treatment of partial/suspended observations must be approved before any labels are constructed; this gate does not bypass the next S3 geometry/execution gates. A proposed ten-session horizon is an explicit design inheritance for comparison, not a calibration result.

| Objective | Example precise criterion | What it answers | Research freedom / limitations |
|---|---|---|---|
| O1 resolution discrimination | For each chronological fold f and common z, D_f(z)=weighted mean(Y given abs(z_t)≥z)−weighted mean(Y given abs(z_t)<1); select max of median_f D_f(z) over the fixed grid | Does thresholded abnormality separate subsequent target resolution from small departures? | One outcome and one ranking objective; not net profitability; full-target resolution gets mechanically harder for larger gaps, which must not be hidden |
| O2 quality/coverage stability | A predeclared functional of resolution rate/magnitude, usable signal count and fold dispersion, e.g. mean(D_f)−lambda*SD(D_f), subject to a coverage constraint | Is discrimination sufficiently supported and stable? | lambda, coverage minimum and any magnitude/rate combination are additional choices; none supplied as an automatic default |
| O3 economic net value | Maximize one predeclared development-only mean net basket value after a separately frozen cost/borrow/exit contract | Which threshold helps executable economic payoff? | Requires forward economics and more modeling choices; much closer to strategy optimization; not appropriate before the next gate |

If Z-C is chosen, recommend **O1 only**, with one threshold across models, the same reference weighting as above, fixed small-departure comparison band abs(z)<1, and no simultaneous optimization of labels/horizon/costs. Use a finite-grid deterministic tie rule (smaller z for greater coverage), declared before access. O1's binary label should be accompanied by non-selecting signed-movement/coverage diagnostics; do not change to a magnitude objective when the binary result disappoints. No confidence/significance cutoff is inferred from few correlated folds.

Coverage/stability are mandatory reporting dimensions under either Z-B or Z-C; they do not become a second hidden optimizer. No 'enough observations' statistical minimum is derived from algebra. Structural identification requires full history and nonempty comparison groups/folds; reliable effective sample size remains a design limitation. If a researcher wants a power/precision requirement, it must be specified separately before access rather than invented after counts. Report pair/time clustering and censoring, not just raw row count.

**Overall recommendation: Z-B first**, because it gives z0 a rarity meaning without using convergence outcomes. If the research question explicitly requires development selection on future convergence, O1 is the least portfolio-performance-adaptive of the listed alternatives. Neither path proves expected economic value; that is the separate economic gate.

## 9. One-sided versus two-sided science

Peer-only identifies the relationship role, not a mandatory positive sign. Two distinct scientific hypotheses are available:

- One-sided under-response: `d_t>0 AND z_t≥z0`; s=+1 is long the dependent coordinate and hedges its declared counterpart/factors. It tests delayed upward relative correction only.
- Two-sided residual convergence: `abs(z_t)≥z0`; s=sign(d_t) or, after the no-reversal overnight gate, sign(d_u). It tests both upward and downward corrections of the same peer residual. It does not add the former source/MP1 channel.

**Recommend two-sided as the scientific definition**, because residual convergence rather than upward catch-up is the selected economic object. This is a recommendation requiring researcher approval, not an inference from the S3 architecture selection. Report signs separately; do not assume symmetric distributions, costs, rates of resolution or aggregate away a failing orientation. Both signs use the same absolute-threshold interpretation unless a later explicit amendment is made. No sign-specific z0 tuning is proposed.

Scientific orientation precedes availability of short stock/hedge legs. One-sided d>0 can also require borrowing a hedge. Define scientific opportunities first; then separately classify whether their required signed legs, borrow, collateral and simultaneous execution are feasible. Infeasible trades are EXECUTION UNAVAILABLE, not absent scientific signals and not permission to reverse or drop a leg. Thus missing borrow data does not select the scientific direction. A two-sided aggregate alone cannot establish that both directions work.

## 10. Connection to the next economic gate

For the recommended two-sided definition, the conceptual actual-admission indicator is

`I(t,u)=I_valid(t,u) * 1{abs(z_t)≥z0} * 1{d_t*d_u>0}`
`        * 1{m_hat_u>c_hat_RT,u} * I_execution(u)`.

I_valid includes pair/directional/model/PIT/identity/C04/C05 admissibility, finite supported aligned scale, origin-geometry lineage, preserved episode/collision rules and still-valid signal at entry. I_execution requires the **whole** declared signed basket's executable prices, borrow, collateral and funding qualification. These are conceptual gates inherited from S3 design, not instructions to implement unfinished execution semantics. For the one-sided alternative multiply by 1{d_t>0}; do not remove the economic/execution gates.

d_u is the remaining origin-coordinate gap after overnight basket movement, not a new target reset. m_hat_u and c_hat_RT,u are respectively expected executable value and round-trip costs in the same economic units. **Their definitions, estimation, numerical values and calibration are deliberately deferred to the next design gate.** z0 measures residual rarity/materiality, not a stand-in for expected profitability or transaction costs. I cannot be evaluated until those later contracts exist. No current borrowing feasibility is inspected.

## 11. Explicit small future development budget

Everything in this section is a proposed ceiling to approve before data access. None is executed or authorized now.

### Period and chronological folds

- Only 2015-01-01 through 2019-12-31 for development. No 2020–2025 calibration, including scale/threshold selection based on later diagnostic convenience.
- Proposed run-in/reference formation: 2015–2016. Early dates without full relationship and scale histories remain unavailable; do not shorten H or silently import earlier/later data. No guarantee of coverage is made.
- Six forward assessment blocks: 2017H1, 2017H2, 2018H1, 2018H2, 2019H1, 2019H2. At each block start estimate any reference quantile or choose a fallback-grid value using only completed prior development blocks; freeze it for that block. Daily scales can update from prior observations as specified, never from the evaluated day.
- For Z-C, use only forward labels resolved before the training cutoff; purge overlapping/unresolved episodes at boundaries. Ten eligible sessions is not automatically ten calendar days. Censored paths do not receive zero labels. If labels would cross 2019-12-31, do not access 2020 to finish them.
- A final common threshold may be bound from all approved development information after procedural assessment, but its training sample is then explicitly 2015–2019, not an untouched test. New prospective validation must follow a final design freeze; already opened 2024–2025 is not re-sealed by this proposal.

### Preferred path P: occurrence-based, no forward-outcome selection

| Configuration | Scale / H_sigma / U_sigma | z0 procedure | Role |
|---|---|---|---|
| P1 | Current-geometry MAD / 126 / daily | Common weighted reference quantile at proposed alpha_ref=0.05 | Preselected primary design proposal |
| P2 | Current-geometry MAD / 252 / daily | Same quantile procedure, separately formed training reference | Window robustness only; cannot replace P1 because its outcome is better |
| P3 | Current-geometry SD / 126 / daily | Same quantile procedure | Scale robustness only; cannot replace P1 by performance |

Primary objective: implement the prescribed weighted occurrence threshold; no optimizer over P1/P2/P3, no convergence labels and no PnL needed for this path's threshold binding. Report subsequent-block signed tail frequencies, scale/fitting-window overlap, unavailable support, residual median, geometry resets and pair/fold concentration. Tail-frequency drift is a finding, not permission to keep adjusting alpha/H/U. Prequential residual diagnostics may be described conceptually but are **not an extra scored configuration** in this budget.

### At most one fallback F: explicitly approved Z-C/O1

Only if selected by the researcher **before** forward outcomes are opened, replace quantile binding with:

`Z={1,2,3}`, current-geometry MAD, H_sigma=126, U_sigma=daily; one common threshold for all six, using O1 above. These three standardized multiples are a small declared sensitivity grid, not chosen values, Gaussian significance levels or promises of adequate support. No further intermediate points, sign-specific values or per-model tuning.

The fallback is not an automatic rescue after P produces inconvenient frequency or poor convergence. Its additional label geometry must first be frozen; absent that prerequisite, the fallback remains a design option only. Do not run O2/O3 in parallel and pick a preferred story.

### Count and stopping rule

- Preferred path: **3 statistical configurations × 6 estimators = 18 estimator/configuration series**, assessed across the six chronological blocks (108 reporting cells). Directions and pairs are observations within a series, not newly optimized strategies.
- Fallback alone: **3 grid configurations × 6 estimators = 18 series**, six chronological blocks (108 reporting cells). Its single chosen threshold is a derived output, not a fourth search point.
- If the researcher explicitly approves both for a one-time methodological comparison *before outcomes*, absolute ceiling is **6 configurations × 6 = 36 series**, 216 block reporting cells. This is not the recommended default; there is no automatic switch or second outcome objective. Sigma-C, weekly refresh, native H/U, additional windows and alternative tail budgets are outside this budget.
- Stop after the prescribed pass and report all results/unavailable states. No expansion when support is sparse, no lowering z0 to manufacture trades, no scale floor, no per-model rescue and no later-year lookup. If a necessary reference/group/fold is unavailable, report it and do not select from an altered population.
- No numerical minimum effective sample size or precision guarantee is claimed. A valid numerical quantile is not proof of stable calibration. Whether observed concentration is acceptable must be considered against a preregistered precision requirement before any future confirmation claim, not a post-hoc change to this selection objective.

## 12. Six-model fairness and limitations

1. The same residual-coordinate rule, MAD formula, H/U, PIT cutoff and scale failure semantics apply to every candidate. Candidate-specific epsilon and sigma values are expected; a common *numerical* sigma would compare different basket risks without standardizing them.
2. One common z0 and interpretation; no six independent threshold optimizations. The C/L duplicate group weighting is fixed before seeing frequencies and does not delete either book.
3. Common-support history/events are used for scale/threshold attribution. Native coverage is separately reported, not substituted for absent common support. Candidate-specific missingness and factor requirements remain visible.
4. Raw noise level alone no longer creates more triggers merely through an unscaled d. Under an exact positive rescaling of residual and signal, abs(z) is invariant. Different tail shapes, bias, leverage, fit optimism and genuine signal dynamics can still yield different trigger frequencies; this is not a promise of equal counts or equal false positives.
5. Current-origin MAD does not include full estimation uncertainty. A more flexible in-sample model can have deceptively small fitted scale. Report fitting-history overlap and predeclared forward frequency stability; do not interpret larger z as model superiority or quietly add candidate-specific df/inflation corrections.
6. No Gaussian calibration or inferential significance claim is attached to the 1.4826 factor. No winsorization, approximate quantiles, pair sampling, cross-sectional scale, A1/A3 substitution or source-channel expansion is introduced.

## 13. Consolidated decision table

| Decision | Bounded options | Formula | Interpretation | Pros | Cons | Development needed? | Recommendation |
|---|---|---|---|---|---|---|---|
| Residual object | Current-origin replay; prequential; disjoint replay | epsilon_(s;t)=w_t'r_s−a0_t | Dispersion of the current declared basket versus historical forecast errors | Replay exactly aligns the current modeled object | Fit overlap/optimism; tradable factor mapping still required | Geometry choice ex ante; qualification later | Current-origin replay, labeled descriptive not predictive uncertainty |
| Scale estimator | MAD; SD; supplied predictive SD | 1.4826 median abs(epsilon−median epsilon) | Robust typical innovation size | Common across six; less tail-sensitive | Zero/tied samples; no full parameter uncertainty | No outcome tuning; adequacy/coverage later | MAD primary; SD diagnostic; predictive scale not a common primary |
| H_sigma | Native; common126; common252 | last H_sigma prior qualified common dates | Equal memory convention, not equal numerical scale | Removes H-based scaling confound | No uniquely optimal economic length; support differences | Design choice plus non-selecting diagnostic | 126 proposed primary; 252 one robustness configuration |
| U_sigma | Native; common daily; common weekly with invalidation | recompute from s<t under current geometry | Denominator freshness separate from model U | Daily avoids stale scale after geometry changes | Additional replay work; still descriptive fitted geometry | No performance selection | Daily; model H/U unchanged |
| z0 method | Z-A convention; Z-B reference tail; Z-C finite grid | quantile_(1−alpha_ref)(abs(z)) or z in {1,2,3} | Common rarity multiple, not profitability | Z-B avoids forward performance selection | Reference-tail frequency is not null false-signal control | Z-B uses past standardized reference; no outcomes; Z-C uses outcomes | Z-B with proposed alpha_ref=.05; z0 not selected now |
| Calibration objective | Occurrence for Z-B; O1/O2/O3 if Z-C | O1: max median_f D_f(z) | Rarity versus future resolution versus economics | Separates statistical and cost gates | Outcome objectives consume freedom; require qualified labels | Only under future explicit authority | Occurrence preferred; O1 only if fallback explicitly chosen |
| Scientific orientation | One-sided peer under-response; two-sided peer convergence | z≥z0 and d>0; or abs(z)≥z0 | Upward-only versus signed residual correction | Two-sided matches convergence hypothesis | Asymmetric tails/costs/borrow; separate signed reporting essential | Hypothesis chosen before feasibility; no performance choice | Two-sided proposed; execution availability separate |

### Preferred specification path and one fallback

**Preferred P:** peer-only S3; propose two-sided scientific residual convergence; current-origin full residual replay with declared tradable mapping; common H126/daily MAD; common-support attribution and separate native coverage; one weighted-reference tail threshold (proposed 5% absolute occurrence budget), not a p-value; H252 MAD and H126 SD diagnostic only. Numerical z0 remains unknown until separately authorized development. No forward economic or resolution performance is used to choose it. The next gate must independently bind the remaining executable-opportunity/cost mapping.

**Only fallback F:** same object/MAD/H126/daily/common-model rule, but researcher-approved Z-C grid {1,2,3} and the single O1 resolution-discrimination objective, after its label geometry is frozen. Not a performance-triggered rescue and no O2/O3 optimizer.

Architectural S3 selection is recorded; every further choice in this checkpoint remains a proposal. No files implementing a strategy, data artifacts, scales, thresholds or PnL were created. Frozen V1 stays unchanged.

**S3 SCALE + THRESHOLD DESIGN / RESEARCHER DECISION REQUIRED**
