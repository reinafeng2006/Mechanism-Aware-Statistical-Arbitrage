# Research Knowledge Map

This catalog is a Learning Layer artifact. Definitions explain standard concepts; they do not select models or supply evidence. Project-specific status is limited to frozen G0 decisions and completed audited G1-02 Pair Formation reviews.

## First-class views

- **Research Stage Map:** where the whole project currently stands.
- **Mechanism & Signal Map:** how M0–M3 and epistemic U connect relationship, abnormality, sequential PIT evidence, resolution validation and possible future decisions. See `MECHANISM_SIGNAL_MAP.md`.
- **Signal Model Registry:** cross-mechanism traceability for signal concepts and candidate measurements. See `SIGNAL_MODEL_REGISTRY.md`.
- **Concepts / Models** and **Papers:** supporting drill-down views; neither is an evidence source.

The five mechanism/state drill-down artifacts are under `mechanisms/`. Signal concept, candidate measurement, frozen factor, model output and trade rule remain distinct.

**Transition status:** G1-04 and the G2 Handoff Contract are **APPROVED / FROZEN — 2026-09-04**. G2 is **ACTIVE — INITIALIZATION / DESIGN ONLY** at its first checkpoint; eleven dependency-ordered decisions remain unresolved. Authorization permits study and operational design for continuous, uncertain sequential belief updating; it does not select a formula, model, threshold, factor or mandatory M0–M3 classifier.

**Frozen prerequisite:** G2-01 relationship semantics are **APPROVED / FROZEN — 2026-09-04**. The frozen semantic framework combines a joint conditional distribution view with separate `i → j` and `j → i` response views. It permits signed, asymmetric, pair-specific and state-dependent relationships; distinguishes relationship state, relationship uncertainty, temporary abnormality, and relationship change/break; and imposes a PIT anti-circularity boundary. All mathematical notation is illustrative; no estimator is selected.

**G2-02:** **APPROVED / FROZEN — 2026-09-04.** P0 is the primary, simpler PIT Market-Relationship-Only architecture with raw joint/co-movement, factor/exposure, conditional/residual, stability/breakdown and signed/asymmetric/state-dependent families kept distinct rather than combined into a Pair Score. P1 is unchanged P0 plus a separate secondary Economic/Company Relationship layer. Slow P1 information normally remains cached relationship context; newly arriving company events require separate later authorization as timestamped discriminator/rejection evidence. P1 requires incremental normal-relationship-level value under the same protocol; superior downstream prediction or PnL alone is insufficient. No representation, metric or winner is selected.

**G2-03:** **APPROVED / FROZEN — 2026-09-04.** N0 and N1 target the same G2-01 normal-relationship object. N0 is Industry-Structured / Strongly Pooled without requiring identical pair parameters; N1 permits substantially greater pair-specific PIT parameterization. Differences are limited to pooling strength, parameter sharing, heterogeneity accommodation, information borrowing, sparse-history behavior and adaptation scope. N2 remains **ILLUSTRATIVE / UNAUTHORIZED** pending specific relationship-level evidence that N0/N1 cannot adequately address. Pooling strength may differ across industries; no Industry Homogeneity Score is defined. PnL is not the primary selection criterion.

**G2-04:** **APPROVED / FROZEN — 2026-09-04.** Pair-specific abnormality is the potentially multidimensional departure of current Observed Joint Response from current Expected Conditional Joint Response, conceptually accounting for Relationship Uncertainty. Multidimensional Abnormality State is primary. Magnitude, signed direction, timing and conditional/residual deviation remain candidate morphology families; relationship-change/break evidence is a parallel diagnostic rather than temporary abnormality. A scalar/low-dimensional Continuous Abnormality Summary is optional and subordinate. Trigger/probability interpretation and every measurement choice remain unresolved. Abnormality is a common pre-mechanism state and identifies neither M0–M3/U nor a trade.

