# G3B Acquisition Design Proposal

Checkpoint: **G3B-01 CONSOLIDATED**  
Status: **APPROVED / FROZEN — 2026-09-08**  
Formal acquisition: **NOT AUTHORIZED**  
Empirical computation/outcome inspection: **PROHIBITED**

This is the current authoritative G3B working proposal. It consolidates the earlier ten-item draft into four dependency-coherent blocks while preserving G2B classifications, minimum/enhancement separation, data tiers, PIT lineage, universe coverage, multi-clock envelopes, provider neutrality and outcome quarantine.

`acquisition breadth ≠ model-use authorization`

`stored data ≠ decision-time available data`

## G3B-A — Acquisition Scope & PIT Universe

- Center first-round acquisition on `CORE-FEASIBILITY`.
- Co-acquire `OPTIONAL-ENHANCEMENT` only when a surviving competing specification genuinely depends on it, or it shares the core snapshot at low marginal cost and retention avoids irreproducible/costly refetch.
- Co-acquisition permits preservation, not model use. `RESEARCH-ONLY` remains excluded absent separate authorization.
- Reconstruct the universe from PIT historical membership, stable entity/security identity, code history, listing/delisting and relevant eligibility states; never backfill from today's universe.
- Require versioned industry membership while leaving provider/taxonomy unselected.
- Sequence: `identity/universe → core market → industry/benchmark vintages → PIT/quality metadata → approved competing classes → justified enhancements → quarantined outcomes`.
- Stop before expansion if the prior layer fails lawful-use, PIT, coverage, reproducibility or immutable-snapshot acceptance. Expansion requires a surviving dependency or the same-snapshot exception, never expected alpha or factor appetite.

| Decision | Classification |
|---|---|
| Core-first scope, enhancement exceptions, research-only exclusion, breadth/use separation, PIT universe, sequence/stop rules | READY TO FREEZE BEFORE ACQUISITION |
| Industry provider/taxonomy and attainable history | PROVIDER-AUDIT INFORMED |
| Field-level coverage/missingness capability | FIELD/SCHEMA AUDIT INFORMED |
| Numerical thresholds and actual expansion | DEFER UNTIL FORMAL ACQUISITION |

## G3B-B — Provider, Source & Clock Contract

Compare sources neutrally on PIT/vintage integrity, historical and universe coverage, field semantics, timestamp quality, stability, reproducibility, lawful licensing/use, cost, acquisition complexity and maintenance burden. Prefer low-cost, stable, automatable sources only after PIT, coverage and reproducibility requirements are satisfied.

Each data class requires `Canonical Source + documented Fallback Source`. Missing canonical observations must not automatically trigger substitution. Every fallback substitution must be explicit, reason-coded, scoped by field/date/security, provenance-preserving, separately versioned where necessary, and auditable downstream. Provider mixing must never be invisible to later measurement or model code.

### Source Consolidation / Minimum Source Count

The preferred production architecture is:

`one primary integrated data platform + the minimum number of authoritative exceptions + documented fallbacks`.

Among architectures that satisfy hard data-integrity and PIT requirements, prefer fewer independently maintained sources. Evaluate integrated C01/C03/C04/C05/E02/E03 coverage, cross-module PIT/identifier/timestamp/calendar/corporate-action consistency, API/export and licence consistency, maintainability and `Source Fragmentation`. Never consolidate through a source that fails a hard PIT or lineage contract. The official C06 path remains a permitted authoritative exception; Sina/Tushare remain fallbacks unless separately promoted. See the [formal decision](../../decisions/G3B_SOURCE_CONSOLIDATION_MINIMUM_SOURCE_COUNT.md).

`minimum capability` is the coarsest granularity preserving the frozen construct and ordering/availability semantics. `enhancement capability` is finer/richer timing whose incremental value remains unproven. No exact clock is selected.

