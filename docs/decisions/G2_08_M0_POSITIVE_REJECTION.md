# G2-08 — M0 Positive Rejection Evidence Freeze Decision

Status: **APPROVED / FROZEN**
Date: 2026-09-07
Boundary: Rejection Architecture only. All equations are **ILLUSTRATIVE / UNAUTHORIZED**. No M0 classifier, threshold, factor score, estimator, provider, database or trade rule is selected.

## Decision objective

Operationalize the M0 principle:

> M0 requires positive PIT evidence that weakens or invalidates the temporary-arbitrage interpretation. It cannot be inferred merely from insufficient evidence for M1, M2 or M3.

Frozen boundaries:

`No Trade ≠ M0`

`absence of M1/M2 evidence ≠ M0`

`U ≠ M0`

`No Trade can result from M0, U, or later decision/economic criteria`

M0 is an economic rejection hypothesis. U is an epistemic state. No Trade is a later action outcome. They must remain separate objects.

## Three rejection channels

### 1. Pair Rejection

Positive evidence that the normal relationship prior/reference is stale, structurally changed, broken or no longer sufficiently valid for temporary-abnormality inference. Candidate families include PIT relationship instability/breakdown, stale linkage, persistent parameter/state change and loss of relationship validity.

Pair Rejection targets the reference on which abnormality is defined. It need not assert a particular fundamental cause and does not follow from one extreme observation.

### 2. Event / Mechanism Rejection

Positive PIT evidence that the current movement has a company-specific, fundamental, structural or otherwise non-temporary explanation that weakens an M1/M2/M3-style temporary-arbitrage interpretation.

Event Rejection targets the interpretation of the current episode. It may coexist with a still-valid long-run pair relationship; rejecting one event does not necessarily reject the pair.

### 3. Decision Rejection / Abstention

The pair or event may lack sufficient positive evidence for M0 while uncertainty, conflict, missing information, stale inputs or poor data quality makes attribution or action irresponsible. This supports `U / Abstain`, continued tracking or later policy-level No Trade—not an M0 label.

Decision Rejection is therefore a decision-system sufficiency boundary, not an economic mechanism and not positive M0 evidence.

## Construct decomposition

1. **Relationship-Break Evidence** — PIT evidence that the current normal-reference state or its stability has materially changed.
2. **Fundamental / Company-Specific Event Evidence** — a dated public event or fundamental update that may explain the observed movement as information-driven rather than temporary.
3. **Structural Exposure / Linkage Change Evidence** — PIT evidence that the economic linkage, exposure direction, business structure or relevant relationship semantics have changed.
4. **Persistent-vs-Temporary Evidence** — evidence available by the current decision time concerning persistence or ongoing change; future realized persistence remains validation-only for earlier origins.
5. **Data / Information Quality Evidence** — availability, staleness, timestamp integrity, missingness, revision, coverage and measurement-reliability information.
6. **Conflict / Ambiguity Evidence** — incompatible mechanism indications, rival explanations or uncertainty preventing responsible attribution.
7. **Downstream M0 Evidence** — a declared, positive, time-valid rejection input supported by one or more of the first four substantive channels and bounded by quality/conflict information.

No component is universally required or sufficient. Data-quality or ambiguity evidence alone normally supports U/abstention, not M0. Components remain distinct and are not combined into a rejection score here.

## Candidate rejection measurement families

### R0 — Relationship-Validity Warning

Candidate warning that the current normal relationship may be stale, unstable or broken.

**ILLUSTRATIVE / UNAUTHORIZED**

`R0_t = diagnostic(PIT relationship state, uncertainty, stability history, break evidence)`

R0 may support Pair Rejection or a relationship-update warning. It does not prove structural break, M0 or permanent divergence by itself.

### R1 — Positive Fundamental / Event Rejection

Candidate PIT evidence that a public company/fundamental event provides a non-temporary explanation for the current movement.

**ILLUSTRATIVE / UNAUTHORIZED**

