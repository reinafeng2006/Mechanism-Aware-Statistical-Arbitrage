# Machinery Industry Scope Map

Version: **v0.1-pre-acquisition**  
Status: **BOUNDED VERSIONED MAP — AMBIGUITIES AWAIT RESEARCHER REVIEW**  
Decision rule: economic scope only; never optimize membership using pair counts, history availability, returns or outcomes.

## Scope semantics

Core machinery means companies classified principally as manufacturing general-purpose or special-purpose machinery/equipment. A manufacturing super-category is never sufficient by itself. Adjacent vehicle, electrical-equipment, instrument and repair categories are not silently folded into core machinery.

| Taxonomy/version | Code | Published meaning | Scope decision | Rationale |
|---|---|---|---|---|
| CSRC Listed Company Industry Classification Guidelines (2012 revision) | C34 / 34 | General-purpose equipment manufacturing | INCLUDE | Direct core machinery/equipment semantics |
| CSRC Listed Company Industry Classification Guidelines (2012 revision) | C35 / 35 | Special-purpose equipment manufacturing | INCLUDE | Direct core machinery/equipment semantics |
| CSRC 2012 regime | C36 / 36 | Automobile manufacturing | EXCLUDE | Vehicle-production economics are distinct from core machinery |
| CSRC 2012 regime | C37 / 37 | Railway, ship, aerospace and other transport equipment manufacturing | EXCLUDE | Transport-equipment sector is distinct and highly specialized |
| CSRC 2012 regime | C38 / 38 | Electrical machinery and equipment manufacturing | AMBIGUOUS-REVIEW | Contains equipment businesses but materially different electrical exposure; inclusion would broaden the thesis |
| CSRC 2012 regime | C40 / 40 | Instrumentation manufacturing | AMBIGUOUS-REVIEW | Related capital-goods characteristics, but not equivalent to general/special machinery |
| CSRC 2012 regime | C43 / 43 | Metal products, machinery and equipment repair | AMBIGUOUS-REVIEW | Service/repair economics differ from equipment manufacturing |
| CAPCO Listed Company Industry Statistical Classification Guideline (effective 2023-05-01) / JR/T 0020—2024 | 34 (within manufacturing secondary class CG) | General-purpose equipment manufacturing | INCLUDE | Semantic continuation of core machinery |
| CAPCO 2023 / JR/T 0020—2024 | 35 (within CG) | Special-purpose equipment manufacturing | INCLUDE | Semantic continuation of core machinery |
| CAPCO 2023 / JR/T 0020—2024 | 36 (within CG) | Automobile manufacturing | EXCLUDE | Do not use the broad CG parent to admit vehicles |
| CAPCO 2023 / JR/T 0020—2024 | 37 (within CG) | Railway, ship, aerospace and other transport equipment manufacturing | EXCLUDE | Do not use the broad CG parent to admit transport equipment |
| CAPCO 2023 / JR/T 0020—2024 | 38 (within CH) | Electrical machinery and equipment manufacturing | AMBIGUITOUS-REVIEW | Adjacent equipment exposure; requires explicit thesis-scope decision |
| CAPCO 2023 / JR/T 0020—2024 | 40 (within CI) | Instrumentation manufacturing | AMBIGUITOUS-REVIEW | Adjacent measurement/control equipment; requires explicit decision |
| CAPCO 2023 / JR/T 0020—2024 | 43 | Metal products, machinery and equipment repair | AMBIGUITOUS-REVIEW | Repair/service relationship is not manufacturing equivalence |

## Cross-version controls

- Store the original published code, label, hierarchy and taxonomy version.
- The `INCLUDE/EXCLUDE/AMBIGUOUS-REVIEW` mapping is a separately versioned derived artifact.
- Similar-looking codes across versions are not overwritten into a timeless field.
- A taxonomy switch becomes usable only after the new result is publicly available.
- `AMBIGUOUS-REVIEW` rows remain outside the formal core universe unless explicitly approved; they are not silently treated as exclusions from all future research.

## Remaining researcher scope decisions

Only codes 38, 40 and 43 require scope review. Codes 34/35 form the bounded core proposal; codes 36/37 remain excluded. Any later change requires a versioned decision record made without outcome inspection.
