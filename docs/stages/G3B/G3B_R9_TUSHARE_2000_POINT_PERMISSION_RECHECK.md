# G3B-R9 — Tushare 2000+ Permission Re-check

Status: **PASS / G3B-FULL RESUME ELIGIBLE — RESEARCHER AUTHORIZATION REQUIRED**

## Account-visible confirmation

The researcher confirmed an account-visible balance of 2,120 points, including 2,000 points purchased on 2026-09-09 and valid through 2027-09-09.

`2000+ POINT TIER CONFIRMED`

No additional points were purchased or authorized. This supersedes the earlier `current tier unresolved` status.

## Bounded authenticated test

The same repository-external environment-variable path used by the acquisition runner was used without printing, logging, persisting, hashing or committing the credential. Four non-empirical requests were made:

| Endpoint | Request 1 | Request 2 | Effective behavior |
|---|---:|---:|---|
| `stock_basic` | PASS, 2,317 rows | PASS, 2,900 rows | Consecutive calls succeeded; no one/hour throttle or permission error |
| `daily_basic` | PASS, 2 rows | PASS, 2 rows | Consecutive calls succeeded; no one/hour throttle or permission error |

The two `daily_basic` requests cover only two named securities over two dates and exist solely to test permission/rate behavior. The `stock_basic` calls are current listing snapshots, not formal historical acquisition.

The successful consecutive endpoint calls demonstrate that the token available to the acquisition runner has effective permissions consistent with the newly active 2,000+ account tier. No credential value or account identifier was captured, so this is an operational permission correspondence rather than a credential-identity record.

Immutable raw QA payloads and the manifest remain Git-ignored under `data/raw/g3b_qa/tushare_permission_recheck_r9_v1/` with status `AUDIT/QA — NON-EMPIRICAL`.

## Preserved limitation

`permission upgrade solves access/throughput, not PIT/vintage qualification`

E02-B remains `PASS WITH LIMITATIONS`: historical values retrieved today do not establish their original `available_time`, source vintage, revision history or restatement lineage.

## Acquisition contract effect

- C01 and E02 no longer have an authenticated permission/rate blocker at the bounded re-check level.
- G3B-FULL is **resume eligible**, but remains paused pending a new researcher authorization.
- Resume must use the preserved journal/checkpoint and must not restart from zero or overwrite the eight existing successful C03 snapshots.
- All source, PIT, immutable-raw, outcome-quarantine and no-measurement boundaries remain unchanged.

`TUSHARE 2000+ PERMISSION RE-CHECK — PASS / G3B-FULL RESUME ELIGIBLE`

