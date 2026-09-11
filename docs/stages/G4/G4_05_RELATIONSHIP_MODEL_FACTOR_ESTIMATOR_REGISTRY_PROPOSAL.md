# G4-05 Relationship Model, Factor & Estimator Registry Proposal

Status: **G4-05 CLARIFIED / AWAITING RESEARCHER APPROVAL**
Boundary: mathematical and estimation preregistration only. No frozen-data inspection, fitting, descriptive statistics, predictive validation, target computation, or held-out access.

## Purpose and namespace

This registry defines the bounded implementation questions that must be frozen before any relationship candidate may be fitted. The labels R0–R5 below belong exclusively to the `G4-05 RELATIONSHIP-MODEL` namespace; they do not replace or reinterpret the existing M0 rejection-family R0–R3 labels.

Every entry remains `NOT COMPUTATION-AUTHORIZED` until its exact equation, estimator, PIT inputs, update rule, authorized Search Budget, and candidate-specific eligibility contract are frozen.

## Common mathematical notation

For ordered pair `i -> j` and decision origin `t`, let `y_{j,t}` be the authorized signed directional response target, `x_{i,t}` the source response, `f_t` the P0 market/industry/common-factor information, `z_{ij,t}` the separately tracked P1 company/pair information, and `I_t` the PIT information set available before prediction. A model emits an expected directional response `mu_{j|i,t}` and, where supported, a separately evaluated uncertainty object `Q_{j|i,t}`.

The downstream abnormality interface is fixed:

`departure_{i->j,t} = observed directional response_{j,t} - mu_{j|i,t}`,

with candidate-neutral PIT scaling and A3 eligibility/anti-circularity rules. Candidate uncertainty never enters that point-departure denominator.

## Orthogonal design axes

The registry separates three questions:

1. `R0–R5`: what mathematical relationship is represented;
2. `N0/N1`: how strongly information is pooled versus allowed to vary by pair;
3. `P0/P1`: which authorized information layer enters the otherwise matched specification.

`relationship representation family != N0/N1 pooling dimension`.

`common-factor adjustment != company-characteristic conditioning`.

R3 makes partial pooling explicit as its mathematical object, but it is not synonymous with N1. N0/N1 may overlay R0-L, R1, R2, R4, and R5 where the estimator is mathematically identifiable; R3 itself may have stronger-pooling and more pair-specific variants. Any inapplicable overlay must be recorded rather than coerced.

## Clarified candidate-family registry

All equations are directional and are repeated separately for `i -> j` and `j -> i`. The proposed H/U entries below are explicit authorized tuple menus, not Cartesian products; H504 remains conditional on an approved representation-specific support contract.

