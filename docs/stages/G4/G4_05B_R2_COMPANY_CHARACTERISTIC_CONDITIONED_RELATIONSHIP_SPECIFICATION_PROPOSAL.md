# G4-05B R2 Company-Characteristic-Conditioned Relationship Specification Proposal

Status: **PROPOSED / AWAITING RESEARCHER REVIEW**
Boundary: preregistration design only. No frozen-data inspection, feature computation, fitting, selection, diagnostics, or outcome access.

## Objective

Specify how separately tracked PIT company and pair characteristics may condition the expected directional relationship itself while preserving complete P0 information and isolating P0-to-P1 incremental value.

`common-factor adjustment != company-characteristic conditioning`.

`P1 = complete P0 + separately tracked Economic/Company Relationship information`.

## Fixed target and interface inherited

R2 retains the same authorized signed directional-response target used by the matched P0 comparator. For `i -> j`, a bounded form is:

`r_j,t = alpha(z_ij,t) + beta(z_ij,t) r_i,t + gamma'f_t + epsilon_ij,t`,

with the reverse direction estimated separately. The pre-decision conditional expectation `mu_j|i,t` is passed to A3, which computes observed minus expected response under its frozen candidate-neutral scaling and anti-circularity rules. Company features and model uncertainty cannot enter the A3 scale denominator.

## Bounded equation roles to resolve

The proposal must later choose a small executable set from these roles without forming their Cartesian product:

1. `R2-I`: company/pair characteristics condition the intercept only;
2. `R2-S`: characteristics condition the directional slope only;
3. `R2-IS`: a parsimonious preregistered subset conditions intercept and slope;
4. one regularized linear challenger only if the authorized feature dimension requires shrinkage.

No black-box nonlinear learner, unrestricted interaction search, outcome-driven basis expansion, or automatic feature library is authorized.

## Feature-role contract

Every feature must bind an entry from the G4-05 Company Feature Registry to one explicit role: company state, pair difference, pair similarity, pooling prior, interaction/slope conditioner, or rival/rejection context. A variable used in multiple roles requires separate preregistered role bindings.

`variable identity != model role`.

Candidate feature families remain bounded to scale/capital structure, profitability/quality, growth, valuation, liquidity/trading structure, and business/subindustry/structural relationship. Exact fields, transformations, signs, interactions, and feature-set versions remain unresolved.

## PIT and missingness contract

- every company value uses its true first-public/available time and historical vintage;
- retrieval time cannot substitute for historical availability;
- later restatements cannot rewrite earlier feature states;
- slow company features update only when genuinely new PIT information arrives;
- missing or non-PIT-qualified values remain explicit and cannot be filled from future reports;
- feature availability at the decision origin is candidate-specific eligibility, not evidence of company state absence;
- C04/C05/C06, identifier, staleness, and provenance states continue to propagate.

## P0/P1 matched increment

Every R2-P1 candidate must retain the complete matched P0 comparator: response target, factor information, representation, estimator class where applicable, H/U geometry, N overlay, support rule, scale, and temporal role. The intended difference is only the registered P1 feature information and its preregistered parameter role.

A P1 candidate that removes or replaces P0 information, changes the target, or simultaneously changes unrelated estimation architecture cannot claim P0-to-P1 incremental value.

## N0/N1 overlay

N0 may impose shared/group characteristic effects and stronger pooling. N1 is the mandatory pair-specific heterogeneity challenger and may allow pair deviations around the same R2 equation and feature roles. R2 is a representation family; it is not synonymous with N1. Pooling structure, priors/penalties, and identifiability requirements remain to be frozen separately.

## Proposed H/U envelope

The working bounded envelope is `(H126,U1W)` and `(H252,U1M)`. These are candidate tuple components, not automatically executable combinations. H504 is unavailable to R2 absent a separate representation-specific structural support justification. U1D is not proposed because slow feature release cadence does not itself justify daily relationship refitting.

## Estimator and uncertainty candidates

Primary estimator proposed for later decision: linear interaction/varying-coefficient regression with intercept and a parsimonious fixed feature set. At most one regularized linear challenger may be retained, with penalty and inner-selection rules frozen before fitting.

Outputs must include directional expected response, coefficient/feature-role version, support and missingness state, and prediction uncertainty where the estimator supports a preregistered calibration procedure. Producing uncertainty is not itself an advantage, and uncertainty cannot mechanically reduce point abnormality.

## Search Budget and computation gate

An executable R2 tuple must bind equation role, exact P0 base, P1 feature set/version, feature roles, estimator, N overlay, H/U, regularization, eligibility rule, and uncertainty procedure. The registry may contain one primary estimator and at most one justified challenger; it may not enumerate all feature subsets or interactions.

Any unresolved equation, estimator, PIT input, feature role, pooling semantics, update rule, H/U authorization, or Search Budget leaves the candidate `NOT COMPUTATION-AUTHORIZED`.

## Researcher decisions required before freeze

1. select the bounded primary equation role: R2-I, R2-S, or R2-IS;
2. freeze the minimal feature-family set and exact permitted Feature Roles;
3. define pair difference/similarity transformations without empirical search;
4. select the primary estimator and decide whether one regularized challenger is justified;
5. freeze N0/N1 parameterization and matched P0 comparator;
6. authorize explicit H/U tuple IDs;
7. define missing-feature eligibility and vintage rules;
8. freeze uncertainty output/calibration and the finite Search Budget.

`G4-05B R2 SPECIFICATION PROPOSED / AWAITING RESEARCHER REVIEW`
