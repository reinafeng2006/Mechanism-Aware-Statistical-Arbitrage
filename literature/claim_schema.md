# Current G1 Claim, Edge, and Data-Linkage Schema

Status: **ADAPTED PROCESS SCHEMA — NO NEW CLAIM ADMISSION**

## Claim record

Each current Claim ID must preserve the existing substantive fields in `registers/LITERATURE_EVIDENCE.md` and add the following control fields when new claims are extracted or when G1-03 reviews an existing claim:

```yaml
claim_id: CL-<family>-<number>
candidate_id: <current candidate ID>
primary_question: A-P1 | A-P2 | A-P3 | B-P1 | B-P2 | B-P3 | B-P4
construct_or_mechanism: ""
pscr_role: [P, S, C, R]
full_text_basis:
  access_route: ""
  source_version: ""
  access_date: ""
  permitted_use_boundary: ""
source_locator:
  page: null
  section: ""
  table_figure: null
claim_paraphrase: ""
exact_observable_or_method: ""
what_identified: ""
what_not_identified: ""
logic_chain:
  premise: {statement: "", status: ASSUMED}
  measurement_identification: {statement: "", status: ESTIMATED}
  intermediate_evidence: {statement: "", status: OBSERVED}
  inference: {statement: "", status: INFERRED}
  final_claim: {statement: "", status: INFERRED}
limitations: []
point_in_time_causal_timing_limitations: ""
sample_market_transferability: ""
competing_explanations: []
missing_link: ""
validation_test_needed: ""
project_testability: ""
data_requirement_ids: []
permitted_g2_candidate_use: []
prohibited_interpretations: []
review_depth: LIGHT | SELECTIVE_DEEP
evidence_direction: SUPPORTS | WEAKENS | MIXED | UNRESOLVED
ancestry: "search run → candidate → full-text source/version → claim"
status: PROVISIONAL_G1_02 | SYNTHESIZED_G1_03 | FROZEN_G1_04 | SUPERSEDED
```

The five logic-link states are `OBSERVED`, `ESTIMATED`, `ASSUMED`, `INFERRED`, and `EXTERNALLY_VALIDATED`. Claim-level credibility, where used, is written reasoning rather than a paper-level score.

## Claim-edge schema

```yaml
edge_id: CE-<number>
from_claim_id: CL-...
to_claim_id: CL-...
relationship: SUPPORTS | CONTRADICTS | QUALIFIES | REPLICATES | EXTENDS | DEPENDS_ON
comparison_dimensions:
  construct_or_mechanism: ""
  market_population: ""
  sample_period: ""
  horizon: ""
  method_or_estimand: ""
  point_in_time_timing: ""
  regime_or_market_structure: ""
status: OPEN | NARROWED | RESOLVED | DEFERRED_TO_G2
notes: ""
```

Contradictions are not settled by paper count. They must be narrowed by construct, sample, horizon, timing, method, or rival mechanism—or remain open.

## Data-linkage schema

Every literature-motivated data requirement must link to one or more current Claim IDs and retain current provisional status until G1-04:

```yaml
data_requirement_id: DR-<number>
construct: ""
candidate_observable: ""
pscr_role: P | S | C | R | OUTCOME_ONLY
frequency_candidate: ""
point_in_time_requirement: ""
history_requirement: ""
source_class_not_provider: ""
raw_or_derived: RAW | DERIVED | MIXED
claim_ids: []
missing_link: ""
validation_test_needed: ""
project_testability: ""
status: PROVISIONAL_G1_02 | SYNTHESIZED_G1_03 | FROZEN_G1_04
```

`OUTCOME_ONLY` may support later evaluation but is prohibited from event-time mechanism labeling.
