# G4-03B Temporal Validation Architecture Freeze

Status: **G4-03B APPROVED / FROZEN — 2026-09-10**
Boundary: architecture selection proposal only. No frozen-data inspection, statistic, measurement, target construction, or development access.

## Objective

Select the temporal-validation structure that will govern later development while preserving chronological information boundaries, dynamic-relationship assessment, selection separation, and a sealed final held-out evaluation. Exact dates, origin spacing, purge/embargo lengths, aggregation rules, and access authorization remain unresolved.

## TP0-TP3 comparison

| Candidate | Dynamic relationship stability | OOS robustness and selection control | Complexity/history burden | Proposed disposition |
|---|---|---|---|---|
| TP0 — single chronological development / sealed held-out | Weak: one development split gives limited evidence across relationship states | Weak-to-moderate: preserves a holdout but is sensitive to one development period | Lowest | Do not select as the primary architecture; retain only as a transparent sensitivity baseline |
| TP1 — rolling-origin development validation / sealed held-out | Strong: repeated chronological origins expose temporal variation | Strong if candidate menus, overlap controls, and aggregation are frozen | Moderate | Retain as the lower-complexity competing architecture |
| TP2 — nested temporal development / sealed held-out | Strongest selection separation: outer temporal evaluation tests stability while inner temporal development contains parameter choice | Strongest protection against reusing the same development evidence for tuning and comparison | Highest and consumes more history | **Proposed primary architecture**, subject to researcher approval and later numerical feasibility within the frozen date envelope |
| TP3 — prespecified regime/calendar strata / sealed held-out | Useful diagnostic view of known dated environments | Complementary only; strata do not replace chronological pseudo-OOS selection | Adds multiplicity and reporting burden | Use only as a prespecified diagnostic overlay on TP2, not as a standalone partition architecture |

## Proposed architecture selection

The selected architecture is **TP2 with a TP3 diagnostic overlay**:

1. an inner time-ordered development loop may choose only among preregistered Search-Budget tuples;
2. an outer time-ordered development-validation loop evaluates fixed inner-loop choices across later origins;
3. one final held-out region remains sealed until separate authorization;
4. TP3 strata, if authorized, are dated ex ante and used only to report stability, not to redefine folds or add candidates;
5. TP1 remains the preregistered lower-complexity comparator for determining whether nesting adds necessary protocol value;
6. TP0 remains a sensitivity baseline and may not govern final candidate selection.

The proposal selects an architecture class, not numerical partitions. If later numerical design shows that TP2 cannot provide minimally adequate candidate-specific estimation, outer-validation, and sealed-held-out support within the frozen date envelope, the protocol must return for researcher decision; it must not silently collapse to TP1.

## Exact TP2 nesting semantics

TP2 qualifies as the proposed primary architecture only through four explicit, non-substitutable information layers:

1. **Formation/estimation history:** PIT inputs preceding a decision origin and admitted by the frozen representation-specific support contract. This history estimates a candidate without serving as outcome evidence for that origin.
2. **Inner development/specification-selection information:** time-ordered development evidence used only to choose among preregistered Search-Budget tuples under a frozen inner selection rule.
3. **Outer pseudo-OOS evaluation information:** later time-ordered evidence used to evaluate the fixed output of the inner process and to apply a preregistered model-selection/validation rule.
4. **Final sealed held-out information:** one chronologically later region outside every inner and outer development activity, inaccessible until separately authorized under G4-02.

`inner development != outer pseudo-OOS != final held-out`.

Outer pseudo-OOS evidence is not an informal second development set. Its permitted outputs, inspection cadence, aggregation, and consequences must be preregistered. Repeated informal inspection or response-driven revision contaminates the outer layer and requires an explicit reopening record; it cannot silently retain pseudo-OOS status.

`outer pseudo-OOS evaluates the preregistered selection procedure; it is not an iterative manual retuning environment`.

After any outer pseudo-OOS fold is inspected, researchers may not manually change candidate definitions, parameter grids, eligibility rules, target definitions, or selection criteria and then treat subsequent outer folds as uncontaminated under the same protocol. Any such change requires an explicit protocol reopening, contamination record, new protocol version, and reassessment of which outer regions remain unconsumed. If multiple outer folds later contribute to selection or confirmation, their aggregation and decision rule must be frozen before any contributing result is inspected.

### Conceptual architecture diagram

```text
PIT formation / estimation history
              |
              v
    Inner time-ordered development
    preregistered tuple selection
              |
              v
    Fixed inner-process output
              |
              v
    Outer pseudo-OOS folds
    preregistered evaluation/selection rule
              |
              v
    Specification frozen for confirmation
              |
              v
    FINAL SEALED HELD-OUT REGION
    separate, irreversible authorization

TP3 dated diagnostic strata overlay permitted evaluations only;
they do not feed specification tuning or selection.
```

## Architecture-role and information-flow matrix

