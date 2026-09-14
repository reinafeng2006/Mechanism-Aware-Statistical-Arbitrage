# G4-05 V1 Executable-Specification Registry Proposal

Status: **APPROVED / FROZEN FOR V1 — PHASE 1 INNER DEVELOPMENT ONLY**

Executable-semantics binding: `V1-EXECUTABLE-SEMANTICS-A1`, approved and frozen before empirical access. Its finite-sample scale rules, leg-specific R1-MI factors, unordered R3 strata, R3/R4 numerical-state contract, exact A6 matrix, and G5 entry-state mapping are controlling where this earlier registry left an implementation choice open.

This registry closes V1 scope without fitting. It preserves the frozen R/P/N axes, A1–A5 interfaces, CS2, SR0→SR1, TP2/CG2/OF4, the Search Budget, and the sealed 2024–2025 held-out region.

## V1 scope disposition

| Family | V1 disposition | Reason |
|---|---|---|
| R0-DIST | `V1 CANDIDATE — REPRESENTATION ONLY` | symmetric standardized cumulative-response-path distance; requires R0-LIN bridge for A3 |
| R0-CORR | `V1 CANDIDATE — REPRESENTATION ONLY` | Pearson primary; Spearman diagnostic only; requires R0-LIN bridge |
| R0-LIN | `V1 PRIMARY DIRECTIONAL BASELINE CANDIDATE` | frozen OLS equation and explicit expected-response bridge |
| R1-M | `V1 FACTOR-ADJUSTED CANDIDATE` | market-adjusted residual relationship, P0 |
| R1-MI | `V1 FACTOR-ADJUSTED CHALLENGER` | adds only the PIT industry factor under the matched R1 sequence |
| R2-LIS | `V1 NOT DATA-READY / PRESERVED FOR V2` | five accounting-derived B1 constructs remain PIT/vintage unresolved; market-cap alone does not preserve a coherent five-construct P1 estimand |
| R2-N | `V2 / DEFERRED` | nonlinear escalation cannot be performance-triggered |
| R3-G | `V1 CANDIDATE — EXECUTABLE BUNDLE SELECTION REQUIRED` | P0 Gaussian EB random-intercept/random-slope family is approved in principle |
| R4-RW | `V1 CANDIDATE — EXECUTABLE BUNDLE SELECTION REQUIRED` | static intercept plus random-walk slope approved in principle |
| R4-MR | `V2 / DEFERRED` | not initial execution |
| R5-EG-ECM | `REGISTERED / BLOCKED / NO V1 EXECUTION` | authoritative C04 and price-construction contract absent |
| VECM | `V2 / DEFERRED` | no V1 execution |

Directed business linkage, MP3, additional factor families, and any new model/feature family are `V2 / FUTURE RESEARCH`.

## Common response and eligibility contract proposed for V1

For security `k`, the one-session signed response candidate is simple close-to-close raw return:

`r_k,t = P_k,t / P_k,t-1 - 1`.

This formula is executable only under the frozen C04-A descendant rule for both endpoints and the intervening interval. V1 requires:

- endpoints must be valid observed raw/unadjusted C03 closes tied to stable C01 identity;
- both endpoint sessions must be `NORMAL TRADING OBSERVED`; `UNKNOWN MISSINGNESS`, suspension, resumption ambiguity, identifier transition, nonpositive/nonfinite price, or a nonconsecutive eligible-session interval makes the response unavailable;
- an official C04-A action calendar must establish whether an identified action/distribution affects the interval; identified affected intervals are excluded, while a retained interval is labelled only `NO IDENTIFIED ACTION UNDER V1 CALENDAR`, never `AUTHORITATIVELY ACTION-CLEAN`;
- no forward fill, zero return, synthetic adjustment, Tushare/Sina adjustment-factor substitution, or economic splicing across `601313.SH -> 601360.SH`;
- every exclusion retains C04/C05/identity reason and rule version.

The frozen V1 C04-A rule is an official action-event exclusion contract, not a canonical adjusted-price construction and not proof of complete action cleanliness. Actions without a defensible effective/ex date remain unresolved and cannot silently qualify an interval. The underlying core-sidecar C04 state remains unresolved; the descendant calendar adds only bounded V1 exclusion evidence.

## Exact estimator mathematics common to V1

- OLS candidates require a full-column-rank PIT design and strictly positive residual degrees of freedom. Rank deficiency or mathematically unsupported variance is SR0-unavailable; no arbitrary completion percentage is added.
- MAD/SD response scales inherit A1b/A1c: finite nonzero scale and mathematical estimator support are hard requirements; near-zero nondegenerate quality is continuous metadata.
- all directional models are fit separately for `i -> j` and `j -> i`.
- every point forecast is fixed before observing its evaluated response; same-decision absorption and future smoothing are prohibited.
- common-support comparison uses matched pair/direction/origin/target/scale/H/U/P/N geometry; native coverage is reported separately.

## Proposed finite V1 relationship Search Budget

The minimal primary tuple bundle recommended for researcher freeze is:

