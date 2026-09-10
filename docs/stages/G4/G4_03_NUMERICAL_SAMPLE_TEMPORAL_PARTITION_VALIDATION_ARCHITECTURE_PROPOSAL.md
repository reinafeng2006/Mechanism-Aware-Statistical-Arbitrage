# G4-03 Numerical Sample, Temporal Partition & Validation Architecture Proposal

Status: **ACCEPTED AS DECISION SCAFFOLD — NO NUMERICAL OR ARCHITECTURE SELECTION**  
Boundary: design only. No frozen-data inspection, descriptive statistics, returns, pairs, relationships, candidate measurements, targets, predictions, or outcomes.

## Objective

Define the decisions and competing protocol structures needed to turn the frozen G4-01 eligibility semantics and G4-02 temporal boundaries into a prespecified numerical validation architecture. This proposal does not choose any numerical value or architecture.

## Researcher Degrees-of-Freedom / Search Budget

`parameter search space is part of the statistical protocol`.

Every later numerical candidate set for history/formation length, update cadence, purge/embargo, outcome horizon, relationship representation, abnormality, UR/MP variants, thresholds, or another tunable quantity must be finite, small, justified by frozen theory/evidence/operational semantics, registered before outcome inspection, and versioned. Adding a value or branch after observing performance requires explicit protocol reopening plus a contamination record; it cannot silently remain confirmatory.

## A. Numerical sample-eligibility decisions

Every value below must be selected before the affected computation and recorded in a versioned candidate rule. Values may differ only where the candidate's semantic/data requirements justify the difference.

| Decision family | Required future choice | Governing boundary |
|---|---|---|
| Observation support | treatment of observed, unknown, suspended, resumed, and C04-unresolved dates | no silent fill/drop/reclassification; raw presence is not universal eligibility |
| Missingness burden | allowable count/share/run pattern of `UNKNOWN MISSINGNESS`, if any | observation unknown, window burden, and pair synchronization remain distinct |
| Corporate-action burden | whether/how raw candidates exclude, quarantine, or retain unresolved C04 dates | no presumed cleanliness; adjusted/action-dependent candidates remain constrained |
| Minimum history | minimum structurally eligible history for each candidate family | no value inferred from acquired coverage or later performance |
| Pair overlap | minimum synchronized candidate-eligible support | two eligible securities do not make a pair eligible |
| Listing/entry history | seasoning or incomplete-history rule | no current-universe or pre-membership backfill |
| Identifier transitions | exclusion/buffer/adjudication around code changes/restructurings | identity continuity is not economic continuity |
| C06 staleness | permissible classification age/stale-gap treatment | PIT-valid is not necessarily economically current |
| Source/schema transitions | acceptance or segmentation across source/schema changes | provenance differences remain visible |
| Comparison support | own-support and common/matched/stratified support policy | sample differences cannot masquerade as model quality |

No threshold, count, percentage, duration, or tolerance is proposed here.

## B. Competing temporal-partition architectures

The following are protocol candidates, not ranked or selected:

### TP0 — Single chronological development / sealed held-out split

One contiguous development region precedes one untouched final held-out region. It is operationally simple but may provide limited evidence on temporal stability and may make development choices sensitive to one period.

### TP1 — Rolling-origin development validation / sealed final held-out

Multiple time-ordered development origins evaluate fixed candidate steps using only prior information; a separate final region remains sealed. It can expose time variation but introduces choices about origin spacing, training history, aggregation, overlap, purge, and multiplicity.

### TP2 — Nested temporal development / sealed final held-out

An inner time-ordered loop governs parameter/window development and an outer development-validation loop governs candidate comparison before one final held-out evaluation. It offers stronger selection separation but consumes more history and adds operational/multiple-comparison complexity.

### TP3 — Regime- or calendar-stratified temporal validation / sealed final held-out

Prespecified dated strata may supplement TP0–TP2 to test stability across known calendar segments without using realized candidate performance to define regimes. Data-driven retrospective regime boundaries are prohibited unless separately designed and kept inside development.

No candidate is the default. The later choice must consider the finite frozen date envelope, candidate history demands, target horizons, overlap leakage, and sufficient untouched held-out support without inspecting results.

## C. Formation, update, and outcome geometry

For every evaluation origin, the later protocol must numerically bind:

`eligible history cutoff → formation/estimation interval → decision time → permitted sequential update times → outcome horizon`

Required decisions include:

- rolling versus expanding estimation history;
- formation refresh and relationship-state update cadence;
- whether adjacent evaluation origins may share estimation observations;
- purge/embargo treatment where input, label, or target horizons overlap;
- maximum outcome horizon and handling of censored end-of-partition outcomes;
- whether candidate clocks require separate geometries while retaining comparable decision origins.

