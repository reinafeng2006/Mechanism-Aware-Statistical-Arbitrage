# G3B-R8 — Tushare Authenticated Integrated-Platform QA

Status: **ACCEPTED / COMPLETE**  
Formal acquisition: **NOT AUTHORIZED**  
Higher-tier purchase: **NOT AUTHORIZED**

## Objective

Determine whether the minimum accessible Tushare permission tier can support a bounded C01/C03/C05/E02/E03 QA for the 2013–2025 historical research platform. C04 is explicitly outside the pass set and remains separately constrained.

## Prior access result

The QA runner was inspected before execution and does not print, log, persist, transmit, hash or commit the credential. A presence-only check found no `TUSHARE_TOKEN` in:

- the current process environment;
- the Windows user-level environment;
- the Windows machine-level environment.

No credential value was accessed or displayed. No API request was made. This is:

`ACCESS BLOCKED — NOT API FAILURE / NOT SCHEMA FAILURE / NOT DATA UNAVAILABLE`.

## Minimum-tier rule

Use only the lowest already-available permission tier that exposes the authorized endpoints. Do not purchase or request a higher tier during QA. If a contract is semantically functional but blocked only by an observed quota/frequency ceiling, record the exact endpoint, tier, limit and required acquisition volume for later researcher decision.

## Authorized endpoints and tests

| Contract | Candidate endpoints | Bounded authenticated test |
|---|---|---|
| C01 | `stock_basic` | SSE/SZSE identifiers, listing/delisting/status fields, current-vs-historical limitation, deterministic join behavior |
| C03 | `daily` | early/late raw-labelled OHLCV/amount, units, SSE/SZSE, missing sessions, repeated retrieval checksum |
| C05 | `suspend_d` | known suspension/resumption case; distinguish explicit status from absent daily row |
| E02 | `daily_basic` plus C03 volume/amount | separate observed activity from turnover and total/float/free-share denominators; document units and present-day historical-query limitation |
| E03 | `index_daily`, `index_weight` | benchmark prices and dated weights/constituents; distinguish `trade_date` from announcement/effective/available time |

`adj_factor` is not needed to pass C01/C03/C05/E02/E03 and must not be used to imply C04 qualification. A later comparison-only probe requires separate explicit scope if needed.

## Deterministic QA slice

When access is available, use only technically selected cases:

- one SSE and one SZSE security;
- one early interval near the 2013 boundary and one late interval;
- one externally documented suspension case;
- one benchmark with dated constituent/weight history;
- share-capital and turnover fields for the same fixed securities/intervals.

Artifacts remain immutable `AUDIT/QA — NON-EMPIRICAL`, stored under ignored raw QA paths with sanitized request IDs, manifests and checksums. Credentials and account identifiers are prohibited.

## Required outcomes

Each of C01/C03/C05/E02/E03 receives `PASS`, `PASS WITH LIMITATIONS`, `FAIL` or `UNRESOLVED`. Until authenticated execution, all remain `UNRESOLVED`.

If all five pass or pass with explicit non-core limitations, produce:

`Tushare primary integrated candidate + official C04 + official C06 + AKShare source-specific fallbacks/cross-checks`

and state the exact residual C04 action/vintage/adjustment-lineage gap and minimum additional production integrations. QA success alone cannot approve this architecture.

## Resume requirement

The researcher must configure a legitimate Tushare credential outside the repository so that a newly started Codex process can detect `TUSHARE_TOKEN`. Do not send the token in chat. After a presence-only check succeeds, execute only this contract.

Authenticated access subsequently became available through a repository-external process environment. The bounded runner executed without printing, logging, persisting, hashing or committing the credential. Results are recorded in `G3B_R8_TUSHARE_AUTHENTICATED_QA_CHECKPOINT.md`.

`G3B-R8 TUSHARE AUTHENTICATED QA ACCEPTED / COMPLETE`