**G2-05:** **APPROVED / FROZEN — 2026-09-04; G2-06 NOT AUTHORIZED.** Trigger, Mechanism Discriminator, Sequential-Updating and Rejection/Rival Evidence are information roles rather than fixed variable types. `variable identity ≠ signal role`; each use is bound to a construct, hypothesis, decision time and PIT availability. Slow prior/context, medium relationship state, fast abnormality/market evidence and fast sequential updates remain distinct. Contemporaneous input, genuinely new sequential information and outcome-only validation remain separated. Independent Production Feasibility distinguishes research usefulness from production suitability using `EASY / CORE-CANDIDATE`, `MODERATE`, `HARD / OPTIONAL` and `UNAVAILABLE / RESEARCH-ONLY`; harder variables require role-relevant incremental value. No specific variable is rated and no activation approach, factor, formula, weight, update rule or model is selected.

## Defined concepts / models

| Concept / model | Standard definition and core form | Project status | Ancestry |
|---|---|---|---|
| Company / economic proximity | Similarity of contemporaneously available company or product-market descriptions. A generic text similarity can be written `sim(i,j) = cosine(x_i,x_j)`, where `x` is a dated company representation. | **DEFINED; CANDIDATE SECONDARY PRIOR; NOT CORE; INCLUSION REQUIRES INCREMENTAL VALIDATION.** | PF-001; CL-PF-001 |
| Raw price-path distance | Distance between common-scale historical price paths: `D(i,j)=sum_t (P_i,t-P_j,t)^2`; `P` is normalized price, unitless after scaling. | **DEFINED**; candidate relationship representation. | PF-004; CL-PF-002 |
| Return correlation | Linear co-movement of returns: `corr(r_i,r_j)=cov(r_i,r_j)/(sd(r_i)sd(r_j))`; returns are dimensionless rates. | **DEFINED**; candidate representation. | PF-005; CL-PF-009 |
| Cointegration | Non-stationary prices may have a stationary linear combination: `z_t=p_i,t-beta p_j,t`; `z_t` is a price-level spread in the chosen scale. | **DEFINED**; candidate representation. | PF-005, PF-006; CL-PF-004, CL-PF-009 |
| Factor-adjusted / residual dependence | A specified control model `r_i,t=B_i f_t+e_i,t`; `e` is what that model leaves unexplained. | **DEFINED**; candidate representation. | PF-008, PF-013; CL-PF-003, CL-PF-006 |
| Relationship stability / break | A statistical description of persistence or change in a specified relationship over time. | **DEFINED**; candidate R / rejection information. | PF-006, PF-007; CL-PF-004, CL-PF-005 |
| Conditional joint/response relationship | The frozen semantic framework for PIT expected joint behavior, bidirectional signed responses and uncertainty conditional on available information. Illustrative only: `R_t={JointLaw(Y_i,Y_j|I_t), Response(j|i,I_t), Response(i|j,I_t), Uncertainty_t}`. | **FROZEN SEMANTICS**; no distribution or estimator selected. | D-017; G2-01 freeze; G1 frozen Claim ancestry |
| Relationship state vs uncertainty vs abnormality vs break | State is current normal conditional behavior; uncertainty is how imprecisely it is known; abnormality is an unusual observation conditional on that reference; break is evidence that the reference itself changed. | **FROZEN SEMANTICS**; operational measurement deferred. | G2-01 freeze; CL-PF-004/005 |
| False discovery rate (FDR) | `E[V/max(R,1)]`, where `R` is number of rejections and `V` erroneous rejections. Unit: expected proportion. | **DEFINED**; candidate statistical governance. | PF-013; CL-PF-006 |
| Global matching / overlap control | A portfolio-level selection constraint; for example choose weighted edges with each asset used at most once. | **DEFINED**; candidate portfolio governance. | PF-010; CL-PF-010 |
| M1 source–link–timing chain | A directional PIT link, identified source public event, coherent direction and contemporaneous peer under-response jointly support a candidate delayed-incorporation interpretation. | **PARTIALLY ANSWERED**; candidate P/C/R construct family only. | M1-001, M1-008; CL-M1-001, CL-M1-003 |
| Event-time provenance vs outcome validation | Inputs available by the decision time are distinct from later peer response used only to evaluate the prediction. | **DEFINED** timing boundary; candidate measurement family. | M1-001, M1-008; CL-M1-001, CL-M1-003 |
| M2 pressure-source / contamination boundary | Temporary pressure requires source, liquidity-state and rival checks; standard flow proxy can embed realized return. | **PARTIALLY ANSWERED**; candidate C/R construct family only. | M2-001–005, B4-004; CL-M2-001–004, CL-B4-002 |

