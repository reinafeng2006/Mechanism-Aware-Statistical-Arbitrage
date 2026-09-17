"""Metadata-only validation of the checkpointed R4-2025 execution engine."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1")
REPO = Path(__file__).resolve().parents[1]
ACCESS_SHA = "E7D129135BF189655A5279301069FEA002344FA249F54A59D117C816E6831714"


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


source = (REPO / "tools/v1_phase1_inner_r4.py").read_text(encoding="utf-8")
for token in (
    "max_workers=workers,max_tasks_per_child=64",
    "starts=starts[:smoke_blocks] if smoke_blocks else starts",
    "valid_engineering_checkpoint",
    "await_block_futures",
    "np.lib.format.open_memmap",
    "ENGINEERING_PARTIAL_NOT_SCIENTIFIC_OUTPUT",
):
    if token not in source:
        raise RuntimeError(f"missing checkpoint-engine binding: {token}")

engineering = ROOT / "rt3_state/V1-R4-63D/_engineering/2025"
markers = sorted(engineering.glob("202501-block-*.complete.json"))
if len(markers) < 3:
    raise RuntimeError("bounded real-path proof has fewer than three blocks")
for marker in markers:
    meta = json.loads(marker.read_text(encoding="utf-8"))
    payload = marker.with_name(marker.name.replace(".complete.json", ".npy"))
    if not payload.is_file() or sha(payload) != meta.get("sha256"):
        raise RuntimeError(f"engineering checkpoint hash failed: {marker.name}")
    if meta.get("status") != "ENGINEERING_PARTIAL_NOT_SCIENTIFIC_OUTPUT" or meta.get("kind") != "R4_FIT_BLOCK":
        raise RuntimeError(f"engineering checkpoint role failed: {marker.name}")

final = ROOT / "rt3_state/V1-R4-63D/2025.npy"
if final.exists() or final.with_suffix(".complete.json").exists():
    raise RuntimeError("bounded proof unexpectedly finalized R4-2025")
if list((ROOT / "rt3_state/V1-R4-63D").rglob("*.tmp*")):
    raise RuntimeError("temporary R4 artifact remains")
if sha(ROOT / "_control/heldout_access_event.json") != ACCESS_SHA:
    raise RuntimeError("held-out access event changed")

print(f"PASS: checkpointed R4 engine; real blocks={len(markers)}; hashes=PASS; R4-2025 final=MISSING; access event=UNCHANGED; values disclosed=false.")
