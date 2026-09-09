# G3B-R5 — Expanded Commercial-Grade Source Shortlist

Status: **ACCEPTED / FROZEN — PUBLIC DISCOVERY CLOSED / EXTERNAL QUALIFICATION PENDING**  
As-of date: **2026-09-09**  
Boundary: source qualification only. No purchase, subscription, trial application, credential entry, download, formal acquisition, empirical computation or source promotion occurred.

## Governing distinctions

- `commercial-grade source ≠ automatically PIT-qualified`;
- `programmable interface ≠ historical vintage lineage`;
- `trial availability ≠ authorized trial access`;
- `more fields ≠ greater contract value`;
- `stored data ≠ decision-time available data`.

The shortlist expands the externally gated due-diligence set. It does not alter the frozen hierarchy of official reference sources or existing fallback qualifications.

## Integrated-platform architecture objective

The governing acquisition preference is now:

`one primary integrated data platform + the minimum number of authoritative exceptions + documented fallbacks`.

Candidates are therefore compared first as integrated C01/C03/C04/C05/E02/E03 architectures. Consolidation is permitted only after hard PIT and lineage qualification. The official C06 historical classification path remains a separate authoritative exception.

| Platform | Integrated contract coverage indicated publicly | Hard qualification failures / unknowns | Cross-module PIT/vintage consistency | Additional sources still required | Expected production integrations | API/batch | Maintenance | Cost | Architecture class pending audit | Remaining authoritative exception |
|---|---|---|---|---:|---:|---|---|---|---|---|
| **iFinD** | Potential C01/C03/C04/C05/E02/E03 coverage in one interface | Raw/action/status semantics; historical available-time; correction vintage; full-history permission | Unproven | At least C06; possibly authoritative C04 lineage | 2 if fully qualified; 3+ if action/status exceptions needed | Strong HTTP/SDK | Low-to-moderate | `QUOTE REQUIRED` | Potential `ONE-PLATFORM + AUTHORITATIVE EXCEPTION` | C06; possibly original C04 records |
| **Choice** | Potential C01/C03/C04/C05/E02/E03 coverage | Exact functions/history; PIT/vintage; action lineage; API trial entitlement | Unproven | At least C06; others audit-dependent | 2 if fully qualified; unknown otherwise | Strong advertised Quant API | Low-to-moderate | `QUOTE REQUIRED` | Potential `ONE-PLATFORM + AUTHORITATIVE EXCEPTION` | C06; possibly original C04 records |
| **Wind** | Broad market/company/equity-event/index platform potentially spans all six | Exact A-share modules, raw semantics, PIT/revision lineage and quote | Unproven publicly | At least C06; contract audit may require original-action exception | 2 if qualified | Strong Client API/FTP/FileSync | Moderate | `QUOTE REQUIRED` | Potential `ONE-PLATFORM + AUTHORITATIVE EXCEPTION` | C06; possibly original C04 records |
| **CSMAR** | Public catalogue most directly indicates integrated coverage of all six | Authenticated fields; raw/action lineage; first-available/vintage; export limits | Potentially coherent but unverified | At least C06 | 2 if qualified | Data Loader/DbSync/API/export | Moderate | `QUOTE REQUIRED` | Best current institutional candidate for `ONE-PLATFORM + AUTHORITATIVE EXCEPTION` | C06 |
| **RESSET** | Potential integrated stock/index/company coverage | Exact modules/fields, PIT/vintage, revision chain, API/batch and quote | Unproven | At least C06; possibly other official companions | 2 if qualified; unknown otherwise | Package-dependent | Moderate | `QUOTE REQUIRED` | Potential `ONE-PLATFORM + AUTHORITATIVE EXCEPTION` | C06 |
| **SSE/SZSE official modular** | Strong C03, venue-specific C01/C05/E02-A; not one integrated cross-venue platform | Separate contracts; C04/E02-B/E03-B not automatically covered | Strong within delivered venue product, cross-source consistency must be engineered | C06 plus C04/E02-B/E03-B and cross-venue integration | At least 4–6 | Interface/product dependent | High | Material / quote required | `HIGHLY FRAGMENTED`, despite best C03 authority | C06 and multiple companion authorities |
| **Sina/Tushare fallback bundle** | Operational coverage across most contracts, with hard lineage limitations | Sina source contract/vintage; Tushare available-time/revision; canonical C04 | Not sufficient for a single PIT-consistent platform | C06 plus official C01/C04/C05 as needed | At least 4–6 | Easy | Moderate-to-high governance maintenance | Low | `HIGHLY FRAGMENTED` | C06 and official governance companions |

