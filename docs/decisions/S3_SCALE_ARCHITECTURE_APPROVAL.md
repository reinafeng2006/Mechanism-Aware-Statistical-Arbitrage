# S3 scale architecture — researcher approval

Decision ID: S3-SCALE-ARCHITECTURE-2026-09-22.
Status: APPROVED DESIGN BINDINGS ONLY.
Authority: direct researcher instruction dated 2026-09-22, headed “RESEARCHER DECISION — APPROVE S3 SCALE ARCHITECTURE; NUMERICAL THRESHOLD REMAINS UNSELECTED”.
Ancestry: [original design checkpoint](../stages/G5/S3_RESIDUAL_SCALE_THRESHOLD_DESIGN_CHECKPOINT.md), [authority ledger](../../research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md).
This descendant records the decision without backdating it into frozen V1 or altering relationship estimators.

## Approved bindings

1. Current-origin residual-basket replay: epsilon_(s;t)=w_t' r_s−a0_t, using the candidate-specific aligned residual equations in the original checkpoint. R0-D/C retain OLS bridges; R1 retains all modeled factor terms; R3 retains conditional pair effects.
2. Primary scale: sigma_t=1.4826*median_(s in W_t)|epsilon_(s;t)−median_(r in W_t)epsilon_(r;t)|. This measures descriptive residual-basket dispersion, not full predictive uncertainty.
3. Common H_sigma=126 qualified prior aligned residual observations across R0-D252, R0-C126, R0-L126, R1-M126, R1-MI126 and R3-252. For common attribution/reference calibration, use the same qualified dates supporting all six objects; native coverage remains separate and cannot replace missing common support.
4. Daily scale refresh from information strictly before the signal. The evaluated response does not enter its denominator. Relationship-estimator H/U is unchanged. Reconstruct the full window after geometry/lineage changes; no stale or mixed-geometry denominator.
5. z_t=d_t/sigma_t. Zero, nonfinite, unsupported or insufficient-history scale means SIGNAL UNAVAILABLE, never zero abnormality. No shortened-window rescue, epsilon floor or outcome-driven substitution. The MAD center defines dispersion only; the numerator retains the model-zero target.
6. Two-sided peer convergence: |z_t|>=z0, with signed directions reported separately. This scientific definition does not assume symmetric tails. Short/borrow feasibility belongs to the later execution gate and does not redefine the scientific signal.
7. One common weighted reference-tail threshold across all six estimators. Use equal chronological calibration-block influence, equal unordered-pair influence within a block, equal supported-direction influence within a pair, and equal estimator-group influence. Groups are {R0-D}, {R0-C,R0-L}, {R1-M}, {R1-MI}, {R3}, with equal C/L shares inside their group. Preserve all six books. Missing required common group/support does not permit silent reweighting.

The threshold architecture is F_ref(x)=sum_l omega_l*1{|z_l|<=x}, sum_l omega_l=1, with the approved balancing hierarchy; z0=inf{x:F_ref(x)>=1−alpha_ref}. This records the architecture only: alpha_ref, the evaluated quantile and numerical z0 are UNSELECTED / NOT COMPUTED. No Gaussian reference law is adopted. An absolute-tail budget is not automatically split into equal signed tails.

## Required limitations and robustness roles

Current-origin replay can understate genuine future prediction error because coefficients are fitted using overlapping formation information. It is PIT at decision t, not an out-of-sample forecast made at historical s. Preserve and later report fit overlap, support and residual bias; neither the MAD factor nor a common threshold establishes Normality, equal false-positive rates, significance or profitable convergence.

H252 MAD and H126 SD are recorded only as non-selecting robustness specifications, retaining daily refresh and aligned geometry. They may not replace H126 MAD based on observed outcomes. Approval of their specification does not authorize their computation.

## Explicitly unselected and unauthorized

No tail probability (including the earlier proposed 5%), numerical quantile or z0 is selected. No finite-grid fallback is activated; no O1/O2/O3 outcome optimization is authorized. The old proposed dates, run-in, folds, numerical search budget and fallback are not approved wholesale.

No historical data access, calibration, expected-capture/cost design, hedge-execution design, implementation, acquisition, C04 repair, backtesting, trading or PnL inspection is authorized. Frozen V1 tag/artifacts, historical exposure and terminal dispositions are unchanged.

The instruction authorizes persistence of this decision and its bounded documentation/control consequences. It does not grant continuing research or execution authority. The successor NEXT_ACTION remains NONE.

## Sole next question

How should the reference-tail probability / numerical z0 be bound without performance-driven optimization?

Compare only directly preregistered rarity/materiality probability versus bounded 2015–2019 occurrence/support development calibration. Neither route is selected or executed. See the [numerical-threshold checkpoint](../stages/G5/S3_NUMERICAL_THRESHOLD_BINDING_CHECKPOINT.md).

**S3 NUMERICAL THRESHOLD BINDING / RESEARCHER DECISION REQUIRED**
