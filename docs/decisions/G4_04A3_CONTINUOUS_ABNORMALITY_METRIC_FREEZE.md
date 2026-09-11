# G4-04A3 Continuous Abnormality Metric Freeze

Decision date: 2026-09-11
Status: **APPROVED / FROZEN**

## Frozen abnormality object

- raw directional departure is observed directional response minus PIT expected directional response;
- `i -> j` and `j -> i` remain separate;
- A3 applies no M1/M2-oriented sign transformation;
- scaling inherits the candidate-neutral MAD architecture;
- candidate-specific uncertainty is excluded from the point-abnormality denominator;
- uncertainty, relationship validity, scale quality, and PIT lineage remain separate channels;
- the Security-Date Eligibility Sidecar and candidate-specific eligibility rules propagate into computation;
- `raw observation eligibility != abnormality-computation eligibility`;
- same-decision anti-circularity ordering holds under every refresh cadence, including U1D;
- abnormality states are representation-specific but mechanism-neutral;
- relationship-break evidence is a parallel diagnostic rather than abnormality magnitude;
- subordinate summaries may serve attention/ranking/monitoring only;
- `abnormality != mechanism identification`;
- no abnormality-to-M3 mapping exists.

No threshold, probability, trigger, weighted score, trading inference, data access, or computation is authorized.
