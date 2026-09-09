# G3B-QA-R3 — Governance Companion Data Qualification

Status: **COMPANION CONTRACT AUDIT COMPLETE / AWAITING RESEARCHER REVIEW**  
Boundary: documentation/source-contract audit only; no full-history acquisition, provider bundle selection, adjusted series, measurements, targets or outcomes.

## Governing source architecture

`C01 canonical source may differ from C03 canonical source may differ from C04/C05 canonical sources`.

Contract-specific sources are permitted only with explicit physical-field mappings, units, timestamps, versions and provider lineage. Logical fields must never be silently mixed or patched. The accepted Sina C03 route remains `FALLBACK ONLY`; this audit does not reopen broad price-history discovery.

Qualification concerns source-contract fitness, not predictive quality. Public availability does not itself prove bulk-access permission, historical completeness, schema stability or PIT vintage integrity.

## Contract assessment

### C01 — Security Master / listing / delisting / identifier history

| Candidate | Exact candidate fields | PIT/history finding | Coverage / compatibility | Revision and reproducibility | Cost / burden | Qualification |
|---|---|---|---|---|---|---|
| SSE/SZSE official security lists, listing/termination notices and venue reference records | venue security code, name, security type/board, listing date, delisting/termination date, status/effective date; source document/publication time | Venue records are authoritative for events, but inspected public catalogues do not prove a single complete versioned code/status history or correction feed back to 2013. | Venue-complete in principle; `SH/SZ + six-digit code` can map to internal IDs, but code/name changes need interval reconstruction. | Dated notices can be checksum-preserved; structured master reconstruction and revision links require engineering and acceptance tests. | Public pages low direct cost; historical normalization/automation moderate to high; bulk-use terms unresolved. | **QUALIFIED WITH LIMITATIONS — leading canonical candidate class** |
| Tushare `stock_basic` | `ts_code,symbol,name,fullname,market,exchange,curr_type,list_status,list_date,delist_date` | Dates/status are documented, but the endpoint is a current/basic snapshot rather than a versioned historical security master. No first-public/available-time or correction vintage. | Broad A-share coverage; identifiers directly compatible with `.SH/.SZ`, but no stable entity ID or code-valid intervals. | Automatable snapshot capture; historical reproducibility only from project-retained snapshots. | Account/points dependent; low technical burden if credential exists. | **FALLBACK ONLY** |
| CSMAR/RESSET licensed history | Exact fields unresolved without authenticated dictionaries | Potentially integrated history, but entitlement and vintage semantics remain unverified. | Potentially broad. | Unknown. | Existing entitlement unverified; licence/cost unknown. | **UNRESOLVED** |

**C01 conclusion:** an official canonical path is defensible in principle but still needs a bounded field/history acceptance contract. Tushare cannot alone satisfy identifier-history PIT semantics.

### C04 — PIT Corporate Actions / adjustment lineage

| Candidate | Exact candidate fields | PIT/history finding | Coverage / compatibility | Revision and reproducibility | Cost / burden | Qualification |
|---|---|---|---|---|---|---|
| Exchange/company official disclosures (including CNINFO for issuer filings) | security/document ID, action type, announcement/publication time, record date, ex-date, payment/effective date, cash dividend, share/rights terms, status/replacement/correction link | Original dated disclosures provide the strongest positive PIT ancestry. Public documentation does not yet establish a stable structured bulk schema or complete replacement chain. | Broad issuer coverage in principle; document-to-C01 joins require security/document mapping. | Originals can be checksummed and append-only; extracting structured terms and linking corrections is high burden. | Mostly public viewing; lawful automation/bulk archive terms unresolved; high reconstruction burden. | **QUALIFIED WITH LIMITATIONS — leading canonical evidence class** |
| Venue market/reference records | ex-right/ex-dividend flags, reference-price/action fields where delivered, security/date/effective state | Authoritative operational semantics; historical delivery and publication/vintage fields remain product-contract dependent. | Venue-specific, requiring SSE/SZSE harmonization. | Potentially strong if authorized versioned files are retained. | Authorized historical products may be paid; not approved here. | **QUALIFIED WITH LIMITATIONS** |
| Tushare `adj_factor` and action/dividend candidates | `ts_code,trade_date,adj_factor`; action endpoints would require `ann_date,record_date,ex_date,pay_date` and cash/share terms where actually returned | `adj_factor` is self-produced by Tushare and updated on a current schedule. No historical factor-vintage archive, source-action ancestry, formula/base version or original availability chain is documented. | Broad advertised A-share history; identifier compatible. | API is automatable, but current values may be retrospectively revised unless every retrieval is retained. | At least 2000 points documented for `adj_factor`; credential currently not visible. | **FALLBACK ONLY for comparison; NOT QUALIFIED as canonical adjustment lineage** |

