# G4-01 Observation, Window & Pair Eligibility Protocol Proposal

Status: **G4-01 APPROVED / FROZEN — 2026-09-10**  
Scope: statistical-protocol design only. No statistical computation, pair construction, return calculation, relationship estimation, target construction, or outcome inspection.

## Governing distinctions

`Core Dataset Structural Freeze ≠ Candidate Measurement Authorization`

`raw observation exists ≠ observation eligible for every measurement`

`structural state ≠ candidate-specific eligibility`

Eligibility is defined as:

`Eligibility(candidate, security/pair, decision_time, rule_version)`

There is no universal eligibility flag. Every materialized mask must be reproducible from:

`CORE-DATASET-FREEZE-V1 + Security-Date Eligibility Sidecar + frozen candidate eligibility rule/version`.

## 1. Observation eligibility semantics

An observation may enter a later candidate rule only through structural metadata available at the applicable decision time:

- stable security identity and the code-valid interval;
- observation date and raw-record presence;
- C04 structural state and basis;
- one frozen C05 state and basis;
- C06 PIT membership state, availability time, taxonomy version, classification age, and stale-gap state where industry conditioning is required;
- identifier-lineage state;
- source, artifact, schema, and provenance qualification.

The rule may not inspect returns, volatility, abnormality, future classification, future relationship behavior, targets, or model outcomes.

Observation presence establishes only that a raw record exists. `NORMAL TRADING OBSERVED` does not establish corporate-action cleanliness. `CORPORATE_ACTION STATUS UNRESOLVED` remains unresolved unless separately qualified evidence changes it in a new dataset/protocol version.

## 2. Missingness and trading-state semantics

Freeze now:

`UNKNOWN MISSINGNESS ≠ suspension`

`UNKNOWN MISSINGNESS ≠ normal trading`

`UNKNOWN MISSINGNESS ≠ zero return`

Silent forward-fill, zero-fill, implicit status inference, and implicit row-dropping that erases the unknown state are prohibited.

Three levels remain distinct:

1. **Observation-level unknown:** a named security-date has no qualified explanation for the absent market observation.
2. **Window-level missingness burden:** the candidate window contains a declared pattern/count of unknown, suspension, resumption, or absent observations.
3. **Pair-synchronization consequence:** one or both security histories cannot supply the representation-required common PIT support on particular dates.

Numerical tolerances and the response to each burden remain unresolved.

## 3. Window eligibility semantics

A candidate window is a versioned interval ending no later than its declared decision/formation origin. Its eligibility record must preserve, without yet adjudicating numerically:

- start, end, decision time, and candidate/rule version;
- candidate-relevant observation support and the dates/reasons not usable under that rule;
- counts and locations of `UNKNOWN MISSINGNESS`, suspension, and resumption states;
- C04 unresolved-state burden and action-lineage qualification;
- identifier transitions and any unresolved economic-continuity question;
- C06 entry, exit, classification availability, taxonomy, age, and staleness;
- incomplete-history reason, including listing after the proposed window start;
- source/schema/provenance changes within the window.

No minimum history, missingness tolerance, window size, or exclusion buffer is selected. A later rule must decide these before computation and may not tune them after viewing research results.

## 4. Identifier transitions

`security identifier continuity ≠ economic relationship continuity`.

The eligibility metadata may map `601313.SH → 601360.SH` through its stable lineage and code-valid intervals. It must also expose the transition and the unresolved economic-continuity state. It may not concatenate histories or treat pre/post-restructuring observations as one economic series absent a separately frozen candidate rule.

## 5. C06 PIT universe discipline

Industry-conditioned eligibility uses only the latest official C06 classification genuinely available at the relevant decision time. It prohibits:

- reconstructing history from the current universe;
- using pre-membership observations merely because the security joins later;
- using a period label as its availability date;
- allowing a future classification or taxonomy revision to alter an earlier mask.

Classification age and stale-gap metadata must survive into the window/pair eligibility record. Their numerical effect remains unresolved.

## 6. Pair eligibility semantics

`security A eligible + security B eligible ≠ pair automatically eligible`.

A pair becomes eligible only under a named relationship-representation candidate and rule version with representation-appropriate, synchronized PIT support. The pair record must preserve:

- both stable identities and code-valid histories;
- ordered decision/formation origin;
- the candidate's required information families and availability boundaries;
- the exact common-support dates and every excluded/unknown date with reason;
- C04/C05 burden for each leg;
- membership and classification-staleness state for each leg where relevant;
- identifier/restructuring discontinuities;
- source and transformation lineage.

No synchronization convention, correlation/distance/residual/cointegration representation, calendar, gap treatment, or minimum overlap is selected.

## 7. Corporate-action boundary

`CORPORATE_ACTION STATUS UNRESOLVED` is preserved. G4-01 defines neither a detector, adjustment algorithm, return threshold, nor action-clean inference.

Raw/unadjusted candidates may have a distinct later eligibility rule, but that rule must explicitly state how unresolved C04 observations are excluded, quarantined, or represented as uncertainty. Adjusted-price or authoritative action-clean candidates remain constrained/blocked under the frozen G3B-C1 matrix until their C04 requirement is satisfied.

## 8. Fair comparison and sample support

Every later comparison of competing specifications must separate:

- differences attributable to the measurement/model; and
- differences attributable to unequal eligible samples.

The protocol must report each candidate's support and either control or explicitly analyze support differences. It may not silently attribute a sample-composition advantage to model quality. The exact common-support, matched-support, stratified, or dual-reporting method is a later numerical protocol decision.

## 9. Versioning and immutability

Each materialized mask must bind the dataset freeze ID/root, sidecar schema/hash, candidate ID, rule ID/version, generation code version, decision time, parameters, upstream hashes, mask hash, and generation timestamp. Rule changes create a new explicit protocol/mask version with ancestry; they never rewrite an earlier mask.

## Frozen classification

| Decision | Classification |
|---|---|
| Candidate/time/rule-indexed eligibility; no global flag | **FREEZE SEMANTICS NOW** |
| Observation/window/pair level separation | **FREEZE SEMANTICS NOW** |
| Durable C04/C05/C06/identifier/provenance propagation | **FREEZE SEMANTICS NOW** |
| Missingness, corporate-action, history, synchronization and staleness tolerances | **NUMERICAL PROTOCOL DECISION LATER** |
| Representation-specific required support and state handling | **CANDIDATE-SPECIFIC** |
| Whether eligibility rules deliver reliable/statistically adequate samples | **EMPIRICAL VALIDATION LATER** |

All numerical tolerances, windows, history lengths, staleness thresholds, synchronization thresholds, and common-support methods remain unresolved.

`G4-01 APPROVED / FROZEN`
