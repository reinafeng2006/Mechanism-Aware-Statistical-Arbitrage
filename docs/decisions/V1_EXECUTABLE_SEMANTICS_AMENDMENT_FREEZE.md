# V1 Executable Semantics Amendment Freeze

Decision date: 2026-09-14
Amendment ID: `V1-EXECUTABLE-SEMANTICS-A1`
Status: **APPROVED / FROZEN BEFORE EMPIRICAL ACCESS**
Ancestry: `V1_PRECOMPUTATION_TRADING_PROTOCOL_FREEZE` + `V1_PAIR_UNIVERSE_FREEZE` + `C06-AVAILABILITY-AMENDMENT-V1`

This amendment closes E1–E6 from the pre-access executable-semantics checkpoint. It changes no dataset, universe membership, candidate family, H/U/O tuple, temporal role, scientific target, or held-out boundary.

## E1 — finite-sample scale contract

For the same economically aligned directional-response quantity on its PIT history:

- `PS0_MAD = 1.4826 * median(|x - median(x)|)` using the conventional finite-sample median (middle order statistic for odd `n`; arithmetic mean of the two middle order statistics for even `n`);
- `PS1_SD = sqrt(sum((x-mean(x))^2)/(n-1))`, exactly `ddof=1`;
- each estimator requires at least two finite observations;
- unavailable, non-finite, exactly zero, or fewer-than-two-finite states make scaled loss unavailable;
- nonzero near-zero scale remains continuous quality evidence; there is no epsilon, floor, completion ratio, or empirical precision cutoff.

PS0 and PS1 use the same PIT history and response object. PS1 remains robustness-only.

## E2 — R1-MI leg-specific factor binding

For each security `k`, residualize against the market factor and `q_{g(k,t),s}`, where `g(k,t)` is that security's own C06 industry state legitimately available at the decision origin. The factor is equal-weighted across other contemporaneously eligible securities in that exact industry state and excludes both members of the evaluated pair. For a `34 x 35` pair, the 34 leg uses factor 34 and the 35 leg uses factor 35. No blended factor exists.

Only after both leg-specific PIT residualizations are fixed are the two directional residual equations estimated. R1-M and R1-MI otherwise share response, support, OLS, H126/U1W, N/P layer, and update order.

## E3 — R3 hierarchy

At each PIT refresh, assign every unordered pair to exactly one taxonomy-versioned unordered industry-pair stratum: `34x34`, `35x35`, or `34x35`. Pair-specific random intercept and slope are nested in that stratum. The same unordered stratum is used for both directional fits, while direction-specific response/regressor roles remain separate. A cross-industry pair is never assigned to either leg alone.

Taxonomy/version change creates a new stratum version. Prior states may not be pooled across incompatible taxonomy versions by implementation convenience.

## E4 — R3/R4 estimation and numerical states

### R3

- fit N0 as stratum-level OLS with intercept and slope and pair covariance fixed exactly to zero;
- fit N1 by Gaussian REML with an unstructured `2x2` pair random-intercept/random-slope covariance and one observation variance per stratum/direction;
- use a Cholesky/square-root covariance parameterization and one deterministic L-BFGS optimization path (`maxiter=1000`, relative objective tolerance `1e-8`), with no optimizer fallback;
- require at least two eligible pair identities in the stratum, full-rank fixed-effects design, positive residual degrees of freedom, and at least two finite observations per fitted pair;
- a converged positive-semidefinite boundary covariance, including an exact zero component, is valid and recorded as `CONVERGED_BOUNDARY`;
- non-convergence, non-finite objective/state, non-PSD covariance, rank failure, or unrecoverable numerical failure is `UNAVAILABLE_AT_ORIGIN`; no floor, repair, alternative hierarchy, or estimator substitution is permitted.

### R4

- estimate pair-direction-specific nonnegative `Q` and `R` by Gaussian prediction-error maximum likelihood inside each PIT H63 window;
- use one bounded L-BFGS-B path (`Q>=0`, `R>=0`, `maxiter=1000`, relative objective tolerance `1e-8`) and no fallback;
- initialize optimization deterministically with `R_start = matched-static OLS residual variance` and `Q_start = 0.01 * R_start`;
- initialize the state with the matched-static OLS intercept, slope mean, and OLS slope-estimation variance; invalid/non-finite initialization is unavailable;
- exact zero `Q` or another converged valid boundary is `CONVERGED_BOUNDARY`, not automatic failure; a zero `R` is valid only while every innovation covariance remains finite and strictly positive;
- state time advances by eligible trading session; U1D predicts before response and updates only afterward. Missing/ineligible responses receive prediction without update. Smoothing is prohibited.

