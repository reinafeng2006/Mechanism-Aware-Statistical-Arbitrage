# G3B Core Dataset Freeze V1

Decision: **APPROVED / FROZEN — 2026-09-10**

Freeze ID: `CORE-DATASET-FREEZE-V1`

Qualified-state Git commit: `2abf9e3e1c82b90f8af8614062b73fb6939774c2`

Freeze-execution Git commit: `64f4bdc5ab0058e7adc8209be0c9923ac8487fd8`

Freeze timestamp: `2026-09-10T04:00:11Z`

The researcher approved structural freeze of the exact G3B-F2-qualified core. The machine-readable authority is [Core Dataset Freeze Manifest V1](../../data/manifests/CORE_DATASET_FREEZE_V1.json).

Root fingerprint: `3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616`.

The fingerprint binds the immutable acquisition manifest/journal, normalized-content manifest, structural validation, C06 reconstruction, identifier lineage, 601313 probe, and Security-Date Eligibility Sidecar. The raw acquisition manifest recursively binds individual raw payload hashes and retains failed and duplicate request lineage.

## Frozen semantics

`Core Dataset Structural Freeze ≠ Candidate Measurement Authorization`

`raw observation exists ≠ observation eligible for every measurement`

- sidecar rows: **1,575,837**;
- `NORMAL TRADING OBSERVED`: **1,526,269**;
- `UNKNOWN MISSINGNESS`: **49,568**;
- C04: `CORPORATE_ACTION STATUS UNRESOLVED`;
- sidecar SHA-256: `A4418E69EDAF92CE0A16DCE72FD6551DA245CF182252528CCB5224768EA9705A`.

Dataset freeze cannot clear, recode, or regenerate these states under changed rules. Candidate computation remains prohibited until its separately frozen eligibility rule is applied. Neither Tushare/Sina adjustment factors nor missing observations acquire a stronger status through freeze.

## Bound scope and limitations

The primary PIT machinery universe uses industry 34/35, official classification snapshots available at each decision time, C01 identity/listing lineage, and the date range 2013-01-07–2025-12-31. C03 is raw/unadjusted. E02 and E03-A retain their documented provider/PIT-vintage limitations. C04/C05 authoritative coverage remains incomplete. E03-B remains excluded and blocks only dependent competing specifications.

`601313.SH → 601360.SH` remains identifier/security lineage only. It neither establishes economic relationship continuity nor authorizes automatic price-series splicing.

## Mutation policy

This version is immutable. Any correction, companion acquisition, identifier amendment, C04/C05 improvement, or source revision creates a new dataset version or explicit amendment with ancestry to this freeze. No later artifact may silently rewrite V1.

G3B is complete/frozen. G4 is initialized for protocol design only; no statistical computation is authorized.
