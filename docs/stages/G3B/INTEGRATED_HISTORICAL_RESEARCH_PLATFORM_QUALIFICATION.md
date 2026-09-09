# Integrated Historical Research Platform Qualification

Status: **EXTERNAL ACCESS / TRIAL / QUOTATION REQUIRED**  
Formal acquisition: **NOT AUTHORIZED**  
Public-web commercial discovery: **STOPPED**

## Objective

Identify one primary integrated platform capable of supporting the 2013–2025 historical research database across C01/C03/C04/C05/E02/E03, while retaining the already-qualified official C06 historical industry-classification path as the authoritative exception.

Preferred architecture:

`one primary integrated historical research platform + official C06 exception + minimum authoritative exceptions + documented fallbacks`

`historical research source ≠ necessarily future live production source`

The historical platform is judged on reproducible research-database construction. It is not required to be the eventual low-latency live feed. Any future live source selection requires its own PIT, latency, reliability, licence and maintenance qualification.

## Qualification priority

1. **CSMAR**
2. **iFinD**
3. **Choice**
4. **RESSET / Wind**, only if the first three fail qualification or pricing

This order is a bounded procurement workflow, not source selection. A lower-priority platform may qualify if a higher-priority one fails hard PIT/lineage requirements or is not economically obtainable.

## Hard platform test

For one platform to become the primary historical research candidate it must demonstrate, through authenticated fields/trial/entitlement and contract evidence:

- integrated C01/C03/C04/C05/E02/E03 coverage for SSE and SZSE;
- sufficient history to construct the proposed 2013–2025 research range;
- raw/unadjusted C03 semantics;
- security and identifier consistency across modules;
- trading-calendar and timestamp consistency;
- corporate-action and adjustment lineage adequate to separate raw records from derived adjusted representations;
- suspension/trading-status semantics distinct from missing observations;
- share-capital/free-float denominator definitions and effective-time history;
- benchmark/index price, constituent, weight and effective-time semantics where required;
- PIT/vintage/revision behavior or an explicit approximation gap acceptable under the frozen MV-PIT contract;
- programmatic API/Data Loader/batch export and reproducible snapshot retention;
- research storage/use licence compatible with immutable raw snapshots and deterministic lineage;
- price and maintenance burden consistent with the source-consolidation objective.

`commercial-grade source ≠ automatically PIT-qualified`

## External actions required — top three

### 1. CSMAR

Researcher-controlled action:

1. Log in through the university/library/VPN route or contact CSMAR through its official institutional channel.
2. Determine whether the institution already licenses the relevant Stock Market Series / China Stock Market Trading Database and companion security, corporate-action/share-capital, suspension and index modules.
3. Return only the accessible module/table names and the non-sensitive contract fields listed in `G3B_EXTERNAL_ACCESS_PENDING.md`.
4. If access is absent or incomplete, request a module-level quote limited to C01/C03/C04/C05/E02/E03, including Data Loader/API/export capability and research-storage terms.
5. Request an authenticated data dictionary or bounded trial/sample sufficient for field/PIT qualification—not a full dataset.

Required evidence: entitlement/module result, exact tables/fields, coverage start, delisted-security coverage, raw-price semantics, publication/available/vintage/revision fields, export/API limits, licence and quoted term.

Status: **EXTERNAL ACCESS / ENTITLEMENT / QUOTATION REQUIRED**.

### 2. iFinD

Researcher-controlled action:

1. Use an existing authorized iFinD account, or request official Quant API trial access; do not create or transmit credentials to the repository/chat.
2. Confirm whether the account/trial includes Basic Data, Date Series, Historical Quotation and relevant Topic Report indicators for the six contracts.
3. Request a formal-user quote supporting history from at least 2013, because published free/trial history limits do not by themselves satisfy the target period.
4. Provide only non-sensitive function/indicator names, history limits, extraction limits, PIT/vintage statements, licence and quote terms.
5. If trial API is granted, separately authorize the already-defined tiny `AUDIT-ONLY / NON-EMPIRICAL` schema/PIT QA before any call.

Required evidence: account class, exact functions/indicators, raw/unadjusted flag semantics, corporate-action/factor ancestry, suspension/status fields, capital denominators, index constituents/weights, available-time/revision support, API limits, licence and price.

Status: **EXTERNAL TRIAL / API ACCESS / QUOTATION REQUIRED**.

### 3. Choice

Researcher-controlled action:

1. Contact the official Choice account manager or responsible university contact to request Quant API trial entitlement; the university edition must not be assumed to include API access.
2. Confirm exact Quant API functions for C01/C03/C04/C05/E02/E03 and history extending to 2013.
3. Request a module/API quote and research-use/export/storage terms.
4. Return only non-sensitive function/field names, coverage, PIT/vintage/revision statements, API limits and quote terms.
5. If trial API is granted, separately authorize the defined tiny `AUDIT-ONLY / NON-EMPIRICAL` schema/PIT QA.

Required evidence: exact functions/fields, raw-price and adjustment semantics, historical security/status/action/capital/index coverage, first-available/vintage/revision support, API/export limits, licence and price.

Status: **EXTERNAL TRIAL / API ACCESS / QUOTATION REQUIRED**.

## Prohibited actions and stopping rule

- No additional broad unauthenticated/public-web commercial-source discovery.
- No purchase, trial registration, personal-information submission or licence acceptance by the project agent.
- No formal data acquisition or empirical inspection.
- No source promotion based on marketing materials, trial availability or field count.
- RESSET/Wind outreach starts only after a documented qualification or pricing failure for the first three, unless the researcher explicitly changes priority.

Resume only when the researcher returns non-sensitive authenticated access, trial or quotation evidence for a priority platform.

`INTEGRATED HISTORICAL RESEARCH PLATFORM QUALIFICATION — EXTERNAL ACTION PENDING`
