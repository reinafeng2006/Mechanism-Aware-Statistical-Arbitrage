# G3B-R4 — Paid / Institutional Source Value Comparison

Status: **ACCEPTED — EXTERNAL ACCESS / QUOTATION PENDING / NO PURCHASE AUTHORIZED**  
As-of date: **2026-09-09**  
Boundary: procurement evidence only. No purchase, subscription, account creation, licence acceptance, formal acquisition, measurement construction or outcome inspection occurred.

## Updated acquisition constraint

The researcher is willing to incur a **modest** data cost when it materially improves PIT integrity, lineage, coverage, reproducibility or operational reliability. Cost does not override the frozen source contract:

- `paid ≠ PIT-qualified`;
- `more fields ≠ greater contract value`;
- `acquisition breadth ≠ model-use authorization`;
- `NO NEW PAID DATA COMMITMENT WITHOUT SEPARATE RESEARCHER APPROVAL`.

Cost tiers below are decision labels, not numerical thresholds. A public price is reported only where the provider publishes it; otherwise the result is `QUOTE REQUIRED`.

## Reference baseline — current zero-cost Sina architecture

Sina remains `FALLBACK ONLY`. The bounded QA established operational access to raw-labelled daily OHLCV/amount for selected SSE/SZSE securities and a benchmark, but did not establish an authoritative source contract, historical vintages, SLA, complete security master, corporate-action lineage, suspension truth, float denominator or historical benchmark membership/weights.

Baseline contract coverage used for incremental comparison:

| Contract | Sina baseline |
|---|---|
| C01 | Not qualified |
| C03 | Fallback-only raw daily observations; governance/source-contract limitations |
| C04 | Not qualified for canonical action/adjustment lineage; qfq/hfq prohibited as sole canonical history |
| C05 | Not qualified; missing rows remain `UNKNOWN MISSINGNESS` |
| E02 | Volume/amount only; denominator lineage absent |
| E03 | Benchmark price history only; constituents/weights/effective-time lineage absent |

## Procurement comparison

