# G2B Pre-G3B Data Requirement Handoff

Status: **APPROVED / FROZEN — 2026-09-08**  
G3B: **LOCKED / NOT AUTHORIZED**

## Core raw information classes for surviving primary candidates

- Vintaged A-share security master: identifiers, listings/delistings, suspensions, corporate actions and adjustment lineage.
- Ordered PIT market observations covering the intended historical universe, with common-clock support and observed price/return/volume/turnover fields at a not-yet-selected granularity.
- Vintaged industry/classification and benchmark membership sufficient for N0 and simple exposure context.
- Source and transformation lineage supporting the frozen six-time vocabulary, immutable decision states and repeated formation vintages.
- Data-quality/availability/revision metadata required by R3 and U0/U4.
- Relationship-history storage sufficient to reconstruct N0/N1 states, uncertainty and break warnings without future leakage.

## Competing implementable data classes

- PIT benchmark/exposure inputs for P0-EXP/RR-EXPOSURE.
- Declared conditioning inputs for P0-RES/RR-RESID/A-RES.
- Longer adjusted histories for stochastic/cointegration candidates.
- Public announcement documents and verified original-publication/version metadata for R1.
- Accessible PIT liquidity/turnover context for MP1.

## Optional enhancement classes — absence does not block core

- Dated economic/company relationship and directed-link histories for P1/R2.
- Finer ordered observations for A-TIME and richer M1/M2 context.
- Pressure-source/flow holdings with contamination lineage for MP2.
- Structured event/NLP enrichments for R1.

## Research-only / blocked classes

- Broad historical L2 trades/quotes/orders/signed-flow infrastructure for MP3.
- Outcome-side M3 discovery targets, which require a later frozen protocol and separate outcome store.
- N2 hierarchical inputs before escalation authorization; U3 decision-policy inputs before decision design.

## Outcome-side resolution-validation information classes

To avoid an input-only database, a later G3B design must be capable of retaining strictly future, separately partitioned observations sufficient to construct—not predefine—the following validation-target families:

- peer/follower response paths that may later support catch-up magnitude and timing targets;
- shocked/source-asset response paths that may later support normalization or reversal magnitude and timing targets;
- continued relative-response paths sufficient to represent persistence or non-resolution;
- future relationship-state histories sufficient to assess relationship continuation versus later break;
- event-origin and future observation timestamps sufficient to define candidate validation horizons later;
- observed response magnitudes needed to quantify degree of resolution later.

These are outcome-side information classes, not labels, formulas, horizons or model choices. They must be stored outside every earlier event-time information set and may never be used as contemporaneous mechanism inputs. Their presence does not authorize M1/M2/M3 identification or empirical inspection.

This handoff names raw information classes, not providers, fields, frequencies or acquisition plans. Approval of G2B would still not activate G3B.
