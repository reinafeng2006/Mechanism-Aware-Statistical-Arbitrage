# G4-03A Sample & Estimation Geometry Freeze

Status: **G4-03A APPROVED / FROZEN — 2026-09-10**  
Boundary: pre-empirical protocol design. No frozen-data inspection or statistical computation.

## Governing search-budget rule

`parameter search space is part of the statistical protocol`.

Every authorized candidate menu must remain finite, small, justified, preregistered, and versioned. Performance-contingent additions require explicit reopening and a contamination record. The geometry and candidate menus below are frozen as protocol scope; no candidate value is selected as an empirical winner.

Candidate geometry must be registered by representation rather than inferred as an unrestricted Cartesian product. Symbolically, for representation family `r`:

`G_r = AuthorizedTuples(H_r, U_r, O_r, T_r, S_r, M_r)`

`SearchBudget = sum_r |G_r|`

Here `H` is estimation history, `U` is normal-relationship refresh cadence, `O` is outcome horizon, `T` is the registered eligibility/tolerance rule, `S` is the support-comparison treatment, and `M` is the already-authorized measurement/representation variant. `AuthorizedTuples` must be an explicit finite list or constrained design; it is not the full Cartesian product of every menu. Market/abnormality evaluation cadence is a separate object and does not multiply `U` unless later explicitly authorized. This is symbolic protocol bookkeeping only and is not run here.

## 1. Minimum-history representation

Represent minimum history through a candidate-specific **support contract**, not a universal row count:

- nominal formation horizon;
- minimum number of candidate-eligible observations;
- minimum synchronized observations for a pair;
- permitted incomplete-history reason/state;
- required coverage across the nominal horizon rather than observations concentrated in one subperiod;
- C04/C05/C06/identifier/source-rule versions;
- whether the requirement is absolute, proportional to the nominal horizon, or both.

Minimum estimation support may be representation-specific. Correlation, distance, residual, stochastic, and cointegration representations need not share one universal minimum-history rule. Each representation-specific rule must be fixed before that representation is evaluated and counted explicitly in the Search Budget.

| Element | Provenance class | Proposed status |
|---|---|---|
| Representation as nominal span + eligible count + synchronized count + coverage pattern | **THEORY/EVIDENCE-DERIVED** from relationship estimation and G4-01 semantics | Fix ex ante before mask computation |
| Exact minimum eligible count/share and coverage pattern | **DESIGN CHOICE** | Candidate-specific; decide later without outcome inspection |
| Selecting among a small preregistered set if more than one defensible value remains | **DEVELOPMENT-SELECTABLE** | Pseudo-OOS only; held-out prohibited |

## 2. Missingness-tolerance representation

Represent window missingness as a vector rather than silently compressing it into one flag:

`{total missingness burden, consecutive-missingness/run structure, boundary missingness, pair-synchronization loss, known suspension-related absence, UNKNOWN MISSINGNESS}`

`UNKNOWN MISSINGNESS` remains neither suspension, normal trading, zero return, nor global ineligibility. Candidate rules must specify which components are hard exclusions, uncertainty inputs, or reported burdens.

| Element | Provenance class | Proposed status |
|---|---|---|
| Vector representation and separation of observation/window/pair consequences | **THEORY/EVIDENCE-DERIVED** from frozen G4-01 | Fix ex ante |
| Component tolerances or hard-exclusion values | **DESIGN CHOICE** | Unresolved; candidate-specific |
| Sensitivity across a small registered tolerance set | **DEVELOPMENT-SELECTABLE** | Only if registered before outcomes |

## 3. Formation / estimation horizon candidates

Propose a deliberately small daily-data family:

- **H63:** approximately one trading quarter;
- **H126:** approximately one trading half-year;
- **H252:** approximately one trading year.

Preserve one controlled extension:

- **H504 — LONG-HISTORY EXTENSION:** approximately two trading years, available only to representation families whose preregistered estimation-support contract supplies a structural or theoretical reason for longer history, such as an authorized cointegration, stochastic, or slow-state candidate.

These are trading-session counts, not calendar-day promises. They span responsiveness versus stability without creating a dense tuning grid. H252 also preserves ancestry to the reviewed distance-pairs tradition's longer formation concept, without selecting that method or claiming general superiority.

| Family | Provenance class | Proposed status |
|---|---|---|
| H63/H126/H252 session menu | **MARKET-CALENDAR-DERIVED + THEORY/EVIDENCE-DERIVED + DESIGN CHOICE** | Finite candidate family; not selected |
| H504 long-history extension | **THEORY/EVIDENCE-DERIVED + DESIGN CHOICE** | Representation-restricted; not universal and not selected |
| One horizon used by a particular relationship candidate | **DEVELOPMENT-SELECTABLE** | Select only within frozen pseudo-OOS protocol |

H504 is not a universal hyperparameter and cannot be introduced after outcome inspection merely because a candidate performs poorly. `representation-specific support requirement != performance-driven parameter expansion`. No shorter/intraday or other longer horizon is added. A later addition requires reopening, justification, and contamination accounting.

## 4. Candidate update cadences

Freeze the semantic distinction `market/abnormality evaluation cadence != normal-relationship re-estimation cadence`. Keep relationship-state re-estimation distinct from both market/abnormality evaluation and event-time mechanism updating. For the daily historical research layer, propose:

