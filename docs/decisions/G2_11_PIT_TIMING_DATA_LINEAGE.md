# G2-11 — PIT Timing, Frequency, Latency & Data Lineage Freeze Decision

Status: **APPROVED / FROZEN**
Date: 2026-09-07
Boundary: semantic timing and data contract only. No provider, frequency, sampling interval, database technology, schema implementation or empirical procedure is selected.

## Decision objective

Define when information is legally and operationally available to each layer of the sequential strategy, and create the semantic Data Lineage & Timing Contract that G3 must later implement and audit.

## Common timing vocabulary

1. **`observation_time`** — when the underlying market/economic phenomenon occurred or the source record refers to. For intervals, both start and end must remain recoverable.
2. **`public_time`** — when information first became publicly disclosed, where applicable. It is distinct from the fiscal or observation period.
3. **`available_time`** — earliest time the project system could legitimately access and use the specific source vintage under its declared acquisition assumptions.
4. **`compute_time`** — when a derived measurement, signal, belief or other output became available after all inputs and computation were available.
5. **`decision_time`** — the decision origin whose PIT information set is being constructed and frozen.
6. **`outcome_time`** — a later timestamp or horizon used only for validation or target/outcome realization relative to the declared decision origin.

Every event-time input must satisfy:

`available_time ≤ decision_time`

Every derived event-time input must additionally satisfy:

`max(upstream available_time, compute_time) ≤ decision_time`

`retrieval_time` records when the project retrieved a record; it does not substitute for `public_time` or true `available_time`.

## Frequency is not latency

The contract separates:

- **source/update frequency** — how often the source can issue new records;
- **observation granularity** — the time span represented by each observation;
- **publication/availability latency** — delay between the phenomenon/period and legitimate usability;
- **computation latency** — time required after all inputs are available to produce a derived artifact;
- **decision-path latency** — total delay relevant to a declared decision path, including source, access and computation.

No actual frequency or interval is selected. Low-frequency content can become fast decision evidence when newly published: a quarterly filing may remain slow relationship context yet create a timestamped rejection/discriminator update at its first legitimate availability time.

## Multi-speed clock architecture

| Operational class | Semantic role | Timing rule |
|---|---|---|
| `SLOW PRIOR / CONTEXT` | precomputed relationship/economic context | use only a source vintage available by decision time; normally cacheable |
| `MEDIUM RELATIONSHIP STATE` | normal relationship, uncertainty, stability/break state | derived only from eligible PIT history; update time and version explicit |
| `FAST ABNORMALITY / MARKET EVIDENCE` | newly observed joint response and abnormality inputs | availability and compute completion must precede the decision origin |
| `FAST SEQUENTIAL UPDATE` | new discriminator, rival, rejection or resolution-relevant evidence | must be genuinely new at that sequential decision time |

Operational class is a role/latency contract, not a fixed source-frequency label. One information family may change role only when a new timestamped vintage or observation becomes legitimately available. Slow cached company context does not silently become fast evidence; a new public company event is a separate time-stamped update artifact under G2-05.

## Data Lineage & Timing Contract

Every future derived measurement, signal, belief and decision artifact must be traceable through:

`raw source → source vintage → availability time → transformation/version → derived measurement → downstream use`

Required semantic metadata:

| Field | Contract meaning |
|---|---|
| `source_id` / `source_class` | stable identity and category of the raw source |
| `entity_id` / `security_id` | entity or security to which the record applies |
| `source_vintage` / `source_version` | exact released or revised version used |
| `observation_start` / `observation_end` | phenomenon or accounting/market period represented |
| `public_time` | first public disclosure time where applicable |
| `available_time` | earliest legitimate system-use time for that vintage |
| `retrieval_time` | project ingestion/retrieval time, kept separate from availability |
| `transformation_id` / `transformation_version` | deterministic derivation identity and version |
| `upstream_input_ids` | immutable references to every raw/derived input |
| `derived_artifact_time` / `compute_time` | time the derived output became usable |
| `permitted_decision_time_start/end` | decision-origin range for which this vintage/artifact is eligible |
| `latency_update_class` | slow prior, medium state, fast abnormality or fast update role |
| `production_feasibility_status` | frozen G2-05 feasibility status and lineage |

Additional required status metadata includes missingness, staleness, revision/restatement flag, timestamp confidence/reliability, authorization/permitted-use status, and whether the artifact is event-time input, sequential-new-information or outcome-only validation.

This is a semantic contract, not a physical table definition, storage engine or database schema.

## Vintage, revision and restatement rules

1. Fiscal-period end is `observation_time`, not information availability.
2. Each revision/restatement is a distinct source vintage with its own public and available times.
3. Earlier decisions may use only the vintage legitimately available then; later corrected values cannot overwrite historical inputs.
4. Final-cleaned datasets must preserve or reconstruct the actually available historical vintage before event-time use.
5. Forward filling is permitted only as an explicitly authorized transformation of a previously available vintage, with staleness and lineage retained. It must never synthesize availability before first publication.
6. Corrections discovered later may enter a later sequential decision from their later availability time but cannot relabel an earlier decision record.
7. Uncertain or unavailable first-public/availability timestamps must be represented as data/provenance uncertainty and may route the case to U; they must not be optimistically imputed.

