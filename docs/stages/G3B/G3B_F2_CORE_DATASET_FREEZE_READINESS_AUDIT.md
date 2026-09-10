# G3B-F2 Core Dataset Freeze Readiness Audit

Status: **G3B-F2 CLOSURE COMPLETE / CORE DATASET FREEZE DECISION REQUIRED**  
Audit date: 2026-09-10  
Boundary: structural audit of already-acquired artifacts only. No acquisition, measurement, target, relationship, return, or outcome computation was performed.

## Decision

`CORE DATASET ELIGIBLE FOR FREEZE`

The sole prior blocker has been closed by the deterministic, immutable [Security-Date Eligibility Sidecar](SECURITY_DATE_ELIGIBILITY_SIDECAR_CONTRACT.md). All hard structural criteria now pass and no previously passing criterion regressed. This is a readiness recommendation only: the dataset is not automatically frozen and no measurement is authorized.

## Criterion audit

| # | Amended Core Dataset Freeze criterion | Status | Evidence / limitation |
|---:|---|---|---|
| 1 | Zero unresolved security identities | **PASS** | The sole historical mismatch is authoritatively resolved as `601313.SH → 601360.SH`; unresolved identity count is zero. |
| 2 | Deterministic C01 identifier lineage | **PASS WITH DOCUMENTED LIMITATION** | C01 snapshots and the versioned identifier-resolution register identify raw records. The mapping establishes security lineage only; economic continuity and automatic series splicing remain prohibited. |
| 3 | C03 complete under documented limitations | **PASS WITH DOCUMENTED LIMITATION** | 751/751 unique requests succeeded; 1,525,136 rows cover 2013-01-07–2025-12-31. One historical request is represented through the authoritative successor-code mapping; provider vintage and missing-session limitations persist. |
| 4 | C06 PIT universe reconstruction and staleness metadata | **PASS WITH DOCUMENTED LIMITATION** | Official snapshots, publication-date lineage, 15,886 membership rows, 861-security union, and the frozen carry-forward/staleness contract are preserved. Classification age/stale-gap remains deterministically derivable rather than materialized for every decision date; known long gaps remain explicit. |
| 5 | E02/E03-A complete under documented limitations | **PASS WITH DOCUMENTED LIMITATION** | E02: 751/751 requests and 1,525,131 rows; E03-A: 1/1 request and 3,156 rows. E02-B PIT/vintage and E03-A provider-vintage limitations remain. |
| 6 | Immutable raw artifacts | **PASS** | Acquisition writes new immutable payload names, including retry objects; no successful object was overwritten or deleted. |
| 7 | Manifests/checksums | **PASS** | Manifest and acquisition journal are preserved; structural validation reports zero journal-referenced checksum failures. |
| 8 | Duplicate normalized-content consistency | **PASS** | All 877 duplicate-success groups have identical normalized `fields/items` hashes; zero semantic-content mismatches. Dynamic provider `request_id` differences remain preserved in raw hashes. |
| 9 | C04/C05 flags and coverage gaps preserved | **PASS WITH DOCUMENTED LIMITATION** | C04 remains `AUTHORITATIVE COVERAGE INCOMPLETE`; 49,568 candidate sessions across 425 securities remain `UNKNOWN MISSINGNESS`. Coverage is preserved at report/contract level, but observation-level propagation is the criterion-12 blocker. |
| 10 | No silent imputation | **PASS** | Validation treats absent rows as a diagnostic set only; it creates neither price nor trading-state values and does not infer suspension. |
| 11 | Input/outcome quarantine | **PASS WITH DOCUMENTED LIMITATION** | Acquisition manifests exclude measurements and outcomes, and no outcome artifacts were constructed. The logical access boundary is frozen; physical outcome separation has not yet been exercised because the outcome store does not exist. |
| 12 | Observation/candidate eligibility metadata capable of downstream propagation | **PASS** | The immutable 1,575,837-row sidecar binds unique stable-security/date keys to C04/C05 states, bases, upstream references, schema and eligibility-rule versions. It contains no universal eligibility flag; later candidate masks must derive from the sidecar plus a frozen candidate rule. |
| 13 | Acquisition single-writer control | **PASS WITH DOCUMENTED LIMITATION** | The runner uses an acquisition-scope exclusive lock and preserves the prior duplicate-run incident. Crash/stale-lock operating procedure remains an implementation concern, but concurrent same-scope starts are prevented. |
| 14 | Deterministic reconstruction from frozen raw artifacts | **PASS WITH DOCUMENTED LIMITATION** | Versioned scripts, raw payloads, C06 union, identifier register, request journal, manifests, and normalized hashes reproduce the structural counts and contract statuses. Reconstruction retains the documented C04/C05 and provider-vintage gaps. |

## Criterion-12 closure evidence

The approved closure produced:

- schema `SECURITY_DATE_ELIGIBILITY_SIDECAR_V1`;
- rule `G3B-C1-C04-C05-ELIGIBILITY-V1`;
- 1,575,837 unique stable-security/date rows;
- 1,526,269 `NORMAL TRADING OBSERVED` rows and all 49,568 prior unresolved sessions retained as `UNKNOWN MISSINGNESS`;
- C04 retained as `CORPORATE_ACTION STATUS UNRESOLVED` without action cleanliness inference;
- immutable artifact SHA-256 `A4418E69EDAF92CE0A16DCE72FD6551DA245CF182252528CCB5224768EA9705A`;
- upstream artifact hashes, stable schema/order, manifest, and deterministic regeneration **PASS**;
- no universal eligible flag and no imputation or empirical output.

The structural validator was rerun after generation: 751-security coverage, 877 duplicate groups with zero normalized-content disagreements, zero journal checksum failures, and all prior documented C04/C05/E02/E03 limitations remain unchanged.

## Preserved non-authorizations

The audit does not freeze the dataset, authorize any observation or candidate for empirical use, construct adjusted prices, select a missingness rule, begin G4, or inspect research outcomes.

`G3B-F2 CLOSURE COMPLETE / CORE DATASET FREEZE DECISION REQUIRED`
