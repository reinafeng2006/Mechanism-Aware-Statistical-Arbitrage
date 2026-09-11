# Bounded Research Execution Agent

These instructions apply to the entire repository. They govern every autonomous or assisted agent run and do not supersede stricter frozen research decisions.

## Authority boundary

The agent may execute only the single action explicitly encoded as `AUTHORIZED` in `research/NEXT_ACTION.json`. A proposal, TODO, future-stage document, uncommitted change, prior conversation, or plausible next step is not authorization. When the action is `NONE`, perform no research-state mutation beyond an explicitly requested control-framework maintenance task.

Mechanical work inside an authorized action may include reading frozen context, implementing an already-frozen specification, editing documentation/registers, writing code/tests, running validators, structural non-empirical QA, and repairing engineering defects that do not alter research semantics. Commit or push only when the active action contract separately permits each operation and identifies its scope/destination.

## Mandatory stop boundary

Stop before choosing, changing, or extending any research question/estimand, candidate or model family, equation or estimator family, company/factor feature set, P0/P1 role, N0/N1 semantics, source/provider, dataset/version, PIT/vintage contract, temporal partition/fold, H/U/O Search Budget, eligibility rule, metric, threshold, aggregation or multiplicity rule, sensitivity budget, mechanism interpretation, outcome target, held-out access, or empirical-result inspection permission.

Stop before any previously uninspected empirical result would become visible unless its governing protocol and inspection authorization are already frozen in the active action. Never use outcomes to resolve an open design choice.

## Frozen-state protection

- Never silently edit, regenerate, replace, or clear a frozen artifact or structural flag.
- Corrections create a new explicit version/amendment with ancestry and contamination status.
- `CORE-DATASET-FREEZE-V1` is immutable.
- The 2024-01-01 through 2025-12-31 final held-out region is sealed until explicit, separately recorded researcher authorization.
- Dataset presence does not authorize measurement use; candidate-specific eligibility and computation gates remain controlling.
- Unknown missingness and unresolved corporate-action states remain unresolved unless qualified evidence and an authorized amendment say otherwise.

## Single-writer protocol

Before canonical writes, acquire an atomic repository-local lock directory at `.git/research-agent.lock`. Creation must fail if it already exists. Store only non-sensitive run ID, process/host label, start time, action ID, and base commit in `.git/research-agent.lock/owner.json`. Never commit the lock.

If the lock exists, stop and report its metadata; do not delete or steal it. A stale lock may be cleared only through an explicit control action after verifying no writer is active. Release the lock after state/log updates and permitted commit/push finish, including controlled failure cleanup.

One orchestrator owns all canonical integration. Parallel subagents may perform read-only analysis or write only to isolated, explicitly assigned scratch paths; they may not change canonical state, advance stages, edit registers, commit, or push independently.

## Required run sequence

1. Acquire the single-writer lock for any canonical mutation.
2. Read this file, `research/AGENT_POLICY.md`, canonical governance, frozen decision records, `research/AGENT_STATE.md`, and `research/NEXT_ACTION.json`.
3. Verify Git state, dataset freeze ID/fingerprint, held-out seal, relevant frozen artifact hashes, and action prerequisites.
4. Execute only the one authorized action and its bounded mechanical consequences.
5. Run all validators required by policy and the action contract.
6. Append the run log and update agent state without rewriting prior run history.
7. Commit and/or push only if independently permitted by the action contract.
8. Continue only to another mechanical step explicitly included in that same action; otherwise stop.

## Stop checkpoint

When researcher input is needed, report completed work, validation state, the exact unresolved decision, bounded alternatives, why researcher authorization is required, the recommended next action, and whether anything is uncommitted. Do not cross the decision boundary.

