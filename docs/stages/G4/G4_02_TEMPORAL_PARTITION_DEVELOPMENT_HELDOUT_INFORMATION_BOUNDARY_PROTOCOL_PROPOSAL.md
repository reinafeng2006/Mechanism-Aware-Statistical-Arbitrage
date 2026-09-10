# G4-02 Temporal Partition, Development/Held-Out & Information-Boundary Protocol Proposal

Status: **G4-02 APPROVED / FROZEN — 2026-09-10**  
Scope: protocol design only. No frozen-data access, descriptive statistic, return, pair, relationship, measurement, target, prediction, or outcome inspection.

## Objective

Prespecify the temporal and access boundaries under which later candidate development, comparison, validation, and held-out evaluation may occur without adapting the protocol to future information or repeatedly consuming held-out evidence.

The dataset's acquisition range is not itself an analysis partition. No calendar boundary, percentage split, window, horizon, embargo, or reuse count is selected here.

## 1. Frozen timing vocabulary

Every later analytical record must preserve the frozen six-time vocabulary:

- `observation_time`: time the phenomenon occurred or the record describes;
- `public_time`: first public disclosure time where applicable;
- `available_time`: first legitimate system-use time;
- `compute_time`: time a derived artifact becomes available after all inputs;
- `decision_time`: origin whose information set is constructed;
- `outcome_time`: later time used only for validation.

For every event-time input:

`available_time ≤ decision_time`

For every derived input, all upstream inputs must be available and computation complete by the decision time. Retrieval time cannot replace historical availability time. Repeated computation on unchanged information is not new evidence.

## 2. Conceptual temporal partitions

The later protocol must distinguish at least:

1. **Protocol-design zone:** governance and specification work performed without empirical inspection.
2. **Development zone:** the only zone in which authorized candidate construction, parameter/window development, diagnostics, and bounded comparison may occur.
3. **Development-internal validation zone:** temporally later evidence used for authorized selection/robustness within development governance; it is not the final held-out test.
4. **Held-out zone:** inaccessible during specification and development; reserved for separately authorized one-way evaluation under a frozen protocol.
5. **Outcome zone:** future observations used to construct validation targets for a fixed earlier decision origin; logically/physically inaccessible to event-time feature construction even when they fall inside a development period.
6. **Post-freeze/future-use zone:** data outside `CORE-DATASET-FREEZE-V1` or acquired later; unavailable unless a new dataset version/amendment and protocol authorization explicitly admits it.

These are roles, not selected dates. A calendar observation can be an event-time input for a later decision and an outcome for an earlier decision; access must be determined by the specific decision origin and artifact path, not by field identity alone.

## 3. Formation and evaluation separation

For each candidate evaluation origin, the protocol must version:

- relationship/pair formation information cutoff;
- estimation window and its candidate-specific G4-01 eligibility mask;
- decision origin and information set;
- update times containing genuinely new PIT information;
- target horizon beginning strictly after the decision origin;
- evaluation/selection role of the resulting record.

Formation, tuning, validation, and target intervals may not silently overlap in a way that transmits future information. Whether rolling, expanding, blocked, walk-forward, nested, purged, or embargoed structures are used remains unresolved.

## 4. Development governance

Development access must be bounded by an approved protocol version. Every inspected output must record dataset freeze ID, partition version, candidate and eligibility-rule versions, parameters, code version, access time, and purpose.

Development may not use held-out results, post-held-out tuning, or outcome variables as event-time features. Choices triggered by development findings require an auditable decision record and remain inside the authorized development search space.

## 5. Held-out governance

Held-out data remain sealed until a separate authorization confirms that all prerequisite measurement, target, metric, multiple-comparison, and stopping rules are frozen.

Before opening held-out evidence, the protocol must freeze:

- exact partition identity and hash;
- allowed candidates and fixed implementations;
- evaluation metrics/estimands and decision rules;
- multiplicity handling;
- permitted outputs and disclosure granularity;
- access owner, audit log, and one-way release procedure;
- whether any reuse is allowed and what consequence follows from inspection.

