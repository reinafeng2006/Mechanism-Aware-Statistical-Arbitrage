# G4-05B2 R2 Exact Equation and Estimator Proposal

Status: **R2-LIS + OLS/RIDGE APPROVED / V1 NOT DATA-READY / PRESERVED FOR V2**
Boundary: no data inspection or fitting. B1 constructs and transformations are unchanged.

## Matched P0 anchor

For direction `i -> j`, let `mu^P0_ij,t` be the frozen matched R0-LIN or R1 expected response under a named representation, factor set, N overlay, H/U tuple, eligibility rule, and temporal origin. R2 adds only PIT B1 P1 state.

## Bounded exact alternatives

### `R2-LI` — level/intercept conditioning

`y_j,t = alpha_ij + a'z_ij,t- + beta_ij x_i,t + gamma'f_t + epsilon_ij,t`.

Tests whether company/pair state shifts expected response level while transmission slope stays matched to P0. OLS with intercept is the primary estimator.

### `R2-LS` — slope conditioning

`y_j,t = alpha_ij + [beta_ij + b'w_ij,t-]x_i,t + gamma'f_t + epsilon_ij,t`.

Tests whether company/pair state changes source-to-peer transmission. OLS with intercept is primary; only frozen source-response interactions may enter.

### `R2-LIS` — approved initial parsimonious level-and-slope conditioning

`y_j,t = alpha_ij + a'z_ij,t- + [beta_ij + b'w_ij,t-]x_i,t + gamma'f_t + epsilon_ij,t`.

Tests both channels but requires a researcher-frozen minimal assignment of B1 bundles to `z` versus `w`; no feature may occupy both roles automatically.

### `R2-RIDGE` — approved sole regularized challenger

For the selected linear equation only:

`theta_hat(lambda)=argmin_theta sum_s (y_j,s-X_ij,s theta)^2 + lambda||P theta||_2^2`,

where `P` leaves the intercept unpenalized and penalty candidates are selected only inside frozen inner development. OLS is primary and Ridge is the sole regularized challenger. Elastic net is outside the initial architecture.

`R2-N` is `DEFERRED / NOT REJECTED / NOT INITIAL EXECUTION`. Poor R2-LIS results cannot activate it. Activation requires a separately preregistered functional-form inadequacy rationale and explicit researcher authorization before the relevant outcomes are inspected.

## Fixed implementation semantics

- reverse direction is estimated separately with directed transformations rebuilt;
- company state is the latest qualifying vintage available before the decision origin;
- carry-forward does not create a daily update;
- the same P0 target, factors, representation, N overlay, H/U, scale, and support are retained;
- output is pre-decision `mu_j|i,t` plus feature-vintage/support and separate uncertainty metadata;
- A3 receives the point expectation only; uncertainty never scales departure;
- B1 data absence makes R2 unavailable, not zero or P0-equivalent.

## Existing tuple envelope preserved

No Search Budget is changed. The previously registered geometry IDs remain: `R2L-126W`, `R2L-252M`, `R2R-126W`, `R2R-252M`, and conditional `R2N-252M`. The R2-N tuple is retained only as deferred registry ancestry and is not authorized to execute.

## Remaining execution gates

The exact minimal B1 feature-to-`z`/`w` allocation, logical/physical PIT fields, P1 enhancement version, Ridge penalty menu and inner-selection rule, and executable H/U tuples remain scientific decisions. The existing-source audit did not qualify the five accounting-derived constructs, and market capitalization alone is not a coherent substitute for the frozen P1 information set. R2 is therefore `V1 NOT DATA-READY`; it remains `NOT COMPUTATION-AUTHORIZED` and is preserved for V2 without weakening PIT requirements.
