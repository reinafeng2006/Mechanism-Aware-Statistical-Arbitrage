# G1 Literature & Mechanism Evidence Design

## Governing hierarchy

This design is executed inside the project gate hierarchy as:

`G1-01 Literature Design, Discovery & Triage → G1-02 Evidence Review → G1-03 Cross-Paper Evidence Synthesis → G1-04 Evidence Freeze & G2 Handoff`

Its internal adaptive workflow remains:

`Discovery → Triage → Light → Selective Deep → Synthesis Checkpoint`

Selective Deep is decision-triggered, not mandatory. Discovery/Triage are G1-01, Light/Selective Deep are G1-02, the formal Synthesis Checkpoint and four maps are G1-03, and downstream permitted-use freeze belongs only to G1-04. See `docs/G1_STAGE_HIERARCHY.md`.

Status: **DESIGN COMPLETE — RESEARCHER REVIEW REQUIRED BEFORE SEARCH**  
Searches executed: **0**  
Empirical work authorized: **No**

## Primary decision map

The controlling search and synthesis structure is the proposed seven-question map in [G1_DECISION_MAP.md](G1_DECISION_MAP.md). All 26 questions below remain unchanged as supporting subquestions. The map must receive researcher approval before search.

## G1 purpose

G1 will determine what the literature supports, disputes, or leaves unresolved about:

- representing companies and forming economically meaningful, stable equity pairs; and
- mechanisms that may generate relative-price dislocations and variables that may distinguish them.

G1 may identify candidate constructs, observable implications, counter-hypotheses, and Measurement Gaps. It may not select project factors, formulas, algorithms, data vendors, thresholds, labels, horizons, estimators, or trading rules.

## Stream A — Pair Formation

### Evidence questions

| ID | Decision-relevant evidence question |
|---|---|
| A-Q01 | What economic concept of “related companies” is used: product-market similarity, supply-chain linkage, common customers, technology, ownership, industry exposure, shared fundamentals, or another relation? |
| A-Q02 | How are firms represented from company/business characteristics, and which representations have evidence of temporal stability and cross-sample portability? |
| A-Q03 | How are common factor exposures used to establish relatedness while distinguishing common exposure from a tradable relative relationship? |
| A-Q04 | How are empirical co-movement, correlation, cointegration, common trends, lead–lag behavior, or residual dependence used in pair formation, and what assumptions do they require? |
| A-Q05 | How is relationship stability defined, diagnosed, updated, or rejected under structural change? |
| A-Q06 | Which approaches combine economic/company information with market co-movement, and does the combination improve generalization rather than merely in-sample fit? |
| A-Q07 | How do studies prevent look-ahead, survivorship, industry-reclassification, revision, and full-sample pair-selection bias? |
| A-Q08 | How are pair-formation rules evaluated separately from signal generation and trading performance? |
| A-Q09 | What evidence exists for transfer across time, industries, markets, or firm cohorts, especially emerging markets or China/A-shares? |
| A-Q10 | What failure modes favor “no valid pair,” relationship decay, or abstention instead of forced pairing? |
| A-Q11 | Are pair relations directional or symmetric, and when does directionality matter economically? |
| A-Q12 | What candidate information families recur across credible studies, without implying that this project should adopt any of them? |

### Required synthesis outputs

A taxonomy of company representations and relationship concepts; a map of assumptions and failure modes; point-in-time and generalization requirements; evidence for hybrid economic/market approaches; and unresolved Measurement Gaps for G2. No preferred factor, formula, or algorithm may be selected at G1.

## Stream B — Monetization / Mechanisms

### Evidence questions

