# Research + Trading V1 Pre-Computation Protocol Freeze

Decision date: 2026-09-14
Status: **APPROVED / FROZEN — PHASE 1 + INNER DEVELOPMENT AUTHORIZED**

## C04-A conservative contract

Acquire and preserve the bounded official SSE/SZSE/company-disclosure corporate-action calendar required for V1. Freeze:

`identified corporate action -> affected interval excluded under the V1 rule`.

The calendar creates two distinct states:

- `IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED`;
- `NO IDENTIFIED ACTION UNDER V1 CALENDAR`.

It must never promote the second state to `AUTHORITATIVELY ACTION-CLEAN`. Absence from the bounded calendar is not proof of clean history. The core-sidecar state remains `CORPORATE_ACTION STATUS UNRESOLVED`; the descendant V1 layer adds evidence and eligibility without rewriting it.

The action-to-exclusion mapping is frozen before response or PnL inspection:

- exclude the close-to-close response whose interval `(previous eligible session, current session]` contains a declared ex-right/ex-dividend date, effective share-capital change date, or other official action-effective date;
- exclude a trading episode if any signal, execution, holding, or exit price interval contains such a date and no separately qualified entitlement/cash treatment exists;
- retain publication date for PIT provenance; it does not replace the economic effective/ex date;
- actions lacking a defensible effective/ex date remain unresolved and cannot generate a fabricated clean interval;
- adjusted-price products, Tushare/Sina factors, forward fills, and synthetic entitlements cannot repair the state.

Every record preserves security identity, action type, announcement/publication time, effective/ex date, source artifact, retrieval time, schema version, and checksum. Raw official artifacts are immutable; corrections create a descendant version.

## MODEL-A

Freeze the seven-tuple V1 Search Budget:

1. `V1-R0D-252M` — R0-DIST + matched R0-LIN bridge, H252/U1M;
2. `V1-R0C-126W` — Pearson R0-CORR + matched R0-LIN bridge, H126/U1W;
3. `V1-R0L-126W` — OLS R0-LIN, H126/U1W;
4. `V1-R1M-126W` — R1-M two-stage OLS, H126/U1W;
5. `V1-R1MI-126W` — matched R1-MI two-stage OLS, H126/U1W;
6. `V1-R3-252M` — P0 Gaussian EB random intercept/slope, REML, N-ZERO, H252/U1M;
7. `V1-R4-63D` — static-intercept/random-walk-slope Kalman model, PIT-ML Q/R, matched-static initialization, H63/U1D.

Spearman and Huber remain diagnostics only. R2 is `V1 NOT DATA-READY / V2`; R2-N, R4-MR, directed linkage and MP3 are deferred. R5-EG-ECM remains blocked/no V1 execution; VECM is deferred. P1 fundamentals acquisition is prohibited for V1.

### R3-A frozen estimator contract

- REML estimates a taxonomy-versioned C06 group-level unstructured random-intercept/random-slope covariance and group observation variance from prior eligible formation information;
- N0 fixes pair-deviation covariance to zero; N1 estimates Gaussian pair deviations under identical target, equation, factors, PIT information, H/U and eligibility;
- singular/nonfinite/boundary fits are explicit estimator-quality states and never silently repaired;
- re-estimation occurs only at U1M refresh using information available before the evaluated response;
- output separates fixed-effect, conditional random-effect, plug-in hyperparameter, observation and predictive uncertainty; omitted hyperparameter uncertainty is labelled.

### R4-A frozen estimator contract

- PIT Gaussian maximum likelihood estimates Q/R from the prior eligible H63 formation set; no variance grid or outcome-dependent alternative remains;
- matched R0-LIN OLS supplies the static intercept, prior slope mean and finite prior slope variance;
- U1D predicts before the response, computes A3 afterward, and may then update for the next decision;
- state variance evolves in eligible trading-session time; missing/ineligible observations predict without measurement update;
- nonfinite/zero/boundary Q/R or failed initialization is an explicit unavailable/quality state; future smoothing is prohibited.

## SCI-A

Freeze the documented minimal A6 protocol, inheriting A1–A5, O1/O5/O10/O20, CS2, SR0→SR1, TP2/CG2/OF4, dependency-ordered multiplicity and non-forced-winner states.

- UR0 is primary M1 morphology; UR1 is calibration-dependent supporting evidence; UR2 is outside V1.
- MP0 plus separately preserved MP1 amount/volume context is V1 M2 architecture; MP2/MP3 are outside V1.
- M0 remains positive-only; U remains a five-dimensional non-probability epistemic state.
- RT0/RT1 use endpoint cumulative response; RT2 and original-state RT3 remain continuous.
- A6 uses OLS only. O5/O10 are small M1/M2 confirmatory horizon families; O1/O20 are diagnostics. Holm FWER applies within each two-horizon family. PV-BOTH is diagnostic.
- no target, metric, threshold or model is added because R2 is unavailable.

## TRADE-A and exact exit implementation

Freeze no additional trading-only entry threshold, deterministic upstream evidence-to-direction mapping, equal-notional sizing, gross cap 1.0, no borrowing, 10% per-security cap, security-level conflict netting, explicit overlap/exposure/missingness/suspension handling, and zero-return cash.

The existing G5 contract defines an executable threshold-free originating-state zero-crossing condition. V1 therefore uses `EXIT-RESOLVE-10`: exit at the first later eligible decision when the signed originating peer gap for TV1-M1 or source excess for TV1-M2 reaches/crosses zero relative to its frozen event-time anchor, or after 10 eligible sessions, whichever occurs first.

This is not an optimized convergence threshold. If an immediately next-session entry is untradeable, no entry occurs. Suspension/untradeability at exit delays execution to the first qualified observed session and is reported; `UNKNOWN MISSINGNESS` makes the episode economically unevaluable.

Transaction cost is 10 bps one-way on absolute executed security notional; 5 and 20 bps one-way are mandatory non-selection sensitivities. Trading performance is downstream evidence and cannot rescue or redefine an upstream candidate.

## Authorized Phase 1 boundary

After this freeze is committed and pushed, the agent may acquire/construct only C04-A official action-calendar artifacts and a versioned descendant exclusion layer; implement the seven relationship tuples, masks, folds, A1–A6 and G5; execute/inspect only 2015–2019 semiannual inner-development evidence; materialize immutable/checksummed artifacts; and stop at `PRE-OUTER V1 GATE / RESEARCHER DECISION REQUIRED`.

OF4 2020–2023 and sealed 2024–2025 remain inaccessible. No P1 acquisition, R2/R5 execution, family/Search-Budget expansion, or scientific-semantic repair is authorized.