`Source Fragmentation` is now a first-class operational risk: more joins, calendars, identifiers, licences, schemas, outage paths, revision policies and fallback controls increase the chance of invisible inconsistency. It cannot override hard qualification.

## Candidate comparison against C01/C03/C04/C05/E02/E03

`Potential` means the public product description indicates relevant content but an authenticated field dictionary and bounded QA remain required. It is not a qualification result.

| Source | Exact product/module to qualify | C01 | C03 raw daily | C04 actions/adjustment | C05 status | E02 capital/turnover | E03 index history/membership | History / SSE+SZSE | PIT/vintage and revisions | Programmatic access | Trial | Cost | Current disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Tonghuashun iFinD** | iFinD Quant API: Basic Data, Date Series, Historical Quotation and relevant Topic Report indicators | Potential | Potential; raw/unadjusted indicator semantics must be verified | Potential; official FAQ describes forward-adjustment computation, but action ancestry/factor vintages are unproven | Potential | Potential; public catalogue includes share-capital and valuation/basic data | Potential; index indicators/constituents/weights require command-level confirmation | Official permissions: free/trial history generally recent 5 years; formal users securities-since-listing; SSE+SZSE supported | No public proof of row-level first-available time, correction vintage or reproducible past extracts | Official HTTP API plus Python, R, MATLAB, C++/C#/Java/VBA SDKs; Linux/Windows support | Trial application exists. Free account language indicates an iFinD account/product relationship; no anonymous API access | `QUOTE REQUIRED` | **PRIORITY BOUNDED QA CANDIDATE — access required** |
| **Eastmoney Choice** | Choice Quant API/Data Service: security/basic, historical quotation, corporate-action/capital, trading-state and index data functions | Potential | Potential | Potential | Potential | Potential | Potential | Official guide advertises Shanghai/Shenzhen/Beijing and multi-market coverage; exact historical depth unresolved | No public proof of PIT vintages, correction history or original adjustment lineage | Official Quant API supports Python/C++/C#/Java/R/MATLAB across Windows/Linux/Mac combinations | University edition advertises 15-day trial after identity verification, but official guide says free Quant API is not included automatically; API trial requires account-manager approval | `QUOTE REQUIRED` | **PRIORITY BOUNDED QA CANDIDATE — trial/API entitlement required** |
| **Wind** | Wind Financial Terminal + Wind Client API/Data Service; exact A-share market, corporate-event, capital and index modules to be quoted | Potential | Potential; official API advertises historical daily playback | Potential; official API advertises equity events/fundamentals, exact action lineage unverified | Potential | Potential | Potential | Broad China/global stocks and indices advertised; exact A-share/de-listed/history contract unresolved | No public evidence sufficient to certify historical available-time/vintage and restatement lineage | Client API supports Python/MATLAB/R/C++/C#/VBA; FTP/FileSync/API delivery also advertised | Official trial application exists | `QUOTE REQUIRED` | **COMMERCIAL GOVERNANCE CANDIDATE — lower QA priority than iFinD/Choice** |
| **CSMAR** | China Stock Market Trading Database / Stock Market Series plus security, action/share-capital, suspension and index modules | Potentially broad | Public guide documents 1990 start and daily stock files; raw semantics require authenticated confirmation | Potential | Public coverage explicitly includes suspension/resumption | Potential | Potential | Integrated SSE/SZSE research coverage advertised | PIT/vintage, corrections and first-available fields remain unverified | Web/export, Data Loader/DbSync/API and selected WRDS delivery | Trial/contact route | `QUOTE REQUIRED`; institutional entitlement may reduce project cost | **FIRST INSTITUTIONAL/QUOTATION CANDIDATE** |
| **RESSET** | RESSET Financial Research Database and licensed stock/index/company modules | Potential | Potential | Potential | Potential | Potential | Potential | China market research coverage advertised; exact depth/delisted coverage unresolved | PIT/vintage and revision chain unverified | Web/platform; exact package API/batch capability requires entitlement audit | Trial/application route | `QUOTE REQUIRED`; university entitlement possible | **SECOND INSTITUTIONAL/QUOTATION CANDIDATE** |
| **SSE/SZSE official** | Venue-authorized historical daily/raw and companion reference products | Venue-specific potential | **Authoritative reference/candidate** | Separate action/reference contract required | Separate status/reference contract required | E02-A possible; denominators separate | Price history possible; constituent/weight publisher contract separate | Full A-share requires both venues | Strongest source authority; delivered vintage/correction semantics still contractual | SSE documents interface delivery; SZSE capability/quote unresolved | Not established | SSE daily K RMB 10,000 per year-unit; SZSE/full bundle `QUOTE REQUIRED` | **BEST DATA-GOVERNANCE REFERENCE / HIGHER-COST ALTERNATIVE** |
| **Tushare** | `stock_basic`, `daily`, `adj_factor`, `suspend_d`, `daily_basic`, `index_basic/index_weight` | Partial | Operational API candidate | Not canonical lineage | Partial | Operationally useful | Partial | Broad SSE/SZSE advertised | Historical source vintages/available-time chain absent | Python/API; low automation burden | Account/points dependent | Points/permission; exact project cost unresolved | **LOW-COST PROGRAMMATIC FALLBACK/COMPANION** |
| **Sina** | Existing raw-labelled daily/benchmark endpoints | Not qualified | Bounded QA passed with limitations | Not qualified; qfq/hfq prohibited as canonical | Not qualified | Volume/amount only | Benchmark price only | Selected SSE/SZSE QA worked; universe history unproven | No historical vintage/source SLA | Simple HTTP endpoint but undocumented/mutable | Not applicable | Zero direct cost | **FALLBACK ONLY** |

