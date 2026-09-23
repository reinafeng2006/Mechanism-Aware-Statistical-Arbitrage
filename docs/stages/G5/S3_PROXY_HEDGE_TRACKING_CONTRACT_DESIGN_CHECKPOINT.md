# S3 proxy hedge and tracking contract — design checkpoint

2026-09-23 — DESIGN ONLY / RESEARCHER DECISION REQUIRED.

[H-C and execution/accounting decisions are approved](../../decisions/S3_HC_PROXY_HEDGE_EXECUTION_ACCOUNTING_APPROVAL.md). Proxy identities, exposure construction, mapping algorithm, hedge refresh, tracking metrics/acceptance and unresolved execution details below are PROPOSALS. No proxy data, borrow evidence, tracking estimates, costs or historical strategy results are accessed.

## 1. Distinguish model exposure from neutralization target

Use a common factor-coordinate dictionary f (market and preregistered industry coordinates). Preserve each frozen model:
epsilon_model,c=y_j−beta_c*y_i−gamma_model,c'f−a0_c.

An R0/R3 model has gamma_model,c=0: this means its equation contains no explicit factor terms, NOT that its pair basket has zero factor exposure.

Let B_(k,c) be the factor-exposure vector used for hedge design, on the same coordinate dictionary. Define the intended neutralization target:
gamma_neut,c=B_(j,c)−beta_c*B_(i,c).

Let A_t be the factor-by-proxy exposure matrix for a common qualified proxy universe, H_t its return vector, and H_t=A_t' f_t+e_t as the declared exposure representation. A_t is not assumed known or exact.

Desired coefficient mapping:
h_c = T(A_t,gamma_neut,c),
w_c=(1,−beta_c,−h_c') on actual instruments, after combining identical physical positions.

The function T, proxy eligibility/selection hierarchy and estimation rules must be common to all candidates. Candidate differences enter through their approved beta and legitimately supplied exposure coefficients, not through six independent hedge searches.

### Application to all six estimators

| Estimator | Pair coefficient retained | Model gamma | Input to common neutralization rule |
|---|---|---|---|
| R0-D252 | Its directional OLS beta_D | Zero explicit factor vector | Auxiliary common exposure specification needed for B_j−beta_D*B_i |
| R0-C126 | Its OLS beta_C | Zero explicit factor vector | Same auxiliary exposure rule; no correlation-as-hedge coefficient |
| R0-L126 | Its OLS beta_L | Zero explicit factor vector | Same auxiliary exposure rule; preserve C/L duplicate lineage |
| R1-M126 | Residual-bridge beta_u | Market b_j−beta_u*b_i | Preserve that market information; any additional industry exposure needs a separately specified rule |
| R1-MI126 | Residual-bridge beta_u | Market b_j−beta_u*b_i; industry-j delta_j; industry-i −beta_u*delta_i | Preserve full model-implied market/industry information and factor-coordinate lineage |
| R3-252 | Conditional pair beta_p | Zero explicit factor vector | Same auxiliary exposure rule using beta_p; do not refit the relationship model |

A common market-plus-industry target therefore needs an additional, separately approved exposure specification for fields not supplied by R0/R3/R1-M. These missing fields are not zero-filled. Define the PIT estimation horizon, refresh, taxonomy, factor-return convention and treatment of incompatible existing factor definitions before access. Existing R1 information cannot be discarded or overwritten silently by the auxiliary layer.

Two bounded target-specification choices: (i) retain compatible model-supplied coefficients and fill only missing dimensions using one common auxiliary rule; or (ii) design one harmonized exposure layer for all models with an explicit reconciliation to the retained R1 coefficients. Recommend (i) for minimal intervention, conditional on coordinate compatibility; incompatibility stops for a binding rather than a covert estimator change. No auxiliary estimator or numerical H/U is selected.

## 2. Bounded proxy-universe constructions

Actual instruments remain UNSELECTED. The following are prospective instrument slots, not assertions that qualified or shortable products exist.

| Construction | Market slot | Industry slot | Main benefit | Principal limitation |
|---|---|---|---|---|
| U1 — fund-share proxies | One preregistered broad-market fund/share instrument from the common universe | One preregistered sector/industry fund-share instrument per eligible taxonomy group | Fewer physical legs and explicit instrument prices | Fund basis, taxonomy mismatch, constituents, cash drag and borrow qualification; not exact research-factor replication |
| U2 — physical constituent proxies | A disclosed tradable constituent basket | Disclosed industry constituent baskets under one fixed formation/weighting rule | Direct holdings/entitlement transparency and possible pair-exclusion control | Many orders/short obligations, eligibility gaps, corporate actions and rebalancing burden |

Recommend U1 as the first proxy-universe specification to consider, based on contract simplicity only, not observed feasibility or returns. U2 is a documented alternative, not an automatic fallback. No named instrument, provider, constituent rule or weight scheme is selected.

A common registry must bind immutable instrument IDs, instrument type, applicable taxonomy/exposure role, price and distribution conventions, eligible dates, borrow evidence requirements, deterministic substitute ranking if any, and mapping version. Any substitute rule must be approved before access; unavailable instruments cannot trigger ad hoc substitution.

A fund containing j/i is not the same physical instrument as j/i: do not cancel underlying economic holdings against fund shares algebraically. Disclose overlap through the exposure/tracking contract. For physical baskets, identical security positions can be aggregated; pair exclusion and gross/borrow consequences must be explicitly bound.

### Same-industry and cross-industry pairs

Use market plus each distinct required industry slot. A same-industry pair combines the industry target into delta_j−beta*delta_i on that common coordinate. A cross-industry pair retains separate industry-j and industry-i targets; no blended “average industry”.

If a required industry hedge is unavailable, compare:
- Strict qualification: ECONOMIC/EXECUTION GATE UNAVAILABLE, preserving the scientific signal.
- Explicit residual-exposure allowance under a preregistered acceptance contract, without claiming the omitted exposure is neutralized.

Recommend strict qualification for the initial contract. A residual allowance would require explicit approval, a declared metric/bound and amended coverage interpretation. It cannot become an automatic market-only or H-A fallback. No tolerance is selected.

## 3. Algebraic mapping gamma -> h in instrument units

After the target and actual registry are bound, use gamma=gamma_neut and A=the selected instruments' common-coordinate exposure matrix.

### M1 — exact exposure matching, with remaining proxy tracking

Require A h=gamma. If A is square and nonsingular, h=A^(-1)gamma. If A has more columns than rows and full row rank, a proposed common minimum-Euclidean-notional solution is:
h=A'*(A*A')^(-1)*gamma.

