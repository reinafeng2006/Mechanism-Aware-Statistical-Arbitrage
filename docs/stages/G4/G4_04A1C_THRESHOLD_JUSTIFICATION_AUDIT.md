# G4-04A1c Threshold Justification Audit

Status: **ACCEPTED — HISTORICAL JUSTIFICATION RECORD / BUNDLES REJECTED**
Boundary: ex-ante semantic audit only. No frozen-data, survival-count, pair-count, distribution, or outcome inspection. Neither bundle is selected or frozen, and no value is changed.

## Frozen meta-principle

`thresholds encode preregistered failure/adequacy semantics; thresholds must not be chosen to achieve a desired candidate survival rate`.

## Exact bundle comparison

Let:

- `Q_scale = directional_MAD / PIT_cross_pair_median_directional_MAD` for the same response semantics at the same pre-origin information set;
- `support_ratio = eligible directional observations / nominal authorized history observations`;
- `A = median absolute candidate-neutral-PIT-scaled loss` for a pair-direction-origin;
- `D_rel = (candidate_loss - comparator_loss) / comparator_loss` on CS2 common support, where positive is adverse;
- `C_ret = common eligible pair-dates / min(named-candidate native eligible pair-dates)` within the frozen comparison layer.

| Rule | Conservative | Permissive | Statistical interpretation | Economic/relationship interpretation | Governance role | Ancestry | Immediately below vs above | Justifiable without survival/performance? |
|---|---:|---:|---|---|---|---|---|---|
| Relative scale quality | `Q_scale >= 0.10` | `Q_scale >= 0.05` | Directional MAD must be at least 10%/5% of the PIT cross-pair median scale | Response variation must be sufficiently identifiable relative to contemporaneous peer-scale context | support-state governance; not candidate performance | robust-scale theory for the ratio object; numerical value is design convention | below: scaled loss unavailable with `SCALE QUALITY / NEAR-ZERO SCALE`; above: scale-qualified, subject to other rules | Object is justifiable; 5% versus 10% is not uniquely justified without a stronger ex-ante tolerance rationale |
| Minimum estimator support | `support_ratio >= 0.90` | `support_ratio >= 0.80` | Requires 90%/80% of nominal eligible directional observations plus the frozen synchronized-history contract | Scale summarizes most of the intended relationship-history interval | support-state governance; may feed SR0 only if the representation contract makes it constitutive | history/support theory plus design convention; no literature-derived percentage | below: scale estimator unavailable; above: estimator support-qualified | Direction is justifiable; exact 80%/90% choice is conventional |
| Absolute-adequacy severe failure | severe if `A > 2.0` | severe if `A > 3.0` | Median directional OOS error exceeds 2/3 historical MAD scale units | Typical response error is materially large relative to the pair-direction's normal response variation | AG2 / SR1 use-adequacy guardrail, not ordinary comparative ranking and not automatically SR0 | robust-normalization theory; numerical value is design convention | at/below: no SF0 flag; above: non-compensatory severe-failure flag | Interpretable ex ante, but 2 versus 3 lacks a unique ancestry-based choice |
| Comparative reversal | severe if `D_rel >= 0.10` | severe if `D_rel >= 0.20` | Candidate common-support loss is at least 10%/20% worse than its preregistered comparator | Material deterioration, not a point estimate merely crossing zero | AG2 / SR1 comparative guardrail | comparative-effect theory; numerical percentage is design convention | below: ordinary adverse/small sign variation, not severe; above: SF1 only if denominator is valid | Relative materiality is coherent, but neither rule is fully justified until an absolute-deterioration companion and denominator-quality rule are frozen |
| Common-support retention | severe if `C_ret < 0.70` | severe if `C_ret < 0.50` | Common attribution sample retains less than 70%/50% of the smaller native support | Evidence is too narrow to attribute differences broadly between specifications | comparable-support evidence state / AG2 support guardrail; not model admissibility | CS2 theory; numerical value is design convention | below: `INSUFFICIENT COMPARABLE SUPPORT`; above: comparable-support evidence available, subject to other rules | Semantic distinction is justifiable; exact retention value is conventional and cannot imply model invalidity |
| Permitted OF4 severe failures | `0` for `DOMINANT / ADVANCES` | up to `1` may retain `NON-DOMINATED / BOTH SURVIVE`, never dominant | Conservative requires no severe annual failure; permissive tolerates one of four only for survival | Dominance requires broad temporal robustness; one adverse year can preserve uncertainty but not dominance | AG2 / SR1 temporal guardrail | frozen OF4 robustness objective and calendar ancestry; count choice is design convention | conservative: first severe fold blocks dominance; permissive: first blocks dominance but may preserve survival; second exceeds allowance | Zero/one roles have coherent ex-ante semantics, though the exact survival consequence still requires complete disposition mapping |

