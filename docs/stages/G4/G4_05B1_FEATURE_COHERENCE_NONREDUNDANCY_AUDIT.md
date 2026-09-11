# G4-05B1 Feature Coherence and Non-Redundancy Audit

Status: **AUDIT ACCEPTED / INCORPORATED INTO G4-05B1 FREEZE — 2026-09-11**
Boundary: construct-level audit only. No empirical values, coverage distributions, outcomes, acquisition, feature computation, or candidate-set changes were used.

## Governing integrity rules

`construct != raw variable != pair transformation != model role`.

`re-expression of existing P0 information != incremental P1 information`.

A robustness variable is an alternative measurement of its construct. It does not enter the primary R2 vector beside the primary variable unless a separate, independently justified role is approved. A PIT-unqualified primary remains blocked or requires a versioned P1 enhancement; it is not replaced opportunistically by a convenient proxy.

## Seven-construct decision table

| Construct | Primary; robustness alternative | Exact economic construct | Authorized pair transformations | Authorized Feature Roles | P0/P1 and PIT readiness | Expected update | Principal overlap and audit assessment | Recommendation |
|---|---|---|---|---|---|---|---|---|
| Scale | total market capitalization; total assets | contemporaneous economic size/capacity of the firm, not leverage or valuation cheapness | i level, j level, signed difference, similarity, source-level interaction | company state; pair difference/similarity; slope conditioner | P1 when used as company-state increment; market cap `AVAILABLE WITH DOCUMENTED LIMITATION` through E02-B; assets `REQUIRES VERSIONED P1 ENHANCEMENT DATA` | market cap follows qualified market/share updates; assets only on new public reports | market cap overlaps valuation denominators; assets overlaps capital-structure denominators. The primary remains interpretable and pair-conditioning relevant if used as size, not price valuation. Do not include market cap and assets together as two scale measures in the primary vector. | `KEEP PRIMARY`; total assets `ROBUSTNESS ONLY` and `REQUIRES P1 ENHANCEMENT` |
| Profitability / quality | ROA; operating margin | operating efficiency/quality relative to resources or revenue | i level, j level, signed difference, similarity | company state; pair difference/similarity; intercept conditioner; rival context | P1; both `REQUIRES VERSIONED P1 ENHANCEMENT DATA` with first-public/vintage lineage | genuinely new filing only; carried state ages between releases | ROA shares an asset denominator with scale and may mechanically vary with leverage, but its numerator/estimand is operating performance. It is distinct if assets are not separately duplicated as a contemporaneous primary scale variable and denominator lineage is explicit. | `KEEP PRIMARY` and `REQUIRES P1 ENHANCEMENT`; operating margin `ROBUSTNESS ONLY` |
| Leverage / capital structure | liabilities/assets; debt/equity | financing structure and balance-sheet amplification, not firm scale | i level, j level, signed difference, absolute difference, source-level interaction | company state; pair mismatch; slope conditioner; rival context | P1; `REQUIRES VERSIONED P1 ENHANCEMENT DATA` | genuinely new filing/capital event only; carried state ages | shares assets/equity with scale and ROA denominators, but measures liability financing. Keep only one leverage ratio in the primary vector; do not interpret denominator overlap as independent evidence. | `KEEP PRIMARY` and `REQUIRES P1 ENHANCEMENT`; debt/equity `ROBUSTNESS ONLY` |
| Growth | revenue growth; operating-profit growth | realized operating trajectory available from reported company information | i level, j level, signed difference, similarity | company state; pair difference/similarity; intercept conditioner | P1; `REQUIRES VERSIONED P1 ENHANCEMENT DATA` | genuinely new filing only; base-period vintage travels with the feature | overlaps valuation only when valuation embeds price relative to earnings/book; realized revenue growth is not valuation. It remains distinct if no forward-looking or price-derived growth proxy is substituted. | `KEEP PRIMARY` and `REQUIRES P1 ENHANCEMENT`; profit growth `ROBUSTNESS ONLY` |
| Valuation | book-to-market; earnings yield | market price relative to PIT accounting fundamentals, not size, profitability, or standalone expected return | signed difference, absolute difference, similarity | relative company state; pair difference/similarity; bounded relationship conditioner | P1; `REQUIRES VERSIONED P1 ENHANCEMENT DATA`; market-cap component alone is only `AVAILABLE WITH DOCUMENTED LIMITATION` | price component may update with market observations, accounting denominator only with genuinely new public information; mixed-clock age preserved | mechanically reuses market cap from scale and book equity/earnings from other constructs. It is nonredundant only as an explicitly relative price-to-fundamental construct; component fields cannot also be counted as separate P1 increments under renamed transformations. | `KEEP PRIMARY` subject to overlap controls and `REQUIRES P1 ENHANCEMENT`; earnings yield `ROBUSTNESS ONLY` |
| Liquidity / trading structure | transaction amount; share volume | observable trading activity/friction state that may condition response transmission, not exogenous pressure or turnover/free float | i level, j level, signed difference, absolute difference, source-state interaction | company trading state; pair difference; slope conditioner; rival context | raw E02-A `AVAILABLE IN FROZEN CORE`; it is P0 if already used as shared/market control, and P1 only for a demonstrably distinct preregistered pair/company-state role | each qualified market observation; any historical state uses only prior available observations | direct overlap with frozen E02/P0 is the largest duplication risk. Renaming amount as a pair difference or interaction does not automatically create P1 information. The primary R2 P1 set may include it only if its role and estimand are absent from matched P0; otherwise it must remain P0 or be removed from P1 increment. | `KEEP PRIMARY` only under explicit P0 nonduplication; volume `ROBUSTNESS ONLY` |
| Business/subindustry structural information | dated C06 industry/subindustry code; directed business/exposure linkage | discrete/relational economic linkage and grouping context, not an ordinary scalar company characteristic | taxonomy-aware similarity; linkage-by-source-response only for separately qualified directed linkage | structural relationship context; pooling prior; pair similarity; slope conditioner; rival/rejection context | C06 is P0 `AVAILABLE WITH DOCUMENTED LIMITATION`; directed linkage is P1 `NOT CURRENTLY QUALIFIED` | C06 only on new published snapshot with carry-forward/age; directed linkage only on qualified dated disclosure | C06 membership is already P0 and cannot become P1 by encoding a match/distance. A directed business linkage would be genuinely distinct P1 information but is not a robustness measurement of C06 and lacks a qualified PIT source. | `STRUCTURAL CONTEXT`; directed linkage `NOT CURRENTLY QUALIFIED`, not a simultaneous robustness variable |

