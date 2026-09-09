# G3B — Tushare Final Acquisition Readiness Checkpoint

Status: **APPROVED / FROZEN**
Formal acquisition: **G3B-FULL AUTHORIZED**
Platform status: **TUSHARE PRIMARY INTEGRATED HISTORICAL PLATFORM — CURRENTLY QUALIFIED PATHS ONLY**

## 1. Accepted R8 contract status

| Contract | Accepted status | Preserved limitation |
|---|---|---|
| C01 Security Master | `PASS WITH LIMITATIONS` | One join/field path was demonstrated; full historical identifier vintages and cross-exchange repetition remain unproven. |
| C03 Daily Market Observations | `PASS WITH LIMITATIONS` | Raw/unadjusted SSE/SZSE coverage was demonstrated at both date boundaries; provider vintage, repeated retrieval and missing-session attribution remain limited. |
| C05 Suspension / Trading Status | `FAIL AT CURRENT TUSHARE PERMISSION` | Tushare `suspend_d` is not available at the current permission. This does not require a Tushare upgrade because an official companion architecture is assessed below. |
| E02 Liquidity / Share Capital | `PASS WITH LIMITATIONS` | Direct volume/amount work; denominator fields are accessible but rate-limited and not historically PIT-vintaged. |
| E03 Benchmark / Constituents / Weights | `PASS WITH LIMITATIONS` | E03-A works; E03-B is unavailable at the current permission. |

`Tushare QA success ≠ canonical approval`.

## 2. Bounded official C05 closure

Official evidence inspected:

- SSE's official public-data catalogue lists daily suspension/resumption information, intraday suspensions and the market calendar: <https://www.sse.com.cn/market/publicdata/>.
- SSE exposes an official suspension/resumption query with security, stop/resume time, duration and reason: <https://www.sse.com.cn/disclosure/dealinstruc/suspension/>.
- SZSE exposes an official dated suspension/resumption notice archive with keyword/date search: <https://www.szse.cn/disclosure/notice/temp/index.html>.

These venue records are authoritative positive-event evidence. The public interfaces inspected do not by themselves establish a complete, stable, bulk-machine-readable 2013–2025 historical state stream or revision/vintage API. C05 therefore closes only as:

`QUALIFIED WITH DOCUMENTED LIMITATIONS — AUTHORITATIVE OFFICIAL COMPANION`

### State-resolution contract

| Available PIT evidence | Permitted state |
|---|---|
| Canonical C03 observation exists for an eligible security/session | `NORMAL TRADING OBSERVED` |
| Dated venue-authoritative suspension record is available | `SUSPENSION` for the explicitly supported interval/date |
| Dated venue-authoritative resumption record is available | `RESUMPTION` from the explicitly supported time/date |
| C03 observation is absent and no qualified C05 record explains it | `UNKNOWN MISSINGNESS` |
| Source outage, unresolved identifier, or uncovered historical interval | `UNKNOWN MISSINGNESS` plus reason/provenance code |

`missing market observation ≠ suspension`.

Official SSE and SZSE records must remain source-specific, timestamped, checksummed and linked through C01 identifiers. Absence from an official search result is not positive evidence of normal trading. Historical archive gaps remain explicit; no silent Tushare or AKShare patch is permitted.

## 3. E03 decomposition

- **E03-A — Benchmark price/return history:** available through the current Tushare `index_daily` path; `PASS WITH LIMITATIONS` because provider vintage/revision guarantees remain incomplete.
- **E03-B — Historical constituents/weights:** unavailable at the current permission; classification is `BLOCKS SPECIFIC COMPETING SPECIFICATIONS ONLY`.

E03-B does not block simple benchmark-price/return conditioning and does not justify an access purchase now. It may re-enter only if a surviving frozen candidate explicitly requires dated constituent/weight lineage.

## 4. Metadata-only acquisition-throughput estimate

Let `N` be the deduplicated number of securities ever entering the frozen C06 machinery universe over 2013-01-07 through 2025-12-31. `N` is not fabricated before the formal C06 universe build.

The efficient query plan is security-history based because Tushare documents a 6,000-row maximum for `daily` and `daily_basic`; roughly 13 years of daily observations fit within one request per security under ordinary A-share calendars.

| Endpoint/object | Planned request count | Basis |
|---|---:|---|
| `stock_basic` | approximately 3 | batch by listing status rather than security |
| `daily` C03 | `N` | one 2013–2025 history request per security; split only on actual row-limit failure |
| `daily_basic` E02 | `N` | one history request per security; split only on actual row-limit failure |
| `index_daily` E03-A | approximately 1 per authorized benchmark | complete daily benchmark history fits the documented limit |
| manifests/retries | `ceil(0.05 × (2N+4))` planning reserve | operational reserve, not an assumption that 5% will fail |

Expected initial request envelope:

`R_initial ≈ 2N + 4 + retry reserve`.

