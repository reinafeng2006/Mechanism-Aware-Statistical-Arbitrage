# G4-05C R3 Hierarchical / Partial-Pooling Specification Clarification

Status: **FAMILY APPROVED IN PRINCIPLE / EXECUTABLE ESTIMATOR CLARIFIED BUT NOT FROZEN**
Boundary: no data inspection or fitting; no additional hierarchical family.

## Approved family and estimand

R3 asks whether information sharing across a preregistered PIT group, while retaining pair deviations, improves directional relationship estimation. R3 is a representation family, not N1. The initial scope is P0-only, with Gaussian empirical-Bayes random intercept and random slope.

For direction `i -> j`, pair `ij`, and PIT group `g`:

`y_ij,t = alpha_ij + beta_ij x_i,t + gamma'f_t + epsilon_ij,t`,

`[alpha_ij,beta_ij]' = [alpha_g,beta_g]' + b_ij`,

`b_ij ~ N(0,Omega_g)`, `epsilon_ij,t ~ N(0,sigma^2_e,g)`.

`R3-P1` is outside initial execution and may be proposed only after a qualified P1 enhancement layer. No Bayesian challenger or additional grouping family is introduced.

## Variance components and hyperparameters

Two bounded implementations of the same Gaussian family remain for selection:

1. `R3-ML`: maximize Gaussian marginal likelihood inside each authorized formation set;
2. `R3-REML`: use restricted marginal likelihood for `Omega_g` and observation variance while separating fixed-effect estimation.

The covariance parameterization, whether observation variance may be pair-specific, singular/boundary-fit handling, and any deterministic variance regularization remain unresolved. They cannot use an evaluated outer response, later outer fold, or held-out information.

## Shrinkage and N0/N1 semantics

The empirical-Bayes pair effect is the conditional Gaussian mean/mode under origin-specific estimated hyperparameters. N0/N1 is an orthogonal matched pooling contrast. The contract must select exactly one of:

- `N-ZERO`: N0 fixes pair-deviation covariance to zero; N1 estimates nonzero random-intercept/random-slope covariance; or
- `N-STRENGTH`: N0 and N1 use the same nonzero covariance family with preregistered stronger versus weaker shrinkage constraints.

These are alternatives, not simultaneous search branches. The contrast must hold fixed equation, P layer, group taxonomy, fixed effects, target, H/U, eligibility, and PIT information. Shrinkage intensity is neither relationship validity nor mechanism evidence.

## Outer-origin re-estimation and U refresh

At every outer origin, fixed effects, variance components, and pair conditional states are re-estimated solely from information authorized before that origin. Within an outer fold, an authorized U refresh may rerun the same frozen procedure using only newly elapsed eligible information; future-origin fits cannot be reused. Automatic temporal updating under a frozen rule is not manual retuning.

Existing tuple envelope only: `(H126,U1W)`, `(H252,U1M)`, and conditional `(H504,U1M)` where an independently approved support contract justifies H504. No tuple is added or selected here.

## PIT ordering

For a response evaluated at `t`:

1. obtain C06 group/taxonomy state and candidate-eligible formation records whose availability precedes `t`;
2. estimate or retrieve the outer-origin/U-authorized hyperparameters;
3. form empirical-Bayes pair states and the pre-response predictive distribution;
4. emit the directional expected response before observing the response being evaluated;
5. only afterward may the response enter a later authorized refresh.

Taxonomy/version, classification age and stale-gap state propagate. Future membership, outcome-based regrouping, and economic splicing of `601313.SH -> 601360.SH` are prohibited.

## Uncertainty output and A3 interface

The record must separate fixed-effect uncertainty, pair random-effect conditional uncertainty, variance-component estimation uncertainty where available, observation noise, and total predictive uncertainty. Plug-in empirical-Bayes intervals that omit hyperparameter uncertainty must say so. A1 assesses calibration separately. A3 receives only the pre-decision point expectation; uncertainty cannot scale point abnormality.

## Consolidated researcher decisions still required

1. `R3-ML` versus `R3-REML`;
2. covariance/observation-variance structure and singular-boundary handling;
3. `N-ZERO` versus `N-STRENGTH` matched N0/N1 semantics;
4. exact C06 grouping hierarchy across taxonomy changes;
5. executable H/U subset and uncertainty/calibration implementation.

R3 remains `NOT COMPUTATION-AUTHORIZED`.
