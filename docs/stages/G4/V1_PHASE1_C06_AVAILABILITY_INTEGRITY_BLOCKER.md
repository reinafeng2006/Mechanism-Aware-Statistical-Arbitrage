# V1 Phase 1 C06 Availability-Time Integrity Blocker

Status: **GENUINE INTEGRITY BLOCKER / RESEARCHER DECISION REQUIRED**

Date: 2026-09-14

## Completed work

- `PAIR-A — COMPLETE PIT ALL-PAIRS` was frozen, validated, committed as `f6d7e9c`, and pushed to `origin/main` before any empirical access.
- The validated C04-A checkpoint remains unchanged.
- A structural pre-computation audit checked the frozen C06 normalized membership artifact against its bound hash and the frozen C06 available-time contract.
- No market observation, relationship, pair count, outcome, or PnL was computed or inspected.

## Exact integrity failure

The frozen C06 contract requires each historical classification snapshot to become usable only from its true publication/available time, with `2013-01-07` recorded as the earliest qualified boundary. The bound normalized artifact
`data/qa_work/g3b_full/c06/20260909T081518Z/primary_membership.jsonl`
does not implement that contract for the historical sequence:

- artifact SHA-256 remains the frozen `288C5BBB457439B88E4D23A6E821D864A4F53A4AF401241C642B48EEBBECBBE4`;
- it contains 15,886 rows across 45 snapshot titles;
- 1,125 rows have `publication_date = null` and correspond to duplicate/corrupt-title snapshot records;
- the dated normalized records for labelled snapshots 2012Q4 through 2019Q2 carry `publication_date = 2019-09-04`, an archive-page date rather than each snapshot's true historical publication date;
- under the artifact's own captured dates, none of the ten 2015–2019 January/July inner calendar boundaries has any C06 snapshot available strictly before the origin.

This is not a model failure and does not invalidate PAIR-A. It is a material C06 availability-time implementation mismatch. Constructing the 2015–2019 candidate universe would require silently backdating a period label, substituting a later archive date, or inventing dates. All are prohibited.

Machine-readable evidence is in `data/manifests/V1_C06_PIT_READINESS_BLOCKER.json`, SHA-256 `DAC22FD9171F6AAAB8E87FF9182A2AF7DA6241B725C416704DF3B93559D4C1FB`.

## Bounded researcher alternatives

| Alternative | Action | Scientific consequence |
|---|---|---|
| `C06-FIX-A — VERSIONED AVAILABILITY-TIME AMENDMENT` | Authorize a bounded reconstruction of true snapshot publication/available dates from already acquired immutable official archive/page evidence, with official reacquisition only where the existing evidence cannot establish a date. Create a new descendant metadata version with ancestry to `CORE-DATASET-FREEZE-V1`; never overwrite the frozen artifact. | Preserves the 2013–2019 calendar, PIT semantics, and PAIR-A. Requires validation of every used snapshot date and a new root/fingerprint for the descendant layer. |
| `C06-FIX-B — RESTRICTED POST-2019 START` | Amend the V1 temporal protocol so C06 is used only after a defensible captured publication date. | Avoids reconstructing historical timestamps but abandons the approved 2015–2019 inner geometry and leaves too little initial development evidence; H252 support may also be impaired. |
| `C06-STOP — DO NOT AMEND` | Keep the frozen dataset unchanged and stop V1 empirical execution. | Maximum conservatism; no Phase 1 inner results. |

## Recommendation

Recommend `C06-FIX-A`. It repairs metadata lineage rather than changing the scientific sample or using present/future membership. The amendment can be bounded to publication/available-time provenance for the already acquired official snapshots; any unresolved snapshot remains quarantined.

Researcher approval is required because this creates a new versioned dataset descendant and may authorize bounded official-source reacquisition. The current action does not permit either change.

## Exact next action after approval

Authorize one `V1-C06-AVAILABILITY-AMENDMENT` action to construct and validate a non-overwriting C06 metadata descendant, bind its ancestry/fingerprint, update PAIR-A to that version, commit/push, and then resume the existing Phase 1 implementation. No market outcomes, OF4, or held-out access should occur during the amendment.

`V1 PHASE 1 SAFELY PAUSED — C06 AVAILABILITY-TIME AMENDMENT REQUIRED`
