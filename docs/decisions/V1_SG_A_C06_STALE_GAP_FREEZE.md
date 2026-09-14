# V1 SG-A C06 Structural Stale-Gap Freeze

Decision date: 2026-09-14

Decision ID: `V1-SG-A-1.0`

Status: **RESEARCHER APPROVED / FROZEN**

## Frozen distinction

`classification age != stale-gap indicator`

Classification age remains the continuous elapsed time since the active PIT C06 snapshot became available. `C06_STALE_GAP` is a separate structural state about a missed expected official update opportunity. It is not a thresholded version of age and does not replace age.

## Deterministic state contract

At decision time `t`, first select the latest qualified C06 snapshot with `available_time <= t` under `C06-AVAILABILITY-AMENDMENT-V1`. Determine the versioned publication regime applicable at `t` from authoritative historical C06 metadata.

Set `C06_STALE_GAP = 1` only when all of the following are established without empirical calibration:

1. the active PIT classification is being carried forward;
2. the applicable authoritative regime establishes the next expected classification period/update opportunity and its normal official publication sequence;
3. that opportunity should already have produced a publicly available qualified successor by `t`; and
4. no qualified successor is genuinely available by `t`.

Set `C06_STALE_GAP = 0` only when the applicable regime and qualified publication sequence establish that no expected update opportunity has been missed by `t`.

If the applicable historical regime, expected opportunity, or defensible availability implication cannot be established, the Boolean is not fabricated. Record `C06_STALE_GAP_QUALIFICATION = UNRESOLVED` and leave the Boolean unavailable under the existing A6 missingness/quality contract.

The regime registry must preserve the authoritative quarterly 2012-regime sequence, the authoritative semiannual 2023-regime sequence, and any intervening unresolved regime/availability interval as distinct versioned states. A modern cadence may not be imposed retrospectively.

## Prohibitions

- no 90/120/180-day or other day-count threshold;
- no sample quantile, observed gap distribution, model performance, or survival-rate calibration;
- no period label, quarter end, half-year end, archive modification date, or current page date used as publication/availability time;
- no default `0` or `1` when regime qualification is unresolved;
- no change to C06 membership, taxonomy, PAIR-A, A6's other 22 PV0 columns, or any frozen model/trading rule;
- no relationship-output recomputation caused by this amendment.

## Lineage and anti-contamination

The implementation must reference `CORE-DATASET-FREEZE-V1` and `C06-AVAILABILITY-AMENDMENT-V1`, retain source snapshot and regime identifiers, and expose classification age, stale-gap value, and stale-gap qualification separately. SG-A was selected before A3, A5, A6, G5, OF4, or held-out inspection. No empirical result informed this definition.

`SG-A — RESEARCHER APPROVED / FROZEN`
