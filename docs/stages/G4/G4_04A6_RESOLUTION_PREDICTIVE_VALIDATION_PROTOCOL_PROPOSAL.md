# G4-04A6 Resolution / Predictive Validation Protocol Proposal

Status: **SCI-A APPROVED / FROZEN FOR V1 — INNER DEVELOPMENT ONLY**

Executable design-matrix binding: `V1-EXECUTABLE-SEMANTICS-A1`. The exact ordered PV0/PV-M1/PV-M2/PV-BOTH columns, optional-value indicator encoding, mandatory-value exclusion, full-rank disposition, and no-future-target rule in that amendment are frozen before empirical access and supersede any residual ambiguity in the information-set descriptions below.

## Estimand and scientific boundary

A6 asks whether event-time-frozen abnormality and admissible mechanism-evidence channels improve prediction of the frozen A5 continuous resolution vector at O1/O5/O10/O20, relative to a relationship/abnormality-only baseline, under matched CS2 support.

`resolution prediction != mechanism identification != trading profitability`.

Trading outcomes cannot select, redefine, or rescue A6. Future observations evaluate but never rewrite event-time forecasts, abnormalities, evidence records, source/peer roles, or information sets.

## Proposed exact continuous targets

Let `g_j,t = mu_j|i,t - y_j,t` be the frozen signed peer response gap and `e_i,t` the source-side event-time excess component under the paired directional state. Let `Delta_h y_j` and `Delta_h y_i` denote future cumulative responses in the same response representation from immediately after `t` through O_h. Let `S_j,t` and `S_i,t` be event-time candidate-neutral PIT MAD scales, frozen at `t`.

For each horizon with a complete authorized interval, propose:

- catch-up displacement `RT0_h = sign(g_j,t) * Delta_h y_j / S_j,t`; positive means movement along the gap-closing direction, without imposing a binary closure threshold;
- source normalization `RT1_h = -sign(e_i,t) * Delta_h y_i / S_i,t`; positive means movement against the source excess direction;
- residual persistence `RT2_h = |g_j,t - Delta_h y_j| / S_j,t` together with the signed residual gap; no event is forced to resolve;
- relationship continuation/change `RT3_h = median_{q=t+1...t+h} |y_j,q - mu^t_j|i(x_i,q,f_q)| / S_j,t`, where `mu^t` uses the relationship equation and parameters frozen at event time `t` and future `x/f` only as outcome-side realized inputs. Lower RT3 means greater continuation adequacy; larger RT3 is continuous change/break evidence. Any later-refitted comparison is a separately labelled diagnostic and cannot rewrite `t`.

If `g_j,t`, `e_i,t`, a required scale, endpoint, or interval is structurally unavailable, the corresponding component is unavailable with reason metadata. Simultaneous positive RT0 and RT1 is permitted. No universal convergence score or binary label is created.

RT0/RT1 use endpoint cumulative response in V1. Path-integral alternatives are closed. Representation-only R0-DIST/CORR use their matched R0-LIN bridge for RT3.

## Predictive models and matched incremental estimands

Use one interpretable predictive equation family only: horizon/component-specific linear prediction with intercept, fitted inside semiannual inner development. For component `c` and horizon `h`:

`RT_c,h = a_c,h + b_c,h' X_t + error_c,h`.

Nested information sets:

1. `PV0`: relationship-validity, raw/scaled A3 abnormality, scale/uncertainty, and eligibility/support state;
2. `PV-M1`: complete PV0 plus authorized UR0 and qualified UR1/context records;
3. `PV-M2`: complete PV0 plus MP0 and MP1 channels with contamination state;
4. `PV-BOTH`: complete PV0 plus the separately tracked M1 and M2 channels, without forcing exclusivity; diagnostic only in V1.

M0/U states enter as explicit quality/rejection/ambiguity context, not pseudo-probabilities. Ridge may be used only as the sole bounded regularized challenger if the researcher explicitly includes it in the A6 Search Budget; otherwise OLS is primary and sole V1 estimator.

Primary paired estimands on common support:

`DeltaLoss_M1 = Loss(PV-M1) - Loss(PV0)`,

`DeltaLoss_M2 = Loss(PV-M2) - Loss(PV0)`,

`DeltaLoss_BOTH = Loss(PV-BOTH) - Loss(PV0)`.

Negative values mean lower OOS resolution-prediction loss. M1 and M2 families remain distinct; PV-BOTH tests coexistence and does not create a mechanism label.

## Metrics and aggregation

Inherit A1 rather than introduce a new metric family:

- primary: absolute OOS error of the already candidate-neutral, event-time-scaled RT component;
- robustness: squared error of that same dimensionless component;
- uncertainty/calibration: separate when predictive intervals are emitted;
- supporting: sign/directional concordance, censoring, support and coverage diagnostics only.

No second candidate-dependent normalization is introduced: RT0–RT3 already inherit event-time candidate-neutral response scaling. Candidate forecast uncertainty remains a separate calibration channel. A1c hard failures and continuous scale-quality semantics apply.

Aggregate in the frozen hierarchy: observations within direction → equal-status directions within pair → equal-pair median on common support → semiannual origins/OF4 median-vector. Preserve magnitude, directional consistency, dispersion, genuinely severe failure, and support separately. No scalar score or arbitrary threshold.

## Horizons, censoring, and dependence

- O1/O5/O10/O20 are validation horizons, not holding periods.
- Each target interval must remain wholly inside its inner, outer, or held-out temporal role.
- Overlapping target labels are not independent. Training labels whose future interval reaches an evaluation origin are purged through target-horizon-aware censoring; embargo beyond the label horizon is not imposed absent separate dependence justification.
- For a model predicting O_h at evaluation origin `t`, the last training decision origin must have its complete O_h outcome available before `t`.
- 2023 outcomes cannot cross into 2024; 2024–2025 remains sealed.

## V1 A6 Search Budget proposal

The frozen V1 budget avoids a target × horizon × information-set tournament:

- RT0 at O5/O10 is the M1 confirmatory family; O1/O20 are registered temporal diagnostics;
- RT1 at O5/O10 is the M2 confirmatory family; O1/O20 are registered diagnostics;
- RT2 and RT3 at O10/O20 are validity/persistence diagnostics, not winner-selection targets;
- PV0 versus PV-M1 and PV0 versus PV-M2 are separate confirmatory incremental families;
- PV-BOTH is a coexistence diagnostic unless separately promoted before outcomes;
- OLS is the sole V1 predictive estimator; Ridge is closed from V1 A6.

Within each small confirmatory family, use Holm-style FWER control over the two horizons. Diagnostics receive descriptive uncertainty and are excluded from confirmatory claims; no FDR screening family is proposed for V1.

## SR0 / SR1 and outputs

SR0 failures: invalid PIT order, outcome leakage, incomplete horizon, undefined target/scale, broken lineage, or violation of C04/C05/identity eligibility. Poor prediction is SR1 evidence.

SR1 keeps common-support incremental loss, uncertainty, temporal consistency/dispersion, severe failure, and native coverage separate and permits advance, baseline retained, both survive, insufficient differentiation, or no advance. No candidate is forced to win.

Every output is immutable and binds model/evidence/target/scale/eligibility/partition versions, native/common support, lineage, and contamination status. Inner results must be materialized and checksummed before interpretation; OF4 and held-out remain inaccessible until later gates.
