# G2-12 — Candidate Measurement Requirements & Feasibility Contract Freeze Decision

Status: **APPROVED / FROZEN**
Date: 2026-09-07
Boundary: translate frozen candidates into feasibility-audit requirements only. No measurement, formula, model, provider, raw field, exact frequency, threshold, data source or empirical winner is selected.

## Objective

Resolve the Pre-G3 checkpoint's five linked blockers as one bounded design task by creating a versioned, one-to-one Candidate Measurement Requirement Envelope inventory, a target-universe feasibility frame, broad decision-use clock envelopes, an inheritance graph and independent Production Data Tiers.

The complete frozen register is [Candidate Measurement Requirement Envelopes v1.0](../../registers/CANDIDATE_MEASUREMENT_REQUIREMENT_ENVELOPES.md). It covers every currently authorized or explicitly preserved candidate family: P0/P1, relationship representations and governance, N0/N1/N2, abnormality and information-role families, UR0–UR2, MP0–MP3, R0–R3, M3 discovery-only context and U0–U4.

## Frozen contract rules

1. `MINIMUM REQUIREMENT ≠ PREFERRED / ENHANCEMENT REQUIREMENT`.
2. Missing enhancement information cannot make a simpler candidate infeasible.
3. Requirement envelopes express capabilities/categories, never selected frequencies, fields, windows or providers.
4. Derived candidates inherit all upstream PIT, vintage, coverage, latency and feasibility burdens.
5. One input may serve multiple candidates, but lineage and information-set use must remain explicit; reuse does not create new evidence.
6. Candidate requirements must be evaluated across the intended production universe rather than convenient pairs or surviving high-quality subsets.
7. Production Data Tier is separate from evidence strength, expected predictive value and G2-05 Production Feasibility.
8. Provider convenience cannot redefine the construct. G3A may report infeasibility or alternatives, not silently substitute a different measurement.

## Production Data Tiers

- `CORE-FEASIBILITY` — absence or inadequate PIT coverage would block the minimum primary production architecture or its governance.
- `OPTIONAL-ENHANCEMENT` — potentially useful addition; absence cannot block the simpler architecture.
- `RESEARCH-ONLY` — diagnostic/discovery capability that cannot block production and does not authorize a production signal.

These are operational scope classifications, not rankings of evidence, identification, maturity or profitability. Existing `EASY / CORE-CANDIDATE`, `MODERATE`, `HARD / OPTIONAL`, `UNAVAILABLE / RESEARCH-ONLY` and inherited/unresolved feasibility assessments remain separate.

## Target-Universe Feasibility Frame

Feasibility must be audited across the intended production scope of economically coherent A-share machinery securities and PIT historical membership, including difficult historical states. Convenient pairs cannot define architecture feasibility. No constituent list, coverage threshold, listing-age rule, liquidity screen or survivorship rule is selected.

## Broad Decision-Use Clock Envelope

The contract uses capability envelopes—relationship-history, ordered-market-response, event-publication, specialized high-resolution and outcome-separation capable—rather than daily/intraday/tick choices. Each candidate records its coarsest conceptual requirement and whether finer timing is only an enhancement. Final frequency remains a post-feasibility G2 decision.

## Dependency and inheritance

The register freezes an explicit candidate graph. Key examples:

- normal-relationship candidates inherit P0/P1 and the chosen representation's requirements;
- abnormality inherits Observed and Expected Response plus uncertainty;
- UR0 inherits Expected Signed Response; UR1 adds uncertainty; UR2 may add only non-duplicative context;
- MP0 inherits Expected Response; MP1–MP3 add successive information burdens without implying stronger identification;
- R0 inherits relationship history; R1/R2 add event/link vintages; R3 inherits timing/quality lineage;
- U0/U4 reuse existing diagnostics; U1/U2 await a belief architecture; U3 awaits a decision architecture;
- N2 inherits N0/N1 and remains unauthorized/research-only unless separately escalated.

## Data-requirement ancestry and non-invention boundary

The envelopes translate the 17 existing literature-derived Data Requirements, frozen G2 decompositions and Claim/decision ancestry into source/information classes. They do not invent provider fields. Where the frozen evidence supports only a broad class—such as PIT market history, dated public event information, factor/exposure context, liquidity/flow context or trades/quotes—the envelope stays at that level.

G3A must flag when a provider field would alter the construct, embed outcomes, lack historical vintages or require an unapproved proxy.

## Frozen G3A / G3B controlled loop

`G3A — PIT Data / Provider Feasibility Audit` is separately authorized after this freeze as **AUDIT-ONLY**. It may inspect provider/source capabilities, lawful availability, PIT/vintage support, history/universe coverage, granularity, latency, stability, lineage and expected burden.

G3A must not acquire the formal empirical dataset, compute outcomes, select winning measurements or inspect performance.

The intended loop is:

`G2-12 envelopes → G3A feasibility audit → return to G2 for implementable measurement specification freeze → separately authorized G3B formal acquisition`

G3B remains locked. G2-12 does not authorize acquisition.

## G3A feasibility-not-desirability boundary

**`G3A evaluates feasibility, not desirability.`**

G3A may assess lawful access, PIT/vintage integrity, history, intended-universe coverage, granularity, latency, reproducibility, stability and operational burden. It must not choose or rank candidates by alpha, infer predictive value, change Production Data Tier because a model appears attractive, use PnL, run backtests or resolve G2 measurement choices.

`MP3 infeasible ≠ M2 infeasible`: dependency-aware findings must preserve simpler branches whenever only an enhancement is constrained.

## Unresolved after G2-12

### G3A-FEASIBILITY INFORMED

Provider/source availability, actual PIT vintage support, timestamps, history/universe coverage, attainable granularity, latency, source stability, lawful use, reconstruction and expected burden.

### RETURN-TO-G2

Which candidate subset is implementable; actual measurement definitions, clocks, frequency, estimators, uncertainty, windows, thresholds, interaction and validation protocol.

### G3B-DEFER

Provider selection, physical database design, formal acquisition, ingestion and production data build.

### EMPIRICAL-DEFER

All relationship, mechanism, resolution, prediction and economic comparisons.

## Frozen classification

### FROZEN CONTRACT

- envelope schema and v0.1 candidate inventory;
- minimum versus enhancement boundary;
- target-universe feasibility principle;
- broad clock capability envelopes;
- dependency/inheritance graph;
- three Production Data Tiers;
- G2-05 feasibility status separation;
- no provider convenience substitution;
- controlled G2-12 → G3A → G2 → G3B loop.

### G3A-AUTHORIZED / AUDIT-ONLY

Feasibility audit scope only; no formal dataset, outcomes, model selection or performance inspection.

### G2/G3/EMPIRICAL-DEFER

All concrete measurements, sources, providers, frequencies, physical schemas, data acquisition and empirical choices.

## Approval record

Researcher approval on 2026-09-07 freezes all 45 envelopes, minimum/enhancement distinction, universe and clock frames, dependency graph, Production Data Tiers, controlled G3A-return-to-G2-G3B loop and feasibility-not-desirability boundary exactly as documented. G3A is authorized audit-only after the milestone push; G3B remains locked.
