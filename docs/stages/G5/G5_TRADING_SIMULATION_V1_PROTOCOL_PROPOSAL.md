# G5 Trading Simulation V1 Protocol Proposal

Status: **TRADE-A APPROVED / FROZEN FOR V1 — PNL LOCKED UNTIL C04-A + INNER ACTION**

Executable entry-state binding: `V1-EXECUTABLE-SEMANTICS-A1`. The exact threshold-free M1/M2 eligibility maps in that amendment define V1 directional economic-probe eligibility; they do not assert mechanism identification.

## Role and non-interference

Trading Simulation V1 tests whether scientifically admissible event-time information can map into economic value through a minimal interpretable policy. It is downstream validation only:

`Relationship -> Abnormality -> Mechanism Evidence -> Resolution Prediction -> Trading Policy -> Economic Validation`.

Trading performance cannot redefine, select, or rescue upstream relationship, abnormality, mechanism, or resolution evidence. No PnL may be computed or inspected before this protocol and its finite Search Budget are researcher-frozen.

## Trading eligibility

A decision record may enter the trading-policy layer only if:

- its upstream relationship candidate passed the applicable SR0 state and is authorized for the current temporal role;
- A3 and mechanism-evidence records are PIT-complete and their candidate-specific C04/C05/identity masks permit both signal and execution;
- expected direction and deterministic source/peer roles are defined without future information;
- no `UNKNOWN MISSINGNESS`, suspension, untradeable state, unresolved identifier transition, or unresolved C04 action interval contaminates signal-to-execution or the held position;
- any M0 positive rejection or relationship-break state is handled by the frozen eligibility rule;
- U dimensions are retained. U is not No Trade by definition, but V1 proposes no position when unresolved/conflicting information prevents a deterministic M1- or M2-consistent mapping.

No abnormality is forced to trade. Missingness is never repaired, filled, or assigned a return.

## Deterministic policy families

### `TV1-M1` — peer catch-up policy

When a preregistered M1-supporting evidence state is present and no blocking rival/quality state applies, hold the peer/follower in `sign(g_j,t)` direction, where `g_j,t = mu_j|i,t - y_j,t`. The source leg is zero in the minimal policy. This is a directional economic test of peer catch-up, not proof of M1.

For V1, “M1-supporting evidence state” is exactly the `TV1-M1 ELIGIBLE` conjunction frozen in `V1-EXECUTABLE-SEMANTICS-A1`; `UR0 > 0` is a morphology-based directional probe condition, not an M1 label or probability.

### `TV1-M2` — source normalization policy

When a preregistered M2-supporting evidence state is present with mandatory contamination metadata and no blocking rival/quality state, hold the source in `-sign(e_i,t)` direction. The peer leg is zero in the minimal policy. This tests source normalization separately from M1.

For V1, “M2-supporting evidence state” is exactly the `TV1-M2 ELIGIBLE` conjunction frozen in `V1-EXECUTABLE-SEMANTICS-A1`; positive primary amount context is a preregistered activity condition and is not proof of exogenous pressure.

### `TV1-COMB` — coexistence handling

If both policies qualify simultaneously, retain both legs before portfolio netting. They are not arithmetic opposites. If evidence conflicts without deterministic qualified mappings, generate no V1 position and retain the conflict/U reason.

Position directions are immutable functions of frozen event-time states and cannot be reversed after PnL inspection.

## Entry proposal and bounded threshold choice

V1 uses `ENTRY-STATE`, with no extra numerical trading-only abnormality threshold. Threshold alternatives are closed. This avoids turning trading optimization into a new abnormality-selection environment.

Signal at close `t` may execute no earlier than the next eligible session's open (`t+1 open`) using an execution price whose timestamp follows all signal inputs. If next-open data are not in the frozen acquisition and no separately authorized executable price exists, the bounded fallback is next eligible close; the choice must be frozen before PnL. Same-close execution is prohibited.

## Exit and holding

V1 freezes `EXIT-RESOLVE-10`: exit at the first later eligible decision when the signed originating gap/excess component reaches or crosses zero under the original event-time anchor, or at 10 eligible sessions, whichever occurs first. This condition is executable, threshold-free and preregistered. `EXIT-FIXED-10` is closed from V1.

The zero-crossing boundary has a natural event-anchor meaning; it is not a tuned percentage closure. Suspension pauses executable exit but not calendar/event history; untradeable intervals extend until the first eligible execution subject to a separately frozen maximum calendar-delay rule. If that delay cannot be bounded without arbitrary choice, the episode is trading-ineligible.

