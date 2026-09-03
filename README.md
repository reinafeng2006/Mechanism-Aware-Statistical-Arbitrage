# Mechanism-Aware Statistical Arbitrage

Status: **G0 FROZEN — G1-02 EVIDENCE REVIEW COMPLETE; G1-03 NOT STARTED**

The mature literature workflow is nested within G1 as G1-01 through G1-04. G1-01 and G1-02 are complete; G1-03 synthesis and G1-04 evidence freeze remain locked pending approval. Empirical work remains prohibited.

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

G0 was frozen on 2026-09-03. G1-01 completed literature design, discovery and triage. G1-02 completed adaptive Light/Selective Deep evidence review and admitted fifteen bounded claims. Its comparison tables and claim-linked Data Requirement Register are provisional inputs to G1-03, not formal synthesis or a G2 handoff.

Still prohibited: claim admission without lawful full text; data acquisition or provider selection; database construction; empirical inspection; formal pair selection; factor or formula selection; measurement design; algorithm choice; model fitting; backtesting; performance estimation; and parameter tuning.

See [G0 freeze decision](docs/G0_FREEZE_DECISION.md), [G1 stage hierarchy](docs/G1_STAGE_HIERARCHY.md), [G1 literature design](docs/G1_LITERATURE_DESIGN.md), and [G1-02 evidence-review checkpoint](docs/G1_REVIEW_CHECKPOINT_02.md).
