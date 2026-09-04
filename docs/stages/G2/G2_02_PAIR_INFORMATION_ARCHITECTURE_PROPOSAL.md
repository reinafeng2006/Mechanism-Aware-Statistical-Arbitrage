# G2-02 — P0/P1 Pair-Information Architecture

Status: **PROPOSED — AWAITING RESEARCHER APPROVAL**

Scope: semantic information architecture for establishing and maintaining a pair relationship prior. No estimator, representation, factor formula, pair score, threshold, update frequency, validation metric or empirical winner is selected.

Preserved boundaries:

- `relationship validity ≠ trading predictability`
- `economic proximity ≠ statistical dependence`
- `more information ≠ better pair model`

## 1. Precise P0 semantics

**P0 — Market-Relationship-Only** is the minimum formal pair-information architecture. Pair relationship evidence is derived only from reproducible market/statistical information that was available point-in-time. P0 must be capable of representing the G2-01 signed joint-conditional and directional-response semantics, but G2-02 does not select how.

P0 is an architecture of distinct evidence families, not a composite Pair Score. Presence in P0 permits later measurement design; it does not require that every family enter one final specification.

## 2. Precise P1 semantics

**P1 — P0 + Economic/Company Relationship Information** preserves the complete, unchanged P0 market layer and adds a separately identifiable secondary economic/company layer. That layer may provide prior information, regularization, tie-breaking, sparse-history support, structural-change/rejection context, or economically meaningful shock/exposure context.

P1 uses the broader **Economic Relationship Representation**, which may later describe similarity, competitor, supplier/customer, upstream/downstream, substitute-product, or opposite exposure to common shocks, including signed, asymmetric or state-dependent economic relationships where justified. P1 does not assume that greater similarity or more fields increase pair validity.

## 3. Permitted information families

| Architecture | Family | Semantic contribution | Non-equivalence boundary |
|---|---|---|---|
| P0 | Raw joint/co-movement information | Unadjusted observed joint market behavior | Does not isolate exposures, residual dependence, stability or economic linkage. |
| P0 | Factor/exposure relationship information | Similarity or opposition in specified market/industry/risk exposures | Does not establish residual relation or a valid normal relationship. |
| P0 | Conditional/residual relationship information | Dependence remaining conditional on a specified information/control representation | Inherits the conditioning model; is not intrinsically superior to raw information. |
| P0 | Dynamic stability/breakdown information | Persistence, evolution or invalidation evidence for a specified relationship | Does not explain the economic cause of a break or prove M0. |
| P0 | Signed/asymmetric/state-dependent relationship information | Direction, response asymmetry and conditional-state variation required by G2-01 | Capability requirement only; no representation is selected. |
| P1 only | Economic/company relationship information | Secondary prior/context concerning economically meaningful links, exposures or structural change | Economic relationship is not statistical dependence or trading validity. |

Correlation, distance, regression, residualization, cointegration and factor models remain examples of non-equivalent candidate representations; none is selected or required here.

## 4. Information excluded from pair formation

- Future catch-up, reversal, convergence, normalization, later PnL or any outcome unavailable at pair-decision time.
- Manual/subjective pair assignment, hand-picked exceptions or outcome-informed pair retention.
- Observatory-only ideas, Discovery/Triage-only material, inaccessible-source claims or unadmitted evidence.
- Mechanism labels or resolution outcomes treated as evidence that the prior pair relationship was valid.
- Company similarity treated as automatic validity, a mandatory core input, or a substitute for market relationship evidence.
- Unversioned, stale or unavailable-at-time inputs represented as contemporaneous.
- A hidden composite Pair Score that collapses non-equivalent information families without a later explicit G2 decision.
- Final strategy PnL as the first criterion for choosing P1 over P0.

## 5. PIT / update / latency classification

The classifications below describe conceptual roles, not selected sampling or update frequencies.