## Sequential-update timing rules

A state or belief may update only when its declared decision-time information set changes through genuinely new PIT information or a newly available authorized derivation.

Distinguish:

- **recomputation on unchanged information** — may reproduce or audit state, but is not new evidence;
- **new market observation** — a newly completed and available market record;
- **new company/event information** — a distinct released vintage available at its first legitimate time;
- **new relationship-state derivation** — an authorized update computed from newly eligible PIT history, with new transformation/version and compute time.

A code rerun, later retrieval, cache refresh or model execution on an unchanged input set cannot increment evidence merely because `compute_time` changed. Idempotent recomputation should reproduce the same versioned artifact or record why it differs.

Every sequential decision record must link its predecessor, enumerate newly admitted input IDs, distinguish carried-forward context from new evidence, and preserve the prior decision state.

## Production-feasibility timing extension

Every future candidate's G2-05 Production Feasibility record must additionally contain:

- expected source latency;
- timestamp reliability and time-zone/calendar convention;
- historical vintage availability;
- revision/restatement risk;
- cacheability and expiry/staleness behavior;
- expected computation latency;
- latency-critical-path status;
- operational tolerance for missing or delayed releases.

These fields describe feasibility, not evidence quality or predictive value. No provider is rated. Transformation simplicity does not overcome unreliable source timestamps or unavailable vintages.

## Prohibited timing and leakage shortcuts

- fiscal-period end used as public or available time;
- later restated/revised values inserted into earlier decisions without the proper vintage;
- final cleaned data used without preserving the historical information state;
- silent forward filling across pre-publication or unknown-availability intervals;
- future relationship breaks, normalization, catch-up, reversal, PnL or realized fundamentals used as earlier inputs;
- provider retrieval time substituted for actual information-availability time;
- compute time preceding the availability of any upstream input;
- repeated computation on unchanged data presented as new evidence;
- a later sequential state overwriting its earlier decision origin;
- time-zone, market-calendar or session-boundary assumptions left implicit.

## G3 handoff contract

If approved, G3 must translate this semantic contract into a physical PIT database and provider-audit design while preserving every timestamp distinction, vintage, upstream lineage, permitted decision range, role class and feasibility field. G3 must document provider-specific semantics, timestamp reliability, historical-vintage support, revisions, calendars, ingestion delays, deterministic transformations and reproducibility.

G3 may not weaken the semantic contract for provider convenience. Provider selection, acquisition, storage technology, table/schema design, frequencies and data-quality tests remain unauthorized until G3 is separately opened.

## Unresolved G2/G3 decisions

### G2-DEFER

- actual decision clocks and synchronization across inputs;
- acceptable timestamp uncertainty, staleness or compute delay;
- relationship-state and sequential update cadence;
- precise permitted decision-time range logic;
- treatment of simultaneous, out-of-order and corrected events;
- calendar/session/time-zone conventions;
- candidate-specific frequency and latency requirements.

### G3-DEFER

- providers and lawful access methods;
- physical database/schema/storage technology;
- source-specific timestamp definitions and vintage coverage;
- ingestion, cache, revision and reconciliation implementation;
- provider audit, quality controls and operational monitoring;
- actual data acquisition and universe coverage.

### EMPIRICAL-DEFER

- realized latency distributions and missingness;
- timestamp-error sensitivity and leakage audits;
- frequency/latency value trade-offs;
- production compute performance;
- revision effects, coverage, A-share transferability and OOS consequences.

## Frozen classification

### FROZEN SEMANTICS

- six-time common vocabulary and event-time eligibility inequalities;
- frequency/granularity/publication/computation/decision-path latency separation;
- four-class multi-speed architecture with role-dependent reuse;
- semantic lineage chain and required metadata;
- vintage/revision/restatement and non-overwrite rules;
- genuinely-new-information requirement for sequential updates;
- timing-related Production Feasibility fields;
- prohibited PIT/leakage shortcuts;
- G3 may implement but not weaken this contract.

### G2-DEFER

All actual clocks, frequencies, intervals, latency tolerances, staleness rules, cadence and candidate-specific timing choices.

### G3-DEFER

All providers, acquisition, provider audit, database technology, physical schema, ingestion and source-specific implementation.

### EMPIRICAL-DEFER

All timing calibration, realized feasibility, data-quality behavior, leakage testing and OOS effects.

G3 remains locked. No data acquisition, provider audit, implementation or empirical testing is performed.

## Approval record

Researcher approval on 2026-09-07 freezes the six-time vocabulary, event-time eligibility, derived-input readiness rule, frequency/latency separation, four-speed architecture, semantic lineage contract, vintage/revision/restatement preservation, forward-fill and retrieval-time restrictions, genuinely-new-information rule, historical-state preservation and all outcome-leakage prohibitions exactly as documented above.

Actual frequency, timestamp precision, provider, database technology, latency tolerance and implementation remain unresolved. G3 is not activated by this decision.