No clock, cadence, window, horizon, purge, or embargo value is selected.

## D. Validation hierarchy

Later evaluation must proceed in dependency order:

1. **Structural eligibility validation:** masks reproduce from the frozen dataset/sidecar/rule versions and preserve all exclusion reasons.
2. **Relationship-level validation:** compare relationship representations, P0/P1, and N0/N1 on prespecified relationship objectives before downstream return or PnL claims.
3. **Abnormality-measurement validation:** assess representation/calibration of the abnormality state without treating it as mechanism or trade identification.
4. **Mechanism-evidence validation:** evaluate permitted M1/M2/M0/U constructs under their identification and rival boundaries; M3 production remains blocked.
5. **Resolution-prediction validation:** evaluate future direction, magnitude, timing, persistence, and resolution under quarantined targets.
6. **Decision/economic validation:** only later and separately authorized, using costs, constraints, and held-out discipline.

Passing a later layer never retroactively proves an earlier construct. Final PnL cannot be the first criterion for relationship or eligibility choices.

## E. Candidate comparison and sample-support architectures

Preserve three unselected reporting candidates:

- **CS0 — Candidate-native support:** report each candidate on its own frozen eligible sample, with complete support differences.
- **CS1 — Common support:** compare candidates only where all named candidates are jointly eligible.
- **CS2 — Dual/stratified support:** report candidate-native and common-support results plus prespecified support strata.

CS0 may confound sample and model differences; CS1 may discard informative coverage and favor narrow candidates; CS2 is more transparent but more complex and multiplicity-heavy. The comparison set, method, strata, and estimands remain unresolved.

## F. Development and held-out access architecture

Before any development access, freeze:

- exact partitions and hashes;
- permitted candidate families and parameter spaces;
- eligibility-rule versions;
- target definitions and horizons;
- metrics/estimands and multiplicity controls;
- stopping/pruning rules;
- output and access logs.

Before held-out access, freeze final implementations and every confirmatory decision above. Held-out access remains separately authorized, one-way, logged, and status-changing. G4-03 does not authorize either development or held-out access.

## G. Proposed decision classification

| Item | Classification |
|---|---|
| Numerical decisions must be candidate/rule-version bound and chosen before computation | **FREEZE SEMANTICS NOW** |
| Chronological direction; outcome strictly after decision origin | **FREEZE SEMANTICS NOW** |
| Dependency-ordered validation hierarchy | **FREEZE SEMANTICS NOW** |
| TP0–TP3 temporal structures | **COMPETING PROTOCOL CANDIDATES / NOT SELECTED** |
| CS0–CS2 sample-support reporting structures | **COMPETING PROTOCOL CANDIDATES / NOT SELECTED** |
| Eligibility tolerances, history, overlap, staleness, and transition values | **NUMERICAL PROTOCOL DECISION LATER** |
| Formation/update windows, horizons, purge, embargo, and origin spacing | **NUMERICAL PROTOCOL DECISION LATER** |
| Candidate-specific clocks and support requirements | **CANDIDATE-SPECIFIC** |
| Stability, sensitivity, calibration, and adequacy findings | **EMPIRICAL VALIDATION LATER** |
| Development and held-out access | **SEPARATE RESEARCHER AUTHORIZATION** |

## Dependency-ordered researcher decision blocks

### Block A — Sample & Estimation Geometry

Resolve candidate-specific C04/C05 handling; minimum history, missingness, staleness, identifier/source transitions; formation/estimation horizons; update cadence; outcome horizons; and conditions/lengths for purge or embargo. Register the finite Search Budget and distinguish ex-ante fixed quantities from development-selectable candidates.

### Block B — Temporal Validation Architecture

Compare TP0–TP3 against dynamic relationship stability and OOS robustness; choose exact development, internal-validation, and held-out boundaries; bind access controls, target censoring, and temporal evaluation sequence. Walk-forward/nested pseudo-OOS remains a candidate, not a selection.

### Block C — Candidate Comparison / Common Support

Choose pair synchronization/overlap and CS0–CS2 or another approved support architecture; distinguish native-support from common-support evaluation; bind candidate/parameter spaces, metrics, multiplicity, stopping, pruning, and the sequence of development then separately authorized held-out access.

No TP0–TP3, CS0–CS2, window, horizon, tolerance, purge, embargo, or update cadence is selected by acceptance of this scaffold.

`G4-03 DECISION SCAFFOLD ACCEPTED / BLOCK A PROPOSAL ACTIVE`
