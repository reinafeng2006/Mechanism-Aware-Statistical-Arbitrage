# G2B Approximation Gap Register

Status: **APPROVED / FROZEN — 2026-09-08**

| Frozen construct | Candidate operational approximation | Approximation gap |
|---|---|---|
| Conditional joint/response relationship | RR-DIST or RR-CORR simple baseline | Omits conditional direction, asymmetry, state dependence and explicit response uncertainty |
| Signed directional response | Coarse common-clock RR-SIGNED/P0-SIGN | May not resolve source/peer ordering, fast delay or within-clock reversals |
| Common exposure structure | Reconstructable benchmark/exposure information | May omit latent, changing or company-specific exposures; historical membership may be imperfect |
| Conditional/residual dependence | Residualization over available declared controls | Meaning is conditional on an incomplete control set; omitted common information remains |
| Economic Relationship Representation | Public industry/profile/company facts | Does not fully capture dated supplier/customer, substitute or opposite-exposure networks |
| Relationship state/change | Repeated trailing estimates and warnings | A warning is not proof of structural break; detection latency and gradual evolution remain |
| Multidimensional abnormality | A-MAG + A-SIGN core morphology set | Timing and residual morphologies may be absent; cannot be called complete abnormality coverage |
| Timing mismatch | Coarse ordered bars | Loses within-interval ordering and fast information-diffusion timing |
| M1 under-response | UR0/UR1 based on implementable Expected Response | Gap does not identify attention/diffusion; source linkage and rivals remain separate |
| M2 temporary pressure | MP0 plus accessible MP1 liquidity context | Excess move/liquidity association cannot establish exogenous temporary pressure |
| Positive event rejection | Dated official announcements with structured tags | Tagging may lose event nuance/direction; archive timestamp/version completeness may vary |
| Structural-linkage rejection | Static/delayed company relationship context | May detect changes late and miss unreported relationship evolution |
| U epistemic uncertainty | U0 plus U4 diagnostics | Does not quantify belief mass, calibrated uncertainty or an abstention policy |

## Proposed G3B-C1 data-qualification additions

Status: **APPROVED / FROZEN BY G3B-C1 — 2026-09-10**. These rows preserve the frozen constructs and add acquisition-derived gaps; they do not authorize measurements. Their C04/C05 states must propagate and cannot be cleared by dataset freeze or transformation.

| Frozen construct | Candidate operational approximation | Approximation gap |
|---|---|---|
| Clean raw security response | Available C03 raw/unadjusted observation | Authoritative C04 coverage is incomplete; observations may carry `CORPORATE_ACTION STATUS UNRESOLVED` and cannot automatically be treated as genuine abnormality |
| Continuous historical response path | Observed C03 sessions | 49,568 candidate security-sessions remain `UNKNOWN MISSINGNESS`; absence is neither a suspension nor a zero return and requires a candidate-specific rule |
| Historical security identity | Versioned `601313.SH → 601360.SH` identifier lineage | Same-security identifier continuity does not establish economic relationship continuity or authorize automatic price-history splicing |
| Adjusted-price representation | Provider-produced adjustment factors | Historical PIT corporate-action vintage/revision lineage is not qualified; adjusted specifications remain constrained/not authorized |

Approximation records do not authorize proxies or redefine constructs. Each gap remains visible in later specifications and validation.
