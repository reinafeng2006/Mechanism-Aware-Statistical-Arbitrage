# G4-03C Candidate Comparison, Common Support & Selection Rules Proposal

Status: **PROPOSED / AWAITING RESEARCHER REVIEW**
Boundary: protocol design only. No frozen-data inspection, statistic, candidate computation, target construction, or result access.

## Objective

Prespecify how competing candidates will be compared and how inner/outer evidence may influence selection without confusing sample support, measurement quality, and downstream performance.

## Support architectures preserved for decision

- **CS0 — candidate-native support:** each candidate is evaluated on its own frozen eligibility mask, with support differences fully reported;
- **CS1 — common support:** named candidates are compared only on shared eligible security-date/pair-date origins;
- **CS2 — dual/stratified support:** report both native and common support, plus only preregistered support strata.

No support architecture is selected here. A candidate cannot gain apparent superiority through hidden sample differences, and common support cannot silently become the only estimand if it removes material native coverage.

## Comparison layers

Comparisons must remain dependency ordered:

1. structural eligibility and support reproduction;
2. relationship-level comparison, including N0/N1 and P0/P1 under their frozen fair-comparison rules;
3. abnormality representation comparison;
4. permitted M1/M2/M0/U measurement comparison, with M3 production blocked;
5. resolution-validation comparison under quarantined outcomes;
6. later decision/economic evaluation only after separate authorization.

Later-layer performance cannot retroactively establish an earlier construct.

## Candidate selection-rule families

- **SR0 — constraint-first admissibility:** candidates must first satisfy semantic, PIT, eligibility, lineage, and minimum-support contracts;
- **SR1 — prespecified metric hierarchy:** eligible candidates are compared through a frozen ordered metric/estimand sequence rather than an unconstrained composite score;
- **SR2 — constrained multi-criterion rule:** a frozen finite rule permits explicit trade-offs among named relationship-level or measurement-level criteria without using final PnL as the first criterion.

These are candidate rule families only. Metrics, priorities, tolerances, aggregation, tie handling, and stopping decisions remain unresolved.

## Inner and outer evidence governance

- Semiannual inner evidence may affect selection only through a rule frozen before access.
- OF4 outer folds evaluate the preregistered selection procedure; outer aggregation and consequences must be frozen before inspection.
- No manual revision after an outer fold may preserve uncontaminated status without reopening/versioning.
- TP3, CG1, CG0, OF3, OF6, and annual-inner structures are diagnostics or registered sensitivities only unless separately authorized in a bounded sensitivity budget.
- Final held-out evidence has no role until separately authorized.

## Required support reporting

Every comparison must preserve candidate/rule versions, native eligible counts, shared eligible counts, exclusion-reason distributions, temporal-fold support, and any loss caused by common-support restriction. No universal eligibility flag may be introduced.

## Unresolved researcher decisions

1. select CS0, CS1, or CS2 and define its estimands;
2. choose SR0/SR1/SR2 structure or a bounded combination;
3. freeze relationship-, abnormality-, mechanism-, and resolution-layer metrics;
4. freeze inner-origin aggregation, tie handling, adequacy, and stopping rules;
5. freeze OF4 outer aggregation and selection/confirmation consequences;
6. define multiple-comparison control across the representation-aware Search Budget;
7. define the explicit sensitivity-execution budget;
8. define failure, no-winner, reopening, and contamination states;
9. bind protocol versions and access logs before computation.

No candidate, metric, selection rule, support architecture, or analysis is authorized here.

`G4-03C CANDIDATE COMPARISON PROPOSED / AWAITING RESEARCHER REVIEW`
