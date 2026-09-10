# G4-01 Eligibility Dependency Graph

Status: **APPROVED / FROZEN — CONCEPTUAL CONTROL FLOW ONLY**

```text
CORE-DATASET-FREEZE-V1
  ├─ C01 identity / listing intervals
  ├─ C03 raw-record presence
  ├─ C04 structural qualification
  ├─ C05 trading / missingness state
  ├─ C06 PIT membership + age / staleness
  ├─ E02 / E03-A qualification metadata
  └─ source / schema / provenance lineage
                 │
                 ▼
Security-Date Eligibility Sidecar
(structural states only; no global eligible flag)
                 │
                 ├──────────────┐
                 ▼              ▼
 Candidate eligibility      Candidate eligibility
 rule/version A             rule/version B
                 │              │
                 ▼              ▼
 Observation mask A         Observation mask B
                 │              │
                 ▼              ▼
 Window-support record A    Window-support record B
                 │              │
                 └──────┬───────┘
                        ▼
 Representation-appropriate pair synchronization
 (support dates and all exclusions/reasons retained)
                        │
                        ▼
 Candidate/pair/decision-time eligibility mask
                        │
                        ▼
 Later statistical computation — separately authorized only
```

## Invariants

- A downstream node inherits all upstream freeze IDs, hashes, states, and rule versions.
- An unknown/unresolved upstream state cannot be promoted merely by aggregation.
- A window cannot conceal which dates or reasons reduced support.
- Two individually eligible histories do not establish pair eligibility.
- Candidate A and Candidate B may legally produce different masks from the same structural sidecar, but comparisons must expose the resulting support difference.
- A rule change creates a new branch/version; it never mutates an existing mask.
- No graph edge computes a return, relationship, abnormality, mechanism belief, target, outcome, or PnL during G4-01.
