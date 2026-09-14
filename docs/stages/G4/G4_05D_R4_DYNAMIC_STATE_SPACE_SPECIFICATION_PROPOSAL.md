# G4-05D R4 Dynamic / State-Space Specification Clarification

Status: **PRIMARY ARCHITECTURE APPROVED IN PRINCIPLE / EXECUTABLE VARIANCE-CLOCK CONTRACT NOT FROZEN**
Boundary: interpretable linear dynamics only; no fitting or data inspection.

## Approved primary architecture

R4 asks whether PIT-filtered evolution of the transmission slope improves directional expected response relative to a matched static relationship without letting an evaluated observation erase its own departure.

`R4-RW` uses a static intercept and random-walk slope:

`y_j,t = alpha_ij + beta_ij,t x_i,t + gamma'f_t + epsilon_ij,t`, `epsilon_ij,t ~ N(0,R_ij)`,

`beta_ij,t = beta_ij,t-1 + eta_ij,t`, `eta_ij,t ~ N(0,Q_ij)`.

The primary estimator is the linear-Gaussian Kalman filter. `R4-MR`, with `beta_ij,t-mu_g = phi(beta_ij,t-1-mu_g)+eta_ij,t`, is `REGISTERED / DEFERRED / NOT INITIAL EXECUTION`. No HMM, regime-switching, particle-filter, nonlinear, or black-box state-space family is authorized.

## State and observation variance

`Q_ij` governs permitted slope evolution; `R_ij` governs observation noise. They are not interchangeable tuning parameters. Three bounded treatments remain for researcher selection:

1. fixed ex ante under a separately justified deterministic rule;
2. PIT maximum-likelihood estimation inside each authorized formation set;
3. a very small preregistered set of variance regimes selected only by the frozen inner procedure.

No unrestricted grid or outer-fold retuning is permitted. Shared/group versus pair-specific `Q/R`, boundary estimates, and regularization remain unresolved.

## Initialization

At each outer origin, initialize static `alpha_ij`, prior slope mean `m_beta,0`, and prior slope variance `P_beta,0` solely from the authorized PIT formation history. Two bounded initializers remain:

- matched static R0/R1 directional estimate plus its estimation uncertainty; or
- group-pooled P0 initializer under a separately frozen N overlay.

Diffuse initialization is not assumed and would require a finite preregistered variance. Initializer choice may not depend on outer results.

## U cadence and state time

Market/abnormality evaluation cadence is distinct from relationship refresh:

- `U1D`: after an observation has been evaluated, an eligible measurement may update the filter for the next decision;
- `U1W`/`U1M` primary clarification: daily predictions use the last authorized filtered state plus state evolution, while measurement updates are batched only at scheduled weekly/monthly refreshes using information then available;
- a sequential-filter-but-publish-on-refresh interpretation creates a different information path and requires explicit selection; it cannot be silently substituted.

Missing or ineligible observations cause prediction without measurement update and retain their reason state; they are not zero innovations. Whether `Q` accumulates in calendar time or eligible-trading time must be frozen before execution.

Existing tuple envelope only: `(H63,U1D)`, `(H126,U1W)`, `(H252,U1M)`, and conditional `(H504,U1M)`. No tuple is added or selected here.

## PIT filtering and prediction order

For an evaluated response at `t`:

1. use only the last authorized filtered state and information available strictly before the response;
2. perform the state prediction and emit `mu_j|i,t`;
3. after the response arrives, compute A3 departure against that frozen prediction;
4. only then may the response enter a later authorized measurement update.

Filtered and one-step-ahead predicted states must be separately labelled. Smoothing with future observations is prohibited for event-time output. This order applies even under U1D.

## N/P and uncertainty

N0 may share variance/state structure; N1 may permit pair deviations only under an otherwise identical state equation, initializer, H/U, target, support, and PIT path. P0 is initial. P1 requires the separately qualified B1 enhancement and a matched incremental specification.

Output includes the pre-decision point forecast, predicted/filtered slope state, covariance, innovation-quality state, initialization/version metadata, eligibility, and separate predictive uncertainty. Uncertainty is a calibration channel, not A3 scaling.

## Consolidated researcher decisions still required

1. fixed, PIT-estimated, or bounded inner-selected `Q/R`, including shared versus pair-specific structure;
2. matched-static versus group-pooled initializer and finite prior-variance rule;
3. batched `U1W/U1M` measurement updates versus the separately defined sequential-filter interpretation;
4. calendar-time versus eligible-trading-time state evolution;
5. N0/N1 sharing structure, executable H/U subset, and uncertainty calibration.

R4 remains `NOT COMPUTATION-AUTHORIZED`.
