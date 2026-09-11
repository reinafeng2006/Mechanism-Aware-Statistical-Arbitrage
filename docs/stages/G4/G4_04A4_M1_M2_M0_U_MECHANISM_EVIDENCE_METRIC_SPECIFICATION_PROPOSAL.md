# G4-04A4 M1/M2/M0/U Mechanism-Evidence Architecture Freeze

Status: **G4-04A4 APPROVED / FROZEN — 2026-09-11**
Boundary: pre-empirical mechanism-evidence metric design only. No frozen-data inspection, evidence computation, classifier, belief model, target construction, or outcome access.

## Objective

Prespecify how PIT evidence may be represented and evaluated for M1, M2, M0, and U after a frozen A3 abnormality state exists. The system remains a sequential belief-updating architecture, not a mandatory mechanism classifier.

`measurement != evidence != mechanism belief != probability != label != trade decision`.

## Common evidence contract

Every mechanism-evidence measurement must preserve:

- construct and evidence role: discriminator, sequential update, rejection/rival, or supporting diagnostic;
- mechanism(s) affected and theoretically justified direction of effect;
- observation/public/available/compute/decision times;
- source, transformation, candidate, eligibility, and rule versions;
- contemporaneous-input versus later outcome status;
- competing interpretations and contamination risks;
- scale/uncertainty/quality state;
- common/native support and production-feasibility status.

No variable becomes evidence solely from its identity. The same observable may have different roles at different decision times only when its PIT lineage establishes genuinely new information.

### Common evidence-record schema

| Field | Required semantics |
|---|---|
| `evidence_record_id` / version | stable append-only identity and schema/rule version |
| `evidence_construct` | economic/statistical construct the measurement is permitted to inform |
| `mechanism_affected` | one or more of M0/M1/M2/U; M3 prohibited |
| `evidentiary_direction` | `SUPPORT`, `OPPOSE`, or `AMBIGUOUS`; not a probability or label |
| `observation_time` | time of the underlying phenomenon/record |
| `available_time` | earliest legitimate PIT use time |
| `decision_time` | information-set origin receiving this record |
| `evidence_role` | trigger-context, discriminator, sequential update, rejection/rival, or supporting diagnostic |
| `use_class` | event-time input, newly arriving sequential update, rejection, or outcome-only validation |
| `source_provenance` | source, vintage, upstream IDs, transformation/version, and availability lineage |
| `uncertainty_quality_state` | measurement, relationship, scale, data, timestamp, and provenance quality where applicable |
| `rival_explanation` | named competing interpretation(s) and whether evaluated/unavailable |
| `contamination_state` | mechanism-specific contamination audit and unresolved risks |
| `authorization_status` | permitted role, candidate status, production feasibility, and prohibition state |

Evidence records do not sum to one and need not be mutually exclusive. One record may affect multiple mechanisms in different directions only when each effect has explicit theoretical ancestry and role metadata.

## M1 evidence estimand

Evaluate whether a candidate measurement faithfully expresses insufficient peer movement in its expected signed direction while preserving that a response gap is not M1 identification.

Evidence channels must remain separate:

- Expected Signed Response;
- Observed Response;
- signed-oriented Response Gap;
- Response Uncertainty;
- additional M1 discriminator/rival evidence.

UR0/UR1/UR2 remain competing measurement specifications. The M1-oriented transformation occurs here, not in A3. Near-zero or unreliable expected direction remains unoriented or eligible for U. Normal-relationship conditioning cannot be repeated silently in UR2.

`response gap / under-response magnitude != M1 identification`.

Signed under-response morphology is a measurement derived from A3 and the frozen UR architecture. It becomes M1-specific evidence only with the relevant source/link/timing context and explicit rival channels, including peer own-news, relationship break, common or continuing shock, liquidity/pressure explanations, stale linkage, and market/industry context. Missing rival information is recorded as insufficiency, not treated as rival absence.

## M2 evidence estimand

Evaluate whether candidate evidence increases or decreases support for temporary liquidity/order-flow pressure rather than information-driven repricing or another rival, while preserving that excess move is not temporary pressure.

Retain separately:

- oriented excess move;
- pressure-source evidence;
- liquidity/flow-state evidence;
- abnormal price/flow response;
- mandatory proxy-contamination audit;
- rival information evidence;
- uncertainty and evidence-quality state;
- later reversal/normalization as outcome-only validation.

MP0 remains an excess-move diagnostic baseline, not M2 identification. MP0–MP3 remain a complexity/information-requirement ladder, not an evidence-strength ranking.

`excess move != temporary pressure`.

`volume / turnover / flow proxy != exogenous pressure`.

Every future M2 proxy record must include contamination metadata for:

- mechanical return content;
- cause/proxy overlap;
- endogeneity;
- overlapping measurement/response windows;
- future/outcome leakage;
- ambiguity of the underlying flow motive.

An unresolved mandatory contamination dimension limits the permitted M2 claim. MP3 remains research-only/difficult under its frozen status and cannot become a production shortcut.

## M0 evidence estimand

Evaluate positive evidence weakening or invalidating the temporary-arbitrage interpretation through distinct channels:

- pair/relationship rejection;
- event/mechanism rejection;
- structural-linkage change;
- persistent-versus-temporary evidence available at the decision time;
- data/information quality and ambiguity evidence.