| Option and relevant product | Official price / form | Venue scope | Incremental contract coverage relative to Sina | PIT, lineage and revision quality | Access / automation / licence | First-year tier | Qualification for this decision |
|---|---|---|---|---|---|---|---|
| **SSE Information — SSE Smart Historical Data, daily K-line** | RMB 10,000 per year-unit; official page also lists L1 RMB 30,000/year and L2 RMB 120,000/year. Any multi-year/member discount and final contract require confirmation. | SSE only; SZSE requires a separate product/contract. | Materially improves C03 source authority, field contract and delivery stability for SSE. Depending on exact delivered files, may help C01/C05/E02-A, but does **not** by itself prove complete C04, E02-B or E03-B. | Venue-authorized provenance is strongest of compared executable product classes. Exact historical correction/vintage retention and corporate-action semantics remain contract/schema questions. | Interface delivery is documented. Internal research/storage/redistribution rights must be confirmed in the executed licence. | **MATERIAL** for a multi-year SSE history; full A-share total remains **HIGH / QUOTE REQUIRED** because SZSE is separate. | **Strongest C03 canonical candidate class, not selected** |
| **SZSE / CNINFO authorized historical market product** | **QUOTE REQUIRED**; no current public official historical-package price was located in the bounded audit. | SZSE only; SSE separate. | Would close the venue half missing from an official C03 bundle and may improve C01/C05/E02-A depending on fields. C04 and E03-B still require explicit contracts. | Potentially venue-authorized and strong, but historical vintages, revisions and exact adjustment/status fields remain quote/schema dependent. | Login/application or commercial access; export/API, licence and maintenance terms require quote. | **HIGH / QUOTE REQUIRED** | **Potential C03 canonical companion, unresolved** |
| **CSMAR — China Stock Market Trading / related security, corporate-action and index databases** | **QUOTE REQUIRED**; institutional/annual database licence or trial/access arrangement. No official public project price verified. | Integrated SSE/SZSE A-share research coverage is advertised. | Potentially adds C01+C03 and parts/all of C04/C05/E02/E03 in one governed research database—largest possible breadth gain over Sina. Exact C04 PIT lineage, C05 semantics, E03 effective-time history and purchased modules must be field-audited. | Standardized research data and export/API/data-loader paths are documented. Historical availability timestamps, correction vintages and original-source ancestry are not proven by the public catalogue alone. | Web/export, data loader/API and some WRDS delivery documented. Institutional entitlement remains unverified; research-use/export limits require contract review. | **HIGH / QUOTE REQUIRED**; could be **LOW/MODEST to this project** only if an existing institutional entitlement is verified. | **Best integrated institutional candidate, not price-qualified or selected** |
| **RESSET — RESSET Financial Research Database / quantitative data services** | **QUOTE REQUIRED**; institutional/annual licence or trial. No official public project price verified. | Integrated China market research coverage is advertised; exact A-share modules/fields require authenticated dictionary. | Potentially improves C01/C03/C04/C05/E02/E03 breadth over Sina. Exact logical-field coverage and PIT/vintage support remain unresolved. | Research-oriented standardized database; public material does not establish historical first-available timestamps, revision vintages or all adjustment lineage. | Web/database/quant platform access is advertised; individual account terms restrict sharing and abnormal bulk downloading. API/batch and licence scope require quote. | **HIGH / QUOTE REQUIRED**; potentially **LOW/MODEST to project** under an existing university entitlement. | **Second integrated institutional candidate, unresolved** |
| **Tushare Pro — stock_basic, daily, daily_basic, adj_factor, suspend_d, index_basic/index_weight and related permissions** | Official interface permissions are points-based (several relevant endpoints document 2,000-point access and higher-frequency allowances at higher point levels); exact cash/annual first-year cost is **ACCOUNT/PERMISSION QUOTE REQUIRED** because points may arise through current platform rules rather than a fixed product price. | Broad SSE/SZSE A-share API coverage is advertised. | Improves automated C01 snapshot joins, C05 status coverage, E02 share/turnover fields and E03 constituent/weight availability relative to Sina; also supplies C03. Does **not** resolve authoritative C04 ancestry or historical availability/revision vintages, and `trade_date` cannot be presumed to be publication/available time. | Strong automation and reproducibility from retained project snapshots; weaker source/vintage lineage than venue or a demonstrably versioned institutional database. Adjustment factors are derived and cannot be canonical corporate-action truth. | API/batch burden low; endpoint row/rate/points limits apply. Terms and permitted research storage/use require account review. | **LOW / MODEST or QUOTE REQUIRED**, contingent on the actual points path and permissions; no cash amount inferred. | **Best low-burden companion/fallback candidate; not a sole canonical architecture** |
| **Current zero-cost bundle — Sina C03 fallback + official public C01/C04/C05/C06 documents + public index material** | No new data fee; engineering and maintenance cost remain material. | SSE/SZSE in principle, but assembled contract by contract. | Reference. Official documents improve governance companions but do not cure Sina C03 source-contract/vintage limitations or guarantee structured completeness. | Strong original-document ancestry where captured; weak unified schema, archive completeness and automated revision chain. | High reconstruction burden; public endpoint stability and lawful bulk terms must be checked per source. | **LOW direct cost / MATERIAL operational burden** | **Zero-cost fallback only** |

## Contract-by-contract gap resolution

Legend: `MATERIAL` = plausibly resolves a current Sina limitation if the product contract/schema confirms it; `PARTIAL` = improves coverage or operation but leaves a frozen lineage/PIT gap; `NONE/UNPROVEN` = no decision-relevant improvement established.

| Option | C01 | C03 | C04 | C05 | E02 | E03 | Main remaining limitation |
|---|---|---|---|---|---|---|---|
| SSE historical daily K | PARTIAL | **MATERIAL (SSE)** | UNPROVEN | PARTIAL | E02-A partial | E03-A possible | No SZSE; action/vintage/status/index-weight details require schema/contract |
| SZSE authorized product | PARTIAL | **MATERIAL (SZSE)** | UNPROVEN | PARTIAL | E02-A partial | E03-A possible | Quote and exact schema/licence unavailable |
| CSMAR | Potentially material | Potentially material | Partial-to-material, field audit required | Potentially material | Potentially material | Potentially material | Public catalogue does not prove purchased fields, PIT vintages or price |
| RESSET | Potentially material | Potentially material | Partial-to-material, field audit required | Potentially material | Potentially material | Potentially material | Same: entitlement, fields, PIT vintages and price unresolved |
| Tushare paid/permission | PARTIAL | PARTIAL | NONE for canonical lineage | PARTIAL | **MATERIAL operationally**, PIT caveat | PARTIAL | Aggregator/source-vintage and historical available-time limitations persist |
| Zero-cost reference | Limited official reconstruction | Sina fallback only | Document reconstruction | Document reconstruction | E02-A only | E03-A only | High maintenance; incomplete structured governance and vintage chain |

This matrix deliberately does not count extra fields. A cell is material only when it plausibly closes a frozen contract gap.

## Value conclusion

### Recommended — institutional integrated database, conditional quote/entitlement gate

