# G4-04 Statistical Governance Architecture Freeze

Status: **G4-04 APPROVED / FROZEN — 2026-09-10**
Boundary: pre-empirical protocol design only. No frozen-data inspection, descriptive statistic, candidate computation, target construction, or outcome access.

## Objective

Prespecify the finite metrics, aggregation semantics, admissibility/dominance thresholds, and dependency-ordered multiplicity controls needed to execute the frozen CS2 plus SR0-to-SR1 architecture without adapting rules after results.

## Decision Block A — Stage-specific estimands and metric families

`metric choice must follow the stage-specific estimand`.

No universal performance metric may rank every candidate family. Strategy return, Sharpe, PnL, or economic performance cannot select an upstream relationship or mechanism measurement unless a later stage explicitly authorizes that estimand.

| Research stage | Estimand | Bounded candidate metric families | What the stage cannot establish |
|---|---|---|---|
| Relationship representation / validity | quality and stability of the estimated signed conditional relationship on PIT support | OOS normal-response error; calibration/coverage of expected response; stability/break behavior; cross-pair generalization; eligible support | trading predictability or mechanism identity |
| Normal-relationship specification | incremental relationship-level quality of N0 versus N1 and P0 versus P1 under frozen fair comparison | comparable-support error/calibration; uncertainty quality; parameter/state stability; sparse-history behavior; generalization | final economic superiority; N2 authorization without its frozen escalation evidence |
| Abnormality measurement | whether the representation faithfully expresses unusual departure relative to normality and uncertainty | morphology preservation; calibration/ranking quality; false-abnormality behavior; relationship-break separation; support | M0/M1/M2/M3 identity or a trade |
| M1/M2 mechanism evidence | permitted incremental evidentiary/discrimination content under PIT rival and contamination boundaries | discrimination/calibration where targets are later authorized; rival sensitivity; uncertainty; temporal consistency; coverage | hard causal identification from response gap, excess move, volume, turnover, or flow proxy alone |
| Resolution/predictive validation | later direction, magnitude, timing, persistence, and non-resolution conditional on frozen event-time information | proper predictive loss/calibration; directional/magnitude/timing error; coverage; temporal stability | retroactive event-time mechanism identification |
| Later economic validation | net implementable economic consequences under separately frozen decision and cost rules | return/risk/cost/capacity/implementation families | retroactive proof of relationship validity or mechanism measurement quality |

Every metric must identify its construct, estimand, support basis, direction, failure interpretation, temporal aggregation role, multiplicity family, and permitted selection use. Final PnL cannot be the first criterion for upstream constructs.

### Effect size, uncertainty, significance, and time

Every later candidate comparison must report separately:

- effect magnitude relative to the stage-specific estimand;
- uncertainty around that magnitude;
- statistical-significance evidence where a valid inferential design exists;
- temporal consistency and dispersion across authorized origins/folds;
- eligible common and native support.

`statistical significance alone is neither necessary nor sufficient for candidate advancement`.

A stage/metric-specific minimum meaningful effect may be required, but it must be frozen before the corresponding outcome is inspected. There is no universal percentage-improvement threshold.

## Decision Block B — CS2 aggregation

Prespecify:

- exact candidate-native estimands for coverage/deployability;
- exact common pair/date intersection per named comparison family and fold;
- common-support estimands for attribution;
- minimum reportable support and support-loss disclosures;
- inner-origin aggregation across semiannual repeated pseudo-OOS evidence;
- OF4 aggregation preserving magnitude, direction consistency, dispersion, severe failure, and support;
- treatment of non-comparable or insufficient-support comparisons.

No aggregation statistic or weighting rule is selected here.

### Inner aggregation alternatives

Semiannual inner-origin evidence must remain a vector rather than an automatic winner-producing average. Bounded aggregation dimensions are:

- central tendency across origins;
- direction/adequacy consistency;
- origin-to-origin dispersion;
- native/common eligible support;
- severe origin-specific failure.

Possible later rules include a hierarchical vector rule, a non-compensatory adequacy-plus-stability rule, or a jointly reported vector with no forced ranking. A compensatory scalar is not proposed.

### Outer aggregation alternatives

OF4 evidence is a multidimensional confirmation vector:

`{magnitude, directional consistency, fold dispersion, severe fold-specific failure, eligible support}`.

Permitted candidate aggregation concepts are a hierarchical vector rule, a dominance/partial-order rule, or a thresholded adequacy-and-stability rule. No weighted compensatory scalar is proposed because it could conceal severe instability.

`strong performance in one outer fold cannot automatically compensate for severe instability elsewhere`.

## Decision Block C — SR0/SR1 numerical semantics

### SR0 — structural/admissibility thresholds only

SR0 contains non-compensatory requirements whose failure invalidates a candidate for the named use: semantic fit; evidence permission; PIT/lineage integrity; candidate-specific eligibility; minimum authorized estimation/support contract; prohibited leakage; required data/feasibility status; and mechanism-specific identification boundaries. Weak empirical performance is not an SR0 structural failure.

### SR1 — meaningful improvement and temporal robustness

For candidates passing SR0, later preregistered rules must combine stage-specific meaningful effect, uncertainty, common-support incremental quality, temporal robustness, native deployability, and finally complexity/feasibility without forcing a scalar score.

The frozen dispositions map conceptually as follows:

