# G3B-QA-R2 — Priority Access Execution

Status: **INSTITUTIONAL ENTITLEMENT NOT VERIFIED / TUSHARE QA BLOCKED PENDING RESEARCHER-CONFIGURED CREDENTIAL**  
Recorded: **2026-09-09**

## Authorization applied

The researcher accepted and committed G3B-QA-R1, selected institutional CSMAR/RESSET verification as Priority 1, authorized bounded Tushare fallback QA as Priority 2 only if no usable institutional entitlement could be verified, and retained paid exchange access as an unapproved escalation option.

`NO NEW PAID DATA COMMITMENT WITHOUT SEPARATE RESEARCHER APPROVAL`

## Priority 1 — final institutional entitlement check

The current Windows/browser/repository environment was checked without requesting, reading, transmitting or storing credentials.

| Route | Observed access state | Entitlement conclusion |
|---|---|---|
| CSMAR | Public site was reachable. `data.csmar.com` displayed an explicit **登录** action and no authenticated account/institution entitlement or accessible data workspace. | **NOT VERIFIED** |
| RESSET | Public site was reachable. `db.resset.com` displayed username/password inputs and a CARSI platform-login link; the current IP/session did not expose an authenticated database workspace. | **NOT VERIFIED** |
| Local environment | No active provider application, authenticated provider browser session, project provider integration, or exact provider-specific token environment-variable name was found. | **NO EXISTING USABLE ROUTE VERIFIED** |

This does not establish that the researcher's university lacks a subscription. It establishes only that no entitlement is usable from the current environment without researcher-led institutional authentication or access setup. The audit did not automate authentication dialogs or inspect credentials.

Consequently, no C01–C05 field/table, coverage, raw-price, corporate-action, suspension, export/API or licence capability can be contractually confirmed under an existing entitlement. Priority 1 does not satisfy the QA continuation condition.

## Priority 2 — bounded Tushare fallback QA readiness

Tushare remains:

`FALLBACK CANDIDATE — NOT CANONICAL / NOT FORMALLY SELECTED`

The researcher authorized a bounded fallback QA, but its runtime prerequisite is not present. Exact checks found neither `TUSHARE_TOKEN` nor `TUSHARE_API_TOKEN` environment configuration and no common user/repository Tushare configuration path. Values were never printed or inspected.

Therefore:

`TUSHARE FALLBACK QA = AUTHORIZED BUT NOT EXECUTABLE UNTIL RESEARCHER CONFIGURES CREDENTIAL LOCALLY`

No API call, sample download, schema probe or market-data acquisition was performed. This is an access prerequisite blocker, not a Tushare schema failure and not a core-strategy infeasibility result.

## Exact continuation boundary

Once the researcher configures a usable Tushare credential locally outside the repository, the bounded QA may proceed without placing that credential in command output, logs, manifests or Git. Before the first data request, the QA runner must verify only credential presence and establish:

1. deterministic QA security/date identifiers from the frozen QA plan;
2. exact requested endpoints/fields for C01/C03/C04/C05/E02/E03;
3. explicit `FALLBACK` provenance and reason code;
4. immutable `AUDIT/QA` raw path, manifest schema and checksum procedure;
5. request limits and stop conditions;
6. prohibition on relationships, returns analysis, measurements, targets and outcomes.

Tushare QA success would validate only fallback technical capability. It would not approve Tushare as canonical, authorize formal acquisition or promote any field to model use.

## Priority 3 — paid exchange access

No SSE/SZSE product was purchased or requested. Paid official access remains an escalation option only after a precise lower-cost contract failure is documented and separately approved by the researcher.

## Current stop state

G3B-QA remains **PARTIALLY COMPLETE / BLOCKED BY AUTHORIZED MARKET-DATA ACCESS**. The next executable step requires researcher-side institutional authentication/setup or local Tushare credential configuration. Full-universe acquisition and all empirical work remain unauthorized.

`G3B-QA PRIORITY ACCESS CHECK COMPLETE / AWAITING RESEARCHER ACCESS SETUP`
