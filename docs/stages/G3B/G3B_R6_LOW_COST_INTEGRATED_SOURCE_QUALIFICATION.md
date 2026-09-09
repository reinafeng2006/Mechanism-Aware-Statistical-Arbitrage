# G3B-R6 — Low-Cost Integrated Source Qualification

Status: **ACCEPTED / FROZEN — JQDATA PROVISIONAL BEST LOW-COST INTEGRATED CANDIDATE**  
As-of date: **2026-09-09**  
Boundary: documentation/source-contract qualification only. No purchase, account/trial registration, credential use, formal data acquisition, empirical computation or source promotion occurred.

## Qualification standard

Candidates are evaluated as integrated architectures for C01/C03/C04/C05/E02/E03 over 2013–2025, with official C06 retained separately. `Potential` means a documented interface exists; it does not mean PIT-qualified.

Hard PIT qualification requires recoverable event-time availability, vintage/revision behavior, raw/adjusted lineage and reproducible immutable acquisition—not merely a date argument or an API that blocks future dates.

## Integrated comparison

| Candidate | C01 | C03 | C04 | C05 | E02 | E03 | PIT/vintage/revision | Integrations incl. C06 | Cost | Qualification |
|---|---|---|---|---|---|---|---|---:|---|---|
| **JoinQuant/JQData** | Date-aware security list; listing/end dates; code-history vintages unproven | 2005+ OHLCV/money; documented unadjusted mode | Factor/reference-date adjustment; original action and factor vintages unproven | Explicit daily `paused`; filled paused bars require controls | Volume/money plus share-capital candidates; effective-time fields need audit | Date-aware index constituents/weights; industry history documented | Strong future-data controls; historical revisions/source ancestry unproven | 2 if fully qualified; likely 3 with authoritative C04 | Quote/tier unresolved | **BEST LOW-COST INTEGRATED CANDIDATE — QUALIFIED WITH MATERIAL LIMITATIONS** |
| **Tushare Pro** | Current/basic listing data, not full versioned identity history | Broad SSE/SZSE daily API | Provider-produced `adj_factor`; no canonical action/vintage chain | Dated `suspend_d`, limited publication/source lineage | `daily_basic` shares/turnover | Index prices/weights and industry endpoints | Update times documented; historical first-available/revisions generally absent | 2–4 | Low/points dependent | **COMPETING LOW-COST PROGRAMMATIC — NOT HARD PIT-QUALIFIED AS SOLE PLATFORM** |
| **BaoStock** | Basic queries; robust versioned security history unproven | Unadjusted daily OHLCV/amount | Adjust flags, but no action/factor vintage lineage | `tradestatus` in daily history | Turnover; PIT denominators incomplete | Selected HS300/SZ50/ZZ500 constituents; no comprehensive historical weights | No demonstrated source vintages/correction history | At least 4 | Free | **C03/C05 FALLBACK — INSUFFICIENT CONSOLIDATION** |
| **AKShare-mediated** | Endpoint-specific only | Sina/Eastmoney paths | Source-specific only | Source-specific only | Source-specific | CSIndex/Sina paths | AKShare versioning cannot create upstream vintage or licence | Usually 4–7 | Free | **FALLBACK/CROSS-CHECK LAYER ONLY** |

All four can technically reach 2013-era daily prices or advertise sufficient price depth; only JQData publicly documents an integrated, date-aware architecture across most required contracts. None is hard PIT-qualified end to end.

## Priority 1 — JoinQuant/JQData

### C01 — PASS WITH LIMITATIONS

`get_all_securities(types=['stock'], date=...)` returns date-filtered securities with name, listing and end dates. It supports historical membership reconstruction better than a current-only snapshot. Stable entity identifiers, code/name change intervals, corrections and source vintages remain unproven.

### C03 — PASS WITH LIMITATIONS

Official documentation states daily history from 2005 and exposes OHLC, volume and money. `fq_ref_date=None` (`get_bars`) and `fq=None` (`get_price`) return unadjusted data. Data are available after close with later daily verification, which is useful timing documentation but not a historical vintage archive.

### C04 — PARTIAL / CANONICAL LINEAGE BLOCKED

Adjustment factors and reference-date transformations are documented. Original corporate-action records, historical factor versions, corrections/replacements and proof of what factor was available on each past date are not. `pre_close` may incorporate dividend/split adjustments and cannot be treated as an untouched raw close.

### C05 — PASS WITH LIMITATIONS

Daily `paused` is explicit. Documentation warns that unskipped paused observations may be filled with prior values, so `paused` must be retained and filled OHLC cannot be treated as actual trades. Reason, announcement and revision lineage remain unresolved.

