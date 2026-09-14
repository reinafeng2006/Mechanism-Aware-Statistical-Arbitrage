# V1 Phase 1 Decision-Cadence and Episode-Admission Blocker

Date: 2026-09-14
Status: **GENUINE SCIENTIFIC-INTEGRITY BLOCKER / RESEARCHER DECISION REQUIRED**

## Why execution stopped before the first fit

`A6-TG-A` is frozen and published, but the existing protocol intentionally freezes only:

`market/abnormality evaluation cadence != relationship re-estimation cadence`.

It never selects the market/abnormality decision-event cadence. Semiannual origins define inner evidence blocks; U1D/U1W/U1M define model/state refresh clocks. Neither determines whether A3 evidence and A5/A6 targets are generated every candidate-eligible session, weekly, monthly, or only at the semiannual boundary.

This choice changes the estimand support, overlapping outcomes, multiplicity, A6 row population, and G5 opportunity process. The structural pair-date count is a feasibility count, not authority to select daily scientific evaluation.

G5 also does not state what happens when the same unordered pair and policy channel produces a new eligible signal while an earlier episode remains active. Stacking, replacing the event-time anchor, and ignoring re-entry produce different holdings and PnL. Exposure caps and security-level netting do not resolve this episode-admission semantics.

No relationship model, abnormality, target, or PnL was computed before this stop. OF4 and held-out were not accessed.

## Bounded decision alternatives

### Decision-event cadence

- `DC-A — EACH CANDIDATE-ELIGIBLE SESSION` (recommended): generate one event-time record per qualified pair-direction/candidate/session. Model refresh remains independently U1D/U1W/U1M. This best matches the dynamic abnormality and next-open trading objective but creates overlapping outcome labels that remain governed by frozen maturity/censoring rules.
- `DC-B — FIRST CANDIDATE-ELIGIBLE SESSION OF ISO WEEK`: lower dependence and compute, but discards within-week event information and changes the intended monitoring frequency.
- `DC-C — SEMIANNUAL ORIGIN ONLY`: maximally sparse and simple, but weakly aligned with daily state filtering and the V1 trading-validation objective.

No cadence may be selected based on realized event counts, survival, returns, or performance.

### Active-episode admission

- `EP-A — ONE ACTIVE EPISODE PER UNORDERED PAIR × POLICY CHANNEL; IGNORE NEW ENTRY UNTIL EXIT` (recommended): retain the original event-time anchor and exit rule; later signals are logged as blocked re-entry, not new positions. Opposite directions are not silently netted at the episode-definition layer.
- `EP-B — ALLOW DISTINCT OVERLAPPING EPISODES`: preserve every eligible signal as a separately anchored episode before portfolio netting. This is faithful to all events but materially increases repeated exposure and dependence.
- `EP-C — REPLACE/RESET ACTIVE EPISODE`: not recommended because a later signal rewrites the holding anchor and exit clock; it requires an additional replacement priority rule.

## Recommended resolution

Freeze `DC-A + EP-A`. It preserves daily scientific evaluation without equating it to relationship refresh, keeps each episode's event-time state immutable, prevents implicit signal stacking, and requires no performance-selected threshold. It also matches the already benchmarked complete pair-date execution geometry.

After publication, resume from `V1-PHASE1-INNER-INPUT-1.0`; do not rebuild the input. OF4 2020–2023 remains inaccessible and 2024–2025 remains sealed.

`V1 DECISION CADENCE / EPISODE ADMISSION BLOCKER — RESEARCHER DECISION REQUIRED`
