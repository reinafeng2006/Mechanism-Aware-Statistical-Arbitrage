# V1 A1 H126 External Synthesis Execution Checkpoint

Status: **1/406 CHECKPOINTED / READY FOR EXTERNAL SYNTHESIS RESUME — 2026-09-16**

The candidate-neutral H126 scale/loss layer is complete and independently revalidated: 98/98 partitions, 823,205,593 paired-direction physical records, zero temporary materialization files, and no held-out access. The immutable relationship, RT3, A3/A5, and OF4 ancestors revalidated without scientific-result inspection.

## Interrupted-session recovery

The prior interactive process unexpectedly completed an atomic but unpublished synthesis JSON after the UI session was believed interrupted. It was not adopted, interpreted, or committed. Its SHA-256 is `61B9F64846377881E11A65162AC780BA8A33656C3E63544167CA5E6D2D90D480`; it was moved intact to the external `_interrupted_unpublished` quarantine. The canonical synthesis path is absent and must be produced only by the checkpointable runner.

## Exact batch architecture

The runner contains 406 independently finalized units:

- 14 temporal-fold exact-common-support indexes;
- 98 candidate × fold common/native summaries;
- 294 candidate-comparison × fold paired-loss summaries.

Each unit is atomically finalized, SHA-256 bound in a progress manifest, and verified before resume. A valid completed unit is skipped and never recomputed. Common support uses exact key intersection across all seven candidates. Within-direction observation losses are reduced by exact median within pair; pair summaries receive equal influence through an exact median. Inner and OF4 temporal roles remain separate and use exact median-vector temporal aggregation. No approximate quantile, sampling, support weighting, scalar score, uncertainty default, multiplicity default, severe-failure invention, or forced ranking is present.

## Bounded runtime benchmark

The fixed-prefix, no-value structural benchmark read 700,000 rows in 2.80 seconds. The layer contains 23,146,110,249 compressed bytes; the largest decompressed unit input is 1,094,594,192 bytes and the two largest together are 2,189,188,384 bytes. The prior exact monolithic calculation's process-to-atomic-finalize elapsed time was approximately two hours; checkpointing adds repeated bounded I/O.

Conservative operational projection:

- units: 406;
- typical unit: approximately 18–35 seconds, with the largest OF4 units potentially 1–3 minutes;
- total: approximately 2–4 hours on the measured host;
- peak RAM: approximately 2.5–4.0 GiB;
- peak temporary storage: less than 0.5 GiB, plus 23.15 GB of already-finalized immutable H126 inputs;
- deterministic logs/progress: `D:\MechanismAwareStatArbData\A1_H126\synthesis_checkpoint_v1`.

The benchmark retained no scientific statistic, exposed no result value, and accessed no 2024–2025 data.

## Researcher-operated boundary

Codex must not start the long runner. The researcher may start it in an independent PowerShell terminal. `status`, `run`, `resume`, and `validate` are supported. Completion does not authorize 2024–2025 access and returns the project to `PRE-HELD-OUT V1 GATE / RESEARCHER DECISION REQUIRED`.

Atomic-write smoke validation completed the exact `support__inner__2015H1` unit under the frozen calculation. Its finalized SHA-256 is `FBABD47A7ED54AD98B79C130980BFAE6553A94D7921C66689EB9BDA230EFC31E`; lossless reload, atomic rename, manifest registration, and no-temp checks passed. A bounded `resume --through-unit support__inner__2015H1` preserved both hash and timestamp, proving that a valid completed unit is skipped. Progress is legitimately `1/406` and must be continued with `resume`, not `run`.

`1/406 CHECKPOINTED / READY FOR EXTERNAL SYNTHESIS RESUME`
