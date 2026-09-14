# V1 R4 CF-A Benchmark Disposition

Date: 2026-09-14
Status: **CF-A PASSED / R4 INCLUDED IN V1**

Under `V1-R4-CF-A-CF-B-1.0`, a fixed-seed synthetic benchmark used the frozen scalar random-walk-slope likelihood and single L-BFGS-B path. It used 4,000 synthetic fits, eight isolated worker processes, and no research value. Median optimizer evaluations were 9; measured aggregate throughput was approximately 1,472 fits/second. The 4,285,028 structurally required monthly pair-direction fits project to approximately 0.81 hour at that measured throughput. Projected state output is approximately 5.6 GB before compression/checkpoint metadata.

The benchmark satisfies the five-day feasibility gate with implementation/restart margin. Activate CF-A:

- complete PAIR-A;
- daily U1D state prediction/update;
- monthly PIT-ML Q/R re-estimation strictly before each monthly origin;
- deterministic within-month Q/R carry-forward;
- no scientific-semantic degradation.

CF-B remains registered but was not triggered. This disposition uses runtime/resource evidence only and says nothing about R4 model quality.

OF4 and held-out were not accessed.

`CF-A PASSED / PHASE 1 RESUME AUTHORIZED`
