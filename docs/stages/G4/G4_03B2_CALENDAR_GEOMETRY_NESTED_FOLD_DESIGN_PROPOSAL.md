# G4-03B2 Calendar Geometry & Nested Fold Design Proposal

Status: **PROPOSED / AWAITING RESEARCHER REVIEW**
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

Outer origins are shared, while each representation uses only its preregistered allowed history/cadence tuple. This best preserves representation-specific support semantics but increases support-comparison and bookkeeping complexity.

These are calendar-design candidates only. They do not add estimation horizons beyond G4-03A or change TP2.

## Fold semantics to freeze later

For each proposed outer fold, the final calendar contract must identify:

`warm-up start -> inner development origins -> inner selection cutoff -> outer pseudo-OOS start/end -> purge/embargo -> next fold`

The final held-out region must begin only after all outer activity and its required outcome/purge boundary. No fold may use later information to determine its earlier composition.

## Decisions required

1. choose CG0, CG1, or CG2, or an explicitly justified bounded combination;
2. choose the number and spacing of outer folds;
3. specify the inner-origin structure and selection cutoff within each outer fold;
4. specify warm-up treatment for H504-restricted candidates;
5. specify outcome censoring and the structural purge/embargo formula;
6. choose the final sealed held-out duration and boundary;
7. specify how candidate-specific eligible origins and shared origins are reported;
8. freeze hashes/versioning and access-log controls before development access.

All dates, fold counts, durations, and purge/embargo lengths remain unresolved in this proposal.

`G4-03B2 CALENDAR GEOMETRY & NESTED FOLD DESIGN PROPOSED / AWAITING RESEARCHER REVIEW`
