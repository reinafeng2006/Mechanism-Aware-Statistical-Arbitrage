# G4-05B R2 Company-Characteristic-Conditioned Relationship Specification

Status: **G4-05B R2 CLARIFIED / AWAITING RESEARCHER APPROVAL**
Boundary: preregistration design only. No frozen-data inspection, feature computation, model fitting, selection, diagnostics, or outcome access.

## R2 estimand

R2 asks whether separately tracked PIT company/economic state provides incremental information about the expected directional pair relationship beyond the complete matched P0 information set. The estimand concerns modification of preregistered relationship parameters—level/intercept, response slope/strength, directional asymmetry, or another explicitly authorized parameter—not generic standalone return prediction.

`company information predicts returns != company information conditions the pair relationship`.

`P1 = complete P0 + separately tracked Economic/Company Relationship information`.

For direction `i -> j`, let `x_i,t` be the authorized source response, `y_j,t` the peer response, `f_t` the complete P0 controls, and `z_ij,t-` the company/pair state genuinely available before decision time. Every R2 version retains the matched P0 target, representation, factor information, temporal role, eligibility, H/U geometry, and N overlay.

## Ordered complexity ladder

The authorized conceptual order is:

`R2-L interpretable linear/interacted conditioner -> R2-R regularized conditioner -> R2-N controlled nonlinear conditioner`.

These are escalation levels, not an unrestricted parallel tournament. A higher level may advance only by demonstrating incremental relationship value under frozen TP2/CG2/OF4 nested pseudo-OOS, CS2, SR0-to-SR1, dependency-ordered multiplicity, and non-forced-winner rules. Complexity cannot be activated after outcomes merely to rescue a weaker lower level.

## R2-L — Interpretable linear/interacted conditioner

Primary bounded equation:

`y_j,t = alpha_0 + a'z_ij,t- + [beta_0 + b'w_ij,t-] x_i,t + gamma'f_t + epsilon_ij,t`.

- `a'z` is level/intercept conditioning: company or pair state shifts the expected response level;
- `b'w * x_i` is slope/response conditioning: only economically justified registered state modifies transmission strength;
- `z` and `w` may contain separately authorized directed levels, signed differences, absolute differences, or similarities;
- direction `j -> i` is fitted separately with its directed feature transformations rebuilt for that direction;
- pair asymmetry is preserved rather than averaged away.

Primary estimator: OLS with intercept on a fixed parsimonious feature/interaction set. No automatic interaction generation, stepwise search, or feature-subset search is authorized. Candidate-specific prediction uncertainty is recorded separately and cannot scale A3 abnormality.

## R2-R — Regularized conditioner

R2-R uses the same target, P0 base, feature-role definitions, interaction design, direction, H/U geometry, and eligibility as its matched R2-L comparator:

`theta_hat = argmin_theta sum_s (y_j,s - X_ij,s theta)^2 + lambda ||theta||_2^2`.

Ridge is the recommended primary regularization family because the bounded company states, pair transformations, and slope interactions are expected to be correlated, while the research question does not presuppose that only a sparse subset is economically real. Ridge stabilizes the full preregistered design without turning variable inclusion into another search layer.

Elastic net is not an authorized co-primary tournament branch. It may be retained only as one separately approved challenger if a sparse-plus-grouped economic hypothesis and its mixing rule are preregistered before outcomes. Lasso alone is not registered. `lambda`, and any authorized elastic-net mixing value, may be selected only within the frozen semiannual inner-development process; outer folds and held-out information cannot tune them.

## R2-N — Controlled nonlinear conditioner

R2-N permits one interpretable additive/spline-style extension:

`y_j,t = alpha_0 + sum_k g_k(z_k,ij,t-) + [beta_0 + sum_l h_l(w_l,ij,t-)] x_i,t + gamma'f_t + epsilon_ij,t`.

Each `g_k` or `h_l` is a prespecified low-dimensional smooth function for an authorized continuous feature; the number of terms, basis family, degrees of freedom/knots, monotonicity if any, and penalty are frozen before fitting. The additional hypothesis is that relationship level or transmission changes smoothly through saturation, threshold-like transition, or diminishing-return behavior that a single linear effect cannot express.

