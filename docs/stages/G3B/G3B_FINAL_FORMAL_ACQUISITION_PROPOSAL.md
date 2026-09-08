# Final Formal Acquisition Proposal

Status: **APPROVED / FROZEN — G3B-QA ONLY AUTHORIZED**  
Version: **v1.0 — 2026-09-08**  
Execution boundary: **BOUNDED QA ACQUISITION ONLY; FULL-UNIVERSE EXPANSION NOT AUTHORIZED**

This proposal converts the frozen G2B/G3B contracts into a bounded acquisition plan. All source selections below are **proposed contract selections**, not active subscriptions, downloads, feature-use permissions or empirical approvals.

## 1. Proposed acquisition scope

First-round scope is limited to C01–C09 minimum requirements plus E02/E03 fields explicitly required by surviving competing specifications or available in the same low-marginal-cost snapshot. E01 is excluded from event-time acquisition/use because its PIT condition is unmet.

`acquisition breadth ≠ model-use authorization`  
`stored data ≠ decision-time available data`

| Contract | Proposed canonical contract | Documented fallback contract | Authorized logical/physical field target | First-round tier |
|---|---|---|---|---|
| C01 Security master | SSE/SZSE official security-reference/listing/status history by venue | CSMAR/RESSET licensed reference history; Tushare `stock_basic` only for explicit gap investigation | Stable internal ID mapped from venue+code; entity ID; code-valid intervals; security type/currency; listing/delisting/status intervals; source/public/available/version metadata. Candidate fallback fields: `ts_code,symbol,name,market,exchange,curr_type,list_status,list_date,delist_date` | CORE |
| C02 Calendar | SSE/SZSE official trading calendars/session notices | Tushare `trade_cal` with explicit source tag | venue, `calendar_date`, trading flag, previous trading day; session/status when supplied; publication/availability lineage. Candidate fields: `exchange,cal_date,is_open,pretrade_date` | CORE |
| C03 Raw market | Venue-authorized SSE and SZSE historical unadjusted L1/EOD products | CSMAR/RESSET; Tushare `daily` only through audited substitution | security/time; raw pre-close/OHLC; volume and amount with units/currency; trading status; delivery/availability/schema lineage. SSE candidate fields: `SecurityID,DateTime,PreClosePx,OpenPx,HighPx,LowPx,LastPx,Volume,Amount`; Tushare fallback equivalents documented in G3B-02 | CORE |
| C04 Corporate actions | Exchange/company official corporate-action and disclosure records | Licensed CSMAR/RESSET; Tushare action/adjustment tables after schema/vintage qualification | action ID/type; announcement, record, ex and effective dates; cash/share terms and units; status/revision/source document. Adjustment products additionally require factor/base/formula/effective/vintage version | CORE; adjustment factor is COMPETING-SPEC |
| C05 Eligibility/suspension | Exchange official trading-status history | Licensed CSMAR/RESSET; Tushare `suspend_d` with explicit provenance | state type/start/end/reason/source; public/available time; intraday interval only if same-source low-cost. Candidate fields: `ts_code,trade_date,suspend_timing,suspend_type` | CORE |
| C06 Historical industry | CSRC/CAPCO immutable dated classification snapshots | Qualified licensed history only after vintage audit; no current-label fallback | Original security code/name; taxonomy/version; hierarchy/code/label; stated period; page publication/available time; checksum/snapshot; derived known-from/to, age and stale-gap state | CORE |
| C07 Benchmark/index | Official index publisher raw index and constituent/weight histories | Licensed CSMAR/RESSET; Tushare `index_weight`/index series with explicit provenance | benchmark identity/version; raw observations; member/weight records; announcement/effective/available/vintage fields | COMPETING-SPEC / E03 |
| C08 Manifest | Internal immutable acquisition manifest | None | source/dataset/request/retrieval/vintage/schema/checksum/count/coverage/missingness/licence/software/retry/fallback records | CORE GOVERNANCE |
| C09 Outcome zone | Same approved raw C01/C03/C04 snapshots, physically/logically routed to outcome zone | Same explicit fallback policy | Raw future observations only; outcome ingest ID/access class; no labels or targets computed during acquisition | CORE VALIDATION |
| E02 Liquidity/turnover | C03 volume/amount co-acquisition; authoritative share-capital/free-float history where PIT-qualified | Licensed database with effective/vintage fields | raw volume/amount; shares outstanding/free float with effective and available/vintage time. No quote/depth/tick acquisition in first round | COMPETING-SPEC |
| E03 Benchmark/exposure | Same C07 official publisher contracts | Same C07 fallback policy | benchmark raw observations and PIT member/weight history. Exposure measurements remain unimplemented | COMPETING-SPEC |
| E01 Announcements/events | None for event-time use | None authorized | Schema/PIT audit records only; no formal first-round event archive | EXCLUDED / CONDITION NOT MET |

