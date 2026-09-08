# G3B Formal PIT Data Acquisition Design — Superseded Initial Draft

Status: **SUPERSEDED / RETAINED FOR WORKING-PROCESS TRACEABILITY**  
Formal acquisition: **NOT AUTHORIZED**  
Empirical computation/outcome inspection: **PROHIBITED**

The current authoritative working state is the [four-block G3B Acquisition Design Proposal](G3B_ACQUISITION_DESIGN_PROPOSAL.md). D1–D10 below are retained only as the initial working draft and are not separate approval gates. The draft preserved minimum/enhancement separation, Production Data Tiers, PIT lineage, universe coverage, multi-frequency envelopes, outcome quarantine and provider neutrality.

## Dependency-ordered researcher decisions required before acquisition

### D1 — Acquisition scope by Production Data Tier

Approve whether the first formal acquisition authorization would cover:

- all `CORE-FEASIBILITY` raw information classes only; or
- core plus a separately enumerated subset of `OPTIONAL-ENHANCEMENT` classes.

`RESEARCH-ONLY` data must remain excluded absent separate later authorization. Missing enhancements must not block the core acquisition design.

### D2 — Operational target-universe contract

Define the production-universe membership source/class and historical membership rules needed to include entrants, exits, suspensions and delistings without survivorship bias. Numerical coverage thresholds, minimum listing history and missingness tolerances remain undecided and require approval before acquisition acceptance criteria can be frozen.

### D3 — Provider/source evaluation and selection protocol

Approve a provider-neutral comparison procedure covering lawful use, non-display/research rights, PIT/vintage integrity, history, universe coverage, update burden, reproducibility, source stability, pricing and exit/portability risk. No source is selected at this checkpoint; source selection must be an explicit later decision.

### D4 — Clock/granularity acquisition envelopes

For each raw class, approve the coarsest acquisition capability that must be available for later comparison while keeping finer clocks as separately costed enhancements. The decision must preserve relationship-history, ordered-market-response and event-publication capability without yet selecting a model or claiming that finer data are superior.

### D5 — PIT timestamp and vintage acceptance standard

Freeze the minimum evidence required to accept `public_time`/`available_time`, source vintages, corrections/restatements, corporate-action versions, classification membership and first-public event timestamps. Decide how records with unverifiable availability time are quarantined or excluded; retrieval time may never substitute for availability time.

### D6 — Security master and adjustment lineage policy

Approve the required identifier history, listing-state, corporate-action and adjustment provenance contract. This is an acquisition/lineage decision only; it must not select a return definition, adjustment formula or relationship estimator.

### D7 — Coverage, missingness and source-failure acceptance policy

Define prespecified acceptance/reporting rules across time, securities and data classes, including source outages, schema changes, partial histories and revision gaps. These rules must not be tuned after inspecting pair relationships or outcomes.

### D8 — Input/outcome physical quarantine design

Approve separate namespaces/stores and access controls for event-time inputs versus future resolution-validation observations. Catch-up, reversal/normalization, persistence, relationship continuation/break, horizon and magnitude must be collectible as outcome-side raw observations but inaccessible to earlier decision-state construction.

### D9 — Deterministic ingestion, lineage and snapshot contract

Approve requirements for immutable raw snapshots, checksums, source/version manifests, transformation-free landing, acquisition logs, schema versions, upstream IDs and reproducible reruns. Select physical storage/database technology only after these semantic requirements are accepted.

### D10 — Acquisition sequencing, budget and stop rules

Approve a bounded order: security/universe lineage → core market history → industry/benchmark vintages → quality/lineage metadata → competing implementable classes → explicitly approved enhancements → quarantined outcome observations. Define budget/licensing ceilings, failure/escalation rules and the condition for stopping before expansion. No acquisition starts with this decision list.

## Explicitly not decided here

- provider or vendor;
- exact fields, frequencies, date range or numerical coverage threshold;
- database/storage technology;
- adjustment, factor, relationship, abnormality, mechanism or resolution formula;
- estimator, window, threshold, label, model or trade rule;
- any empirical winner or performance claim.

The next action requires researcher resolution of D1–D10 or authorization to prepare bounded alternatives for them. Until then, G3B remains design-only and formal acquisition remains unauthorized.
