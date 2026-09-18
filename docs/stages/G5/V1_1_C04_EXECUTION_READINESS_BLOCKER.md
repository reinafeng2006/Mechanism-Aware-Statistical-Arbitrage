# Trading V1.1 C04 coverage prerequisite failure

Date: 2026-09-18. Status: **POLICY COMPLETE / PRE-PNL DATA QUALIFICATION BLOCKER**.

The researcher approved the complete [simultaneous-admission policy](../../decisions/V1_1_SIMULTANEOUS_ADMISSION_FINAL_FREEZE.md). No further allocation-policy decision is requested. Eight synthetic accounting tests pass, including same-open order invariance, A+B counting, preserved survivors, no cap redistribution, maximal common cash scaling, passive drift, net-security costs and exit clocks. No trading data values or PnL were computed/inspected.

## Verified structural evidence

The only registered C04-A calendar is [C04_A_OFFICIAL_CALENDAR_V1.json](../../../data/manifests/C04_A_OFFICIAL_CALENDAR_V1.json). It declares:

- status: `IMMUTABLE C04-A DESCENDANT — V1 INNER DEVELOPMENT ONLY`;
- empirical role: `2013-2014 formation reserve plus 2015-2019 inner development only`;
- last archive period: `2019-12`.

Exact verified exclusion SHA-256: `B63188E35EF76A3B8E5DAE4F02FE68CE2033ED5554113DBE30CEF3B3C993F910`.

Repository manifest/decision discovery and external OF4/final-held-out metadata inspection found no qualified post-2019 C04 descendant. `v1_of4_materialize.py` extends the input dates but reuses `v1_phase1_prepare.py` and its original `C04` path. The preparation code excludes only dates found in that calendar; the existence of a 2020-2025 input matrix does not extend the calendar's qualification. No market prices, coefficients, losses, outcomes or PnL were inspected for this finding.

## Why execution cannot be labelled qualified

The inherited trading contract requires qualified C04 coverage across signal, execution, holding and exit intervals. No identified action under a qualified bounded calendar is already weaker than authoritative action-clean status; no calendar coverage at all cannot be promoted to that qualified state.

Using the existing post-2019 mask as a sufficient trading-execution gate would silently pass a missing prerequisite. Backfilling synthetic entitlements, assuming no actions, dropping unknown intervals and renormalizing survivors are prohibited. This finding does not rewrite or automatically adjudicate prior immutable research results; their byte-integrity receipts are distinct from this downstream trading-use qualification.

## Bounded resolution

1. Authorize a separate bounded C04 qualification/acquisition extension through 2025 using the existing source contracts, with immutable source ancestry and no changes to trading policy. Then validate and execute the approved six-book protocol.
2. Alternatively, explicitly accept OF4/final-held-out trading as unavailable for C04 coverage and authorize a limited closure reporting that limitation, with only independently qualified inner trading execution. Do not label unavailable periods zero-return, no-trade performance or negative H6 evidence.

Neither resolution is selected by the agent. The current authorized task contains no new source acquisition permission, and silently reducing the registered economic evaluation would change the requested execution scope. Execution is paused before the first PnL; no final V1 tag is created.
