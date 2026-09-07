# G3A Coverage, Frequency & Latency Map

Status: **APPROVED / COMPLETE — FEASIBILITY ONLY**

| Clock envelope | Attainable source classes | Coverage / latency finding | Constrained candidates |
|---|---|---|---|
| Relationship-history-capable | EOD authorized market history; company/industry databases | Broad A-share history plausible; entrants, exits, suspensions and identifiers need audit; generally cacheable | P0/RR/N0/N1/R0 |
| Ordered-market-response-capable | Common-clock bars; licensed minute/tick/L2 | Coarse ordering plausible; fine causal ordering not universal and adds burden | P0-SIGN, RR-SIGNED, A-SIGN/A-TIME, UR, MP0 |
| Event-publication-capable | CNINFO/exchanges; licensed event databases/APIs | Public documents plausible; structured event/link coverage uneven; use only after verified availability | P1, UR2, MP2, R1/R2 |
| High-resolution-specialized | Exchange-authorized L2/tick; licensed research databases | Partial technical availability; broad signed-flow history not established; high cost/storage/compute | MP3; optional MP1/A-TIME |
| Outcome-separation-capable | Versioned internal store built later | Feasible if IDs/vintages precede acquisition; outcomes unavailable to prior states | All validation, M3-DISC |

No exact sampling frequency or latency tolerance is selected.