| ID | Distinct mathematical role and exact target | Bounded candidate equation forms | Primary estimator; bounded challenger | Proposed authorized H/U tuples | PIT inputs, uncertainty, and A3 interface |
|---|---|---|---|---|---|
| R0-S | Statistical baseline representation of aligned pair behavior; target is a PIT pair-representation statistic, not a predicted response | normalized distance `D_ij,t(H)` or correlation `rho_ij,t(H)` on the same authorized aligned response series | deterministic sample statistic; one robust correlation/distance variant only if separately justified | `(H63,U1W)`, `(H126,U1W)`, `(H252,U1M)` | C01/C03/C05/C06 eligibility and alignment; support/quality output, no forecast uncertainty; does not itself produce an A3 expected-response departure |
| R0-L | Statistical baseline for signed directional response `y_j,t` | primary `y_j,t=alpha_ij+beta_ij x_i,t+epsilon_ij,t`; challenger may add only a preregistered intercept-stability/robust-loss variant without changing the target | OLS primary; one robust linear estimator challenger | `(H63,U1D)`, `(H63,U1W)`, `(H126,U1W)`, `(H252,U1M)` | PIT aligned raw responses and eligibility; `mu_j|i,t`, residual diagnostics, optional qualified prediction interval; A3 uses observed response minus pre-decision `mu` |
| R1 | Remove or condition on shared market, industry, or common-factor exposure before measuring pair-specific response; target remains `y_j,t` | two-stage: `y_k,t=a_k+b_k'f_t+u_k,t`, then `u_j,t=alpha_ij+beta_ij u_i,t+e_ij,t`; bounded joint form: `y_j,t=alpha_ij+beta_ij x_i,t+gamma'f_t+e_ij,t` | two-stage OLS residualization primary; one joint linear estimator challenger after equivalence/PIT rules are frozen | `(H126,U1W)`, `(H252,U1M)` | complete PIT P0 factors plus aligned responses; factor and conditional-response uncertainty kept distinct; A3 receives factor-adjusted pre-decision `mu` |
| R2 | Allow registered company/pair characteristics to modify the expected pair relationship itself; target remains `y_j,t` | `y_j,t=[alpha_0+a'z_ij,t]+[beta_0+b'z_ij,t]x_i,t+gamma'f_t+e_ij,t`; bounded challenger permits a preregistered subset of nonlinear basis terms, not a black box | parsimonious linear interaction/varying-coefficient estimator primary; one regularized linear challenger | `(H126,U1W)`, `(H252,U1M)` | complete P0 plus PIT-vintaged P1 `z`; parameter and optional prediction uncertainty; A3 uses the conditioned pre-decision `mu` without using uncertainty as scale |
| R3 | Represent shared industry/group structure plus explicit pair deviations through hierarchical partial pooling; target remains `y_j,t` | `theta_ij,t=theta_g,t+Bz_ij,t+b_ij,t`, `y_j,t=alpha_ij,t+beta_ij,t x_i,t+gamma'f_t+e_ij,t`; bounded challenger changes shrinkage distribution, not target/information | hierarchical Gaussian shrinkage/empirical-Bayes estimator primary; at most one preregistered Bayesian or robust-shrinkage challenger | `(H126,U1W)`, `(H252,U1M)`, conditional `(H504,U1M)` | PIT group identity, complete P0 and authorized P1 when used; group/pair parameters and shrinkage-aware uncertainty; A3 receives pair-direction pre-decision `mu` |
| R4 | Interpretable time-varying relationship parameters; target is the one-step authorized directional response | observation `y_j,t=alpha_ij,t+beta_ij,t x_i,t+gamma_t'f_t+e_t`; state `theta_t=Gtheta_t-1+eta_t`; no unrestricted nonlinear/black-box dynamics | linear-Gaussian Kalman filter/state-space estimator primary; one robust observation-noise or local-level challenger | `(H63,U1D)`, `(H126,U1W)`, `(H252,U1M)`, conditional `(H504,U1M)` | PIT observations through `t-1`, explicit initialization/state clock; filtered forecast and calibrated state/prediction uncertainty; A3 uses pre-update forecast, then state update occurs in frozen order |
| R5 | Long-run equilibrium/cointegration relationship with short-run conditional adjustment; target is authorized `Delta p_j,t` or another preregistered response transformation | long run `p_j,t=a+beta p_i,t+u_t`; primary ECM `Delta p_j,t=lambda u_t-1+delta Delta p_i,t+e_t`; one single-equation alternative only, no broad VECM/regime-switching zoo | Engle-Granger plus single-equation ECM primary; one preregistered system/robust challenger only if separately authorized | `(H252,U1M)`, conditional `(H504,U1M)` | PIT price/adjustment eligibility, C04 limitations, no contemporaneous leakage; long-run state, conditional forecast, representation-specific uncertainty/diagnostics; A3 uses pre-decision directional forecast |

Distance, correlation, stationarity, cointegration, residual, likelihood, and state diagnostics remain representation-specific. They are not universal winner metrics. `correlation != normal relationship` and `distance != pair validity`.

## N0/N1 overlay map

| Relationship family | N0 strongly pooled baseline | N1 mandatory pair-specific challenger | Boundary |
|---|---|---|---|
| R0-S | shared/group reference construction where meaningful | pair-specific statistic | representation statistic is not itself R3 |
| R0-L | shared/group coefficients | pair coefficients or partial pooling | matched equation, target, P layer, H/U, and scale required |
| R1 | pooled factor/residual response structure | pair-specific residual response | factor set and residualization held fixed |
| R2 | pooled characteristic effects | pair-varying deviations around the same characteristic-conditioned form | complete P layer and feature roles held fixed |
| R3 | stronger hierarchical shrinkage | weaker shrinkage/more pair heterogeneity | R3 hosts both variants; `R3 != N1` |
| R4 | shared state-transition/noise structure | pair-specific state deviations where identifiable | state equation and information clock held fixed |
| R5 | pooled long-run/adjustment parameters where defensible | pair-specific long-run/ECM parameters | diagnostics and H support remain representation-specific |

