"""Integrity-only validation of the held-out RT3 resume frontier."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1")
ACCESS_SHA = "E7D129135BF189655A5279301069FEA002344FA249F54A59D117C816E6831714"
STATIC = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W"]


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def validate(candidate: str, year: str) -> None:
    payload = ROOT / "rt3_state" / candidate / f"{year}.npy"
    marker = payload.with_suffix(".complete.json")
    if not payload.is_file() or not marker.is_file():
        raise RuntimeError(f"missing finalized checkpoint {candidate}/{year}")
    meta = json.loads(marker.read_text(encoding="utf-8"))
    ancestor = ROOT / "relationships" / candidate / f"{year}.npy"
    if not (meta.get("candidate") == candidate and meta.get("partition") == year and
            meta.get("equivalence") == "PASS_EXACT" and meta.get("shared_field_mismatches") == 0 and
            sha(payload) == meta.get("sha256") and sha(ancestor) == meta.get("ancestor_sha256")):
        raise RuntimeError(f"checkpoint validation failed {candidate}/{year}")


for candidate in STATIC:
    for year in ("2024", "2025"):
        validate(candidate, year)
for year in ("2024", "2025"):
    validate("V1-R3-252M", year)
validate("V1-R4-63D", "2024")

r4_2025 = ROOT / "rt3_state/V1-R4-63D/2025.npy"
r4_2025_marker = ROOT / "rt3_state/V1-R4-63D/2025.complete.json"
if r4_2025.exists() or r4_2025_marker.exists() or list(r4_2025.parent.glob("2025*.tmp*")):
    raise RuntimeError("R4-2025 is not a clean missing resume frontier")
progress = json.loads((ROOT / "_control/progress.json").read_text(encoding="utf-8"))
if len(progress["completed_stages"]) != 8 or "state" in progress["completed_stages"]:
    raise RuntimeError("outer progress frontier mismatch")
if sha(ROOT / "_control/heldout_access_event.json") != ACCESS_SHA:
    raise RuntimeError("held-out access event changed")
if list((ROOT / "a3_a5").rglob("*.complete.json")) if (ROOT / "a3_a5").exists() else []:
    raise RuntimeError("downstream A3/A5 unexpectedly started")
if (ROOT / "synthesis_checkpoint_v1/progress.json").exists():
    raise RuntimeError("downstream synthesis unexpectedly started")

print("PASS: 13/14 RT3 checkpoints hash/equivalence-validate; R4-2025 is the clean next unit; downstream pending; access event unchanged; values disclosed=false.")
