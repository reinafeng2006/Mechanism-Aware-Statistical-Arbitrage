# G3B C04/C05 Authoritative Companion Coverage Resolution

Status: **BOUNDED RESOLUTION COMPLETE — FORMAL COVERAGE INCOMPLETE**

## C04 — Corporate actions / distributions

Official company/exchange disclosure records remain the authoritative source class. The bounded resolution confirmed that the public official interfaces do not provide a qualified, stable, complete bulk historical 2013–2025 action stream with a uniform schema, publication/effective dates, correction/replacement lineage and deterministic universe-wide export under the current source contract.

Formal authoritative C04 payload coverage acquired for the full 751-security universe: **0/751 complete security histories**.

The two official `601313 → 601360` documents are identity-resolution evidence, not a substitute for universe-wide C04 coverage. No Tushare/Sina adjustment factor was substituted. Raw/unadjusted C03 remains preserved, and every adjusted representation remains `CONSTRAINED / NOT AUTHORIZED FOR EMPIRICAL USE`.

Final C04 status: **FAIL — AUTHORITATIVE FORMAL COVERAGE INCOMPLETE**.

## C05 — Suspension / resumption / trading status

Official SSE/SZSE records remain the authoritative positive-event source class. The bounded resolution confirmed authoritative public query/notice surfaces, but not a complete, stable, bulk-machine-readable 2013–2025 state history with correction/vintage lineage for the full universe.

Formal authoritative C05 payload coverage acquired for the full 751-security universe: **0/751 complete security histories**.

Using only the E03-A benchmark trading calendar, C01 listing intervals and C03 row presence, structural QA flags **49,568 candidate unexplained security-sessions across 425 securities**. This is a coverage diagnostic, not a suspension label: without authoritative C05 positive records, every such gap remains `UNKNOWN MISSINGNESS` and may include suspension, source omission or another unresolved cause.

Structural state handling therefore remains:

- a C03 row supports `NORMAL TRADING OBSERVED` for that security/session;
- no official suspension/resumption state is assigned without a qualified positive record;
- absent C03 rows remain `UNKNOWN MISSINGNESS`;
- no row is imputed and absence from a public query is not treated as proof of normal trading.

Final C05 status: **FAIL — AUTHORITATIVE FORMAL COVERAGE INCOMPLETE / UNKNOWN MISSINGNESS PRESERVED**.

## Boundary

The task did not weaken the source hierarchy or silently introduce an aggregator. These failures are acquisition-contract coverage findings, not strategy or mechanism findings. They prevent dataset freeze under the currently frozen complete C04/C05 contract.
