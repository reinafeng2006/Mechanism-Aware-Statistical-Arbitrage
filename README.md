# Mechanism-Aware Statistical Arbitrage

Status: **G0 FROZEN — G1-02 EVIDENCE REVIEW REOPENED; G1-03 NOT STARTED**

The mature literature workflow is nested within G1 as G1-01 through G1-04. G1-01 and G1-02 are complete; G1-03 synthesis and G1-04 evidence freeze remain locked pending approval. Empirical work remains prohibited.

## Objective

Develop and test a potentially profitable statistical-arbitrage framework for economically related A-share machinery stocks. The central hypothesis is that visually similar relative-price dislocations may arise from different mechanisms and therefore resolve differently; strategy quality may depend on identifying the mechanism before deciding whether and how to trade.

This is a research hypothesis, not a claim of profitability or an established market fact.

## Active strategy architecture

`Company Representation → Pair Relationship Prior → Abnormality Trigger → Sequential Mechanism Tracking + Dynamic Resolution Prediction → Trade / Update / Reject / Abstain`

This architecture is approved by [Amendment 001](docs/ARCHITECTURE_AMENDMENT_001.md). The original G0 seven-stage pipeline is preserved unchanged as a historical freeze record. M0–M3 are competing hypotheses; `U = Unresolved / Abstain` is an epistemic state, not a fifth mechanism. Literature evidence is not a mandatory real-time trading gate. Representations, variables, formulas, thresholds, algorithms, labels, horizons and policies remain unselected.

## Frozen pair-formation philosophy

Formal strategy pairs must be company-aware, fully data-driven, point-in-time, reproducible, and generalizable. Subjective or manual pair assignment is prohibited in the formal strategy. Company/business characteristics, factor exposures, empirical co-movement, and relationship stability are candidate information families only—not frozen factors, formulas, weights, or selection rules.

## Initial mechanism hypotheses

- **M1 — delayed peer repricing / information diffusion:** possible follower catch-up.
- **M2 — temporary liquidity or flow pressure:** possible shocked-stock reversal.
- **M3 — temporary idiosyncratic relative dislocation:** possible relative normalization.
- **M0 — structural, fundamental, ambiguous, or unresolved divergence:** no-trade candidate.

M0–M3 are falsifiable working hypotheses, not assumed true mechanism classes. Ambiguity, rejection, and no trade remain valid outcomes.

## Candidate-information roles

- **P — Relationship Prior:** why a pair should normally share a relationship.
- **S — Abnormality Trigger:** evidence that the current relative state is unusual.
- **C — Mechanism Discriminator / Updating Evidence:** contemporaneously arriving information that changes mechanism or resolution belief.
- **R — Rejection / Rival Evidence:** structural/fundamental invalidation, competing explanations, or abstention evidence.

## Current boundary

G0 was frozen on 2026-09-03. G1-01 completed literature design, discovery and triage. An audit found that G1-02/02b claim admission was not backed by candidate-specific Light/Selective Deep review artifacts. All nineteen claims and sixteen provisional data requirements are retained as preliminary inputs while G1-02 is reopened for full-text evidence review. G1-03 remains unauthorized.

Still prohibited: claim admission without lawful full text; data acquisition or provider selection; database construction; empirical inspection; formal pair selection; factor or formula selection; measurement design; algorithm choice; model fitting; backtesting; performance estimation; and parameter tuning.

See [G0 freeze decision](docs/G0_FREEZE_DECISION.md), [active architecture](docs/STRATEGY_ARCHITECTURE.md), [Amendment 001](docs/ARCHITECTURE_AMENDMENT_001.md), [G1 stage hierarchy](docs/G1_STAGE_HIERARCHY.md), [G1-02 review-depth audit](docs/G1_02_REVIEW_DEPTH_AUDIT.md), and [Literature OS migration](docs/LITERATURE_OS_MIGRATION.md).
