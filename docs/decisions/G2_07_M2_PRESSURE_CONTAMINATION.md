# G2-07 — M2 Pressure and Proxy-Contamination Measurement Freeze Decision

Status: **APPROVED / FROZEN**
Date: 2026-09-07
Boundary: candidate measurement design only. All equations are **ILLUSTRATIVE / UNAUTHORIZED**. No final M2 formula, factor, estimator, threshold, window, pressure proxy, belief model, provider or data source is selected.

## Decision objective

Operationalize the candidate M2 interpretation:

> The source/shocked asset may have moved excessively relative to its expected signed conditional response because of temporary liquidity/order-flow pressure rather than permanent information-driven repricing.

Binding boundaries:

`excess move ≠ temporary pressure`

`abnormal volume / turnover ≠ M2 identification`

`flow proxy ≠ exogenous pressure`

`future reversal / normalization ≠ event-time M2 input`

M2 Evidence remains downstream of overshoot-like abnormality, uncertainty, pressure-source lineage, liquidity/flow state, contamination audit and rival evidence. It cannot follow mechanically from excess movement alone.

## Construct decomposition

1. **Expected Signed Conditional Response** — what the current valid relationship/state implies the shocked asset would normally do using only PIT information already incorporated into normality.
2. **Observed Source/Shocked-Asset Response** — what the asset has actually done by the current decision time under a declared response definition and clock.
3. **Oriented Excess-Move / Overshoot-Like Gap** — departure beyond the expected signed response, oriented consistently across positive and negative expected directions.
4. **Response / Relationship Uncertainty** — uncertainty around the expected response, normal variation and relationship state.
5. **Pressure-Source Evidence** — PIT evidence that a trading/liquidity mechanism could plausibly create temporary demand or supply pressure.
6. **Liquidity / Flow-State Evidence** — observable state information potentially consistent with temporary pressure, without presuming causality or exogeneity.
7. **Proxy-Contamination Audit** — an explicit examination of mechanical return content, endogenous price response, overlapping inputs/windows, future leakage and motive ambiguity.
8. **Rival Information Evidence** — evidence favoring permanent/fundamental repricing, M1-type diffusion, relationship change/break or another explanation.
9. **M2 Evidence** — a downstream, role- and time-specific belief-update input formed only after the preceding components and limitations are declared; never an automatic label or probability.

The decomposition separates abnormal movement from evidence about its economic source.

## Oriented excess-move semantics

Positive orientation means movement beyond the expected response in its expected signed direction. Overshoot is therefore directionally consistent for positive and negative expected responses.

Notation for illustration only:

- `e_t`: expected signed response of the source/shocked asset;
- `o_t`: observed source/shocked-asset response;
- `d_t = sign(e_t)`: expected direction when meaningfully established;
- `u_t`: unresolved response/relationship uncertainty;
- `l_t`: declared PIT liquidity/flow context;
- `p_t`: declared PIT pressure-source evidence;
- `r_t`: declared rival/rejection evidence.

One possible orientation is:

**ILLUSTRATIVE / UNAUTHORIZED**

`excess_gap_t = d_t × (o_t − e_t)`

Positive indicates movement beyond expectation in the expected direction; negative indicates shortfall relative to expectation. This is the semantic counterpart—not the arithmetic negative or economic opposite—of M1 under-response. If expected direction is near zero, unstable or too uncertain, oriented excess must not be mechanically assigned; the observation may remain unoriented abnormality or U. No sufficiency rule is selected.

## Competing candidate measurement ladder

### MP0 — Excess-Move Diagnostic

Measures overshoot-like abnormality relative to Expected Signed Conditional Response. It may remain raw or uncertainty-aware; no variant is selected.

**ILLUSTRATIVE / UNAUTHORIZED**

`MP0_raw,t = d_t × (o_t − e_t)`

`MP0_std,t = MP0_raw,t / u_t`

MP0 measures an excess-move morphology only. It does not identify temporary pressure, exogeneity or M2.

### MP1 — Excess Move + Accessible Liquidity/Flow Context

Adds broadly available PIT market/liquidity/trading-state context where permitted by reviewed evidence.

**ILLUSTRATIVE / UNAUTHORIZED**

`MP1_t = diagnostic(MP0_t, l_t)`

Volume, turnover, liquidity or generic flow may provide context but cannot independently identify M2. Inputs already used in the Expected Response or MP0 construction must be lineage-audited to avoid double use or mechanical amplification.

### MP2 — Pressure-Source / Contamination-Audited Diagnostic

Adds stronger pressure-source provenance and an explicit contamination/rival audit.

**ILLUSTRATIVE / UNAUTHORIZED**

`MP2_t = diagnostic(MP0_t, l_t, p_t, contamination_t, r_t)`

