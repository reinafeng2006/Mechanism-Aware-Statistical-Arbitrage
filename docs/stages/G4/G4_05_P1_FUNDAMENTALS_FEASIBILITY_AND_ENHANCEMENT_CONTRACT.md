# G4-05 P1 Fundamentals Feasibility and Enhancement Contract

Status: **AUTONOMOUS NON-EMPIRICAL AUDIT COMPLETE / SCIENTIFIC AND ACQUISITION DECISIONS DEFERRED**
Action: `G4-05-PREEMPIRICAL-ADVANCEMENT-V1`

## Dependency conclusion

The frozen five-construct B1 information set is not present as a qualified PIT feature layer in `CORE-DATASET-FREEZE-V1`. R2 design can be completed, but no R2 candidate using these constructs can become computation-authorized until a separately versioned `P1 FUNDAMENTALS ENHANCEMENT LAYER` is source/field qualified, acquired under separate authority, and frozen.

This is a data-contract dependency, not evidence that R2 is desirable, predictive, or infeasible.

## Logical-field feasibility matrix

| Frozen construct | Required logical raw fields | PIT requirements | Current contract status | Mechanical conclusion |
|---|---|---|---|---|
| Scale | total market capitalization primary; total assets robustness | market cap must bind price/share lineage; assets use first-public time and vintage | market-cap ingredients partly covered under E02 limitations; assets absent | `REQUIRES VERSIONED P1 ENHANCEMENT`; market-cap field semantics need qualification |
| Profitability / Quality | net/operating profit and total assets for ROA; operating profit and revenue for margin robustness | fiscal period, announcement/available time, original vintage, restatements | no frozen fundamentals layer | `REQUIRES VERSIONED P1 ENHANCEMENT` |
| Leverage / Capital Structure | total liabilities and total assets; debt/equity robustness | consistent accounting scope, first-public time, restatement lineage | no frozen fundamentals layer | `REQUIRES VERSIONED P1 ENHANCEMENT` |
| Growth | current and comparable base-period operating revenue; operating-profit growth robustness | both periods' PIT vintages, denominator-quality state, release time | no frozen fundamentals layer | `REQUIRES VERSIONED P1 ENHANCEMENT` |
| Valuation | PIT book equity plus market cap; PIT earnings plus market cap robustness | mixed market/fundamental clocks, valid denominator, vintage lineage | market component limited; fundamental component absent | `REQUIRES VERSIONED P1 ENHANCEMENT` |

Existing E02 liquidity stays P0 and C06 stays P0 structural context. Directed business linkage remains unqualified P1 and outside the initial Search Budget.

## Enhancement-layer contract

Any later acquisition must create a new immutable descendant layer, not mutate the core:

`CORE-DATASET-FREEZE-V1 -> P1-FUNDAMENTALS-ENHANCEMENT-Vn -> PIT-aligned feature state -> frozen R2 feature-set version`.

Minimum metadata: security identity, fiscal period, logical/physical field, units/accounting scope, source and vintage, first-public and available time, retrieval time, revision/restatement ancestry, feature generation version, carry-forward state, age/staleness, missingness reason, upstream hashes, and permitted B1 bundle/role.

## Existing-source feasibility boundary

The repository contains an approved Tushare historical-platform role for C01/C03/E02/E03-A, but no frozen decision qualifies Tushare fundamental endpoints, announcement timestamps, historical vintages, revision lineage, or licensing for this P1 layer. Extending that platform is a candidate audit path only—not an authorized provider extension or acquisition. Official filings/disclosures are an authoritative semantic reference already permitted as a source class, but no automated PIT fundamentals contract is frozen.

No new provider is proposed. Qualification must test the existing-source path against each logical field rather than assume platform-wide suitability.

## Required pre-acquisition qualification

1. exact physical field and accounting definition for every primary/robustness variable;
2. first-public/available-time field or defensible reconstruction;
3. original and restated-vintage preservation;
4. 2013–2023 development coverage and identifier consistency without inspecting values/distributions;
5. lawful local storage and deterministic batch/export capability;
6. immutable snapshot/manifests and explicit ancestry to the core freeze;
7. no change to the frozen five constructs, transformations, P0/P1 roles, or Search Budget.

Acquisition remains unauthorized. The next permitted data step would be a bounded authenticated field/PIT qualification action approved by the researcher.

