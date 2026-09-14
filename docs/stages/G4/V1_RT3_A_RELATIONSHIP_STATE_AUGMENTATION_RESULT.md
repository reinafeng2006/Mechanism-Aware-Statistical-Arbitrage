# V1 RT3-A Relationship-State Augmentation Result

Date: 2026-09-14

Status: **FROZEN / PUBLICATION PENDING**

The seven frozen relationship candidates were deterministically replayed over the ten authorized 2015–2019 inner partitions solely to materialize the minimal event-time state required by frozen A5 RT3. The original `V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0` artifacts were opened read-only and remain unchanged.

- Candidates: 7
- Candidate × half-year partitions: 70
- Exact common-output equivalence passes: 70
- Shared-field mismatches: 0
- OF4 access: none
- Final held-out access: none
- Empirical interpretation: none

The immutable companion is bound by `V1-RT3-RELATIONSHIP-STATE-AUGMENTATION-1.0`. Each partition records its own SHA-256, ancestor relationship-partition SHA-256, model/schema identity, and exact-equivalence result. Future RT3 construction must use the event-time state from this companion; it may not substitute a state estimated at `t+h`.

No relationship ranking, abnormality, resolution target, A6 result, trade, or PnL was inspected. Downstream use remains denied until this qualified augmentation and its validator are published.

`RT3-A RELATIONSHIP-STATE AUGMENTATION — PASS_EXACT`
