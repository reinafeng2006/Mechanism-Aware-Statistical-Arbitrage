# G4-04A1c Scale-Quality & Severe-Failure Numerical Thresholds Proposal

Status: **G4-04A1c NUMERICAL THRESHOLDS PROPOSED / AWAITING RESEARCHER REVIEW**
Boundary: bounded pre-empirical cutoff design only. No frozen-data inspection, statistic, loss computation, outcome access, or A2 work.

## Objective

Choose only the numerical cutoffs required to execute the frozen MAD/SD scale and median-vector/AG2 architecture. Values are protocol-design candidates, not empirical estimates. No new metric or aggregation branch is introduced.

## SQ — Relative scale-quality cutoff

For each direction and origin, define candidate-neutral relative scale quality conceptually as:

`Q_scale = directional_MAD / PIT_cross_pair_median_directional_MAD`

The reference uses only candidate-neutral, pre-origin eligible pairs with identical response semantics. Candidate cutoffs:

- **SQ05:** require `Q_scale >= 0.05`;
- **SQ10:** require `Q_scale >= 0.10`.

Below the selected cutoff, scaled loss is unavailable and reason-coded `SCALE QUALITY / NEAR-ZERO SCALE`; no epsilon replacement occurs. The cross-pair reference's minimum support and fallback when undefined must also be frozen.

## MS — Estimator-support cutoff

For MAD and SD within the already-authorized H63/H126/H252/H504 history, propose only:

- **MS80:** at least 80% of the candidate's nominal eligible directional observations plus its frozen minimum synchronized-history contract;
- **MS90:** at least 90% plus the same contract.

This threshold governs scale estimability only and cannot recode `UNKNOWN MISSINGNESS` or other eligibility states.

## SF0 — Absolute adequacy failure cutoff

Using the pair-direction-origin median absolute scaled loss, propose:

- **SF0-2:** severe absolute failure when the value exceeds 2.0 scale units;
- **SF0-3:** severe absolute failure when it exceeds 3.0 scale units.

This is an SR1/AG2 use-quality guardrail, not automatically an SR0 structural failure.

## SF1 — Comparative reversal cutoff

Define the common-support loss difference so positive means the candidate is worse than its preregistered comparator. Propose:

- **SF1-10:** severe reversal at a deterioration of at least 10% of comparator loss;
- **SF1-20:** severe reversal at a deterioration of at least 20%.

The denominator must be candidate-neutral and have a frozen zero/near-zero rule. Absolute loss difference must also be reported so a percentage alone cannot create a failure on a negligible base.

## SF2 — Structural/support cutoff

For common-support retention relative to the smaller named candidate-native support, propose:

- **SF2-50:** structural support failure below 50%;
- **SF2-70:** structural support failure below 70%.

Candidate-native coverage remains separately reported. SF2 does not recode exclusions or make low coverage equivalent to poor predictive performance.

## Temporal severe-failure allowance

For four annual outer folds, propose:

- **TF0:** zero severe AG2 fold failures permitted for `DOMINANT / ADVANCES`;
- **TF1:** at most one severe fold failure may retain `NON-DOMINATED / BOTH SURVIVE`, but cannot yield `DOMINANT / ADVANCES`.

One exceptional positive fold cannot offset a severe failure. Directional consistency and dispersion remain separate evidence; candidate cutoffs for them are deferred until their exact statistics are frozen, rather than inventing incompatible thresholds here.

## Coherent cutoff bundles

To avoid a Cartesian search, propose only:

- **CUT-CONSERVATIVE:** SQ10 + MS90 + SF0-2 + SF1-10 + SF2-70 + TF0;
- **CUT-PERMISSIVE:** SQ05 + MS80 + SF0-3 + SF1-20 + SF2-50 + TF1.

These bundles encode different strictness philosophies and are not performance-selectable. Researcher approval must select one or explicitly revise it before computation; components cannot be mixed opportunistically.

## Remaining decisions

1. select or revise one coherent cutoff bundle;
2. freeze the cross-pair reference support and undefined-reference rule;
3. confirm whether SF1 requires both relative and absolute deterioration conditions;
4. freeze the consequence mapping from each AG2 failure type to SR1 dispositions;
5. later freeze exact direction-consistency and dispersion statistics/cutoffs before execution.

All values remain **PROPOSED / UNAUTHORIZED**. No data access or computation is authorized.

`G4-04A1c NUMERICAL THRESHOLDS PROPOSED / AWAITING RESEARCHER REVIEW`
