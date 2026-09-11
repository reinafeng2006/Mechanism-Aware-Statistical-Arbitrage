# G4-04A5 Resolution / Outcome Target & Validation Specification Proposal

Status: **PROPOSED / AWAITING RESEARCHER REVIEW**
Boundary: pre-empirical outcome protocol only. The outcome zone and final held-out region remain sealed. No future-outcome inspection, target computation, label creation, or model evaluation.

## Objective

Prespecify later resolution/outcome objects and validation roles for a fixed earlier decision origin while preventing outcome information from entering pair formation, normality, abnormality, mechanism evidence, or sequential updates before it genuinely becomes PIT-observable.

`outcome target != event-time evidence != trading holding period != trade decision`.

## Decision-origin contract

Every future outcome record must bind:

- originating decision/evidence-state ID and decision time;
- pair, direction, relationship representation, normal-state version, and eligibility-rule version;
- authorized outcome horizon and complete future interval;
- temporal role/fold and target-construction version;
- raw outcome-side artifact lineage and availability times;
- censoring, missingness, C04/C05, identifier, relationship-validity, and support states;
- strict `OUTCOME-ONLY / QUARANTINED` authorization.

An outcome record cannot mutate or relabel its originating evidence state.

## Frozen horizon boundary inherited

O1, O5, O10, and O20 are the only registered outcome-validation horizons. They are validation geometry, not exit or holding-period rules. Target-horizon-aware censoring requires the complete future interval to remain inside the same authorized temporal role; no outer outcome crosses into 2024–2025 held-out.

## Proposed target families

### RT0 — Directional follower response / catch-up

Future peer movement relative to its decision-time expected signed response and source/peer roles. This may validate later follower catch-up behavior but cannot establish that M1 was identified at the origin.

### RT1 — Source normalization / reversal

Future movement of the shocked/source asset relative to its event-time excess movement and frozen reference state. This may validate reversal/normalization behavior but cannot serve as event-time M2 pressure evidence.

### RT2 — Persistence / non-resolution

Degree to which the abnormal directional/joint departure remains, grows, changes morphology, or fails to resolve through an authorized horizon.

### RT3 — Relationship continuation / change / break

Later evidence about whether the originating normal relationship remains valid or changes. It validates relationship-state dynamics but cannot be leaked backward as M0 or break evidence at the origin.

### RT4 — Resolution timing and magnitude

Continuous time-to-resolution and magnitude/path summaries where observable and uncensored. Exact event definition, path functional, competing risks, and censoring treatment remain unresolved.

These families may coexist for one origin. They are not mutually exclusive mechanism labels.

## Continuous versus categorical targets

Prefer continuous direction, magnitude, persistence, and timing objects where semantics allow. Any categorical resolved/unresolved, catch-up, reversal, or break label requires an independently justified preregistered definition; arbitrary thresholds cannot be introduced merely to simplify modeling.

Absence of observed resolution by a horizon is not automatically proof of permanent non-resolution, M0, or relationship break. It may be censored or horizon-specific persistence.

## Directional and pair structure

- retain `i -> j` and `j -> i` outcome paths separately;
- bind source/peer roles as defined at the originating decision time;
- do not redefine roles from future performance;
- aggregate observations to direction, pair, and temporal origin only under a later frozen rule;
- prevent observation-rich pairs from dominating through row count;
- report common support for target/specification attribution and native support for target availability/deployability.

## Outcome eligibility and quarantine

Target eligibility is distinct from event-time eligibility. `UNKNOWN MISSINGNESS`, `CORPORATE_ACTION STATUS UNRESOLVED`, suspension/resumption, identifier transitions, and relationship-validity states propagate through the target interval. No zero return, forward fill, synthetic resolution, or future-based repair is allowed.

Feature-generation and mechanism-evidence paths must not access outcome artifacts. Later sequential decision times may use an observation only after it becomes genuinely PIT available, through a new evidence record; that does not retroactively change its outcome-only role for the earlier origin.

## Proposed validation dimensions

For each authorized target family, later validation should preserve separately:

- directional accuracy or proper directional loss where meaningful;
- magnitude/path error;
- timing and censoring adequacy;
- calibration/uncertainty where predictions support it;
- persistence/non-resolution behavior;
- temporal consistency, dispersion, severe failure, and support;
- native/common target availability;
- comparison uncertainty and multiplicity family.

No universal target metric or weighted score is proposed. Relationship and mechanism candidates cannot be selected retroactively using a target for which their upstream estimand was not authorized.

## SR0 / SR1 boundary

SR0 may cover invalid temporal ordering, incomplete required horizon, outcome leakage, irreproducible target lineage, mathematically undefined target, or violation of target-specific C04/C05/identifier rules. Failure to resolve, wrong direction, large error, or weak prediction is SR1 evidence—not structural invalidity.

## Multiplicity and claim roles

RT0–RT4 are distinct target families with explicit ancestry and claim scopes. O1/O5/O10/O20 do not automatically create a full Cartesian tournament. Each mechanism/target/horizon combination requires an explicit Search Budget entry. Discovery uses, sensitivity horizons, and confirmatory claims remain separately classified.

## Unresolved decisions

1. exact continuous definitions for catch-up, normalization/reversal, persistence, relationship continuation/break, timing, and magnitude;
2. whether any categorical targets have independently defensible boundaries;
3. source/peer role freezing and handling of bidirectional shocks;
4. path versus endpoint target semantics;
5. horizon-specific censoring and incomplete-path rules;
6. C04/C05/identifier eligibility through the outcome interval;
7. aggregation from observation/path to direction, pair, origin, and OF4 fold;
8. target-specific losses, calibration, uncertainty, and severe-failure rules;
9. finite target/horizon Search Budget and multiplicity families;
10. access controls, manifests, code versions, and contamination handling before outcome construction.

No target formula, categorical label, threshold, horizon-to-mechanism mapping, holding rule, metric, or computation is selected here.

`G4-04A5 RESOLUTION / OUTCOME TARGET SPECIFICATION PROPOSED / AWAITING RESEARCHER REVIEW`
