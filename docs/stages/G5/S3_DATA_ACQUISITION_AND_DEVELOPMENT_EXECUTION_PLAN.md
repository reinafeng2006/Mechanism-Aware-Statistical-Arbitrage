# S3 data acquisition + development execution plan

2026-09-30 · **ONE BOUNDED PLAN — NOT AUTHORIZED**
Plan ID: S3-ACQUIRE-DEVELOP-FROZEN-1.
Sole governing specification: [frozen S3 protocol](S3_FROZEN_STRATEGY_AND_PRE_DEVELOPMENT_PROTOCOL.md).
Authority: [final design freeze](../../decisions/S3_FINAL_PROTOCOL_FREEZE.md).
Current execution contract: [NEXT_ACTION](../../../research/NEXT_ACTION.json), action NONE.

This is the only proposed acquisition/development plan derived from the frozen strategy. Approving the strategy has not activated any part of it. It contains sequential mechanical checkpoints, not new scientific selection gates. A later action must explicitly authorize its dataset/provider/account identifiers, allowed paths, evidence/result visibility, implementation scope and publication rights. Nothing below authorizes purchases, licensing, credentials, live trading or prospective validation.

## 1. Hard envelope

Historical acquisition/reconstruction/computation is limited to **2015-01-01 through 2019-12-31** and the existing six-model/pair/factor universe plus qualifying fund-share candidates needed by the frozen registry. Preserve PIT vintages and immutable lineage. No 2013/2014 warm-up extension, no 2020 settlement completion, no 2020–2025 validation/reuse and no external D: bulk discovery. 2015 is warm-up, 2016 initial formation/reference, six 2017–2019 half-years are the sole forward development budget, followed by one 2019-end fit.

An inventory or qualification result may show required historical account/borrow/quote/entitlement evidence does not exist. Report that result before unsupported scientific computation; do not approximate with daily bars or substitute a new strategy. Missing data do not permit new sources/periods outside the bounded manifest.

Metadata such as licensing and present contractual documentation can describe admissible access, but cannot be backdated as historical evidence. Provider/account selection is procurement/evidence qualification under this plan, not strategy optimization; no specific provider has been selected here.

## 2. Exact required evidence and fields

| Dataset/evidence family | Required fields and source requirements | Scope and purpose |
|---|---|---|
| Immutable baseline/relationship inputs | Freeze/version/hash; pair and security IDs; PIT membership/industry; trading calendars; response/price/factor definitions, units, native H/U, coefficient lineage and available timestamps | Existing approved six estimators, historical permitted region only. Frozen baseline read/validation only after authority; new descendants never overwrite V1. |
| Official fund-share universe/registry | Immutable exchange/instrument/share-class ID; first tradable date; mandate/benchmark/taxonomy and effective versions; holdings/disclosure issue and receipt dates; dead/delisted/merged predecessor lineage; currency, tick, lot, order/settlement access, official calendar | Full PIT eligible universe for required market/industry slots, not current survivors. Issuer/exchange/index-definition evidence with qualified publication lineage; rank only by frozen rule. |
| Stock and fund cash-flow/price histories | Raw executable currency prices; signal closes; receipt/effective timestamps; units/share multipliers; distributions/splits/rights/mergers, long/short entitlement terms, taxes and receivable settlement; quality/unknown intervals | All potential actual legs and annual prior histories within 2015–2019. No future-adjusted clean price shortcut. Official action terms and qualified price-vintage evidence required. |
| Research factor reconstruction | Original market/industry definitions, constituent/weight/return/cash-flow lineage, publication and availability, transformation between modeled response and instrument coordinate | Needed for model residual, OLS, xi and cash-flow-consistent factor holding accumulation. A factor time series alone may not identify C_f; absent reconstruction => tracking unavailable. |
| Intraday quotes/trades/calendar states | Per-leg bid/ask prices/quantities, depth relevant to actual order size, event sequence and event/receipt timestamps, trade corrections, halt/limit/open/close/calendar records and availability | First synchronized post-open reference, crossing IOC and liquidation; sufficiently complete event history to certify timing and executable size. Official/qualified venue feed lineage, not daily OHLC fill inference. |
| Account-specific borrow | Account/lender/broker and instrument IDs; binding locate ID, timestamp, validity, reserved and available quantity; rate/reset/day-count/minima; recalls/notice/deadline, buy-ins, manufactured entitlements and short restrictions | Every actual short after duplicate aggregation. Signed/historically effective lender/broker records; indicative inventory/modern lists cannot prove historical borrow. |
| Funding/collateral/fees/capital | Declared funded book and portfolio NAV/capital allocation; actual balances/encumbrances; eligible collateral/haircuts/margin, restricted proceeds, committed credit, rates/tiers/day-count, commissions/taxes/minima and account applicability | Historical terms effective and available at each decision. No invented CNY1m/equal sleeve capital or generic cost rates. Account input must be declared before economic replay. |
| Order/fill/cancel/settlement | Parent/child/attempt IDs, side, exact requested/filled quantity, limit and benchmark, timestamps/sequence, acknowledgements/rejections/cancels/late fills, fees, loan return and settled/remaining cash/claims | Observed records or separately authorized qualified reconstruction of this precise IOC/unwind policy. Retain rejected/no-fill/partial attempts and eventual obligations. |
| Timing contracts | Feed clock/receipt/latency guarantees; broker/venue dispatch/ack/cancel validity/deadlines and lawful retry/settlement terms | Derive quote-age/skew/IOC timing. Missing bounded evidence => unavailable, not 1s/5s assumed defaults. |