Each definition measures its stated statistical or economic construct only. None establishes economic/trading validity, and none is **FROZEN** as the project model.

## Candidate / unresolved models

All formulas below are **ILLUSTRATIVE / NOT AUTHORIZED**. They communicate possible model families, not project specifications.

| Candidate | Illustrative form | Motivation / open decision |
|---|---|---|
| Company representation | `x_i,t = g(disclosures available by t)` | Economic similarity has literature ancestry; G2 must define inputs, timing, representation, and validation. |
| Pair construction | `select pairs = h(similarity, dependence, stability, governance)` | Components are distinct and must not be silently merged into a Pair Score. G2 must decide whether/how each is measured and validated. |
| Normal relationship | raw distance, `corr(r_i,r_j)`, `p_i-beta p_j`, or residual `e_i-e_j` | Literature does not establish a generally dominant representation. G2 must retain candidates and test them internally. |
| Stability rejection | `reject if break_risk(i,j,t) is high` | Breaks support a candidate rejection construct, not a threshold, method, or M0 interpretation. |
| Statistical screening | `control FDR among tested relationships` | Controls statistical false discoveries under assumptions; G2 must decide testing family, assumptions and PIT process. |
| M1 candidate interpretation | `candidate_M1 = h(link, source, timing, underresponse, rival_checks)` | **ILLUSTRATIVE / NOT AUTHORIZED**. Completed evidence motivates components, but not a causal attention label, formula or threshold. |
| N0 — Industry-Uniform Normality Baseline | common industry schema / relationship semantics, with stronger pooling | **CANDIDATE / NOT SELECTED**. Deliberately simple benchmark; no universal pair parameter assumed. |
| N1 — Pair-Specific Normality Candidate | same construct as N0, estimated from the pair's own PIT history | **CANDIDATE / NOT SELECTED**. Must be compared fairly with N0. |
| N2 — Hierarchical / Partial-Pooling Normality | `pair relationship = industry prior + pair-specific adjustment` | **ILLUSTRATIVE / UNAUTHORIZED** later-complexity candidate only. |
| Continuous Pair-Specific Abnormality | degree of departure from estimated pair normal joint behavior and uncertainty | **CANDIDATE / NOT SELECTED**. Not a binary trigger. |
| P0 — Market-Relationship-Only Pair Model | prespecified PIT market/statistical relationship information only | **CANDIDATE / NOT SELECTED**. Primary formal-pair-validity comparator. |
| P1 — Market Relationship + Company/Economic Proximity | P0 plus proximity in a specified secondary role | **CANDIDATE / NOT SELECTED**. Requires incremental relationship-level OOS value beyond P0. |

No mechanism classifier, abnormal-state formula, resolution-prediction model, factor list, pair score, threshold, or trading rule is authorized.

## Active sequential architecture status

The active architecture has five displayed elements: sequential mechanism tracking and dynamic resolution prediction are deliberately coupled into one element. The original seven-stage G0 map remains a preserved historical record, not the current operating map.

| Pipeline stage | Knowledge status | Expected resolver |
|---|---|---|
| Company Representation | **PARTIALLY ANSWERED** | G2 Measurement & Timing |
| Pair Relationship Prior | **PARTIALLY ANSWERED** | G2 Measurement & Timing |
| Pair-Specific Normal Relationship | **UNRESOLVED DESIGN REQUIREMENT RECORDED** | G2 Measurement & Timing |
| Continuous Pair-Specific Abnormality | **UNRESOLVED DESIGN REQUIREMENT RECORDED** | G2 Measurement & Timing |
| Sequential Mechanism Tracking + Dynamic Resolution Prediction | **PARTIALLY ANSWERED for M1 evidence boundaries only** | G1 evidence review / G2–G4 |
| Trade / Update / Reject / Abstain | **NOT YET STUDIED** | G4–G9 |

