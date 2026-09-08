# Machinery Industry Scope Map

Version: **v1.0-frozen-primary-scope**
Status: **APPROVED / FROZEN**
Decision rule: economic scope only; never optimize membership using pair counts, history availability, returns or outcomes.

## Scope semantics

Core machinery means companies classified principally as manufacturing general-purpose or special-purpose machinery/equipment. A manufacturing super-category is never sufficient by itself. Adjacent vehicle, electrical-equipment, instrument and repair categories are not silently folded into core machinery.

| Taxonomy/version | Code | Published meaning | Scope decision | Rationale |
|---|---|---|---|---|
| CSRC Listed Company Industry Classification Guidelines (2012 revision) | C34 / 34 | General-purpose equipment manufacturing | INCLUDE | Direct core machinery/equipment semantics |
| CSRC Listed Company Industry Classification Guidelines (2012 revision) | C35 / 35 | Special-purpose equipment manufacturing | INCLUDE | Direct core machinery/equipment semantics |
| CSRC 2012 regime | C36 / 36 | Automobile manufacturing | EXCLUDE | Vehicle-production economics are distinct from core machinery |
| CSRC 2012 regime | C37 / 37 | Railway, ship, aerospace and other transport equipment manufacturing | EXCLUDE | Transport-equipment sector is distinct and highly specialized |
| CSRC 2012 regime | C38 / 38 | Electrical machinery and equipment manufacturing | OUT-OF-PRIMARY / EXTENSION-ELIGIBLE | Adjacent equipment exposure, excluded from the primary thesis unless separately authorized |
| CSRC 2012 regime | C40 / 40 | Instrumentation manufacturing | OUT-OF-PRIMARY / EXTENSION-ELIGIBLE | Adjacent capital-goods exposure, excluded from primary membership |
| CSRC 2012 regime | C43 / 43 | Metal products, machinery and equipment repair | OUT-OF-PRIMARY / EXTENSION-ELIGIBLE | Repair/service economics differ from primary equipment manufacturing |
| CAPCO Listed Company Industry Statistical Classification Guideline (effective 2023-05-01) / JR/T 0020—2024 | 34 (within manufacturing secondary class CG) | General-purpose equipment manufacturing | INCLUDE | Semantic continuation of core machinery |
| CAPCO 2023 / JR/T 0020—2024 | 35 (within CG) | Special-purpose equipment manufacturing | INCLUDE | Semantic continuation of core machinery |
| CAPCO 2023 / JR/T 0020—2024 | 36 (within CG) | Automobile manufacturing | EXCLUDE | Do not use the broad CG parent to admit vehicles |
| CAPCO 2023 / JR/T 0020—2024 | 37 (within CG) | Railway, ship, aerospace and other transport equipment manufacturing | EXCLUDE | Do not use the broad CG parent to admit transport equipment |
| CAPCO 2023 / JR/T 0020—2024 | 38 (within CH) | Electrical machinery and equipment manufacturing | OUT-OF-PRIMARY / EXTENSION-ELIGIBLE | Adjacent equipment exposure, excluded from primary membership |
| CAPCO 2023 / JR/T 0020—2024 | 40 (within CI) | Instrumentation manufacturing | OUT-OF-PRIMARY / EXTENSION-ELIGIBLE | Adjacent measurement/control equipment, excluded from primary membership |
| CAPCO 2023 / JR/T 0020—2024 | 43 | Metal products, machinery and equipment repair | OUT-OF-PRIMARY / EXTENSION-ELIGIBLE | Repair/service relationship differs from primary manufacturing |

## Cross-version controls

- Store the original published code, label, hierarchy and taxonomy version.
- The `INCLUDE/EXCLUDE/OUT-OF-PRIMARY / EXTENSION-ELIGIBLE` mapping is a separately versioned derived artifact.
- Similar-looking codes across versions are not overwritten into a timeless field.
- A taxonomy switch becomes usable only after the new result is publicly available.
- `OUT-OF-PRIMARY / EXTENSION-ELIGIBLE` rows cannot enter primary membership, pair formation, N0/N1 estimation or primary evaluation. Same-process, negligible-cost raw records may be retained only in a quarantined extension raw zone.

## Remaining researcher scope decisions

Codes 34/35 form the frozen primary universe; 36/37 are excluded; 38/40/43 are out of primary but extension-eligible. Any extension requires a separate versioned authorization made without outcome inspection. `acquisition breadth ≠ universe membership authorization`.
