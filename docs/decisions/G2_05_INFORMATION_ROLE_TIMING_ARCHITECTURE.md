# G2-05 — Information Role & Timing Architecture Freeze Decision

Status: **APPROVED / FROZEN**  
Date: 2026-09-04  
Boundary: semantics and governance only. No factor, formula, estimator, threshold, probability model, classifier, update rule, window, provider or trade rule is selected.

## Decision objective

Define how point-in-time (`PIT`) information may legally enter the sequential strategy after a frozen Pair-Specific Multidimensional Abnormality State exists. The governing principle is:

`variable identity ≠ signal role`

An observable's role is determined by the construct it is used to measure, the decision time, its lawful availability, the mechanism hypothesis being assessed and the competing interpretations—not by its column name or data type.

## Frozen four-role architecture

### 1. Trigger Evidence

PIT information used to decide whether an existing multidimensional abnormality deserves active mechanism and resolution tracking. Trigger Evidence allocates attention; it does not identify M0/M1/M2/M3/U, assert temporary arbitrage, predict resolution or authorize a trade. Not every abnormality must activate tracking.

### 2. Mechanism Discriminator Evidence

PIT information available at the current decision time that raises or lowers relative support for competing M0/M1/M2/M3 interpretations or supports remaining in U. A discriminator is mechanism-relative and rival-aware. It need not produce a discrete label, and literature-supported direction is recorded only where the evidence ancestry justifies it.

### 3. Sequential-Updating Evidence

New PIT information arriving after tracking begins that changes mechanism belief, resolution belief, relationship credibility or uncertainty. The same information type may be initial Discriminator Evidence at one decision origin and Sequential-Updating Evidence when a genuinely new observation becomes available later. Reuse of an unchanged observation is not a new update.

### 4. Rejection / Rival Evidence

Positive PIT evidence that weakens a particular mechanism interpretation, the temporary-arbitrage interpretation or the validity of the underlying pair relationship. This role preserves M0's positive-rejection requirement and may support continued updating, rejection or U/abstention. Absence of M1/M2/M3 support is not positive M0 evidence.

The four roles are logical roles, not mutually exclusive variable inventories. One timestamped observation may be declared for more than one role only when each role, affected hypothesis and direction are recorded separately.

## Role assignment through time

For every use of an observable, the project must bind the value to a decision origin `t`, its public/PIT availability time and a declared role. A data type has no permanent role.

- Information already available when tracking is considered may serve as Trigger Evidence, a contemporaneous discriminator, rival evidence or cached context according to its declared construct.
- A later release or newly formed market observation may become Sequential-Updating Evidence at the first decision time when it is lawfully available.
- A value cannot be relabeled as "new" merely because the system recomputes it.
- A future realization can become an input only to a genuinely later sequential decision after its availability time. That does not make it a valid input at the original event time.
- When future catch-up, reversal, normalization, persistence, PnL or realized fundamentals are defined as final evaluation targets, they remain outcome-validation variables and cannot leak into the corresponding prediction origin.

## Required candidate metadata

Every future measurement candidate must record at least:

1. construct measured;
2. signal role or roles, separately declared;
3. mechanism or mechanisms affected, including U where relevant;
4. direction of evidentiary effect where theoretically supported, otherwise `UNRESOLVED`;
5. observation timestamp;
6. first public/PIT availability timestamp and applicable vintage;
7. data frequency;
8. update/latency class;
9. precomputed/cached versus latency-critical status;
10. competing interpretation or rival explanation;
11. contemporaneous input, sequential new information or outcome-only validation status;
12. Literature/Paper/Claim ancestry, or explicit `OBSERVATORY-ONLY HYPOTHESIS — NOT EVIDENCE` status;
13. current authorization status.

Each candidate must additionally carry the separate Production Feasibility record defined below. Research status and production feasibility must never be collapsed into one rating.

The metadata must preserve the following separation:

`measurement ≠ evidence ≠ signal ≠ mechanism belief ≠ resolution prediction ≠ trade decision`

