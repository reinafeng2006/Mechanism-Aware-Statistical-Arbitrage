# Current G1 Bibliography and Triage Control

Status: **MIGRATED SCHEMA — EXISTING INVENTORY REMAINS AUTHORITATIVE**

The existing inventory in `registers/G1_CANDIDATE_PAPERS.md` remains the authoritative paper-level record for G1-01/G1-02. This file supplies the adapted operating-system fields for all future records; it does not re-review or re-admit any paper.

## Required paper-level fields

| Field | Current-project requirement |
|---|---|
| Candidate ID | Current stable ID, e.g. PF-001, M1-001, M2-001, M3-001, M0-001, B4-001 |
| Current G1 question(s) | One or more of A-P1–A-P3 and B-P1–B-P4 |
| Status | `DISCOVERED`, `TRIAGED`, `REVIEWED_LIGHT`, `REVIEWED_DEEP`, `ADMITTED_FOR_BOUNDED_CLAIMS`, `DEFERRED`, or `REJECTED` |
| Full-text basis | Access route, version/date, access date, lawful-use boundary, and retention constraint |
| Decision relevance | Named G2-relevant decision or missing link; not popularity/citation count |
| Review depth | `DISCOVERY`, `TRIAGE`, `LIGHT`, or `SELECTIVE_DEEP`, with trigger/rationale |
| Construct / role | Candidate construct and P/S/C/R role; no factor/formula selection |
| Transferability | Market, sample, period, and A-share-machinery limits |
| Ancestry | Search-run → candidate → source version → current Claim ID(s) |

## Prohibited import

Predecessor bibliography rows, Paper IDs, categories, paper admission decisions, depth decisions, and local file paths are not valid current rows. A common title may be added only after current-project triage and current ID assignment.