Held-out inspection cannot be undone. Any post-inspection modification creates a new declared research status and may require a new untouched holdout; it cannot silently retain the original confirmatory label.

No number of held-out accesses or reuse policy is selected here.

## 6. Outcome and target boundary

Future catch-up, reversal/normalization, persistence, relationship continuation/break, resolution horizon/magnitude, realized fundamentals, returns, and PnL are outcome-side information relative to an earlier decision time.

They may be constructed only under a later frozen target protocol in the quarantined outcome path. They may never enter earlier pair formation, normal-relationship estimation, abnormality, M0/M1/M2/U inference, or sequential updates before becoming genuinely observable at a later decision time.

The same raw market record may support later outcome construction and a different later decision state, but each use requires distinct lineage and access roles.

## 7. Eligibility and partition interaction

Each partition is applied after binding `CORE-DATASET-FREEZE-V1` and before candidate computation. G4-01 candidate masks remain decision-time-specific and cannot be defined using support observed in future partitions.

Competing candidates must report both temporal partition support and eligibility-mask support. A candidate cannot gain a favorable comparison by using information, securities, or dates unavailable to its competitor without the sample-support difference being exposed under the later fair-comparison protocol.

## 8. C06, identifiers, and structural states through time

- C06 membership uses only classifications available by each decision time; future membership/taxonomy information cannot revise earlier partitions or masks.
- Classification age/staleness remains visible within every partition.
- `601313.SH → 601360.SH` remains identifier lineage only; partition boundaries do not establish economic continuity.
- `UNKNOWN MISSINGNESS` and `CORPORATE_ACTION STATUS UNRESOLVED` remain durable states across partitions and cannot be resolved using later outcomes.

## 9. Versioning, amendments, and leakage incidents

Every partition definition is immutable and versioned with dataset ancestry. Changing dates, roles, access permissions, embargo/purge rules, target horizons, or reuse policy requires a new explicit protocol version; previous partitions and inspection logs remain preserved.

Any accidental held-out access, outcome-to-input path, future classification use, unavailable vintage use, or partition misassignment is a reportable leakage incident. The affected artifact cannot be treated as clean merely by rerunning it.

## Frozen classification

| Decision | Classification |
|---|---|
| Six-time vocabulary and `available_time ≤ decision_time` | **FREEZE SEMANTICS NOW** |
| Distinct design/development/internal-validation/held-out/outcome/future-use roles | **FREEZE SEMANTICS NOW** |
| Held-out sealed until separate authorization; inspection is irreversible | **FREEZE SEMANTICS NOW** |
| Outcome-to-input prohibition and decision-origin-specific role lineage | **FREEZE SEMANTICS NOW** |
| Immutable versioned partitions, access logs, and leakage-incident handling | **FREEZE SEMANTICS NOW** |
| Exact calendar boundaries and allocation proportions | **NUMERICAL PROTOCOL DECISION LATER** |
| Rolling/expanding/blocked/walk-forward/nested structure | **NUMERICAL PROTOCOL DECISION LATER** |
| Embargo, purge, overlap, update, and target-horizon lengths | **NUMERICAL PROTOCOL DECISION LATER** |
| Candidate-specific formation/estimation/update clocks | **CANDIDATE-SPECIFIC** |
| Held-out access/reuse count and release outputs | **LATER RESEARCHER AUTHORIZATION** |
| Sensitivity, stationarity across partitions, and transferability | **EMPIRICAL VALIDATION LATER** |

## Dependency-ordered unresolved decisions

1. permissible analysis period within the frozen 2013-01-07–2025-12-31 acquisition envelope;
2. temporal partition architecture and exact boundaries;
3. formation/estimation/decision/update clock relationships;
4. overlap, purge, and embargo governance;
5. development search and internal-validation sequence;
6. target horizons and outcome-zone construction rules;
7. held-out seal, access owner, release contents, and reuse consequences;
8. partition-aware common-support reporting for competing candidates;
9. post-inspection amendment, failure, and new-holdout rules.

All numerical and structural partition choices remain unresolved.

`G4-02 APPROVED / FROZEN`