### Sequential Mechanism Tracking + Dynamic Resolution Prediction: M1 detail

**What is answered / defined.** Completed M1 reviews establish that lead-lag alone is not M1. A candidate delayed-incorporation interpretation needs a PIT directional economic link, an identified and time-stamped public source event/response, economically coherent direction, peer under-response by the decision time, and rival/leakage checks. Event-time provenance is conceptually distinct from a later peer response used only as validation.

**Defined concepts/models.** The source–link–timing chain and the event-time-versus-outcome boundary are **DEFINED** concepts. Their logical representation is `link → source event → peer under-response → candidate M1 → later validation`; it is not a fitted model or standard statistical formula.

**Candidate / unfrozen idea.** `candidate_M1 = h(link, source, timing, underresponse, rival_checks)` and `belief_(t+1) = update(belief_t, new_PIT_evidence_(t+1))` are **ILLUSTRATIVE / NOT AUTHORIZED**. They are component/checklist forms, not a Bayesian filter, HMM, state-space model, classifier, factor score, formula, threshold or M1 label.

**Potential additional candidate observables.** PIT link vintage/effective date and materiality; source identity, content/sentiment and first-public timestamp; source/peer response through decision time; peer own-news; market/industry context; pre-event peer movement; and common-ownership/trading context only where its reporting lag permits. These have differing roles and are not an approved factor list.

**Deferred decisions.** G2 must define operational measurement, first-public versus effective-information timing, frequency, link/event lineage, peer-under-response and abstention/rejection rules. Later internal validation (G4 onward) must test future catch-up without leakage and test competing explanations: private/pre-release diffusion, common shocks, peer own news, risk, liquidity, stale/mismeasured links and news endogeneity. Individual causal attention state, A-share transferability and M2/M3/M0 multi-mechanism discrimination remain unresolved.

### M2 detail

M2 evidence can update belief only through pressure-source provenance, market/liquidity-state context, abnormal price/flow response and rival-information checks. Generic flow, turnover, volume, illiquidity and later reversal do not identify M2 alone. Permanent/transitory decomposition is model conditional. M1 concerns peer under-response after source information; M2 concerns possible source over-movement under pressure. G2 must define PIT pressure-source lineage, contamination checks, liquidity/quote/trade timing and the boundary between event-time inputs and later normalization validation. No model family is selected.

### Normal relationship and abnormality requirement

Industry information supplies economically meaningful dimensions and relationship semantics; pair PIT history supplies the pair's actual normal relationship. N0 and N1 are competing candidates under the same prespecified construct, information set, timing and validation protocol. N2 is reserved only for a later demonstrated bias–variance or sample-efficiency problem. Abnormality is a continuous pair-specific departure candidate that can include magnitude, direction, timing, residual and break dimensions; formula, uncertainty and trigger/probability treatment are unresolved. Relationship-level evaluation precedes strategy PnL. See `docs/decisions/G2_NORMAL_RELATIONSHIP_REQUIREMENT.md`.

### Company/economic proximity role

PIT market relationship evidence is the primary basis for formal pair validity. Company/economic proximity is a secondary candidate prior/context variable—not a default core input—and may remain only if P1 adds prespecified OOS relationship-level value beyond P0. It can be considered as a prior, regularizer, tie-breaker, context, rejection/structural-change evidence or sparse-history aid. PF-001 still establishes only economic/product-market proximity.

### Signed conditional relationships

Pair validity need not imply positive or same-direction movement. The future G2 object is observed joint response versus expected signed conditional joint response; only a departure is candidate abnormality. Positive, negative, asymmetric and state-dependent relations are admissible candidates. Opposite direction alone is neither abnormal nor M3. This is **ILLUSTRATIVE / UNAUTHORIZED** and does not select a representation or estimator.