**C04 conclusion:** canonical adjustment requires original corporate-action records plus a versioned derivation. Neither Sina qfq/hfq nor Tushare `adj_factor` may be the sole canonical adjusted history.

### C05 — Suspension / trading status

| Candidate | Exact candidate fields | PIT/history finding | Coverage / compatibility | Revision and reproducibility | Cost / burden | Qualification |
|---|---|---|---|---|---|---|
| SSE/SZSE official stop/resume public records and trading-status files | security code, state/type, start/end or trade date, intraday interval where available, reason, announcement/source ID, publication/available time | Official public catalogues explicitly include stop/resume information; complete 2013–2025 historical schema, correction trail and bulk route remain unproven. | Venue-authoritative; must join through C01 and normalize venue semantics. | Dated files/notices can be immutable; public UI alone is not a deterministic historical feed. | Low public-view cost; moderate/high historical extraction; authorized files may carry access terms. | **QUALIFIED WITH LIMITATIONS — leading canonical candidate class** |
| Tushare `suspend_d` | `ts_code,trade_date,suspend_timing,suspend_type` (`S`/`R`) | Documentation says update is irregular and `trade_date` covers suspension dates. It does not provide reason/source ID, first-public time, original vintage or correction history. | Broad advertised A-share coverage; direct identifier compatibility. | Automatable if authorized; historical snapshot reproducibility must be created internally. | At least 2000 points; credential currently not visible. | **FALLBACK ONLY** |

**C05 conclusion:** Sina missing rows remain `UNKNOWN MISSINGNESS`. Only an explicit qualified C05 record may establish suspension/trading state.

### E02 — Share-capital / free-float denominator

| Candidate | Exact candidate fields | PIT/history finding | Coverage / compatibility | Revision and reproducibility | Cost / burden | Qualification |
|---|---|---|---|---|---|---|
| Official issuer/exchange capital-change disclosures | security/document ID, total shares, listed/circulating/free-float-relevant components where disclosed, effective date, publication/available time, correction/replacement | Strong PIT ancestry but heterogeneous documents and free-float semantics; no inspected unified historical structured contract. | Broad in principle, high mapping burden. | Original documents can be versioned; derived denominators require transparent definitions and transformations. | Low direct public cost, high extraction/maintenance burden. | **QUALIFIED WITH LIMITATIONS — canonical evidence candidate** |
| Tushare `daily_basic` | `ts_code,trade_date,turnover_rate,turnover_rate_f,total_share,float_share,free_share`; documented shares in ten-thousand-share units and turnover in percent | Daily fields and update window (15:00–17:00) are documented, but original source, historical correction vintage and true first-available timestamp per row are not. | Broad daily A-share coverage; maximum 6000 rows/request; direct identifiers. | Automatable snapshots; historical vintages not recoverable unless prospectively captured. | At least 2000 points; lower technical burden. | **FALLBACK ONLY / QUALIFIED WITH LIMITATIONS for non-canonical comparison** |
| Sina share-amount endpoint | dated share-amount response | Field/unit/effective/vintage semantics remain insufficiently self-describing. | Bounded selected names worked. | Immediate hashes reproducible only. | Low access burden, fragile undocumented endpoint. | **FALLBACK ONLY / NOT PIT-QUALIFIED denominator** |

