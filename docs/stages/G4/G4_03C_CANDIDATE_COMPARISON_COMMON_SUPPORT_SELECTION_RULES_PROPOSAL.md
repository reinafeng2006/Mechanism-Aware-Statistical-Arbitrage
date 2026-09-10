# G4-03C Candidate Comparison, Common Support & Selection Rules Freeze

Status: **G4-03C APPROVED / FROZEN — 2026-09-10**
Boundary: protocol design only. No frozen-data inspection, statistic, candidate computation, target construction, or result access.

## Objective

Prespecify how competing candidates will be compared and how inner/outer evidence may influence selection without confusing sample support, measurement quality, and downstream performance.

## Exact support architectures

| Architecture | Native-support evaluation | Common-support evaluation | Pair/date rule | Candidate eligibility | Coverage/deployability | Unequal support |
|---|---|---|---|---|---|---|
| **CS0 — candidate-native support** | Primary: each candidate uses its own frozen candidate/pair/date eligibility mask | Not required for attribution | No forced intersection; candidate-native eligible pair-dates remain distinct | Fully preserved | Directly measurable and reportable | Preserved and exposed, but model and sample effects cannot be cleanly separated |
| **CS1 — common support** | Secondary coverage report only | Primary: intersect the eligible pair-date origins of the named candidates inside the same fold/comparison family | Exact preregistered pair/date intersection; no later origin shifting | Applied first, then intersected | Must report discarded native coverage separately | Eliminated inside the estimand, potentially concealing deployability loss |
| **CS2 — dual/stratified support** | Required for coverage, deployability, and practical-use evidence | Primary for attribution of candidate/model differences | Named candidate set and exact pair/date intersection frozen per comparison; optional strata must be preregistered | Preserved in native view and explicitly intersected in common view | Required alongside common-support attribution | Preserved and explained in native reporting; eliminated only within the common-support comparison |

Proposed governing principle:

`common-support evidence is primary for attribution of model/specification differences; native-support evidence is separately required for deployability, coverage and practical usefulness`.

`better native-support result != model superiority if sample support differs materially`.

`better common-support result != sufficient deployability`.

**Selected support architecture: CS2 — DUAL-SUPPORT ARCHITECTURE.** Common-support comparisons are primary for attribution; candidate-native results are separately mandatory for coverage, deployment, and practical usefulness. Common-support construction must apply frozen candidate-specific eligibility and temporal rules without recoding excluded observations.

## Comparison layers

Comparisons must remain dependency ordered:

1. structural eligibility and support reproduction;
2. relationship-level comparison, including N0/N1 and P0/P1 under their frozen fair-comparison rules;
3. abnormality representation comparison;
4. permitted M1/M2/M0/U measurement comparison, with M3 production blocked;
5. resolution-validation comparison under quarantined outcomes;
6. later decision/economic evaluation only after separate authorization.

Later-layer performance cannot retroactively establish an earlier construct.

## Exact selection-rule families

- **SR0 — constraint-first admissibility:** a non-compensatory gate. A candidate proceeds only if it satisfies frozen semantic validity, PIT, eligibility, lineage, minimum-support, and role-specific evidence-permission requirements. Superior downstream performance cannot compensate for failure.
- **SR1 — ordered hierarchical dominance:** among SR0-admissible candidates, apply a preregistered ordered sequence: (1) structural/validity admissibility; (2) incremental relationship or predictive quality on comparable support at the appropriate dependency layer; (3) temporal stability across outer folds; (4) native-support coverage/deployability; and (5) production/data complexity as a feasibility constraint or later tie-break. A candidate advances only under frozen dominance, adequacy, and tie rules.
- **SR2 — constrained multi-criterion rule:** among SR0-admissible candidates, apply a finite preregistered rule that permits explicit trade-offs among named criteria. SR2 is not permission for an arbitrary weighted composite; weights or compensating trade-offs require a specific ex-ante theoretical/statistical justification.

**Selected primary architecture: SR0 followed by SR1.** Use non-compensatory admissibility followed by hierarchical rule-based dominance. For SR0-admissible candidates, SR1 orders: incremental quality on comparable/common support; temporal robustness; native-support coverage/deployability; then production/data complexity and feasibility as a later discriminator or tie-break consideration. No arbitrary weighted composite is permitted.

SR1 is not required to produce a unique winner. Permitted dispositions are:

