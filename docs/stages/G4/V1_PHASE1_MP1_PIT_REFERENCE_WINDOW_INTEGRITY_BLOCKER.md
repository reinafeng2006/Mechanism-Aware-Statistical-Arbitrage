# V1 Phase 1 MP1 PIT Reference-Window Integrity Blocker

Date: 2026-09-14

Status: **GENUINE SCIENTIFIC / EXECUTABLE-SEMANTICS BLOCKER**

## Completed before the stop

`V1-RT3-RELATIONSHIP-STATE-AUGMENTATION-1.0` is published and qualified. All 70 authorized 2015–2019 candidate × half-year partitions passed exact replay equivalence with zero shared-field mismatches. The original `V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0` artifacts and hashes remain unchanged. No relationship result was interpreted.

## Exact blocker

The frozen V1 registry defines MP1 amount and volume context as:

`log(current activity / median_PIT(prior activity))`.

The frozen executable semantics then use the amount component directly in `PV-M2` and require a positive available amount log-ratio for `TV1-M2 ELIGIBLE`. No repository contract specifies:

- the PIT historical reference window for the prior median;
- whether support is counted in source-security eligible sessions, pair-synchronized sessions, or calendar/exchange sessions;
- whether the reference is updated daily or carried between a frozen refresh cadence; or
- the mathematically required support when the authorized history contains unavailable/nonpositive activity.

Selecting these in software would change MP1, PV-M2, M2 entry eligibility, episode formation, and PnL. This is not a mechanical engineering detail and cannot be inferred from a relationship candidate's H/U tuple without also making MP1 candidate-dependent and confounding relationship-model comparisons.

## Bounded alternatives

1. **MP1-A — common H126 / U1W PIT reference.** For every relationship candidate, use the most recent 126 finite, positive, source-security eligible activity observations strictly before the decision event; refresh on the first eligible exchange session of each ISO week and carry the median within week. This keeps MP1 candidate-neutral across relationship representations and uses an already registered medium-history/calendar cadence, but newly binds that geometry to MP1.
2. **MP1-B — common H63 / U1D PIT reference.** Use the most recent 63 finite, positive source-security eligible observations strictly before every event. This is more adaptive and operationally heavier; it may respond more strongly to short-lived activity regimes.
3. **MP1-C — expanding PIT reference.** Use all finite, positive source-security eligible activity observations available strictly before the event. This avoids a new finite-window choice but makes the reference increasingly slow and calendar-age dependent.

For all alternatives, amount and volume are separate; nonpositive/nonfinite activity is unavailable rather than imputed; current-event activity never enters its own reference median; and no empirical distribution or result may choose the alternative.

Recommendation: **MP1-A**. A common H126/U1W reference best preserves cross-representation attribution, avoids silently importing each model's different H/U geometry into the M2 evidence definition, and remains a bounded medium-horizon PIT state. This recommendation is ex ante and used no activity values, coverage counts, model outputs, outcomes, or PnL.

The decision cannot be deferred if frozen PV-M2 and G5 M2 are to remain in V1. Deferral would require an explicit V1 scope amendment; it cannot occur silently.

After approval: freeze the selected MP1 reference contract, publish it, then resume the existing A3 → A5 → A6 → G5 inner-only action without recomputing R0/R1/R3/R4 or RT3 augmentation.

`V1 MP1 PIT REFERENCE WINDOW / RESEARCHER DECISION REQUIRED`