R2-N does not authorize trees, random forests, boosting, neural networks, unrestricted kernels, regime-switching discovery, or automatic nonlinear/interaction searches. Only one additive/spline family may enter the R2 Search Budget, and only after its increment over matched R2-L/R2-R is defined.

## Company Feature Role Registry

Raw candidate variables are conceptual logical fields, not selected physical fields and not automatic model inputs. Every realized variable still requires a PIT-qualified source contract and exact definition.

| ID / economic construct | Bounded raw candidate variables | P0/P1 | Permitted Feature Roles | Permitted pair transformations | PIT source, availability, cadence, and limitations | Authorized R2 levels |
|---|---|---|---|---|---|---|
| CF0 Scale / capital structure | PIT market capitalization; total assets; equity; debt/leverage; total/circulating/free-float shares where qualified | P1 | company state; pair difference/similarity; pooling prior; slope conditioner; rival/rejection context | directed level; signed difference; absolute difference; similarity; one registered source-response interaction | PIT-vintaged company filings and qualified share-capital lineage; use first-public/available time; release/share-change update only; age retained; E02-B and restatement limitations explicit | L, R; N only for one justified size/leverage smooth |
| CF1 Profitability / quality | ROA/ROE-type profitability; operating margin; cash-flow/earnings quality measure | P1 | company state; pair difference/similarity; pooling prior; slope conditioner; rival/rejection context | level; signed/absolute difference; similarity; interaction only with explicit transmission rationale | PIT-vintaged filings; release-driven; publication lag, restatement, missing vintage, and feature age retained | L, R; N only for one justified profitability smooth |
| CF2 Growth | revenue growth; operating-profit/earnings growth; asset growth | P1 | company state; pair difference/similarity; slope conditioner; rival/rejection context | level; signed/absolute difference; similarity; interaction only if direction is justified | PIT-vintaged reports; release-driven; denominator/base-period quality and revisions preserved | L, R; N only with prespecified saturation hypothesis |
| CF3 Valuation | book-to-market or price-to-book; earnings yield or price/earnings where denominator is valid | P1 | company state; pair difference/similarity; slope conditioner; rival/rejection context | level; signed/absolute difference; similarity; bounded interaction | PIT market numerator plus PIT-qualified accounting denominator; mixed clocks retained; nonpositive/undefined denominator and restatement states explicit | L, R; N only for one justified smooth |
| CF4 Liquidity / trading structure | E02-A volume/amount/activity; E02-B turnover, total/circulating/free-float denominator fields where qualified | P0 only when already frozen as shared market-state control; otherwise P1 | company state; pair difference/similarity; slope conditioner; rival/rejection context | level; signed/absolute difference; similarity; bounded interaction | E02 lineage; market observations update at their own cadence, denominators only on genuine changes; E02-B remains `PASS WITH LIMITATIONS`; volume/amount is not turnover/free float | L, R; N only with explicit friction/saturation hypothesis |
| CF5 Business / subindustry / structural relationship | C06 taxonomy membership; subindustry match; separately qualified business/exposure linkage | C06 shared context may be P0; additional relationship information is P1 | pair similarity; pooling prior; slope conditioner; rival/rejection context | exact match; taxonomy-aware similarity/distance; directed relation; interaction only if linkage modifies response | official C06 PIT snapshots plus separately qualified linkage sources; carry-forward with snapshot, taxonomy, age, and stale-gap state; current membership never backfilled | L, R; N not authorized absent separate structural justification |

`raw variable != automatically authorized transformation`.

`variable identity != model role`.

A raw variable may enter only through a registered `(feature ID, definition/version, direction, role, transformation)` binding. Using the same variable in another role or transformation is a new Search Budget entry.

## PIT low-frequency state-update contract

