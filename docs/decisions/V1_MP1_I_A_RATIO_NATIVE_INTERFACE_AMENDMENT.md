# V1 MP1-I-A Ratio-Native Executable Interface Amendment

Decision date: 2026-09-15

Amendment ID: `V1-MP1-I-A-1.0`

Status: **RESEARCHER APPROVED / FROZEN BEFORE A3/A5/A6/G5 COMPUTATION**

Ancestry: `V1-EXECUTABLE-SEMANTICS-A1` + `V1-MP1-A-1.0` + A6 `PV-M2` + `G5-TRADING-V1-1.1`

This versioned consistency amendment supersedes only the legacy MP1 executable interface. It does not mutate the historical frozen records.

The canonical MP1 object is `q_t = amount_t / volume_t`. Its PIT reference is `q_ref,t = median_PIT,H126(q)`, refreshed at U1W and carried within the week under `V1-MP1-A-1.0`. The sole executable normalized state is:

`MP1_ratio_log_state = log(q_t / q_ref,t)`.

The descendant A6 `PV-M2` additions are, in order:

`{MP0, MP1_ratio_log_state, MP1_ratio_available, mechanical_return_content, cause_proxy_overlap, endogeneity, overlapping_windows, future_leakage, flow_motive_ambiguity}`.

The unsupported legacy `MP1_amount_log_ratio`, `MP1_volume_log_ratio`, `amount_available`, and `volume_available` interface fields are removed. No separate `median_PIT(amount)` or `median_PIT(volume)` reference is introduced, and raw volume is not substituted for the removed normalization.

The descendant `TV1-M2 ELIGIBLE` conjunction replaces only its legacy positive-amount condition with: MP1 ratio state available and `MP1_ratio_log_state > 0`. All other frozen excess-move, contamination, rejection, invalidity, evidence-conflict, C04/C05/identity, signal and execution requirements remain unchanged. No additional numerical threshold is introduced.

`MP1_ratio_log_state > 0 != M2 identification`. `amount/volume` is not interpreted as a pure liquidity-pressure measure. It is a transaction-price/reference-state proxy in the already frozen contextual role and cannot alone create an M2 label or trade.

This amendment was required before empirical computation because the older interface referenced independently normalized historical amount and volume objects that were not authorized by the later canonical MP1-A specification. No outcome or empirical result informed it.

`V1-MP1-I-A-1.0 — APPROVED / FROZEN`
