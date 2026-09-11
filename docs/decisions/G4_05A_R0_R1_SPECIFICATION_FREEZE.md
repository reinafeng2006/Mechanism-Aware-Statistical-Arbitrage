# G4-05A R0/R1 Specification Freeze

Decision date: 2026-09-11
Status: **APPROVED / FROZEN**

## Frozen architecture

- R0-DIST is a symmetric standardized cumulative-response-path distance representation only;
- R0-CORR is a relationship representation only;
- R0-LIN is the sole preregistered directional expected-response bridge for the R0 layer;
- no implicit correlation-to-beta shortcut is permitted;
- Pearson is the primary correlation specification;
- Spearman is a preregistered robustness diagnostic only;
- OLS is the primary R0-LIN estimator;
- Huber is a preregistered robustness diagnostic only;
- R1-M and R1-MI use identical PIT residualization, directional pair-estimation, and update architecture;
- the sole intended R1-M to R1-MI difference is inclusion of the industry common factor;
- R0/R1 remain P0 unless separately tracked P1 information is added;
- N0/N1 remains an orthogonal pooling/heterogeneity axis;
- Spearman and Huber cannot post-hoc rescue, replace, or select a primary specification.

All numerical and tuning details explicitly listed as unresolved in the frozen specification remain unresolved. This freeze authorizes no fitting, data inspection, computation, or outcome access.