This is an evidence architecture, not a formula, classifier or exogeneity label. Even a passed audit cannot prove temporary pressure; it narrows known contamination and rival channels.

### MP3 — High-Frequency Permanent/Transitory Diagnostic

Preserves specialized trades/quotes/signed-flow or permanent/transitory decomposition only as a possible difficult extension when it offers distinct identification value.

**ILLUSTRATIVE / UNAUTHORIZED**

`observed_move = model-dependent permanent component + model-dependent transitory component`

The decomposition is conditional on its microstructure model, data construction and identification assumptions. A model-estimated transitory component is not automatically M2 or exogenous pressure.

MP0–MP3 form a candidate complexity/information-requirement ladder, not an evidence-strength, identification-quality or model-maturity ranking. They remain competing/nested architecture candidates, not a mandatory progression. Greater complexity does not imply better M2 identification and is not presumed superior.

## M1 versus M2

| Dimension | M1 candidate question | M2 candidate question |
|---|---|---|
| Asset being judged | Linked peer/follower | Source or shocked asset |
| Response morphology | Insufficient movement in expected signed direction | Excessive movement beyond expected signed response |
| Additional evidence | Source/link/timing and rival evidence | Pressure source, liquidity/flow state, contamination and rival evidence |
| Candidate future validation | Follower catch-up | Source reversal/normalization |
| Identification boundary | Under-response does not identify M1 | Excess movement does not identify M2 |

The same multidimensional abnormality may support competing M1 and M2 interpretations. M1 is not defined as the negative of M2, and M2 is not defined as the negative of M1: they concern different response objects and different economic evidence chains.

## Proxy-Contamination Audit Contract

Every future M2 proxy must carry a versioned `Contamination Record` containing at least:

1. exact construction inputs and transformations;
2. whether realized return enters mechanically;
3. whether price/volume variables act simultaneously as proposed cause, response and proxy;
4. endogenous-response risk;
5. overlapping-window and shared-input risk;
6. future-information or revised-data leakage;
7. pressure-source and flow-motive ambiguity;
8. what the proxy actually identifies under its assumptions;
9. what it cannot identify.

The record must also link observation/availability timestamps, source lineage, formula version and any overlap with Expected Response, abnormality or outcome construction. A contaminated proxy may remain descriptive/contextual or rival information, but cannot silently become Mechanism Discriminator Evidence. Cleaning a known mechanical component does not by itself establish exogeneity.

## PIT and sequential timing

Every candidate must distinguish:

1. **Pressure-source/event time** — when the candidate pressure-generating event occurs or becomes observable;
2. **Market/flow observation time** — when trades, quotes, volume, turnover, flow or liquidity state are measured;
3. **PIT availability time** — when each observation becomes lawfully usable, including release/vintage delay;
4. **Abnormal-price observation time** — the interval used to measure observed excess movement;
5. **Decision time** — the prediction origin for initial M2 discrimination;
6. **Subsequent sequential-update times** — later decision origins when genuinely new information becomes available;
7. **Outcome-validation horizon** — the future interval used to evaluate reversal, normalization, persistence or permanent repricing.

Information available by the initial decision time may serve declared discriminator or rival roles. Later-released flow, holdings, event or market-state information may update beliefs only from its actual PIT availability time. Recomputed unchanged data are not new evidence. Future reversal/normalization remains an outcome at the original decision origin even though the realized path may become input to a genuinely later decision.

No daily-close, intraday or event clock is presumed. Frequency, synchronization, market microstructure treatment, non-trading intervals, release delays, update cadence and horizons remain unresolved.

## Rival and rejection boundaries

Candidate rivals include:

- permanent or fundamental information-driven repricing;
- M1-type delayed diffusion across the pair;
- relationship change/break or stale conditional reference;
- continuing/common shock;
- liquidity shortage versus excess supply/demand pressure;
- endogenous trading response to returns;
- microstructure effects, measurement error or non-synchronous observation;
- peer/source own-news and market/industry context.

Rivals must be separately timestamped and assigned G2-05 roles. Evidence may weaken M2 without proving M0. M0 still requires positive rejection evidence; conflicting or insufficient evidence may preserve U. Abnormal volume, turnover, illiquidity, flow or estimated transitory movement alone cannot bypass this boundary.

## Production-feasibility comparison

These are preliminary architecture-level assessments under G2-05, not provider claims, empirical rankings or final classifications. End-to-end feasibility inherits all underlying Expected Response and proxy requirements.

