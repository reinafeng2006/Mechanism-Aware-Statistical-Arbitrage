# Pre-client migration canonicalization audit

2026-09-18. Migration only; no scientific decision, historical calibration, C04 repair or PnL action. Start with [current state and next action](CURRENT_PROJECT_STATE_AND_NEXT_ACTION.md).

## 1. Git baseline and classification

Fetched canonical `origin` before comparison. Branch `main`; remote `https://github.com/reinafeng2006/Mechanism-Aware-Statistical-Arbitrage.git`. At audit start HEAD=origin/main=`1359dcb7fc1876321fec00709a00ccca26d1f217`, ahead/behind 0/0. No staged files. No existing writer lock; this migration acquired an atomic owned lock and releases it after publication. One tag, `v1-final-frozen-2026-09-18`, dereferences to the same frozen commit and must remain unchanged. No reset/clean/stash/discard/amend/force-push.

Classification is **at audit start**, before the migration commit. Successful publication makes every required document/control row below ON GITHUB / CURRENT. The exact publishing commit is the commit containing this audit (`git log -1 --format=%H -- docs/stages/G5/PRE_CLIENT_MIGRATION_AUDIT.md`), avoiding an impossible self-referential embedded commit hash.

| File/group | Starting classification | Migration disposition |
|---|---|---|
| `docs/stages/G5/V1_1_COMPLETE_TRADING_STRATEGY_MATHEMATICAL_SPECIFICATION.md` | LOCAL UNTRACKED / REQUIRED | Publish unchanged; retain equation audit and conformance caveats |
| `docs/decisions/V1_1_HELD_SECURITY_POST_ENTRY_ELIGIBILITY_FREEZE.md` | LOCAL UNTRACKED / REQUIRED | Publish approved binding unchanged |
| `docs/stages/G5/TRADING_STRATEGY_ECONOMIC_REDESIGN_CHECKPOINT.md` | LOCAL UNTRACKED / REQUIRED | Publish proposals unchanged |
| `docs/stages/G5/S3_RESIDUAL_SCALE_THRESHOLD_DESIGN_CHECKPOINT.md` | LOCAL UNTRACKED / REQUIRED | Publish architecture selection and unresolved proposals unchanged |
| `GOVERNANCE.md` | LOCAL MODIFIED / NOT PUSHED | Publish existing review/pause overlay; frozen decisions remain historical |
| `research/AGENT_RUN_LOG.md` | LOCAL MODIFIED / NOT PUSHED | Append-only post-V1 authority/actions and migration audit |
| `research/AGENT_STATE.md` | LOCAL MODIFIED / NOT PUSHED | Current projection corrected for published handoff and pending S3 gate |
| `research/NEXT_ACTION.json` | LOCAL MODIFIED / NOT PUSHED | Remove obsolete active-looking historical fields; final NONE with explicit prohibitions |
| `research/G4_05_MODEL_SPECIFICATION_CONTRACT.json` | LOCAL MODIFIED / NOT PUSHED | Only mutable computation gate changed to design-review/no execution; frozen model definitions unchanged |
| `research/validate_agent_control.ps1` | LOCAL MODIFIED / NOT PUSHED | Validate review gate and bounded migration publication; no research engine changes |
| Frozen V1 policy, final snapshot, terminal registry, evidence manifests, scientific tools and historical decisions | ON GITHUB / CURRENT | Preserve; no redesign rewrite or tag change |
| Existing documentation migration map | ON GITHUB / CURRENT | Historical directory map only, not current project handoff; preserve |
| `README.md` | ON GITHUB / CURRENT but obsolete G1 entry text | Update entry status/link so a clone finds the actual current checkpoint |
| `docs/stages/G5/CURRENT_PROJECT_STATE_AND_NEXT_ACTION.md`, this audit | LOCAL UNTRACKED / REQUIRED (created by migration) | Fresh-client entry point and inventory/restoration guide |
| `research/POST_V1_RESEARCHER_AUTHORITY_LEDGER.md` | LOCAL UNTRACKED / REQUIRED (created by migration) | Persist exact approved/proposed boundary without chat dependence |
| `research/migration/EXTERNAL_ARTIFACT_INVENTORY.json` | LOCAL UNTRACKED / REQUIRED (generated metadata) | Commit portable locators, byte sizes, prior hash bindings and metadata fingerprints only |
| `tools/audit_client_migration_metadata.py` | LOCAL UNTRACKED / REQUIRED (migration utility) | Commit metadata-only inventory recipe; not a scientific runner |
| `.venv/`, `tools/__pycache__/` | ENVIRONMENT/CACHE / EXCLUDE | Preserve locally, never stage; no global ignore/reset/cleanup needed |
| Ignored `data/raw/`, `data/qa_work/` | EXTERNAL LARGE ARTIFACT / MANIFEST ONLY | Inventory metadata; payloads stay local and excluded |
| D: artifact families below | EXTERNAL LARGE ARTIFACT / MANIFEST ONLY | Inventory and reference existing manifests; do not upload payloads |
| Chat attachment copies, transient logs/cache/generated runtime paths | LOCAL ONLY / NOT REQUIRED for design | Authority transcribed canonically; no client-history dependency |

