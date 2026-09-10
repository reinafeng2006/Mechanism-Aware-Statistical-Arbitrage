# G4-04 Statistical Governance Architecture Freeze

Decision date: 2026-09-10
Status: **APPROVED / FROZEN**

## Frozen architecture

- metrics follow stage-specific estimands; no universal performance metric ranks all stages;
- effect magnitude, uncertainty, statistical significance, temporal consistency, and support remain distinct evidence dimensions;
- arbitrary compensatory weighted scores are prohibited;
- SR0 structural/admissibility requirements are distinct from performance thresholds;
- inner and OF4 aggregation remains multidimensional;
- selection does not force a unique winner;
- multiplicity follows the dependency graph and preregistered comparison families;
- FWER-style control is available for suitable small confirmatory families;
- FDR-style control is available only for suitable preregistered screening families;
- exploratory/reopened analyses cannot support confirmatory claims;
- registered sensitivity-budget tiers remain separate from primary selection;
- sensitivity evidence cannot be mined to rescue or opportunistically select a primary winner.

`statistical significance alone is neither necessary nor sufficient for advancement`.

`metric choice must follow the stage-specific estimand`.

`strong performance in one outer fold cannot automatically compensate for severe instability elsewhere`.

## Deferred numerical specification

Exact metrics, meaningful-effect thresholds, uncertainty rules, alpha/q levels, aggregation statistics, severe-failure cutoffs, correction procedures, and sensitivity execution counts remain unresolved for G4-04A and subsequent bounded protocol decisions. This freeze authorizes no data access or computation.