| ID | Decision-relevant evidence question |
|---|---|
| B-Q01 | What theory and evidence support delayed peer repricing through information diffusion, limited attention, investor inattention, or lead–lag effects? |
| B-Q02 | Under M1, what establishes the source firm, follower firm, information relevance, diffusion channel, and temporal ordering without using later price resolution? |
| B-Q03 | What theory and evidence support temporary liquidity or flow pressure followed by reversal, and how is pressure distinguished from information-driven price change? |
| B-Q04 | Under M2, which observable variables have been used for liquidity shocks, order imbalance, fund flows, fire sales, index/rebalance pressure, or constrained intermediation? |
| B-Q05 | What evidence supports temporary idiosyncratic relative dislocation and normalization after accounting for shared risks and identified information/flow channels? |
| B-Q06 | Is M3 independently identified in prior work, or is it typically a residual category vulnerable to circular labeling? |
| B-Q07 | What structural or fundamental changes produce persistent divergence and therefore support M0, rejection, ambiguity, or no trade? |
| B-Q08 | Which point-in-time variables have been used to discriminate information diffusion, liquidity/flow pressure, idiosyncratic displacement, and structural divergence? |
| B-Q09 | What competing mechanisms can produce the same observable dislocation, and what observable implications distinguish them? |
| B-Q10 | How do studies treat mixed mechanisms, uncertain classifications, non-resolution, censored outcomes, and abstention? |
| B-Q11 | Does mechanism conditioning improve resolution forecasts or economic decisions relative to mechanism-agnostic baselines, and is the evidence genuinely out of sample? |
| B-Q12 | What evidence links predictive improvement to implementable net value rather than gross return, post hoc storytelling, or selected cases? |
| B-Q13 | Which findings are market-structure-specific, and what limits transfer to A-share machinery stocks? |
| B-Q14 | What evidence would falsify each M1–M3 hypothesis or favor M0/no trade? |

### Required synthesis outputs

For each M0–M3: theory, supporting and contrary evidence, candidate observable families, temporal ordering, discriminating implications, confounds, boundary conditions, falsifiers, and Measurement Gaps. G1 must preserve an UNKNOWN/MIXED possibility even if reviewed papers force exhaustive labels.

## Adaptive literature workflow

### 1. Discovery

Purpose: build a broad candidate corpus and vocabulary, not support claims.

- Search each stream independently before cross-stream synthesis.
- Use scholarly databases, citation indexes, working-paper repositories, and backward/forward citation chaining approved in the search plan.
- Use concept blocks rather than one narrow query; record the exact query, platform, filters, timestamp, result count, and export hash.
- Prefer recent reviews and studies to map current terminology; retain older papers when foundational to a mechanism, construct, or method.
- Discovery metadata or abstracts may support triage only, never a substantive project claim.

### 2. Triage

For every candidate, record relevance to question IDs, study type, market/sample, apparent identification, point-in-time relevance, full-text availability, recency/foundational status, conflicts, and duplicate family.

Triage outcomes:

- **INCLUDE — LIGHT:** full text is available and the paper informs a mapped question.
- **INCLUDE — DEEP CANDIDATE:** potentially decision-changing, conflicting, foundational, unusually transferable, or central to a mechanism.
- **EXCLUDE:** record a reason; never silently discard.
- **PENDING FULL TEXT:** no claim use until lawful full text is obtained.

Venue or citation count may inform prioritization but cannot substitute for design quality or relevance.

### 3. Light review

Read full text selectively but sufficiently to capture exact claims, design, sample, timing, limitations, and usable evidence. Create claim-level records with page/section/table/figure locators. Do not infer support from abstracts.

### 4. Selective deep review

Deep review is triggered only when the paper is decision-relevant because it:

- could materially change a G1 synthesis or candidate construct;
- provides foundational theory or a canonical identification design;
- conflicts with credible evidence;
- supplies mechanism-discriminating observables or falsifiers;
- is unusually relevant to China/A-shares or transferability; or
- is necessary to resolve an ancestry or interpretation gap.

Deep review includes full design reconstruction, variable timing, identification assumptions, robustness/limitations, claim verification, and citation-chain checks. Deep reading stops once the decision-relevant claim is resolved or the source is judged non-informative; it is not performed for completeness alone.

