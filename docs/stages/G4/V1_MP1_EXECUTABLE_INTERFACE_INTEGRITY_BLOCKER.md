# V1 MP1 Executable Interface Integrity Blocker

Status: **GENUINE SCIENTIFIC-SEMANTICS BLOCKER / RESEARCHER DECISION REQUIRED**

Date: 2026-09-15

The published `V1-MP1-A-1.0` contract defines one candidate-neutral reference object: the weekly carried median of the most recent 126 qualified historical `amount / volume` ratios. The pre-existing frozen executable amendment instead defines two distinct PV-M2 fields, `MP1_amount_log_ratio` and `MP1_volume_log_ratio`, and makes M2 trade eligibility depend on `log(amount / median_PIT(amount)) > 0`.

These are not the same mathematical object. The approved ratio reference cannot mechanically supply the separately frozen amount and volume normalizations. Implementing it as the legacy amount field would change that field's economic meaning and the M2 entry gate; inventing a separate volume reference would exceed MP1-A; retaining the old amount/volume medians would contradict the newly published MP1-A contract.

This conflict was found by a pre-execution contract audit before any activity values, A3 abnormality, A5 outcome, A6 result, trade, PnL, OF4, or held-out information was inspected. Existing relationship outputs and the qualified RT3 augmentation remain unchanged.

## Bounded resolutions

1. **MP1-I-A — ratio-native interface.** Amend PV-M2 to one primary `log((amount/volume) / median_PIT(amount/volume))` field plus its availability state; make the frozen M2 gate use that positive ratio-native field. Remove the unsupported separate volume-normalization claim from V1. This exactly follows MP1-A but explicitly amends EXEC-A/G5.
2. **MP1-I-B — separate activity references.** Amend MP1-A so H126/U1W applies separately to `amount` and `volume`, retaining the existing PV-M2 fields and amount-based M2 gate. This retains EXEC-A/G5 but changes the just-published MP1 reference object.
3. **MP1-I-C — defer M2 execution for V1.** Preserve both contracts and exclude PV-M2/M2 trading until a consistent interface is separately frozen. M1 and non-M2 scientific work could continue only under an explicit V1 scope amendment.

Recommendation: **MP1-I-A**. It preserves the researcher's latest explicit mathematical choice—`amount / volume` as the reference object—and makes the smallest transparent downstream amendment. It is not applied automatically because it changes the frozen PV-M2 design matrix and M2 entry condition.

`V1 MP1 EXECUTABLE INTERFACE / RESEARCHER DECISION REQUIRED`
