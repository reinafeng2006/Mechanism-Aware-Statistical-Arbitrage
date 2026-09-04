# G1-02 Review-Depth Audit

Status: **COMPLETE — G1-02 REOPENED; G1-03 NOT AUTHORIZED**

Audit date: 2026-09-03

## Audit rule

An admitted claim, a candidate-inventory row, a source link, or a claim YAML is not by itself a completed Light or Selective Deep review. A completed review requires a candidate-specific artifact in `literature/reviews/<ID>.md` with full-text provenance, identification logic, claim linkage, rival explanations, permitted/prohibited use, missing link, validation test, and project testability.

No such candidate-specific review artifact existed at audit time. Consequently no candidate has auditable completed Light or Selective Deep depth. All recorded claims are preserved, but their wording is **preliminary pending full-text review**.

`PF-003` and `PF-012` are two decision sections of one discovery work. The original discovery inventory is 34 ID rows / 33 distinct works; G1-02b appended four new candidates after Discovery. All 38 rows appear below so that no current evidence dependency is hidden.

## Candidate audit

`Verified` means verified against full text through a review artifact at the stated depth, not merely that a citation or locator appears in a register.

| Paper ID | Full text currently available | Completed depth | Review artifact | Dependent Claim IDs | G1 question(s) | Decision relevance | Full-text wording verified? | Recommended remaining depth |
|---|---|---|---|---|---|---|---|---|
| PF-001 | Yes | Triage | — | CL-PF-001 | A-P1, A-P3 | High | No | Selective Deep |
| PF-002 | Yes | Triage | — | — | A-P1 | Medium | N/A | Light |
| PF-003 | Yes | Triage | — | — | A-P1, A-P2, A-P3 | High | N/A | Selective Deep |
| PF-004 | Yes | Triage | — | CL-PF-002 | A-P2, A-P3 | High | No | Selective Deep |
| PF-005 | Yes | Triage | — | — | A-P2 | Medium | N/A | Light |
| PF-006 | Yes | Triage | — | CL-PF-004 | A-P2, A-P3 | High | No | Selective Deep |
| PF-007 | Yes | Triage | — | CL-PF-005 | A-P2, B-P3 | High | No | Selective Deep |
| PF-008 | Yes | Triage | — | CL-PF-003 | A-P2, A-P3 | High | No | Selective Deep |
| PF-009 | Yes | Triage | — | — | A-P2, A-P3 | Medium | N/A | Light |
| PF-010 | Yes | Triage | — | — | A-P3 | Medium | N/A | Light |
| PF-011 | Yes | Triage | — | — | A-P2 | Low / transfer | N/A | Defer unless gap persists |
| PF-012 | Yes (same work as PF-003) | Triage | — | — | A-P3 | High | N/A | Selective Deep section within PF-003 |
| M1-001 | Yes | Selective Deep | literature/reviews/M1-001.md | CL-M1-001 | B-P1, A-P1 | High | Yes | Complete |
| M1-002 | No — lawful readable full text unresolved | Source access only | literature/reviews/M1-002.md | CL-M1-002 | B-P1, A-P2 | High | No | Reopen only on lawful full text |
| M1-003 | No / pending | Discovery only | — | — | B-P1, B-P4 | High | N/A | Obtain full text, then Selective Deep if admitted |
| M1-004 | No / pending | Discovery only | — | — | B-P1, A-P1 | High | N/A | Obtain full text, then Selective Deep if admitted |
| M1-005 | No / pending | Discovery only | — | — | B-P1, B-P4 | High | N/A | Obtain full text, then Selective Deep if admitted |
| M1-006 | Yes | Triage | — | — | B-P1, A-P1 | High | N/A | Light, escalate only if it changes transferability |
| M1-007 | Yes | Triage | — | — | B-P1, B-P4 | Medium | N/A | Light |
| M1-008 | Yes | Light | literature/reviews/M1-008.md | CL-M1-003 | B-P1, A-P1 | Medium | Yes | Complete |
| M2-001 | Yes | Selective Deep | literature/reviews/M2-001.md | CL-M2-001 | B-P2 | High | Yes | Complete, linked with M2-002 |
| M2-002 | Yes | Selective Deep | literature/reviews/M2-002.md | CL-M2-002 | B-P2, B-P4 | High | Yes | Complete, linked with M2-001 |
| M2-003 | Yes | Selective Deep | literature/reviews/M2-003.md | CL-M2-003 | B-P2 | High | Yes | Complete |
| M2-004 | No / pending | Discovery only | — | — | B-P2, B-P4 | Medium | N/A | Obtain full text, then Light if admitted |
| M2-005 | Yes | Selective Deep | literature/reviews/M2-005.md | CL-M2-004 | B-P2, B-P4 | High | Yes | Complete |
| M2-006 | Yes | Triage | — | — | B-P2 | Medium | N/A | Light |
| M2-007 | Yes | Triage | — | — | B-P2 | High | N/A | Selective Deep if M2 boundary remains open |
| M3-001 | Yes | Triage | — | CL-M3-001 | B-P3, B-P4 | High | No | Selective Deep |
| M3-002 | Yes (same work/source family as PF-014) | Triage | — | — | B-P3, A-P2 | Medium | N/A | Light; re-admit separately only if needed |
| M0-001 | Yes | Triage | — | CL-M0-001 | B-P3 | High | No | Selective Deep, paired with M0-002 |
| M0-002 | Yes | Triage | — | CL-M0-001 | B-P3 | High | No | Selective Deep, paired with M0-001 |
| B4-001 | Yes | Triage | — | CL-B4-001 | B-P4 | High | No | Selective Deep |
| B4-002 | Yes | Triage | — | — | B-P1, B-P2, B-P4 | Medium | N/A | Light |
| B4-003 | No / pending | Discovery only | — | — | B-P3, B-P4 | Medium | N/A | Obtain full text, then Light if admitted |
| PF-013 | Yes | Triage | — | CL-PF-006 | A-P2, A-P3 | High | No | Selective Deep |
| PF-014 | Yes | Triage | — | CL-PF-007 | A-P2, B-P3 | High | No | Light |
| PF-015 | Yes | Triage | — | CL-PF-008 | A-P2, A-P3, B-P4 | High | No | Light |
| B4-004 | Yes | Selective Deep | literature/reviews/B4-004.md | CL-B4-002 | B-P2, B-P4 | High | Yes | Complete |

