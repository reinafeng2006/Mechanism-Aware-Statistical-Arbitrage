# G4-04A1 Relationship Metric Architecture Freeze

Decision date: 2026-09-10
Status: **APPROVED / FROZEN**

## Frozen metric architecture

- cross-representation point losses use a candidate-neutral PIT scale;
- candidate-specific uncertainty is excluded from the point-loss denominator;
- PIT-scaled absolute OOS conditional-response error is the primary relationship-comparison loss architecture;
- PIT-scaled squared OOS conditional-response error is the preregistered tail-sensitive robustness loss architecture;
- both losses use the same scale definition;
- calibration and uncertainty diagnostics form a separate evidence channel;
- `i -> j` and `j -> i` directional losses remain separate before pair aggregation;
- aggregation proceeds through observations within direction, directions within pair, pairs within comparison support, then temporal origins/folds;
- observation-rich or long-history pairs cannot dominate merely through row count;
- absolute/squared loss, calibration, and temporal robustness are SR1 comparative evidence rather than SR0 structural failures.

`point-prediction scaling != candidate-specific uncertainty calibration`.

## Deferred specification

The exact PIT scale estimator, zero/near-zero handling, directional aggregation, pair weighting, temporal aggregation, meaningful-effect and severe-failure thresholds, calibration procedure, and multiplicity levels remain unresolved. This decision authorizes no data access or computation.
