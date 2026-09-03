# G1-02 Reconciliation into the Migrated Literature OS

Status: **COMPLETE ONE-TO-ONE CONTROL RECONCILIATION — SUBSTANTIVE STATUS UNCHANGED**

This document maps existing current-project records into the migrated process infrastructure. It does not edit their claims, evidence direction, source locators, or provisional status. The canonical substantive records remain `registers/LITERATURE_EVIDENCE.md` and `registers/DATA_REQUIREMENTS.md`.

## Claim reconciliation — 15 of 15

| Control row | Existing Claim ID | Current G1 question | Existing candidate ancestry | Migrated status |
|---|---|---|---|---|
| RC-01 | CL-PF-001 | A-P1 | PF-001 | PROVISIONAL_G1_02 |
| RC-02 | CL-PF-002 | A-P2/A-P3 | PF-004 | PROVISIONAL_G1_02 |
| RC-03 | CL-PF-003 | A-P2/A-P3 | PF-008 | PROVISIONAL_G1_02 |
| RC-04 | CL-PF-004 | A-P2/A-P3/B-P3 | PF-006 | PROVISIONAL_G1_02 |
| RC-05 | CL-PF-005 | A-P2/B-P3 | PF-007 | PROVISIONAL_G1_02 |
| RC-06 | CL-M1-001 | B-P1/A-P1 | M1-001 | PROVISIONAL_G1_02 |
| RC-07 | CL-M1-002 | B-P1/A-P2 | M1-002 | PROVISIONAL_G1_02 |
| RC-08 | CL-M1-003 | B-P1/A-P1 | M1-008 | PROVISIONAL_G1_02 |
| RC-09 | CL-M2-001 | B-P2 | M2-001 | PROVISIONAL_G1_02 |
| RC-10 | CL-M2-002 | B-P2/B-P4 | M2-002 | PROVISIONAL_G1_02 |
| RC-11 | CL-M2-003 | B-P2 | M2-003 | PROVISIONAL_G1_02 |
| RC-12 | CL-M2-004 | B-P2/B-P4 | M2-005 | PROVISIONAL_G1_02 |
| RC-13 | CL-M3-001 | B-P3/B-P4 | M3-001 | PROVISIONAL_G1_02 |
| RC-14 | CL-M0-001 | B-P3 | M0-001/M0-002 | PROVISIONAL_G1_02 |
| RC-15 | CL-B4-001 | B-P4 | B4-001 | PROVISIONAL_G1_02 |

## Data Requirement reconciliation — 15 of 15

| Control row | Existing Data Requirement ID | Claim linkage retained | Migrated status |
|---|---|---|---|
| RD-01 | DR-001 | CL-PF-001 | PROVISIONAL_G1_02 |
| RD-02 | DR-002 | CL-PF-002 | PROVISIONAL_G1_02 |
| RD-03 | DR-003 | CL-PF-003 | PROVISIONAL_G1_02 |
| RD-04 | DR-004 | CL-PF-004 | PROVISIONAL_G1_02 |
| RD-05 | DR-005 | CL-PF-005 | PROVISIONAL_G1_02 |
| RD-06 | DR-006 | CL-M1-001, CL-M1-003 | PROVISIONAL_G1_02 |
| RD-07 | DR-007 | CL-M1-001, CL-M1-003 | PROVISIONAL_G1_02 |
| RD-08 | DR-008 | CL-M1-002 | PROVISIONAL_G1_02 |
| RD-09 | DR-009 | CL-M2-001, CL-M2-002 | PROVISIONAL_G1_02 |
| RD-10 | DR-010 | CL-M2-003 | PROVISIONAL_G1_02 |
| RD-11 | DR-011 | CL-M2-004, CL-B4-001 | PROVISIONAL_G1_02 |
| RD-12 | DR-012 | CL-M3-001, CL-B4-001 | PROVISIONAL_G1_02 |
| RD-13 | DR-013 | CL-PF-003, CL-M3-001 | PROVISIONAL_G1_02 |
| RD-14 | DR-014 | CL-PF-001, CL-PF-004, CL-PF-005, CL-M0-001 | PROVISIONAL_G1_02 |
| RD-15 | DR-015 | CL-M2-004, CL-B4-001 | PROVISIONAL_G1_02; OUTCOME_ONLY |

## Schema-field migration state

The existing claims already retain question, construct/method, identification limit, timing/transfer limit, competing explanation, candidate use, evidence direction, full-text basis, locator, and ancestry. The migrated fields `logic_chain`, `missing_link`, `validation_test_needed`, and `project_testability` are required for future extraction and G1-03 review. For all reconciled claims and DRs these added fields are `NOT YET ASSESSED — G1-03 UNAUTHORIZED`; no substantive inference is added during migration.

## Reconciliation invariant

- exactly 15 current Claim IDs appear once in the claim control table and once in the canonical evidence register;
- exactly 15 Data Requirement IDs appear once in the data control table and once in the canonical data register;
- every Data Requirement retains one or more current Claim IDs;
- no predecessor Paper ID or Claim ID is used as a current identifier.
