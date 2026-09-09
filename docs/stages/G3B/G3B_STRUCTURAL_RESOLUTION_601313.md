# G3B Structural Resolution — 601313.SH

Status: **VALID HISTORICAL SECURITY — C01 MAPPING REQUIRED**

Official CSRC historical classification records identify `601313` as **江南嘉捷**, an SSE-listed company classified in industry 34 during the relevant historical snapshots. The identifier is therefore valid historical C06 content, not an excludable parsing artifact.

The company's official code-change announcement states that holdings registered under `601313` were removed under that code and added under `601360` without changing investors' share quantities. The new code and name, `601360 / 三六零`, became effective on 2018-02-28.

The bounded provider-behavior probe found:

- Tushare `daily` and `daily_basic` return zero rows for historical code `601313.SH`;
- the same endpoints return 1,135 rows covering the pre-change period when queried under successor code `601360.SH`;
- Tushare therefore keys the earlier history to the current/successor code rather than preserving the historical code as a queryable security-master interval.

Frozen mapping:

`601313.SH / 江南嘉捷 / SSE / valid through 2018-02-27`

`→ same-security code change →`

`601360.SH / 三六零 / valid from 2018-02-28`

This mapping repairs the C01 identifier join but does not imply continuing machinery-industry membership after the official classification changes. C06 PIT snapshots continue to control industry membership at each date.

Provenance and hashes are recorded in `registers/G3B_IDENTIFIER_HISTORY_RESOLUTION_REGISTER.jsonl`; official raw PDFs and the two bounded provider probes remain immutable and Git-ignored.