## Claim maturity audit

All current claim wording is retained exactly as substantive content, but none has the required candidate-specific review artifact. Therefore each is `PRELIMINARY — TRIAGE-DERIVED / FULL-TEXT REVIEW PENDING`, not an evidence-review-complete claim.

| Claim ID | Paper ID(s) | Full text | Completed depth | Artifact | Wording verified at sufficient depth? | Required next review |
|---|---|---|---|---|---|---|
| CL-PF-001 | PF-001 | Yes | Triage | — | No | Selective Deep |
| CL-PF-002 | PF-004 | Yes | Triage | — | No | Selective Deep |
| CL-PF-003 | PF-008 | Yes | Triage | — | No | Selective Deep |
| CL-PF-004 | PF-006 | Yes | Triage | — | No | Selective Deep |
| CL-PF-005 | PF-007 | Yes | Triage | — | No | Selective Deep |
| CL-M1-001 | M1-001 | Yes | Selective Deep | literature/reviews/M1-001.md | Yes | None for M1 Round 2 |
| CL-M1-002 | M1-002 | No — unresolved | Not admitted | literature/reviews/M1-002.md | No | Lawful full text, then Selective Deep |
| CL-M1-003 | M1-008 | Yes | Light | literature/reviews/M1-008.md | Yes | None for M1 Round 2 |
| CL-M2-001 | M2-001 | Yes | Triage | — | No | Selective Deep, linked with CL-M2-002 |
| CL-M2-002 | M2-002 | Yes | Triage | — | No | Selective Deep, linked with CL-M2-001 |
| CL-M2-003 | M2-003 | Yes | Triage | — | No | Selective Deep |
| CL-M2-004 | M2-005 | Yes | Triage | — | No | Selective Deep |
| CL-M3-001 | M3-001 | Yes | Triage | — | No | Selective Deep |
| CL-M0-001 | M0-001, M0-002 | Yes | Triage | — | No | One linked Selective Deep artifact per paper |
| CL-B4-001 | B4-001 | Yes | Triage | — | No | Selective Deep |
| CL-PF-006 | PF-013 | Yes | Triage | — | No | Selective Deep |
| CL-PF-007 | PF-014 | Yes | Triage | — | No | Light |
| CL-PF-008 | PF-015 | Yes | Triage | — | No | Light |
| CL-B4-002 | B4-004 | Yes | Triage | — | No | Selective Deep |

## Minimum priority queue before G1-03

This is a **minimum review set**, not a paper-count quota. Each completed item must create `literature/reviews/<ID>.md`, update claim maturity/provenance, and retain the full current schema fields. Stop a branch when its permitted-use boundary and missing-link record would not change.

| Priority | Review set | Depth | Why it is minimum |
|---|---|---|---|
| 1 | PF-001, PF-004, PF-006, PF-007, PF-008, PF-013 | Selective Deep | Covers company-aware representation, raw/residual comparator, stability/break rejection, and outcome-independent false-pair/generalization boundary. |
| 2 | M1-001, M1-002, M1-008 | Selective Deep for M1-001/002; Light for M1-008 | Tests whether directed links, leader-lag, and news timing support a bounded M1 implication rather than a label. |
| 3 | M2-001 + M2-002 as one linked block; M2-003; M2-005; B4-004 | Selective Deep | Required to set an M2 permitted-use boundary with contamination critique, exogenous timing, China rival evidence, and narrow microstructure identification. |
| 4 | M3-001, PF-014, PF-015, B4-001 | Selective Deep for M3-001/B4-001; Light for PF-014/PF-015 | Establishes whether M3 is identifiable or must remain residual/no-trade, while preserving outcome-use restrictions. |
| 5 | M0-001 + M0-002 | Selective Deep | Sets the theory-backed no-trade/rejection boundary and stops M0 from being treated as a catch-all empirical label. |

Supporting Light reviews (PF-002, PF-005, PF-009, PF-010, M1-006/007, M2-006, B4-002) are conditional: review only if a priority review exposes a gap that could change a permitted-use boundary. Pending China-specific candidates remain discovery-only until lawful full text is obtained; they are not preconditions for beginning the listed full-text reviews.

## Gate consequence

G1-02 is **reopened / in progress**. G1-03 cannot legitimately begin until the priority queue reaches a documented decision-saturation or stop result and every claim proposed for G1-03 has a review artifact and verified current-project provenance.