Every row carries provider/document identifiers, account applicability, license/access scope, raw checksum, version/vintage, economic and receipt time, units/denominator, parent lineage and reason-coded unknown states. Store only required fields/time partitions. Do not acquire optional NAV/look-through/H-B datasets to rescue mandatory qualification; optional benchmark acquisition is excluded from this bounded primary plan.

## 3. Source and manifest qualification checkpoint

Before empirical processing, an authorized operator must bind an immutable manifest to this protocol revision: source/provider IDs, account applicability, exact datasets/versions/fields/date partitions, permitted storage paths, access modes, result visibility and integrity hashes. Official rule/issuer records and contract-bound broker/lender evidence take precedence for obligations; a vendor is admissible only with matching provenance/vintage rights.

Confirm V1 integrity under the later authorized payload scope and retain its original fingerprint. Existing metadata does not establish usable S3 evidence. Known C04/entitlement-response discrepancies require explicit inclusion of immutable descendant requalification in the later action; no frozen artifact or original response mask may be silently repaired. If such authority/evidence is absent, affected inputs remain unavailable and development stops where dependent. Do not claim a successful freeze validator from the present no-data action.

Deliver a schema/lineage/coverage report and source-contract certificates. Researchers may see coverage/reason codes, not out-of-scope values or outcomes. Any unqualified source, calendar, account applicability or reconstruction is a FEASIBILITY / DATA AVAILABILITY RESULT.

## 4. Conformance implementation and reconstruction checkpoint

Only a later explicit implementation authorization may create S3 code. Its permitted scope is mechanical implementation of the frozen protocol, synthetic fixtures, and structural tests for PIT timestamps, exact identities, state machines, accounting and budget limits; no tunable alternative algorithms.

Required reconstructions:
- As-of identifier/taxonomy/member/registry history including dead funds and corporate actions.
- The approved model response to actual price/cash-flow bridge; annual common exposure history, daily aligned residual replay and exact duplicate physical aggregation.
- Qualified cash-flow-consistent C_H/C_f and historical static J_H; no sum-of-daily-rebalanced-returns substitute.
- Signal time, first qualified post-open snapshot, target persistence, exact shares/lots, shared capital and binding borrow reservations.
- Complete parent-order inventory paths, late fills/abort/legal-unwind, joint exit, cash and borrow closure, unique cost ledger and maturity timestamps.
- Shadow pre-E1 estimation opportunities under the same size/resource/execution rules, distinct from actual executions. Counterfactual fills/impact may be reconstructed only where specifically authorized evidence identifies them; otherwise unobservable.

Certify scale-aware numerical rank/equality/sign/lot checks with documented error bounds before empirical decision use. Do not choose arbitrary cutoff substitutes. P1/reference precision certificates must document dependence, effective information, fixed population and confidence construction before their calculations, and certify the frozen .0005/.01 requirements without support-selected trimming. No particular sample size or inferential guarantee is presumed by this plan. If a defensible certificate cannot be produced under these restrictions, the relevant quantity is unavailable, not a request to choose a friendlier rule.

## 5. Single chronological development pass

Run only if the required input/reconstruction checkpoints pass and the later action permits the listed economic labels.

1. **2015 warm-up:** reconstruct permitted native and auxiliary inputs. Unavailable early history stays unavailable; never extend earlier dates.
2. **2016 formation/reference:** form the predeclared common weighted reference and pre-E1 shadow ledger using only contemporaneously available inputs. Certify tail support. No retrospective admission using future cutoff/P1.
3. **2017H1, 2017H2, 2018H1, 2018H2, 2019H1, 2019H2:** at each origin freeze deterministic registry, completed reference cutoff and mature pooled P1/cost/path components. Purge boundary-overlapping information; unresolved eligible cohorts remain reported, not silently excluded. Process forward chronologically, retaining all coverage/failure flags. Learned components do not refit inside blocks.
4. **2019-end final fit:** one final fit from available mature permitted records. No 2020 labels. At most seven scheduled learned-component fits total, plus the prescribed daily/native refresh.
5. **Scale-only diagnostics:** only H252 MAD and H126 SD, same origins/reference weighting and no second economic portfolio or replacement of primary.
6. **Precision/power disposition:** certify support and candidate future horizon under frozen criteria. 10bp effect and 80% power are ex ante design inputs, not estimates of expected profit. Use development variance/dependence/occurrence without profit-maximizing choices.