## Primary-variable assessment

| Construct | Interpretability | PIT/vintage feasibility | Non-redundancy | Pair-relationship relevance |
|---|---|---|---|---|
| Scale | high as firm size | limited for market-cap lineage; enhancement required for assets | acceptable with valuation/denominator controls | plausible for level/transmission conditioning |
| Profitability / quality | high | requires PIT fundamental vintage | distinct operating construct despite denominator overlap | plausible for economic linkage strength/state |
| Leverage / capital structure | high | requires PIT fundamental vintage | distinct financing construct if one ratio only | plausible for amplification/asymmetry |
| Growth | high | requires PIT fundamental and base-period vintages | distinct from valuation when based on reported operations | plausible for changing economic co-movement |
| Valuation | high only as relative price/fundamental state | requires synchronized market and PIT accounting vintages | conditionally distinct; strongest mechanical overlap after liquidity | plausible only as pair-relative conditioner, not standalone-return signal |
| Liquidity / trading structure | high for activity, not causal pressure | raw amount is core-available; state construction remains unfrozen | conditionally distinct; directly overlaps E02/P0 | plausible for response/friction conditioning only if matched P0 lacks the same role |
| Structural relationship | high as categorical/relational context | C06 qualified with limitations; directed linkage unqualified | C06 duplicates existing P0 by design; true directed linkage would be distinct | directly relevant to pair linkage and pooling, not ordinary covariate treatment |

## Cross-construct findings

1. **Scale versus assets/capital structure:** total assets is an alternative scale measure and a denominator elsewhere; liabilities/assets is the financing construct. Multiple denominator-based ratios do not create independent evidence merely by label.
2. **Profitability versus leverage:** ROA and liabilities/assets share assets but have different numerators and economic meanings. Preserve one primary per construct and expose common-denominator dependence.
3. **Growth versus valuation:** reported revenue growth describes realized operating trajectory; book-to-market describes price relative to book state. Forward-looking or price-derived growth proxies would blur the boundary and are not registered.
4. **Liquidity versus P0/E02:** transaction amount is already acquired E02-A information. It is incremental P1 only if a distinct company/pair conditioning role is absent from complete P0 and is explicitly matched; transformation alone is insufficient.
5. **Structural information versus C06:** dated C06 classification remains P0 structural context. Encoding it as similarity, dummy variables, or pooling groups does not convert it to P1. A separately sourced directed business linkage could be P1 but is currently unqualified.

## Structural relationship disposition

Business/subindustry/linkage information should remain `STRUCTURAL RELATIONSHIP CONTEXT`, separate from ordinary continuous company covariates. C06 may support taxonomy-aware pair context and later hierarchical pooling while retaining snapshot version, available time, age, and stale-gap state. A future directed business/exposure linkage may condition slopes or pooling only through a separately qualified P1 contract.

This preserves structural interpretation and prevents industry codes from being treated as numeric distances or repackaged as artificial P1 evidence.

## Researcher selections required

1. confirm market capitalization as the scale primary despite E02-B limitations, or mark scale unavailable pending P1 enhancement rather than substituting a proxy;
2. confirm ROA, liabilities/assets, revenue growth, and book-to-market as the four fundamental primaries;
3. decide whether transaction amount has a genuinely distinct R2-P1 role beyond complete P0; otherwise retain it as P0 only;
4. confirm C06 as structural P0 context and remove directed business linkage from “robustness alternative” treatment while leaving it unqualified P1;
5. decide which primary constructs form the eventual small R2 vector; this audit does not authorize all seven simultaneously;
6. keep every listed alternative robustness-only unless separately justified.

The researcher accepted the audit subject to the formal B1 dispositions: five core fundamental P1 constructs; existing E02 liquidity as P0; C06 as structural P0; and directed business linkage as unqualified, deferred P1.

`G4-05B1 FEATURE COHERENCE AUDIT ACCEPTED / INCORPORATED`
