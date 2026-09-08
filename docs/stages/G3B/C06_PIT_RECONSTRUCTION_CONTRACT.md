# C06 PIT Reconstruction Contract

Version: **v1.0-frozen**  
Status: **APPROVED / FROZEN**

## Semantic rule

For decision time `t`, use only the latest official classification snapshot whose defensible `available_time ≤ t`, joined to the security's listing/code/status history known at `t`.

The result answers **known official membership as of t**, not latent economic truth at t.

## Required immutable source record

Each source snapshot must preserve:

- `classification_source` and source URL/document ID;
- `taxonomy_id`, `taxonomy_version`, hierarchy level and code/name;
- stated classification period;
- official page publication date/time;
- conservative `available_time` and its precision;
- retrieval time, snapshot ID, original file checksum and schema/parser version;
- security code/name exactly as published;
- original row and extraction-quality flags;
- replacement/correction relation if discovered;
- licence/use metadata.

## Derived membership interval

For each source row and resolved stable security ID:

- `membership_known_from = conservative available_time of this snapshot`;
- `membership_known_to = available_time of next accepted snapshot, exclusive`;
- `classification_age = decision_time - membership_known_from`;
- `staleness_flag` records long intervals but does not invent a reclassification;
- `source_snapshot_id` and `taxonomy_version` remain visible downstream.

No snapshot may be backdated to the quarter/half-year start or fiscal period end.

## Listing, delisting and reclassification

- Membership requires a C01-resolved stable security ID and contemporaneous eligibility.
- A newly listed security is not included merely because it appears in today's classification; entry begins only when a qualifying snapshot becomes available.
- Delisting/suspension/eligibility is governed by C01/C05 and may end tradable-universe eligibility even while the last classification remains historically true.
- A changed code in a later snapshot produces a new known-state interval. Prior intervals remain immutable.
- A taxonomy change never overwrites old codes. A versioned crosswalk may be added only as a derived layer and must preserve non-equivalence/ambiguity.

## Time precision rule

If only a publication date is defensible, the snapshot becomes usable at the first project decision clock strictly after that publication date, unless a later audit establishes an exact release timestamp. This prevents same-day look-ahead.

## Target-industry mapping boundary

The acquisition layer stores official classification codes and versions. The separately versioned `registers/MACHINERY_INDUSTRY_SCOPE_MAP.md` identifies which codes count as the bounded machinery universe and surfaces ambiguous adjacent codes. It never retroactively harmonizes the raw source.

## Acceptance checks for later acquisition

- Every accepted snapshot has immutable original content and publication/availability provenance.
- Every membership row resolves to one stable C01 security ID or is quarantined as unresolved.
- Duplicate/conflicting rows are retained and reason-coded, not silently collapsed.
- Snapshot-to-snapshot additions, removals and code changes receive deterministic transition records.
- Missing publications create explicit stale intervals; they do not trigger current-membership backfill or invisible vendor substitution.