Illustrative operational planning only: if the PIT union contains 500–1,000 securities, the initial pull is approximately 1,054–2,104 requests including the reserve. This range is not a frozen universe-size estimate.

### Limits and duration

- The authenticated QA observed effective one-call-per-minute limits on `stock_basic`, `daily_basic` and `index_daily`, while `daily` completed more freely. The slowest authorized endpoint therefore controls current-tier elapsed time.
- At the observed `daily_basic` rate, the E02 portion alone requires approximately `N` minutes: about 8.3–16.7 hours for the illustrative 500–1,000-security planning range, before conservative retries and scheduled pauses.
- Tushare's current official permission table states that 120 points provide 50 requests/minute and 8,000 daily requests but only unadjusted daily data; 2,000 points provide 200 requests/minute and 100,000 requests per API for interfaces meeting their point requirement, priced at RMB 200/year; 5,000 points provide 500 requests/minute and no ordinary-data total limit, priced at RMB 500/year. Actual account/interface entitlements remain controlling.
- The observed account behavior is more restrictive than the headline table for several endpoints, so planning must use observed effective limits until a permission entitlement page or subsequent QA proves otherwise.

### Retry/backoff contract

- endpoint-specific token bucket; no concurrent burst against one-call-per-minute interfaces;
- retry only explicit rate-limit/temporary transport failures, never permission failures;
- exponential backoff with bounded jitter and maximum attempts;
- immutable failed-attempt log and resume cursor;
- idempotent request IDs and checksum comparison;
- stop on schema/field changes, repeated inconsistent payloads or unexplained coverage loss.

### Initial versus incremental cost

Incremental refresh is materially cheaper. A date-based refresh can request all securities for one trade date for C03 and E02, plus authorized benchmarks, yielding approximately 2–3 ordinary requests per completed session before retries, subject to row limits. C01 refresh is occasional; official C05 records are event-driven; C06 follows official release cadence.

### Operational conclusion

`CURRENT TIER SUFFICIENT BUT SLOW`.

The present tier is capable of the core initial pull using scheduled, restartable acquisition; its throughput is inconvenient rather than construct-invalidating. No upgrade is justified before a bounded formal acquisition demonstrates that observed one-call-per-minute limits materially prevent completion. If that trigger occurs, the minimum documented candidate is the 2,000-point tier at the currently published personal price of RMB 200/year, but access to each required endpoint must be rechecked before purchase. No purchase is authorized.

## 5. Exact remaining limitations

1. C01 lacks complete historical identifier/version ancestry; unresolved mappings must be quarantined.
2. C03 lacks provider historical-vintage/revision guarantees and cannot explain missing rows alone.
3. C04 still requires authoritative action records and a versioned action-to-adjustment transformation; `adj_factor` is insufficient.
4. C05 official public records are authoritative positive evidence but complete 2013–2025 bulk/archive/revision coverage is not proven; uncovered cases remain `UNKNOWN MISSINGNESS`.
5. E02-B denominator values remain current-produced historical queries without source-vintage proof.
6. E03-B is unavailable and blocks only dependent competing specifications.
7. Current-tier initial acquisition is slow and must use rate-aware resumable scheduling.
8. Tushare remains a proposed primary platform, not canonical-approved, until the final acquisition contract is approved.

## 6. Proposed source bundle

`Tushare proposed primary: C01 + C03 + E02-A + constrained E02-B + E03-A`

`+ official C04 corporate-action companion`

`+ official SSE/SZSE C05 positive-event companion`

`+ official C06 historical industry-classification exception`

`+ source-specific AKShare fallback/cross-check interfaces only, with underlying-source provenance`

E03-B is excluded from the minimum bundle unless a surviving specification dependency is activated. No fallback silently patches a canonical/primary gap.

## 7. Minimum researcher decisions before formal acquisition

Only two decisions remain:

1. **Approve or reject the proposed source-contract status:** authorize Tushare as the primary historical acquisition source subject to every limitation above, with official C04/C05/C06 companions and source-specific fallbacks. This would be acquisition authorization, not evidence that Tushare is perfectly PIT-vintaged.
2. **Approve the current-tier execution choice:** accept `CURRENT TIER SUFFICIENT BUT SLOW` for the first acquisition, with no permission purchase; or separately authorize investigation/purchase of the minimum 2,000-point tier only after endpoint entitlement is reconfirmed.

No choice of model, factor, measurement, target, relationship or trading rule is included.

Researcher decisions recorded:

- the current permission tier is accepted as `OPERATIONALLY SUFFICIENT BUT SLOW`;
- `NO NEW PURCHASE / PERMISSION UPGRADE AT THIS STAGE`;
- E03-B remains excluded unless separately authorized;
- formal acquisition is limited to C01/C03/C04/C05/C06/E02/E03-A and the frozen 34+35 PIT universe/date zones;
- measurement computation and empirical outcome inspection remain prohibited.

`G3B TUSHARE FINAL ACQUISITION READINESS CHECKPOINT — APPROVED / FROZEN`
