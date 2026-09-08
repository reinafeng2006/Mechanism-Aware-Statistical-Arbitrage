# G3B Logical Field Necessity Register

Version: **v1.0-frozen-2026-09-08**  
Status: **APPROVED / FROZEN — G3B-02 AUDIT INPUT**

Necessity concerns contract coverage, not predictive value. Extra fields do not improve a provider's qualification.

| Contract | Logical fields | Necessity class | Reason |
|---|---|---|---|
| C01 | internal security ID, venue/code and valid dates, listing/delisting/status and valid dates | REQUIRED CORE | PIT universe and stable joins |
| C01 | internal entity ID, security type, currency | REQUIRED CORE | company lineage and scope/units |
| C01 | security name | ENHANCEMENT | human audit aid only |
| C01 | public/available time | LINEAGE / GOVERNANCE ONLY | PIT status provenance |
| C02 | venue, calendar date, trading-day flag, previous trading day | REQUIRED CORE | legal common market clock |
| C02 | session/status code | ENHANCEMENT | finer state context |
| C02 | available time | LINEAGE / GOVERNANCE ONLY | calendar vintage |
| C03 | security ID, venue, trade date, observation start/end | REQUIRED CORE | security/time key |
| C03 | raw close/previous close and units/currency | REQUIRED CORE | minimum response history |
| C03 | volume/amount and units | REQUIRED CORE | market observation; same-snapshot E02 |
| C03 | raw open/high/low | REQUIRED FOR COMPETING SPEC | path/magnitude alternatives |
| C03 | trading status | REQUIRED CORE | zero/missing interpretation |
| C03 | delivery/available-time semantics | LINEAGE / GOVERNANCE ONLY | event-time legality |
| C04 | security/action IDs, type, record/ex/effective dates, terms/units, status | REQUIRED CORE | action reconstruction |
| C04 | announcement/available time, source document, revision/cancellation link | LINEAGE / GOVERNANCE ONLY | PIT and revision control |
| C04 | factor value/effective date/vintage/base/formula version | REQUIRED FOR COMPETING SPEC | only for retained adjusted representations |
| C05 | security ID, state type/start/end, reason/source | REQUIRED CORE | eligibility/suspension history |
| C05 | intraday interval | ENHANCEMENT | finer clock only |
| C05 | public/available time | LINEAGE / GOVERNANCE ONLY | state provenance |
| C06 | classification ID/taxonomy version/member/valid dates | REQUIRED CORE | N0 and historical universe context |
| C06 | announcement/effective/available time and source vintage | LINEAGE / GOVERNANCE ONLY | membership PIT integrity |
| C07 | benchmark ID/member/valid dates/raw observation/weight | REQUIRED FOR COMPETING SPEC | E03/P0-EXP/RR-EXPOSURE |
| C07 | announcement/effective/available time and vintage | LINEAGE / GOVERNANCE ONLY | benchmark PIT integrity |
| C08 | source/dataset/request/retrieval/vintage/schema/checksum/software/license IDs | LINEAGE / GOVERNANCE ONLY | immutable ancestry |
| C08 | byte/row/time bounds, coverage/missingness, retry and fallback records | LINEAGE / GOVERNANCE ONLY | completeness/substitution audit |
| C09 | C01/C03/C04 raw fields observed after event origin | REQUIRED CORE | resolution validation without target definition |
| C09 | outcome-zone ingest ID/access classification | LINEAGE / GOVERNANCE ONLY | quarantine enforcement |
| E01 | security/entity, document ID/type/title/original, first-public time, revision link | ENHANCEMENT | R1; acquisition conditional on PIT qualification |
| E01 | retrieval/snapshot/schema provenance | LINEAGE / GOVERNANCE ONLY | audit/event eligibility |
| E02 | raw volume/amount | REQUIRED FOR COMPETING SPEC | MP1; same C03 snapshot |
| E02 | outstanding/free-float shares and effective/vintage time | REQUIRED FOR COMPETING SPEC | turnover denominator |
| E02 | quote/depth | ENHANCEMENT | richer liquidity only |
| E03 | benchmark identity/version/raw observations/member history/weights | REQUIRED FOR COMPETING SPEC | P0-EXP/RR-EXPOSURE |
| E03 | richer macro/industry exposures | ENHANCEMENT | optional context |