An overlay is executable only where its pooling parameterization and identification are frozen. The N0/N1 comparison continues to isolate added pair-specific heterogeneity/adaptation under the A2 matched-comparison contract.

## P0/P1 map

| Family/version | P0 version | P1 version | Incremental boundary |
|---|---|---|---|
| R0-S | authorized market/industry context for construction and eligibility | only a separately registered economic/company filter or conditioning version | P1 contains complete P0; diagnostics cannot silently redefine pair validity |
| R0-L | source/peer response plus complete P0 controls | same equation/target with registered company/pair conditioning added | no P0 removal or target change |
| R1 | complete common-factor-adjusted specification | R1-P0 plus separately tracked company relationship information | P1 does not replace common-factor adjustment |
| R2 | R2-P0 permits only complete P0 conditioning | R2-P1 adds registered company/pair features to intercept/slope/strength | principal P1 family; complete P0 remains present |
| R3 | hierarchy/group structure plus complete P0 | same hierarchy plus registered P1 predictors of heterogeneity | pooling change and P-layer change cannot occur in the same incremental contrast |
| R4 | dynamic parameters with complete P0 | same state form plus preregistered P1 state/parameter conditioner | no outcome-driven state-input additions |
| R5 | long-run/ECM with complete P0 eligibility/context | same long-run target plus separately justified P1 conditioner | long-run representation and P increment remain separable |

`P1 = complete P0 + separately tracked Economic/Company Relationship information`.

A P1 version that removes, replaces, or changes P0 cannot claim P0-to-P1 incremental value.

## Mandatory per-candidate implementation record

Before computation, every concrete candidate ID must bind all of the following without relying on family defaults:

1. research role and G2B ancestry;
2. mathematical object and exact executable equation;
3. directional target variable and transformation;
4. explanatory variables and complete P0/P1 partition;
5. company/factor feature-set version;
6. observation/public/available/compute/decision timing contract;
7. estimator and estimation objective;
8. N0/N1 pooling or shrinkage structure;
9. regularization and penalty selection rule;
10. representation-specific minimum-history eligibility;
11. relationship update/state-transition rule and anti-circularity ordering;
12. explicitly authorized `(representation, H, U, feature set, estimator)` tuples;
13. finite hyperparameters and Search Budget entry;
14. point output, diagnostic output, and uncertainty output or explicit absence;
15. A3 directional abnormality interface;
16. production-feasibility, latency, cacheability, and dependency state.

## Company Feature Registry

The registry below defines bounded information families, not automatic covariates. Exact logical fields and transformations require later approval and must inherit the frozen source/PIT contracts.

