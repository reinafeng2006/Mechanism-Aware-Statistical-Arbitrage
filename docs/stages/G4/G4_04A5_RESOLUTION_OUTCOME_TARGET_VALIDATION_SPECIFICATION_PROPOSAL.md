# G4-04A5 Resolution / Outcome Target & Validation Specification Freeze

Status: **G4-04A5 APPROVED / FROZEN — 2026-09-11**
Boundary: pre-empirical outcome protocol only. The outcome zone and final held-out region remain sealed. No future-outcome inspection, target computation, label creation, or model evaluation.

## Resolution estimand

Resolution is the future evolution of the event-time abnormality and relationship state, evaluated from a fixed decision origin at the preregistered O1, O5, O10, and O20 horizons. It describes what happens after the event; it does not infer a trade, retrofit the event-time information set, or require an event to resolve through one mechanism.

`outcome target != event-time evidence != trading holding period != trade decision`.

`mechanism resolution != trading profitability`.

## Decision-origin contract

Every future outcome record must bind:

- originating decision/evidence-state ID and decision time;
- pair, direction, relationship representation, normal-state version, and eligibility-rule version;
- authorized outcome horizon and complete future interval;
- temporal role/fold and target-construction version;
- raw outcome-side artifact lineage and availability times;
- censoring, missingness, C04/C05, identifier, relationship-validity, and support states;
- strict `OUTCOME-ONLY / QUARANTINED` authorization.

An outcome record cannot mutate or relabel its originating evidence state. All components are evaluated relative to the frozen expected response, abnormality, relationship state, source/peer roles, and information set at the event-time origin.

`future information evaluates the event; it does not rewrite the event`.

## Frozen horizon boundary inherited

O1, O5, O10, and O20 are the only registered outcome-validation horizons. Each horizon produces a horizon-specific view of the same anchored resolution state; it is not a trading exit or holding-period rule. Target-horizon-aware censoring requires the complete future interval to remain inside the same authorized temporal role. In particular, no outcome attached to the 2023 outer fold may cross into the sealed 2024–2025 held-out region.

## Primary multidimensional continuous outcome state

At each authorized horizon, retain a mechanism-neutral continuous resolution vector rather than a single convergence score:

`R_h = (peer/follower catch-up, source normalization, persistence/non-resolution, relationship continuation/change-break)`.

The components may coexist and may point in different directions. Peer catch-up and source normalization may both occur; persistence may coexist with later relationship-change evidence. The vector is not a probability simplex, a mutually exclusive M1/M2 label, or a weighted score.

## Component semantics

### RT0 — Directional follower response / catch-up

M1 outcome evidence asks whether the peer that was under-responding at the event-time origin subsequently closes the remaining signed response gap along the expected PIT relationship direction. It is anchored to the event-time expected signed response and the event-time remaining response gap, not to the peer's unconditional price direction.

`peer price increase != catch-up`.

A peer move in the economically wrong direction, or a move unrelated to the frozen response gap, is not catch-up merely because its raw price rises. This component may validate later M1-consistent resolution but cannot establish that M1 was identified at the origin. No binary catch-up or percentage-closure threshold is proposed.

### RT1 — Source normalization / reversal

M2 outcome evidence asks whether the shocked/source asset's event-time excess component subsequently normalizes or reverses relative to the frozen event-time relationship and abnormality state. It is distinct from peer catch-up and cannot be validated solely by movement of the peer.

`M1 resolution != M2 resolution`.

This component may validate M2-consistent normalization but cannot serve as event-time temporary-pressure evidence. A sign change alone is not yet a qualified reversal rule.

### RT2 — Persistence / non-resolution

Continuous degree to which the event-time directional/joint abnormality remains, grows, changes morphology, or fails to resolve through an authorized horizon. The protocol does not force every event into M1 or M2 resolution. Persistence may remain unresolved, and it may coexist with relationship-change evidence. Non-resolution observed through O_h is horizon-specific evidence, not proof of permanent non-resolution.

### RT3 — Relationship continuation / change / break

