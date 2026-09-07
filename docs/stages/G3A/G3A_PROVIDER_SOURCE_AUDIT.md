# G3A Provider / Source Audit

Status: **APPROVED / COMPLETE — FEASIBILITY ONLY**  
Date: 2026-09-07  
Boundary: feasibility only. **G3A evaluates feasibility, not desirability.** No provider is selected and no formal dataset or outcome was inspected.

| Source class | Lawful capability evidenced | PIT / vintage finding | Operational finding | Permitted conclusion |
|---|---|---|---|---|
| Exchange-authorized market data | SSE publishes licensed L1/L2 historical snapshots, daily/minute bars and tick trades; SZSE documents L1/L2 depth and tick trades/orders | Native timestamps plausible; corporate-action/security-master vintages still require schema inspection | L1/EOD broadly feasible; L2/tick licensed, costly and storage-heavy | Market-history core feasible; microstructure enhancement constrained |
| Official disclosure portals | CNINFO and exchange pages expose announcements and publication dates | First-public precision, amendments and machine-readable version lineage require endpoint audit | Lawful documents exist; full historical event coding is non-trivial | Event rejection feasible with limitations |
| Research databases | CSMAR and RESSET advertise market, company/fundamental, announcement and high-frequency families | Public pages do not establish field-level `available_time`, vintage or restatement guarantees | Broad but licensed and schema/contract dependent | Candidate source class; detailed PIT fitness unknown |
| General financial-data APIs | Tushare documents daily/minute/tick, fundamentals and announcements with access tiers | API availability does not prove original-vintage preservation | Programmatic access plausible; permissions/history vary | Useful candidate; PIT fields require audit |
| Professional terminals | iFinD advertises market, company, industry and macro information | Public material insufficient for historical-vintage semantics | Licensed; API/reconstruction rights require commercial audit | Candidate source class only |
| Official benchmark/index sources | Exchange/index publishers provide benchmark/index information | Membership/rebalance effective-time vintages must be retained | Generally cacheable/manageable | Plausible context source; representation remains G2-deferred |

## Sources consulted

- [SSE historical market data](https://www.sseinfo.com/services/assortment/historical/)
- [SSE Level-2](https://www.sseinfo.com/services/assortment/level2/)
- [SSE pricing](https://www.sseinfo.com/services/cpfwjg/)
- [SZSE data services](https://www.szse.cn/English/services/dataServices/index.html)
- [CNINFO](https://www.cninfo.com.cn/new/index)
- [SZSE company disclosures](https://www.szse.cn/www/disclosure/notice/company/index.html)
- [CSMAR](https://www.csmar.com/channels/31.html)
- [RESSET](https://www.resset.com/index/db/db.jsp)
- [Tushare market catalog](https://www.tushare.pro/document/1?doc_id=15)
- [Tushare access/coverage](https://tushare.pro/document/1?doc_id=290)
- [iFinD](https://download.10jqka.com.cn/free/iFinD/)

No sample data were downloaded. No endpoint response was admitted as empirical evidence.