## Contract-focused qualification questions for iFinD and Choice

Any researcher-controlled trial/API session must answer only the following, using a tiny deterministic `AUDIT-ONLY / NON-EMPIRICAL` slice:

| Contract | Physical capability to inspect | PIT/source-contract test |
|---|---|---|
| C01 | security code, exchange, name/code history, listing/delisting date/status | historical versus current snapshot; effective dates; delisted coverage; corrections |
| C03 | raw/unadjusted daily OHLCV/amount for one SSE and one SZSE security over a short fixed interval | raw-price flag/indicator definition; units; missing-session semantics; field/schema stability |
| C04 | cash/share corporate actions, record/ex/effective dates and adjustment factors | announcement/publication time; action-source ancestry; factor formula/base/version; retrospective revision behavior |
| C05 | suspension/resumption/trading state | event/status dates versus publication/available time; reason/source; missing-row distinction |
| E02 | total/float/free-float shares and turnover | units, denominator definition, effective/publication dates and historical revisions |
| E03 | index price plus dated constituents/weights | announcement/effective/available dates; weight version; constituent revision behavior |

Required artifact controls, if access is later supplied:

- no credentials in commands, output, logs, manifests or repository;
- fixed securities/date slice and exact field list;
- raw response immutability, request metadata, retrieval timestamp, schema version and checksum;
- explicit licence/account type and extraction-limit record;
- no pair calculation, measurement, target, outcome or PnL;
- trial QA success does not promote the source.

## Trial-access determination

### iFinD

An official free/limited interface tier and a trial application route are documented. However, access requires an iFinD account/token or approved trial, and public documentation says free/trial historical functions generally cover only the most recent five years. That is useful for schema QA but insufficient to prove the project's full historical requirement. No authorized credential was available in this environment, so no endpoint call was made.

Disposition: **BOUNDED QA AUTHORIZED IN PRINCIPLE / ACCESS PENDING**.

### Choice

Official materials advertise a programmable Quant API and a university-edition 15-day trial. They also state that university edition does not automatically provide a free Quant API; a responsible university contact or account manager must request API trial access. No authorized trial/API session was present, so no endpoint call was made.

Disposition: **BOUNDED QA AUTHORIZED IN PRINCIPLE / TRIAL API APPROVAL PENDING**.

## Final shortlist labels

### BEST VALUE — iFinD Quant API, conditional on quote and PIT QA

