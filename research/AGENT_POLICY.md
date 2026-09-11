# Research Execution Agent Policy

Policy version: `REA-POLICY-1.0`
Initialized: 2026-09-11
Mode: **BOUNDED / RESEARCHER-GATED**

## 1. Purpose

The agent reduces mechanical coordination while preserving scientific governance. Autonomy applies to execution already authorized by a frozen decision and the active action contract; it does not apply to research judgment, empirical reveal, or stage advancement.

## 2. Sources of authority

Authority is evaluated in this order:

1. repository-wide `AGENTS.md` and this policy;
2. canonical governance and approved/frozen decision records;
3. the verified dataset freeze and temporal-access contracts;
4. exactly one `AUTHORIZED` action in `NEXT_ACTION.json`;
5. mechanical implementation details that do not alter any item above.

A lower source cannot relax a higher source. Text labelled proposed, candidate, suggested, future, unresolved, awaiting review, or not computation-authorized grants no execution authority.

## 3. Action-contract requirements

An executable action must state: stable action ID/version, status `AUTHORIZED`, objective, included paths/artifacts, excluded work, prerequisite frozen decisions, input dataset/version, whether data/result access is permitted, held-out permission, validation commands, commit permission, push permission and destination, completion condition, and mandatory stop conditions.

Ambiguous or internally inconsistent actions resolve to STOP. Authorization cannot be inferred by analogy. Materially broader work requires a new researcher-approved action version.

## 4. Permitted autonomous mechanics

Within a valid action, the orchestrator may read authorized context; implement exact frozen equations/rules; create deterministic code, tests, schemas, manifests, and documentation; run non-empirical structural QA; repair engineering/documentation defects without semantic change; update state/logs; and commit/push only as explicitly allowed.

Mechanical repair becomes a research decision if it changes sample membership, eligibility, equation meaning, estimator behavior, feature definition, timing, target, metric, threshold, aggregation, or interpretation. In that case stop.

## 5. Empirical and held-out controls

- Default empirical access: `DENIED`.
- Default fitting/computation: `DENIED`.
- Default outcome access: `DENIED`.
- Default held-out access: `SEALED / DENIED`.
- Development access requires an action naming the frozen protocol, permitted region, output visibility, and contamination handling.
- Held-out access always requires separate irreversible researcher authorization and access logging.
- A command likely to print empirical values is inspection and requires permission even if nominally a validator.

## 6. Dataset and PIT controls

Verify `CORE-DATASET-FREEZE-V1` with its canonical validator before any downstream action. Never overwrite upstream raw, sidecar, manifest, or frozen decision artifacts. New data or corrections create an explicit descendant dataset/enhancement version. Preserve observation/public/available/compute/decision/outcome times, vintages, revisions, identifier lineage, missingness, C04/C05 states, and outcome quarantine.

## 7. Single writer and parallelism

Canonical mutation requires `.git/research-agent.lock` as described in root `AGENTS.md`. Only the orchestrator may integrate. Subagents receive bounded read-only or isolated scratch assignments; their output is untrusted until the orchestrator verifies it against the action contract. No subagent may independently advance `AGENT_STATE`, alter `NEXT_ACTION`, commit, or push.

## 8. Validation minimum

Unless a stricter action adds checks, canonical documentation/control changes require:

- `literature/validators/validate_literature_os.ps1`;
- `literature/validators/validate_documentation_architecture.ps1`;
- `learning/validators/validate_learning_layer.ps1`;
- `tools/validate_core_dataset_freeze.py` using the configured project Python runtime;
- `git diff --check`;
- explicit review of staged paths and untracked files.

Validation success does not authorize a next stage. A validator failure stops the run unless repair is mechanical and inside scope.

## 9. Git and external effects

Preserve unrelated user changes. Never include credentials, environment secrets, ignored raw payloads, or unrelated untracked files. No force-push or history rewrite. Commit and push are separate permissions. Push permission must name the remote/destination and branch; an unpushed local commit does not imply permission to push it later.

Purchases, registrations, credential entry, communications, provider selection, data acquisition, and license acceptance require explicit action authority.

## 10. State and logging

`AGENT_STATE.md` is a current-state projection; `AGENT_RUN_LOG.md` is append-only history. Update both only while holding the writer lock. `NEXT_ACTION.json` contains exactly one action object; the orchestrator may mark an executed action complete only when the contract permits state mutation, but may not invent its successor. The successor defaults to `NONE` pending researcher activation.

## 11. Researcher checkpoint format

Every mandatory stop checkpoint contains:

- completed work;
- validator/fingerprint status;
- exact unresolved decision;
- bounded alternatives already permitted by governance;
- why human approval is required;
- recommended next authorized action;
- uncommitted/unpushed state.

The agent remains stopped until `NEXT_ACTION.json` is replaced by an explicitly researcher-authorized action contract.

