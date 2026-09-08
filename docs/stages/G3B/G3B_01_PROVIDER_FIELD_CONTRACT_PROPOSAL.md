# G3B-01 — Provider & Field Contract Proposal

Status: **APPROVED / FROZEN — 2026-09-08**  
Boundary: contract resolution only. No provider is selected, no credentials are used, no formal data are downloaded, and no empirical artifact is computed or inspected.

Priority: `PIT integrity + coverage + reproducibility + maintainability` before convenience or field richness.

## First-round scope interpretation

- Core contracts below cover the raw information needed by frozen `PRIMARY IMPLEMENTABLE CANDIDATE` branches.
- E02 Liquidity/Turnover and E03 Benchmark/Exposure are authorized for first-round co-acquisition consideration, not model use.
- E01 Announcements/Events is authorized for provider/schema/PIT audit; acquisition remains conditional on defensible historical first-public/available-time reconstruction and adequate coverage.
- `RESEARCH-ONLY` branches, including MP3/M3-DISC/U3/N2, remain outside the acquisition contract.

## Candidate source-contract rules

`Canonical Source + documented Fallback Source`

Canonical status is proposed per venue/data class, not per vendor bundle. A fallback row does not authorize use: missing canonical data must first remain missing. Any later substitution requires a reason code, field/date/security scope, source/version identity and downstream-visible provenance.

| Data class | Candidate canonical source(s) | Candidate fallback source(s) | Access/burden | Known PIT limitation | G2B dependencies |
|---|---|---|---|---|---|
| C01 Security identity/listing state | Venue-authorized SSE/SZSE security-reference/history products | Tushare `stock_basic`; licensed CSMAR/RESSET reference tables | Official products licensed/schema-specific; API moderate | Public API current rows do not prove complete historical code/status vintages | P0-RAW, GOV-MATCH, N0/N1, all joins |
| C02 Trading calendar | Venue/exchange official calendar | Tushare `trade_cal`; licensed database calendar | Low | Corrections/special sessions and historical publication vintage require audit | all market clocks, suspensions, outcome horizons |
| C03 Raw unadjusted market observations | SSE authorized historical L1 by venue; SZSE authorized market-data product by venue | Licensed CSMAR/RESSET market tables; Tushare `daily` | Official history licensed; vendor/API easier | Cross-venue schemas differ; API timestamps/revision policy not proven | P0-RAW, RR-DIST/CORR/SIGNED, N0/N1, abnormality, UR/MP0, outcomes |
| C04 Corporate actions / adjustment inputs | Official exchange/company disclosure/action records by venue | Tushare corporate-action/`adj_factor`; licensed databases | Reconstruction moderate/high | Effective date, announcement time and revisions must be linked; opaque adjusted series unacceptable as sole raw | adjusted-path candidates, relationship history, return construction later |
| C05 Suspension/eligibility state | Exchange trading-status/reference records | Tushare `suspend_d`; licensed databases | Low/moderate | API documentation shows dates/status but not complete original-vintage guarantee | universe eligibility, missingness interpretation, decision feasibility |
| C06 Historical industry membership | Versioned official/regulatory or approved classification history—provider unselected | Licensed CSMAR/RESSET/iFinD classifications; documented public records | Provider/history dependent | Current `industry` field is not historical membership | N0, P0-EXP, target universe context |
| C07 Benchmark/index history | Official index publisher membership/weights and index market data | Tushare `index_weight`/index prices; licensed databases | Low/moderate | Monthly/API snapshots may not equal effective-time membership vintage | P0-EXP, RR-EXPOSURE, optional conditioning |
| C08 Acquisition/PIT quality metadata | Internally generated immutable acquisition manifest | None; source-native logs are upstream inputs | Core engineering burden | Must be designed before any acquisition | R3, U0/U4, ROLE-UPD, every candidate |
| C09 Resolution-validation raw observations | Same canonical raw market/relationship source snapshots as C03/C01, stored in outcome zone | Same documented fallback policy as source class | Low marginal storage, strict access burden | Storage does not make observations event-time available | catch-up, reversal, persistence, continuation/break, horizon/magnitude validation |

## Logical field contracts

Provider-native names must map to these logical fields without changing semantics. `source_record_id`, `source_version`, `retrieval_time`, `snapshot_id`, `schema_version` and checksum/coverage metadata apply to every table.

### C01 — Security identity and PIT membership

Required: `internal_security_id`, `internal_entity_id`, `venue`, `venue_security_code`, `security_name`, `security_type`, `currency`, `code_valid_from`, `code_valid_to`, `listing_date`, `delisting_date`, `listing_status`, `status_valid_from`, `status_valid_to`, applicable `public_time`, `available_time`.

Candidate mapping evidence: Tushare documents `ts_code`, `symbol`, `name`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date`; these are fallback-schema candidates only and do not establish historical vintages.

### C02 — Calendar

Required: `venue`, `calendar_date`, `is_trading_day`, `previous_trading_day`, optional session/status code, `available_time` where historically reconstructable.

Candidate mapping: Tushare documents `exchange`, `cal_date`, `is_open`, `pretrade_date`.

### C03 — Raw unadjusted market observations

Required minimum capability: `internal_security_id`, `venue`, `observation_start`, `observation_end`, `trade_date`, `open_raw`, `high_raw`, `low_raw`, `close_raw`, `previous_close_raw`, `volume` plus unit, `turnover_amount` plus currency/unit, `trading_status`, `available_time`/delivery semantics.

SSE's published historical interface identifies `SecurityID`, `DateTime`, `PreClosePx`, `OpenPx`, `HighPx`, `LowPx`, `LastPx`, `Volume`, and `Amount`. Tushare's fallback candidate exposes `ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `vol`, and `amount`. Units and venue-specific definitions require schema audit.