For a slow company feature with report observation period `p`, its state becomes usable only at its defensible `available_time`. At decision time `t`, the feature state is the latest qualifying vintage with `available_time <= t`, accompanied by source/vintage ID, observation period, available time, feature age, staleness state, transformation version, and missingness/revision state.

The latest public state may be carried forward between genuine releases. Carry-forward creates no new evidence record and does not reset age:

`PIT carry-forward != daily information update`.

Restatements create a new later vintage and never rewrite the value visible to an earlier decision. Missing, non-finite, unavailable, or non-PIT-qualified fields remain explicit. Future values, retrieval timestamps, cross-sectional hindsight, silent imputation, and assumed freshness are prohibited.

## P0/P1 matched-comparison contract

For every R2 P1 candidate and its P0 comparator, hold fixed pair, direction, decision origin, target, complete P0 variables, relationship representation, factor-adjustment architecture, estimator geometry where logically possible, N0/N1 overlay, H/U tuple, candidate-neutral scale, temporal role, and common-support eligibility. The only intended increment is the registered P1 feature state in its frozen parameter role.

If adding a feature necessarily changes an estimator, the comparison record must name that difference as part of the estimand; it cannot be silently attributed to company information. R2 may not remove P0 variables or change unrelated geometry while claiming P1 value. Native-support losses from feature availability are reported separately under CS2 and cannot compensate for worse common-support relationship evidence.

## Bounded Search Budget

The proposed registry contains five explicit geometry-level tuple IDs; feature-set and N-overlay versions must be frozen within each ID before it becomes executable:

| Tuple ID | Complexity | Equation/estimator | H/U | Permitted purpose |
|---|---|---|---|---|
| `R2L-126W` | R2-L | fixed linear/interacted design, OLS | `(H126,U1W)` | primary interpretable geometry |
| `R2L-252M` | R2-L | same fixed design, OLS | `(H252,U1M)` | preregistered longer/slower geometry |
| `R2R-126W` | R2-R | matched design, ridge | `(H126,U1W)` | regularization increment on matched geometry |
| `R2R-252M` | R2-R | matched design, ridge | `(H252,U1M)` | regularization increment on longer/slower geometry |
| `R2N-252M` | R2-N | one frozen additive/spline design | `(H252,U1M)` | controlled nonlinear escalation only |

These five entries are not automatically all executed. Primary versus sensitivity execution, exact feature-set IDs, and N0/N1 pairings must be frozen without creating `feature x transformation x interaction x estimator x H x U` combinations. H504 and U1D are not authorized for R2. Elastic net requires explicit replacement/challenger authorization and does not silently add a sixth primary branch.

## Downstream interface and uncertainty

Each authorized direction emits pre-decision `mu_j|i,t`, coefficient/function and feature-role versions, feature vintage/age states, eligibility/support state, and an uncertainty object if supported by a separately frozen calibration procedure. A3 receives only the pre-decision point expectation for observed-minus-expected departure; candidate uncertainty remains a separate channel.

## Remaining decisions before freeze

1. choose the primary R2-L role set: intercept, slope, or a minimal combination;
2. select exact raw variables and one bounded feature-set version from the registry;
3. freeze transformations, direction conventions, similarity definitions, and authorized interactions;
4. determine whether both R2-L geometries are primary/robustness or whether one closes;
5. freeze ridge penalty-selection grid/rule and decide whether elastic net is rejected or separately justified;
6. decide whether the R2-N economic hypothesis merits inclusion, then freeze its basis and smoothness budget;
7. freeze N0/N1 parameterization and tuple pairing without confounding pooling with company information;
8. specify mathematical estimator support, missing-feature eligibility, and uncertainty/calibration output;
9. bind each feature to a qualified source/field/vintage contract or leave the affected tuple blocked;
10. freeze the finite execution and multiplicity budget.

Any unresolved equation, estimator, PIT input, feature-role/transform binding, pooling semantics, update rule, H/U authorization, or Search Budget leaves that candidate `NOT COMPUTATION-AUTHORIZED`.

`G4-05B R2 CLARIFIED / AWAITING RESEARCHER APPROVAL`
