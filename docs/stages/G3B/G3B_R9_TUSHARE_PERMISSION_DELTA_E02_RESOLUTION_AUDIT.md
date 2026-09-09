# G3B-R9 — Tushare Permission Delta / E02 Resolution Audit

Status: **OPTION A SELECTED / 2000+ POINT TIER CONFIRMED / PERMISSION RE-CHECK PASS**

Scope: permission and acquisition-architecture audit only. No purchase, acquisition resume, measurement construction, or outcome inspection was performed.

## 1. Authenticated permission evidence

The researcher subsequently confirmed an account-visible balance of 2,120 points, including 2,000 points purchased on 2026-09-09 and valid through 2027-09-09. The current status is `2000+ POINT TIER CONFIRMED`; no further purchase is required or authorized.

What is established directly:

- `daily` succeeded for eight sequential 2013–2025 security-history requests.
- `stock_basic` returned an authenticated effective limit of approximately one request/hour.
- `daily_basic` returned an authenticated effective limit of approximately one request/hour.
- The earlier one-request/minute planning assumption is superseded.

Official documentation currently states:

- `daily_basic` requires at least 2,000 points, returns at most 6,000 rows/request, and 5,000 points removes its ordinary total-volume limit;
- `stock_basic` requires 2,000 points and documents 50 requests/minute;
- the general current points table prices 2,000 points at RMB 200/year for an individual and describes 200 requests/minute plus 100,000 requests/day per qualifying API; 5,000 points costs RMB 500/year and provides 500 requests/minute with no ordinary-data total limit;
- actual authenticated account/endpoint behavior remains controlling.

Therefore the minimum documented upgrade candidate is **2,000 points / RMB 200 per individual year**, subject to confirming the account permission page and post-upgrade endpoint behavior before purchase. No purchase is authorized.

## 2. Request and duration implications

The current official C06 structural reconstruction contains 861 distinct securities in the PIT machinery-universe union. A 2013–2025 `daily_basic` history ordinarily fits inside the documented 6,000-row single-request limit, so the E02-B plan requires approximately 861 successful security-history calls, plus bounded retries and coverage validation.

- Current observed one/hour limit: theoretical minimum approximately **861 hours / 35.9 days** of continuous scheduling. This is not operationally useful for the one-time formal build.
- Documented 2,000-point rate: theoretical request-rate floor approximately **4.3 minutes** for 861 calls at 200/minute. Allowing transport, validation, retry/backoff and account-specific controls, practical completion should be planned as **tens of minutes to several hours**, not assumed from the headline rate alone.
- Documented 5,000-point rate: theoretical floor approximately 1.7 minutes, but this higher tier is not required unless authenticated post-upgrade evidence shows a separate operational constraint.

Other endpoints:

- `daily`: already completed eight sequential history calls and is not the observed blocker.
- `stock_basic`: needs only a small number of listing-status batches; one/hour is inconvenient but not a multi-week bottleneck. Official documentation separately requires 2,000 points.
- `index_daily`: E03-A needs only a small number of benchmark-history calls; prior QA observed a much less material endpoint throttle. It does not control the full acquisition duration.
- Official/current permissions for each endpoint must still be checked after any upgrade; a points-table headline is not a substitute for authenticated behavior.

## 3. E02 decomposition and G2B dependency impact

### E02-A — directly observed activity

`daily.vol` and `daily.amount` are already part of C03. They preserve the implementable raw market-activity/liquidity-context branch supporting MP1 as a competing candidate. They do not measure turnover or free-float-normalized activity.

### E02-B — denominator-dependent context

`daily_basic` supplies candidate `turnover_rate`, `turnover_rate_f`, `total_share`, `float_share`, and `free_share` fields. Its absence constrains turnover/free-float-normalized MP1 variants and related optional liquidity standardizations only.

Preserved boundaries:

`E02-B unavailable ≠ M2 unavailable`

`volume/amount context ≠ turnover/free-float context`

MP0 remains an excess-move diagnostic baseline; the E02-A MP1 branch remains implementable; MP2 stays optional enhancement; MP3 stays research-only/blocked. An upgrade would solve access/throughput for E02-B but would **not** establish historical PIT vintage or revision lineage for values queried today.

## 4. Exactly three acquisition alternatives

| Alternative | Cost / rate / time | Source count and contracts | Candidate impact | Qualification |
|---|---|---|---|---|
| **A — Upgrade Tushare** | Minimum documented candidate: 2,000 points, RMB 200/individual/year; headline 200/min and 100,000/day/API; about 4.3 minutes theoretical for 861 calls, practically tens of minutes to several hours after controls | No extra integration; keeps E02-A/E02-B with the primary platform and also removes the documented access mismatch for `stock_basic`; C04/C05/C06 companions remain | Preserves turnover/free-float-normalized MP1 competitors, but does not cure E02-B vintage/lineage limitations | Lowest-cost way to retain E02-B without fragmentation; requires permission-page confirmation and separate purchase approval |
| **B — Keep current Tushare + defer E02-B** | RMB 0; no E02-B wait | Zero additional source fragmentation; continue only C03/E02-A and other currently executable contracts after a separate resume decision | MP0 and M2 architecture remain; raw volume/amount MP1 remains; turnover/free-float-normalized MP1 variants and related enhancements become constrained | **Recommended lowest-complexity option preserving the primary architecture** |
| **C — Keep current Tushare + qualified E02 companion** | Public official disclosure route may have zero direct access price, but cost is unknown for normalized/bulk products; high extraction, mapping and maintenance burden | Adds at least one maintained integration. Candidate class: authoritative issuer/exchange share-capital and capital-change disclosures; any aggregator remains fallback-only unless separately qualified | Could support denominator lineage selectively; broad daily free-float/turnover coverage and historical available-time reconstruction remain limited | Higher governance burden and fragmentation; use only if E02-B becomes a required competing branch and A is rejected |

## 5. Recommendation and boundary

Recommend **B**. It has the lowest complexity, no new source integration, and preserves the primary M2 research architecture plus the implementable E02-A/MP1 branch. Choose A only if the researcher assigns sufficient design value to retaining turnover/free-float-normalized competing specifications; the modest fee buys operational access, not PIT-vintage quality. C is inferior at this stage because it adds a difficult integration without assured broad daily denominator coverage.

The bounded authenticated re-check subsequently passed two consecutive `stock_basic` and two consecutive `daily_basic` calls. C01/E02 are no longer permission-blocked. G3B-FULL remains safely paused but is resume eligible; resumption requires a new explicit researcher decision and must continue from the preserved checkpoint.

`TUSHARE 2000+ PERMISSION RE-CHECK — PASS / G3B-FULL RESUME ELIGIBLE`
