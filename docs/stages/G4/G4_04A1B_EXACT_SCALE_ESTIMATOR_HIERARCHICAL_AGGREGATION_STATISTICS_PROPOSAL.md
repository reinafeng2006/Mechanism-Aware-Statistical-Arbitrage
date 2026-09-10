# G4-04A1b Exact Scale Estimator & Hierarchical Aggregation Statistics Freeze

Status: **G4-04A1b APPROVED / FROZEN — 2026-09-10**
Boundary: exact-candidate protocol design only. No frozen-data inspection, statistical computation, or A2 work.

## Objective

Choose a small exact candidate set implementing the frozen PS0/PS1 and AG1/AG2 architecture. Every formula below is **ILLUSTRATIVE / UNAUTHORIZED** until researcher approval.

Let `x_d,s` denote the historical observed directional-response target for direction `d` at pre-origin session `s`, using only the frozen PIT support history.

## PS0 robust estimator candidates

### PS0-MAD

`scale_d = 1.4826 * median_s |x_d,s - median_s(x_d,s)|`

- Robustness: high breakdown resistance.
- Interpretability/comparability: standard robust analogue of standard deviation when the reference distribution is symmetric.
- Sample efficiency: lower than standard deviation under ideal Gaussian behavior.
- Extremes: strongly resistant.

### PS0-IQR

`scale_d = (Q_0.75(x_d) - Q_0.25(x_d)) / 1.349`

- Robustness: resistant to tail extremes, though dependent on stable quartiles.
- Interpretability/comparability: transparent central-spread measure.
- Sample efficiency: workable but potentially coarse with limited support.
- Extremes: resistant.

**Selected:** MAD is the primary robust PIT scale. IQR remains a registered sensitivity/reference only and is outside primary selection.

## PS1 quadratic estimator candidates

### PS1-SD

Sample standard deviation of the same directional-response target around its pre-origin sample mean, with a frozen degrees-of-freedom convention.

### PS1-RMS-MEDIAN

Root mean squared deviation of the same directional-response target around its pre-origin median.

**Selected:** standard deviation is the preregistered quadratic-scale robustness normalization. RMS-about-median remains a registered diagnostic/reference only and is outside primary selection.

## Near-zero scale qualification candidates

- **NZ0 — strict qualification:** scaled loss is ineligible when the estimator is undefined, non-positive, or fails its frozen minimum-support contract; reason code remains `SCALE QUALITY / NEAR-ZERO SCALE`.
- **NZ1 — candidate-neutral relative floor:** compare the scale with a preregistered PIT cross-pair reference scale for the same direction/target semantics; below the frozen relative boundary, mark the scaled observation ineligible or use the frozen common floor with an explicit floor-applied flag.

**Selected semantic approach:** NZ1 candidate-neutral relative scale-quality qualification, with a PIT cross-pair reference for the same directional-response semantics. A genuinely degenerate or insufficiently identifiable scale makes scaled loss unavailable. No arbitrary epsilon is permitted. The numerical relative-quality cutoff remains unresolved.

## AG1 hierarchical statistic candidates

### Level 1 — observations within direction

- **L1-MEDIAN:** median scaled loss per pair-direction-origin; robust and interpretable but less sensitive to persistent tail failures.
- **L1-TRIMMED-MEAN:** symmetrically trimmed mean with a preregistered trim fraction; uses more observations but introduces one numerical choice.

**Selected:** L1-MEDIAN. Trimmed mean remains a registered sensitivity only. Separate dispersion, severe-failure, and support fields remain mandatory.

### Level 2 — direction to pair

- **L2-EQUAL-VECTOR:** retain both directional summaries and use their equal-influence center only as the pair central component; also preserve directional difference and maximum/severe direction.
- **L2-WORST-DIRECTION-GUARDED:** use the equal-influence center, but pair advancement additionally requires the worse direction to clear AG2.

**Selected:** retain an equal-status two-direction vector at pair level; do not create a compensatory directional average. AG2 applies a non-compensatory worst-direction/severe-failure guardrail. Neither direction is discarded or row-weighted.

### Level 3 — equal-pair representation aggregation

- **L3-EQUAL-PAIR-MEDIAN:** median of pair summaries, with each eligible pair contributing one unit.
- **L3-EQUAL-PAIR-TRIMMED-MEAN:** equal-pair trimmed mean with a frozen trim fraction.

**Selected:** L3-EQUAL-PAIR-MEDIAN. Every eligible pair has equal representation-level influence regardless of row count. Native coverage remains separate under CS2. Equal-pair trimmed mean remains a registered sensitivity only; support weighting is excluded absent a later structural amendment.

### Level 4 — temporal-origin/fold summary

- **L4-MEDIAN-VECTOR:** median central effect plus separate sign consistency, inter-origin dispersion, severe-failure count/state, and support.
- **L4-MEAN-VECTOR:** equal-origin mean central effect plus the same separate non-compensatory dimensions.

**Selected:** L4-MEDIAN-VECTOR. It preserves directional consistency, dispersion, severe fold-specific failure, and eligible support separately and does not reduce OF4 to a scalar. Mean-vector remains a registered sensitivity only.

## AG2 severe-failure semantic candidates

AG2 is a guardrail evaluated separately at direction, pair, and temporal levels. Register only:

- **SF0 — absolute adequacy breach:** loss/calibration/support violates a preregistered use-specific adequacy boundary;
- **SF1 — comparative reversal:** a candidate's common-support comparative effect is materially adverse at an authorized direction/origin/fold under a preregistered boundary;
- **SF2 — structural support failure:** directional or pair support falls below the frozen comparison requirement.

**Selected:** SF0–SF2 jointly define AG2's non-compensatory guardrail. They are failure types, not a score or winner ranking and are not interchangeable with SR0 unless the condition is genuinely structural. Exact boundaries, allowed failure count, and consequences remain unresolved.

## Frozen primary path and sensitivity closure

The primary path is:

`PS0-MAD + PS1-SD robustness + NZ1 relative qualification + L1 median + equal-status directional vector + L3 equal-pair median + L4 median-vector + SF0/SF1/SF2 AG2 guardrail`.

IQR, RMS-about-median, trimmed-mean, equal-pair trimmed-mean, and mean-vector were explicitly registered and remain sensitivity/reference candidates only. They are closed to primary selection and require separate sensitivity-budget authorization to execute. No new combinations are permitted.

## Remaining numerical cutoff decisions

1. relative near-zero scale-quality cutoff and minimum estimator support;
2. SF0 absolute adequacy cutoff;
3. SF1 comparative-reversal cutoff;
4. SF2 structural/support cutoff;
5. permitted severe-failure count/dispersion and its advancement consequence;
6. numerical directional-consistency and temporal-dispersion cutoffs where used.

`G4-04A1b APPROVED / FROZEN`