### E02 — E02-A PASS WITH LIMITATIONS / E02-B UNRESOLVED

Volume and money support E02-A. Share-capital/valuation candidates may support E02-B, but units, denominator definitions, effective/publication times and historical revisions require authenticated field audit.

### E03 — PASS WITH LIMITATIONS

Date-aware index constituents/weights and industry-history APIs are documented. A date query and future guard do not establish announcement/effective/available timestamps, complete historical weight vintages or revision retention.

### JQData platform conclusion

JQData could reduce the architecture to **JQData + official C06**, with a possible third authoritative C04 source. It covers the target daily period and offers a local Python SDK/batch queries. Access tier, volume limits, storage/research licence, exact E02 fields, action lineage and revision/vintage behavior still require authenticated contract or bounded QA evidence.

## Priority 2 — Tushare

Tushare covers more named logical endpoints than Sina/BaoStock and is operationally inexpensive. It remains weaker than JQData for integrated semantics because C01 is snapshot-like, adjustment factors are current provider products, and index/action/status rows lack a complete historical available-time/vintage chain. It remains a strong fallback/competing acquisition branch, not a sole hard-PIT platform.

## Priority 3 — BaoStock

BaoStock materially duplicates C03 and adds `tradestatus` and turnover fields. It does not demonstrate integrated C01 history, canonical C04, E02 denominator vintages or comprehensive historical E03 weights. It therefore does not materially reduce source fragmentation.

## Priority 4 — AKShare source-specific map

| Underlying source | AKShare interface | Logical contract | Qualification boundary |
|---|---|---|---|
| Sina Finance | `stock_zh_a_daily` / Sina-labelled history | C03; limited E02-A | Inherits accepted Sina `FALLBACK ONLY`; AKShare adds no upstream vintage/SLA |
| Eastmoney | `stock_zh_a_hist` | C03 and displayed activity/turnover | Separate fallback candidate; raw/adjustment semantics, revisions and bulk stability need endpoint QA |
| China Securities Index | `index_stock_cons_csindex`, `index_stock_cons_weight_csindex` | E03 | Official underlying publisher, but documented endpoint does not establish historical announcement/effective/vintage archive |
| Sina Finance | `index_stock_cons_sina` | E03 latest constituents | Fallback only; not historical effective-time lineage |
| Sina Finance | `tool_trade_date_hist_sina` | Calendar support | Calendar aid only; range and source version must be preserved |

No audited AKShare path closes canonical C04 or complete historical E03 lineage. Endpoint count is irrelevant.

## Decision labels against retained shortlist

| Label | Candidate | Remaining blocker |
|---|---|---|
| **BEST LOW-COST INTEGRATED** | **JoinQuant/JQData — provisional** | Tier/quote, storage licence, C04 lineage, E02 semantics, revisions/vintages |
| **BEST PAID INTEGRATED** | **CSMAR — unchanged** | Authenticated modules/fields, PIT/vintage, export licence and quotation |
| **BEST GOVERNANCE** | **SSE/SZSE official products — unchanged** | Cost/source fragmentation and companion contracts |
| **FALLBACK** | **Tushare programmatic fallback; Sina/BaoStock/AKShare endpoint-specific cross-checks** | None qualifies as a single hard-PIT platform; explicit provenance required |

Choice/iFinD/Wind/RESSET retain their accepted prior status. This bounded reconsideration did not reopen their public discovery.

## Next decision

The researcher accepted the provisional JQData conclusion and authorized [G3B-R7](G3B_R7_JQDATA_AUTHENTICATED_QUALIFICATION_CONTRACT.md) as the only next source-qualification task. No purchase or acquisition is authorized. R7 cannot begin without legitimate researcher-controlled authenticated access.

`G3B-R6 ACCEPTED / FROZEN — R7 AUTHENTICATED ACCESS PENDING`

## Primary documentation

- JQData official usage/data-range documentation: <https://www.joinquant.com/help/api/doc?id=9875&name=JQDatadoc>
- JoinQuant security documentation: <https://www.joinquant.com/help/data/stock?f=home&m=footer>
- JoinQuant future-data restrictions: <https://www.joinquant.com/community/post/detailMobile?postId=23804>
- Tushare permission catalogue: <https://tushare.pro/document/1?doc_id=108>
- BaoStock package documentation: <https://pypi.org/project/baostock/>
- AKShare stock documentation: <https://akshare.akfamily.xyz/data/stock/stock.html>
- AKShare index documentation: <https://akshare.akfamily.xyz/data/index/index.html>
- AKShare source-naming convention: <https://akshare.akfamily.xyz/contributing.html>