No other untracked research text/code or modified strategy/model registry was found by Git status. The four post-V1 documents are the complete starting set of untracked scientifically relevant text. The terminal V1 model registry is unchanged, not replaced by an S3 registry. Runtime generated source and receipts outside Git are listed in the inventory, not silently treated as canonical current source.

## 2. External artifacts — what a clone does not contain

Counts/bytes are filesystem metadata at audit time, **not a fresh validation of every scientific payload**. Family totals include intermediates, logs, cache and partial artifacts as well as canonical payloads. Do not infer canonical completion from a file count. The inventory is not a backup.

| Logical family | Original location | Files / bytes | Scientific role and absence consequence |
|---|---|---|---|
| `external://A1_H126` | `D:\MechanismAwareStatArbData\A1_H126` | 510 / 23,304,112,818 | Inner/OF4 H126 scale-loss partitions and 406-unit synthesis checkpoints; unavailable for exact historical reproduction without storage |
| `external://OF4` | `D:\MechanismAwareStatArbData\OF4` | 354 / 88,490,475,986 | 2020–2023 inputs, relationship/RT3/A3/A5 compressed and intermediate artifacts, metadata and generated runners |
| `external://FINAL_HELDOUT_V1` | `D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1` | 1,491 / 181,829,193,177 | Exposed 2024–2025 reduced-support relationships/RT3/A3/A5/H126/synthesis/H5 vectors; access event; 524 R4 engineering checkpoints, not completed R4 science |
| `external://C04_THROUGH_2025_V1` | `D:\MechanismAwareStatArbData\C04_THROUGH_2025_V1` | 589 / 44,255,254 | Official acquisition evidence and qualified descendants/transport; no permission for new source work or correction |
| `external://TRADING_V1_1` | `D:\MechanismAwareStatArbData\TRADING_V1_1` | 124 / 893,106,056 | Historical one-shot unit payloads, checkpoints, validation/access records; may contain private prefix accounting/results; no inspection now |
| `repo://data/raw` (ignored) | Current repository local `data/raw` | 2,937 / 600,787,915 | Provider/raw research and C04 acquisition ancestors; not supplied by clone |
| `repo://data/qa_work` (ignored) | Current repository local `data/qa_work` | 7,564 / 80,615,000,015 | Prepared/core/inner relationship/RT3/A3/A5 working artifacts and ancillary packages; not supplied by clone |

**None of these payload families is needed for the next scale/threshold design discussion.** Each would matter for later authorized artifact validation, replication or development. If the new client cannot access the machine/storage or a verified backup, these bytes are unavailable; Git hashes cannot recreate them. We did not create a backup or verify off-machine redundancy. Do not infer a copy exists elsewhere.

Other ignored patterns include `data/outcomes/`, `data/extensions/`, `data/post_2025/` and local literature-library inputs; Git status did not identify populated untracked scientific changes under them in this audit. Their mere ignore rule is not evidence of an acquired dataset. No secret/environment payload is staged.

## 3. Manifests, identity, ancestry and schema map

