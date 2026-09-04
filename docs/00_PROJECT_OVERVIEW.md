# Project Overview and Research Charter

## Research question

Can fully data-driven, point-in-time market-relationship evidence, optionally augmented by incrementally validated company/economic context, support sequential mechanism/resolution updating and a later trade/update/reject/abstain decision for abnormal relative states among A-share machinery stocks, with economic value assessed only later under realistic frictions?

## Active strategy architecture

`Company Representation → Industry-Specific Relationship Prior → Pair-Specific Normal Relationship → Continuous Pair-Specific Abnormality → Sequential Mechanism & Resolution Updating → Trade / Update / Reject / Abstain`

This is the active architecture under D-014. The exact G0 pipeline remains preserved as a historical freeze record and is not overwritten. Mechanism and resolution beliefs may update jointly as new PIT information arrives; neither a hard mechanism label nor a selected update model is authorized.

## Unit of inquiry

Conceptually, the project concerns a time-indexed company-pair state, a sequential evidence history and a later decision. The exact security universe, representation, relationship-prior rule, trigger, event clock, state measure, update model, horizons, and trade implementation are deferred to later gates.

## Pair-formation boundary

Formal strategy pair formation must be:

- **company-aware:** capable of using legitimate information about firms and businesses;
- **fully data-driven:** formal inclusion follows a declared reproducible rule, not researcher assignment;
- **point-in-time:** only information available at formation time may be used;
- **reproducible:** identical declared inputs and environment reproduce the same pairs;
- **generalizable:** the rule must apply beyond hand-picked examples and be assessed outside development data.

Company/business characteristics, factor exposures, empirical co-movement, and relationship stability are candidate information families. G0 does not select factors, formulas, weights, distances, thresholds, clustering methods, learning algorithms, or refresh rules. Manual examples may be used later for exposition only and may never enter the formal strategy as assigned pairs.

Under approved D-016, observed PIT market/statistical relationship evidence is primary for formal pair validity. Company/economic proximity is a secondary candidate prior/context input, not a required core factor, and may remain only after prespecified incremental relationship-level validation against P0.

## Claims are separated

1. **Description:** characterize candidate information and relative states.
2. **Prediction:** forecast resolution using information available at the decision time.
3. **Intervention:** compare an explicit trade/no-trade policy with a predeclared comparator.
4. **Economic validation:** test net implementability under eligibility, costs, constraints, capacity, and held-out evaluation.

Evidence for one layer does not establish the next.

## G0 scope lock

G0 freezes only the economic thesis and population boundary at a conceptual level, monetization objective, M0–M3 as initial hypotheses, pair-formation philosophy, causal and point-in-time information boundary, Observatory quarantine, falsifiability standard, claim separation, and governance authority. Constructs, literature conclusions, measurements, estimands, validation protocol, algorithms, and implementation details belong to later gates.

## Governance principles

Freeze before inspection; preserve causal timing and point-in-time information; record material decisions; separate development and held-out evidence; retain evidence ancestry; produce deterministic artifacts; predeclare stopping rules before empirical work; and prohibit retrospective relabeling using predicted outcomes.

## Canonical documentation

- [Economic Thesis](01_ECONOMIC_THESIS.md)
- [Strategy Architecture](02_STRATEGY_ARCHITECTURE.md)
- [Literature Evidence](03_LITERATURE_EVIDENCE.md)
- [Measurement Design](04_MEASUREMENT_DESIGN.md)
- [Research Governance](05_RESEARCH_GOVERNANCE.md)

`Canonical docs = current truth`; `Stage docs = active working state`; `Archive = completed historical process`.