- **DOMINANT / ADVANCES**;
- **NON-DOMINATED / BOTH SURVIVE**;
- **INSUFFICIENT DIFFERENTIATION**;
- **FAILS ADMISSIBILITY**;
- **NO CANDIDATE ADVANCES**.

A candidate cannot be promoted merely because the process expects one winner. SR2 remains available only for specifically justified and preregistered trade-offs under separate authorization before relevant outcome inspection; it cannot become a generic weighted-score escape hatch when SR0/SR1 yields no preferred candidate.

## Inner and outer evidence governance

- Semiannual inner evidence may affect selection only through a rule frozen before access.
- OF4 outer folds evaluate the preregistered selection procedure; outer aggregation and consequences must be frozen before inspection.
- No manual revision after an outer fold may preserve uncontaminated status without reopening/versioning.
- TP3, CG1, CG0, OF3, OF6, and annual-inner structures are diagnostics or registered sensitivities only unless separately authorized in a bounded sensitivity budget.
- Final held-out evidence has no role until separately authorized.

### Inner aggregation semantics

Each semiannual inner origin generates one repeated pseudo-OOS evidence record for every eligible preregistered candidate tuple, including origin/fold identity, support basis, eligibility exclusions, and the later-authorized layer-specific estimands. Inner origins are repeated temporal evidence, not independent opportunities to hand-pick a winner.

`inner origins generate repeated pseudo-OOS evidence; they are not independent opportunities to hand-pick a winner`.

Later aggregation must be deterministic and frozen before development computation, preserve origin-level evidence, prevent one origin from being selected post hoc, and distinguish aggregate evidence from dispersion and failures. Exact statistics and weights remain unresolved.

### Outer aggregation semantics

Across annual OF4 folds 2020–2023, later aggregation must retain conceptually separate evidence for:

- aggregate magnitude;
- direction consistency;
- fold-to-fold dispersion;
- severe fold-specific failure;
- eligible native and common support.

`one exceptional outer fold must not automatically dominate the confirmation decision`.

The exact aggregate statistic, consistency rule, failure rule, weights, and confirmation consequence must be frozen before any outer result is inspected.

## Dependency-ordered multiplicity architecture

Testing families follow the frozen dependency graph rather than forming one global tournament:

`relationship validity / representation -> normal-relationship specification -> abnormality -> mechanism measurements -> resolution / predictive validation`.

An upstream candidate that fails a preregistered admissibility/adequacy gate does not generate unrestricted downstream families. Multiplicity records must distinguish:

1. **within-family multiplicity:** alternatives serving the same construct and comparison layer;
2. **across-stage multiplicity:** conditional propagation from an upstream surviving family into a downstream stage;
3. **sensitivity analyses:** preregistered robustness work outside primary winner selection;
4. **exploratory/reopened analyses:** separately labeled, versioned, and contamination-recorded work that cannot inherit confirmatory status.

Exact correction/control procedures and family definitions remain numerical/statistical decisions.

## Sensitivity budget boundary

OF3, OF6, annual inner origins, CG0, CG1, TP3 diagnostics, and other registered sensitivities remain outside the primary winner-selection loop unless explicitly authorized in a frozen sensitivity budget. Sensitivity evidence may challenge robustness but cannot be mined to rescue an unsuccessful primary specification or opportunistically replace the TP2/CG2/OF4 process.

## Required support reporting

Every comparison must preserve candidate/rule versions, native eligible counts, shared eligible counts, exclusion-reason distributions, temporal-fold support, and any loss caused by common-support restriction. No universal eligibility flag may be introduced.

## Preserved unresolved decisions

1. define CS2 native/common estimands and exact pair/date intersection implementation;
2. freeze relationship-, abnormality-, mechanism-, and resolution-layer metrics and adequacy criteria;
3. freeze inner-origin aggregate, dispersion, failure, tie, and stopping rules;
4. freeze OF4 magnitude, consistency, dispersion, severe-failure, support, and confirmation rules;
5. define within-family and across-stage multiple-comparison control across the representation-aware Search Budget;
6. define the explicit sensitivity-execution budget and permitted outputs;
7. define numerical dominance, insufficient-differentiation, and no-advance rules;
8. bind protocol versions and access logs before computation.

No metric, numerical threshold, candidate computation, sensitivity execution, or analysis is authorized here.

`G4-03C APPROVED / FROZEN`
