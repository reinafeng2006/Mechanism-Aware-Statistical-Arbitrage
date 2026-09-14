# V1 A6-TG-A Training Geometry Freeze

Decision date: 2026-09-14
Contract ID: `V1-A6-TG-A-1.0`
Status: **APPROVED / FROZEN BEFORE A6 FITTING**

## Temporal training geometry

2015H1 generates eligible training evidence only. The first A6 pseudo-OOS prediction origin is 2015H2. At every later semiannual origin, training expands over prior inner blocks only when the block has ended, the exact target horizon has fully matured, target-horizon censoring authorizes it, and the complete label was available before the prediction origin.

`elapsed historical information may accumulate under the frozen protocol; future or not-yet-mature outcomes may not enter training`.

O1, O5, O10 and O20 maturity is evaluated separately. A target without at least one prior completed block containing mathematically valid matured labels remains unavailable. There is no horizon substitution, partial-label imputation, rolling window, or additional A6 history hyperparameter.

## Fitting unit and weights

Each A6 equation is fit separately by:

`relationship candidate × resolution component × horizon × PV information set`.

It is not fit separately for every pair or direction. Direction-specific records and state columns remain intact.

Within one fitting problem, every eligible unordered pair receives equal total fitting weight. If pair `p` has `n_p` valid training rows across its observations and directions, every such row has deterministic weight proportional to `1/n_p`; weights are normalized by one common positive factor only. Thus each pair contributes equal total weight while directional identity remains explicit. This is weighted least squares using the frozen OLS equation and a deterministic design weight, not a new estimator-search branch.

Pairs with longer history or more valid rows receive no additional total influence solely from row count. No alternative row weighting, pair-specific A6 model, horizon pooling, rolling window, or sample-size cutoff is in V1.

## Boundaries

Only fully observable outcomes may enter a fit. 2013–2014 remains formation/warm-up and cannot become A6 development-label evidence. OF4 2020–2023 is inaccessible. The 2024–2025 final held-out region remains sealed.

No empirical value, survival count, model result, outcome, or PnL informed this decision.

`V1-A6-TG-A-1.0 — APPROVED / FROZEN`