`R1_t = diagnostic(event content, first-public time, affected asset, expected economic direction, current response)`

R1 requires event identity, first-public availability, affected security, directional relevance and competing-explanation records. Event existence alone is insufficient.

### R2 — Structural-Linkage Change Diagnostic

Candidate evidence that the economic relation, exposure direction, product-market link or pair semantics have changed.

**ILLUSTRATIVE / UNAUTHORIZED**

`R2_t = diagnostic(previous PIT linkage, newly available structural evidence, relationship implications)`

R2 may affect Pair Rejection, Event Rejection or cached P1 context depending on timing and role. Company similarity changes do not automatically invalidate a market relationship.

### R3 — Ambiguity / Information-Quality Rejection

Candidate information-sufficiency diagnostic for missing, stale, conflicting, revised or unreliable inputs.

**ILLUSTRATIVE / UNAUTHORIZED**

`R3_t = diagnostic(availability, staleness, conflict, lineage, uncertainty)`

R3 primarily supports U/abstention, measurement rejection or continued tracking. It does not create M0 unless separate positive structural/fundamental rejection evidence exists.

R0–R3 are competing/complementary candidate families, not a maturity ladder and not a unified rejection score. A future candidate may occupy multiple channels only with separate construct, target and PIT-role records.

## M0, U and No Trade boundary

| Object | Required basis | Meaning | What it is not |
|---|---|---|---|
| M0 | Positive structural, fundamental, relationship/link invalidation or other admitted non-temporary evidence | Economic hypothesis weakening temporary arbitrage | Default residual when M1/M2/M3 are weak |
| U | Insufficient, conflicting, unreliable or unresolved evidence | Epistemic inability to assign a responsible mechanism interpretation | Fifth mechanism or weak form of M0 |
| No Trade | Later decision policy outcome | Action may follow M0, U, costs, constraints, uncertainty or poor economics | Direct synonym for M0 |

There is no fallback transition `U → M0`. New positive evidence may later update U toward M0 at that later decision time, but the original state and information set remain recoverable.

## PIT and outcome timing

Every rejection candidate must distinguish:

1. **Relationship-evidence availability time** — when instability, state change or break-related information became usable;
2. **Company/fundamental first-public time** — when the event or disclosure became lawfully available, including vintage/revision lineage;
3. **Abnormal-movement observation time** — the interval over which the episode was observed;
4. **Current decision time** — when rejection, U or continued tracking may be assessed;
5. **Later persistence/break validation horizon** — future data used to evaluate whether rejection was well-founded.

Only information available by the current decision time may enter that decision origin. A break, persistent divergence, revised fundamental or stale linkage discovered with future data cannot be leaked backward into event-time M0 inference. At a later sequential decision it may become newly available evidence, but the earlier state must not be rewritten.

No event clock, daily/intraday frequency, persistence horizon, window or update cadence is selected.

## Outcome-leakage restrictions

- Future persistence or continued break may validate R0/R2 but cannot establish event-time M0 retrospectively.
- Later fundamental realization or revised reporting is not an earlier input unless its earlier public vintage was available.
- Future non-reversal, loss or PnL cannot become M0 evidence at the original decision time.
- A later No Trade outcome or avoided loss does not prove the M0 mechanism.
- Relationship updates must preserve G2-01 anti-circularity: a current anomaly cannot be immediately absorbed into a break diagnosis or new normality by construction.

## Production-feasibility comparison

These are preliminary architecture-level assessments under G2-05, not evidence-quality, predictive-value or final provider conclusions. End-to-end feasibility inherits the selected underlying measurements and source lineage.

