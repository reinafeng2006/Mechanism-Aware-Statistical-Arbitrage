# S3 reference-tail probability — direct preregistration

Decision ID: S3-REFERENCE-TAIL-PREREGISTRATION-2026-09-22.
Status: APPROVED DESIGN BINDING; NUMERICAL z0 NOT ESTIMATED.
Authority: direct researcher instruction “RESEARCHER DECISION — DIRECTLY PREREGISTER THE S3 REFERENCE-TAIL PROBABILITY”.
Ancestry: [approved scale architecture](S3_SCALE_ARCHITECTURE_APPROVAL.md), [prior threshold checkpoint](../stages/G5/S3_NUMERICAL_THRESHOLD_BINDING_CHECKPOINT.md), [authority ledger](../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).
This is a descendant decision, not a change to frozen V1.

## Frozen primary definition

Select the direct-preregistration path. Do not use 2015–2019 occurrence/support calibration to choose the primary threshold.

alpha_ref = 0.05.

z0 = Q^w_0.95(|z^ref|).

Primary S3 abnormality: |z_t| >= z0, with signed directions reported separately and the previously approved scale/unavailable-state rules retained.

The weighted empirical quantile uses the already-approved balancing: equal chronological-block influence; equal unordered-pair influence within block; equal supported-direction influence within pair; equal estimator-group influence. Groups are {R0-D}, {R0-C,R0-L}, {R1-M}, {R1-MI}, {R3}; R0-C/R0-L split their group's weight equally. No duplicate-equation double counting, per-model threshold tuning or silent missing-group reweighting.

Use the existing empirical inverse-CDF convention:
F_ref(x)=sum_l omega_l*1{|z_l^ref|<=x}, sum_l omega_l=1;
Q^w_0.95=inf{x:F_ref(x)>=0.95}.
This fixes the quantile rule, not its numerical value. The reference population/dates, chronological formation and threshold estimation/refresh schedule still need a separately bounded specification before any data access; the former proposed development folds are not adopted by this probability decision.

## Interpretation and finite-reference qualification

The primary state identifies the most extreme 5% upper-tail region of the preregistered weighted distribution of absolute standardized residual states: a rarity/materiality convention.

It is not a Gaussian significance test, a p-value, a 5% false-positive probability, an economic-profitability threshold or a convergence-probability estimate. Do not substitute 1.96 or another parametric cutoff. A coincident numerical equality would be incidental to the mechanical empirical quantile.

With a finite weighted empirical distribution, atoms/ties at the cutoff and the approved inclusive >= rule can make the included reference mass exceed 5%. Report that actual mass later; do not change alpha, inequality, weighting or randomize ties to force exactly 5%. No guarantee of 5% frequency in each estimator, signed direction or future period follows. Do not split the absolute-tail budget into equal signed tails.

Current-origin replay's formation overlap can understate genuine future prediction error. The 1.4826 MAD factor and this threshold binding do not remove that limitation.

## No adaptive selection

Do not change alpha_ref=0.05 because signal counts are low/high, support is concentrated, convergence appears weak/strong, PnL is unfavorable, or one estimator generates more/fewer events. Insufficient support is a reported limitation or unavailable reference, never a reason to repair the primary threshold by retuning.

The finite-grid fallback remains INACTIVE. The occurrence/support path is not selected for choosing the primary definition. Later separately authorized support reporting may diagnose limitations but cannot choose a replacement threshold.

H252 MAD and H126 SD retain their approved non-selecting robustness roles. Any future alternative tail probabilities require separate authorization, remain non-selecting sensitivities and may not replace the 5% primary based on outcomes. No alternative probabilities are defined here.

## Numerical estimation and scope

The numerical weighted Q^w_0.95 has NOT been computed. Future estimation is mechanical under the approved quantile rule only after separate bounded reference-specification/data-access authorization. This decision grants no historical access, fitting, cost estimation, implementation, acquisition, C04 repair, backtest, trading or PnL inspection.

The present instruction authorizes persistence plus design-only discussion of expected capturable remaining convergence m_hat_u and all-in round-trip cost c_hat_RT,u. It does not approve a capture/cost model or any numerical parameters. NEXT_ACTION remains NONE after documentation closeout.

Next: [capture and cost design checkpoint](../stages/G5/S3_CAPTURE_COST_DESIGN_CHECKPOINT.md).

**S3 CAPTURE + COST GATE DESIGN / RESEARCHER DECISION REQUIRED**