| Architecture | Specification-selection role | Pseudo-OOS role | Final-evidence role | Diagnostic role | Allowed information flow | Forbidden information flow |
|---|---|---|---|---|---|---|
| **TP2 — proposed primary** | Inner time-ordered selection from the frozen Search Budget; outer rule evaluates/selects only as preregistered | Explicit outer time-ordered folds, separated from inner development | None until one external final held-out region is separately opened | May receive TP3 overlay without feedback | past formation inputs -> inner selection -> fixed output -> outer rule -> later frozen specification | outer/final evidence -> inner tuning; repeated informal outer inspection; any final-held-out feedback |
| **TP3 — proposed diagnostic overlay** | None | None independently; stratifies already-permitted evaluation records | None; cannot define confirmatory success after inspection | Explain prespecified where/when heterogeneity of a frozen specification | frozen specification/results -> prespecified dated diagnostic summaries | diagnostic result -> tune, replace, rescue, or select primary specification |
| **TP1 — lower-complexity competitor** | Only under its own preregistered walk-forward rule fixed before TP2 results | Rolling-origin pseudo-OOS without TP2 nesting | None; shares no access to final held-out before authorization | Lower-complexity sensitivity/comparator | its frozen prior-data origins -> its preregistered aggregation | switching to TP1 as an opportunistic tuning environment after TP2 results |
| **TP0 — sensitivity baseline** | None for the primary selection process | One simple fixed/blocked development comparison only | None | Transparency/sensitivity baseline | prespecified fixed split -> baseline report | favorable TP0 result -> override or replace the preregistered primary architecture |

The frozen TP3 boundary is: `TP3 explains heterogeneity; TP3 does not tune the primary specification`. TP3 may explain where or when a frozen specification behaves differently, but cannot rescue, replace, tune, or select it after primary results are observed. Any TP3-driven specification change requires explicit protocol reopening and contamination recording.

TP1 and TP0 are preregistered robustness/sensitivity architectures, not opportunistic alternative tuning environments. Favorable TP1 or TP0 results cannot override TP2 merely because they produce a preferred conclusion.

## Final held-out boundary

One final held-out region must lie outside all TP2 inner and outer development activity. Its calendar boundary remains unresolved. Access remains separate, logged, irreversible, and consequence-bearing under G4-02; architecture approval does not authorize access.

## Required subsequent calendar-geometry decision

After architecture selection, a separate bounded decision must reconcile, without using returns, model performance, pair counts, or candidate outcomes:

- H504 maximum authorized history;
- O20 maximum authorized outcome horizon;
- warm-up requirements;
- number and spacing of outer pseudo-OOS folds;
- inner development support;
- final held-out duration;
- purge/embargo geometry;
- the available 2013-2025 historical range.

No exact date, fold count, spacing, duration, purge, or embargo value is selected here.

## Information-boundary and access rules

- Every origin uses only information with `available_time <= decision_time`.
- Inner-loop outputs cannot inspect outer-loop future observations; neither loop can inspect final held-out evidence.
- Outcome records are quarantined relative to their decision origins.
- Overlapping estimation windows or outcome horizons activate the structurally triggered purge/embargo analysis frozen in G4-03A.
- Eligibility, partition, candidate, and Search-Budget versions must be bound before development computation.
- Any development inspection, outer-validation inspection, or future held-out access must be logged under G4-02.

## Decisions preserved for later numerical protocol

- exact development, outer-validation, and held-out dates;
- rolling versus expanding history within each permitted representation contract;
- number and spacing of inner and outer origins;
- exact purge and embargo rules/lengths;
- target censoring at fold and partition boundaries;
- aggregation and stability summaries across origins;
- whether every candidate uses identical origins or candidate-specific eligible origins with explicit support reporting;
- the finite TP3 strata, if any;
- TP2-versus-TP1 adequacy decision rule;
- all development and held-out access authorizations.

## Frozen classification

| Item | Proposed classification |
|---|---|
| Chronological nested development with sealed final held-out | **TP2 — PRIMARY NESTED TEMPORAL VALIDATION ARCHITECTURE** |
| Prespecified regime/calendar reporting | **TP3 — DIAGNOSTIC OVERLAY ONLY** |
| Rolling-origin non-nested structure | **TP1 — PREREGISTERED LOWER-COMPLEXITY WALK-FORWARD ROBUSTNESS COMPETITOR** |
| Single split | **TP0 — FIXED/BLOCKED SENSITIVITY BASELINE** |
| Dates, origins, purge/embargo, aggregation, strata | **G4 NUMERICAL DECISION — DEFER** |
| Development access | **NOT AUTHORIZED** |
| Held-out access | **SEPARATE LATER AUTHORIZATION** |

No development access follows from this freeze. G4-03B2 must separately freeze calendar geometry and access controls without inspecting research outcomes.

`G4-03B APPROVED / FROZEN`
