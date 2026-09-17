"""Structural and checksum validator for the finalized pre-held-out H126 checkpoint.

This validator deliberately prints no scientific values and never recomputes a unit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = Path(r"D:\MechanismAwareStatArbData\A1_H126\synthesis_checkpoint_v1")
PROGRESS = WORK / "progress.json"
FINAL = ROOT / "data/manifests/V1_PRE_HELD_OUT_A1_SYNTHESIS.json"
LAYER = ROOT / "data/manifests/V1_A1_H126_CANDIDATE_NEUTRAL.json"
CANDIDATES = {
    "V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W",
    "V1-R1MI-126W", "V1-R3-252M", "V1-R4-63D",
}
FOLDS = {*(f"{year}H{half}" for year in range(2015, 2020) for half in (1, 2)),
         *(str(year) for year in range(2020, 2024))}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


progress = json.loads(PROGRESS.read_text(encoding="utf-8"))
require(progress["state"] == "COMPLETE", "checkpoint state is not COMPLETE")
require(progress["unit_count"] == 406 and progress["completed"] == 406, "checkpoint is not 406/406")
require(progress["held_out_accessed"] is False, "progress records held-out access")
require(progress["scientific_values_exposed"] is False, "progress manifest exposes scientific values")
require(len(progress["units"]) == 406, "progress unit registry does not contain 406 entries")
for unit_id, record in progress["units"].items():
    path = Path(record["path"])
    require(path.is_file(), f"missing finalized unit: {unit_id}")
    require(path.stat().st_size == record["bytes"], f"unit byte-size mismatch: {unit_id}")
    require(sha256(path) == record["sha256"], f"unit checksum mismatch: {unit_id}")

require(FINAL.is_file() and sha256(FINAL) == progress["final_sha256"], "final synthesis checksum mismatch")
require(LAYER.is_file() and sha256(LAYER) == progress["layer_manifest_sha256"], "H126 layer lineage mismatch")
final = json.loads(FINAL.read_text(encoding="utf-8"))
require(final["status"] == "CORRECTED_EVIDENCE_AVAILABLE_FOR_RESEARCHER_INTERPRETATION", "final synthesis status mismatch")
require(final["held_out"] == "2024_2025_SEALED_NOT_ACCESSED", "held-out is not sealed/unaccessed")
require(final["a6_g5"] == "V1_NON_ESTIMABLE_NOT_EXECUTED", "A6/G5 disposition changed")
require(len(final["results"]) == 98, "candidate-fold summary count is not 98")
require(len(final["pairwise_common_support"]) == 294, "pairwise summary count is not 294")
require({row["candidate"] for row in final["results"]} == CANDIDATES, "candidate registry mismatch")
require({row["fold"] for row in final["results"]} == FOLDS, "temporal fold registry mismatch")
for row in final["results"]:
    require(row["support"]["common_rows"] <= row["support"]["native_rows"], "common support exceeds native support")
    for field in ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba"):
        require(row["common"][field]["pair_count"] > 0, "empty common-support pair aggregation")
for row in final["pairwise_common_support"]:
    for field in ("loss_abs_ab", "loss_abs_ba", "loss_sq_ab", "loss_sq_ba"):
        require(row["metrics"][field]["pair_count"] > 0, "empty pairwise common-support aggregation")

print("PASS: 406/406 finalized units, hashes, H126 lineage, exact-support structure, temporal separation, and sealed held-out state validate.")
