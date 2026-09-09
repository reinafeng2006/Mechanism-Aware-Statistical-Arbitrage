# G3B-FULL Acquisition Structural Checkpoint

Status: **G3B STRUCTURAL RESOLUTION COMPLETE / AWAITING DATASET FREEZE DECISION**

The Tushare portion of the authorized acquisition runner reached its deterministic request-plan endpoint. No measurements, pair relationships, targets, predictions, returns or PnL were computed or inspected.

## Preserved raw acquisition

- PIT machinery request universe: 751 SSE/SZSE securities derived from the C06 union;
- C01: 3 unique successful listing-status requests, 5,899 returned security records;
- C03: 751/751 unique successful requests, 1,525,136 rows, 2013-01-07 through 2025-12-31;
- E02: 751/751 unique successful requests, 1,525,131 rows, 2013-01-07 through 2025-12-31;
- E03-A: 1/1 unique successful request, 3,156 rows, 2013-01-07 through 2025-12-31;
- all required returned-field schemas present;
- no duplicate trade dates within a canonical security payload;
- acquisition journal: 2,393 events; every referenced file checksum passes;
- the original 3 C01 and 7 E02 permission-failure events remain preserved.

The completed immutable Tushare manifest SHA-256 is `AB8F27B4D5CA419BE5FCB00406DF58B71A6489C34846A578983C5D8C19CE5776`.

## Concurrent-resume incident

The initial foreground process remained alive after its command wrapper returned, overlapping temporarily with the explicitly launched background runner. The earlier duplicate process was stopped as soon as it was detected. No payload was deleted or overwritten.

- 877 request IDs have more than one successful raw response;
- raw file hashes differ because Tushare embeds a provider-generated response `request_id`;
- after excluding that response metadata, all 877 duplicate groups have identical returned `fields/items` data hashes;
- duplicates remain immutable and are excluded from canonical unique-request coverage counts.

## Contract-level structural status

| Contract | Status | Structural finding |
|---|---|---|
| C01 | **PASS WITH LIMITATIONS** | `601313.SH` is authoritatively resolved as historical 江南嘉捷, with same-security code change to `601360.SH` effective 2018-02-28. A versioned code-valid interval mapping is required downstream. |
| C03 | **PASS WITH LIMITATIONS** | 751/751 request coverage and valid schemas; 750 securities return observations. Provider vintage/revision limitations and unexplained missing sessions remain. |
| C04 | **FAIL** | No authoritative formal corporate-action/disclosure payload was acquired. Raw observations remain separate; no adjusted representation is authorized. |
| C05 | **FAIL** | No authoritative formal suspension/trading-status payload was acquired. Missing market rows therefore remain `UNKNOWN MISSINGNESS`. |
| C06 | **PASS WITH LIMITATIONS** | Official historical snapshots and PIT reconstruction are preserved; taxonomy/staleness and the `601313.SH` identifier issue remain explicit. |
| E02 | **PASS WITH LIMITATIONS** | 751/751 request coverage; E02-B still lacks historical available-time/vintage/revision qualification. |
| E03-A | **PASS WITH LIMITATIONS** | Benchmark history acquired with complete requested date envelope; provider-vintage limitations remain. |
| E03-B | **EXCLUDED** | Continues to block specific competing specifications only. |

## Stop reason

The frozen automatic-stop rule remains triggered by:

1. missing authoritative formal C04/C05 companion acquisitions.

These are acquisition-contract issues, not evidence that the strategy is infeasible. There are no unresolved universe identities after the authoritative `601313.SH → 601360.SH` mapping, but G3B-FULL cannot truthfully be frozen while C04/C05 remain failed under the current contract.

## Freeze eligibility

`NOT STRUCTURALLY ELIGIBLE FOR DATASET FREEZE UNDER THE CURRENT C04/C05 CONTRACT`

The researcher must either provide/authorize a qualified authoritative historical C04/C05 acquisition route or explicitly amend the completeness requirement while preserving raw-only analysis restrictions, `UNKNOWN MISSINGNESS`, and the prohibition on adjusted-series use. No such amendment is inferred here.

The machine-readable report remains quarantined under `data/qa_work/g3b_full/tushare/full_2013_2025_v1/structural_validation_report.json`.

The structural missing-session diagnostic identifies 49,568 candidate unexplained security-sessions across 425 securities. It uses benchmark sessions within C01 listing intervals minus observed C03 rows and does not infer suspension or impute observations.

`G3B STRUCTURAL RESOLUTION COMPLETE / AWAITING DATASET FREEZE DECISION`
