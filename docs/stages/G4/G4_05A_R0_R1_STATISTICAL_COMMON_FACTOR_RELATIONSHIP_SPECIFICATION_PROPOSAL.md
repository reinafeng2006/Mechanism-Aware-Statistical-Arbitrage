# G4-05A R0/R1 Statistical & Common-Factor Relationship Specification Freeze

Status: **G4-05A APPROVED / FROZEN — 2026-09-11**
Boundary: executable preregistration proposal only. No frozen-data inspection, fitting, residualization, pair construction, diagnostics, or outcome access.

## Shared notation and PIT contract

For security `k`, let `r_k,t` be the authorized one-period signed response ending at `t`, constructed only from observations passing the later frozen response-specific C04/C05 eligibility rule. For ordered pair `i -> j`, all estimators use a formation window ending strictly before the decision/evaluation observation. The observation evaluated by A3 is never included in its own same-decision fit.

`W_H(t) = {eligible synchronized observations strictly available before decision origin t under history H}`.

All means, scales, correlations, factor exposures, residuals, and relationship parameters are recomputed or carried forward only under the registered U rule. Full-sample estimation or residualization is prohibited. H/U labels specify the relationship-estimation clock, not market-observation cadence.

## R0-DIST — Distance representation

### Exact transformed object

For each security and PIT window `W_H(t)`, the exact transformed object is the complete synchronized, candidate-eligible path of cumulative one-period signed responses—not prices, levels, a directional forecast, or an outcome variable. Define:

`C_k,s(t,H) = sum_{q in W_H(t), q <= s} r_k,q`,

then normalize it using a candidate-neutral, security-level PIT path scale and location fixed from `W_H(t)`:

`Z_k,s(t,H) = [C_k,s(t,H) - median_{q in W_H(t)} C_k,q] / S_k,t,H`.

`S_k,t,H` is proposed as the MAD of that security's historical cumulative path within the same PIT window. Zero, non-finite, unavailable, or mathematically unsupported scales make DIST unavailable; no epsilon replacement is allowed. This normalization is a representation-only path normalization and is not the A1 directional-response loss scale.

### Distance and semantics

Primary distance:

`D_ij,t,H = |W_H(t)|^-1 * sum_{s in W_H(t)} [Z_i,s(t,H) - Z_j,s(t,H)]^2`.

This is a symmetric, non-directional path-proximity representation score: `D_ij = D_ji`. Lower distance means closer normalized historical response paths under this definition only. Its permitted downstream roles are representation description, bounded candidate comparison, and—only under a later authorized pair rule—possible pair-screening context. It is not a signed response, expected response, abnormality, mechanism variable, or pair-validity declaration.

`distance != pair validity`.

DIST cannot independently produce an expected directional response. Its A3 interface is therefore `NONE STANDALONE`: if DIST is used to define or stratify a relationship representation, a separately registered and versioned R0-LIN bridge must produce `mu_i->j,t` and `mu_j->i,t`. The bridge is not inferred from the distance value, and DIST may not be disguised as abnormality.

`representation score != directional expected response unless an explicit bridge is frozen`.

Proposed tuple menu: `(H63,U1W)`, `(H126,U1W)`, `(H252,U1M)`. Estimator: deterministic squared path distance only; no challenger is proposed. Output uncertainty is a support/scale-quality record, not a probabilistic forecast interval.

## R0-CORR — Correlation representation

### Primary and robustness candidates

On synchronized eligible responses in `W_H(t)`:

`rho^P_ij,t,H = PearsonCorr(r_i, r_j)`.

Pearson is the primary statistic. A single Spearman rank-correlation robustness diagnostic is registered to assess monotone/outlier sensitivity:

`rho^S_ij,t,H = PearsonCorr(rank(r_i), rank(r_j))`.

Spearman is a preregistered robustness diagnostic only. It cannot select a winner, rescue or replace Pearson after observing results, or create an alternative primary-selection environment. No additional correlation family is authorized.

PIT uncertainty is represented by sample support, missingness/synchronization state, and a preregistered correlation uncertainty interval or standard-error procedure still requiring exact specification. Correlation is symmetric and non-directional.

`correlation != normal relationship validity`.