This is a mapping-rule proposal, not a fitted optimization or an approved algorithm. It exactly matches the declared exposure coefficients, NOT the model-return path. Rank, conditioning and gross-notional checks are mandatory; no rank tolerance, leverage cap or numerical regularizer is invented. Unsupported/unstable mapping is unavailable until requirements are bound.

Illustration with actual-instrument slots H_M,H_J,H_I and a triangular exposure specification:
A = [[b_M,b_J,b_I],[0,d_J,0],[0,0,d_I]].
Then:
h_J=gamma_J/d_J;
h_I=gamma_I/d_I;
h_M=(gamma_M−b_J*h_J−b_I*h_I)/b_M.

This corrects for the market exposure of industry proxies; setting h_M=gamma_M regardless of sector proxy exposures is generally wrong. The illustrative zeros are NOT asserted properties of real instruments. Use the full A for any cross-loadings. For a same-industry pair use one combined industry column/target.

### M2 — bounded residual exposure

A proposed common constrained rule can minimize (gamma−Ah)'W(gamma−Ah), subject to preregistered instrument, gross, borrow and position constraints, with a fixed deterministic tie rule. W, constraints and uniqueness conditions would be additional decisions, not values to tune on S3 performance.

Compare M1 versus M2 before access. Recommend M1 where the qualified exposure system supports it, with fail-unavailable behavior; M2 only if the researcher explicitly accepts a residual-exposure budget. Neither algorithm is approved now and no matrix is estimated.