| Candidate | PIT availability / reliability | Latency / coverage / acquisition | Reproducibility / cacheability / critical path | Preliminary feasibility |
|---|---|---|---|---|
| R0 | Requires PIT relationship history and state/uncertainty lineage | Broad market-data coverage may be plausible; burden inherits chosen break/stability method | Medium-state diagnostics may be cached; current warning may enter fast rejection path | Transformation may be `MODERATE`; end-to-end `UNRESOLVED / INHERITED` |
| R1 | Requires reliable first-public company/event timestamp and content | Coverage and latency depend on disclosure/event source; structured public events may be easier than difficult NLP | Historical vintages and parsers must be reproducible; new events may be latency-critical | `MODERATE` for structured PIT events; difficult NLP may be `HARD / OPTIONAL` |
| R2 | Often slow-changing but requires dated structural/linkage evidence | Coverage may be sparse and reconstruction-intensive | Normally precomputed/cached; a newly published change can enter fast rejection only from availability time | `MODERATE` to `HARD / OPTIONAL`, source-dependent |
| R3 | Uses data-lineage, availability, staleness, conflict and quality metadata | Broadly required; acquisition burden inherits monitored inputs | Mostly precomputable governance metadata plus latency-critical health checks | Core governance candidate; end-to-end feasibility depends on system lineage |

Reliable, reconstructable PIT evidence is preferred. Difficult NLP, proprietary linkage or specialized event data remains `HARD / OPTIONAL` unless later validation shows material incremental rejection/abstention value over simpler production-feasible evidence. Final PnL is not the first justification for a difficult relationship- or event-rejection variable.

## Unresolved G2 decisions

- operational definition and estimator for relationship break, instability and loss of validity;
- boundary between gradual relationship evolution, temporary abnormality and structural change;
- event taxonomy, materiality, directional relevance and public-time lineage;
- structural linkage/exposure representation and stale-link definition;
- persistence evidence available contemporaneously versus validation-only outcomes;
- data-quality, conflict and evidence-sufficiency measurements;
- whether and how multiple rejection components interact without a single score;
- permitted-use downgrade rules for stale, revised, missing or conflicting information;
- clocks, frequency, windows, update cadence and validation horizon;
- M0 evidence sufficiency, U representation and later No Trade policy;
- final Production Feasibility classifications, providers and database design;
- validation criteria, cross-pair/industry generalization and A-share transferability.

## Frozen classification

### FROZEN SEMANTICS

- positive evidence is required for M0; no M0 by elimination;
- Pair Rejection, Event/Mechanism Rejection and Decision Rejection/Abstention are distinct;
- seven-part construct decomposition;
- `No Trade ≠ M0`, `U ≠ M0`, and no default `U → M0`;
- relationship, company-event, abnormal-movement, decision and validation times remain distinct;
- future break/persistence/fundamental/economic outcomes cannot leak backward;
- data-quality/ambiguity evidence supports U unless separate positive M0 evidence exists.

### CANDIDATE MEASUREMENT

- R0 Relationship-Validity Warning;
- R1 Positive Fundamental/Event Rejection;
- R2 Structural-Linkage Change Diagnostic;
- R3 Ambiguity/Information-Quality Rejection.

All remain **ILLUSTRATIVE / UNAUTHORIZED**. None is selected, required universally or combined into a score.

### G2-DEFER

All formulas, estimators, event/link representations, materiality, persistence, quality/conflict measurements, clocks, windows, thresholds, interaction rules, M0 sufficiency, U representation and decision rules; final feasibility ratings, providers and database choices.

### EMPIRICAL-DEFER

Calibration, false-rejection behavior, break/event identification, PIT latency, incremental rejection/abstention value, production feasibility, generalization, A-share transferability and outcome validation without leakage.

## Approval record

Researcher approval on 2026-09-07 freezes the three-channel Rejection Architecture, seven semantically distinct constructs, R0–R3 as candidate families only, positive-evidence requirement for M0, R3/U boundary, PIT/outcome-leakage rules and preliminary feasibility distinctions exactly as documented above.

`No Trade ≠ M0`; `absence of M1/M2 evidence ≠ M0`; `U ≠ M0`; U must not default to M0.

No combined rejection score, measurement, threshold, window, event/NLP model, provider or trade rule is selected. G2-09 remains unauthorized. No data acquisition, implementation or empirical testing is performed.
