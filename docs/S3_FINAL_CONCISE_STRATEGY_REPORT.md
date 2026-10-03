# S3 final concise strategy report

## 1. Executive summary

**S3 is a fully specified prospective strategy hypothesis, not a historically validated profitable strategy.**

The phenomenon of interest is temporary disagreement between economically related A-share equities: an unusually large deviation from a pair-conditioned normal relationship may subsequently narrow. Historical research found lower descriptive out-of-sample relationship loss from market adjustment, additional industry adjustment and hierarchical pooling in specified comparisons. Those findings concern prediction fit, not trading returns; later evidence also carries a corporate-action input-lineage limitation.

S3 separates discovering abnormality from trading its resolution. Six relationship estimators share one trading rule. A robust residual scale and preregistered weighted reference-tail threshold identify extreme model deviations. The proposed trade holds the two equities plus qualified market/industry fund-share hedges in a static-origin basket. Entry requires the model and tradable opportunity to agree in direction, the displacement to survive until executable entry, and expected capture to exceed all-in costs. Exit follows tradable-basket convergence, a holding cap or binding exceptional obligations.

Historical executable development stopped because mandatory evidence could not be qualified. No S3 profitability test was performed. The contribution is a precise, prospectively testable strategy and explicit economic identification requirements.

## 2. Economic hypothesis

**Extreme pair-conditioned deviations from a normal equity relationship may subsequently converge in an approximately factor-neutral tradable relative-value basket.**

For related equities i and j, the model asks what response in j is normal given i and the permitted information set. An unusual shortfall or excess identifies a possible opportunity, not a guaranteed correction. The relevant sequence is
\[
\text{relationship fit}\ne\text{statistical abnormality}
\ne\text{tradable convergence}\ne\text{executable alpha}.
\]

Good fit describes a conditional relationship. Abnormality measures distance from it. Tradable convergence requires a subsequently capturable movement in actual instruments. Executable alpha additionally requires feasible execution and net economic value.

A single-leg trade would also carry the equity's market and industry risks; a favorable outcome could reflect broad market movement rather than relative-value convergence. S3 retains the pair-response hedge and neutralizes declared exposures with tradable proxies. This clarifies the economic hypothesis without claiming perfect neutrality, exact model-residual replication, persistent stationarity or causal mechanism identification.

Throughout, t is the signal origin, u the next qualified executable entry reference, and q a later observation. Point-in-time (PIT) means information actually available by the decision timestamp. The underlying modeled response y is the qualified one-session equity response; price, response and entitlement coordinates must have auditable compatibility.

## 3. Six relationship models, one trading rule

\[
\boxed{\text{Six estimators of the normal relationship under one common trading rule}}
\]

Let mu denote the predicted response of j conditional on i. H counts prior synchronized eligible observations. Weekly/monthly relationship refreshes are native model schedules; the S3 scale and auxiliary exposures refresh daily.

| Model | Core equation/idea | Adjustment | Role in S3 |
|---|---|---|---|
| R0-D252 | Standardized cumulative-response-path distance; directional prediction uses its matched OLS bridge, mu=alpha+beta y_i | H252, monthly refresh; no explicit factor subtraction | Distance representation with a directional reference |
| R0-C126 | Pearson correlation plus matched OLS bridge: beta=rho sigma_j/sigma_i, alpha=mean(y_j)−beta mean(y_i) | H126, weekly refresh | Co-movement representation; prediction coincides with matched R0-L |
| R0-L126 | OLS y_j=alpha+beta y_i+epsilon | H126, weekly refresh | Direct pairwise regression baseline |
| R1-M126 | Residualize each equity on market response; mu=F_j+alpha+beta(y_i−F_i) | H126, weekly, two-stage OLS | Market-adjusted relationship |
| R1-MI126 | Same residual equation, with market and each leg's own industry factor in F_k | H126, weekly, two-stage OLS | Adds industry conditioning |
| R3-252 | Conditional hierarchical mean mu=(alpha_g+u_pair)+(beta_g+v_pair)y_i | H252, monthly; Gaussian empirical-Bayes random intercept/slope, REML | Pools pair information within the frozen industry-pair hierarchy |

For R1, F_k=a_k+b_k M+delta_k I_k, omitting industry for R1-M. Each industry factor uses eligible, equal-weighted peers, excluding both pair securities; cross-industry pairs retain distinct leg factors. R3 uses taxonomy-versioned unordered industry-pair strata, with direction-specific response/regressor roles.