No parameter grids, alpha changes, proxy reselection on outcomes, flexible ML, smoothing/P3, alternate eta/caps, repeated support rescue or ranking of economic variants. A pure implementation defect stops the pass and requires logged bounded repair authority, retaining contaminated/exposed lineage; it does not authorize a scientific change or hidden budget reset.

## 6. Outputs and researcher visibility

Mechanically produced artifacts, if supported:
- Qualified source/input manifest and descendant lineage, deterministic proxy IDs by development block, actual dated legal/fee/borrow/timing contracts and resource basis.
- Daily compatible exposures/A/h/w, numeric-certification flags and static T1 diagnostic/qualification records; no tolerance estimation.
- Model scale and weighted empirical z0 with reference-population/support certificate; alpha fixed.
- Immutable attempt/event and cost-component ledger with joint R/G/T/inventory paths, all E-A failures, censor/unknown states, maturity/purging audit.
- Pooled P1 frequencies/raw state means, qualified execution/cost expectations and relevant 5bp precision support; no replacement forecasting family.
- Single development diagnostics report: coverage, concentration, censoring, accounting reconciliation, model probability/gross/duration/execution error, input identification and feasibility limitations.
- Development dependence/information-span and prospective power-planning certificate; mechanically selected shortest qualified 1/2/3-calendar-year horizon or inadequate-feasibility disposition.

A later action must expressly permit event gross payoff, costs, duration and net-return moments needed for these estimates and precision/power calculations. Calling them diagnostics does not make them non-economic. No portfolio PnL curve, Sharpe optimization, winner ranking, 2020–2025 result reveal or held-out test is included in this plan. Researcher-visible economic summaries are limited to the fixed estimation/qualification outputs above; no ad hoc empirical browsing.

## 7. Storage, runtime and resumability

Use one explicitly authorized descendant workspace/storage root. Keep raw licensed payloads and account-sensitive records outside Git; Git stores schemas, manifests, checksums, protocol/conformance records and authorized summaries. Never write into frozen V1 or external D: by implication. Preserve raw inputs immutably; transformations carry parent hashes.

Partition by source/version/instrument/date and by block/attempt for derived artifacts. Checkpoint before and after each fit origin, daily chronological processing boundary and final reconciliation. Each checkpoint records protocol/input/code hash, native state, ledger reservations, last complete event/receipt sequence, unavailable reasons and consumed fit budget. Resume only with matching hashes and idempotent parent IDs; no double fills, duplicate fits or silent skipped obligations.

One canonical writer uses the repository lock. Streaming/chunked processing and cached algebra are permitted engineering choices only if they preserve timestamps, sample/weights and determinism. Runtime exhaustion stops with an incomplete checkpoint; it does not authorize reduced history, approximate algorithms or omitted candidates. Runtime/storage budgets are operational allocations in the later action, not new strategy parameters. No runtime/size feasibility is estimated now.

## 8. Exit from development; validation remains separate

If development qualifies all mandatory requirements, prepare a technical release candidate with exact source/registry/account identities, code/input/model hashes, fitted z0/P1/cost outputs, and prospective calendar/inference certificate. A future release must precede any validation observation; this plan does not acquire future feeds or start validation.

For each permitted 1/2/3-calendar-year candidate, n for the approved validation bootstrap is the count of common scheduled validation sessions in that candidate's fixed calendar. Final n is that of the mechanically selected calendar; it is not the development row count. H=20 and L_information are in common sessions. Lock b=max(H,L_information,ceil(n^(1/3))), 50,000 replicates, documented deterministic protocol-hash seed conversion, plus-one p and five-group Holm .05 before validation. Contract-derived settlement follow-up and the no-access first-session boundary are fixed at release. If calendars, support or weak-dependence certification are inadequate, report unavailable; do not truncate b or extend the horizon.

A new action may authorize prospective validation only after technical conformance and required data/outputs exist. This is access/execution authority, not an ordinary strategy-design gate. No live account order authority is conveyed by this plan or a paper protocol.

Completion of this plan means either qualified bounded development outputs/release candidate or an explicit **FEASIBILITY / DATA AVAILABILITY RESULT**, with consumed budget and unavailable dependencies recorded. Both end with NEXT_ACTION=NONE; neither automatically starts another run.

**S3 PROTOCOL FROZEN / DATA ACQUISITION + DEVELOPMENT AUTHORIZATION REQUIRED**
