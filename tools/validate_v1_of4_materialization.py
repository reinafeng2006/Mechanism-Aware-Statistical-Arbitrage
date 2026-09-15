"""Validate the finalized external PO-C OF4 manifest without interpretation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/manifests/V1_OF4_RELATIONSHIP_STAGE.json"


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    root = Path(manifest["physical_root"])
    failures: list[str] = []
    records = manifest.get("payloads", [])
    if manifest.get("status") != "IMMUTABLE_COMPLETE_CHECKSUMMED":
        failures.append("status")
    if manifest.get("payload_count") != 112 or len(records) != 112:
        failures.append("payload_count")
    if manifest.get("annual_folds") != ["2020", "2021", "2022", "2023"]:
        failures.append("annual_folds")
    if manifest.get("a6_g5") != "V1_NON_ESTIMABLE_NOT_EXECUTED":
        failures.append("a6_g5")
    if manifest.get("held_out") != "2024_2025_SEALED_NOT_ACCESSED":
        failures.append("held_out")
    if manifest.get("retuning") != "NONE":
        failures.append("retuning")
    for record in records:
        path = root / record["physical_relative_path"]
        checkpoint = path.with_suffix(path.suffix + ".complete.json")
        if not path.exists() or sha(path) != record["sha256"]:
            failures.append(f"payload:{record['physical_relative_path']}")
            continue
        if not checkpoint.exists() or json.loads(checkpoint.read_text(encoding="utf-8")) != record:
            failures.append(f"checkpoint:{record['physical_relative_path']}")
        if record.get("compression") != "GZIP_DEFLATE_LEVEL9_MTIME0_FILENAME_EMPTY" or record.get("validation") != "LOSSLESS_ROUNDTRIP_PASS":
            failures.append(f"compression:{record['physical_relative_path']}")
    raw_files = list(root.glob("relationships/*/*.npy")) + list(root.glob("rt3_state/*/*.npy")) + list(root.glob("a3_a5/*/*.npy"))
    temp_files = list(root.rglob("*.tmp"))
    if raw_files:
        failures.append("uncompressed_payloads_remain")
    if temp_files:
        failures.append("temporary_files_remain")
    result = {"manifest_id": manifest.get("manifest_id"), "payload_count": len(records), "compressed_bytes": sum(int(x["compressed_bytes"]) for x in records), "raw_bytes": sum(int(x["raw_bytes"]) for x in records), "result": "PASS" if not failures else "FAIL", "values_disclosed": False, "failures": failures}
    print(json.dumps(result))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
