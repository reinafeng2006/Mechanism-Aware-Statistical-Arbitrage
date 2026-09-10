# G4-03B3 Nested Fold Count, Origin Structure & Boundary Geometry Freeze

Status: **G4-03B3 APPROVED / FROZEN — 2026-09-10**
Boundary: calendar/protocol design only. No frozen-data statistics, availability counts, returns, pairs, measurements, targets, or outcomes may be inspected.

## Objective

Choose a finite nested-fold geometry inside the frozen 2015-01-01 through 2023-12-31 development region while keeping 2013-01-07 through 2014-12-31 as warm-up only and 2024-01-01 through 2025-12-31 sealed.

## Non-negotiable constraints

- outer origins and decision periods are shared within each comparison layer;
- H63/H126/H252 and representation-restricted H504 are the only history menu;
- O20 is the maximum registered outcome horizon;
- inner development, outer pseudo-OOS, and final held-out remain distinct;
- fold boundaries are calendar/protocol determined, never moved for support counts or results;
- outer aggregation/selection rules are frozen before outer inspection;
- boundary targets are censored or excluded under a preregistered purge/embargo rule;
- unequal candidate eligibility is exposed rather than repaired through origin changes.

## Bounded outer-fold candidates

### OF3 — Lower-fold-count sensitivity

Three chronologically ordered pseudo-OOS blocks. Fewer folds reduce repeated evaluation and multiplicity but provide coarser evidence about temporal stability. OF3 is a preregistered sensitivity architecture, not an alternative tuning environment.

### OF4 — Primary outer-fold architecture

Select four annual outer pseudo-OOS blocks: **2020, 2021, 2022, and 2023**. This leaves 2015–2019 for initial development and inner-selection support, preserves the 2013–2014 warm-up reserve, and leaves 2024–2025 sealed. The selection is justified by calendar geometry, H504 support, four distinct outer evidence periods, and five prior development years—not by observed outcomes.

### OF6 — Higher-fold-count sensitivity

Six ordered blocks increase stability observations and approximate more frequent deployment cycles, but create stronger overlap, multiplicity, and dependence-control burdens. OF6 is a preregistered sensitivity architecture, not an alternative tuning environment.

No other fold count is registered. **OF4 is primary**; OF3 and OF6 are registered sensitivity architectures whose execution is not authorized merely by registration. They cannot become alternative tuning environments.

## Frozen OF4 annual-fold calendar

| Period | Role |
|---|---|
| 2013-01-07–2014-12-31 | Warm-up / formation reserve only |
| 2015-01-01–2019-12-31 | Initial development and inner-selection support |
| 2020-01-01–2020-12-31 | Outer pseudo-OOS fold 1 |
| 2021-01-01–2021-12-31 | Outer pseudo-OOS fold 2 |
| 2022-01-01–2022-12-31 | Outer pseudo-OOS fold 3 |
| 2023-01-01–2023-12-31 | Outer pseudo-OOS fold 4 |
| 2024-01-01–2025-12-31 | Final sealed held-out; no access authorized |

## Frozen inner-origin design

Select **SEMIANNUAL CALENDAR-BOUNDARY ANCHORED INNER ORIGINS**. Inner validation origins are determined from calendar structure and remain independent of U1D/U1W/U1M relationship refresh.

`validation-origin cadence != relationship-refresh cadence`.

Annual sparse origins remain a registered lower-frequency sensitivity only. Registration does not authorize execution of both structures.

- **Annual sparse origins:** one prespecified calendar-boundary origin per eligible inner year; lowest inspection and dependence burden, but fewer inner validation observations.
- **Semiannual sparse origins:** two prespecified calendar-boundary origins per eligible inner year; broader seasonal/temporal coverage, but more dependence, multiplicity, and purge/censoring burden.