| Tuple ID | Specification | `(H,U)` | Estimator | Role |
|---|---|---|---|---|
| `V1-R0D-252M` | R0-DIST + matched R0-LIN bridge | `(H252,U1M)` | deterministic distance + OLS bridge | representation baseline |
| `V1-R0C-126W` | R0-CORR Pearson + matched R0-LIN bridge | `(H126,U1W)` | Pearson + OLS bridge | co-movement baseline |
| `V1-R0L-126W` | R0-LIN | `(H126,U1W)` | OLS | primary directional baseline |
| `V1-R1M-126W` | R1-M | `(H126,U1W)` | two-stage OLS | factor baseline |
| `V1-R1MI-126W` | R1-MI | `(H126,U1W)` | identical two-stage OLS | industry-factor challenger |
| `V1-R3-252M` | R3-G P0 | `(H252,U1M)` | selected EB bundle | pooling candidate |
| `V1-R4-63D` | R4-RW P0 | `(H63,U1D)` | selected Kalman bundle | dynamic candidate |

Registered but non-primary diagnostics: Spearman on `V1-R0C-126W` and Huber on `V1-R0L-126W`, each on identical support; they cannot rescue or replace primaries. Other already-registered H/U tuples remain unexecuted V2/sensitivity inventory unless the researcher replaces—not adds to—the proposed tuple for that family before any outcome inspection. H504 is unused in V1 because R5 is blocked and no retained V1 family requires it.

This seven-tuple set is not a Cartesian product. R1-M versus R1-MI, N0 versus N1, and representation comparisons are distinct dependency-ordered families.

## R1 factor construction proposed for V1

- market factor: the frozen E03-A benchmark response, with benchmark identity bound in the execution manifest;
- industry factor: leave-pair-out, equal-weighted raw responses of currently PIT-eligible C06 peers in the same taxonomy/version scope, excluding both pair securities at each date;
- insufficient eligible industry constituents yields unavailable factor state, not imputation;
- R1-M and R1-MI use identical response, OLS, H/U, N overlay, support, and forecast sequence; only the industry factor differs.

Benchmark identity remains a gate binding because the acquired E03-A artifact identity must be named without inspecting its returns.

## R3 proposed executable bundle

Frozen `R3-A`:

- REML estimates group-level unstructured random-intercept/random-slope covariance and group observation variance inside each PIT formation set;
- C06 taxonomy-versioned industry is the only initial hierarchy;
- `N0` fixes pair-deviation covariance to zero; `N1` estimates it under the identical equation and information path;
- singular/boundary covariance yields an explicit estimator-quality/unavailable state, never silent covariance repair;
- all components re-estimate at each authorized origin/U1M refresh using prior information only;
- output separates fixed-effect, conditional random-effect, plug-in hyperparameter, observation, and predictive uncertainty; omission of hyperparameter uncertainty is labelled.

ML and `N-STRENGTH` are closed from V1. No additional hierarchy is available.

## R4 proposed executable bundle

Frozen `R4-A`:

- PIT maximum likelihood estimates `Q/R` inside each H63 formation set, with explicit zero/boundary/singular quality states;
- matched R0-LIN static fit supplies `alpha`, prior slope mean, and finite prior slope variance;
- U1D performs pre-response prediction, then an eligible post-evaluation measurement update for the next decision;
- state variance advances in eligible-trading-session time; missing/ineligible observations predict without measurement update;
- filtered and predicted state/uncertainty are separately versioned; event-time smoothing is prohibited.

Fixed-Q/R and inner-selected variance menus are closed from V1.

## Mechanism-evidence V1 boundary

- M1: with nonzero qualified expected direction `s=sign(mu_j|i,t)`, `UR0=|mu_j| - s*y_j` is the unclipped continuous signed under-response morphology (positive under-response, negative over-response). `UR1=UR0/q_j|i,t` is supporting only when predictive scale `q` is finite, positive and separately calibrated; it never replaces candidate-neutral A3 scaling. Zero/unreliable direction or uncertainty routes to U. UR2 is V2 because no qualified nonduplicative P1/event context exists. Morphology alone is not M1 identification.
- M2: source excess is `e_i,t=y_i,t-mu_i|j,t`; `MP0=e_i,t/S_i,t` preserves its signed direction under candidate-neutral scale. `MP1` appends, without combining, `log(amount_i,t/median_PIT(amount_i))` as primary E02-A context and the analogous positive-volume ratio as supporting context. Zero/nonfinite activity yields an explicit quality state. MP1 retains return-content, cause/proxy overlap, endogeneity, window overlap, leakage and flow-motive contamination fields. MP2 and MP3 are excluded from V1. Volume/amount is not exogenous pressure.
- M0: only positive PIT relationship-validity/data-quality rejection available under frozen P0 inputs; absent event/link data cannot be treated as no event. Missing M1/M2 evidence is not M0.
- U: use the frozen five-dimensional structured uncertainty record (`U4`-style representation) with no score, probability simplex, or label. U0 remains the explicit umbrella state; U1/U2/U3 are not V1 execution branches.

No mechanism probability or forced class is proposed. Evidence can support, oppose, conflict, or remain ambiguous.

## Computation gate

The researcher froze the seven tuples, R3-A, R4-A, SCI-A and TRADE-A. The C04-A descendant exclusion layer is acquired and structurally validated under manifest `C04-A-OFFICIAL-CALENDAR-V1`; the E03-A benchmark identity is structurally bound. `PAIR-A — COMPLETE PIT ALL-PAIRS` is the frozen V1 candidate universe: every contemporaneously PIT-eligible unordered pair in C06 scope `34 + 35`, including cross-code pairs, is evaluated through two separate directional channels with no pre-screening. Only 2015–2019 semiannual inner development is authorized; OF4 and held-out access remain denied.

All E1–E6 implementation gaps are closed by [the V1 executable-semantics amendment](../../decisions/V1_EXECUTABLE_SEMANTICS_AMENDMENT_FREEZE.md). No library default may supersede that amendment.