Every fallback substitution must be explicit, reason-coded, field/date/security scoped, separately versioned where needed and visible to downstream code. Missing canonical rows remain missing unless a later rule authorizes substitution.

## 2. Versioned PIT machinery universe

Universe construction uses:

`C01 eligible A-share security state at t`  
`+ latest C06 official snapshot with available_time ≤ t`  
`+ versioned MACHINERY_INDUSTRY_SCOPE_MAP`  
`→ PIT machinery-universe membership at t`.

Primary universe: include official classes 34 and 35 under their applicable taxonomy versions; exclude 36 and 37. Codes 38, 40 and 43 are `OUT-OF-PRIMARY / EXTENSION-ELIGIBLE`: they cannot enter primary membership, pair formation, N0/N1 estimation or primary evaluation. Same-process, negligible-marginal-cost raw records may be retained only in a quarantined extension raw zone. `acquisition breadth ≠ universe membership authorization`.

Carry-forward retains `source_snapshot_id`, publication/available time, taxonomy version, `classification_age` and stale-gap indicator. No hard staleness threshold is proposed. The 2021 Q3–2023 H1 publication interval is preregistered for later robustness/validity analysis.

## 3. Proposed date range and clock capability

- **Primary complete-period acquisition zone:** `2013-01-07 through 2025-12-31`.
- **Separate future-use zone:** `2026-01-01 through the latest complete trading day available at acquisition time`, physically/logically marked `POST-2025 / FUTURE-USE`.
- **Earliest eligible decision observation:** first authorized decision clock strictly after the 2013-01-07 C06 publication becomes available; not assumed to be the period start.
- POST-2025 data have no development, validation, held-out, extension or production-evaluation status until G4 assigns permitted use. Storage authorizes neither outcome inspection nor feature use.
- **Minimum market capability:** daily venue EOD raw OHLC/pre-close/volume/amount/status plus corporate-action and calendar history.
- **Minimum C06/C07/C04/C05 capability:** native event/snapshot frequency with actual publication/effective/available lineage; never resampled into false availability.
- **Enhancement capability:** E02 daily activity/free-float denominator and E03 daily benchmark observations plus native constituent/weight changes.
- **Excluded enhancement:** tick, L2/depth, signed order flow and full event/NLP archive.

Acquiring daily data does not freeze daily measurement windows, event clocks, factors or models. Any later finer-frequency expansion requires a separate requirement and acquisition authorization.

## 4. Immutable storage and lineage

Every retrieval creates a new immutable raw snapshot preserving provider/source, endpoint/dataset, exact request parameters, retrieval time, source/vintage semantics, schema version, checksum, byte/row counts, temporal/security/field coverage, missingness summary, license tag, acquisition-code version and retry/failure/fallback log.

Pipeline:

`Immutable Raw → Cleaned → PIT-Aligned → Derived Measurement`

No upstream overwrite is allowed. Adjusted prices are derived/comparison artifacts only; raw unadjusted observations plus corporate-action lineage remain canonical. Provider-adjusted products require method/base/version/vintage provenance and cannot be the sole raw record.

## 5. Outcome quarantine

`EVENT-TIME INPUT DATA` and `RESOLUTION / VALIDATION OUTCOME DATA` receive separate physical/logical zones and access policies. C09 may store later raw observations needed eventually for catch-up, reversal/normalization, persistence, relationship continuation/break, horizon and magnitude, but acquisition computes none of these targets.