Seek a written, module-specific quote or entitlement confirmation for **CSMAR first**, with **RESSET as a parallel substitute quote**, limited to the contracts C01/C03/C04/C05/E02/E03. The bounded access/quotation audit is recorded in [CSMAR / RESSET Access & Quotation Audit](G3B_R4_CSMAR_RESSET_ACCESS_QUOTATION_AUDIT.md). Proceed only if the accessible package is genuinely modest for this project and a bounded authenticated field/vintage audit confirms the required logical contracts.

Why: this is the only route in the comparison that may improve several companion contracts and both exchanges at once, while reducing manual reconstruction. It is not yet purchase-ready: price, entitlement, exact fields, first-available/vintage behavior, revision chain, export limits and research licence must be confirmed. If those fail, it loses the recommendation.

Exact remaining limitations: `QUOTE REQUIRED`; no verified entitlement; no authenticated field dictionary; PIT/vintage and correction ancestry unproven; module/export limits unknown.

### Second-best — modular official venue C03 + official governance companions

Use SSE and SZSE authorized historical raw daily products for C03, retain the frozen official C01/C04/C05/C06 and index-publisher companion architecture, and use Tushare only as an explicitly reason-coded fallback/operational comparison where allowed.

Why: it offers the strongest market-source provenance and avoids making an aggregator the canonical raw record. It is likely more expensive and still does not automatically solve corporate-action, float-denominator or historical constituent/vintage contracts. SSE and SZSE must be contracted separately; only SSE has a verified public daily-K price in this audit.

Exact remaining limitations: full A-share cost and SZSE quote unresolved; multi-year SSE cost is material; schema/vintage/correction/licence terms require contract review; companion reconstruction remains operationally heavy.

### Zero-cost fallback — preserve current architecture

Retain Sina as `FALLBACK ONLY` for C03, combine it with official public C01/C04/C05/C06 documents and public benchmark material, and keep E02-B/E03-B and adjusted representations constrained.

Exact remaining limitations: Sina is not canonical-qualified; no source SLA or historical vintage reproducibility; qfq/hfq prohibited as canonical adjusted history; missing rows remain `UNKNOWN MISSINGNESS`; security master/action/status/constituent histories require distributed reconstruction; maintenance and schema risk remain high.

### Tushare placement

Tushare is a useful **low-burden companion/fallback layer**, particularly for C01 snapshots, C05, E02 and E03 operational access. On currently verified documentation it is not the recommended sole canonical bundle because it does not cure the principal source-vintage, historical available-time and authoritative corporate-action-lineage gaps. A later bounded credentialed field test can qualify physical behavior, but QA success would still require researcher approval for any source promotion.

## Minimum purchase decision now required

No purchase is authorized. The next researcher decision should be one of:

1. authorize **quote/entitlement collection only** from CSMAR and RESSET for the named modules and frozen contract questionnaire;
2. authorize **official SSE/SZSE product quote collection only** for the exact historical daily and companion schemas; or
3. decline paid escalation and retain the zero-cost governance-limited branch.

The project should not choose between vendors until a quote and a bounded authenticated field/PIT contract audit are available. The MV-PIT formal source bundle therefore remains unresolved rather than silently selecting the easiest source.

Further CSMAR/RESSET qualification is now externally gated. See [G3B External Access Pending](G3B_EXTERNAL_ACCESS_PENDING.md). Public-source discovery is closed unless the external response exposes a specific contract ambiguity requiring bounded verification.

## Official-source register

- SSE Information product pricing: <https://www.sseinfo.com/services/cpfwjg/>
- SSE Information historical-data catalogue: <https://www.sseinfo.com/services/assortment/historical/>
- SZSE/CNINFO data-service portal: <https://webapi.cninfo.com.cn/module/index-series.html?act_menu=1&index_type=-1>
- CSMAR product catalogue: <https://www.csmar.com/channels/31.html>
- CSMAR delivery platforms: <https://www.csmar.com/en/channels/77.html>
- RESSET product catalogue and trial/contact route: <https://www.resset.com/>
- RESSET access/manual: <https://manual.resset.com/RESSETDB4.0.pdf>
- Tushare permission catalogue: <https://tushare.pro/document/1?doc_id=108>
- Tushare `daily_basic`: <https://tushare.pro/document/2?doc_id=32>
- Tushare `adj_factor`: <https://tushare.pro/document/2?doc_id=28>
- Tushare `suspend_d`: <https://tushare.pro/document/2?doc_id=214>

Public documentation was used only for procurement comparison. Where it did not establish price, licence, vintage or field semantics, this record deliberately says `QUOTE REQUIRED` or leaves the property unresolved.

`G3B-R4 SOURCE VALUE COMPARISON ACCEPTED / EXTERNAL ACCESS PENDING`
