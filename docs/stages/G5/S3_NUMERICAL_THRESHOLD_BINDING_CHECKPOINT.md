# S3 numerical threshold binding checkpoint

2026-09-22 — DESIGN ONLY / RESEARCHER DECISION REQUIRED.

The [approved scale architecture](../../decisions/S3_SCALE_ARCHITECTURE_APPROVAL.md) binds current-origin aligned residual MAD, common H126, daily prior-information refresh, two-sided peer convergence and the common weighted reference-tail architecture. H252 MAD and H126 SD are non-selecting robustness specifications. This gate does not reopen those bindings.

## Exact question

How should the reference-tail probability / numerical z0 be bound without performance-driven optimization?

No probability, quantile or numerical z0 is selected or computed. In particular, the earlier 5% proposal has not been approved. Current-origin fit-overlap optimism remains; neither route yields a predictive-error probability, significance test or economic-profitability guarantee.

## Two bounded alternatives only

| Item | A — directly preregistered probability | B — bounded occurrence/support development |
|---|---|---|
| Design choice | Researcher fixes alpha_ref before seeing historical occurrence/support values, with a written signal-rarity/materiality rationale. | Researcher first freezes a finite, non-performance selection rule; later authorized 2015–2019 development uses only occurrence/support characteristics to bind alpha_ref and its numerical threshold. |
| Meaning | A declared upper-tail rarity convention under the approved weighted reference population. Materiality is relative to dispersion, not expected monetary gain. | A development-selected rarity/support convention; must be labeled adaptive to development occurrence information, even without PnL. |
| Numerical z0 | Still requires a separately approved reference population/period and authorized estimation of its weighted quantile; fixing alpha does not provide z0 now. | Obtained only through the frozen occurrence/support procedure on approved development data; no per-model or per-sign threshold optimization. |
| Information permitted in a future bounded action | Prior standardized residual reference values sufficient for the prescribed quantile; support/occurrence reporting cannot retrospectively change alpha. | Only prespecified occurrence frequencies, qualified-history availability, concentration by time/pair/group/sign and occurrence stability; no forward resolution labels, returns, PnL or economics. |
| Benefit | Least adaptation; the rarity target is transparent and independent of observed historical support. | Can account for sparse common support, concentration and unstable occurrence before final binding. |
| Limitation | The chosen rarity level may have sparse or concentrated support; no algebra supplies an optimal probability or an adequate effective sample size. | More selection freedom; tuning until events look plentiful or stable can overfit occurrence itself. No guarantee of predictive or economic quality. |
| Required pre-access commitments | Probability and rationale, reference dates and chronological construction, quantile convention, fixed approved weights, reporting and stopping rules. | Finite probability candidates or another finite bounded rule, explicit occurrence/support criteria, temporal separation, deterministic choice/tie rule, inspection budget and failure/stop rule. None is supplied or approved here. |
| Failure behavior | Report unavailable/unstable support; do not relax alpha or replace the primary scale automatically. | If no candidate meets preregistered criteria, stop with no selected threshold; no grid expansion, later-year lookup or fallback to outcomes. |

These are alternative ways to bind the rarity target, not “no calibration” versus “calibration”: even A generally needs later reference-quantile estimation. A justified theoretical law could change that need, but no such law is adopted here; MAD's 1.4826 does not justify a Normal quantile.

## Common safeguards

- Use the approved common-support, block/pair/direction/estimator-group weighting. R0-C/R0-L share their group; do not silently reweight missing required groups.
- Keep the evaluated observation out of its own scale and use only legitimately available prior coefficients/inputs. Daily scale refresh does not authorize threshold retuning.
- The inclusion rule remains |z|>=z0. Quantile atoms/ties can make actual inclusion exceed the intended tail budget; disclose that rather than changing the inequality or randomizing ties.
- Signed counts are reported separately without imposing equal signed-tail probabilities or separate thresholds.
- Support is not raw row count alone: pair/time dependence and concentration limit effective information. Any precision requirement must be declared before access; none is invented here.
- H252 MAD/H126 SD remain non-selecting diagnostics. No outcome-based replacement of H126 MAD and no optimization across robustness specifications.
- Under B, only 2015–2019 is proposed for bounded development. The old 2015–2016 run-in and six half-year assessment blocks remain unapproved proposals, not an active action. No 2020–2025 access, no claim that any previously exposed period is pristine, and no claim that 2026 is untouched.
- Freeze the final reference procedure and numerical binding before any subsequent validation. No repeated revision after inspecting inconvenient occurrence or support.
- The finite-grid z0 fallback {1,2,3} and all forward-resolution/PnL objectives remain inactive; B is not that fallback.

## Recommendation for researcher consideration — not a selection

Prefer A when signal rarity/materiality can be justified before inspecting the reference sample: it uses the least adaptation and leaves later quantile estimation as a prescribed operation. If the researcher needs occurrence/support evidence to choose a defensible rarity target, B is the bounded alternative, but its complete finite decision rule and stop conditions must be frozen before access. No numerical probability is recommended or selected by this checkpoint.

The present task stops at comparing A and B. No historical observations, scales, reference distribution, quantile, thresholds, forward labels or PnL were accessed or computed. Do not proceed to expected-capture/cost design, hedge execution or implementation.

**S3 NUMERICAL THRESHOLD BINDING / RESEARCHER DECISION REQUIRED**
