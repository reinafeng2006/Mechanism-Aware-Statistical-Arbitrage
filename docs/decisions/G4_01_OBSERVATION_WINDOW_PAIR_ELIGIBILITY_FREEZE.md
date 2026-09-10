# G4-01 Observation, Window & Pair Eligibility Freeze

Decision: **APPROVED / FROZEN — 2026-09-10**

The researcher froze observation, window, pair, and candidate-specific eligibility as distinct layers. Eligibility is indexed by candidate, entity/pair, decision time, and rule version; no universal eligibility flag is permitted.

Frozen requirements:

- C04/C05/C06, provenance, missingness, and identifier states propagate into every downstream mask;
- unknown observations cannot be silently dropped, filled, or reclassified;
- pair synchronization exclusions and reasons remain explicit;
- raw-data candidates receive no presumed corporate-action cleanliness;
- later competing-specification comparisons expose unequal eligible-sample support;
- masks are reproducible and versioned from `CORE-DATASET-FREEZE-V1`, the frozen sidecar, and the applicable frozen candidate rule/version.

The authoritative protocol is [G4-01](../stages/G4/G4_01_OBSERVATION_WINDOW_PAIR_ELIGIBILITY_PROTOCOL_PROPOSAL.md), supported by its [Candidate Rule Matrix](../stages/G4/G4_01_CANDIDATE_ELIGIBILITY_RULE_MATRIX.md), [Dependency Graph](../stages/G4/G4_01_ELIGIBILITY_DEPENDENCY_GRAPH.md), and [Deferred Numerical Queue](../stages/G4/G4_01_UNRESOLVED_NUMERICAL_DECISION_QUEUE.md).

No tolerance, window, history length, staleness threshold, synchronization threshold, common-support rule, eligibility mask, statistic, or measurement is selected or computed.