Rationale: the official API is directly automatable across HTTP/Python and several SDKs, covers both exchanges, publishes transparent extraction limits, and offers a low-friction path to a bounded trial/schema audit. It can become `BEST VALUE` only if the quote is modest and C01/C03/C04/C05/E02/E03 field/PIT tests pass. It is **not selected or PIT-qualified**.

Remaining gaps: full-history access requires formal permission; raw/action/status indicator semantics need authenticated command inspection; original-source ancestry, revision history and row-level available time are unproven.

Consolidation implication: potentially two maintained integrations—iFinD plus the preserved C06 exception—if all six contracts qualify; otherwise additional official action/status sources remain necessary.

### BEST DATA GOVERNANCE — SSE/SZSE official authorized bundle

Rationale: venue-authorized raw market records provide the strongest source authority. This remains a reference, not a purchase recommendation.

Remaining gaps: separate venue contracts; material/full-bundle cost; exact correction/vintage licence; C04/E02-B/E03-B require companion sources.

Consolidation implication: highest expected fragmentation and maintenance burden; superior C03 authority does not automatically make it the preferred total architecture.

### BEST LOW-COST PROGRAMMATIC — Tushare companion architecture

Rationale: lowest known API and maintenance burden across several contracts while preserving explicit fallback status.

Remaining gaps: aggregator provenance; historical available-time/vintage and revision chain; canonical corporate-action lineage. Tushare is a companion/fallback, not a sole canonical solution.

Consolidation implication: reduces API engineering for companion fields but cannot currently reduce authoritative-source count enough to qualify as the primary integrated platform.

### FALLBACK — Sina raw daily path

Rationale: bounded C03 operational QA has already passed with limitations and zero direct cost.

Remaining gaps: no canonical source contract, SLA or historical vintage reproducibility; unknown missingness; no C01/C04/C05/E02-B/E03-B completion.

## Other retained candidates

- **Choice** is the strongest second trial/API candidate and could displace iFinD on value only after an actual quote and bounded PIT/schema QA.
- **Wind** is a strong commercial interface candidate but remains `QUOTE REQUIRED`; public materials do not establish enough contract-level PIT detail to outrank the prioritized trial candidates.
- **CSMAR** remains the first institutional-entitlement/quotation candidate and may become best value if existing university modules are available.
- **RESSET** remains the second institutional-entitlement/quotation candidate.

## External-access handoff additions

For iFinD, Choice and Wind, the researcher may return only provider, access/trial status, product/module name, quoted price/term, accessible function/field names, history limits, API/export limits, PIT/vintage statements and licence restrictions. Do not return usernames, passwords, access/refresh tokens, personal contact information or account screenshots.

The subsequent procurement workflow is controlled by [Integrated Historical Research Platform Qualification](INTEGRATED_HISTORICAL_RESEARCH_PLATFORM_QUALIFICATION.md). No further qualification of CSMAR/iFinD/Choice may rely solely on public marketing where the unresolved fact requires authenticated fields, entitlement, trial access or quotation.

`EXPANDED PAID-SOURCE SHORTLIST ACCEPTED / EXTERNAL QUALIFICATION REQUIRED`

## Official-source register

- iFinD Quant API: <https://quantapi.51ifind.com/gwstatic/static/ds_web/quantapi-web/>
- iFinD permission/history limits: <https://quantapi.51ifind.com/gwstatic/static/ds_web/quantapi-web/help-center/permission.html>
- iFinD SDK/HTTP/trial page: <https://quantapi.51ifind.com/gwstatic/static/ds_web/quantapi-web/download.html>
- iFinD FAQ: <https://quantapi.51ifind.com/gwstatic/static/ds_web/quantapi-web/help-center/faq.html>
- Choice user guide / Quant API description: <https://choice.eastmoney.com/choicewebfile/UserGuide.pdf>
- Choice university-edition guide: <https://choice.eastmoney.com/FileDownLoad/GXSC.pdf>
- Wind Financial Terminal: <https://www.wind.com.cn/portal/zh/WFT/index.html>
- Wind Client API: <https://www.wind.com.cn/portal/zh/ClientApi/index.html>
- CSMAR: <https://www.csmar.com/channels/31.html>
- RESSET: <https://www.resset.com/>
- SSE official product pricing: <https://www.sseinfo.com/services/cpfwjg/>