- **U1D:** every eligible trading session;
- **U1W:** every five eligible trading sessions;
- **U1M:** every 21 eligible trading sessions.

These are operational session-count conventions, not claims that weeks/months always contain those counts. U1D is the highest-adaptation candidate, not an implicit default. Daily observation or daily signal evaluation does not imply daily relationship refitting. Genuinely new fast information may later update mechanism/resolution beliefs without forcing full normal-relationship re-estimation. Under the frozen anti-circularity principle, frequent refresh must not automatically absorb the current abnormal observation into normality.

| Family | Provenance class | Proposed status |
|---|---|---|
| U1D/U1W/U1M relationship-state refresh menu | **MARKET-CALENDAR-DERIVED + DESIGN CHOICE** | Finite candidates; not selected |
| Candidate-specific cadence choice | **DEVELOPMENT-SELECTABLE** | Pseudo-OOS only |
| Distinction between relationship refresh and new-evidence sequential update | **THEORY/EVIDENCE-DERIVED** | Fix ex ante |

## 5. Candidate outcome-horizon family

Propose a small multi-timescale daily validation family:

- **O1:** one eligible trading session after decision origin;
- **O5:** five eligible trading sessions;
- **O10:** ten eligible trading sessions;
- **O20:** twenty eligible trading sessions.

The menu covers immediate through approximately monthly daily resolution without interpreting any horizon as optimal. It does not define catch-up, reversal, persistence, relationship break, magnitude, or a label.

`outcome horizon != trading holding period`. O1/O5/O10/O20 define later resolution/validation geometry only and authorize no exit, holding-period, or trade-policy rule.

| Family | Provenance class | Proposed status |
|---|---|---|
| O1/O5/O10/O20 menu | **MARKET-CALENDAR-DERIVED + THEORY/EVIDENCE-DERIVED + DESIGN CHOICE** | Finite outcome-horizon candidates; not selected |
| Mechanism/target-specific admissible subset | **CANDIDATE-SPECIFIC** | Must be fixed before target construction |
| Selection among admissible horizons | **DEVELOPMENT-SELECTABLE** only if the later target/multiplicity protocol permits | Held-out prohibited |

All outcome observations remain quarantined and cannot enter the originating event-time information set.

## 6. When purge / embargo is structurally required

Freeze later, after approval, the principle that a temporal exclusion is required whenever an evaluated record could transmit information across a partition or selection boundary through:

- an outcome horizon crossing the boundary;
- an estimation/formation window using observations from the wrong side of the boundary;
- overlapping labels/targets sharing future realizations across folds;
- sequential updates whose available information crosses the evaluation origin;
- parameter/relationship estimates trained on records whose targets overlap the validation region;
- duplicated or linked security/pair episodes that make nominally separated records informationally dependent.

The proposed structural rule is:

- **purge** any record whose input/target lineage violates the intended partition role;
- consider an **embargo** after a boundary when serial dependence or overlapping information availability could contaminate the next role.

Purge/embargo is structurally triggered, not universally imposed. Overlapping outcome horizons, overlapping estimation windows, and a later nested or walk-forward architecture may create the dependence that activates it. Exact purge/embargo length is **DESIGN CHOICE** and remains unresolved until Block B selects the temporal architecture; it must then reflect the selected maximum relevant input/target overlap and be frozen before computation. No numerical length is selected here.

## 7. Ex-ante fixed versus development-selectable

### Fix ex ante before any computation

- dataset/sidecar/partition/rule versions;
- structural state meanings and no-imputation rules;
- finite candidate menus and Search Budget;
- permitted candidates per construct;
- target semantic definitions and event-time/outcome separation;
- hard eligibility exclusions and lineage requirements;
- temporal architecture, outer partition boundaries, purge/embargo formula, metrics, multiplicity, and stopping rules;
- held-out seal and access policy.

### Potentially development-selectable within frozen pseudo-OOS

- one option from the approved formation-horizon menu;
- one option from the approved relationship-refresh menu;
- candidate-specific admissible outcome horizon(s), subject to later target/multiplicity rules;
- one of a small preregistered set of missingness/support tolerances;
- competing representation/UR/MP variants already permitted by the frozen candidate inventory.

Development selection must use only authorized development pseudo-OOS evidence and cannot add options. Nothing may be selected using final held-out evidence.

## Dependencies handed to future blocks

**Block B** must compare TP0–TP3, explicitly including walk-forward/nested pseudo-OOS candidates, against dynamic relationship stability, finite-history use, leakage control, and OOS robustness. No architecture is selected here.

**Block C** must report candidate-native support separately from common-support evaluation and decide how CS0–CS2 are used. No support architecture is selected here.

## Frozen disposition

- H63/H126/H252 are the common estimation-history menu; H504 is a representation-restricted extension only.
- Minimum-history support contracts are representation-specific and fixed before evaluation.
- Market/abnormality evaluation cadence is separate from relationship refresh; U1D/U1W/U1M are refresh candidates and U1D is highest-adaptation, not default.
- O1/O5/O10/O20 are outcome-validation horizons, not trading holding periods.
- Missingness remains multidimensional; purge/embargo remains structurally triggered.
- The Search Budget counts explicit representation-aware authorized tuples and prohibits silent Cartesian-product expansion.
- Numerical tolerances, exact purge/embargo lengths, and representation-specific support thresholds remain unresolved as documented.

`G4-03A APPROVED / FROZEN`
