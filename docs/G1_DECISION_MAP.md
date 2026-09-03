# G1 Compressed Decision Map

Status: **APPROVED — DISCOVERY/TRIAGE AUTHORIZED 2026-09-03**  
Audit result: **7 primary decision questions; all 26 existing questions preserved as supporting subquestions.**

## Compression principle

The primary questions control search sequencing, saturation judgments, and synthesis. The original A-Q01–A-Q12 and B-Q01–B-Q14 wording remains authoritative in `G1_LITERATURE_DESIGN.md`. Compression changes neither scope nor meaning and resolves no downstream choice.

Search priority uses:

- **P0 — prerequisite:** needed to interpret evidence elsewhere;
- **P1 — core:** directly informs the frozen thesis and must be covered;
- **P2 — contextual:** important for transferability or completeness after prerequisites.

## Stream A — Pair Formation

### A-P1 — What company/economic representation can justify treating two firms as economically related?

**Downstream decision informed:** G1 candidate-construct taxonomy for Company Representation and the economic content of Normal Pair Relationship; later supplies G2 with candidate information families, not selected variables.

**Evidence that would answer it:** full-text theory, validated firm-similarity or economic-network studies, comparative representation studies, temporal/portability evidence, and work separating shared economic exposure from mere industry labels.

**Still unresolved after literature review:** exact project universe, data sources, fields, encodings, weights, similarity functions, thresholds, update schedule, and chosen representation.

**Supporting subquestions:** A-Q01, A-Q02, A-Q03, A-Q12.

**Search priority:** **P0 — prerequisite.** It establishes what “company-aware” can mean before statistical relatedness is interpreted.

**Stopping condition:** stop discovery when each materially distinct economic-relation family has at least one credible full-text anchor plus contrary/limiting evidence, additional sources no longer change the taxonomy or boundary conditions, and unresolved Measurement Gaps are explicit. Do not stop merely at a paper-count target.

### A-P2 — What statistical representation supports a normal pair relationship, including stability, directionality, decay, and rejection?

**Downstream decision informed:** G1 definition space for Normal Pair Relationship and conditions under which “no valid pair” or relationship failure is conceptually warranted.

**Evidence that would answer it:** full-text theoretical and empirical studies on co-movement, correlation, cointegration, common trends, lead–lag, residual dependence, stability/breaks, directional relations, and explicit rejection/decay criteria, with assumptions and failure evidence.

**Still unresolved after literature review:** chosen statistic/model, estimation window, break test, stability threshold, direction rule, refresh cadence, and operational rejection rule.

**Supporting subquestions:** A-Q04, A-Q05, A-Q10, A-Q11.

**Search priority:** **P0 — prerequisite.** A defensible normal relationship is necessary before a deviation can be called an abnormal pair state.

**Stopping condition:** stop when the main statistical relationship families, assumptions, stability diagnostics, and rejection cases are represented by full-text evidence; material contradictions are mapped; and further sources do not add a new decision-relevant relationship or failure class.

### A-P3 — What construction and evaluation principles make data-driven pairs point-in-time, reproducible, and generalizable?

**Downstream decision informed:** G1 design requirements for formal pair construction and the separation of pair quality from later signal/trading outcomes.

**Evidence that would answer it:** full-text comparisons of hybrid economic/statistical construction, leakage and survivorship controls, formation-only evaluation, temporal/entity transfer, external validation, and market/jurisdiction portability.

**Still unresolved after literature review:** algorithm, objective function, hyperparameters, validation split, performance metric, data pipeline, and final construction procedure.

**Supporting subquestions:** A-Q06, A-Q07, A-Q08, A-Q09.

**Search priority:** **P0 — prerequisite.** It operationalizes the frozen philosophy at the level of research requirements without selecting an implementation.

**Stopping condition:** stop when credible evidence covers hybrid construction, point-in-time failure controls, evaluation separate from trading, and generalization across at least time plus one other axis; remaining China/A-share transfer gaps are recorded rather than filled by assumption.

## Stream B — Monetization / Mechanisms

### B-P1 — When can delayed information incorporation or limited attention plausibly generate follower catch-up?

**Downstream decision informed:** whether M1 remains a literature-supported working hypothesis and which causal ordering, observable families, confounds, and falsifiers should advance as G1 candidates.

**Evidence that would answer it:** full-text theory and identification studies showing source-to-peer information transmission, limited attention, lead–lag, economically linked firms, timing, and contrary cases where apparent delay reflects risk or liquidity.

**Still unresolved after literature review:** event definition, source/follower labeling rule, information-relevance measure, availability lag, horizon, classification rule, and causal estimator.

**Supporting subquestions:** B-Q01, B-Q02.

**Search priority:** **P1 — core**, after an initial A-P1/A-P2 vocabulary pass.

**Stopping condition:** stop when the principal diffusion/attention channels have credible support and counterevidence, temporal-order requirements are clear, at least one non-M1 rival is mapped for each major observable pattern, and new sources no longer alter candidate discriminators or falsifiers.

### B-P2 — When can temporary liquidity or flow pressure plausibly generate reversal by the shocked stock?

**Downstream decision informed:** whether M2 remains literature-supported and which pressure, reversal, information-control, and market-structure observables should advance as candidates.

**Evidence that would answer it:** full-text theory and identified shocks involving order imbalance, flows, fire sales, rebalancing, liquidity provision, or constrained intermediation, including evidence separating uninformed pressure from information-driven repricing.

