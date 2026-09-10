# G4-03B2 Calendar Geometry & Nested Fold Design Freeze

Status: **G4-03B2 APPROVED / FROZEN — 2026-09-10**
Boundary: pre-empirical calendar design only. No frozen-data statistics, pair counts, returns, candidate outcomes, or research results may be inspected.

## Objective

Translate the frozen TP2 architecture into a finite calendar/fold geometry that provides adequate chronological support for inner selection, outer pseudo-OOS evaluation, and one final sealed held-out region within the frozen 2013-01-07 through 2025-12-31 data envelope.

## Required geometry constraints

The later calendar selection must jointly reconcile:

- H504 as the maximum authorized representation-restricted history;
- O20 as the maximum authorized outcome-validation horizon;
- candidate-specific warm-up and eligibility-mask generation;
- adequate inner time-ordered development support;
- number and spacing of outer pseudo-OOS folds;
- final held-out duration and strict separation from all development activity;
- structurally triggered purge/embargo geometry;
- target censoring at fold and partition boundaries;
- the available 2013-2025 historical envelope;
- the frozen representation-aware Search Budget.

No geometry may be chosen using returns, model performance, pair counts, candidate outcomes, or favorable sample availability.

## Candidate calendar-geometry families

### CG0 — Expanding-history nested origins

Each successive inner/outer origin uses all eligible prior history, subject to the relevant H63/H126/H252 or authorized H504 support contract. This maximizes historical reuse but allows training-span age and composition to grow.

### CG1 — Rolling fixed-span nested origins

Each origin uses a frozen representation-specific history span. This keeps adaptation geometry more comparable through time but discards older observations and requires explicit handling of candidates with different support contracts.

### CG2 — Hybrid representation-bound nested origins

CG2 is defined exactly as:

`shared evaluation origins + preregistered representation-specific authorized estimation geometry`.

Outer evaluation origins and decision periods are shared within the same temporal comparison layer. Each representation may use only the history/cadence tuples authorized by the frozen G4-03A Search Budget and its preregistered support contract. No representation may acquire a new history length after performance inspection.

`representation-specific estimation support != model-specific outcome-driven tailoring`.

Candidate-specific eligibility restrictions frozen in G4-01 may reduce usable support at a shared origin, but the difference must remain visible in native-support and later common-support reporting; it cannot be hidden by moving the origin or silently dropping the candidate.

These are calendar-design candidates only. They do not add estimation horizons beyond G4-03A or change TP2.

## CG0-CG2 protocol comparison

| Criterion | CG0 — expanding history | CG1 — rolling fixed span | CG2 — representation-bound hybrid |
|---|---|---|---|
| Dynamic-relationship objective | Weaker adaptation because increasingly old observations remain influential | Strong adaptation geometry through bounded histories | Strongest semantic fit: adaptation may differ only where frozen representation contracts justify it |
| Comparability across time | Changing history length/composition reduces comparability | High within a fixed rolling specification | High at shared origins; representation-specific support differences remain explicit |
| Representation-specific support | Poor fit if one expanding rule is imposed universally | Moderate; separate fixed spans can become cumbersome | Directly accommodates H63/H126/H252 and restricted H504 without adding values |
| Sample efficiency | Highest reuse of earlier observations | Lower because older observations roll out | Controlled compromise; each representation uses its authorized support efficiently |
| Live-deployment realism | Realistic for cumulative estimators but may under-adapt | Realistic for rolling production refresh | Most realistic for a production system containing multiple representation families |
| Leakage resistance | Strong if cutoffs are fixed, though growing histories require careful lineage | Strong with fixed cutoffs and spans | Strong if tuple/origin versions are bound before access; more bookkeeping is required |
| TP2 compatibility | Compatible | Compatible | Best aligned with nested selection while retaining shared outer evaluation origins |
| Native/common-support reporting | Simple native support; common support may drift with expanding availability | Relatively transparent | Explicitly compatible, but requires both candidate-native masks and shared-origin/common-support reporting |
| Search Budget discipline | Small geometry but may force semantically inappropriate uniformity | Finite if rolling spans are preregistered | Strongest if only explicit authorized tuples are materialized; highest risk of silent expansion if governance is ignored |

### Frozen role structure

- **CG2 — PRIMARY CALENDAR GEOMETRY:** preserves shared evaluation origins while honoring frozen representation-specific support.
- **CG1 — ROLLING FIXED-SPAN ROBUSTNESS COMPETITOR:** may later test a simpler rolling geometry but cannot become a new tuning environment.
- **CG0 — EXPANDING-HISTORY SENSITIVITY:** may later test cumulative-history sensitivity and cannot override CG2 merely because its results are favorable.

## Shared evaluation-origin principle

Competing specifications evaluated within the same temporal comparison layer must share outer evaluation origins and decision periods, subject only to candidate-specific eligibility restrictions already frozen in G4-01. Support loss, exclusion reasons, and unequal eligible samples must be exposed. Outer boundaries cannot move because of pair counts, candidate availability, returns, model performance, or perceived regime favorability.

## Warm-up versus evaluative information

`warm-up / formation history != development / evaluation information`.

Observations used solely to satisfy H252 or representation-restricted H504 support may establish the first eligible estimation origin, but do not automatically become inner tuning records, outer pseudo-OOS records, or final held-out evidence. Every calendar version must label the role of each interval explicitly.

## Frozen high-level calendar structure

| Period | Proposed role | Geometry assessment |
|---|---|---|
| 2013-01-07 through 2014-12-31 | **Warm-up / formation reserve only** | May support estimation, including H504 where authorized, but is not development or evaluation evidence |
| 2015-01-01 through 2023-12-31 | **Nested development plus outer pseudo-OOS region** | Contains all TP2 inner and outer development activity; fold count, spacing, inner support, and aggregation remain unresolved |
| 2024-01-01 through 2025-12-31 | **Final sealed held-out region** | Outside all development activity; no access is authorized |

The structure is compatible in principle with H504 and O20: the reserve precedes development, and the final held-out follows all outer activity. `warm-up information may support estimation but does not constitute development or evaluation evidence`. Exact session sufficiency is not asserted without a later rule-based calendar construction. O20 outcomes near any boundary must be censored or separated by the later frozen purge/embargo rule.

No alternative calendar is proposed at this checkpoint because the stated structure meets the conceptual nesting requirements without outcome-based adjustment. If later deterministic calendar construction reveals a structural incompatibility, any alternative must be justified using H504/O20, fold-support, censoring, or purge/embargo geometry only.

## Fold semantics to freeze later

For each proposed outer fold, the final calendar contract must identify:

`warm-up start -> inner development origins -> inner selection cutoff -> outer pseudo-OOS start/end -> purge/embargo -> next fold`

The final held-out region must begin only after all outer activity and its required outcome/purge boundary. No fold may use later information to determine its earlier composition.

## Preserved unresolved decisions

1. choose the number, spacing, and duration of outer folds without empirical convenience criteria;
2. specify the inner-origin structure and selection cutoff within each outer fold;
3. decide rolling/expanding behavior within CG2 for every authorized representation tuple;
4. specify outcome censoring and the structural purge/embargo formula and exact lengths;
5. specify how candidate-specific eligible origins, native support, and common support are reported;
6. freeze hashes/versioning and access-log controls before development access.

All dates, fold counts, durations, and purge/embargo lengths remain unresolved in this proposal.

`G4-03B2 APPROVED / FROZEN`
