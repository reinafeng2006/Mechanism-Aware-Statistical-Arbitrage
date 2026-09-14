# V1 C06 Availability-Time Amendment Freeze

Decision ID: `C06-AVAILABILITY-AMENDMENT-V1`

Status: **APPROVED / QUALIFIED / FROZEN**

Date: 2026-09-14

Ancestor: `CORE-DATASET-FREEZE-V1`

Ancestor root: `3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616`

## Scope and non-mutation boundary

This amendment changes only the publication/available-time metadata used to activate the already-frozen official C06 snapshots. It does not replace or overwrite `CORE-DATASET-FREEZE-V1` and does not change snapshot payloads, membership rows, taxonomy/version labels, security identities, machinery scope `34 + 35`, PAIR-A, temporal geometry, or any G4/G5 scientific rule.

`C06-FIX-A was authorized before any empirical relationship, pair-count, return, outcome, or PnL inspection`.

## Authoritative evidence rule

Every qualified date comes from the visible historical publication record preserved in an immutable first-party CSRC or CAPCO page capture. The current archive location, archive-page modification date, download date, reference-period label, quarter/half-year end, and neighboring publication dates were not used as availability evidence.

The evidence has date precision rather than verified intraday precision. Accordingly, each snapshot becomes usable only at the first project decision clock strictly after its visible publication date. `reference period ≠ publication time ≠ available time`.

## Amendment result

- 45 frozen snapshot titles were individually registered.
- They represent 42 logical historical snapshots.
- All 1,125 rows whose old normalized `publication_date` was null are explicitly assigned to three duplicate-title groups: 2015Q4 (264), 2020Q4 (401), and 2021Q3 (460).
- Each duplicate group has identical normalized membership content across its title variants; no membership row was changed or collapsed.
- 7,456 rows carrying the erroneous shared `2019-09-04` archive-migration date were linked to independently preserved first-party visible publication dates.
- Zero snapshots remain `C06 AVAILABILITY UNRESOLVED`.
- The archive-migration date is retained only as old lineage; it activates no historical snapshot unless independently supported. No registered snapshot independently qualified with `2019-09-04` as its true publication date.

## PIT origin validation

The structural-only validation selected the latest qualified snapshot published strictly before each frozen inner origin:

| Inner origin | Latest qualified snapshot | First-party publication date | State |
|---|---|---:|---|
| 2015-01-01 | 2014Q3 | 2014-10-13 | CONSTRUCTIBLE |
| 2015-07-01 | 2015Q1 | 2015-05-04 | CONSTRUCTIBLE |
| 2016-01-01 | 2015Q3 | 2015-10-27 | CONSTRUCTIBLE |
| 2016-07-01 | 2016Q1 | 2016-05-06 | CONSTRUCTIBLE |
| 2017-01-01 | 2016Q3 | 2016-11-10 | CONSTRUCTIBLE |
| 2017-07-01 | 2017Q1 | 2017-06-01 | CONSTRUCTIBLE |
| 2018-01-01 | 2017Q3 | 2017-11-14 | CONSTRUCTIBLE |
| 2018-07-01 | 2018Q1 | 2018-05-21 | CONSTRUCTIBLE |
| 2019-01-01 | 2018Q3 | 2018-11-02 | CONSTRUCTIBLE |
| 2019-07-01 | 2019Q1 | 2019-04-19 | CONSTRUCTIBLE |

Carry-forward remains governed by the frozen C06 contract. The source snapshot ID, publication/available-time rule, taxonomy version, classification age, and staleness state must remain visible when decision-date membership is later materialized. No numerical staleness exclusion threshold is added.

## Immutable binding

- Base C06 membership SHA-256: `288C5BBB457439B88E4D23A6E821D864A4F53A4AF401241C642B48EEBBECBBE4`
- Snapshot amendment register SHA-256: `FA9A527B180A303F094E52F7258A552CCC1261660746283319250C0A1272B03A`
- PIT-origin validation SHA-256: `9762DF95030C7A078934C6D8392D6462893DD834C48DD127AD24B3AAF248BD67`
- Generator SHA-256: `35341BE6370ED24C57C268DA8F529B4E3094032879338671B63CA5F6D9C7660A`
- Amendment root fingerprint: `C53FC338A47B4CD1E5D83E3F945D47544D0211D9338B6006499E08CC76D2E95F`

Canonical amendment artifacts:

- `data/manifests/C06_AVAILABILITY_AMENDMENT_V1.json`
- `data/amendments/c06/C06_AVAILABILITY_AMENDMENT_V1/snapshot_availability_register.jsonl`
- `data/amendments/c06/C06_AVAILABILITY_AMENDMENT_V1/pit_origin_validation.json`
- `tools/v1_c06_availability_amendment.py`
- `tools/validate_v1_c06_availability_amendment.py`

Any later correction creates a new amendment version with ancestry to this record and the unchanged frozen core. Silent overwrite is prohibited.

## Downstream binding

V1 PAIR-A construction must join the unchanged frozen membership content to `C06-AVAILABILITY-AMENDMENT-V1`. The old `publication_date` field in the base normalized file remains preserved as lineage but is superseded for activation semantics by this amendment. This does not itself authorize empirical access; the Phase 1 action contract remains controlling.

OF4 2020–2023 was not accessed. The 2024–2025 final held-out region remains sealed.

`C06-FIX-A QUALIFIED / PHASE 1 RESUME ELIGIBLE AFTER PUBLICATION`
