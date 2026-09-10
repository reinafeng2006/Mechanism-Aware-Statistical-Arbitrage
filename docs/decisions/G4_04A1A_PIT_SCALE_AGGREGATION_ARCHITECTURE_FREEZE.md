# G4-04A1a PIT Scale & Aggregation Architecture Freeze

Decision date: 2026-09-10
Status: **APPROVED / FROZEN**

## Scale architecture

- PS0 is the primary robust historical directional-response scale;
- PS1 is the preregistered quadratic-scale robustness check;
- PS2 is optional/non-primary and cannot become a hidden second relationship model;
- `SCALE QUALITY / NEAR-ZERO SCALE` is an explicit state;
- `i -> j` and `j -> i` scales remain separate where response semantics differ;
- unrelated source-stock volatility cannot substitute for the response-aligned scale.

## Aggregation architecture

- AG1 is the primary robust hierarchy: observations, direction, pair, temporal origin/fold;
- AG2 is a non-compensatory directional/pair severe-failure guardrail, not a winner score;
- AG0 is a simple sensitivity/reference only;
- equal-pair influence is preferred at representation-comparison level unless a preregistered structural justification authorizes otherwise;
- OF4 preserves magnitude, directional consistency, dispersion, severe failure, and support without scalar collapse.

Exact estimators, support history, scale-quality cutoff, zero-scale treatment, directional statistic, pair-weight implementation, temporal summaries, and AG2 failure rules remain unresolved. No computation is authorized.
