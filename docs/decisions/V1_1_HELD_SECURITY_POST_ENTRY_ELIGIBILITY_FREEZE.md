# Trading V1.1 held-security post-entry eligibility binding

Decision ID: `TRADING-V1.1-HELD-SECURITY-POST-ENTRY-1.0`.
Date: 2026-09-18. Authority: explicit researcher decision in the current task.
Status: **APPROVED BINDING / NO EXECUTION AUTHORITY**.

## Ancestry and contamination boundary

This is an explicit descendant clarification of `research/TRADING_V1_1_POLICY.json` (`TRADING-V1.1-MORPHOLOGY-OPTION-A-BATCH-1.0`, SHA-256 `851EC63DB822E889F9DC103C87B63BCBAF93EA48810941731686D43CA28A9786`), TRADE-A, EP-A, DECA-A, FD-A, ER-A, Option A and the simultaneous-admission freeze. It resolves G1 in the complete mathematical specification. The ancestor policy and existing scientific payloads are not overwritten.

This decision is recorded after the repository's prior terminal execution history. It is not backdated or claimed to have been part of that historical executable contract. No PnL was computed or inspected during this binding/audit task. The decision neither certifies prior implementation conformance nor authorizes rerunning it.

## Frozen binding

1. Full frozen pair/directional eligibility is required at signal and admission, using only information then available. An ineligible pair cannot create an episode.
2. After valid admission, untraded-counterparty-only ineligibility does not terminate, invalidate, pause or reset the episode. It does not alter its frozen expected relationship state, original gap/excess, direction, identity or holding clock.
3. Holding, valuation, corporate-action accounting, resolution and exit retain all qualification requirements of the actually held security. Failure follows existing unavailable/suspension/accounting rules, never fabricated prices, zero returns or clean-action inference.
4. Peer resolution is `r_j(q)=g−Delta y_j(t,q)`, with trigger `g*r_j(q)≤0`. Source resolution is `r_i(q)=e+Delta y_i(t,q)`, with trigger `e*r_i(q)≤0`. The response sums and their qualification are inherited unchanged. Neither equation uses the untraded counterparty after admission.
5. The entry-inclusive ten-eligible-session clock follows held-security qualification alone. Counterparty-only ineligibility neither pauses nor resets it. Unknown held-security response/accounting intervals remain unavailable and cannot be skipped to create an apparently complete path.
6. New pair-conditioned signals/admissions still require the counterparty. This binding does not authorize re-entry, signal replacement, anchor refresh or episode stacking.
7. No T01–T12, direction, sizing, cap, cost, source, estimator, metric or data rule is otherwise changed. Known suspension keeps exits pending under the existing first-qualified-open rule; it does not waive valuation or response qualification.

The complete equations and held-security predicates are in `docs/stages/G5/V1_1_COMPLETE_TRADING_STRATEGY_MATHEMATICAL_SPECIFICATION.md`, sections 5–6. C04 correction, trading execution, PnL inspection and V2 remain paused pending separate researcher approval/action.