Raw prices are canonical inputs. An adjusted-price product may only be stored as a derived or separately sourced comparison object with adjustment-factor vintage and formula lineage; it cannot replace recoverable raw prices plus corporate actions.

### C04 — Corporate actions / adjustment lineage

Required: `internal_security_id`, `action_id`, `action_type`, `announcement_time`, `record_date`, `ex_date`, `effective_date`, cash/share terms with units, status, cancellation/revision link, original source document ID, `available_time`. Any candidate adjustment series additionally requires `factor_value`, `factor_effective_date`, `factor_vintage`, base convention and reconstructable formula/version.

### C05 — Suspension/eligibility

Required: `internal_security_id`, `state_type`, `state_start`, `state_end`, intraday interval if supplied, reason/source record, `public_time`, `available_time`. Candidate fallback mapping includes `ts_code`, `trade_date`, `suspend_timing`, `suspend_type`.

### C06/C07 — Industry and benchmark membership

Required: `classification_or_index_id`, `taxonomy/version`, `member_security_id`, `membership_valid_from`, `membership_valid_to`, `announcement_time`, `effective_time`, weight where applicable, source vintage and `available_time`. A current `industry` label is insufficient. Tushare's `index_weight` candidate fields (`index_code`, `con_code`, `trade_date`, `weight`) require effective-time/vintage interpretation before use.

### C08 — Immutable acquisition manifest

Required: `snapshot_id`, source/provider, dataset/endpoint, request parameters, retrieval timestamp, source/vintage semantics, schema version, file/object checksum, byte and row count, min/max source time, security/field/date coverage, missingness summary, license/use tag, acquisition software version, success/failure/retry log and fallback substitution record.

### C09 — Outcome-zone raw observations

Use the same raw logical fields and canonical-source provenance as C01/C03/C04 where relevant, plus `outcome_zone_ingest_id` and access-control classification. Do not precompute or name labels. Event-time pipelines receive no read path to this zone.

## Proposed first-round enhancement candidates

Authorization status:

| Enhancement class | Candidate sources | Required fields / semantics | PIT/use boundary | Dependency |
|---|---|---|---|---|
| E01 Public announcements — `AUDIT AUTHORIZED / ACQUISITION CONDITIONAL ON PIT QUALIFICATION` | CNINFO/exchange disclosure portals as canonical candidates; Tushare/licensed archive fallback candidates | security/entity, document ID, title/type, original document, first-public timestamp, revision/replacement link, retrieval/snapshot metadata | If first-public/available time cannot be reconstructed, unsuitable for event-time R1; may remain descriptive/archive-only | R1, ROLE-RIVAL, possible UR2 context |
| E02 Accessible liquidity/turnover context — `CO-ACQUISITION CONSIDERATION AUTHORIZED` | Same C03 snapshot where volume/amount are native; float-share/reference source for turnover denominator | raw volume/amount, shares/outstanding or free float with effective/vintage time, quote/depth only as separately authorized enhancement | Volume/turnover never identifies M2; derived turnover inherits denominator vintage | MP1 |
| E03 Benchmark/exposure inputs — `CO-ACQUISITION CONSIDERATION AUTHORIZED` | Official index publisher; documented API/licensed fallback | index raw observations, member/weight effective history, benchmark identity/version | Exposure construction remains G2/statistical-deferred | P0-EXP, RR-EXPOSURE |

Fundamentals are not proposed for event-time use merely because a source exposes `ann_date`. A source must preserve first-public/available time and original/restated versions; otherwise it is `UNSUITABLE FOR EVENT-TIME USE` and may only be retained under a separately authorized descriptive/outcome role.

## Source-document evidence used for this proposal

- [SSE historical data product](https://www.sseinfo.com/services/assortment/historical/) and [SSE historical interface fields](https://www.sseinfo.com/services/assortment/market/hqywwd/wdzsjk/c/10800481/files/43b75567ae224148bd576acf11d30bd3.pdf)
- [SZSE official data services](https://www.szse.cn/English/services/dataServices/index.html)
- [CNINFO official disclosure platform](https://www.cninfo.com.cn/new/index.jsp)
- [Tushare stock basic](https://tushare.pro/document/1?doc_id=25), [daily market fields](https://tushare.pro/document/1?doc_id=27), [trading calendar](https://tushare.pro/document/2?doc_id=26), [suspensions](https://tushare.pro/document/2?doc_id=214), and [index weights](https://tushare.pro/document/2?doc_id=96)
- [CSMAR product scope](https://www.csmar.com/channels/31.html) and [RESSET database scope](https://www.resset.com/index/db/db.jsp)

Documentation establishes candidate capability, not PIT fitness or provider selection.

## Approved decisions

1. C01–C09 are formal audit targets; every logical field carries the necessity class in `registers/G3B_LOGICAL_FIELD_NECESSITY_REGISTER.md`.
2. E02/E03 receive co-acquisition consideration; E01 receives audit authorization with acquisition conditional on PIT qualification. None is authorized for model use.
3. Venue-authorized exchange data lead the canonical-source candidate class for C01/C03/C04/C05 where applicable; `leading canonical candidate class ≠ selected provider`.
4. Opaque or insufficiently traceable adjusted prices cannot be the sole canonical raw record.
5. Company/fundamental/event information without defensible historical `first_public_time`/`available_time` cannot enter event-time inference; retrieval time is not a substitute.
6. G3B-02 bounded qualification audit is authorized. Strict-necessity probes must be `AUDIT-ONLY / NON-EMPIRICAL`; formal acquisition and empirical computation remain prohibited.

G3B-01 approval does not select a source or authorize formal acquisition.