| Candidate | Required raw data | PIT reliability / frequency / coverage | Acquisition, latency, compute, reproducibility | Cacheability / critical path | Preliminary feasibility |
|---|---|---|---|---|---|
| MP0 | Expected/observed signed response and possibly uncertainty | Broad coverage may be plausible with ordinary PIT market data, but inherits response specification and clock | Gap transformation is simple; end-to-end burden inherits Expected Response/uncertainty | Normal reference may be cached; observed response is latency-critical | Transformation `EASY`; end-to-end `UNRESOLVED / INHERITED` |
| MP1 | MP0 plus accessible market/liquidity/trading-state data | Frequency and historical/universe coverage depend on selected contextual inputs | Usually moderately derived; reproducibility requires exact definitions and timestamp alignment | slower context may be cached; current state may be critical | `MODERATE` preliminary; component-dependent |
| MP2 | MP1 plus pressure-source lineage, construction inputs and contamination/rival records | PIT reliability may be limited by release lag, motive ambiguity and source coverage | Moderate to hard acquisition/governance burden; explicit lineage and overlap audit required | source history may be cached; newly released evidence may be critical | `MODERATE` to `HARD / OPTIONAL`; source-dependent |
| MP3 | Trades, quotes, possibly signed flow and microstructure history | Specialized high-frequency coverage, clock alignment and reconstruction required | High acquisition, storage, compute and model-reproduction burden | historical calibration may be cached; real-time inputs likely critical | `HARD / OPTIONAL` or `UNAVAILABLE / RESEARCH-ONLY` pending G3 |

The ladder is `widely available PIT market/liquidity data → moderately derived diagnostics → specialized intraday/trades-quotes/signed-flow only if incrementally justified`. A harder candidate may supplement or displace a simpler one only after later validation demonstrates material incremental M2 discrimination or resolution-prediction value. Final PnL is not the first justification for a difficult diagnostic whose declared role is mechanism discrimination.

## Unresolved decisions

- Expected Signed Conditional Response and uncertainty estimators;
- excess-gap formula, scale, normalization and near-zero direction handling;
- MP0 raw versus uncertainty-aware form;
- exact MP1 liquidity/flow context and whether it is input, rival or descriptive only;
- pressure-source definition, provenance and exogeneity limits;
- contamination thresholds, adjudication and permitted-use downgrade rules;
- MP2 composition and whether any source is sufficiently timely/generalizable;
- MP3 microstructure model, identification assumptions and incremental purpose;
- information-set overlap with normality, abnormality and outcomes;
- clock, frequency, synchronization, windows, update cadence and validation horizon;
- M1/M2 joint discrimination, M0 rejection and U handling measurements;
- activation, weighting, probability, belief update and decision rules;
- final feasibility ratings, providers, database design and acquisition;
- validation metrics, A-share transferability and future reversal targets.

## Frozen classification

### FROZEN SEMANTICS

- nine-part M2 measurement decomposition;
- oriented excess movement relative to a valid expected signed response;
- excess-move, temporary-pressure, exogeneity, M2-belief and outcome separation;
- M1/M2 non-equivalence and possible competition over the same abnormality;
- mandatory Contamination Record and permitted-use downgrade boundary;
- seven-time PIT/sequential lineage;
- rival, M0-positive-rejection and U boundaries;
- transformation complexity versus inherited end-to-end feasibility.

### CANDIDATE MEASUREMENT

- MP0 excess-move diagnostic;
- MP1 excess move plus accessible liquidity/flow context;
- MP2 pressure-source/contamination-audited diagnostic;
- MP3 high-frequency permanent/transitory diagnostic as a difficult extension only.

All remain **ILLUSTRATIVE / UNAUTHORIZED**. None is preferred or selected.

### G2-DEFER

All formulas, estimators, uncertainty representations, proxies, contextual inputs, pressure-source definitions, contamination adjudication, clocks, frequencies, windows, role assignments, thresholds, weights, beliefs and model choices; final feasibility ratings and M2 decision use.

### EMPIRICAL-DEFER

Proxy contamination and endogeneity behavior, calibration, stability, incremental mechanism discrimination, resolution prediction, PIT latency, production feasibility, generalization, A-share transferability and reversal/normalization validation without leakage.

## Approval record

Researcher approval on 2026-09-07 freezes the nine-object decomposition, Oriented Excess-Move/Temporary Pressure separation, separate pressure-source and liquidity/flow-state components, mandatory Proxy-Contamination Audit, separate rival channel, MP0–MP3 as unselected competing candidates, seven-time PIT architecture, M1/M2 competing-explanation boundary and preliminary feasibility classifications exactly as documented above.

MP0–MP3 are explicitly a complexity/information-requirement ladder—not an evidence-strength, identification-quality or model-maturity ranking. Greater complexity does not imply better M2 identification.

No candidate, pressure proxy, estimator, threshold, window, provider, frequency, belief model or trade rule is selected. G2-08 remains unauthorized. No data acquisition, implementation or empirical testing is performed.
