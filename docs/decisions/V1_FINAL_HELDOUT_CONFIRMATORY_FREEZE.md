# V1 Final Held-Out Confirmatory Evaluation Freeze

Decision ID: `V1-FINAL-HELDOUT-CONFIRMATORY-1.0`

Status: `APPROVED / FROZEN — ACCESS AUTHORIZED, RESULTS NOT YET MATERIALIZED`

Accepted ancestry: canonical pre-held-out checkpoint at commit `27be564a5fd24b5e10ba63e114cff3553f478d5a`.

## Confirmatory questions and frozen bindings

The final 2024–2025 evaluation asks only whether the already-observed dependency-ordered descriptive structure persists. It is not a new model-selection environment.

| Question | Frozen comparison (`right - left`) | Registry basis |
|---|---|---|
| C1 market-adjustment incremental value | `V1-R1M-126W - V1-R0L-126W` | R0-L is the primary directional baseline; R1-M adds the frozen market adjustment on the same H126/U1W geometry |
| C2 industry-adjustment incremental value | `V1-R1MI-126W - V1-R1M-126W` | identical R1 equation/estimator/support; industry factor is the registered increment |
| C3 hierarchical-pooling incremental value | `V1-R3-252M - V1-R0D-252M` | the registered H252/U1M non-hierarchical representation baseline and H252/U1M pooling candidate |
| C4 dynamic-adaptation incremental value | `V1-R4-63D - V1-R0L-126W` | registered dynamic candidate versus the registered primary static directional baseline; their frozen H/U histories remain different and are not retuned |

Negative loss differences are descriptively lower for the incremented/right candidate. No numerical effect threshold, inferential significance threshold, winner rule, or unique-winner claim is created.

## Frozen execution

- Candidate set: all seven already-authorized R0/R1/R3/R4 candidates.
- Region: `2024-01-01` through `2025-12-31` only for evaluated held-out folds, with earlier frozen observations available solely as PIT history.
- Primary loss: absolute error divided by candidate-neutral H126 PIT `1.4826 × MAD`.
- Robustness loss: squared error divided by the squared H126 sample standard deviation (`ddof=1`).
- Scale observations are qualified, directionally aligned and strictly prior to the evaluated event; 126 means qualified observations, not calendar days.
- Aggregation: exact common support, exact within-pair median, equal pair influence, directional vectors, and exact temporal median across the two annual held-out folds.
- Native support is reported separately for coverage/deployability and never substitutes for common-support attribution.
- Existing PAIR-A, PIT, C04/C05/C06, missingness, provenance, SR0→SR1, Search Budget, multiplicity and severe-failure governance remain unchanged.
- Relationship, RT3, A3 and A5 use their already-frozen implementations. No retuning, rescue, candidate reduction, sampling, Top-K, or post-access semantic amendment is permitted.
- `A6/G5 = V1 NON-ESTIMABLE / NOT EXECUTED`; this is an evidence/data-availability limitation, not negative trading performance.

## Interpretation boundary

Inner and OF4 evidence remains descriptive pseudo-OOS evidence. Held-out evidence is confirmatory descriptive evidence under the frozen comparison architecture. No p-value, confidence interval, new multiplicity procedure, numerical effect threshold, forced ranking, or unique-winner rule may be added.

After the first held-out byte is read, model, metric, scale, support, threshold, aggregation, Search Budget, pair universe, comparator and claim definitions are irreversibly closed for V1.

## Access and execution control

One-time access is authorized. The external checkpointed runner must create an atomic, checksum-bound, append-only access event before reading any held-out input. The event binds this decision, the accepted pre-held-out commit, the core freeze fingerprint, the runner version, host/process/time, and `held_out_accessed=true`. Existing access-event content may be verified but never replaced or cleared.

Long computation must be researcher-operated from an independent PowerShell terminal. External payloads use `D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1` and temporary-write → validate → checksum → atomic-finalize semantics. Progress metadata must not disclose scientific values.
