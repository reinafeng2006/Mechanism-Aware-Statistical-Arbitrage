# Mechanism-Aware Statistical Arbitrage

Current status: **S3 CONVERGENCE TARGET BRIDGE / RESEARCHER DECISION REQUIRED**.

**Fresh client: start with [Current project state and next action](docs/stages/G5/CURRENT_PROJECT_STATE_AND_NEXT_ACTION.md)**, then read `AGENTS.md`, `research/AGENT_POLICY.md` and `research/NEXT_ACTION.json`. Historical V1 is frozen at tag `v1-final-frozen-2026-09-18`; S3 peer-only hedged relative-value architecture and its [scale architecture](docs/decisions/S3_SCALE_ARCHITECTURE_APPROVAL.md) are approved. The [primary tail binding](docs/decisions/S3_REFERENCE_TAIL_PROBABILITY_PREREGISTRATION.md) is frozen at alpha=0.05 and z0=Q^w_0.95(abs(z_ref)); numerical z0 is not estimated. The finite-grid fallback is inactive. The [minimal capture/cost architecture](docs/decisions/S3_MINIMAL_SCENARIO_CAPTURE_COST_ARCHITECTURE_APPROVAL.md) is approved: F/P/N/A/X, pooled P1, joint duration/exposure, all-leg ledger and E1; P3 inactive. [H-C proxy hedging and execution/accounting](docs/decisions/S3_HC_PROXY_HEDGE_EXECUTION_ACCOUNTING_APPROVAL.md) are approved: common hedge rule, abort/unwind, E-A, intended K and obligation-first exit precedence. [Fund-share/M1/static-origin/T1 construction](docs/decisions/S3_PROXY_CONSTRUCTION_APPROVAL.md) is approved; actual funds and numerical qualification remain unselected. [Target A versus Target B](docs/stages/G5/S3_CONVERGENCE_TARGET_BRIDGE_DESIGN_CHECKPOINT.md) is the unresolved design gate; model z is unchanged. No historical data access, implementation, calibration, C04 repair, backtest or PnL inspection is authorized. Git contains design context and artifact metadata, not the external scientific payload backup.

The historical framework below explains project ancestry, not current execution authority. Its earlier gate language does not override the current handoff or NEXT_ACTION.

## Objective

Develop and test a potentially profitable statistical-arbitrage framework for economically related A-share machinery stocks. The central hypothesis is that visually similar relative-price dislocations may arise from different mechanisms and therefore resolve differently; strategy quality may depend on identifying the mechanism before deciding whether and how to trade.

This is a research hypothesis, not a claim of profitability or an established market fact.

## Historical research architecture

`Company Representation → Industry-Specific Relationship Prior → Pair-Specific Normal Relationship → Continuous Pair-Specific Abnormality → Sequential Mechanism & Resolution Updating → Trade / Update / Reject / Abstain`

This architecture is approved by [Amendment 001](docs/decisions/ARCHITECTURE_AMENDMENT_001.md). The original G0 seven-stage pipeline is preserved unchanged as a historical freeze record. M0–M3 are competing hypotheses; `U = Unresolved / Abstain` is an epistemic state, not a fifth mechanism. Literature evidence is not a mandatory real-time trading gate. Representations, variables, formulas, thresholds, algorithms, labels, horizons and policies remain unselected.

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

## Canonical documentation

- [Project Overview](docs/00_PROJECT_OVERVIEW.md)
- [Economic Thesis](docs/01_ECONOMIC_THESIS.md)
- [Strategy Architecture](docs/02_STRATEGY_ARCHITECTURE.md)
- [Literature Evidence](docs/03_LITERATURE_EVIDENCE.md)
- [Measurement Design](docs/04_MEASUREMENT_DESIGN.md)
- [Research Governance](docs/05_RESEARCH_GOVERNANCE.md)

Formal decisions are under `docs/decisions/`, active working artifacts under `docs/stages/`, and completed process records under `docs/archive/`.
