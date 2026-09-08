# C06 Approximation Gaps

Status: **CONTROLLED LIMITATIONS — NO SILENT WEAKENING OF PIT**

| Alternative | Permitted construction | Approximation gap | Bias/risk retained | Use boundary |
|---|---|---|---|---|
| A. Direct official snapshot path | Use each CSRC/CAPCO full-market result only after publication | Classification updates are discrete and delayed relative to business change | Stale membership; delayed entry/reclassification | Preferred qualified path |
| B. Versioned dated-snapshot reconstruction | Difference successive immutable official snapshots and create known-state intervals | Does not reveal the exact underlying economic-change date | Interval censoring; publication timing dominates | Permitted derived reconstruction |
| C. Conservative availability reconstruction | If only publication date exists, use from next decision clock; carry last known state until next release | Intraday availability and unpublished changes remain unknown | Extra conservatism and stale intervals | Permitted; staleness must be observable |
| D. Restricted research start | Begin no earlier than first defensibly available complete official snapshot (currently 2013-01-07 under inspected archive) | Excludes earlier market history | Shorter history; potential regime coverage loss | Permitted scope candidate; researcher must approve actual start |
| E. Licensed historical classification | Use only after schema/vintage/source transformation audit | Vendor may have retroactively harmonized classifications | Hidden look-ahead/version loss | Fallback candidate only |
| F. Index constituent history | Define a separate index-based universe if explicitly amended | Omits non-index machinery firms and changes universe semantics | Selection/liquidity/index methodology bias | Not a substitute without scope amendment |

Explicitly prohibited: using current constituents retrospectively; assigning quarter/half-year membership from period start when the result was published later; treating a taxonomy crosswalk as exact when categories changed; filling archive gaps from an aggregator without visible source/version lineage.