| Criterion | Annual sparse | Semiannual sparse |
|---|---|---|
| Selection-evidence breadth | Lower | Higher |
| Dependence/multiplicity burden | Lower | Higher |
| H504 warm-up compatibility | Compatible after the authorized support becomes available | Compatible, but early half-year origins may require more explicit support handling |
| Live deployment realism | Coarse periodic protocol review | Moderately frequent protocol review |
| Search Budget burden | Smaller | Larger but bounded |
| Relationship-refresh independence | Preserved | Preserved |

Inner origins provide selection evidence only. They may not move because of pair counts, missingness realizations, regime labels, model performance, or candidate availability. They do not move outer boundaries or consume the final held-out region.

Semiannual origins specify when inner pseudo-OOS evidence may be generated. They do not specify aggregation or winner selection; those rules remain unresolved for G4-03C.

## Outer sequential information flow

At outer fold `k`, the preregistered selection procedure may use only information authorized before that fold's evaluation origin. Calendar advancement may add newly elapsed PIT history under the frozen rule; researchers may not manually revise the procedure after prior outer results.

`automatic temporal updating under a frozen rule != manual retuning`.

```text
Fold 1: warm-up 2013–2014 -> inner information 2015–2019 -> evaluate 2020
Fold 2: authorized elapsed history through 2020 -> frozen inner procedure -> evaluate 2021
Fold 3: authorized elapsed history through 2021 -> frozen inner procedure -> evaluate 2022
Fold 4: authorized elapsed history through 2022 -> frozen inner procedure -> evaluate 2023
Final:  all TP2 activity ends -> 2024–2025 remains sealed
```

Prior outer results may enter only the preregistered aggregation/selection rule. They cannot trigger manual changes to candidate definitions, grids, eligibility, targets, or criteria while later folds retain uncontaminated status.

## Target-horizon boundary and censoring semantics

For each outer fold, bind:

Select **TARGET-HORIZON-AWARE OUTCOME CENSORING** as the primary boundary rule. For decision origin `t` and authorized horizon `O_h`, an outcome evaluation is eligible only when its complete required future interval remains inside the same authorized temporal role.

`eligible warm-up/history cutoff -> inner origins -> inner selection cutoff -> conditional purge/embargo -> outer start -> eligible O_h interval -> outer end/censoring -> next fold`

No outer-fold outcome may cross into the 2024–2025 held-out region. Censoring does not change the raw observation or decision-time eligibility; it governs only whether the outcome is usable for that temporal evaluation role. O20 does not by itself impose a universal embargo. Purge or embargo is **CONDITIONAL / STRUCTURALLY TRIGGERED** and applies only when training/selection label construction and an evaluation interval would otherwise overlap or transmit future information.

The exact purge geometry remains unresolved until target construction is frozen. The protocol must also decide whether CG2 histories roll or expand for each preregistered representation tuple; this may vary only under an authorized support contract and cannot be outcome-driven.

## Proposed comparison criteria

Compare OF3/OF4/OF6 and annual/semiannual sparse origins using protocol geometry only:

- sufficient chronological separation for TP2 roles;
- compatibility with maximum H504 and O20 geometry;
- number of outer evidence consumptions;
- dependence and multiplicity burden;
- live-deployment realism;
- representation-aware Search Budget size;
- transparent native/common-support reporting;
- feasibility of a meaningful final inner selection cutoff before each outer block.

## Preserved unresolved decisions

1. inner and outer aggregation and selection/confirmation rules;
2. rolling/expanding behavior for each authorized CG2 representation geometry;
3. numerical purge/embargo lengths derived from later frozen target/label overlap rules;
4. detailed O1/O5/O10/O20 censoring implementation;
5. native-support/common-support comparison and reporting;
6. authorization and budget for any OF3/OF6 or annual-inner sensitivity execution;
7. versions, hashes, access logs, Search Budget tuples, and contamination consequences.

No development or sensitivity execution is authorized here. OF3/OF6 and annual-inner alternatives remain registered structures, not automatically authorized analyses. Any later execution must fit the frozen comparison/sensitivity budget. No alternatives may be silently multiplied into a Cartesian model-search space.

`G4-03B3 APPROVED / FROZEN`