**E02 conclusion:** raw C03 volume/amount remains usable independently. Float-normalized turnover remains constrained until an effective-time/vintage-qualified denominator is accepted.

### E03 — Historical benchmark constituents / weights / effective-time lineage

| Candidate | Exact candidate fields | PIT/history finding | Coverage / compatibility | Revision and reproducibility | Cost / burden | Qualification |
|---|---|---|---|---|---|---|
| Official index publisher (CSI and applicable venue/index publisher) | index code/version, constituent security code, weight, announcement/publication time, effective-from/to, adjustment type, source file/snapshot | Publisher announcements and dated constituent/weight artifacts are authoritative. The bounded documentation audit did not prove a complete machine-readable 2013–2025 archive with both announcement and effective timestamps. | Correct standard-index scope; joins to C01 required; taxonomy/version changes explicit. | Dated files can be checksummed; archive completeness, revised files and bulk-use terms require acceptance audit. | Public documents may be low cost; systematic historical assembly moderate; licensed feed may cost. | **QUALIFIED WITH LIMITATIONS — leading canonical candidate class** |
| Tushare `index_weight` + `index_basic` | `index_code,con_code,trade_date,weight`; index identity fields | Documentation describes monthly constituents/weights. `trade_date` must not be assumed to equal announcement, effective or available time; vintage/revision history is absent. | Broad standard-index catalogue; direct `.SH/.SZ` constituent identifiers. | Automatable but current historical table may be revised; project snapshots cannot reconstruct pre-retrieval availability. | 2000 points documented; credential currently not visible. | **FALLBACK ONLY** |
| Sina benchmark history | benchmark OHLCV/amount | Provides price history only. | Selected `sh000300` worked. | Immediate reproducibility passed; no constituent lineage. | Low. | **FALLBACK ONLY for benchmark prices; NOT QUALIFIED for constituents/weights** |

**E03 conclusion:** the official publisher is the leading canonical class, but a bounded archive/effective-time audit remains necessary before acquisition. Tushare can only provide an explicitly limited comparison branch unless announcement/effective lineage is independently supplied.

## Cross-contract access and automation result

| Source class | Direct project cost | Automation burden | Binding governance limitation |
|---|---:|---|---|
| Official exchange/company/index public documents | Usually no viewing fee; bulk/licensed terms unresolved | Moderate to high because histories are distributed across pages/files | Archive completeness, structured schema, corrections and lawful automation must be proven contract by contract |
| Venue/index authorized historical products | Potentially paid; no purchase authorized | Moderate once delivered | Exact quote/licence/schema/version required before use |
| Tushare | Account/points dependent; configured credential still not visible to this process | Low API burden | Aggregator provenance, absent source vintages and endpoint-specific point requirements; fallback only |
| CSMAR/RESSET | Unknown; institutional entitlement not verified | Potentially moderate | Cannot infer access, fields or PIT quality from institutional possibility |
| Sina | Low direct access burden | Low for bounded requests, fragile at scale | Undocumented mutable web endpoints; accepted C03 fallback only |

## Audit disposition and next bounded decisions

1. **C01:** retain exchange records as leading canonical candidate; authorize a later bounded historical identifier/listing schema test if desired.
2. **C04:** retain original official disclosures/venue action records as canonical evidence candidates; structured reconstruction and vintage rules remain unresolved.
3. **C05:** retain exchange trading-status records as leading canonical candidate; Tushare `suspend_d` remains fallback only.
4. **E02:** do not make denominator availability a condition for raw activity acquisition; separately audit official capital history or Tushare as a limited fallback.
5. **E03:** retain official index publisher as leading canonical candidate; require announcement/effective-time archive proof.

No final provider bundle is selected. In particular, a qualified source for one contract does not inherit qualification for another. No fallback may silently patch a canonical or Sina observation.

`G3B-QA-R3 COMPANION CONTRACT AUDIT COMPLETE / AWAITING RESEARCHER REVIEW`