| Logical object | Canonical Git reference | Schema / reconstruction recipe in Git |
|---|---|---|
| Frozen core | `data/manifests/CORE_DATASET_FREEZE_V1.json` | `tools/validate_core_dataset_freeze.py`; bound sidecars and original acquisition manifests |
| Inner relationship / RT3 / A3-A5 | `V1_PHASE1_INNER_INPUT.json`, `V1_PHASE1_RELATIONSHIP_OUTPUTS.json`, `V1_RT3_RELATIONSHIP_STATE_AUGMENTATION.json`, `V1_INNER_A3_A5.json` under `data/manifests` | `tools/v1_phase1_prepare.py`, `v1_phase1_inner_relationships.py`, `v1_phase1_inner_r3.py`, `v1_phase1_inner_r4.py`, `v1_inner_a3_a5.py`; explicit NumPy field definitions and PIT versions |
| OF4 | `data/manifests/V1_OF4_RELATIONSHIP_STAGE.json`; `research/V1_OF4_EXTERNAL_STORAGE_CONTRACT.json` | `tools/v1_of4_materialize.py`; logical/physical-relative payload mapping, compression/raw and compressed hashes |
| Inner/OF4 H126 and synthesis | `data/manifests/V1_A1_H126_CANDIDATE_NEUTRAL.json`, `V1_PRE_HELD_OUT_A1_SYNTHESIS.json` | `tools/v1_a1_h126_candidate_neutral.py` structured dtype; `v1_a1_h126_synthesis_batch.py` unit/progress schema; ancestor/scale-input hash lineage |
| Reduced held-out | `research/V1_FINAL_HELDOUT_COMPLETION.json`; `data/manifests/V1_FINAL_HELDOUT_EVIDENCE_CHECKPOINT.json` | `tools/v1_final_heldout_reduced_support.py` plus referenced orchestration/schema code; canonical external manifest locations and hashes |
| R4 partial engineering | Frozen H4 disposition and inventory pointers to `_engineering/2025/*.complete.json` | `tools/v1_phase1_inner_r4.py`; block/month markers with input/ancestor hash and partial-only state; **no resume authority** |
| C04 descendants | `data/manifests/C04_A_OFFICIAL_CALENDAR_V1.json`, `C04_A_THROUGH_2025_V1.json`, `C04_A_THROUGH_2025_V2.json`, `C04_A_THROUGH_2025_FINAL_AUDIT.json` | Corresponding C04 tools/contracts; source/effective/publication/qualification lineage; no absence-as-clean inference |
| Trading V1.1 | `research/V1_FINAL_FREEZE.json`, `data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json`, `TRADING_V1_1_INPUT_QUALIFICATION.json` | `tools/v1_1_trading.py`, `v1_1_accounting.py`; frozen policy and prior unit hashes; no new PnL authority |

The committed migration inventory contains all file locators/sizes for the seven enumerated roots; 921 declared JSON metadata receipts were fingerprinted, and 5,659 recorded hash bindings exported with source JSON pointers/path context. Generated-runner Python files have separate source hashes. The utility exports hash/path metadata and schema key names, not coefficients, returns or scientific result vectors. It does not copy entire result-bearing JSON documents. It reads only declared manifest/control/progress/completion/hash-receipt documents, never scientific unit payloads or arrays.

Hash semantics: `metadata_sha256_verified_now` fingerprints the receipt itself; `recorded_hash_bindings` preserves previously recorded expected hashes and ancestry, **not newly rehashed large payloads**. The inventory does not claim a fresh 406/406 or 524-block full data validation. Missing hash bindings for caches/intermediates remain unverified, not silently promoted to canonical artifacts. Existing canonical manifests, not directory counts, decide which outputs are finalized.

## 4. Path-independent restoration, not recomputation

1. Clone canonical main, read the current handoff and NEXT_ACTION. No empirical activity is presently authorized.
2. When later authorized, map `external://` to the restored artifact root and `repo://` to the clone root. These logical locators are independent of drive letters. Original Windows roots are recorded for provenance only.
3. Restore byte-identical payloads plus manifests/markers from the existing storage or a verified backup. Preserve relative paths. Relative paths inside old manifests resolve against their manifest's declared physical root or the recorded source family; JSON pointers identify the original binding. Do not blindly concatenate a basename with the wrong root.
4. Compare restored compressed/payload SHA-256 with the appropriate recorded hash, distinguishing raw/decompressed hashes from compressed hashes. Validate ancestry, dtype/shape/eligibility versions using the canonical manifest and source schema. Never alter an old manifest hash merely because its physical root changed; use a separate relocation map.
5. Exact recipes/schema code are in Git for provenance and future authorized reconstruction. Some historical runners hard-code physical paths and generated-runner placement; **relocation is not proven turnkey**. If a script needs a path adapter, that is separate bounded engineering authority, not a reason to run or refit now.
6. If bytes or metadata cannot be recovered, mark the artifact unavailable. Do not download substitute data, recompute valid checkpoints, resume incomplete R4 or inspect private trading unit files under a migration approval. Cache/source generation is distinguishable from immutable scientific identity, but do not delete anything during this audit.

## 5. Validation and canonical reconstruction

Required checks: documentation architecture, literature, learning layer, bounded agent control, core integrity, whitespace, reviewed staging, frozen-tag equality, and post-push fetch/HEAD equality. Core root fingerprint remains `3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616` (11 bound artifacts). Policy hash remains `851EC63DB822E889F9DC103C87B63BCBAF93EA48810941731686D43CA28A9786`; held-out event hash remains `E7D129135BF189655A5279301069FEA002344FA249F54A59D117C816E6831714`.

The conceptual fresh-clone audit follows the reconstruction matrix in the handoff: objective, V1 terminal/unavailable states, redesign motivation, exact approved architecture, pending recommendations, honest exposure history, next decision and external dependencies are all explicit in canonical text. It requires no D: access and no hidden chat approval. It does not certify data sufficiency or create a new scientific result.

This migration publishes current context and preserves the gate: **S3 SCALE + THRESHOLD DESIGN / RESEARCHER DECISION REQUIRED**.