**Still unresolved after literature review:** chosen pressure proxy, shock threshold, affected leg, reversal horizon, exclusion controls, A-share feasibility, and measurement source.

**Supporting subquestions:** B-Q03, B-Q04.

**Search priority:** **P1 — core**, after an initial A-P2 pass.

**Stopping condition:** stop when major exogenous/quasi-exogenous pressure designs, observable families, information confounds, reversibility conditions, and contrary evidence are covered and further papers do not change the candidate discrimination set.

### B-P3 — What separates temporary idiosyncratic dislocation from structural/fundamental divergence?

**Downstream decision informed:** whether M3 has independent content or is only a residual story, and what evidence should favor M0, ambiguity, rejection, relationship invalidation, or no trade.

**Evidence that would answer it:** full-text studies that condition on common risks and identified information/flow channels; studies of structural breaks, fundamentals, persistent divergence, non-convergence, and explicit falsification or abstention.

**Still unresolved after literature review:** operational residual definition, structural-event list, persistence threshold, outcome horizon, censoring, multi-label policy, and no-trade rule.

**Supporting subquestions:** B-Q05, B-Q06, B-Q07, B-Q14.

**Search priority:** **P1 — core**, dependent on A-P2 because relationship decay can mimic a relative dislocation.

**Stopping condition:** stop when evidence establishes whether M3 can be independently interpreted, maps the main structural-divergence alternatives, provides falsifiers for M1–M3, and yields explicit reasons to preserve M0/UNKNOWN rather than force classification.

### B-P4 — Can contemporaneously available evidence distinguish mechanisms well enough to improve resolution and trade/no-trade decisions?

**Downstream decision informed:** the G1 candidate discrimination framework: which observable families and competing implications merit later G2 measurement design, and whether mechanism conditioning is sufficiently plausible to retain the project thesis.

**Evidence that would answer it:** full-text comparative or mechanism-discrimination studies using point-in-time observables, mixture/uncertainty handling, out-of-sample resolution evidence, mechanism-agnostic comparators, net-value evidence, and transferability analysis.

**Still unresolved after literature review:** final feature set, labels, confidence threshold, classifier/model, estimand, split, comparator construction, cost model, trade policy, and materiality threshold.

**Supporting subquestions:** B-Q08, B-Q09, B-Q10, B-Q11, B-Q12, B-Q13.

**Search priority:** **P1 — integrative; searched after B-P1–B-P3 and the A prerequisites.**

**Stopping condition:** stop when every mechanism has at least one mapped point-in-time discriminator and rival explanation, uncertainty/no-trade treatment is covered, predictive and economic claims are distinguished, transfer limits are explicit, and additional sources do not change the candidate decision matrix. If credible comparative evidence is absent, record that absence as a G1 finding rather than expanding indefinitely.

## Cross-stream dependencies

1. **A-P1 → A-P2:** economic relatedness constrains which statistical relationships are interpretable as company-aware rather than accidental co-movement.
2. **A-P1 + A-P2 → A-P3:** construction cannot be evaluated for generalization until the economic and statistical relationship targets are conceptually clear.
3. **A-P2 → B-P1/B-P2/B-P3:** a relative move is not a mechanism-specific dislocation unless a defensible normal relationship existed before the event.
4. **A-P2 relationship failure → B-P3/M0:** decay or structural break may invalidate the pair rather than indicate temporary M3 normalization.
5. **A-P1 directionality + A-P2 lead–lag → B-P1:** source/follower interpretation requires economic relevance and temporal structure; price leadership alone is insufficient.
6. **A-P3 point-in-time controls → all B questions:** mechanism evidence is inadmissible for project translation if pair membership or relationship quality uses future information.
7. **B-P1/B-P2/B-P3 → B-P4:** contemporaneous discrimination requires distinct candidate implications from each mechanism and its rivals.
8. **B evidence → A rejection criteria:** repeated mechanism ambiguity may imply that a relationship representation is inadequate for monetization, but cannot retrospectively alter pair construction using outcomes.
9. **Pair quality is necessary but not sufficient:** stable relatedness permits interpretation of relative states; it does not establish abnormality, mechanism, resolution, or profitability.
10. **Mechanism plausibility is not pair quality:** mechanism literature cannot justify manually selecting pairs or bypass A-stream construction evidence.

## Proposed search sequence

1. Parallel discovery vocabulary pass for A-P1 and A-P2.
2. A-P3 construction/generalization evidence.
3. Separate B-P1, B-P2, and B-P3 searches using the stable A vocabulary but independent evidence ledgers.
4. B-P4 integrative discrimination search.
5. Cross-stream synthesis and gap audit.
6. Researcher review before any G1 conclusion is frozen or any G2 question is opened.

This sequence is approved for the first bounded Discovery/Triage checkpoint. Light and Selective Deep review remain subject to the checkpoint proposal.

## Compression audit checks

- All A-Q01–A-Q12 appear exactly once under A-P1–A-P3.
- All B-Q01–B-Q14 appear exactly once under B-P1–B-P4.
- Original wording remains unchanged in the G1 literature design.
- No supporting question was deleted, merged, answered, or downgraded.
- Stopping is based on decision saturation and contradiction coverage, not paper counts.
- Downstream measurement, statistical, model, and implementation choices remain unresolved.

## Approval record

G1-01 was approved on 2026-09-03. Discovery/Triage is authorized in the documented dependency order. Stop at the first checkpoint with coverage, gaps, and a proposed Light/Selective Deep set.