| Decision | Classification |
|---|---|
| Neutral criteria, conditional simplicity, canonical/fallback, no silent mixing, minimum/enhancement clock semantics, source-consolidation preference and fragmentation risk | READY TO FREEZE BEFORE ACQUISITION |
| Source identity, license, price, stability and coverage | PROVIDER-AUDIT INFORMED |
| Field meaning, native timestamps, schema continuity and attainable clocks | FIELD/SCHEMA AUDIT INFORMED |
| Final contracts, credentials, quotas and refresh operations | DEFER UNTIL FORMAL ACQUISITION |

## G3B-C — Security Master & PIT Integrity

Require stable internal security/entity IDs; code history; listing/delisting; historical industry membership; corporate-action announcement/effective/version lineage; relevant suspension/eligibility states; price-adjustment input/transformation lineage without selecting a formula; and the frozen timestamp/vintage/restatement fields.

| Condition | Pre-threshold handling |
|---|---|
| Missingness | Explicit missing state/reason; no silent imputation/forward-fill; report by field/time/universe |
| Incomplete universe | Do not redefine universe; quarantine and report dependency impact |
| Source outage | Log interval; fallback only through explicit versioned source-switch |
| Schema change | Preserve old schema; version new schema; map before continuation |
| Revision/restatement | Append vintage; never overwrite original |
| Identifier conflict | Quarantine; prohibit downstream join pending versioned resolution |

| Decision | Classification |
|---|---|
| Identity/state/timestamp/vintage semantics and exception principles | READY TO FREEZE BEFORE ACQUISITION |
| Authoritative historical identity, membership and action availability | PROVIDER-AUDIT INFORMED |
| Timestamp semantics, adjustment inputs, revision flags and crosswalks | FIELD/SCHEMA AUDIT INFORMED |
| Numerical tolerances and actual exception adjudication | DEFER UNTIL FORMAL ACQUISITION |

## G3B-D — Immutable Storage, Provenance & Outcome Quarantine

Every formal raw snapshot must be immutable/versioned and preserve provider/source, dataset/endpoint, query parameters, retrieval timestamp, source/vintage semantics, schema version, checksum, row/coverage metadata and acquisition log.

`Immutable Raw → Cleaned → PIT-Aligned → Derived Measurement`

No layer may overwrite upstream artifacts. Every transformation requires version, upstream IDs, execution metadata and deterministic output identity.

Require physically or access-logically separated `EVENT-TIME INPUT DATA` and `RESOLUTION / VALIDATION OUTCOME DATA`. Feature/event-time paths must not silently read outcomes. Catch-up, reversal/normalization, persistence, relationship continuation/break, horizon and magnitude remain outcome-side only. Database technology stays open unless requirements create a genuine decision need.

Storage authorization is not feature-use authorization. Resolution/outcome observations may later be acquired and stored for validation, but their presence in storage never makes them available at an earlier decision time or authorizes their use in mechanism inference.

| Decision | Classification |
|---|---|
| Immutable manifest, non-overwrite lineage, outcome quarantine, technology neutrality | READY TO FREEZE BEFORE ACQUISITION |
| Export/snapshot/version-retention capability | PROVIDER-AUDIT INFORMED |
| Request metadata, schema version, coverage fields and timestamp precision | FIELD/SCHEMA AUDIT INFORMED |
| Physical technology, sizing, credentials, scheduling and recovery | DEFER UNTIL FORMAL ACQUISITION |

## Researcher decisions genuinely required now

1. Approve **G3B-A** core-first scope, enhancement exceptions, research-only exclusion, PIT universe and sequence/stop rules.
2. Approve **G3B-B** neutral source criteria, conditional simplicity, canonical-plus-fallback, no silent mixing and clock-capability semantics.
3. Approve **G3B-C** security-master/PIT semantic contract and pre-threshold exception handling.
4. Approve **G3B-D** immutable manifests, deterministic lineage, outcome quarantine and technology neutrality.

Researcher approval on 2026-09-08 freezes all four blocks and both clarifications. Provider/field/schema and acquisition-time decisions remain unresolved exactly as classified. Formal acquisition still requires separate authorization.
