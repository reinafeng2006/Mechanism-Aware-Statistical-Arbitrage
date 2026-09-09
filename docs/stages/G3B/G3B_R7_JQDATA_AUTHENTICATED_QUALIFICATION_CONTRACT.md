# G3B-R7 — JQData Authenticated Integrated-Platform Qualification

Status: **PAUSED — ACCESS COST EXCEEDS RESEARCHER BUDGET**
Formal acquisition: **NOT AUTHORIZED**  
Platform purchase: **NOT AUTHORIZED**

## Objective

Determine whether JoinQuant/JQData can serve as the primary 2013–2025 historical research platform for C01/C03/C04/C05/E02/E03, with the official C06 historical industry-classification path retained as the authoritative exception.

Public documentation is no longer admissible for unresolved hard requirements when the answer requires authenticated fields, paid/trial entitlement, endpoint behavior, quota information, licence terms or historical query evidence.

## Access boundary

R7 may begin only after the researcher confirms legitimate trial/paid JQData access. Credentials must never be printed, logged, transmitted to chat, stored in artifacts or committed.

Without authenticated access, every hard question below remains `UNRESOLVED`; public marketing cannot upgrade it.

## Deterministic non-empirical QA slice

The authenticated QA, when available, must be selected solely for contract coverage and include:

- one SSE and one SZSE security;
- one early-history and one late-history interval;
- one known corporate-action case;
- one known suspension case;
- one benchmark constituent/weight history case;
- one share-capital/turnover field case.

The exact securities/dates must be pre-registered from authoritative event documentation or mechanical coverage criteria, never returns or strategy outcomes. Outputs are `AUDIT/QA — NON-EMPIRICAL`, immutable, checksummed and prohibited from later research use unless separately reacquired under formal authorization.

## Contract tests

### C01 — Security Master

Verify historical security identity, listing/delisting, dated universe behavior, identifier consistency, name/code changes where supported, schema and correction behavior.

### C03 — Market Data

Verify 2013–2025 SSE/SZSE coverage; raw/unadjusted mode; OHLCV/money definitions and units; trading calendar; missing-observation behavior; paused-row treatment; deterministic repeated retrieval and restart reproducibility.

### C04 — Corporate Actions / Adjustment

Test separately:

1. raw corporate-action records and their publication/effective dates;
2. adjustment factors;
3. factor formula, basis and version;
4. retrospective revision behavior;
5. availability of historical factor vintages/revision lineage.

`factor exists ≠ PIT corporate-action lineage qualified`.

### C05 — Suspension / Trading Status

Verify historical `paused` and related status semantics; distinction among suspension, non-listing, delisting, source failure and missing observation; any reason/publication/revision fields; and whether filled prices can be excluded from genuine observations.

### E02 — Liquidity / Share Capital

Test separately: directly observed volume/money, turnover, total shares, circulating shares and free-float shares. For denominators, verify definition, unit, effective time, first availability and revision/vintage behavior—not merely the ability to query a historical value today.

### E03 — Benchmark / Constituents / Weights

Verify benchmark prices, date-specific constituents, historical weights, announcement/effective/available-time meanings and whether later revisions change past queries.

## Cross-platform tests

Record:

- Python/local SDK and batch interfaces;
- account/tier-visible quota and rate limits;
- maximum rows/date span/query size;
- full-universe batch feasibility without executing it;
- schema version/stability and change notices;
- historical revision policy;
- local immutable research-storage rights;
- reproducibility after logout/session/process restart;
- retention, export, automation and redistribution restrictions;
- exact trial/paid tier needed for 2013–2025.

## Required provenance artifacts

- sanitized request specification with no credential or account identifier;
- account/tier capability summary without personal information;
- endpoint/field/schema version;
- raw response snapshot under ignored QA storage;
- retrieval/compute timestamps;
- row counts, coverage metadata and checksums;
- deterministic rerun comparison;
- licence/terms summary or non-sensitive provider statement reference;
- contract-by-contract test result and approximation gap.

## Qualification decisions

Each contract receives exactly one:

- `PASS`;
- `PASS WITH LIMITATIONS`;
- `FAIL`;
- `UNRESOLVED`.

The platform receives exactly one:

- `QUALIFIED PRIMARY HISTORICAL PLATFORM`;
- `QUALIFIED PRIMARY + AUTHORITATIVE COMPANION REQUIRED`;
- `INTEGRATED PLATFORM WITH MATERIAL LIMITATIONS`;
- `NOT QUALIFIED`.

The output must state the minimum additional production integrations, including C06, and trace each extra source to a failed/limited contract. It must not recommend empirical models or infer predictive value.

## Prohibitions

No purchase, full-history acquisition, source promotion, pair construction, relationship/abnormality/UR/MP/R computation, resolution target, prediction, return analysis or PnL. R7 stops after qualification for researcher decision.

## Current disposition

No authenticated access has been supplied in the current project context. Therefore the QA has not started and all authenticated hard tests remain unresolved.

`G3B-R7 JQDATA AUTHENTICATED QUALIFICATION PAUSED / TUSHARE R8 ACTIVE`
