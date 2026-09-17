# V1 Held-Out R4-2025 Recurrent Resource Failure

Status: `ROOT CAUSE REPAIRED / CHECKPOINTED RESUME READY`

## Primary root cause

The recurrent loss was Windows commit-pressure failure in an unbounded multiprocessing execution shape. The R4 coordinator retained the growing full-year RT3 record list and all submitted fit inputs/results while eight workers loaded NumPy/SciPy native runtimes without explicit BLAS/OpenMP thread limits. Both temporary storage and the system-managed pagefile were C:-backed. Windows recorded event 26, `Virtual Memory Minimum Too Low`, during the failure interval, and the second stranded coordinator retained approximately 3.26 GB RSS after all workers disappeared.

## Contributing factors

- The year was the only durable R4 state unit, so completed monthly and pair-block work was lost on failure.
- Eager submission retained every monthly pair-block argument and future until the full fit batch returned.
- Eight workers multiplied native-runtime commit demand; nested native thread counts were unconstrained.
- C: had recently been near 10.8 GB free, while D: retained more than 600 GB. Pagefile growth and default TEMP/TMP therefore competed on the constrained volume.
- The original synchronous collection path could wait indefinitely after abrupt worker loss. The first repair improved propagation but did not bound parent retention or native-library resource demand.

## Evidence and alternatives ruled out

- Relationship 14/14, static RT3 10/10, R3 RT3 2/2 and R4-2024 remain finalized and hash-valid. R4-2025 has no canonical payload, marker or stale temporary payload.
- Both failures occurred only during the coarse R4-2025 state unit. No downstream A3/A5, compression, H126 or synthesis stage began.
- No Python traceback, Application Error crash event, access-violation record, path-length failure, permission failure or D:-disk-full condition was found. Child exit codes were unrecoverable after both pools disappeared.
- Windows spawn guards were present. Task arguments were picklable and the repaired bounded real-task test completed through the identical SciPy optimizer path.
- The old logs did not record month/block identifiers, so a unique repeated optimizer call cannot be established. The repair therefore eliminates the complete smallest plausible set: commit pressure, eager queue retention, nested native parallelism, C:-temporary pressure and coarse restart granularity.

Confidence in resource/commit exhaustion as the primary mechanism is `HIGH`. Confidence in any single numerical task as a trigger is `LOW / NOT ESTABLISHED`.

## Semantics-preserving repair

- R4 state work is decomposed deterministically as year → month → ordered 256-pair blocks.
- Four spawned workers are used, with at most four fit blocks in flight. Workers are recycled after 64 tasks.
- BLAS/OpenMP/NumExpr/BLIS and Numba thread counts are fixed to one per process.
- Each fit block and completed month uses temporary-write, fsync, checksum and atomic finalize under the authorized D: root. Resume verifies hashes and structural lineage before skipping.
- Monthly state construction preserves pair order, exact optimizer calls, frozen monthly reinitialization, within-month state updates and field-by-field equivalence against the immutable relationship ancestor.
- Final annual assembly streams ordered monthly payloads into a temporary memory map and atomically finalizes only after every month validates.
- Abnormal worker exits, broken pools and timeouts propagate as explicit contextual failures. Valid earlier blocks remain reusable.
- TEMP, TMP, Numba cache and all new R4 engineering checkpoints are routed to `D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1`.

`SCIENTIFIC SEMANTICS IMPACT = NONE`. Equations, Q/R, PIT inputs, H63 geometry, optimizer objective/options, initialization, convergence/boundary handling, pair universe, eligibility, output fields and held-out scope are unchanged.

## Bounded proof

The actual held-out R4-2025 path completed multiple frozen pair blocks using the repaired worker architecture. Every block was checksum-valid and marked `ENGINEERING_PARTIAL_NOT_SCIENTIFIC_OUTPUT`. Repeating the identical bounded command hash-verified and skipped those blocks, created no final R4-2025 artifact, left no temporary file and disclosed no scientific value.
