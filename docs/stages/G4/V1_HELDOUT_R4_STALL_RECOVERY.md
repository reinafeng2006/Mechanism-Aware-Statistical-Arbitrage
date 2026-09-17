# V1 Held-Out R4 Stall Recovery

Status: `ENGINEERING REPAIR VALIDATED / RESUME FRONTIER R4-2025`

The researcher-operated held-out run completed and checksum-finalized 13 of 14 RT3 candidate-year companions. `V1-R4-63D/2024` is immutable, hash-valid, exactly equivalent to its relationship ancestor, and has zero shared-field mismatches. R4-2025 has no payload, marker or temporary file. No A3/A5, compression, H126 or synthesis unit started.

## Bounded diagnosis

- The eight R4 workers exited while the coordinator remained blocked inside the synchronous `pool.map` collection path. The coordinator showed no CPU, memory or file progress after the pool disappeared.
- The wrapper could not write the complete traceback until its nested subprocess returned. After controlled termination it recorded exit code `-1`; the traceback itself was truncated at termination and contains no recoverable child exit codes.
- The only preceding stderr comprises SciPy finite-difference `RuntimeWarning` messages. The frozen `fit_one` implementation already converts non-finite/unsuccessful optimization states into its existing unavailable result; these warnings do not identify the pool-loss cause.
- No incomplete R4-2025 artifact was created. Observed worker working sets before loss were small relative to the coordinator, and no accessible resource-exhaustion event established an out-of-memory cause. Resource exhaustion is therefore unconfirmed.
- Each task serializes a bounded `256 × 63 × 2` numerical batch. Windows spawning is protected by the module's `__main__` guard. Neither structure reveals a serialization recursion or import-side scientific execution defect.
- The prior synchronous `pool.map` path had no timeout or explicit child-liveness audit. Abrupt child loss could therefore leave the coordinator waiting without a finalized unit or actionable failure record.

## Semantics-preserving repair

Static, R3 and R4 RT3 generators now treat an existing checkpoint as complete only when payload and marker both exist and payload hash, ancestor hash, candidate, partition, exact-equivalence state and zero shared-field mismatches all validate. Valid checkpoints are skipped; partial or mismatched checkpoints fail closed.

R4 pool work now uses ordered futures with the identical task batches and result order. It adds only bounded waiting, child exit-code/liveness inspection, cancellation of pending futures after failure, and an explicit contextual exception. Equations, optimizer, Q/R semantics, initialization, monthly refresh, PIT inputs, state updates, convergence rules, pair universe and numerical outputs are unchanged.

The held-out access-event SHA-256 remains `E7D129135BF189655A5279301069FEA002344FA249F54A59D117C816E6831714`.

Resume must hash-verify and skip all 13 valid checkpoints and execute R4-2025 as the next scientific unit. Long execution remains researcher-operated.