The desired actual instrument coefficient vector is always (1,−beta,−h'). Its coefficients are close-notional weights, not share ratios. All six estimators use the same T and registry rules.

## 4. Two kinds of tracking difference

Preserve the approved total discrepancy:
xi_c=epsilon_model,c−epsilon_trade,c=h_c'H−gamma_model,c'f.

Define residual target exposure ell_c=gamma_neut,c−A h_c and implementation tracking:
tau_c=h_c'H−gamma_neut,c'f=−ell_c'f+h_c'e.

Therefore:
xi_c=(gamma_neut,c−gamma_model,c)'f + tau_c.

The first term is the intended change from the model's factor content to the chosen approximately neutral economic basket; tau is the remaining proxy implementation error relative to that target. For compatible full R1-MI targets those gamma vectors may coincide. For R0/R3 the intentional term need not vanish. Requiring small total xi for every candidate would wrongly penalize the very factor removal H-C intends.

Report both total model-to-trade difference and neutralization/implementation error. Do not redefine gamma_model or set it to gamma_neut merely to make xi appear small.

Exact modeled-residual replication requires xi=0 under the declared return/cash-flow identity and corresponding holding-path identity. A h=gamma_neut alone proves neither. H-B is benchmark only; its calculations would still need separate authority.

## 5. Static versus rebalanced hedge

| Choice | Prospective rule | Benefit | Limitation |
|---|---|---|---|
| S1 static origin shares | Freeze beta, h and resulting share proportions at the origin/entry protocol; only entitlement-preserving transformations thereafter | Preserves fixed-origin accounting; no extra hedge-refresh trading | Factor/weight exposure drifts; entry matching does not guarantee neutrality during holding |
| S2 rebalanced proxy hedge | Adjust h/shares on a preregistered schedule or deterministic exposure rule | Can control evolving exposures | Creates extra trades, costs, borrow/margin checks and a different path-dependent target/accounting protocol |

Recommend S1 for the first version, with explicit holding-period tracking/exposure reporting. H-C selection alone does not approve S2. No schedule, drift tolerance, rebalance threshold or discretionary replacement is supplied.

For S1:
L_u=sum_l abs(w_l)*O_l,u/P_l,t;
n_l=s*K*w_l/(P_l,t*L_u).

K is the approved fixed intended event capital. Compute L on unique actual instruments; fill differences enter economics, not ex-post denominator changes. Fixed shares produce changing notional exposures: exposure diagnostics must use n_l*P_l,q/K and actual outstanding positions, rather than pretending initial w remains a constant-dollar portfolio.

## 6. Model abnormality versus proxy-basket target

The approved z-gate remains abs(z_model)>=Q^w_0.95(abs(z_ref)), with numerical z0 uncomputed. It selects extreme pair-conditioned abnormality; H-C does not authorize replacing it with a newly scaled proxy residual.

At the signal, d_trade=−epsilon_trade=d_model+xi is an algebraic difference. It is NOT automatically the approved target or forecast. Neither discrepancy alone proves a forward correction.

The contract must explicitly map the model event into a fixed-origin tradable target D^C_t, deduct actual proxy-basket overnight movement to obtain D^C_u, and bind its orientation/no-reversal and exit-monitoring interpretation. Two prospective choices are: retain d_model as an explicitly hypothesized proxy-basket displacement target, or specify a tracking-aware target using the declared trade residual. The latter must not silently replace the model z-gate or create a second fitted trigger.

No target bridge is selected here. Identifying this prerequisite avoids treating approximate replication as exact by notation. G_target=abs(D^C_u)/L_u is a geometric target once that bridge is approved, not expected capture. The approved E1/P1 architecture remains, but economic payoff labels cannot be estimated until this target/exit dependency is closed.

## 7. Tracking metrics and prospective acceptance

Define all metrics on a preregistered prior reference window using only entry-available information. Future holding-period realizations are diagnostics/outcomes, never a justification for admitting that same trade or retroactively removing a bad observation.

| Metric | Purpose |
|---|---|
| Signed mean and RMS of total xi | Describe how the traded economic object differs from the model residual |
| Signed mean and RMS of tau | Measure unwanted proxy implementation difference relative to the neutralization target |
| Residual exposure ell=gamma_neut−Ah, plus qualified exposure drift | Test the claimed factor-neutralization quality |
| Tail/maximum path discrepancy on qualified prior episodes | Reveal concentrations and severe mismatch hidden by average error |
| Cash-flow-consistent holding-path error per intended K | Test static holdings through prices, distributions and actions, not only one-session factor returns |
| Tracking relative to declared target distance and scale | Assess whether mismatch is economically large for the hypothesized correction; report small-denominator instability without an arbitrary floor |

Compare two acceptance designs:
- T1: preregistered absolute bounds on exposure and implementation-tracking metrics, with coverage/lineage/support prerequisites.
- T2: the same type of qualification plus a target-relative tracking budget, requiring a defined target bridge and treatment of near-zero denominators.

Recommend T1 as the minimal initial acceptance architecture, with target-relative measures reported as non-selecting diagnostics until their admission interpretation is explicitly bound. No bound, quantile, confidence level, window, minimum support or acceptance number is selected. The final choices must precede exposure to S3 performance and cannot be tuned to obtain favorable PnL or more trades.

Rank deficiency, missing proxy history/borrow, inconsistent factor coordinates, unsupported prior metrics or breached approved bounds must produce a declared unavailable state. A numerical result alone is not proof of acceptable tracking. Do not repair failure by switching to H-A/H-B, relaxing alpha or activating P3.

## 8. Proxy actions, borrow and qualification

For fund-share proxies, qualify fund distributions, splits/consolidations, mergers/liquidations, NAV-versus-execution-price differences, underlying taxonomy changes and any restrictions affecting tradability. A fund's own accounting/borrow contract is required; underlying constituent eligibility does not establish fund shortability.

For physical baskets, qualify every constituent's long/short corporate-action entitlements and any formation/rebalance changes. Model factor total-return conventions, actual cash flows and manufactured short payments must reconcile; unknown actions remain unavailable. No new C04 repair.

For every actual negative instrument leg, obtain separate future-qualified evidence of borrowable quantity, locate/reservation timestamp and validity, fee/rate/reset/day count, recalls/buy-ins, collateral/margin/funding, manufactured distributions, settlement and account restrictions. Long legs require qualified funding/trading capacity. No availability is inferred from instrument type.

Fees/entitlements enter the existing non-overlapping ledger exactly once. Missing required evidence means ECONOMIC GATE UNAVAILABLE or EXECUTION UNAVAILABLE as appropriate; never zero cost or assumed exact tracking.

Entry uses the approved partial-fill -> abort/unwind architecture. First fill creates exposure, full qualified basket admits the episode, abort latches at the later-frozen failure condition, late fills join unwind, and no completion chase follows. Failed attempts remain E-A economics per intended K. Exit obligations precede risk reduction and ideal hedge preservation; detailed ordering/timings are still unresolved. Proxy replacement is not authorized by “risk reduction”.

## 9. Bounded comparison and remaining researcher bindings

One common registry and rule applies to all six estimators. Proposed comparison is limited to U1/U2 instrument constructions, M1/M2 coefficient maps, S1/S2 holding rules and T1/T2 acceptance architectures. These are design alternatives, not a factorial empirical search or a development-run budget. No combinations are tested.

Preferred complete proposal for consideration: U1 fund-share proxy slots, a compatible common exposure dictionary preserving supplied R1 coefficients and explicitly filling missing fields, M1 deterministic exact exposure matching where qualified, S1 static origin shares and T1 prior tracking/exposure qualification. Missing required industry proxies produce unavailability. All these details remain proposals.

The researcher must still bind actual instrument IDs/eligibility, exposure estimation and coordinate reconciliation, mapping uniqueness/conditioning controls, target bridge, tracking metrics/window/acceptance values, action/borrow qualification and detailed entry/exit mechanics before data access or capture/cost estimation.

| Decision | Bounded choice / proposed preference | Status |
|---|---|---|
| Market and industry proxy universe | U1 fund shares versus U2 physical portfolios; U1 proposed | No instruments selected |
| Cross-industry mapping | Separate industry targets/slots, combine only identical coordinates | Detailed common mapping pending |
| Missing industry hedge | Strict unavailable preferred; residual allowance requires explicit contract | No automatic substitute |
| Exposure mapping | Preserve R1 information; auxiliary common rule for missing dimensions; M1 versus M2 | No coefficients/model estimated or selected |
| Static/rebalanced | S1 preferred; S2 requires different path/cost contract | Not selected |
| Tracking | Distinguish intended model-to-target change from tau and ell | Metrics/acceptance contract pending |
| Acceptance | T1 absolute qualification proposed; T2 target-relative alternative | No tolerance selected |
| Proxy actions/borrow | Instrument-specific long/short qualification and unique ledger allocation | No evidence acquired |
| Signal-to-target bridge | Explicit D^C from model event versus tracking-aware target | No silent change to z-gate |
| Execution/accounting | Approved abort/unwind, E-A, intended K, obligation-first exits | Detailed mechanics remain pending |

No proxy/borrow data, tracking error, capture/cost parameters or numerical z0 accessed/estimated. No implementation, backtest or PnL inspection. NEXT_ACTION remains NONE.

**S3 PROXY HEDGE + TRACKING CONTRACT / RESEARCHER DECISION REQUIRED**