## Common-support boundary

`INSUFFICIENT COMPARABLE SUPPORT != FAILS MODEL ADMISSIBILITY`.

Insufficient common support weakens or prevents attribution of observed differences to competing specifications. It does not automatically establish that either model is structurally invalid. Candidate-native coverage and deployability remain separately reported under CS2. Only a candidate's independent failure of its own frozen minimum-support or structural contract can produce `FAILS MODEL ADMISSIBILITY`.

## OF4 severe-failure semantics

| Severe failures across 2020–2023 | Ex-ante interpretation |
|---:|---|
| `0` | Compatible with a dominance claim if every other SR1 dimension clears its rule; does not itself prove dominance |
| `1` | Evidence of material temporal fragility; may support `NON-DOMINATED / BOTH SURVIVE` or `INSUFFICIENT DIFFERENTIATION`, but cannot support `DOMINANT / ADVANCES` under the permissive bundle |
| `2+` | Half or more of the annual outer evidence contains severe failure; incompatible with the frozen temporal-robustness objective for advancement under either current bundle |

Two or more severe failures should therefore preclude advancement, subject to a later exact mapping between `NO CANDIDATE ADVANCES` and candidate-specific non-advancement. Favorable folds cannot compensate for them.

## Specific audit findings

- **Scale quality:** the relative PIT cross-pair reference is candidate-neutral and is not an epsilon in disguise. However, reference-cohort eligibility, undefined-reference behavior, and why 5% or 10% represents meaningful identifiability remain unresolved.
- **Comparative reversal:** 10%/20% prevents a trivial sign crossing from being called severe, but relative deterioration can be unstable on a negligible comparator loss. The already-noted absolute-deterioration companion condition is necessary before either bundle is executable.
- **Absolute adequacy:** SF0 is interpretable as typical directional error measured in MAD scale units and is distinct from relative SR1 ranking. It remains a use-adequacy AG2 guardrail, not an automatic SR0 failure.
- **Support:** C-retention governs attribution evidence, not structural model validity. No excluded observation is recoded.
- **Multiplicity/search:** the two bundles remain indivisible proposals; no component mixing or third bundle is introduced.

## Recommendation

**NEITHER JUSTIFIABLE AS CURRENTLY SPECIFIED.**

Both bundles have coherent strictness direction, but a full ex-ante selection is not currently defensible because:

1. SQ05/SQ10 and MS80/MS90 are design conventions without a frozen identification-tolerance rationale;
2. SF1 lacks the required absolute-deterioration companion and denominator-quality rule;
3. SF2-50/SF2-70 correctly describe attribution strength but do not have a frozen claim-scope rationale connecting retention to permitted conclusions;
4. the exact disposition consequence for one versus two severe folds is incomplete outside the dominance restriction.

This recommendation does not authorize changing either value, creating another bundle, or inspecting empirical survival. The next researcher action is to supply or approve purely ex-ante semantic rationales and complete the missing rule definitions, or decline both bundles and explicitly reopen the threshold design.

This audit is preserved as the ancestry for the revised Hard Failure Rules & Continuous Evidence Semantics proposal and Threshold Registry.

`G4-04A1c THRESHOLD JUSTIFICATION AUDIT ACCEPTED`