CORR is a relationship representation only. It has `NONE STANDALONE` as its A3 interface, and this proposal does not freeze a correlation-to-beta algebraic shortcut. Its sole preregistered directional bridge is a separately fitted and versioned R0-LIN specification on the same authorized pair/support geometry. R0-LIN—not the correlation statistic—produces pre-decision `mu_i->j,t` and `mu_j->i,t`. Any future bridge requires its own equation, estimator, PIT contract, and Search Budget authorization.

Proposed primary tuples: `(H63,U1W)`, `(H126,U1W)`, `(H252,U1M)`. Spearman uses the identical tuple and support geometry when executed so that robustness does not change the estimand.

## R0-LIN — Signed directional linear response

For each direction, fit separately on `W_H(t)`:

`r_j,s = alpha_ij,t + beta_ij,t r_i,s + epsilon_ij,s`,

`r_i,s = alpha_ji,t + beta_ji,t r_j,s + epsilon_ji,s`.

The primary estimator is OLS with an intercept. The intercept is always estimated in the primary specification; omitting or shrinking it is not an unregistered alternative. One Huber M-estimation diagnostic is proposed solely for preregistered outlier-sensitivity robustness. It uses the same target, regressors, PIT window, intercept, and H/U tuple as OLS. Huber cannot select a winner, rescue or replace OLS after observing results, or create an alternative primary-selection environment.

At decision origin `t`, the A3 expected-response interface is:

`mu_j|i,t = alpha_ij,t- + beta_ij,t- r_i,t`,

with parameters `t-` estimated only from authorized information before the evaluated response. The reverse direction is retained separately. A3 computes observed minus expected directional response and applies its independent candidate-neutral MAD scaling.

Outputs include coefficients, fitted expected response, estimator/support state, residual diagnostics, and a candidate-specific prediction-uncertainty object where estimable. Prediction uncertainty remains separate from A3 point-abnormality scaling.

Proposed tuple menu: `(H63,U1D)`, `(H63,U1W)`, `(H126,U1W)`, `(H252,U1M)`. OLS is primary for each explicitly authorized tuple; Huber is one robustness-estimator branch whose execution must be separately Search-Budget authorized.

## R1 — Common-factor-adjusted directional relationship

R1 removes or conditions on shared market/industry/common-factor exposure. It does not use company fundamentals or allow company characteristics to modify pair parameters.

`factor adjustment != company-characteristic conditioning`.

### R1-M — Market-adjusted

First estimate each security's PIT market exposure on the same registered formation geometry:

`r_k,s = a_k,t + b_k,t m_s + u_k,s`, for `k in {i,j}`,

where `m_s` is the authorized E03-A market benchmark response. Then estimate the directional residual relationship:

`u_j,s = c_ij,t + d_ij,t u_i,s + e_ij,s`,

and separately the reverse direction.

Primary estimator: the fixed PIT residualization-and-pair OLS sequence below, with intercepts. A single joint linear challenger may later be authorized only if its equation, equivalence target, uncertainty propagation, and PIT ordering are frozen; it is not currently computation-authorized.

The A3 response forecast reconstructs the expected peer response from the PIT market component plus the directional residual component. Factor and residual uncertainty are reported separately and may not scale away point abnormality.

### R1-MI — Market + industry-adjusted

Use:

`r_k,s = a_k,t + b_k,t m_s + g_k,t q_g,s + u_k,s`,

followed by the same directional residual equation. `q_g,s` is a PIT industry benchmark/factor tied to the C06 taxonomy and membership state available at `s`. Its exact construction must exclude mechanical self/pair contamination under a preregistered rule and preserve classification-age/staleness metadata.

R1-M is the lower-complexity factor baseline; R1-MI is the bounded industry-adjusted challenger. R1-MI cannot change the response target, relationship equation, estimator, pooling overlay, H/U tuple, support rules, uncertainty procedure, or update ordering merely because it adds an industry factor.

### Fixed PIT residualization-and-pair-estimation sequence

At each authorized relationship-refresh origin `tau < t`, both R1-M and R1-MI must execute the same sequence:

