# G4-04A1c Hard Failure Rules & Continuous Evidence Semantics Freeze

Status: **G4-04A1c APPROVED / FROZEN — 2026-09-11**
Boundary: pre-empirical rule semantics only. No frozen-data inspection, computation, outcome access, or A2 work.

## Accepted audit conclusion

The threshold-justification audit and its conclusion **NEITHER JUSTIFIABLE AS CURRENTLY SPECIFIED** are accepted. CUT-CONSERVATIVE and CUT-PERMISSIVE are rejected as primary protocol bundles. No third bundle is created.

## Frozen governing principles

`absence of a defensible natural/preregistered threshold must not be repaired by inventing a design-convention cutoff`.

`continuous evidence need not be discretized merely because the selection protocol ultimately requires a decision`.

`thresholds encode preregistered failure/adequacy semantics; thresholds must not be chosen to achieve a desired candidate survival rate`.

SR1 may retain continuous, partially ordered evidence and return `INSUFFICIENT DIFFERENTIATION`, `NON-DOMINATED / BOTH SURVIVE`, or `NO CANDIDATE ADVANCES` without manufacturing a cutoff or winner.

## 1. Scale quality

Remove SQ05 and SQ10 from the primary protocol. Hard scaled-loss failure is limited to:

- scale unavailable;
- scale non-finite;
- mathematically degenerate zero scale;
- failure of the preregistered mathematical minimum estimator-support requirement.

Near-zero but nondegenerate scale remains a continuous `SCALE QUALITY / NEAR-ZERO SCALE` diagnostic. It does not trigger epsilon replacement or automatic exclusion. A later hard boundary requires independent justification and freeze before outcome inspection. The diagnostic remains candidate-neutral and PIT.

## 2. Estimator support

Remove MS80 and MS90 from the primary protocol. Distinguish:

- **minimum mathematical estimator support:** the smallest structurally defined support under which MAD/SD and their required response history can be computed as specified; eligible to act as an SR0 hard requirement;
- **statistical precision/support quality:** additional history, completeness, dispersion precision, and representativeness; continuous SR1 evidence or candidate-specific support metadata.

Desirable precision cannot be promoted to SR0 by selecting an arbitrary completion percentage.

## 3. Common support

Remove SF2-50 and SF2-70 as hard model-admissibility or attribution thresholds. Report common-support retention continuously under CS2, together with native support and exclusion reasons.

`insufficient comparable support limits attribution scope; it does not by itself imply model invalidity`.

Use claim-scope states without numerical boundaries in A1c:

- `BROAD COMPARABLE-SUPPORT EVIDENCE`;
- `LIMITED COMPARABLE-SUPPORT EVIDENCE`;
- `INSUFFICIENT SUPPORT FOR COMPARATIVE CLAIM`.

These are claim-scope dispositions, not model-validity states. Any numerical mapping requires separate ex-ante justification.

## 4. Comparative reversal

Remove SF1-10 and SF1-20 as hard vetoes. A sign crossing or ordinary adverse point estimate is not a severe reversal.

Preserve as continuous SR1/AG2 evidence: adverse absolute and relative deterioration; uncertainty; direction and temporal occurrence; common/native support; and scale quality.

`SEVERE COMPARATIVE REVERSAL` requires both materially adverse absolute deterioration and adequate denominator/scale/uncertainty quality under a separately frozen rule. Until then, no numerical comparative-reversal veto operates.

## 5. Absolute adequacy

Remove SF0-2 and SF0-3 as hard failures. PIT-scaled loss remains continuous SR1/AG2 evidence because no independently established natural failure boundary currently exists.

A future hard boundary is permitted only if it has an independently interpretable relationship/use failure meaning frozen before outcomes. It cannot duplicate weak relative SR1 performance or become an SR0 failure merely because error is unfavorable.

## 6. OF4 severe-failure count

Freeze the protocol-level temporal rule:

`two or more genuinely severe outer-fold failures among OF4 are incompatible with ADVANCES / DOMINANT status`.

- `0` severe failures: no failure-count veto; advancement still requires the full SR1 vector.
- `1` severe failure: advancement remains unresolved and requires the full SR1 vector.
- `>=2` severe failures: the candidate cannot receive `ADVANCES / DOMINANT` under the primary protocol.

This is a temporal-robustness veto, not automatic candidate invalidation. It cannot operate until the underlying severe-failure definition is independently justified and frozen. Ordinary adverse point estimates do not count as severe failures.

## 7. SR1 without arbitrary thresholds

SR1 compares the continuous evidence vector through the frozen hierarchy:

1. common-support incremental quality and uncertainty;
2. temporal direction, dispersion, and independently justified severe failures;
3. native coverage/deployability;
4. production/data complexity as a later discriminator.

Partial ordering permits `DOMINANT / ADVANCES`, `NON-DOMINATED / BOTH SURVIVE`, `INSUFFICIENT DIFFERENTIATION`, or `NO CANDIDATE ADVANCES`. Lack of a hard cutoff or unique winner is a valid protocol result.

## Remaining bounded decisions

1. define minimum mathematical support for MAD/SD from estimator mathematics and frozen response-history semantics;
2. define continuous scale-quality reporting and undefined/zero-scale reason codes;
3. define claim-scope states without arbitrary percentage boundaries, or retain them as narrative evidence states;
4. independently justify any future absolute-adequacy or severe comparative-reversal definition;
5. define the severe-fold event before activating the OF4 count veto;
6. freeze continuous evidence reporting, uncertainty, and partial-order comparison implementation.

No numerical threshold bundle, epsilon, hard loss cutoff, support percentage, comparative-reversal veto, computation, or A2 work is authorized.

`G4-04A1c APPROVED / FROZEN`
