# Data Requirement Register

Status: **G1-02 CLAIM-LINKED INPUT TO G1-03 — NOT YET THE FORMAL LITERATURE-DERIVED DATA REQUIREMENT MAP**

Frequency and history are literature-motivated candidate requirements, not frozen specifications. PIT means only the version publicly available at the decision timestamp, including publication and revision lags. G1-03 must synthesize these rows into the formal Literature-Derived Data Requirement Map; G1-04 must classify permitted downstream use before any row may enter G2.

| ID | Construct | Candidate observable | Role | Frequency | PIT requirement | Required history | Source class (not provider) | Raw / derived | Claim ID |
|---|---|---|---|---|---|---|---|---|---|
| DR-001 | Product-market proximity | Versioned business/product text; pairwise semantic similarity | P | Filing-event / annual | Filing public timestamp; retain amendments | Multiple annual vintages to observe drift | Regulatory/issuer filings | Raw text + derived | CL-PF-001 |
| DR-002 | Raw co-movement | Adjusted prices/returns; normalized-price distance | P/S | Daily candidate | PIT corporate actions and universe | Separate formation windows; length deferred | Exchange/market records | Raw + derived | CL-PF-002 |
| DR-003 | Conditional replicability | Lagged return panel; sparse replicate weights and fit | P/R | Daily candidate | Universe/inputs frozen at estimation time | Rolling history; length deferred | Market records | Raw returns + derived | CL-PF-003 |
| DR-004 | Relationship persistence | Rolling dependence/cointegration edge and survival/recurrence | P/R | Daily or periodic | Trailing observations only | Multiple rolling/nonoverlapping windows | Market records | Derived | CL-PF-004 |
| DR-005 | Relationship break | Spread diagnostics; stationarity/break probability | R | Intraday/daily candidate | Data through decision time; record detection delay | Baseline plus monitoring window | Market records | Derived | CL-PF-005 |
| DR-006 | Directed economic linkage | Customer–supplier identity, direction, exposure and disclosure date | P/C/R | Disclosure-event / periodic | Public release/effective timestamps; no backfill | Several reporting vintages | Regulatory/issuer relation disclosures | Raw relation + derived network | CL-M1-001, CL-M1-003 |
| DR-007 | Source-follower timing | Timestamped source news/announcement and linked-firm return | C | Event/intraday/daily | First-public timestamp and revisions | Event history across regimes | Exchange/regulatory news archive | Raw + derived event measures | CL-M1-001, CL-M1-003 |
| DR-008 | Attention/leader context | Lagged size, idiosyncratic volatility, visibility/competition, directed lag | C/R | Daily/monthly candidate | All definitions and accounting inputs lagged | Rolling multi-regime history | Market, filings, coverage archives | Mixed | CL-M1-002 — **PRELIMINARY / NOT ADMITTED: unresolved full-text access; no current G2 use** |
| DR-009 | Forced-flow pressure | Fund flows, lagged holdings, predicted trades; corrected flow ratios | C/R | Native reporting frequency | Actual release dates; prohibit embedded contemporaneous return | Several reporting cycles | Fund filings/holdings/flow records | Raw + audited derived | CL-M2-001, CL-M2-002 |
| DR-010 | Exogenous liquidity timing | Settlement/payment calendar; institutional net sales scaled by beginning market cap | C | Calendar/daily | Calendar known ex ante; record trade-data availability | Many month ends/rule regimes | Official calendars; transaction-class records | Raw + derived | CL-M2-003 |
| DR-011 | Liquidity / oversupply rivals | Spread, depth, turnover, Amihud illiquidity, abnormal volume, market cap | C/R | Intraday/daily candidate | Quotes/trades only through decision time | Rolling baseline plus event window | Exchange quote/trade records | Raw + derived | CL-M2-004, CL-B4-001 |
| DR-012 | Fundamental news | Forecast revisions, issuer announcements, earnings/cash-flow-news component | C/R | Event/daily | First-public and revision timestamps; original vintage | Multiple events and regimes | Analyst archive; regulatory/issuer news | Raw + derived | CL-M3-001, CL-B4-001 |
| DR-013 | Idiosyncratic relative component | Return residual after frozen common-risk and news controls | S/C | Daily candidate | Trailing estimates and PIT characteristics | Rolling estimation history | Market and PIT company/factor inputs | Derived only | CL-PF-003, CL-M3-001 |
| DR-014 | Structural/fundamental divergence | Corporate event, business/link/fundamental change, relationship break | R | Event/daily/periodic | Publication/effective timestamps; preserve taxonomy vintages | Multi-year vintages plus events | Regulatory/issuer disclosures and PIT fundamentals | Mixed | CL-PF-001, CL-PF-004/005, CL-M0-001 |
| DR-015 | Ex-post resolution | Continuation/reversal/non-resolution path | Outcome only | Intraday/daily horizons | Strictly unavailable to event-time mechanism assignment | Candidate horizons deferred | Market records | Derived outcome | CL-M2-004, CL-B4-001 |

## G1-02b addition — still provisional

| ID | Construct | Candidate observable | Role | Frequency | PIT requirement | Required history | Source class (not provider) | Raw / derived | Claim ID |
|---|---|---|---|---|---|---|---|---|---|
| DR-016 | Permanent/transitory microstructure component | Timestamped trade price and quote; signed trade/order flow; liquidity-provider/quote-competition proxy; model-conditional permanent/transitory component | C/R | Tick/intraday candidate | Exchange timestamps, quote/trade sequence and any model input must be available by the decision timestamp; prohibit future-interval revisions in event-time use | Multiple intraday periods, liquidity regimes and event windows; length deferred | Exchange trade/quote/order-book records | Raw + derived | CL-B4-002 |
| DR-017 | Pair-candidate overlap governance | Candidate-pair incidence graph; shared-asset count/concentration and candidate-edge weight lineage | P/R | Formation-period candidate | Candidate edges, weights, universe and overlap rule frozen from PIT information before portfolio governance use | Repeated formation vintages; length deferred | Derived from approved candidate relationship inputs | Derived | CL-PF-010 |

## Prohibitions before G1-04 handoff

- No provider, field, frequency, lookback, formula, threshold, classifier, or schema is selected at G1.
- A residual, later reversal, later continuation, or profitable trade is not a mechanism label.
- Any flow-pressure measure requires an algebraic audit for embedded contemporaneous/future returns.
- Observatory-only ideas remain outside this register until a literature Claim ID is admitted.
