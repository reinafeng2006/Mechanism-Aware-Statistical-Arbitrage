# V1 DC-A + EP-A Execution Semantics Freeze

Decision date: 2026-09-14
Contract ID: `V1-DC-A-EP-A-1.0`
Status: **APPROVED / FROZEN BEFORE MODEL FITTING**

## DC-A — decision-event cadence

Generate one event-time record for every authorized candidate-eligible session and every eligible pair-direction/relationship-candidate state under the frozen PIT, C04/C05, identity, C06, PAIR-A and candidate-specific eligibility contracts.

`decision-event cadence != relationship/state refresh cadence`.

Daily event generation does not re-estimate parameters. R0/R1/R3 refresh only on their frozen U1W/U1M clocks; R4 filters states at U1D and re-estimates Q/R only at U1M under CF-A. Overlapping O1/O5/O10/O20 labels remain subject to target-specific maturity, censoring, A6-TG-A and multiplicity rules.

## EP-A — active-episode admission

Episode identity is `unordered pair × policy channel`. M1 and M2 remain distinct policy channels. At most one episode for that identity may be active.

An otherwise eligible later signal during an active episode is recorded as `BLOCKED RE-ENTRY`. It creates no episode, PnL, trade count, position, new anchor, or reset of the exit/holding clock. The original episode retains its immutable event-time anchor until its frozen resolution-based or 10-eligible-session exit.

Directional scientific records remain separate. Opposite-direction and cross-pair exposures are not netted at the episode-definition layer. Security-level netting, exposure and concentration controls operate only in the downstream portfolio layer.

No weekly/monthly event sampling, overlapping episode stacking, replacement/reset, re-entry threshold or performance-dependent cooldown is authorized for V1.

No empirical value, event count, model output, outcome or PnL informed this freeze. OF4 remains inaccessible and the 2024–2025 held-out region remains sealed.

`V1-DC-A-EP-A-1.0 — APPROVED / FROZEN`
