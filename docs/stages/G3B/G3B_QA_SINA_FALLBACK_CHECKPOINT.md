# G3B-QA — Sina Bounded Fallback Checkpoint

Status: **BOUNDED QA COMPLETE / AWAITING RESEARCHER REVIEW**  
Source role: **FALLBACK ONLY — NOT CANONICAL / NOT FORMALLY SELECTED**  
Recorded: **2026-09-09**

Prior predecessor-project experience justified auditing this source only. No predecessor data, artifacts, measurements, results or conclusions entered this project.

`Sina QA success ≠ canonical-source approval`

**Frozen interpretation:** Sina has demonstrated operational usefulness for C03 raw daily observations, but has not demonstrated sufficient governance/source-contract quality to become a canonical source under the currently frozen requirements.

`operationally useful ≠ canonical-qualified`

## Deterministic scope and immutable acquisition

The probe used only `sz000157`, `sz000404`, `sh600031`, `sh600055`, benchmark `sh000300`, and the frozen 2013-01-07–2013-01-11 / 2025-12-29–2025-12-31 inspection slices. Because Sina's history endpoint returns the available history for one requested symbol, the immutable raw payload contains full history for these four names and one benchmark only; it is not a universe acquisition.

Two independent snapshots each made 17 requests: raw history for five symbols plus qfq factor, hfq factor and share-amount responses for the four securities. All returned HTTP 200. All 17 raw response hashes matched on the immediate repeat. Snapshot manifest hashes and paths are recorded in [`G3B_QA_SINA_FALLBACK_MANIFEST.json`](../../../data/manifests/G3B_QA_SINA_FALLBACK_MANIFEST.json). Raw payloads remain Git-ignored `AUDIT/QA — NON-EMPIRICAL` artifacts.

## Structural findings

- Raw daily payload fields decoded as `date, prevclose, open, high, low, close, volume, amount, postVol, postAmt` for equities; the benchmark omitted the equity-specific fields.
- The four securities cover both SSE and SZSE and returned histories beginning between 1996 and 2003, continuing through the retrieval date. All contained the required 2013 and 2025 slices.
- The prefix convention (`sh`/`sz` + six-digit code) was stable across requests, but it is not a security master or identifier-history contract.
- In the early slice, `sz000157` omitted 2013-01-08 while the other three securities and benchmark contained it. Sina supplies a missing row, not an explicit suspension/status reason; missing-session interpretation is therefore non-identifying.
- Public AKShare documentation for this Sina path describes volume in shares and amount in yuan. The raw Sina payload is not self-describing and no authoritative endpoint dictionary/version was exposed, so units remain externally documented rather than contract-enforced.
- Separate qfq/hfq endpoints returned dated factor arrays using fields `d` and `f`. Current AKShare logic constructs qfq/hfq by merging and forward-filling these factors against raw history, then dividing/multiplying OHLC. These adjusted values are derived, not independent raw observations.
- Sina exposes no historical factor vintage archive or adjustment-method version in the observed response. Qfq is anchored to a current factor basis and both factor files may change after later corporate actions/corrections; retrospective revision cannot be reconstructed from a single current download. Qfq/hfq are therefore not PIT-qualified event-time raw records.
- The share-amount endpoint returned response arrays for all four securities. Its observed response is useful for an E02 approximation, but its fields, units, effective-time and revision semantics are not sufficiently self-describing for canonical use.
- No explicit corporate-action terms, announcement/publication times, suspension reasons, historical listing/code intervals, benchmark constituent history or benchmark weights were supplied by the tested endpoints.
- Immediate reproducibility passed 17/17 byte-for-byte. Long-run reproducibility remains limited by undocumented webpage endpoints, lack of schema/version guarantees, mutable current snapshots and stated risk of temporary IP blocking under repeated access.

## Contract-by-contract disposition

| Contract | QA result | Sina qualification | What passed | Material limitation / remaining source need |
|---|---|---|---|---|
| C01 Security master | **FAIL** | **NOT QUALIFIED** | Stable exchange-prefixed request identifiers joined the bounded files. | No security/entity master, listing/delisting intervals, ticker history, eligibility history or versioned identifier mapping. Another source is required. |
| C03 Raw daily market | **PASS WITH LIMITATIONS** | **FALLBACK ONLY** | Raw/unadjusted daily OHLC, previous close, volume and amount; long selected-name history; SSE/SZSE; bounded missing-row behavior; immediate checksum reproducibility. | No authoritative field dictionary, source vintage, correction history, SLA, schema version or guaranteed endpoint stability. Units are externally documented. Cannot qualify as canonical without a separate researcher decision and stronger contract evidence. |
| C04 Corporate actions / adjustment | **PASS WITH LIMITATIONS** | **FALLBACK ONLY for factor comparison; NOT QUALIFIED for canonical action lineage** | Separate qfq/hfq factor responses and reproducible current snapshots. | No action terms/publication/effective lineage or historical factor vintages. Retrospective adjustment revision risk is not reconstructable. Another PIT corporate-action source is required. |
| C05 Suspension / trading status | **FAIL** | **NOT QUALIFIED** | Missing observations can be detected relative to an external calendar. | Missing row cannot distinguish suspension, outage, non-trading eligibility or source omission. Another explicit status source is required. |
| E02 Liquidity / turnover | **PASS WITH LIMITATIONS** | **FALLBACK ONLY** | Raw volume/amount plus a separate share-amount response exists. | Share denominator units, effective time, vintage and revision semantics are insufficiently documented. Turnover would be derived and remains unauthorized. A PIT share-capital/free-float source is still required for robust use. |
| E03 Benchmark linkage | **PASS WITH LIMITATIONS** | **FALLBACK ONLY for benchmark price history; NOT QUALIFIED for linkage** | `sh000300` daily raw index history was available. | No PIT constituent membership, weights, announcement/effective times or benchmark identity-version history. Another source is required for relationship/exposure linkage. |

## Overall source decision

Sina qualifies as **FALLBACK ONLY** for bounded C03 raw daily observations, with explicit provenance and limitations. It is not a possible canonical candidate on current evidence because the webpage endpoints lack adequate contractual schema, vintage/revision, correction, availability-time and stability guarantees.

Its qfq/hfq and share-amount products may be retained only as fallback comparison/diagnostic artifacts. They cannot replace raw history plus corporate-action lineage and cannot enter event-time features without later PIT qualification.

Sina qfq/hfq must not become canonical historical adjusted-price records. Any adjusted representation requires separately qualified corporate-action and adjustment lineage. Immediate hash reproducibility does not establish historical-vintage reproducibility. A missing Sina row remains `UNKNOWN MISSINGNESS` unless a separately qualified C05 source establishes its trading/suspension state. No fallback provider may silently patch a missing or disputed Sina observation: every substitution requires an explicit reason, field/date/security scope, independent version and downstream-visible provenance.

## Remaining acquisition dependencies

- C01 requires a security-master/listing/status source.
- C04 requires PIT corporate-action records and reconstructable adjustment lineage.
- C05 requires explicit suspension/trading-status records.
- E02 requires PIT-qualified share-capital/free-float denominators if retained.
- E03 requires benchmark constituent/weight history with announcement/effective/available times.

No source promotion, formal acquisition, measurement, target or outcome work is authorized by this checkpoint.

`G3B-QA SINA FALLBACK COMPLETE / AWAITING RESEARCHER REVIEW`