| Information family | Primary latency role | Secondary timing interpretation | G2/G3 unresolved boundary |
|---|---|---|---|
| Raw joint/co-movement | **fast market relationship information** | Accumulated history may support a medium relationship state | Return/price object, event clock, history and refresh rule. |
| Factor/exposure relationship | **medium relationship state** | New market observations may update exposure evidence quickly | Exposure semantics, factor information set, estimation and PIT vintage. |
| Conditional/residual relationship | **medium relationship state** | New conditional innovations may be fast observations | Conditioning set, residual meaning, history, uncertainty and update policy. |
| Dynamic stability/breakdown | **medium relationship state** | New observations may add fast warning evidence without instantly redefining normality | Break/change construct, accumulation, anti-circularity and materiality. |
| Signed/asymmetric/state-dependent relationship | **medium relationship state** | Observed directional responses are fast market information | State semantics, direction/horizon, uncertainty and adaptation policy. |
| Economic/company relationship | **slow prior** | Dated structural change may later support relationship/rejection context | Representation, vintage, decay/staleness and sparse-history use. |

**Latency-critical boundary:** slow company information should normally be precomputed/cached as relationship context. It must not be placed automatically in fast abnormality or mechanism paths. A newly arriving, timestamped public company event may later be considered as a separate mechanism-discriminator or rejection update under its own PIT rules; that does not convert the slow P1 relationship layer into a fast pair-formation signal.

## 6. P0/P1 fair-comparison principle

P0 is the simpler primary benchmark. P1 is an incremental candidate, not the default full model. P0 and P1 must be compared under the same prespecified pair universe, market-information layer, PIT availability rules, timing origin, candidate relationship semantics, validation protocol and outcome quarantine. P1 must differ only through the declared economic/company layer and its declared role. P1 may not be introduced, redefined or retained after inspecting P0 outcomes.

## 7. Conceptual incremental value

P1 survives only if the added layer demonstrates incremental **relationship-level** value beyond P0. The future validation design must be capable of assessing stability, calibration, generalization, false-pair/false-relationship behavior, relationship-break detection, uncertainty and sparse-history performance. These are constructs to assess, not frozen metrics, loss functions or thresholds.

Incremental value is not established by more features, economic plausibility alone, isolated examples, improved in-sample fit or final strategy PnL as the first test.

## 8. G2 measurement decisions deferred

- Which P0 families become operational candidates and whether any are combined.
- Raw versus factor-adjusted/residual representation and every estimator/formula.
- Economic Relationship Representation inputs, encoding, direction/sign and P1 role.
- Pair universe, eligibility, refresh/event clocks, histories, windows and missing/stale handling.
- Update frequencies, cache invalidation, uncertainty representation and stability/break rules.
- Fair-comparison metrics, estimands, validation protocol and incremental-value threshold.
- Sparse-history definition and how P1 support avoids leakage or subjective assignment.
- Whether timestamped company events enter later C/R paths and how they remain separate from P1 slow context.

## 9. Mechanism & Signal Map implications

- The **Relationship** role gains an explicit P0 market layer and optional P1 slow economic context.
- Neither P0 nor P1 is an abnormality detector, mechanism classifier, resolution model or trade rule.
- P0/P1 establishes context against which later observed-versus-expected response may be measured; it does not itself identify M0–M3.
- Slow P1 context is cached by default. Any fast company event must be separately timed and governed as later C/R evidence.
- Relationship-break and structural-change information may weaken the prior or support later rejection, but cannot alone create a hard M0 gate.

## 10. Proposed classification

### FROZEN SEMANTICS — proposed

- P0 as the simpler, reproducible PIT market/statistical relationship-information architecture.
- P1 as unchanged P0 plus a separate secondary Economic/Company Relationship layer.
- The six permitted information families and their non-equivalence.
- P0/P1 same-protocol comparison and P1 incremental relationship-level survival requirement.
- Slow P1 context is normally precomputed/cached rather than automatically latency-critical.
- The exclusions and preserved non-equivalence boundaries above.
- No P2: G2-02 found no distinct architecture that cannot be represented within P0/P1.

### G2 MEASUREMENT DECISION — DEFER

All representations, estimators, variables, formulas, combinations, clocks, histories, update rules, uncertainty treatments, metrics and thresholds listed in Section 8.

### EMPIRICAL VALIDATION — DEFER

Whether any P0 specification establishes usable relationship quality; whether P1 adds OOS relationship-level value; whether signed/asymmetric/state-dependent structure is measurable; and performance on stability, calibration, generalization, false relationships, break detection, uncertainty and sparse history. Trading PnL remains later economic validation, not the first pair-architecture test.

## Approval decision

Researcher action required: **APPROVE, REVISE or REJECT** this P0/P1 semantic architecture, timing roles, fair-comparison principle, incremental-value boundary and proposed classification. G2-03 remains unauthorized.