1. construct the identical synchronized eligible formation set `W_H(tau)` using only artifacts available by `tau`;
2. bind `{m}` for R1-M or `{m,q_g}` for R1-MI; this factor-set addition is the sole intended difference;
3. estimate each security's factor equation by OLS with intercept on `W_H(tau)` under the same N0/N1 overlay and support rule;
4. calculate formation residuals using only those PIT-fitted parameters and the same formation observations—never full-sample or future-fitted residuals;
5. estimate both directional residual-pair equations by OLS with intercept on the same residual formation set, holding equation, estimator, pooling, history, refresh, and support fixed across M versus MI;
6. freeze factor and pair parameter versions until the next authorized U refresh;
7. at decision time `t`, use factor observations legitimately available by `t` and the frozen pre-decision exposure estimates to form current factor components and the source residual; combine the peer factor component with its frozen directional residual-pair forecast to obtain `mu_j|i,t`, retaining the reverse direction separately;
8. only after that forecast is fixed may the evaluated peer observation enter A3 departure computation; it cannot update the same-decision parameters first.

If a required contemporaneous factor is unavailable by decision time, the R1 expected response is unavailable under that rule rather than backfilled. R1-M and R1-MI use matched common support; native-support loss from industry-factor availability is reported separately.

`R1-M vs R1-MI must isolate factor-information differences rather than simultaneous changes in estimation architecture`.

Proposed R1 tuples: `(H126,U1W)` and `(H252,U1M)`. The factor-exposure and pair-residual estimators share the authorized formation origin; factor data must be available before the decision origin. R1-M and R1-MI are compared only on matched common support under CS2, with native support separately reported.

## Additional factor extensions

Size, value, momentum, quality, or liquidity extensions are `REGISTERED CONCEPTUAL CHALLENGERS / NOT AUTHORIZED`. Any one extension requires an explicit economic rationale, exact factor definition, PIT-qualified source and construction, self-contamination rule, finite H/U tuple, and separate Search Budget approval before it can enter this registry. A factor library or outcome-driven factor addition is prohibited.

## N0/N1 overlay

| Specification | N0 stronger-pooling form | N1 pair-specific form | Required matched dimensions |
|---|---|---|---|
| R0-DIST | group/reference distance distribution or shared normalization rule where justified | pair-specific distance statistic | transformed object, window, normalization, and update rule |
| R0-CORR | group/reference correlation structure where justified | pair-specific correlation | response series, H/U, support, and uncertainty procedure |
| R0-LIN | shared/group `alpha,beta` | pair-specific or partially pooled `alpha_ij,beta_ij` | equation, estimator, target, H/U, scale, and P layer |
| R1-M | pooled market exposures/residual relation where identifiable | security/pair-specific exposures and residual response | market factor, residualization, target, H/U, and support |
| R1-MI | pooled market/industry exposures/residual relation | security/pair-specific exposures and residual response | market/industry factors, taxonomy, residualization, H/U, and support |

This table registers mathematical applicability only. It selects neither N0 nor N1. DIST/CORR pooling forms require a later exact estimator and therefore remain `NOT COMPUTATION-AUTHORIZED`.

## P0/P1 boundary

R0 and R1 versions in G4-05A are P0. Market and industry factors remain shared-context P0 inputs; their economic interpretation does not make them P1.

Any later P1 version must equal the complete matched P0 specification plus separately tracked Economic/Company Relationship information. Adding P1 belongs to a separate registered comparison and cannot silently alter the factor set, target, estimator, support, or H/U geometry.

## Search Budget

Primary branches are R0-DIST, R0-CORR-Pearson, R0-LIN-OLS, R1-M, and R1-MI under only the listed H/U tuples. Spearman and Huber are preregistered robustness diagnostics outside winner selection; the R1 joint form and any additional factor are not authorized without a later explicit entry.

The list is not a Cartesian product. Each executable candidate must receive one immutable tuple ID binding representation, estimator, H, U, N overlay, P layer, factor version, eligibility rule, and uncertainty procedure before fitting.

## Remaining specification decisions

1. exact response construction and candidate-specific C04/C05 eligibility rule;
2. R0-DIST path-start convention and sufficient mathematical support rule;
3. Pearson/Spearman uncertainty procedure and mathematical support rule;
4. Huber tuning constant and whether the registered robustness branch will execute;
5. R0-LIN prediction-uncertainty procedure;
6. exact market benchmark and industry-factor construction, including self/pair exclusion;
7. R1 factor-exposure versus relationship-update synchronization;
8. exact N0/N1 estimators for each applicable specification;
9. which listed H/U tuple IDs enter the primary comparison versus registered sensitivity budget;
10. regularization, if any, and all estimator-support requirements.

Until these items and the full candidate tuple records are frozen, all G4-05A candidates remain `NOT COMPUTATION-AUTHORIZED`.

`G4-05A APPROVED / FROZEN`
