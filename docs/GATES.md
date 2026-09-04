# Gate Structure

No gate may be passed by repository activity alone. Each gate requires a recorded decision, listed artifacts, reviewer, and explicit PASS / REVISE / STOP outcome.

| Gate | Purpose | Minimum exit evidence | Status |
|---|---|---|---|
| G0 Economic Thesis | Freeze thesis, monetization aim, initial mechanisms, pair-formation philosophy, information boundary, falsifiability, Observatory quarantine, and governance scope | Approved reduced G0 decision set | **PASS / FROZEN — 2026-09-03** |
| G1 Literature & Mechanism Evidence | Determine what existing evidence says deserves measurement and why through nested G1-01–G1-04 | Approved design/discovery; full-text claim ledger; four synthesis maps; evidence freeze/handoff | **G1-02 REOPENED / IN PROGRESS — G1-03 LOCKED PENDING VERIFIED REVIEWS AND APPROVAL** |
| G2 Measurement & Timing | Define how literature-eligible constructs will be operationally measured: trigger variables, mechanism-discriminator variables, sequential-updating variables, universe, event clock, transformations, validity and rejection logic | Frozen measurement specification and timing DAG/table | Locked |
| G3 Point-in-Time Data & Database | Determine required PIT fields/vintages, source classes/providers, licensing, acquisition, lineage, storage and QA; build only after approval | Approved data-requirement/database design; access and lineage controls | Locked |
| G4 Statistical Protocol Freeze | Freeze estimands, pair-formation evaluation, comparators, splits, metrics, multiplicity controls, quantitative stopping rules, and model-selection protocol | Timestamped preregistration; held-out custody record | Locked |
| G5 Implementation Readiness | Specify algorithms, trading feasibility, costs, execution, and deterministic build controls | Audited implementation plan; no outcome inspection | Locked |
| G6 Development Evidence | Conduct development-only descriptive and predictive work | Reproducible development report; failure log | Locked |
| G7 Held-Out Authorization | Audit compliance before any held-out reveal | Independent audit and bounded access token | Locked |
| G8 Predictive Validation | Evaluate frozen resolution predictions on held-out data | Locked-score report; calibration and stability results | Locked |
| G9 Intervention & Economic Validation | Evaluate the frozen policy, net economics, constraints, capacity, and adverse regimes | Reproducible intervention/economic dossier | Locked |
| G10 Release / Stop | Decide release, redesign, archive, or stop | Final decision and evidence ancestry manifest | Locked |

## Universal fail conditions

Leakage or unverifiable timing; subjective/manual pair assignment in the formal strategy; outcome-informed construct changes; held-out contamination; missing ancestry; irreproducible material artifacts; or breach of an approved stopping rule.