A measurement is an operational value; evidence is its hypothesis-relevant interpretation under ancestry and limitations; a signal is an authorized decision-system use; beliefs and predictions are later model outputs; a trade decision is a still-later policy action.

## Multi-speed timing architecture

| Latency class | Conceptual role | Normal handling | Boundary |
|---|---|---|---|
| Slow prior/context | Dated economic/company relationship context and other slowly changing priors | Precomputed/cached with PIT vintage | Normally excluded from the latency-critical path |
| Medium relationship state | Current normal relationship, uncertainty and accumulated stability/break context | Updated on a separately governed relationship clock | Must obey anti-circularity; one anomaly cannot instantly redefine normality |
| Fast abnormality/market evidence | Current joint response and market-state information relevant to tracking attention | Evaluated at a decision origin using only then-available inputs | Abnormality/trigger does not identify mechanism or trade |
| Fast sequential update | Newly arriving discriminator, rival or resolution-relevant information | Applied only after its actual availability timestamp | Unchanged/recomputed data are not new evidence |

Slow company/economic information normally remains cached relationship context. A newly published company/event item may enter the fast path only at its actual PIT availability time and only as a separately authorized discriminator or rejection candidate. No update frequency is selected here.

## Production / Data Feasibility constraint

The primary production strategy should preferentially use variables that are economically meaningful, point-in-time reliable, broadly available, reproducible, computationally manageable and realistically maintainable across the target universe.

A theoretically attractive or literature-supported variable does not automatically enter the primary strategy when it depends on difficult, expensive, unreliable, proprietary, sparse, non-PIT or hard-to-reconstruct data. This creates a separate operational screen:

`research-useful diagnostic ≠ production-suitable signal`

Every future measurement/signal candidate must carry a `Production Feasibility` record with at least:

1. data availability;
2. PIT reliability;
3. historical coverage;
4. universe coverage;
5. required frequency;
6. acquisition complexity;
7. update latency;
8. computational burden;
9. reproducibility;
10. source stability;
11. proprietary or difficult-to-reconstruct dependency;
12. precomputable/cacheable status;
13. latency-critical-path status.

The permitted operational classifications are:

- `EASY / CORE-CANDIDATE`;
- `MODERATE`;
- `HARD / OPTIONAL`;
- `UNAVAILABLE / RESEARCH-ONLY`.

These labels describe operational feasibility only. They do not rank evidence quality, causal identification, predictive value or economic value. No specific candidate is classified in this proposal.

The complexity ladder is:

`easy, broadly available PIT variables → moderately complex derived variables → difficult intraday / proprietary / specialized variables only if justified`

A harder variable may supplement or displace a simpler alternative only after later frozen validation shows material incremental value at the level corresponding to its declared role: relationship quality, mechanism discrimination, resolution prediction or final economic performance. Final PnL cannot be the first justification for retaining a difficult relationship-level variable.

For example, a literature-supported high-frequency permanent/transitory decomposition may remain `HARD / OPTIONAL` or `UNAVAILABLE / RESEARCH-ONLY` if it requires trades, quotes or signed-flow infrastructure. This is an illustration of the classification rule, not a present classification or selection. Simpler daily PIT candidates remain eligible for priority comparison, but are not selected here.

## Input and outcome separation

| Category | Meaning | Permitted temporal use |
|---|---|---|
| Contemporaneous input | Available by the current decision origin | May be considered in an authorized trigger/discriminator/rejection use |
| Sequential new information | First becomes available after tracking begins | May update beliefs only at or after its actual PIT availability |
| Outcome target | Future path or realization defined to validate a prior prediction | Never an input at the originating decision time |

The same economic fact can move between these categories across decision times, but the immutable historical prediction origin and its information set must remain recoverable.

## Rejection and U/abstention

- M0 requires positive structural, fundamental, relationship-break or other admitted rejection evidence; it is not the residual of failed M1/M2/M3 attribution.
- Rejection evidence may target one mechanism without invalidating the pair, or may target temporary arbitrage or the relationship itself. The target must be explicit.
- `U = Unresolved / Abstain` remains an epistemic state throughout tracking. No active case is required to receive an M0–M3 label.
- Insufficient, contradictory, stale, unavailable or contaminated evidence may preserve U, continue tracking, or support rejection under later policy design. No action mapping is selected here.

