# V1 MP1-A Common H126 / U1W PIT Reference Freeze

Decision date: 2026-09-15

Decision ID: `V1-MP1-A-1.0`

Status: **RESEARCHER APPROVED / FROZEN**

MP1 uses a candidate-neutral normal transaction-size/liquidity reference based on `amount / volume`. At each authorized weekly refresh, the reference is the median of the most recent 126 qualified observations available strictly before that refresh.

A qualified reference observation has finite `amount` and `volume`, both strictly positive, a positive finite ratio, and a qualified security-date state under the frozen C04/C05/identity contracts. Missing, zero, suspension, unknown-missingness, or otherwise ineligible observations do not enter as zeroes.

`H126` counts qualified observations, not calendar days. The reference is refreshed at the first authorized eligible ISO-week point and carried forward within the week. The evaluated observation never enters its own reference.

The same reference state is consumed across R0/R1/R3/R4. Relationship-model H/U geometry never changes MP1 reference geometry. If 126 prior qualified observations do not exist, MP1 reference support is unavailable; no shortened window, expanding substitute, other-security borrowing, epsilon, or fallback median is permitted.

`MP1-B H63/U1D` and `MP1-C expanding-history` are not selected for V1 and cannot rescue V1 results.

`V1-MP1-A-1.0 — APPROVED / FROZEN`