Coefficients, support and update schedules retain their frozen definitions. These are not six independently optimized strategies. Model identity supports comparison and diagnostics, not separate hedge algorithms, tuned scenario systems or performance-based capital allocation.

## 4. Historical relationship evidence

The published contrasts below are AB / BA directional temporal medians of equal-pair paired absolute-loss differences: candidate minus frozen reference.

| Contrast | Inner development | Historical OF4 | Historical final held-out |
|---|---|---|---|
| Market: R1-M minus R0-L | −0.040348712 / −0.041032549 | −0.018791002 / −0.021400854 | −0.029309064 / −0.025782511 |
| Industry: R1-MI minus R1-M | −0.057673057 / −0.053985012 | −0.051491349 / −0.053554524 | −0.079608202 / −0.0861149 |
| Pooling: R3 minus matched R0-D | −0.0028566569 / −0.0026186183 | −0.0022209547 / −0.0020105019 | −0.0018858761 / −0.0018927902 |

Negative differences indicate lower **descriptive relationship-prediction loss**, not trading returns. Qualified inner evidence supports improvement in these specified contrasts. R0-C/R0-L equality is consistent with their matched prediction bridges; no unique winning model was established.

OF4 denotes the historical 2020–2023 evaluation, followed by 2024–2025 held-out research. Later input masks admitted subsequently identified corporate-action intervals, the documented C04 ancestry limitation. Those immutable outputs are historical descriptions, not validated confirmation under the completed exclusion contract. Different temporal roles also have different common-support intersections. No new significance test, ranking or bias correction is inferred from this table. Existing resolution findings describe morphology, not executable S3 gains.

## 5. Signal construction

The model-space displacement is
\[
d_t^{model}=\mu_{j|i,t}-y_{j,t}.
\]
Write the model residual as epsilon_model=y_j−beta y_i−gamma_model'f−a0. At origin t, replay the current coefficients on the common 126 qualified prior aligned observations W_t:
\[
\varepsilon_{v;t}=y_{j,v}-\beta_ty_{i,v}
-(\gamma_t^{model})'f_v-a_{0,t},
\]
\[
\sigma_t=1.4826\,MAD_{126}
=1.4826\,\operatorname{median}_{v\in W_t}
\left|\varepsilon_{v;t}-\operatorname{median}_{r\in W_t}\varepsilon_{r;t}\right|,
\qquad z_t^{model}=\frac{d_t^{model}}{\sigma_t}.
\]

Refresh daily using strictly-prior information. Zero, nonfinite, unsupported or insufficient-history scale gives SIGNAL UNAVAILABLE, never zero abnormality. Current-origin replay can understate future prediction error because fitting and formation information overlap.

The preregistered two-sided reference-tail probability is .05:
\[
z_0=Q^w_{0.95}(|z^{ref}|),\qquad |z_t^{model}|\ge z_0.
\]
The weighted empirical inverse CDF balances completed chronological blocks, pairs, two ordered directions and five equation groups; R0-C/R0-L share one group. Dates within complete cells receive equal weight. Missing required support cannot be repaired by favorable reweighting. Inclusive ties can admit more than exactly 5%.

This defines abnormality rarity, not profitability or a Gaussian significance test. Numerical z0 remains unestimated; it is not set to 1.96. H252 MAD and H126 SD are non-selecting robustness specifications only.

## 6. From model signal to tradable hedge