| Disposition | Required later semantics |
|---|---|
| **DOMINANT / ADVANCES** | clears SR0; meets the meaningful-effect/uncertainty rule on comparable support; satisfies temporal/failure requirements; is not dominated on later coverage/feasibility criteria |
| **NON-DOMINATED / BOTH SURVIVE** | multiple admissible candidates retain material, non-comparable advantages and none dominates under the hierarchy |
| **INSUFFICIENT DIFFERENTIATION** | admissible candidates cannot be distinguished at the frozen meaningful-effect/uncertainty resolution |
| **FAILS ADMISSIBILITY** | a genuine SR0 structural/use requirement fails, irrespective of performance |
| **NO CANDIDATE ADVANCES** | no admissible candidate satisfies the frozen SR1 adequacy/robustness requirements |

Numerical effect, uncertainty, adequacy, instability, severe-failure, and support thresholds remain unresolved.

Translate frozen semantic outcomes into preregistered rules:

- SR0 admissibility failures;
- adequate versus inadequate incremental quality;
- hierarchical dominance and non-dominance;
- insufficient differentiation;
- severe-fold failure;
- no-candidate-advances;
- complexity/feasibility tie-break eligibility;
- stopping and pruning without forced winners.

Thresholds may be statistical, practical, or both, but must be construct-specific, finite, justified, and frozen before relevant access. An arbitrary global score is prohibited.

## Decision Block D — Dependency-ordered multiplicity

Define families and control separately for:

- within-family candidate comparisons;
- conditional across-stage propagation;
- repeated inner origins and OF4 outer folds;
- registered sensitivities outside primary selection;
- reopened/exploratory analyses with contamination status.

Upstream failure cannot create unrestricted downstream tests. Family boundaries, correction/control methods, alpha/error budgets if used, and reporting of all attempted comparisons remain unresolved.

### Multiplicity alternatives

| Alternative | Appropriate role | Principal trade-off |
|---|---|---|
| Family-wise error control | small, high-stakes confirmatory families or final confirmatory claims | strongest false-positive protection; lower power |
| FDR-style control | broader preregistered within-stage screening families where a controlled proportion of false discoveries is meaningful | more power; does not provide claim-wise confirmatory protection |
| Hierarchical/gated testing | dependency graph from relationship through resolution | prevents failed upstream branches from spawning unrestricted downstream families; requires gates and error allocation fixed ex ante |
| Exploratory descriptive reporting | reopened or hypothesis-generating work | cannot support confirmatory advancement and requires explicit exploratory/contamination status |

**Recommended architecture:** hierarchical/gated stage progression, with correction applied inside each preregistered comparison family. Reserve stronger family-wise control for a small number of final confirmatory claims; permit FDR-style control only for suitable broader preregistered screening families; keep exploratory work outside confirmatory claims.

`multiplicity control should operate within preregistered comparison families under hierarchical stage gates rather than as one global all-project tournament`.

The same correction method need not govern every stage, but the method and claim role for each family must be frozen before inspection.

## Decision Block E — Sensitivity budget

Proposed three-tier structure, not yet frozen:

- **Mandatory bounded robustness:** one coherent lower-complexity TP1/CG1 walk-forward bundle, if approved, testing whether primary conclusions require TP2/CG2 complexity. It is one registered bundle, not a Cartesian set of components.
- **Optional diagnostics/sensitivities:** TP3 heterogeneity reporting; TP0/CG0 expanding/fixed baseline views; OF3/OF6 fold-count sensitivities; annual inner-origin sensitivity. Each requires explicit authorization within a finite budget and cannot enter primary selection.
- **Explicit reopening required:** any new date boundary, history/window, origin cadence, candidate, metric, threshold, regime definition, or unregistered combination added after inspection; any SR2 trade-off not authorized ex ante.

Sensitivity evidence may challenge robustness and change the claim's robustness status, but cannot rescue or select an otherwise unsuccessful primary candidate. Exact mandatory execution scope, optional count, output access, and consequences remain unresolved.

## Search Budget and versioning

The metric, threshold, aggregation, and multiplicity menus are part of the Search Budget. Every authorized tuple must be finite, preregistered, versioned, and bound to dataset, eligibility, calendar, candidate, target, and code versions before computation. Outcome-driven additions require reopening and contamination records.

## Preserved unresolved numerical decisions

1. choose exact stage-specific metric sets and their estimands/directions;
2. choose stage-specific minimum meaningful effects and uncertainty treatment;
3. freeze CS2 pair/date intersection, native/common estimands, and minimum reportable support;
4. choose inner central-tendency, consistency, dispersion, support, and severe-failure statistics/rules;
5. choose OF4 magnitude, directional-consistency, dispersion, severe-failure, and support statistics/rules;
6. choose numerical SR0 support/feasibility cutoffs that genuinely govern admissibility;
7. choose numerical SR1 meaningful-effect, uncertainty, dominance, tie, instability, and no-advance rules;
8. define comparison-family boundaries and choose FWER/FDR/other within-family procedures and any error budgets;
9. freeze the mandatory and optional sensitivity-execution budget;
10. freeze stopping, reopening, contamination, manifests, hashes, and access rules.

No exact metric, numerical threshold, alpha/q level, aggregation statistic, failure cutoff, sensitivity execution count, or analysis is selected or authorized here.

`G4-04 APPROVED / FROZEN`
