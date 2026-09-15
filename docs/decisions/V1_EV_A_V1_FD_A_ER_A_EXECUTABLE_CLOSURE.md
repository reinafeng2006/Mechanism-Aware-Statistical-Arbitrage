# V1 EV-A-V1 + FD-A + ER-A Executable Closure

Decision date: 2026-09-15

Contract ID: `V1-EXECUTABLE-CLOSURE-EV-A-V1-FD-A-ER-A-1.0`

Status: **RESEARCHER APPROVED / FROZEN BEFORE DOWNSTREAM INNER COMPUTATION**

Ancestry: `G4-04A4` + `V1-EXECUTABLE-SEMANTICS-A1-MP1-I-A` + A6 PV0/PV-M1/PV-M2 + `G5-TRADING-V1-1.2-MP1-I-A`.

## General evidence state

Every Boolean evidence proposition is encoded by independent `present` and `unavailable` indicators: `(0,0)=ABSENT`, `(1,0)=PRESENT`, `(0,1)=UNAVAILABLE`; `(1,1)` is schema-invalid. This is categorical encoding, not an ordinal or scalar mechanism score.

`not observed != ABSENT`; `missing/unqualified != ABSENT`; `UNAVAILABLE != 0`; `morphology != mechanism evidence`.

## EV-A-V1

PV0 keeps the first 16 frozen columns. Each of the five U dimensions—measurement uncertainty, information insufficiency, mechanism ambiguity, evidence conflict and data/provenance uncertainty—then receives separate `present` and `unavailable` indicators. U is never inferred from all-zero mechanism fields.

Positive M0 receives `M0_present` and `M0_unavailable`. Presence requires an already-qualified PIT V1 positive-rejection source. Because V1 has no exhaustive qualified negative M0 coverage, an ordinary no-record case is unavailable, not absent. Absence of M1/M2, persistence, no detected event/action and missing evidence never create M0.

The legacy merged relationship-break/invalidity field is replaced by two propositions, each with present/unavailable indicators:

- `mechanical_or_data_invalidity`: determined only from frozen estimator non-convergence, non-finite state, invalid covariance, unsupported/invalid scale, eligibility failure, or required PIT/provenance/identifier failure;
- `relationship_break_evidence`: requires separately qualified positive PIT break evidence; without a qualified V1 break contract it is unavailable. One extreme abnormality or mechanical model failure never establishes a relationship break.

PV-M1 adds `M1_evidence_unavailable` and retains separate non-ordinal support, oppose and ambiguous indicators. Support requires qualified contextual M1 evidence and evaluable required evidence; UR morphology alone cannot set it. Oppose requires qualified positive rival/rejection evidence. Ambiguous requires evaluable support/opposition coexistence or multiple evaluated live explanations. Insufficient observability sets unavailable, not ambiguity. Under current V1, absent a qualified contextual identification source, `M1_evidence_unavailable=1`.

Each PV-M2 contamination proposition is independently three-state encoded:

- `mechanical_return_content`: formula/lineage audit establishes presence or absence; otherwise unavailable;
- `cause_proxy_overlap`: complete frozen role audit establishes overlap or separation; statistical relation alone is irrelevant; otherwise unavailable;
- `endogeneity`: qualified design/source evidence establishes endogenous risk, or qualified identification establishes exogeneity; otherwise unavailable;
- `overlapping_windows`: exact frozen intervals mechanically overlap or are disjoint; otherwise unavailable;
- `future_leakage`: input availability violates the cutoff, or complete lineage verifies all inputs were timely; otherwise unavailable;
- `flow_motive_ambiguity`: qualified motive evidence establishes multiple motives, or an exhaustive qualified contract excludes rivals; otherwise unavailable. MP0/MP1 presence alone is irrelevant.

Measurement uncertainty, information insufficiency, mechanism ambiguity, evidence conflict and data/provenance uncertainty follow the same positive/exhaustive/unavailable rule specified by the researcher. The five dimensions remain independent and may coexist. Invalid/unavailable observations are never ordinary zero-evidence rows.

`evidence-state encoding != mechanism classification != probability != belief != trade decision`.

## FD-A

Execution occurs only at the already-authorized next eligible open opportunity. Failure there produces `EXECUTION UNAVAILABLE`; no delayed fill, carry, anchor reset, trade, PnL, turnover, exposure or episode exists. The unavailable opportunity remains in deployability diagnostics. There is no delayed-fill V1 Search Budget.

## ER-A

Annualized return, volatility and derived annualized risk-adjusted metrics use exactly 252 trading sessions/year where mathematically applicable. Reports also preserve cumulative return, realized duration/support, raw/net PnL, trade count, turnover and maximum drawdown. Annualization is reporting only and cannot select candidates.

This closure uses no empirical information. OF4 and held-out remain denied.

`V1 EXECUTABLE SEMANTICS CLOSED`
