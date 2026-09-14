# V1 Phase 1 A6 C06 Stale-Gap Integrity Blocker

Date: 2026-09-14
Status: **GENUINE EXECUTABLE DESIGN-MATRIX BLOCKER / RESEARCHER DECISION REQUIRED**

DECA-A is frozen and published. The seven frozen V1 relationship candidates have been mechanically executed over the authorized 2015–2019 inner region and materialized as 70 immutable candidate × half-year partitions. No relationship result has been interpreted or compared.

Before A3/A5/A6/G5 continuation, the executable audit found that column 16 of the frozen 23-column PV0 matrix requires a `C06 stale-gap indicator`. The governing C06 and G4 records explicitly preserve classification age as continuous metadata and leave the stale-gap threshold/numerical effect unresolved. No frozen rule maps age or snapshot timing to this Boolean column.

Choosing a threshold, redefining the column as always zero, silently dropping it, or deriving it from observed coverage would change the frozen A6 equation. Full-rank handling also prohibits silent column dropping. This cannot be resolved as an engineering default.

## Bounded decision

- `SG-A — STRUCTURAL PUBLICATION-GAP INDICATOR` (recommended): define stale-gap without an outcome-calibrated day threshold as `1` when the active snapshot is being carried past the first subsequent expected quarterly reference-period boundary without a newly qualified publication; otherwise `0`. Preserve calendar-day classification age separately. This uses taxonomy publication structure, not performance or realized survival.
- `SG-B — PREREGISTERED CALENDAR-DAY THRESHOLD`: researcher supplies one ex-ante day count; indicator is `classification_age_days > threshold`. This is operationally simple but the cutoff is a design convention unless independently justified.
- `SG-C — REMOVE BOOLEAN FROM A6 BY VERSIONED AMENDMENT`: retain continuous classification age only and create a new A6 matrix version. This reduces arbitrary discretization but changes the already frozen 23-column matrix and requires explicit amendment ancestry.

Recommendation: `SG-A`, because it gives the registered Boolean a structural calendar/publication meaning without selecting a cutoff from empirical distributions. It does not exclude observations or relabel PIT validity; it is a predictor/quality-state field only.

No OF4 2020–2023 or held-out 2024–2025 information was accessed. No A3 abnormality, A5 target, A6 fit, trade, or PnL was computed.

`V1 A6 C06 STALE-GAP RULE / RESEARCHER DECISION REQUIRED`