## Search-plan architecture

Searches will be grouped into versioned concept blocks:

### Stream A blocks

1. company/product-market/business similarity;
2. supply-chain, customer, technology, ownership, and fundamental networks;
3. factor-exposure similarity and residual relationships;
4. correlation, cointegration, common trends, lead–lag, and dependence;
5. dynamic/stable relationships, breaks, decay, and regime dependence;
6. pairs trading/statistical arbitrage formation separated from execution;
7. point-in-time, survivorship, look-ahead, OOS, transfer, and generalization;
8. China/A-share/emerging-market context.

### Stream B blocks

1. information diffusion, limited attention, investor inattention, peer effects, lead–lag;
2. liquidity shocks, order imbalance, price pressure, flows, fire sales, rebalancing;
3. temporary mispricing, idiosyncratic shocks, relative-value normalization;
4. fundamental news, structural change, divergence, breaks, and non-convergence;
5. mechanism identification, competing explanations, mixtures, uncertainty, rejection;
6. observable proxies, causal timing, publication/availability lag;
7. resolution forecasting, abstention, no trade, decision value, and net profitability;
8. China/A-share market-structure transferability.

The executed protocol must specify approved databases, coverage dates, languages, document types, exact syntax translations, deduplication, update date, and stopping rules. None is selected by this design.

## Evidence standard

A substantive literature statement requires lawful full-text access and a claim-level record containing:

- stable bibliographic identifier and full citation;
- source version and immutable snapshot or content hash;
- access route, access date, and permitted-use boundary;
- exact page/section plus table/figure/equation when relevant;
- a concise paraphrased claim and claim type;
- study design, sample/market/period, temporal ordering, and identification basis;
- supporting result and material limitations or contrary evidence;
- mapped G1 question, M/P/S/C/R relevance, and transferability note;
- reviewer, review depth, extraction date, and ancestry links.

Abstracts, snippets, citation metadata, Observatory material, and secondary descriptions may locate sources but cannot support substantive claims.

## Permitted-use boundaries

Before extraction, record whether the source permits access, local retention, quotation, text mining, redistribution, and repository inclusion. Store only what is permitted. Prefer paraphrase; keep quotations minimal and locator-specific. Restricted full text must not be committed to the repository. Bibliographic facts and researcher-authored evidence notes remain separate from source files.

## Evidence ancestry

The ancestry chain is:

`Search run → Candidate record → Full-text source/version → Claim extraction → Synthesis statement → G1 decision or Measurement Gap`

Every link receives a stable ID. Corrections append a superseding record; prior records remain auditable. Synthesis tables must distinguish supportive, contrary, mixed, and absent evidence.

## Recency and foundations

Use a rolling recent-literature window to capture current constructs, data practices, and market evidence, with the exact cutoff decided in the approved search protocol. Add older work only when it is foundational, repeatedly antecedent to current claims, or necessary to understand identification. “Recent” and “foundational” are triage attributes, not quality judgments.

## G1 review and stopping rules

Before searching, the researcher must approve:

1. the evidence questions and whether any are missing or improperly downstream;
2. databases/source types and access constraints;
3. coverage windows, languages, and jurisdiction emphasis;
4. query-block translations and documentation format;
5. triage criteria and deep-review triggers;
6. permitted-use and repository-retention rules;
7. saturation and update stopping rules;
8. reviewer roles and disagreement resolution.

Stop and escalate if full text cannot be lawfully accessed for a decision-critical source; provenance cannot be reconstructed; a question requires choosing a G2/G3/G4 design; or source restrictions conflict with the planned artifact.

## Non-authorization statement

This document authorizes no search. No sources have been discovered, triaged, included, excluded, or reviewed. No literature conclusion, construct, factor, formula, mechanism label, measurement, model, pair, or empirical result is established.