Future evidence about whether the originating normal relationship continues, changes, or breaks, retained separately from catch-up and source normalization. It may later validate failure of the original temporary-abnormality interpretation, but it cannot be leaked backward as M0, relationship-break, or other event-time mechanism evidence.

### RT4 — Resolution timing and magnitude

RT4 is subordinate to the four-component state: it records continuous time-to-resolution and magnitude/path information where observable and uncensored rather than collapsing the components into a fifth competing mechanism. Exact event definition, path functional, competing risks, and censoring treatment remain unresolved.

## Continuous versus categorical targets

Primary targets remain continuous wherever semantics allow. Any categorical resolved/unresolved, catch-up, reversal, or break label requires an independently justified preregistered definition; arbitrary 50% gap closure, sign-only reversal, convergence threshold, or binary resolution rule cannot be introduced merely to simplify modeling.

Absence of observed resolution by a horizon is not automatically proof of permanent non-resolution, M0, or relationship break. It may be censored or horizon-specific persistence.

## Directional and pair structure

- retain `i -> j` and `j -> i` outcome paths separately;
- bind source/peer roles as defined at the originating decision time;
- do not redefine roles from future performance;
- aggregate observations to direction, pair, and temporal origin only under a later frozen rule;
- prevent observation-rich pairs from dominating through row count;
- report common support for target/specification attribution and native support for target availability/deployability.

No aggregation may erase coexistence among catch-up, normalization, persistence, and relationship-state components. Component-to-vector, direction-to-pair, horizon, and temporal-fold aggregation remain separately unresolved.

## Outcome eligibility and quarantine

Target eligibility is distinct from event-time eligibility. `UNKNOWN MISSINGNESS`, `CORPORATE_ACTION STATUS UNRESOLVED`, suspension/resumption, identifier transitions, and relationship-validity states propagate through the target interval. No zero return, forward fill, synthetic resolution, or future-based repair is allowed.

Feature-generation and mechanism-evidence paths must not access outcome artifacts. Later sequential decision times may use an observation only after it becomes genuinely PIT available, through a new evidence record; that does not retroactively change its outcome-only role for the earlier origin.

Future expected responses or re-estimated relationships may describe later decision states, but they may not retrospectively replace the original expected response, original abnormality, or original mechanism evidence used to anchor an earlier outcome record.

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

Transaction costs, entries, exits, holding-period rules, Sharpe, PnL, portfolio construction, and strategy returns are outside A5. A mechanism-resolution outcome may occur without an economically profitable trade, and profitability cannot substitute for resolution validation.

## SR0 / SR1 boundary

SR0 may cover invalid temporal ordering, incomplete required horizon, outcome leakage, irreproducible target lineage, mathematically undefined target, or violation of target-specific C04/C05/identifier rules. Failure to resolve, wrong direction, large error, or weak prediction is SR1 evidence—not structural invalidity.

## Multiplicity and claim roles

RT0–RT4 are distinct target families with explicit ancestry and claim scopes. O1/O5/O10/O20 do not automatically create a full Cartesian tournament. Each mechanism/target/horizon combination requires an explicit Search Budget entry. Discovery uses, sensitivity horizons, and confirmatory claims remain separately classified.

## Unresolved decisions

1. exact continuous formulas for event-time-gap closure, source normalization/reversal, persistence, relationship continuation/break, timing, and magnitude/path;
2. whether any categorical targets have independently defensible boundaries;
3. source/peer role freezing and handling of bidirectional shocks;
4. path versus endpoint target semantics;
5. horizon-specific censoring and incomplete-path rules;
6. C04/C05/identifier eligibility through the outcome interval;
7. aggregation across components, observations/paths, directions, pairs, horizons, origins, and OF4 folds without creating a convergence score;
8. target-specific losses, calibration, uncertainty, and severe-failure rules;
9. finite target/horizon Search Budget and multiplicity families;
10. access controls, manifests, code versions, and contamination handling before outcome construction.

No target formula, categorical label, threshold, horizon-to-mechanism mapping, holding rule, metric, or computation is selected here.

`G4-04A5 APPROVED / FROZEN`
