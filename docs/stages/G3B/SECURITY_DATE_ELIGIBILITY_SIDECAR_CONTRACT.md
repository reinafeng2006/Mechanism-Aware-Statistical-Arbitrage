# Security-Date Eligibility Sidecar Contract

Status: **GENERATED / VALIDATED — IMMUTABLE GOVERNANCE METADATA / NON-EMPIRICAL**  
Schema: `SECURITY_DATE_ELIGIBILITY_SIDECAR_V1`  
Eligibility rule: `G3B-C1-C04-C05-ELIGIBILITY-V1`

## Artifact

- local immutable artifact: `data/qa_work/g3b_f2/security_date_eligibility/v1/security_date_eligibility_sidecar_v1.csv.gz`;
- manifest: `data/qa_work/g3b_f2/security_date_eligibility/v1/manifest.json`;
- rows: **1,575,837**;
- artifact SHA-256: `A4418E69EDAF92CE0A16DCE72FD6551DA245CF182252528CCB5224768EA9705A`;
- `NORMAL TRADING OBSERVED`: **1,526,269**;
- `UNKNOWN MISSINGNESS`: **49,568**;
- deterministic independent regeneration: **PASS**.

The local payload and manifest remain under the existing Git-ignored QA-data policy. The versioned generator is `tools/g3b_f2_build_security_date_eligibility.py`.

## Grain and fields

Unique grain: `stable_security_identity × observation_date`.

Stable ordered schema:

1. `stable_security_id`;
2. `observation_date`;
3. `historical_ticker_code`;
4. `identifier_lineage_state`;
5. `c04_structural_state`;
6. `c04_basis`;
7. `c05_structural_state`;
8. `c05_basis`;
9. `eligibility_rule_version`;
10. `upstream_artifact_references`;
11. `schema_version`;
12. `generation_version`.

There is deliberately no universal `eligible` field. Structural state is not candidate-specific measurement eligibility. Any later materialized candidate mask must be regenerated from this sidecar plus a frozen candidate eligibility rule/version.

## State construction

- C04 remains `CORPORATE_ACTION STATUS UNRESOLVED` throughout because authoritative universe-wide C04 coverage is incomplete.
- A date with an observed raw C03 row is `NORMAL TRADING OBSERVED`; this means an observation exists, not that it is corporate-action clean or eligible for every measurement.
- A benchmark session inside the C01 listing interval without a raw C03 row and without qualified C05 evidence is `UNKNOWN MISSINGNESS`.
- No absence becomes suspension, resumption, normal trading, a zero return, or a forward-filled observation.
- The `601313.SH → 601360.SH` lineage is represented without asserting economic continuity or splicing price series.

## Integrity

The manifest records upstream hashes for the raw acquisition manifest and journal, C06 union and membership artifacts, identifier-resolution register, and the bounded 601313 probe. Gzip output uses a fixed header time, stable columns, stable row ordering, and deterministic serialization. Generation refuses silent overwrite; `--verify-existing` validates an existing immutable artifact against a fresh deterministic reconstruction.

The sidecar contains no returns, pair relationships, abnormality, candidate measurement values, beliefs, targets, predictive outcomes, or PnL.
