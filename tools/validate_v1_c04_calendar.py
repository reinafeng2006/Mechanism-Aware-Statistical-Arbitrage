"""Validate the immutable C04-A official calendar and conservative semantics."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data" / "manifests" / "C04_A_OFFICIAL_CALENDAR_V1.json"
EXPECTED_CORE = "3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616"
ALLOWED_HOSTS = {"query.sse.com.cn", "www.szse.cn", "docs.static.szse.cn"}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest().upper()


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    failures: list[str] = []
    if manifest.get("manifest_id") != "C04-A-OFFICIAL-CALENDAR-V1":
        failures.append("manifest ID")
    if manifest.get("ancestry", {}).get("root_fingerprint") != EXPECTED_CORE:
        failures.append("core ancestry")
    if manifest.get("adjusted_price_constructed") is not False:
        failures.append("adjusted-price prohibition")
    if manifest.get("core_c04_state_mutated") is not False:
        failures.append("core C04 mutation")
    if manifest.get("nonclaim") != "NO IDENTIFIED ACTION UNDER V1 CALENDAR != AUTHORITATIVELY ACTION-CLEAN":
        failures.append("C04 nonclaim")
    if manifest.get("failures"):
        failures.append("acquisition failures")

    raw_records = manifest.get("raw_artifacts", [])
    material = bytearray()
    for record in sorted(raw_records, key=lambda item: item["file"]):
        path = ROOT / record["file"]
        if not path.is_file() or digest(path) != record["sha256"]:
            failures.append(f"raw hash: {record['file']}")
        if urlparse(record["url"]).hostname not in ALLOWED_HOSTS:
            failures.append(f"nonofficial host: {record['url']}")
        material.extend(f"{record['file']}\t{record['sha256']}\n".encode("utf-8"))
    if hashlib.sha256(material).hexdigest().upper() != manifest.get("raw_artifact_root_sha256"):
        failures.append("raw artifact root")

    for key in ("normalized_action_calendar", "exclusion_calendar"):
        record = manifest[key]
        path = ROOT / record["file"]
        if not path.is_file() or digest(path) != record["sha256"] or path.stat().st_size != record["bytes"]:
            failures.append(f"derived hash: {key}")

    action_rows = [json.loads(line) for line in (ROOT / manifest["normalized_action_calendar"]["file"]).read_text(encoding="utf-8").splitlines()]
    exclusions = [json.loads(line) for line in (ROOT / manifest["exclusion_calendar"]["file"]).read_text(encoding="utf-8").splitlines()]
    if len(action_rows) != manifest.get("normalized_action_rows"):
        failures.append("action row count")
    if len(exclusions) != manifest.get("exclusion_rows"):
        failures.append("exclusion row count")
    if any("AUTHORITATIVELY ACTION-CLEAN" in json.dumps(row, ensure_ascii=False) for row in action_rows + exclusions):
        failures.append("forbidden cleanliness claim")
    if any(row.get("source") not in {"SSE_OFFICIAL", "SZSE_OFFICIAL"} for row in action_rows):
        failures.append("normalized source class")
    if any(not row.get("effective_ex_date") for row in exclusions):
        failures.append("exclusion without effective date")
    if any(row.get("state") != "IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED" for row in exclusions):
        failures.append("exclusion state")
    if any(row.get("interval_rule") != "EXCLUDE_CLOSE_TO_CLOSE_INTERVAL_(PREVIOUS_ELIGIBLE_SESSION,CURRENT_SESSION]_CONTAINING_EFFECTIVE_EX_DATE" for row in exclusions):
        failures.append("interval rule")

    raw_manifest = ROOT / "data" / "raw" / "v1" / "c04_a" / "official_calendar_v1" / "manifest.json"
    derived_manifest = ROOT / "data" / "qa_work" / "v1" / "c04_a" / "official_calendar_v1" / "manifest.json"
    if not raw_manifest.is_file() or raw_manifest.read_bytes() != MANIFEST_PATH.read_bytes():
        failures.append("raw/public manifest identity")
    if not derived_manifest.is_file() or derived_manifest.read_bytes() != MANIFEST_PATH.read_bytes():
        failures.append("derived/public manifest identity")

    result = {
        "manifest_id": manifest.get("manifest_id"),
        "raw_artifacts": len(raw_records),
        "actions": len(action_rows),
        "exclusions": len(exclusions),
        "pre_core_boundary_records_retained_as_nonapplied_source_history": sum(row["effective_ex_date"] < "2013-01-07" for row in exclusions),
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
