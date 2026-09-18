# Trading V1.1 final economic evidence

Status: **TERMINAL / VALIDATED WITH EXPLICIT UNAVAILABLE SCOPE**.

H6: `ECONOMICALLY_UNAVAILABLE_NO_COMPLETE_FOLD_H6_DISPOSITION`.

One-shot inner execution: 60 candidate/fold checkpoints, all 180 cost-books validated before first disclosure. The ledger also records 108 uncomputed OF4/held-out cost-fold books as input-lineage unavailable. Unavailable is not zero return, a losing trade, or a supported/rejected profitability hypothesis.

No complete-book metric is inferred from a qualified prefix. No book is restarted or survivor-renormalized after an unqualified held interval. No new across-fold mean/median, ranking, p-value, threshold or winner is introduced.

## All six books and all three frozen costs

| Candidate | Cost bps | Inner complete / 10 | Inner unavailable / 10 | OF4 / held-out | Peer / source entries observed | Short unavailable observed | Funding unavailable observed | Coexistence sessions observed |
|---|---:|---:|---:|---|---|---:|---:|---:|
| V1-R0D-252M | 5 | 0 | 10 | Unavailable / unavailable | 93544 / 85207 | 183807 | 0 | 22 |
| V1-R0D-252M | 10 | 0 | 10 | Unavailable / unavailable | 93544 / 85207 | 183807 | 0 | 22 |
| V1-R0D-252M | 20 | 0 | 10 | Unavailable / unavailable | 93544 / 85207 | 183807 | 0 | 22 |
| V1-R0C-126W | 5 | 0 | 10 | Unavailable / unavailable | 101684 / 94714 | 202099 | 0 | 21 |
| V1-R0C-126W | 10 | 0 | 10 | Unavailable / unavailable | 101684 / 94714 | 202099 | 0 | 21 |
| V1-R0C-126W | 20 | 0 | 10 | Unavailable / unavailable | 101684 / 94714 | 202099 | 0 | 21 |
| V1-R0L-126W | 5 | 0 | 10 | Unavailable / unavailable | 101684 / 94714 | 202099 | 0 | 21 |
| V1-R0L-126W | 10 | 0 | 10 | Unavailable / unavailable | 101684 / 94714 | 202099 | 0 | 21 |
| V1-R0L-126W | 20 | 0 | 10 | Unavailable / unavailable | 101684 / 94714 | 202099 | 0 | 21 |
| V1-R1M-126W | 5 | 0 | 10 | Unavailable / unavailable | 174073 / 109409 | 222109 | 0 | 22 |
| V1-R1M-126W | 10 | 0 | 10 | Unavailable / unavailable | 174073 / 109409 | 222109 | 0 | 22 |
| V1-R1M-126W | 20 | 0 | 10 | Unavailable / unavailable | 174073 / 109409 | 222109 | 0 | 22 |
| V1-R1MI-126W | 5 | 0 | 10 | Unavailable / unavailable | 185786 / 111625 | 203925 | 0 | 22 |
| V1-R1MI-126W | 10 | 0 | 10 | Unavailable / unavailable | 185786 / 111625 | 203925 | 0 | 22 |
| V1-R1MI-126W | 20 | 0 | 10 | Unavailable / unavailable | 185786 / 111625 | 203925 | 0 | 22 |
| V1-R3-252M | 5 | 0 | 10 | Unavailable / unavailable | 90097 / 84295 | 185233 | 0 | 21 |
| V1-R3-252M | 10 | 0 | 10 | Unavailable / unavailable | 90097 / 84295 | 185233 | 0 | 21 |
| V1-R3-252M | 20 | 0 | 10 | Unavailable / unavailable | 90097 / 84295 | 185233 | 0 | 21 |

**Coverage is observed prefix coverage, not full-period deployability.** The checksum-bound ledger retains channel-specific entry, blocked re-entry, entry-execution-unavailable, funding-unavailable, short-unavailable, conflict, MP1-unavailable and coexistence counts. Counts after the first unevaluable portfolio interval are not fabricated.

## Qualified complete-fold returns only

| Candidate | Fold | Cost bps | Net cumulative | Annualized return | Annualized vol | Sharpe | Maximum drawdown | Turnover | Open terminal episodes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| All six books | All inner folds | 5 / 10 / 20 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable as full-fold metric | Preserved in private checkpoint state |

## Unavailable accounting scope

| Reason | Cost-fold books |
|---|---:|
| C04_ACTION_WITHOUT_QUALIFIED_ENTITLEMENT | 87 |
| UNQUALIFIED_HELD_OPEN_PRICE_OR_C05_ID | 93 |
| Immutable post-2019 input C04 exclusion mismatch | 108 |

The official calendar itself passed the original bounded C04-A exclusion contract. However, the later model-input masks omit newly identified action exclusions; a trading overlay cannot retroactively qualify those immutable predictions. Inner T09 failures and exact date/security indices are retained in the evidence ledger. No entitlement, adjusted-price substitution, borrowing or delayed-entry search was invented.

Both channels remain morphology-only economic probes, not M1/M2/M0 identification. Original A6/G5 stays V1 NON-ESTIMABLE / NOT EXECUTED. H4 remains computationally incomplete.

[Complete checksum-bound evidence ledger](../../../data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json). [Input qualification and later-book limitation](V1_1_FINAL_INPUT_QUALIFICATION.md).
