# CSMAR / RESSET Access & Quotation Audit

Status: **ACCEPTED — PUBLIC/NON-AUTHENTICATED DUE-DILIGENCE LIMIT REACHED / EXTERNAL ACCESS PENDING**  
As-of date: **2026-09-09**  
Scope: bounded commercial/access due diligence and source-contract qualification only.

No purchase, subscription, paid-term acceptance, account creation, credential entry, dataset download, formal acquisition, implementation or empirical inspection occurred.

## Access-state verification

| Provider | Official route inspected | Observed session state | Entitlement conclusion |
|---|---|---|---|
| CSMAR | `data.csmar.com` official platform and public product/delivery documentation | Official platform loaded with `登录` and `注册`; no authenticated institution/account context was present | **UNVERIFIED** — institutional branding or advertised university coverage is not evidence that this researcher has usable access |
| RESSET | `uni.resset.com`, public product pages and official DB4.0 access manual | Official platform loaded with `登录` and `注册`; no authenticated entitlement was present | **UNVERIFIED** — the manual states that university e-mail registration inherits only databases actually purchased by the institution |

The bounded check deliberately did not automate authentication or inspect credentials. Actual entitlement can be established only through the researcher's university account/library/VPN route or written provider confirmation.

## Minimum quotation / entitlement scope

The inquiry must be limited to the following logical contracts and must request module-level pricing before any full-database bundle:

| Contract | Minimum requested content | Qualification questions |
|---|---|---|
| C01 | A-share security master, listing/delisting, identifier/name/status history | Stable identifiers; effective dates; correction/version history; SSE+SZSE; delisted securities |
| C03 | Daily raw/unadjusted A-share OHLCV and amount | Start date; raw-price semantics; exchange coverage; suspended/non-trading representation; correction vintages |
| C04 | Corporate actions and adjustment lineage | Announcement/publication, record, ex/effective and payment dates; cash/share terms; replacement/correction chain; derivation formula/version for adjusted products |
| C05 | Suspension/resumption and trading-status history | Event/status semantics; publication/available time; intraday versus daily representation; historical corrections |
| E02 | Total/float/free-float share capital and turnover denominators | Units; effective and first-public dates; historical revisions; definition changes |
| E03 | Benchmark/index prices plus dated constituents and weights | Announcement, effective and available times; weight methodology/version; corrections; index universe |

Every response must also address API/Data Loader/batch export, row/export limits, programmatic reproducibility, research-use/storage licence, historical coverage, PIT/vintage support, restatement/revision history, trial/sample access, module pricing and whether the researcher's university already holds the relevant modules.

## Provider findings

### CSMAR

Relevant official product/database:

- China Stock Market Trading Database / Stock Market Series;
- security/fundamental company databases containing company profile, dividend/corporate-action and share-capital content;
- market-index and stock suspension/resumption content;
- web query/export, CSMAR Data Loader/DbSync/API and selected WRDS delivery routes.

Publicly established capabilities:

- the stock trading database documents a 1990 start and a research-use orientation;
- public material advertises SSE and SZSE listed-company/market coverage, including delisted securities in an institutional-market product description;
- public delivery documentation supports web access, export and Data Loader/API-style delivery;
- stock market coverage publicly lists stock trading, market index, suspension/resumption and related company-market content;
- some products can be selected/customized by module, theme or table.

Not established without an authenticated dictionary and written quote:

- exact C01/C03/C04/C05/E02/E03 physical tables and fields in the quoted package;
- whether raw/unadjusted prices and action records preserve original source lineage;
- historical `first_public_time` / `available_time` and row-level vintages;
- correction/restatement history and whether past extracts can be reproduced;
- row/export/API limits and storage/reuse rights;
- module-level and first-year project price;
- this researcher's university entitlement.

Commercial status: **QUOTE REQUIRED / INSTITUTIONAL ENTITLEMENT UNVERIFIED**.  
Official inquiry channel: `service@csmar.com`, hotline `400-639-8883`; public international channel `global@csmar.com`.

### RESSET

Relevant official product/database:

- RESSET Financial Research Database and related stock/index/company modules;
- web database/terminal and quantitative platform/API facilities, subject to the licensed package.

Publicly established capabilities:

- RESSET describes a research database for universities and institutions with stock and index market coverage;
- official account guidance says a verified university e-mail receives only the database permissions already purchased by that institution;
- trial/application channels exist;
- individual account terms shown publicly restrict account sharing and abnormal/bulk automated downloading.

Not established without authenticated access, an exact data dictionary and written quote:

- exact logical/physical coverage of C01/C03/C04/C05/E02/E03;
- raw/unadjusted price semantics and corporate-action derivation lineage;
- publication/available-time fields, historical vintages and revision chain;
- complete historical depth, delisted-security coverage and index constituent/weight effective-time history;
- supported batch/API/export routes for the purchased module and their limits;
- programmatic storage/reproducibility rights;
- module-level and first-year price;
- this researcher's university entitlement.

Commercial status: **QUOTE REQUIRED / INSTITUTIONAL ENTITLEMENT UNVERIFIED**.  
Official inquiry channel: `resset@resset.cn`, hotline `010-82601461`; official site offers trial/application routes requiring researcher and institution details.

