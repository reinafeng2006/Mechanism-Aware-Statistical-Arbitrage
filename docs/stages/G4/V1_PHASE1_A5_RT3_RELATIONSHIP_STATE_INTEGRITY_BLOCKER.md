# V1 Phase 1 A5 RT3 Relationship-State Integrity Blocker

Date: 2026-09-14

Status: **GENUINE SCIENTIFIC/DATA-LINEAGE BLOCKER / RESEARCHER DECISION REQUIRED**

## Completed recovery state

- All 70 existing R0/R1/R3/R4 inner relationship partitions passed SHA-256 verification without model recomputation.
- The relationship checkpoint was published as `fc5693d`.
- SG-A was frozen and published as `599d7a3`; its inner-only action guard was published as `34697ff`.
- No relationship value was interpreted or compared. No A3, A5, A6, G5, OF4, or held-out output was inspected.

## Exact blocker

The frozen A5/SCI-A contract defines:

`RT3_h = median_(q=t+1...t+h) |y_j,q - mu^t_j|i(x_i,q,f_q)| / S_j,t`

where the relationship equation and parameters/state are frozen at event time `t`, while future `x/f` are outcome-side realized inputs. Representation-only R0-DIST/R0-CORR must use their matched R0-LIN bridge.

The immutable `V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0` partitions contain event identity, support, representation score, current expected responses (`mu_ab`, `mu_ba`), PS0/PS1 scales, and current predictive standard deviations. They do **not** contain the event-time equation/state sufficient to evaluate the frozen mapping at future inputs:

- R0-LIN bridge intercept and slope;
- R1-M/R1-MI factor exposures, pair residual intercept/slope, and applicable factor-state binding;
- R3 stratum/pair posterior intercept and slope state;
- R4 filtered intercept/slope state and associated event-time parameter version.

One current fitted value `mu(t)` cannot identify an intercept/slope function at future `x_q`. Treating `mu(t)` as a constant future expectation, refitting from outcomes, or silently omitting RT3 would alter the frozen target. Re-running R0/R1/R3/R4 to materialize missing state is explicitly outside the current no-recomputation recovery authorization.

## Bounded alternatives

1. `RT3-A — VERSIONED RELATIONSHIP-STATE AUGMENTATION` (recommended): authorize deterministic re-execution of the already-frozen R0/R1/R3/R4 implementations solely to create new immutable state/parameter companion partitions with ancestry to the existing relationship checkpoint. Preserve existing outputs and hashes unchanged; verify that reproduced common fields match before binding the companion. This changes no estimator, universe, Search Budget, or scientific semantics.
2. `RT3-B — VERSIONED V1 TARGET AMENDMENT`: remove/defer RT3 from V1 and retain RT0–RT2 only. This avoids recomputation but changes the frozen SCI-A/A5 target package and requires explicit scientific amendment/contamination lineage.
3. `RT3-C — DEFER DOWNSTREAM V1 EXECUTION`: preserve all frozen contracts and outputs, but stop A3/A5/A6/G5 until a later environment/run can create the exact state companion under explicit authorization.

Recommendation: `RT3-A`. It preserves the frozen target and model semantics while treating the omission as an output-schema/lineage correction. It must be a new versioned companion and may not overwrite `V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0`.

`V1 A5 RT3 RELATIONSHIP-STATE SUFFICIENCY / RESEARCHER DECISION REQUIRED`