O10 motivates but does not equate to the 10-session maximum holding rule. O1/O5/O20 are not holding candidates in V1. Stop-loss/take-profit grids are excluded.

## Sizing, overlap, and portfolio accounting

Primary proposed sizing is equal notional per active policy leg at entry. One optional simple risk-normalized sizing using prior PIT MAD may be retained as a cost/risk sensitivity only; Kelly sizing and optimization are prohibited.

Portfolio rules proposed for V1:

- fixed gross capital budget normalized to 1.0; no borrowing and maximum gross exposure 1.0;
- net exposure is reported, not optimized to zero;
- each active pair-policy episode receives equal gross allocation within the contemporaneous active set;
- all legs involving the same security are algebraically netted before execution and costs;
- conflicting same-security legs offset; no grossing of economically cancelled positions;
- per-security absolute exposure is capped at 10% of capital and excess is proportionally scaled across contributing episodes;
- remaining capital is cash with zero return in V1;
- no pair or security may bypass the cap because it appears repeatedly; pair overlap, concentration, gross/net exposure, and scaling factors are logged daily.

The researcher approved the 10% cap and zero cash return for V1. A no-cap architecture is not permitted because unlimited concentration/leverage is incompatible with V1 governance.

## Execution, untradeability, and C04/C05

- primary execution price candidate: next eligible open; fallback candidate: next eligible close if open is unavailable in the authorized data contract;
- signal and execution timestamps, exchange calendar, price field/source, and delay are persisted;
- suspension, limit/untradeable state where qualified, and `UNKNOWN MISSINGNESS` prohibit assumed fills;
- no trade begins or closes at a fabricated price; unresolved fill stays pending only under the frozen delay rule, otherwise the episode is excluded with reason;
- authoritative C04 action coverage must span every holding interval. If an action affects a position, V1 either uses a separately qualified cash/share entitlement treatment or marks the episode unavailable; raw price movement alone is not economic PnL;
- Tushare/Sina adjustment factors cannot silently repair C04.

This makes qualified C04 trading-interval coverage a hard prerequisite for defensible Trading V1.

## Transaction costs and turnover

Proposed convention is cost per executed notional side:

- `TC10`: 10 bps one-way primary;
- `TC05`: 5 bps one-way sensitivity;
- `TC20`: 20 bps one-way sensitivity.

Each entry, exit, rebalance, and netted security-level change incurs cost on absolute traded notional. Round-trip cost is therefore 20 bps under TC10 before intermediate rebalancing. Turnover is `sum absolute security notional changes / capital` at each execution and accumulated by period.

The cost represents combined commissions, fees, taxes, spread, and simple slippage as a stylized all-in convention. It does not explicitly model asymmetric stamp duty or market impact; both are limitations. TC05/TC20 are mandatory cost sensitivities, not policy-selection environments.

## Economic metrics

Report at minimum, without feeding them upstream:

- gross and net cumulative performance;
- annualized return and volatility;
- Sharpe with zero cash/risk-free convention unless separately frozen;
- maximum drawdown;
- turnover and trade/episode count;
- gross/net exposure, per-security concentration, overlap and capacity flags;
- TC05/TC10/TC20 sensitivity;
- M1-policy, M2-policy, coexistence, and excluded/U decomposition where scientifically valid.

Hit rate is supporting only. All metrics include native eligibility/coverage and no-trade reasons. Economic multiplicity is separate from upstream scientific claims.

## Trading Search Budget proposal

Frozen primary V1 policy is exactly:

`ENTRY-STATE x {TV1-M1, TV1-M2, deterministic coexistence} x EXIT-RESOLVE-10 x EQUAL-NOTIONAL x NEXT-OPEN x TC10`.

Mandatory non-selection sensitivities: `TC05`, `TC20`. `EXIT-FIXED-10` and risk-normalized sizing are closed from V1. Next-close is not a performance branch; it may be used only if the authorized data contract structurally lacks next-open, and that substitution must be declared before PnL. No other entry, exit, holding, sizing, leverage, stop, take-profit, or execution branch is in V1.

## Temporal protocol

Trading-rule choices use only semiannual inner development and must be frozen before OF4. OF4 evaluates the already frozen selection procedure and is not a retuning environment. Trading artifacts are materialized and checksummed before interpretation. Final 2024–2025 access requires a later separate irreversible authorization.
