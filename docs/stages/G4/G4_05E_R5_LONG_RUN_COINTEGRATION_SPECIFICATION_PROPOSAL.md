# G4-05E R5 Long-Run / Cointegration Specification Proposal

Status: **R5-EG-ECM REGISTERED / BLOCKED PENDING QUALIFIED C04 AND PRICE-CONSTRUCTION CONTRACT**
Boundary: no price-series construction, diagnostics, fitting, or data inspection.

## Estimand

R5 asks whether a preregistered long-run price relationship and error-correction term provide adequate PIT directional expected-response information beyond short-run statistical representations. Cointegration diagnostics remain representation-specific and do not define universal pair validity.

### `R5-EG-ECM` — bounded primary candidate

Long-run equation estimated on an authorized PIT formation window:

`p_j,s = a_ij + beta_ij p_i,s + u_ij,s`.

Directional response equation:

`Delta p_j,s = c_ij + lambda_ij u_ij,s-1 + delta_ij Delta p_i,s + epsilon_ij,s`,

with reverse direction separately specified. Deterministic constant/trend treatment, lag count, price transformation, and normalization must be frozen before fitting. Primary estimator candidate: Engle-Granger OLS followed by a single-equation ECM.

### Bounded challenger boundary

VECM is deferred and not registered for execution. Any later activation requires separate authorization establishing rank, deterministic terms, lag structure, estimator, directional forecast bridge, and Search Budget. Regime-switching cointegration, multiple nonlinear adjustment models, and automated lag/rank/model searches are prohibited.

## C04 and PIT eligibility blocker

`CORE-DATASET-FREEZE-V1` preserves raw/unadjusted observations while C04 is `AUTHORITATIVE COVERAGE INCOMPLETE` and corporate-action status is unresolved. R5 cannot silently construct canonical historical adjusted prices from Tushare/Sina factors. The exact price object and C04 eligibility/amendment must be researcher-approved before R5 computation.

This blocks the affected R5 specification, not R0–R4 or the broader architecture. Raw observation presence is not R5 eligibility.

## Geometry, N/P, and output

Existing envelope only: `(H252,U1M)` and conditional `(H504,U1M)`. H504 requires its frozen representation-specific support contract. N0/N1 may compare pooled versus pair-specific long-run/adjustment parameters only if the same price object, equation, lag, rank, H/U, and support are held fixed. P1 is excluded from the initial R5 proposal.

Output is a pre-decision long-run state and directional conditional response plus representation-specific residual/rank/stability diagnostics and uncertainty where qualified. A3 uses only the authorized expected directional response; stationarity or cointegration significance is not abnormality or mechanism evidence.

## Remaining blocker and later decisions

1. a qualified authoritative C04 and price-construction contract;
2. exact price/adjustment object and eligibility contract after that qualification;
3. constant/trend and lag structure;
4. H252 versus conditional H504 execution;
5. whether deferred VECM is ever separately proposed;
6. N0/N1 applicability, diagnostics, uncertainty, and failure rules.

R5 remains `NOT COMPUTATION-AUTHORIZED`.
