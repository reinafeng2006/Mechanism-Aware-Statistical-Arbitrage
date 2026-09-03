# Mechanism-Aware Statistical Arbitrage

Status: **G0 FROZEN — G1 DISCOVERY/TRIAGE ACTIVE**  
Literature Discovery is authorized under G1-01; empirical work remains prohibited.

## Objective

Develop and test a potentially profitable statistical-arbitrage framework for economically related A-share machinery stocks. The central hypothesis is that visually similar relative-price dislocations may arise from different mechanisms and therefore resolve differently; strategy quality may depend on identifying the mechanism before deciding whether and how to trade.

This is a research hypothesis, not a claim of profitability or an established market fact.

## Frozen conceptual pipeline

`Company Representation → Data-Driven Pair Formation → Normal Pair Relationship → Abnormal Relative State → Mechanism Identification → Resolution Prediction → Trade / No-Trade Decision`

The pipeline order and stage separation are frozen at G0. Representations, variables, formulas, thresholds, algorithms, labels, and horizons are not selected at G0.

## Frozen pair-formation philosophy

Formal strategy pairs must be company-aware, fully data-driven, point-in-time, reproducible, and generalizable. Subjective or manual pair assignment is prohibited in the formal strategy. Company/business characteristics, factor exposures, empirical co-movement, and relationship stability are candidate information families only—not frozen factors, formulas, weights, or selection rules.

## Initial mechanism hypotheses

- **M1 — delayed peer repricing / information diffusion:** possible follower catch-up.
- **M2 — temporary liquidity or flow pressure:** possible shocked-stock reversal.
- **M3 — temporary idiosyncratic relative dislocation:** possible relative normalization.
- **M0 — structural, fundamental, ambiguous, or unresolved divergence:** no-trade candidate.

M0–M3 are falsifiable working hypotheses, not assumed true mechanism classes. Ambiguity, rejection, and no trade remain valid outcomes.

## Candidate-information roles

- **P — Pair Relationship:** why the securities should normally move together.
- **S — State/Dislocation:** what abnormal relative state is currently observed.
- **C — Context/Mechanism Discrimination:** information useful for distinguishing why the dislocation occurred.
- **R — Rejection:** evidence that weakens or invalidates the arbitrage interpretation.

## Current boundary

G0 was frozen on 2026-09-03. G1-01 authorizes a bounded Literature Discovery/Triage checkpoint under the seven-question dependency map.

Still prohibited: substantive claim admission without lawful full text; unapproved Light/Selective Deep expansion beyond the checkpoint; data acquisition; empirical inspection; formal pair selection; factor or formula selection; measurement design; algorithm choice; model fitting; backtesting; performance estimation; and parameter tuning.

See [G0 freeze decision](docs/G0_FREEZE_DECISION.md), [G0 thesis](docs/G0_ECONOMIC_THESIS.md), and [G1 literature design](docs/G1_LITERATURE_DESIGN.md).