Event-time feature jobs must have no read path to the outcome zone. Promotion of a later observation into a later sequential decision requires a new legitimate decision-time information set, never retroactive use.

## 6. Missingness, outage and schema-change contract

- Missing canonical data remains missing until an explicit substitution decision.
- Outages create incident and retry records; repeated retrieval cannot masquerade as a new source vintage.
- Schema changes trigger quarantine, dictionary diff, parser-version change and revalidation before ingestion resumes.
- Identifier conflicts remain unresolved rows until deterministic C01 reconciliation; no name-only silent joins.
- Revisions/restatements append a new source version linked to the prior record; no overwrite.
- Coverage summaries are produced before acceptance, but no numerical completeness threshold is frozen in this proposal.
- PIT-unreconstructable fields are excluded from event-time paths and reason-coded.

## 7. Acquisition sequence

1. Resolve access/licence terms and exact dictionaries for approved source classes; enforce the frozen primary/extension scope map.
2. Create empty immutable storage zones, manifest schema and access controls; validate without research data.
3. Acquire one bounded canonical metadata snapshot for C01/C02/C06/C08 and verify identifiers, publication times, checksums and taxonomy versions.
4. Acquire bounded C03/C04/C05 history for a prespecified tiny schema-validation slice; quarantine it until acceptance. This is acquisition QA, not empirical inspection.
5. If QA passes, expand mechanically to the approved universe/date range; compute coverage/missingness only.
6. Co-acquire C07/E02/E03 only under their approved source contracts and fields.
7. Route C09 copies/partitions to the outcome zone and test access denial from event-time paths.
8. Stop and return an acquisition completion/quality report before any cleaning, PIT alignment or measurement computation beyond structural QA.

## 8. Frozen budget and access constraint

- **No new paid data commitment without separate researcher approval.**
- Exact SSE/SZSE historical product licence, internal-use limits and fees must be accepted before purchase/access.
- CAPCO/CSRC public archive reuse and automated retrieval terms must be recorded; public visibility is not assumed to grant redistribution rights.
- Licensed CSMAR/RESSET fallback access is optional and cannot be purchased merely for field richness.
- Acquisition may use lawful public sources, existing authorized exchange/source access, and institutional databases already legitimately available to the researcher. The production architecture must not silently depend on a costly/non-portable source.
- Budget priority: C01/C03/C04/C05/C06/C08/C09 core integrity first; C07/E02/E03 are approved for first-round scope; E01 excluded.
- If a new subscription, API purchase, licence upgrade or material expense is required, stop and report the exact requirement, benefit, alternative and cost.
- No credentials may be embedded in manifests, code or repository artifacts.

## 9. Stop and expansion rules

Stop acquisition and return for review if:

- required PIT/vintage semantics differ from the approved contract;
- a provider supplies only opaque adjusted history;
- historical universe/code lineage cannot be reconciled deterministically;
- C06 originals/publication provenance or version transitions are incomplete;
- licence terms prohibit the intended internal reproducible use;
- a schema change invalidates the parser or logical mapping;
- coverage gaps affect required core fields and no explicit fallback decision exists;
- outcome quarantine/access controls fail;
- expected cost or storage burden exceeds the approved envelope.

Expansion beyond daily/L1 EOD, the proposed date range, core 34/35 universe, or authorized E02/E03 fields requires a new decision record. Poor PnL, model preference or desire for extra factors cannot expand acquisition scope.

## 10. Authorization now in force

Only `G3B-QA — Bounded Formal Acquisition & Structural Validation Slice` is authorized. The slice must be selected deterministically for technical coverage across SSE/SZSE, identifier/listing/delisting, suspension/missing sessions, corporate-action lineage, C06, C07/E03, E02 and schema time consistency. It may validate structural contracts and immutable/quarantine controls only. It may not compute or inspect pair/relationship statistics, abnormality, UR/MP/R objects, mechanisms, targets, predictions, portfolios or PnL.

After QA, full-universe expansion requires a new researcher approval.
