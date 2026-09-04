# Research Knowledge Map

This catalog is a Learning Layer artifact. Definitions explain standard concepts; they do not select models or supply evidence. Project-specific status is limited to frozen G0 decisions and completed audited G1-02 Pair Formation reviews.

## Defined concepts / models

| Concept / model | Standard definition and core form | Project status | Ancestry |
|---|---|---|---|
| Company / economic proximity | Similarity of contemporaneously available company or product-market descriptions. A generic text similarity can be written `sim(i,j) = cosine(x_i,x_j)`, where `x` is a dated company representation. | **DEFINED**; candidate information family only. | PF-001; CL-PF-001 |
| Raw price-path distance | Distance between common-scale historical price paths: `D(i,j)=sum_t (P_i,t-P_j,t)^2`; `P` is normalized price, unitless after scaling. | **DEFINED**; candidate relationship representation. | PF-004; CL-PF-002 |
| Return correlation | Linear co-movement of returns: `corr(r_i,r_j)=cov(r_i,r_j)/(sd(r_i)sd(r_j))`; returns are dimensionless rates. | **DEFINED**; candidate representation. | PF-005; CL-PF-009 |
| Cointegration | Non-stationary prices may have a stationary linear combination: `z_t=p_i,t-beta p_j,t`; `z_t` is a price-level spread in the chosen scale. | **DEFINED**; candidate representation. | PF-005, PF-006; CL-PF-004, CL-PF-009 |
| Factor-adjusted / residual dependence | A specified control model `r_i,t=B_i f_t+e_i,t`; `e` is what that model leaves unexplained. | **DEFINED**; candidate representation. | PF-008, PF-013; CL-PF-003, CL-PF-006 |
| Relationship stability / break | A statistical description of persistence or change in a specified relationship over time. | **DEFINED**; candidate R / rejection information. | PF-006, PF-007; CL-PF-004, CL-PF-005 |
| False discovery rate (FDR) | `E[V/max(R,1)]`, where `R` is number of rejections and `V` erroneous rejections. Unit: expected proportion. | **DEFINED**; candidate statistical governance. | PF-013; CL-PF-006 |
| Global matching / overlap control | A portfolio-level selection constraint; for example choose weighted edges with each asset used at most once. | **DEFINED**; candidate portfolio governance. | PF-010; CL-PF-010 |
| M1 source–link–timing chain | A directional PIT link, identified source public event, coherent direction and contemporaneous peer under-response jointly support a candidate delayed-incorporation interpretation. | **PARTIALLY ANSWERED**; candidate P/C/R construct family only. | M1-001, M1-008; CL-M1-001, CL-M1-003 |
| Event-time provenance vs outcome validation | Inputs available by the decision time are distinct from later peer response used only to evaluate the prediction. | **DEFINED** timing boundary; candidate measurement family. | M1-001, M1-008; CL-M1-001, CL-M1-003 |

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

No mechanism classifier, abnormal-state formula, resolution-prediction model, factor list, pair score, threshold, or trading rule is authorized.

## Seven-stage status

| Pipeline stage | Knowledge status | Expected resolver |
|---|---|---|
| Company Representation | **PARTIALLY ANSWERED** | G2 Measurement & Timing |
| Pair Formation | **PARTIALLY ANSWERED** | G2 Measurement & Timing |
| Normal Relationship | **PARTIALLY ANSWERED** | G2 Measurement & Timing |
| Abnormal Relative State | **NOT YET STUDIED** | G1 mechanism evidence, then G2 |
| Mechanism Identification | **PARTIALLY ANSWERED for M1 only** | G1 evidence review / G2 |
| Resolution Prediction | **NOT YET STUDIED** | G1 evidence review / G2–G4 |
| Trade / No Trade | **NOT YET STUDIED** | G4–G9 |
