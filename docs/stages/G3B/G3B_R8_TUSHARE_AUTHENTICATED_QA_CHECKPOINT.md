# G3B-R8 — Tushare Authenticated Integrated-Platform QA Checkpoint

Status: **ACCEPTED / COMPLETE**
Evidence class: **AUDIT/QA — NON-EMPIRICAL**
Formal acquisition: **NOT AUTHORIZED**
Source promotion: **NOT AUTHORIZED**

## Scope and credential boundary

The deterministic QA exercised only C01, C03, C05, E02 and E03 endpoints. C04 was not queried. The credential was read only from the process environment for authenticated transport and was not printed, logged, persisted, hashed or committed. Raw responses and the manifest are under the Git-ignored path `data/raw/g3b_qa/tushare_integrated_qa_r8_v1/`.

The run issued 28 bounded requests: 11 succeeded, 17 returned explicit API permission/rate-limit responses, and none failed at the transport layer. Checksums establish immutability of this retrieval; they do not establish historical-vintage reproducibility.

## Contract results

| Contract | Result | Authenticated observation | Qualification implication |
|---|---|---|---|
| C01 Security Master | **PASS WITH LIMITATIONS** | One successful `stock_basic` response returned a deterministic SZSE identifier and listing/status fields, including `list_date` and `delist_date`; later SSE/SZSE probes hit the observed one-call-per-minute limit. | The field contract and one join path are functionally demonstrated, but cross-exchange repetition, a fully versioned historical identifier master and historical response vintages are not established. **Possible primary-candidate component subject to approval; not canonical-approved.** |
| C03 Daily Market Observations | **PASS WITH LIMITATIONS** | `daily` returned both SSE and SZSE early-2013 and late-2025 slices with `open/high/low/close/pre_close/change/pct_chg/vol/amount`. The endpoint labels this as unadjusted daily observations; no adjusted product was used. | Functionally supports the bounded raw/unadjusted daily field contract, but source/version vintage guarantees, repeated-retrieval stability and missing-session attribution remain limited. **Possible primary-candidate component subject to approval.** |
| C05 Suspension / Trading Status | **FAIL AT CURRENT PERMISSION** | Every `suspend_d` request returned an explicit no-interface-permission response. | Tushare at the currently available permission cannot establish suspension status or distinguish suspension from missing/source failure. A separately qualified official/companion C05 path remains required. |
| E02 Liquidity / Share Capital | **PASS WITH LIMITATIONS** | `daily` supplied directly observed `vol/amount`. One `daily_basic` request returned turnover and total/float/free-share fields; subsequent requests hit the observed one-call-per-minute limit. | E02-A is functionally supported. E02-B is queryable but operationally constrained and the QA does not establish historical PIT vintages for denominator values. **Possible primary-candidate component with explicit PIT/throughput gap.** |
| E03 Benchmark / Constituents / Weights | **PASS WITH LIMITATIONS** | `index_daily` returned benchmark history. Every `index_weight` request returned an explicit no-interface-permission response. | E03-A is supported. E03-B is not supported at the current permission and needs an additional qualified source or separately approved permission escalation. |

## Field and timing findings

- Identifier joins use the same `ts_code` convention across successful security, equity-daily and daily-basic responses for the tested SSE/SZSE slice.
- C03 contains date-labelled daily records, not publication/vintage histories. Retrieval today does not prove what a historical API response would have contained at the original decision time.
- `daily_basic` exposes denominator-dependent fields, but historical queryability today is not itself PIT-vintage qualification.
- `index_weight.trade_date` is not proven to equal announcement, effective or first-available time; the endpoint was inaccessible at the current permission in any case.
- An absent daily row remains `UNKNOWN MISSINGNESS` without separately qualified C05 evidence.
- No C04 inference is permitted. In particular, availability of any Tushare adjustment product elsewhere would not establish PIT corporate-action lineage.

## Reproducibility and operational limits

The run preserved sanitized request parameters, response schemas, row counts, raw-response checksums and retrieval timestamps. Immediate endpoint repetition was materially constrained by observed one-call-per-minute limits on `stock_basic`, `daily_basic` and `index_daily`. Therefore:

- deterministic request construction: **PASS**;
- immutable response capture and checksum lineage: **PASS**;
- repeated identical retrieval under the current run: **UNRESOLVED / RATE-LIMITED**;
- historical-vintage reproducibility: **UNRESOLVED**;
- bounded batch feasibility at this tier: **PASS WITH MATERIAL THROUGHPUT LIMITATIONS**.

These findings satisfy the rule that a higher permission may be considered only because the lower tier is functionally useful yet operationally or contractually limited. They do not authorize a higher-tier purchase.

## Proposed minimum-source architecture

The bounded evidence supports the following proposal, not an approval:

`Tushare candidate for C01 + C03 + E02-A/E02-B-limited + E03-A`

`+ separately qualified official/authoritative C04 exception`

`+ separately qualified C05 companion source`

`+ official C06 authoritative exception`

`+ separately qualified E03-B source if a surviving specification requires constituents/weights`

`+ AKShare source-specific fallback/cross-check only, with underlying-source provenance`

Minimum additional production integrations beyond Tushare and official C06 are: one C04 action/adjustment-lineage path and one C05 trading-status path; these may be the same integrated authoritative companion only if separately qualified. E03-B is conditional on surviving specification need.

## Exact remaining C04 gap

No current R8 evidence establishes a versioned, PIT-reconstructable chain from corporate-action announcement/public availability through effective action terms to an authorized adjusted representation. Raw/unadjusted C03 observations may be acquired under a later authorization, but adjusted specifications remain constrained until C04 preserves action identity, announcement/public/available/effective times, terms, revisions and transformation methodology/version. `adj_factor` availability alone cannot close this gap.

## Governance conclusion

`Tushare QA success ≠ automatic canonical approval`.

Tushare is recorded as **PROPOSED PRIMARY INTEGRATED HISTORICAL PLATFORM — SUBJECT TO FINAL ACQUISITION CONTRACT**, with all companion-contract and PIT-vintage limitations preserved. This is not canonical approval. No formal data acquisition, permission purchase, measurement computation or outcome inspection occurred.

`G3B-R8 BOUNDED AUTHENTICATED QA ACCEPTED / COMPLETE`