## Minimal inquiry text for researcher/institutional procurement

The following text is prepared but was **not transmitted**:

> 本项目为高校研究用途，拟研究 2013 年以后沪深 A 股机械行业证券的点时（PIT）关系。请仅就下列最小模块确认本校现有授权及新增模块报价：证券主表及上市/退市/代码历史；沪深 A 股未复权日 OHLCV/成交额；公司行动及复权可追溯信息；停复牌/交易状态；总股本/流通股本/自由流通股本；指数行情、历史成分与权重。请分别说明历史起始日、退市证券覆盖、原始/调整字段语义、公告/首次公开/可用时间字段、历史 vintage 与修订链、API/Data Loader/批量导出方式和限制、研究存储许可、试用方式，以及模块级与整库首年报价。请勿增加无关模块。

Provider submission requires the researcher's name, university, institutional e-mail/phone and possibly proof of affiliation. Those details were not available and were not inferred or transmitted.

## Procurement comparison after inquiry audit

| Architecture | Expected project cost | C01/C03/C04/C05/E02/E03 coverage | PIT/vintage quality | Automation / reproducibility | Licensing | Maintenance | Remaining approximation gaps |
|---|---|---|---|---|---|---|---|
| **CSMAR scoped institutional package** | `QUOTE REQUIRED`; potentially LOW/MODEST only if existing entitlement covers the modules | Public catalogue suggests broad integrated coverage; exact purchased contract unresolved | Potentially stronger than Sina/Tushare, but row-level PIT/vintage is unverified | Web/export and Data Loader/API paths documented; exact limits unresolved | Institutional research licence required | Potentially moderate | Fields, vintages, correction ancestry, export/storage limits and price require written confirmation |
| **RESSET scoped institutional package** | `QUOTE REQUIRED`; potentially LOW/MODEST only with existing university access | Potentially integrated; exact contract coverage is less publicly verifiable | Unverified | Web/platform access documented; package API/batch limits unresolved | Institutional/user terms required | Potentially moderate | Same core gaps: fields, PIT/vintage, revisions, delisted/index history and quote |
| **SSE + SZSE official modular bundle** | SSE daily K publicly RMB 10,000 per year-unit; full multi-year SSE cost is material; SZSE and companion products `QUOTE REQUIRED` | Strongest C03 provenance by venue; companion coverage must be separately contracted | Potentially strongest source authority; exact delivered revision/vintage semantics still contractual | Interface delivery documented for SSE; cross-venue harmonization required | Separate venue contracts/licences | Moderate/high | Separate exchanges, multi-year cost, C04/E02-B/E03-B not automatically solved |
| **Sina/Tushare modular fallback** | Low direct cost / Tushare points-permission dependent | C03 operational fallback; Tushare can improve C01/C05/E02/E03 operations | Does not resolve authoritative source vintage, historical available time or canonical C04 lineage | Lowest API burden; reproducibility starts with project-retained snapshots | Aggregator terms apply | Low-to-moderate technical, higher governance burden | Sina non-canonical; unknown missingness; qfq/hfq not canonical; PIT/revision gaps persist |

## Value decision

No new evidence permits choosing or purchasing CSMAR or RESSET today because neither entitlement nor price has been verified. CSMAR remains the **preferred first quotation target** because its official public catalogue most directly maps to all six required contracts and documents Data Loader/API delivery. RESSET remains the **parallel/second quotation target**, particularly if the university already subscribes.

The lowest-cost integrity-improving architecture can be chosen only after one of the following produces evidence:

1. the researcher verifies university/library/VPN entitlement and provides only the non-secret entitlement/module result; or
2. the researcher submits the prepared inquiry through the official channel and supplies the written module quote/field response; or
3. the researcher authorizes transmission of specific identity/institution contact data in a separate action-time confirmation.

Until then, G3B-MV remains pre-acquisition and no source is promoted.

## Accepted stopping boundary

`Further CSMAR / RESSET qualification requires researcher-controlled institutional login, entitlement verification, or direct quotation and therefore cannot be resolved by further public-source audit.`

The exact permitted non-sensitive return fields and prohibited credential fields are controlled by [G3B External Access Pending](G3B_EXTERNAL_ACCESS_PENDING.md). No additional broad provider discovery is authorized while that record remains pending.

## Official-source register

- CSMAR platform: <https://data.csmar.com/>
- CSMAR database catalogue: <https://www.csmar.com/channels/31.html>
- CSMAR institutional financial data service: <https://www.csmar.com/channels/36.html>
- CSMAR delivery platforms: <https://www.csmar.com/en/channels/77.html>
- CSMAR Stock Market Trading Database guide: <https://file.csmar.com/group1/M00/AA/99/CuIKV2XAnKiABeLbAB4nDGC5Ano840.pdf>
- RESSET platform: <https://uni.resset.com/>
- RESSET product/contact portal: <https://www.resset.com/>
- RESSET DB4.0 access manual: <https://manual.resset.com/RESSETDB4.0.pdf>
- SSE official product pricing: <https://www.sseinfo.com/services/cpfwjg/>

`CSMAR / RESSET ACCESS & QUOTATION AUDIT ACCEPTED / EXTERNAL ACCESS PENDING`