H-C is the practical fund-share proxy architecture. Begin with pair-response weights (1,−beta). Let B_i and B_j be compatible exposures to the common local market/industry basis:
\[
\gamma_t^{neut}=B_{j,t}-\beta_tB_{i,t},\qquad A_th_t=\gamma_t^{neut}.
\]
Columns of A are the exposures of actual qualified fund-share proxies. M1 exposure matching uses
\[
h_t=A_t^{-1}\gamma_t^{neut}
\]
for square nonsingular A, or
\[
h_t=A_t'(A_tA_t')^{-1}\gamma_t^{neut}
\]
for a full-row-rank underdetermined system. The tradable basket is
\[
\boxed{w_t=(1,-\beta_t,-h_t')}.
\]

Preserve compatible model-supplied loadings; fill missing dimensions using one common daily, strictly-prior, one-calendar-year unweighted auxiliary OLS rule. R0/R3's lack of explicit model factor subtraction does not imply zero actual factor exposure.

Use qualified market and industry fund-share slots, including both industries for cross-industry pairs. The deterministic registry ranks qualified instruments by first tradable date, then immutable identifier. Combine duplicate physical legs. Missing required qualified hedge or infeasible exact declared exposure matching gives HEDGE UNAVAILABLE, without market-only or physical-replication fallback. No actual fund has been selected.

Neutrality is approximate because fitted exposures and proxy returns are imperfect. With H denoting proxy responses,
\[
\xi_t=h_t'H_t-(\gamma_t^{model})'f_t
=(\gamma_t^{neut}-\gamma_t^{model})'f_t+\tau_t,
\quad \tau_t=h_t'H_t-(\gamma_t^{neut})'f_t.
\]
The first term is intentional model-to-trade difference; tau is unwanted implementation tracking. Exact exposure matching requires ell=gamma_neut−Ah=0 within certified numerical accuracy, not an economic tolerance.

Primary T1 qualification requires max |J_20|<=.005 per signal-origin gross. J_20 compares qualified cash-flow-consistent static proxy and target-factor holding paths over 20 common sessions in the strictly-prior annual history. This 0.5% budget is an ex-ante hedge-quality constraint, not a future guarantee. Mean, RMS, daily maximum, residual exposure, drift and target-relative tracking remain diagnostics. Shares are static-origin, not rebalanced daily.

## 7. Target B: tradable convergence

The actual trade residual is epsilon_trade=y_j−beta y_i−h'H−a0, so xi=epsilon_model−epsilon_trade. Target B maps the signal into that coordinate:
\[
D_t^{trade}=d_t^{model}+\xi_t,\qquad
d_t^{model}D_t^{trade}>0.
\]
All mapping inputs must be available at signal time. Failure means TARGET-MAPPING UNAVAILABLE / NO TRADE; no direction reversal or model-target substitution.

Let O_k,u be the first qualified synchronized post-open midpoint and P_k,t the signal-origin instrument price. Subtract movement before executable entry:
\[
\Delta B_{ON}^{trade}=\sum_kw_{k,t}(O_{k,u}/P_{k,t}-1),\qquad
D_u=D_t^{trade}-\Delta B_{ON}^{trade},
\]
\[
D_t^{trade}D_u>0.
\]
Otherwise the opportunity is exhausted: no trade and no target reset. Valid entry preserves sign(d_model)=sign(D_t_trade)=sign(D_u).

The model discovers abnormality, but the actual tradable basket defines the remaining economic opportunity. Future realized tracking cannot revise this target retrospectively.

## 8. Economic admission

Five mutually exclusive mature outcome classes describe the same Target-B basket:

| State | Meaning |
|---|---|
| F | Full target hit by the holding cap; target/cap tie counts as F |
| P | No hit; partial progress between .10 and 1 of the entry target |
| N | No hit; absolute progress at most eta=.10 |
| A | No hit; progress below −.10, indicating adverse divergence |
| X | Priority forced/exceptional exit, including failed-entry attempts |

Progress is b(q)=s DeltaB_u_trade(q)/|D_u|. X takes priority through financial closure; pending or unobservable paths have separate censor/unavailable status.

The pooled prior-event model P1 uses
\[
\widehat\pi_r=N_r/N,\quad
\widehat G_r=N_r^{-1}\sum_{e:R_e=r}G_e,\quad
\widehat m_u=\sum_r\widehat\pi_r\widehat G_r.
\]
G is signed benchmark gross capture per intended K, not a clipped target. One raw arithmetic pool covers estimators and directions, counting exact C/L duplicates once. Joint scenario, payoff, duration and inventory paths preserve the dependence needed for borrow, funding and exit costs.

All-in expected round-trip cost is
\[
\widehat c_{RT,u}
=c_{entry}+E[c_{exit}]+E[c_{borrow}]+E[c_{funding}]+E[c_{other}],
\qquad
\boxed{\widehat m_u>\widehat c_{RT,u}}.
\]
E1 uses no safety margin or cost multiple. Failed-attempt costs enter the same economics; missing required evidence gives ECONOMIC GATE UNAVAILABLE, not zero. Sparse states cannot trigger smoothing, flexible conditional models or fallback. Mature prior support must satisfy the frozen 95% net-mean precision halfwidth of 5bp per K; this is an estimation-support condition, not a positive-return confidence-bound entry rule.

## 9. Position construction and capital

After physical-leg aggregation,
\[
L_u=\sum_k|w_{k,t}|\frac{O_{k,u}}{P_{k,t}},\qquad
\boxed{n_k=\frac{sKw_{k,t}}{P_{k,t}L_u}},
\qquad s=\operatorname{sign}(D_u).
\]
Therefore sum_k |n_k|O_k,u=K. Full remaining target displacement per intended gross is G_target=|D_u|/L_u, distinct from expected capture.

Raw intended gross is **1% of declared book NAV per attempt**, subject to **100% total gross** and **10% gross per physical security** caps at book/portfolio level. Actual borrow, collateral, funding and liquidity constraints also bind. A single common proportional shrinking pass handles simultaneous proposals; rejected allocations are not redistributed. Apply E1 at the resulting size with relevant nonlinear fees.

Gross commitments include pending orders and unwinds, without hidden cross-basket netting credit. Restricted short proceeds are not free capital. Exact lawful lot-compatible geometry is required; there is no rounding rescue. Submitted K remains immutable through success or failure. Peak deployed capital is diagnostic, while portfolio NAV is the aggregate-return denominator.

## 10. Exit

Using qualified entitlement-consistent static-origin instrument coordinates,
\[
\Delta B_u^{trade}(q)=\sum_kw_{k,t}\frac{P_{k,q}-O_{k,u}}{P_{k,t}},
\quad R^{trade}(q)=D_u-\Delta B_u^{trade}(q),
\]
\[
\boxed{sR^{trade}(q)\le0}.
\]
This is the normal convergence trigger, monitored at qualified common closes. Maximum holding is **20 common scheduled sessions**, counting entry as session 1; suspensions do not pause the counter. Target or cap triggers liquidation at the next lawful joint opening opportunity, not a presumed fill at the trigger price.

Exceptional exits follow contractual/legal obligations -> feasible risk reduction -> hedge preservation. Recall, buy-in, margin failure, suspension or unsupported action can break hedge geometry. Tradable legs are reduced deterministically; blocked legs and unsettled claims remain obligations. The cap is not a guarantee of financial closure.

## 11. Execution realism and accounting

Entry uses synchronized quotes and coordinated lawful immediate-or-cancel orders, with timing bounds derived from actual feed/broker/venue contracts. First fill begins exposure; only the complete qualified basket admits an episode. Incomplete execution latches deterministic abort: cancel remaining orders and unwind actual plus late fills, without completion chasing.

E-A retains failed attempts in economics even when no episode is admitted:
\[
E[R_{attempt}]
=p_{admit}E[R|admitted]+(1-p_{admit})E[R|failed].
\]
Historical borrow permission, binding locates, quantities and recall terms cannot be assumed. Corporate actions must preserve original-share value and correctly allocate long and short entitlements.

For signed fill quantity q_l, actual price p_l, pre-order benchmark m_l and signed entitlement value D_e,
\[
G_e=\frac{-\sum_lq_lm_l+D_e}{K_e},\quad
C_{exec,e}=\frac{\sum_lq_l(p_l-m_l)}{K_e},
\]
\[
R_e^{net}=G_e-C_{exec,e}-C_{fees,e}-C_{borrow,e}
-C_{funding,e}-C_{other,e}.
\]
Each charge or entitlement appears once. Collateral principal is not itself a cost; its actual financing may be. An unknown settlement, mark or entitlement remains unavailable, not an assumed flat position.

## 12. Entire strategy in thirteen steps

1. Load only qualified PIT prices/responses, identities, factors, calendars, proxy and account evidence.
2. Update each native relationship model on its frozen prior formation window; obtain mu and beta.
3. Observe the qualified signal response and calculate d_model=mu−y_j.
4. Replay current-origin residuals on common prior H126 observations; obtain MAD scale and model z.
5. Apply the fixed weighted empirical absolute-z threshold; record unsupported scale/reference states.
6. Select the qualified registered proxy slots; retain supplied exposures, estimate missing dimensions by the common rule, solve M1 and check T1.
7. Form the physically aggregated static basket w and signal-time D_t_trade; require agreement with d_model.
8. At the first qualified synchronized post-open snapshot, subtract overnight basket movement; require surviving same-direction D_u.
9. Determine intended K under common gross/resource constraints; obtain supported pooled capture and all-leg cost expectations. Apply E1 once at that size.
10. Construct exact lawful signed shares, confirm locates/collateral/funding, reserve resources and submit the coordinated order batch.
11. Admit only a complete basket. Otherwise latch abort, cancel and deterministically unwind, retaining failed-attempt economics.
12. Hold origin shares; monitor C4 convergence and the 20-session cap, giving exceptional obligations priority over hedge preservation.
13. Liquidate and reconcile all positions, borrow, cash and entitlements; classify mature outcomes or censoring and account for every attempt per its original K.

## 13. What was actually validated?

| Layer | Status | Supported claim |
|---|---|---|
| Relationship modeling | Historical comparisons completed with stated qualifications | Lower descriptive inner loss for the specified adjustment/pooling contrasts; no unique winner |
| Abnormality specification | Frozen H126 scale and weighted .05-tail architecture; numerical z0 unestimated | A precise rarity definition, not calibrated economic predictive power |
| S3 mathematical strategy | Fully specified | A coherent prospective signal-to-execution hypothesis |
| Historical executable development | NON-ESTIMABLE UNDER FROZEN EXECUTABILITY PROTOCOL | Mandatory evidence could not be qualified; Phase B did not run |
| Profitability | Untested | No supported positive or negative S3 profitability claim |
| Prospective validation | Design preserved; not started | A future qualified study remains conditional on evidence and prerequisites |

\[
\boxed{\text{S3 profitability was not tested.}}
\]

The historical development budget specified one 2015–2019 economic protocol: 2015 warm-up, 2016 formation/reference, six 2017–2019 half-years and one final fit. It was not executed as S3 development.

The prospective design requires a new unobserved post-release window. Using supported development dependence/variance/occurrence, it selects the shortest qualifying 1/2/3-calendar-year horizon for a 10bp material net effect and 80% planning power. Validation uses 50,000 paired calendar-block bootstrap replicates, a protocol-hash seed and five-group Holm testing at .05. Block length is max(20,L_information,ceil(n^(1/3))), with all terms in common scheduled sessions and n the fixed validation calendar's session count. Neither power nor success is presumed.

## 14. Why historical development stopped

Phase A found **eight mandatory evidence families missing/non-estimable and one requiring descendant requalification**. Major gaps included the PIT fund-share registry, synchronized intraday evidence, historical account-specific borrow, funding/collateral contracts, orders/fills/settlement and timing contracts. Stock/fund entitlement histories and cash-flow-consistent factor reconstruction were also unqualified. The baseline needed accessible permitted-date partitions and lineage requalification.

These gaps prevent identification of the actual basket, executable opportunity, admission/failure paths and joint capture/cost distribution:
\[
\text{missing evidence}\ne 0\text{ cost / perfect execution}.
\]
Daily bars cannot establish fills; current contracts cannot establish historical account terms. Inaccessible evidence does not prove that no provider possesses it. The finding concerns available qualified evidence, not negative performance, a failed backtest or evidence against convergence. No synthetic historical profitability claim was produced.

Historical development remains closed. Future prospective work would require qualified locates, funding/collateral contracts, synchronized quotes/order events, audited settlement/entitlements and a post-freeze window, together with all frozen initialization and support prerequisites. New observations alone do not authorize a replacement training period or relaxed strategy.

*Canonical sources:* [frozen protocol](stages/G5/S3_FROZEN_STRATEGY_AND_PRE_DEVELOPMENT_PROTOCOL.md), [final numerical approval](decisions/S3_FINAL_PROTOCOL_FREEZE.md), [final synthesis](stages/G5/S3_FINAL_SYNTHESIS_AND_DISPOSITION.md), [Phase A report](stages/G5/S3_PHASE_A_DATA_FEASIBILITY_AND_MANIFEST_REPORT.md), [relationship registry](stages/G4/G4_05_V1_EXECUTABLE_SPECIFICATION_REGISTRY.md), [executable-semantics amendment](decisions/V1_EXECUTABLE_SEMANTICS_AMENDMENT_FREEZE.md). This is the concise researcher-facing reading reference; the frozen specifications control technical details.

## 15. Three takeaways

1. **Empirical finding:** specified factor-adjustment and pooling comparisons improved descriptive inner relationship prediction; that evidence does not establish persistent stationarity or tradable convergence.
2. **Strategy contribution:** S3 connects model abnormality to an actual proxy-hedged target, expected-net-value admission, static positions, realistic failures and auditable all-attempt economics.
3. **Evidence boundary:** historical executable development is non-estimable because mandatory evidence could not be qualified. The project produced a fully specified, prospectively testable statistical-arbitrage strategy, but not evidence that the strategy is profitable.
