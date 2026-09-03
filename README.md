# Mechanism-Aware Statistical Arbitrage

Status: **STOPPED AT G0 — ECONOMIC THESIS (not approved)**  
Repository phase: research operating system initialization only.

## Objective

Develop and test a potentially profitable statistical-arbitrage framework for economically related A-share machinery stocks. The central hypothesis is that visually similar relative-price dislocations may arise from different mechanisms and therefore resolve differently; strategy quality may depend on identifying the mechanism before deciding whether and how to trade.

This is a research hypothesis, not a claim of profitability or an established market fact.

## Frozen conceptual pipeline

`Company Representation → Data-Driven Pair Formation → Normal Pair Relationship → Abnormal Relative State → Mechanism Identification → Resolution Prediction → Trade / No-Trade Decision`

The pipeline order and stage separation are G0 boundaries. Representations, variables, formulas, thresholds, algorithms, labels, and horizons are not selected at G0.

## Frozen pair-formation philosophy

Formal strategy pairs must be company-aware, fully data-driven, point-in-time, reproducible, and generalizable. Subjective or manual pair assignment is prohibited in the formal strategy. Company/business characteristics, factor exposures, empirical co-movement, and relationship stability are candidate information families only—not frozen factors, formulas, weights, or selection rules.

## Initial mechanism hypotheses

- **M1 — delayed peer repricing / information diffusion:** possible follower catch-up.
- **M2 — temporary liquidity or flow pressure:** possible shocked-stock reversal.
- **M3 — temporary idiosyncratic relative dislocation:** possible relative normalization.
- **M0 — structural, fundamental, or unresolved divergence:** no-trade candidate.

These labels are provisional hypotheses. They are neither directly observed states nor permission to trade.

## Candidate-information roles

- **P — Pair Relationship:** why the securities should normally move together.
- **S — State/Dislocation:** what abnormal relative state is currently observed.
- **C — Context/Mechanism Discrimination:** information useful for distinguishing why the dislocation occurred.
- **R — Rejection:** evidence that weakens or invalidates the arbitrage interpretation.

## Current boundary

Permitted now: approval of the economic thesis, monetization objective, mechanism hypotheses, pair-formation philosophy, causal/point-in-time boundary, Observatory quarantine, falsifiability, and governance boundary.

Prohibited now: data acquisition; empirical inspection; manual/formal pair selection; factor or formula selection; measurement design; algorithm choice; model fitting; backtesting; performance estimation; parameter tuning; and any claim of empirical support.

The reduced G0 approvals and the classification of all former decision groups are in [docs/G0_ECONOMIC_THESIS.md](docs/G0_ECONOMIC_THESIS.md).