| Feature family | Economic rationale | Feature Role | Information form | Source and PIT timing | P0/P1 | Limitations and authorized models |
|---|---|---|---|---|---|---|
| CF0 Scale / capital structure | size, financing capacity, leverage, and response transmission may condition heterogeneity | company state; pair difference/similarity; pooling prior; interaction/slope conditioner; rival/rejection context | level, pair difference/ratio, similarity, preregistered interaction | qualified PIT company/fundamental records; observation period differs from first-public/available time; update only on genuinely new releases | P1 | vintage/restatement and C04/share-capital gaps explicit; R2/R3, and R4 only if state role is registered |
| CF1 Profitability / quality | operating quality and balance-sheet resilience may explain response strength | company state; pair difference/similarity; pooling prior; interaction/slope conditioner; rival/rejection context | level, difference, similarity, limited interaction | first-public/available-time reconstructable fundamentals only; release-driven cadence | P1 | unavailable historical vintage means event-time prohibition; R2/R3 |
| CF2 Growth | differing growth state may alter economic linkage and expected response | company state; pair difference/similarity; interaction/slope conditioner; rival/rejection context | level, difference, similarity, limited interaction | PIT-vintaged company reports; release-driven cadence | P1 | restatement and sparse-update limitations; R2/R3 |
| CF3 Valuation | relative valuation may condition sensitivity but is not relationship validity itself | company state; pair difference/similarity; interaction/slope conditioner; rival/rejection context | level, relative/difference, similarity | PIT market value plus qualified denominator lineage; market numerator and slow denominator keep distinct clocks | P1 | denominator vintage/availability and near-zero quality states; R2/R3/R4 only when clocks are explicit |
| CF4 Liquidity / trading structure | activity and trading frictions may affect observed response and heterogeneity | common factor when authorized as market-state control; company state; pair difference/similarity; interaction/slope conditioner; rival/rejection context | level, pair difference/ratio, similarity, limited interaction | E02-A observed PIT activity; E02-B denominator-dependent fields retain `PASS WITH LIMITATIONS`; market/update cadence separately recorded | P0 only in an explicitly registered common-factor/control role; otherwise P1 | volume/amount is not turnover/free float or exogenous pressure; R1/R2/R3/R4 as explicitly registered |
| CF5 Business / subindustry / structural relationship | shared operations, exposure, or industry structure may explain linkage | common factor; pair similarity; pooling prior; interaction/slope conditioner; rival/rejection context | categorical match, taxonomy-aware distance/similarity, directed pair relation | official C06 PIT snapshots and separately qualified company/link information; carry-forward plus age/staleness state | C06 industry context may be P0; additional economic/company linkage is P1 | taxonomy/version and long-gap staleness preserved; R1/R2/R3/R4/R5 only where equation defines its role |

For every realized feature, the registry must additionally record feature ID/version, exact definition and units, explicit Feature Role, level/difference/similarity/interaction form, source artifact IDs, observation period, public and available times, update cadence, missingness/vintage state, authorized model families, and transformation lineage. One variable may occupy more than one role only through separate preregistered role bindings.

`variable identity != model role`.

`variable availability != automatic model inclusion`.

P1 may add registered information; it may not replace, remove, or silently redefine P0. A feature exposed by a provider remains excluded unless its economic role, PIT lineage, family authorization, and Search Budget entry are approved.

## Pooling, factor, and clock boundaries

- N0 is the strongly pooled baseline and N1 is the mandatory pair-specific challenger; neither is selected in advance, and neither is identical to a relationship family.
- P0/P1 and N0/N1 comparisons remain distinct paired incremental families under A2.
- factor observation/update clocks, company-release clocks, relationship-refresh cadence, market-evaluation cadence, and decision time remain distinct.
- U1D is highest adaptation, not a default. Daily evaluation does not imply daily refitting.
- an observation evaluated for abnormality cannot first be absorbed into the same-decision relationship estimate.
- H504 is restricted to preregistered representation-support contracts; poor performance cannot activate it.

## Search Budget and advancement

Each family has one primary estimator and at most one or a very small number of theoretically justified challengers. Authorized implementation candidates are an explicit tuple list, not the Cartesian product of all histories, cadences, features, estimators, penalties, lags, and state assumptions.

Every tuple must state whether each choice is theory/evidence-derived, market-calendar-derived, design choice, or development-selectable. New branches after outcome inspection require protocol reopening and contamination recording.

Complexity creates no advancement presumption. All candidates remain subject to TP2/CG2/OF4 nested pseudo-OOS, CS2 dual support, SR0 admissibility, SR1 non-forced hierarchical dominance, dependency-ordered multiplicity, and the registered sensitivity budget.

## Unresolved decisions and computation gate

The following remain unresolved for candidate-level freezing:

- executable equations, response transformations, intercept/trend/lag structures, and factor definitions;
- exact P0 factors and bounded P1 feature set;
- primary estimator and any single justified challenger per family;
- N0/N1 pooling priors/penalties and regularization-selection rules;
- representation-specific mathematical support and C04/C05 eligibility;
- explicit H/U tuple list, state initialization, and update timing;
- finite hyperparameters and inner-selection rules;
- uncertainty object and calibration contract;
- production latency, storage, and maintenance qualification.

Any entry with an unresolved equation, estimator, PIT input, update rule, or Search Budget is `NOT COMPUTATION-AUTHORIZED`.

`G4-05 CLARIFIED / AWAITING RESEARCHER APPROVAL`
