# MV-PIT Logical Data Contract

Status: **PROPOSED**

| Contract | Minimum required semantics | Permitted MV handling | Deferred branch |
|---|---|---|---|
| C01 | stable internal security ID; exchange; historical ticker/code where reconstructable; listing date; delisting date/status; C06 PIT membership linkage | Build from dated official SSE/SZSE records plus C06. Preserve source record, public/available time, extraction version and unresolved alias intervals. Never name-join silently. | Perfect unified versioned master and complete alias history |
| C03 | security ID; trade date; raw/unadjusted pre-close/OHLC; volume; amount; source/retrieval/schema/checksum lineage | Acquire only after the source-role decision. Preserve original raw payload before parsing; no adjusted product may substitute. | Canonical venue history until access exists |
| C04 | original action/document ID; security ID; action type/terms; announcement/publication, record, ex, payment/effective times; revisions | Acquire authoritative records where obtainable. Raw C03 may proceed if action reconstruction is incomplete, but no adjusted research representation is authorized. | Adjusted-price candidates RR-DIST/RR-COINT and any return definition needing complete adjustment |
| C05 | security ID; explicit suspension/resumption/trading state; effective interval/date; reason/source; available time | Use qualified official records with visible coverage limitations. Unexplained market gaps remain `UNKNOWN MISSINGNESS`; no imputation. | Fine intraday state and periods outside verified coverage |
| E02-A | directly observed raw volume and amount with documented units and C03 lineage | Include with C03 when raw semantics qualify. | None for raw activity; mechanism interpretation remains prohibited |
| E02-B | PIT total/float/free-float denominator; effective and available times; revision/vintage | Keep `CONSTRAINED / COMPETING-OR-ENHANCEMENT` until qualified. | Turnover-normalized MP1 and related comparisons |
| E03-A | benchmark ID plus raw/unadjusted index observations and common clock | Include if the C03 source decision explicitly covers the benchmark or another qualified source is approved. | Rich exposure inference |
| E03-B | constituent security ID; weight; announcement/publication and effective intervals; index version | Acquire only for surviving P0-EXP/RR-EXPOSURE specifications after source qualification. | Historical membership/weight exposure branch |
| C08 | immutable source/endpoint/request/retrieval/schema/checksum/count/coverage/fallback record | Mandatory for every snapshot; no overwrite. | None |
| C09 | later raw observations copied/routed to an access-separated outcome zone | May be co-acquired but never read by event-time feature paths. | Labels/horizons/targets remain unauthorized |

## Identity and missingness invariants

Each provider-native identifier maps to an internal ID through a versioned mapping record. Ambiguous mappings are quarantined. Missing canonical or governance-amended observations remain missing unless an explicit, reason-coded, field/date/security-scoped fallback decision is separately recorded.

Storage authorization does not establish event-time availability or feature-use permission.
