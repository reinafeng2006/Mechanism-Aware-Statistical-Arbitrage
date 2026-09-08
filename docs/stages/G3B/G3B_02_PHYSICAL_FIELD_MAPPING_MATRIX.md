# G3B-02 Candidate Physical-Field Mapping Matrix

Status: **AUDIT-ONLY / NON-EMPIRICAL**  
Purpose: map documented provider-native fields to frozen logical contracts without selecting a provider or redefining semantics.

| Contract | Candidate source | Documented physical fields | Logical mapping / semantics | Qualification limitation |
|---|---|---|---|---|
| C01 | Tushare `stock_basic` | `ts_code`, `symbol`, `name`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date` | Venue code, display name, venue/board, currency and listing state/dates | No stable internal entity/security ID, code-valid intervals, status-valid intervals or historical vintage/availability contract; `FALLBACK ONLY` |
| C02 | Tushare `trade_cal` | `exchange`, `cal_date`, `is_open`, `pretrade_date` | Venue, calendar date, trading-day flag and prior trading day | Special-session/correction vintage not documented |
| C03 | SSE authorized historical L1 | `SecurityID`, `DateTime`, `PreClosePx`, `OpenPx`, `HighPx`, `LowPx`, `LastPx`, `Volume`, `Amount` | Venue security key; observation time; raw pre-close/OHLC; volume and amount | Units, delivery availability, license and schema-version handling must be contracted; no inference that prices are adjusted |
| C03 | SZSE official L1 product class | security code/name, open, close, high, low, last, volume, value | Logical raw L1 market observation family | Public page is product-level; exact historical file names, units and version lineage require schema contract |
| C03 | Tushare `daily` | `ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `vol`, `amount` | Daily security/date, OHLC/pre-close, volume/amount | Unit definitions must be locked; delivery/vintage/revision policy not established; `FALLBACK ONLY` |
| C04 | Tushare adjustment/action candidates | provider action fields; `adj_factor` where contracted | Possible structured action/factor branch | Exact action terms, source-document ancestry, revision links, factor base and vintage must be proven before qualification |
| C05 | Tushare `suspend_d` | `ts_code`, `trade_date`, `suspend_timing`, `suspend_type` | Security/date, suspension timing/type | Full interval, reason/source record, public/available time and original vintage are incomplete |
| C06 | Tushare `stock_basic.industry` | `industry` | Current/basic industry label only | `NOT PIT-QUALIFIED` for historical membership; no taxonomy version/effective history |
| C07/E03 | Tushare `index_weight` | `index_code`, `con_code`, `trade_date`, `weight` | Index/member/date/weight candidate | `trade_date` must not be assumed to equal announcement/effective/available time; vintage unresolved |
| E01 | CNINFO portal records | document identity/title/date/time displayed by portal; exact API fields unresolved | Official disclosure-document candidate | Historical first-public timestamp, replacement chain, automated schema and complete universe coverage not established |
| E01 | Tushare statement/indicator schemas | `ts_code`, `ann_date`, `f_ann_date`, `end_date`, `report_type` where documented | Announcement/final-announcement/report-period/type candidates | These fields do not alone prove first-public/available timestamp, raw filing lineage or restatement history; not event-time qualified by name alone |
| E02 | C03 market records | `Volume`/`Amount` or `vol`/`amount` | Raw activity inputs | Does not identify M2; turnover needs PIT denominator |
| C08 | Internal manifest | `snapshot_id`, provider/source, dataset/endpoint, request parameters, retrieval time, source vintage semantics, schema version, checksum, counts/coverage, software version, license tag, retry/fallback log | Canonical acquisition and lineage metadata | Internal fields cannot manufacture absent upstream source availability/vintage |
| C09 | Same raw source as C01/C03/C04 | Same physical raw fields plus internal `outcome_zone_ingest_id` and access class | Later observations stored under outcome-only access | Must be reacquired/recorded under formal acquisition authorization and cannot be read by event-time feature paths |

## Required mapping rule

A later source contract must specify, field by field:

`physical field + provider dataset/version + unit + adjustment status + observation semantics + public/available/delivery semantics → logical field`.

Name similarity is insufficient. Unmapped required fields remain explicit gaps; they cannot be imputed from retrieval time or silently patched from fallback sources.