U1W refresh means the first candidate-eligible exchange session of each ISO week; U1M means the first candidate-eligible exchange session of each calendar month. H counts the most recent synchronized candidate-eligible observations strictly before prediction, not calendar days.

## E5 — exact A6 design matrix

Every horizon/component regression uses OLS with intercept. Mandatory continuous values being absent makes that row unavailable; optional uncertainty uses value `0` together with an availability indicator. Boolean/state fields are encoded independently as `0/1`; they are not one mutually exclusive mechanism label.

`PV0` columns, in order:

1. signed peer directional departure divided by peer PS0;
2. absolute value of column 1;
3. signed source-side excess divided by source PS0;
4. absolute value of column 3;
5. expected peer response divided by peer PS0;
6. expected source response divided by source PS0;
7. peer predictive standard deviation divided by peer PS0, or zero plus column 8;
8. peer predictive-uncertainty-available indicator;
9. source predictive standard deviation divided by source PS0, or zero plus column 10;
10. source predictive-uncertainty-available indicator;
11. peer scale value;
12. source scale value;
13. peer finite formation-support count divided by authorized H;
14. source finite formation-support count divided by authorized H;
15. C06 classification age in calendar days;
16. C06 stale-gap indicator;
17–21. separate indicators for measurement uncertainty, information insufficiency, mechanism ambiguity, evidence conflict, and data/provenance uncertainty;
22. positive M0/rejection-evidence-present indicator;
23. relationship-break/invalidity-diagnostic-present indicator.

Rows with a positive M0 or invalidity diagnostic may remain in predictive validation as PIT context but are never relabelled as valid mechanism evidence. Full-rank failure or nonpositive residual degrees of freedom makes that A6 fit unavailable; no column is silently dropped.

`PV-M1 = complete PV0 + {UR0/PS0_peer, UR1_value_or_zero, UR1_available, M1_support, M1_oppose, M1_ambiguous}`.

`PV-M2 = complete PV0 + {MP0, MP1_amount_log_ratio, MP1_volume_log_ratio, amount_available, volume_available, mechanical_return_content, cause_proxy_overlap, endogeneity, overlapping_windows, future_leakage, flow_motive_ambiguity}`.

`PV-BOTH` is the exact union of PV-M1 and PV-M2 additions with no interaction and remains diagnostic-only. Future RT0–RT3 values never enter predictors. Each RT component/horizon is fitted separately; no binary label or collapsed resolution target is created.

## E6 — G5 entry-state mapping

The rules below determine eligibility for a V1 directional economic probe, not mechanism identification.

`TV1-M1 ELIGIBLE` iff all of the following hold at event time: relationship/A3 state valid; expected direction finite and nonzero; `UR0 > 0`; peer gap finite and nonzero; no positive M0 rejection; no relationship-break/invalidity flag; no unresolved evidence-conflict flag; and all signal/execution eligibility and C04/C05/identity requirements pass. UR1, when available, is recorded but is not a gate.

`TV1-M2 ELIGIBLE` iff all of the following hold: relationship/A3 state valid; source excess and MP0 finite and nonzero; primary MP1 amount context is available and `log(amount/median_PIT(amount)) > 0`; no positive M0 rejection; no relationship-break/invalidity flag; no future-leakage contamination; no unresolved evidence-conflict flag; and all signal/execution eligibility and C04/C05/identity requirements pass. Volume context and remaining contamination dimensions are reported but do not create a second threshold.

M1 direction is the sign of the event-time remaining peer gap. M2 direction is opposite the event-time source excess. Simultaneously eligible M1/M2 legs coexist before security-level netting. U alone is not `NO TRADE`; only the enumerated invalidity, rejection, conflict, data/eligibility, and quality conditions block. Events not satisfying either exact map create no position and retain reason codes. No additional abnormality/z-score threshold is authorized.

`measurement != evidence != belief != probability != label != trade decision` remains controlling.

## Numerical and contamination governance

All tolerances above are fixed engineering convergence identities, not performance tuning values. A retry may repeat the identical deterministic call after a transient process failure, but it may not change optimizer, initialization, bounds, estimator, hierarchy, support, or model. No result, survival count, return, pair count, outcome, OF4, or held-out information informed this amendment.

`V1-EXECUTABLE-SEMANTICS-A1 — APPROVED / FROZEN`
