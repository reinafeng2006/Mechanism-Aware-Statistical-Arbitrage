# Gate Structure

No gate may be passed by repository activity alone. Each gate requires a signed decision record, listed artifacts, reviewer, and explicit PASS / REVISE / STOP outcome.

| Gate | Purpose | Minimum exit evidence | Status |
|---|---|---|---|
| G0 Economic Thesis | Freeze economic objects, falsifiable mechanism claims, scope, decision problem, and stopping logic | Approved G0 thesis record and resolved decision IDs | **STOPPED / unresolved** |
| G1 Constructs & Literature | Independently define P/S/C/R constructs, mechanisms, counter-hypotheses, and literature map | Construct dictionary; literature protocol; discriminating implications | Locked |
| G2 Measurement & Timing | Specify point-in-time universe, event clock, labels, availability lags, and leakage tests | Measurement plan; timing DAG/table; data-access approval | Locked |
| G3 Protocol Freeze | Freeze estimands, comparators, splits, metrics, costs, multiplicity controls, and stopping rules | Timestamped preregistration; held-out custody record | Locked |
| G4 Development Evidence | Conduct development-only descriptive and predictive work | Reproducible development report; failure log | Locked |
| G5 Held-Out Authorization | Audit protocol compliance before any held-out reveal | Independent audit and bounded access token | Locked |
| G6 Predictive Validation | Evaluate frozen resolution predictions on held-out data | Locked-score report; calibration and stability results | Locked |
| G7 Intervention Validation | Evaluate frozen trade/no-trade policy against comparator | Policy contrast without economic overclaim | Locked |
| G8 Economic Validation | Assess net returns, constraints, capacity, robustness, and adverse regimes | Reproducible economic dossier | Locked |
| G9 Release / Stop | Decide release, redesign, archive, or stop | Final decision and evidence ancestry manifest | Locked |

## Universal fail conditions

Leakage or unverifiable timing; outcome-informed construct changes; held-out contamination; missing ancestry; irreproducible material artifact; mechanism classes that are not empirically distinguishable; or breach of a predeclared stop rule.
