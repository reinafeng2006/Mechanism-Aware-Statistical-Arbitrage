# Core Dataset Freeze Criteria

Status: **APPROVED / FROZEN UNDER G3B-C1 — DATASET ITSELF NOT FROZEN**

Core Dataset Structural Freeze may be proposed only when all of the following are true:

1. zero unresolved security identities;
2. deterministic C01 lineage sufficient to identify every raw observation;
3. C03 acquisition complete under its documented limitations;
4. C06 PIT universe reconstruction complete under documented taxonomy and staleness limitations;
5. E02 and E03-A preserved under their documented limitations;
6. immutable raw artifacts and no upstream overwrite;
7. complete manifests and checksum integrity;
8. normalized-content consistency for duplicate requests, while preserving all raw provenance;
9. explicit C05 states, including unresolved observations retained as `UNKNOWN MISSINGNESS`;
10. explicit C04 state, including `CORPORATE_ACTION STATUS UNRESOLVED` where authoritative cleanliness is absent;
11. explicit C04/C05 coverage reports and candidate-impact lineage;
12. no silent fallback substitution or imputation;
13. event-time inputs and outcome-side information remain physically/logically quarantined;
14. no outcome leakage or empirical authorization is introduced by freeze.

Passing these criteria would establish a reproducible raw core only. It would not authorize any candidate measurement. Candidate use remains governed by a separately approved eligibility rule and the frozen G2B constraints.

C04/C05 qualification flags survive dataset freeze and every downstream transformation. A derived artifact must carry or deterministically recover its upstream observation eligibility, applicable candidate eligibility rule, and rule version.

Current state: **CRITERIA FROZEN / DATASET NOT FROZEN / AWAITING F2 READINESS AUDIT**.