## Non-prescriptive examples

These examples use admitted candidate concepts only; they are not factors, formulas, required inputs or hard gates.

| Candidate concept | Possible role at a stated time | What it cannot establish alone |
|---|---|---|
| Source response | Contemporaneous M1/M2 discriminator context; later newly observed response may be an update | M1, M2, causality or a trade |
| Peer under-response in the expected signed direction | Candidate M1 discriminator once measured relative to the frozen relationship object | Limited attention, future catch-up or trading validity |
| Turnover/liquidity context | Candidate M2 discriminator or rival/contamination check | Exogenous temporary pressure or later reversal |
| Newly published company-specific event | Timestamped discriminator or rejection evidence from its first PIT availability; earlier company profile remains slow cached context | A mechanism before publication, or pair validity merely from company similarity |
| Relationship-break evidence | Medium-state rejection/update evidence concerning the normal reference | M0 from one large deviation, or temporary abnormality by itself |

## Unresolved G2 measurement choices

The proposal deliberately defers:

- activation by fixed/soft threshold, ranking, resource budget, probability or continuous attention;
- measurement and normalization of every role;
- factor or observable selection and combination;
- evidentiary weights, belief representation and update rule;
- mechanism and resolution model structure;
- update frequency, clocks, windows, staleness tolerances and missing-data treatment;
- M1 under-response and M2 pressure/contamination formulas;
- M0 operational rejection criteria and U action policy;
- validation metrics and empirical winner;
- providers, database schema implementation and trading rules.
- candidate-specific Production Feasibility classifications and the evidence required to assign them;
- material-increment thresholds and validation designs for admitting harder variables.

## Frozen classification

### FROZEN SEMANTICS

- `variable identity ≠ signal role`;
- the four information roles and their non-equivalence;
- role assignment is construct-, mechanism-, context-, decision-time- and availability-dependent;
- the required candidate metadata categories;
- slow/medium/fast multi-speed architecture;
- strict contemporaneous/sequential/outcome separation;
- positive rejection, M0 and U boundaries;
- measurement/evidence/signal/belief/prediction/decision separation.
- the Production / Data Feasibility principle, mandatory feasibility record, four operational labels and complexity ladder;
- separate `Research Status` and `Production Feasibility Status` fields;
- role-matched incremental-value discipline for harder variables, including the prohibition on using final PnL first for relationship-level variables.

### G2 MEASUREMENT DECISION — DEFER

All operational definitions, candidate selections, role-specific measurements, activation approaches, clocks, frequencies, update mechanics, belief representation, uncertainty treatment, formulas, thresholds, models, candidate-specific feasibility ratings and incremental-value tests.

### EMPIRICAL VALIDATION — DEFER

Whether a candidate provides incremental PIT information; its latency, calibration, stability, contamination, rival-explanation sensitivity and OOS value; whether any role assignment generalizes without leakage; and whether harder production requirements deliver material role-relevant incremental value.

## Downstream implications

The Signal Model Registry must add role-and-timing metadata and separate `Research Status` and `Production Feasibility Status` before candidate measurements are frozen. Learning artifacts must teach that an observable is not intrinsically a trigger or mechanism signal, distinguish research usefulness from production suitability, and display the temporal transition from contemporaneous evidence to genuinely new sequential evidence while keeping outcomes separate.

## Approval record

Researcher approval on 2026-09-04 freezes the four information roles, `variable identity ≠ signal role`, mandatory PIT/timing metadata, multi-speed timing architecture, M0/U handling, layer separation, outcome-leakage boundary, Production/Data Feasibility as an independent dimension, its four statuses and the harder-variable incremental-value requirement exactly as documented above.

All specific variables, factors, formulas, thresholds, update frequencies, windows, models, providers, databases and trade rules remain unresolved. G2-06 remains unauthorized. This decision performs no implementation or empirical work.
