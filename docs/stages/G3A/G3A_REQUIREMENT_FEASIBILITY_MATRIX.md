# G3A Requirement Feasibility Matrix

Status: **APPROVED / COMPLETE — FEASIBILITY ONLY**  
Interpretation: technical feasibility only; never alpha, identification strength or model quality. Minimum and enhancement requirements are separate.

| Candidate | Feasibility outcome | Minimum information / source class | Enhancement and dependency finding |
|---|---|---|---|
| P0-RAW | FEASIBLE — CORE REQUIREMENTS | Authorized market history and security master | Fine clocks limited; adjustment/delisting vintages require audit |
| P0-EXP | FEASIBLE WITH LIMITATIONS | P0-RAW plus benchmark/exposure class | Rich contexts partial; inherits P0-RAW |
| P0-RES | FEASIBLE WITH LIMITATIONS | P0-RAW plus declared PIT conditioning | Broader controls partial; all conditioning vintages inherited |
| P0-STAB | FEASIBLE WITH LIMITATIONS | Repeated versioned relationship histories | Multi-regime context partial; representation inherited |
| P0-SIGN | FEASIBLE WITH LIMITATIONS | Ordered joint observations/state context | Fine asymmetry/state coverage partial |
| P1-ECR | PARTIALLY FEASIBLE | Dated filings/company/industry facts | Historical directed links sparse/costly |
| RR-DIST | FEASIBLE — CORE REQUIREMENTS | P0-RAW adjusted paths | Scaling feasible; path lineage inherited |
| RR-CORR | FEASIBLE — CORE REQUIREMENTS | P0-RAW aligned returns | Conditional variants limited by context |
| RR-EXPOSURE | FEASIBLE WITH LIMITATIONS | P0-EXP | Factor vintages/constituents require audit |
| RR-RESID | FEASIBLE WITH LIMITATIONS | P0-RES | Rich controls partial; conditioning lineage inherited |
| RR-STOCH | FEASIBLE WITH LIMITATIONS | Ordered market history | State extensions partial; repeated vintages needed |
| RR-COINT | FEASIBLE WITH LIMITATIONS | Long adjusted-price history | Sparse/new listings constrain coverage |
| RR-SIGNED | FEASIBLE WITH LIMITATIONS | P0-SIGN | Coarse direction feasible; causal ordering constrained |
| GOV-FDR | FEASIBLE — CORE REQUIREMENTS | Complete candidate universe/test outputs | Dependence-aware variants possible; completeness essential |
| GOV-MATCH | FEASIBLE — CORE REQUIREMENTS | Candidate graph/security IDs | Capacity context optional; inherits candidate completeness |
| N0 | FEASIBLE WITH LIMITATIONS | Industry vintages plus selected P0/P1/RR | Conditional on G2 choice; burdens inherited |
| N1 | FEASIBLE WITH LIMITATIONS | Pair history plus same selected inputs | Sparse histories constrain coverage |
| N2 | NOT CURRENTLY FEASIBLE | N0/N1 inputs | Governance-blocked/RESEARCH-ONLY; cannot block N0/N1 |
| A-MAG | FEASIBLE WITH LIMITATIONS | Observed/expected response | Standardization partial; Expected Response inherited |
| A-SIGN | FEASIBLE WITH LIMITATIONS | Ordered signed observed/expected response | Near-zero direction remains G2 issue |
| A-TIME | PARTIALLY FEASIBLE | Ordered market/event timestamps | Fine timestamps licensed/costly |
| A-RES | FEASIBLE WITH LIMITATIONS | Residual observed/expected response | Inherits P0-RES/RR-RESID |
| A-BREAK | FEASIBLE WITH LIMITATIONS | Versioned relationship state | Structural context partial; no future labels |
| A-SUM | UNKNOWN — SOURCE AUDIT REQUIRED | Derived morphologies | G2 formula/dimensions absent; no independent raw need |
| ROLE-TRIG | FEASIBLE WITH LIMITATIONS | Abnormality plus quality metadata | Activation policy deferred; upstream inherited |
| ROLE-DISC | PARTIALLY FEASIBLE | UR/MP/R components | Simple branches feasible; full discrimination not guaranteed |
| ROLE-UPD | FEASIBLE WITH LIMITATIONS | New observation/vintage IDs | Immutable predecessor linkage required |
| ROLE-RIVAL | PARTIALLY FEASIBLE | Market, relationship, event and quality rivals | Event/link archives have PIT gaps |
| UR0 | FEASIBLE WITH LIMITATIONS | Expected signed response plus peer response | Transform easy; N0/N1/RR-SIGNED inherited |
| UR1 | FEASIBLE WITH LIMITATIONS | UR0 plus uncertainty history | Calibration context partial |
| UR2 | PARTIALLY FEASIBLE | UR0/UR1 plus non-duplicative PIT context | News/link context constrained; overlap audit mandatory |
| MP0 | FEASIBLE WITH LIMITATIONS | Expected response plus source move | Inherits normal relationship; no pressure identification |
| MP1 | FEASIBLE WITH LIMITATIONS | MP0 plus accessible volume/turnover/liquidity | Quote/depth enhancement licensed |
| MP2 | PARTIALLY FEASIBLE | Dated pressure/flow source plus contamination lineage | Holdings/predicted trades sparse; endogeneity unresolved |
| MP3 | NOT CURRENTLY FEASIBLE | Historical trades/quotes/order/signed flow | Specialized, licensed, high burden; does not block M2 |
| R0 | FEASIBLE WITH LIMITATIONS | Versioned relationship state | Inherits P0-STAB/N0/N1 |
| R1 | FEASIBLE WITH LIMITATIONS | Dated public events/original documents | NLP hard/optional; timestamp/version audit required |
| R2 | PARTIALLY FEASIBLE | Dated linkage/exposure vintages | Historical network/product links sparse |
| R3 | FEASIBLE — CORE REQUIREMENTS | Lineage/timestamp/missingness metadata | Must be engineered for every source |
| M3-DISC | NOT CURRENTLY FEASIBLE | Frozen PIT record plus separated outcomes | Production blocked; research protocol required |
| U0 | FEASIBLE — CORE REQUIREMENTS | Existing status/quality metadata | Transform easy; metadata completeness inherited |
| U1 | UNKNOWN — SOURCE AUDIT REQUIRED | Future belief outputs | Representation not specified; no independent source audit yet |
| U2 | UNKNOWN — SOURCE AUDIT REQUIRED | Future mechanism-uncertainty outputs | Representation not specified |
| U3 | NOT CURRENTLY FEASIBLE | Future beliefs/cost/risk/policy | Outside current scope/RESEARCH-ONLY |
| U4 | FEASIBLE WITH LIMITATIONS | Uncertainty/missingness/conflict/PIT lineage | Source-specific health detail varies |

## Reconciliation

- Envelope count: **45 / 45**.
- No candidate was ranked or selected.
- `NOT CURRENTLY FEASIBLE` applies to the branch as scoped, not its parent mechanism.
- Missing enhancements never invalidate a feasible minimum branch.
