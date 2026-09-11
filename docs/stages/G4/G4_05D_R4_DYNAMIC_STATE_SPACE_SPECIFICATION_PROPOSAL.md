# G4-05D R4 Dynamic / State-Space Specification Proposal

Status: **BOUNDED PROPOSAL / AWAITING CONSOLIDATED RESEARCHER DECISION**
Boundary: interpretable linear dynamics only; no fitting or data inspection.

## Estimand

R4 asks whether an interpretable, PIT-filtered evolution of relationship parameters improves the expected directional response relative to a matched static relationship, without allowing the evaluated abnormal observation to erase its own departure.

Observation equation:

`y_j,t = alpha_ij,t + beta_ij,t x_i,t + gamma'f_t + epsilon_ij,t`, `epsilon_t ~ N(0,R)`.

### `R4-RW` — local random-walk state

`theta_ij,t = theta_ij,t-1 + eta_ij,t`, `eta_t ~ N(0,Q)`.

Tests gradual parameter drift with no fixed long-run mean. Primary estimator candidate: linear-Gaussian Kalman filter with pre-decision prediction followed by post-observation state update.

### `R4-MR` — mean-reverting state challenger

`theta_ij,t-mu_g = Phi(theta_ij,t-1-mu_g) + eta_ij,t`, with preregistered stable `Phi`.

Tests whether parameter changes are temporary deviations around a shared state. This is the sole bounded dynamic challenger; no switching regimes, trees, neural nets, particle-filter zoo, or outcome-triggered state specification is authorized.

## Ordering and clock contract

At decision time: (1) carry/filter state using information through the prior authorized update; (2) form `mu_j|i,t` before observing the peer response being evaluated; (3) compute A3 departure; (4) only then may the observation update the state for a later decision. This ordering applies under U1D.

Market evaluation cadence is distinct from state/relationship refresh. Missing or ineligible observations generate an explicit no-measurement/update state under a later frozen rule; they are not zero innovations.

## N/P and geometry

N0 may share `Q/R/Phi` or group states; N1 may permit pair deviations under an identical state equation. P0 is primary. P1 state conditioners require the B1 enhancement and a separate matched incremental specification.

Existing envelope only: `(H63,U1D)`, `(H126,U1W)`, `(H252,U1M)`, and conditional `(H504,U1M)`. State initialization, covariance estimation, and which tuple IDs execute remain unresolved; no grid expansion is authorized.

## Outputs

Pre-decision directional forecast, filtered/predicted parameter state, covariance and innovation-quality state, initialization/version metadata, and support/eligibility. Forecast uncertainty is a separate calibration channel, not A3 scaling.

## Scientific decisions required

1. R4-RW primary versus R4-MR challenger status/execution;
2. which parameters vary: intercept, slope, or both;
3. `Q/R/Phi` estimation/regularization and finite inner-selection budget;
4. state initialization and missing-observation update rule;
5. N0/N1 sharing structure and P0/P1 boundary;
6. executable H/U tuple subset and uncertainty calibration.

R4 remains `NOT COMPUTATION-AUTHORIZED`.

