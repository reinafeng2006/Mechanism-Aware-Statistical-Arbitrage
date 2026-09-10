# G4-04A1b Exact Scale Estimator & Hierarchical Aggregation Statistics Proposal

Status: **G4-04A1b EXACT SCALE & AGGREGATION PROPOSED / AWAITING RESEARCHER REVIEW**
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

Proposed bounded choice: MAD primary candidate, IQR robustness candidate. No additional robust estimator is registered.

## PS1 quadratic estimator candidates

### PS1-SD

Sample standard deviation of the same directional-response target around its pre-origin sample mean, with a frozen degrees-of-freedom convention.

### PS1-RMS-MEDIAN

Root mean squared deviation of the same directional-response target around its pre-origin median.

PS1-SD is simpler and conventional; PS1-RMS-MEDIAN keeps the PS0 location reference but mixes a robust center with quadratic dispersion. Both are tail sensitive. Proposed bounded choice: SD primary quadratic candidate and RMS-median diagnostic only.

## Near-zero scale qualification candidates

- **NZ0 — strict qualification:** scaled loss is ineligible when the estimator is undefined, non-positive, or fails its frozen minimum-support contract; reason code remains `SCALE QUALITY / NEAR-ZERO SCALE`.
- **NZ1 — candidate-neutral relative floor:** compare the scale with a preregistered PIT cross-pair reference scale for the same direction/target semantics; below the frozen relative boundary, mark the scaled observation ineligible or use the frozen common floor with an explicit floor-applied flag.

No arbitrary absolute epsilon is permitted. NZ1 adds cross-pair dependence and complexity; NZ0 is simpler but may reduce support. The numerical support and near-zero boundaries remain unresolved.

## AG1 hierarchical statistic candidates

### Level 1 — observations within direction

- **L1-MEDIAN:** median scaled loss per pair-direction-origin; robust and interpretable but less sensitive to persistent tail failures.
- **L1-TRIMMED-MEAN:** symmetrically trimmed mean with a preregistered trim fraction; uses more observations but introduces one numerical choice.

Both retain separate dispersion, severe-failure, and support fields.

### Level 2 — direction to pair

- **L2-EQUAL-VECTOR:** retain both directional summaries and use their equal-influence center only as the pair central component; also preserve directional difference and maximum/severe direction.
- **L2-WORST-DIRECTION-GUARDED:** use the equal-influence center, but pair advancement additionally requires the worse direction to clear AG2.

Neither silently discards or row-weights a direction.

### Level 3 — equal-pair representation aggregation

- **L3-EQUAL-PAIR-MEDIAN:** median of pair summaries, with each eligible pair contributing one unit.
- **L3-EQUAL-PAIR-TRIMMED-MEAN:** equal-pair trimmed mean with a frozen trim fraction.

Both prevent longer-history pairs from dominating by row count. Any support weighting is excluded from the primary menu absent a later structural amendment.

### Level 4 — temporal-origin/fold summary

- **L4-MEDIAN-VECTOR:** median central effect plus separate sign consistency, inter-origin dispersion, severe-failure count/state, and support.
- **L4-MEAN-VECTOR:** equal-origin mean central effect plus the same separate non-compensatory dimensions.

Neither reduces OF4 evidence to one scalar. Equal-fold influence is preserved.

## AG2 severe-failure semantic candidates

AG2 is a guardrail evaluated separately at direction, pair, and temporal levels. Register only:

- **SF0 — absolute adequacy breach:** loss/calibration/support violates a preregistered use-specific adequacy boundary;
- **SF1 — comparative reversal:** a candidate's common-support comparative effect is materially adverse at an authorized direction/origin/fold under a preregistered boundary;
- **SF2 — structural support failure:** directional or pair support falls below the frozen comparison requirement.

SF0–SF2 are failure types, not a score and not interchangeable with SR0 unless the condition is genuinely structural. Exact boundaries, allowed failure count, and consequences remain unresolved.

## Proposed small authorized menu

To prevent Cartesian expansion, propose two coherent bundles for later selection rather than freely combining every component:

- **Bundle R:** PS0-MAD; PS1-SD robustness; NZ0; L1-MEDIAN; L2-WORST-DIRECTION-GUARDED; L3-EQUAL-PAIR-MEDIAN; L4-MEDIAN-VECTOR; SF0–SF2 guardrail.
- **Bundle T:** PS0-IQR robustness; PS1-SD; NZ0; L1-TRIMMED-MEAN; L2-EQUAL-VECTOR plus AG2; L3-EQUAL-PAIR-TRIMMED-MEAN; L4-MEAN-VECTOR; SF0–SF2 guardrail.

These are proposals, not selected bundles. NZ1 and RMS-median remain separately registered diagnostics requiring explicit authorization; they are not automatically crossed with both bundles.

## Remaining numerical decisions

1. select PS0-MAD or PS0-IQR and confirm PS1-SD/RMS-median role;
2. select scale support-history rule already allowed by G4-03A;
3. choose NZ0 or explicitly justify NZ1 and set its candidate-neutral reference/boundary;
4. set minimum robust/quadratic estimator support;
5. choose L1 statistic and any trim fraction;
6. choose L2 pair rule and directional-difference reporting;
7. choose L3 equal-pair statistic and any trim fraction;
8. choose L4 equal-origin/fold statistic and dispersion/consistency summaries;
9. set SF0–SF2 boundaries, permitted failure count, and consequences;
10. select one coherent bundle and freeze its version before computation.

`G4-04A1b EXACT SCALE & AGGREGATION PROPOSED / AWAITING RESEARCHER REVIEW`