M0 requires positive structural, fundamental, or relationship-invalidating evidence. R0–R3 remain candidate families; R3 normally supports U rather than M0. Absence of M1/M2 evidence is not M0.

Valid positive channels remain relationship break/change, fundamental or company-specific event evidence, structural exposure/linkage change, and another independently positive non-temporary explanation already authorized by ancestry.

`absence of M1/M2 evidence != M0`.

`U != M0`.

C04/C05 limitations and other data-quality states propagate into M0 evidence availability. Missing authoritative evidence creates an unavailable/unresolved evidence state; it cannot fabricate company-event, structural, or relationship-rejection evidence.

## U evidence estimand

Represent the extent and source of insufficiently resolved mechanism belief under the current PIT information set without forcing a probability simplex or action.

Preserve overlapping sources:

- measurement uncertainty;
- information insufficiency;
- mechanism ambiguity;
- evidence conflict;
- data/provenance uncertainty.

U0–U4 remain candidate representation families. U is dynamic and may update only with genuinely new PIT information. `U != M0`, `U != M3`, `Abstain != U`, and `No Trade != U`.

The five U dimensions may overlap and are not scores or exclusive labels. U is an epistemic state, not an economic mechanism or a residual numeric bucket.

`unexplained live abnormality -> U, not M3`.

No architecture requires M0/M1/M2/U quantities to sum to one.

## M3 production prohibition

G2-09 remains unchanged:

- no M3 production evidence metric;
- no M3 score, probability, factor, proxy, classifier, or label;
- no residual/unexplained-abnormality-to-M3 mapping;
- M3 discovery research remains separately governed and cannot supply event-time production evidence.

## Sequential-update semantics

Evidence state is append-only and decision-time versioned:

`prior evidence-state version -> newly available PIT evidence record(s) -> new evidence-state version`.

- New evidence must have an `available_time` later than the prior state's information cutoff or otherwise represent a previously unavailable, newly legitimate record.
- Prior records and prior decision-state outputs remain immutable and queryable.
- Corrections require provenance-preserving supersession/amendment links; they do not overwrite history.
- A new state may strengthen, weaken, conflict with, or leave unchanged M0/M1/M2/U-relevant evidence without forcing a label.
- `repeated computation of unchanged information != new evidence`.
- Future catch-up, reversal, normalization, persistence, realized fundamentals, and PnL remain outcome-only relative to the originating decision and cannot enter event-time mechanism evidence.

## Competition and coexistence

Simultaneous support and opposition across mechanisms is permitted. M1 and M2 evidence are not arithmetic opposites, and weakening one does not mechanically strengthen the other. M0 requires its own positive evidence. Conflicting or incomplete records may preserve or increase U rather than forcing resolution.

## Proposed metric dimensions

For each authorized mechanism candidate, retain a multidimensional evaluation vector:

- construct fidelity;
- incremental discriminator/rejection information on comparable support;
- calibration/uncertainty quality where applicable;
- rival sensitivity and proxy contamination;
- temporal consistency, dispersion, and independently justified severe failure;
- native coverage/deployability and production feasibility;
- outcome-leakage compliance.

No weighted mechanism-evidence score or universal cross-mechanism metric is proposed.

## SR0 / SR1 boundary

SR0 may include prohibited look-ahead, invalid PIT lineage, failure of the candidate's frozen construct, missing mandatory contamination/rival channel, mathematically unsupported output, or violation of eligibility/production authorization.

Weak evidence, adverse comparative evidence, ambiguity, conflict, poor calibration, or temporal inconsistency belongs to SR1/U unless an independently frozen use-validity rule establishes otherwise. No mechanism label is forced.

## Multiplicity and comparison families

- M1 UR candidates form an M1 measurement family downstream of an admissible relationship/abnormality state.
- M2 MP candidates form a distinct M2 family with mandatory contamination and rival reporting.
- M0 R candidates form a rejection family.
- U representation candidates form an uncertainty family.
- M3 has no production family and remains blocked.

Families may share inputs but cannot be pooled into one all-mechanism tournament. Upstream failure restricts downstream testing. Supporting components are not extra opportunities to select favorable evidence.

## Unresolved decisions

1. exact formulas and transformations for UR0–UR2, MP0–MP3, R0–R3, and U0–U4;
2. source/link/timing and rival-context measurements needed to elevate M1 morphology into evidence;
3. M2 pressure proxies, exogeneity evidence, and contamination evaluation implementation;
4. M0 event/relationship/structural evidence sources and positive-evidence measurements;
5. U representation, uncertainty/conflict metrics, and evidence-maturity states without forced probabilities;
6. precise construct-fidelity and incremental-evidence comparison estimands;
7. common/native-support aggregation and equal-pair influence;
8. semiannual inner and OF4 temporal evidence aggregation;
9. independently justified severe-failure meanings;
10. within-family multiplicity and claim roles;
11. sequential evidence-state storage/version implementation;
12. relationship to later resolution targets while preserving outcome quarantine.

No M1/M2/M0/U formula, factor, proxy, weight, probability, belief-update model, threshold, classifier, winner, or computation is authorized here.

`G4-04A4 APPROVED / FROZEN`
