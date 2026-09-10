# G3B-C1 Structural Data Contract Amendment Proposal

Status: **G3B-C1 APPROVED / FROZEN — 2026-09-10**  
Scope: governance correction only. The dataset is **not frozen**; no measurement, model, target, or empirical use is authorized.

## Proposed two-layer architecture

### Core Dataset Structural Freeze

Core freeze asks whether raw observations, security identities, PIT universe membership, provenance, missingness states, and known qualification gaps are preserved reproducibly. It authorizes preservation and controlled access to a research dataset, not the use of any candidate measurement.

### Candidate Measurement Eligibility

Measurement eligibility asks whether a named candidate may use a named observation/history under its C04, C05, E02, E03, adjustment, and PIT requirements. Every implementation must pass a separate candidate-specific rule before empirical use.

`core dataset frozen ≠ measurement authorized`

`raw observation exists ≠ observation eligible for every measurement`

## Mandatory downstream propagation

C04/C05 qualification states are durable observation-level and candidate-level controls. Dataset freeze, cleaning, alignment, derivation, or later stage transitions must not clear, reset, conceal, or silently recode them.

- `CORPORATE_ACTION STATUS UNRESOLVED` never silently becomes `clean observation`;
- `UNKNOWN MISSINGNESS` never silently becomes normal trading, zero return, a forward-filled price, or suspension;
- every candidate requiring C04/C05 information must enforce its frozen eligibility status before computation;
- every downstream artifact must retain traceability to the source C04/C05 state and the rule, version, and decision that established eligibility.

## C04 authoritative coverage

C04 remains **AUTHORITATIVE COVERAGE INCOMPLETE**. Raw/unadjusted C03 observations may be preserved in the core dataset, but neither Tushare nor Sina adjustment factors become canonical PIT corporate-action lineage. No adjusted-price history is constructed or authorized by this proposal.

Introduce the observation-level semantic state:

`CORPORATE_ACTION STATUS UNRESOLVED`

It applies where authoritative corporate-action cleanliness cannot be established. Such an observation must not automatically be interpreted as genuine price abnormality. Candidates requiring clean returns, adjusted paths, continuity across actions, or action-aware abnormality remain **BLOCKED / CONSTRAINED** until a separately approved C04 eligibility rule or qualified lineage satisfies their requirement. No return threshold or action detector is defined here.

## C05 authoritative coverage

The four structural states remain:

- `NORMAL TRADING OBSERVED`
- `SUSPENSION`
- `RESUMPTION`
- `UNKNOWN MISSINGNESS`

All 49,568 candidate unexplained security-sessions across 425 securities remain `UNKNOWN MISSINGNESS` unless authoritative evidence resolves them. No price or status is imputed. A candidate whose required history intersects these sessions must later define an approved eligibility, exclusion, or uncertainty-handling rule before empirical use.

## Identifier-lineage governance

Frozen principle:

`security identifier continuity ≠ economic relationship continuity`

The authoritative `601313.SH → 601360.SH` record establishes a valid historical identifier/security-lineage mapping and removes the unresolved identity. It does not authorize automatic splicing into one economically continuous research series. Major restructuring, code-change, or control-change cases require later relationship-validity treatment. The existing identifier register remains the factual provenance record and is not rewritten by this proposal.

## Revised freeze basis

The approved minimum criteria are defined in [Core Dataset Freeze Criteria](CORE_DATASET_FREEZE_CRITERIA.md). C04/C05 incompleteness may remain visible candidate-level restrictions rather than an automatic veto over reproducible raw-data preservation.

## Candidate impact

The approved dependency-aware classifications are in [C04/C05 Measurement Eligibility Matrix](C04_C05_MEASUREMENT_ELIGIBILITY_MATRIX.md). They do not select a candidate or supersede G2B classifications. They add a separate data-eligibility dimension.

## Non-authorizations

This amendment does not freeze the dataset, authorize adjusted representations, define missingness or corporate-action treatments, select models, compute measurements, construct targets, inspect outcomes, or begin G4.

`G3B-C1 APPROVED / FROZEN`
