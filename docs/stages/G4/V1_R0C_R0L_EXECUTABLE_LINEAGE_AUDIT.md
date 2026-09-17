# V1 R0-C / R0-L Executable Lineage Audit

Status: `PASS — EXACT A1 EQUALITY IS SPECIFICATION-CONSISTENT`

This audit is source/lineage-only. It inspected no additional empirical value.

The executable registry retains two distinct candidates:

- `V1-R0C-126W`: Pearson relationship representation plus the matched R0-LIN directional bridge, H126/U1W.
- `V1-R0L-126W`: the primary R0-LIN OLS directional baseline, H126/U1W.

In `tools/v1_phase1_inner_relationships.py`, candidate kinds 1 and 2 are distinct. Kind 1 computes and stores the Pearson `representation` field. Both kinds then intentionally enter the same `kind <= 2` OLS bridge, using the same qualified H126 observations, refresh clock, directional equations, predicted responses, native scales and prediction uncertainty. Kind 2 has no separate representation statistic.

The H126 A1 layer consumes the immutable directional expected responses and candidate-neutral scale, not the R0-C Pearson representation field. Therefore R0-C and R0-L have identical A1 losses by frozen construction while remaining distinct relationship-representation records. No implementation alias, candidate-ID collision, path collision or array reuse was found.

Disposition: proceed under the frozen complete candidate set. Do not collapse, delete or reinterpret either candidate.
