# G3B Source Consolidation / Minimum Source Count

Decision status: **APPROVED / FROZEN — 2026-09-09**  
Decision type: acquisition-design extension; no source selection or purchase authorization.

## Frozen production architecture preference

`one primary integrated data platform + the minimum number of authoritative exceptions + documented fallbacks`

Among source architectures that satisfy the required data-integrity and PIT standards, prefer the architecture with fewer independently maintained sources.

This preference is subordinate to hard PIT, lineage, licensing and construct-integrity requirements. Source count must never be reduced by accepting a platform that fails a hard requirement.

## Evaluation dimensions

An integrated platform must be evaluated across C01/C03/C04/C05/E02/E03 on:

- integrated logical-contract coverage;
- PIT consistency across modules;
- identifier consistency;
- timestamp and trading-calendar consistency;
- cross-module corporate-action consistency;
- API/export consistency;
- licensing and retention consistency;
- operational maintainability;
- number of independently maintained production integrations;
- `Source Fragmentation` operational risk.

Field count and vendor brand are not substitutes for these properties.

## Architecture classes

Preference order, conditional on hard qualification:

1. `ONE-PLATFORM QUALIFIED`;
2. `ONE-PLATFORM + AUTHORITATIVE EXCEPTION`;
3. `TWO-SOURCE MODULAR`;
4. `HIGHLY FRAGMENTED`.

These are architecture/operations classifications, not rankings of predictive value.

## Preserved exceptions and fallbacks

- The qualified official C06 historical industry-classification path remains a separate authoritative exception. It must not be migrated solely to reduce source count.
- Sina and Tushare remain documented fallback/cross-check sources unless separately promoted.
- A fallback cannot silently patch a primary platform observation.
- A platform that covers most fields but fails a hard PIT/lineage contract may remain an enhancement or fallback; consolidation cannot cure non-qualification.

## Scope unchanged

No provider, product, price, physical field, model-use permission or acquisition is selected. G3B remains pre-acquisition.
