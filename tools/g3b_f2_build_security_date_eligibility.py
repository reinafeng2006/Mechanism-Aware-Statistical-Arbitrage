"""Build the G3B-F2 security-date structural-eligibility sidecar.

Metadata/governance only: no returns, relationships, measurements, targets or outcomes.
The output records structural states; it deliberately has no universal eligible flag.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/g3b_full/tushare/full_2013_2025_v1"
C06 = ROOT / "data/qa_work/g3b_full/c06/20260909T081518Z"
PROBE = ROOT / "data/raw/g3b_full/structural_resolution/601313_tushare_probe_v1/daily.json"
IDENTITY = ROOT / "registers/G3B_IDENTIFIER_HISTORY_RESOLUTION_REGISTER.jsonl"
OUT = ROOT / "data/qa_work/g3b_f2/security_date_eligibility/v1"
SCHEMA_VERSION = "SECURITY_DATE_ELIGIBILITY_SIDECAR_V1"
RULE_VERSION = "G3B-C1-C04-C05-ELIGIBILITY-V1"

COLUMNS = [
    "stable_security_id", "observation_date", "historical_ticker_code",
    "identifier_lineage_state", "c04_structural_state", "c04_basis",
    "c05_structural_state", "c05_basis", "eligibility_rule_version",
    "upstream_artifact_references", "schema_version", "generation_version",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load_payload(path: Path) -> tuple[list[str], list[list]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = payload.get("data") or {}
    return data.get("fields") or [], data.get("items") or []


def canonical_c03_files() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for line in (RAW / "acquisition_journal.jsonl").read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("contract") != "C03" or event.get("response_code") != 0:
            continue
        code = (event.get("params") or {}).get("ts_code")
        path = RAW / event["file"]
        if code and code not in result and path.exists():
            result[code] = path
    return result


def c01_intervals() -> dict[str, tuple[str, str]]:
    intervals: dict[str, tuple[str, str]] = {}
    seen: set[str] = set()
    for line in (RAW / "acquisition_journal.jsonl").read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("contract") != "C01" or event.get("response_code") != 0:
            continue
        if event.get("request_id") in seen:
            continue
        seen.add(event["request_id"])
        fields, rows = load_payload(RAW / event["file"])
        ix = {name: fields.index(name) for name in ("ts_code", "list_date", "delist_date")}
        for row in rows:
            intervals[str(row[ix["ts_code"]])] = (
                str(row[ix["list_date"]] or ""), str(row[ix["delist_date"]] or "")
            )
    return intervals


def dates_from(path: Path) -> set[str]:
    fields, rows = load_payload(path)
    if "trade_date" not in fields:
        return set()
    ix = fields.index("trade_date")
    return {str(row[ix]) for row in rows}


def stable_id(code: str) -> tuple[str, str]:
    if code == "601313.SH":
        return "CN-SSE-601313-601360-LINEAGE", "MAPPED HISTORICAL CODE; ECONOMIC CONTINUITY NOT ASSERTED"
    exchange, numeric = code.split(".")[1], code.split(".")[0]
    return f"CN-{exchange}-{numeric}", "DIRECT C01/C03 IDENTIFIER"


def rows() -> list[dict[str, str]]:
    c03 = canonical_c03_files()
    intervals = c01_intervals()
    benchmark: set[str] = set()
    # E03-A is not in the C03 map; obtain its first canonical journal object.
    for line in (RAW / "acquisition_journal.jsonl").read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("contract") == "E03-A" and event.get("response_code") == 0:
            benchmark = dates_from(RAW / event["file"])
            break
    universe = []
    for raw_code in C06.joinpath("security_union.txt").read_text(encoding="utf-8").splitlines():
        raw_code = raw_code.strip()
        if raw_code.startswith("6"):
            universe.append(f"{raw_code}.SH")
        elif raw_code.startswith(("0", "3")):
            universe.append(f"{raw_code}.SZ")

    output: list[dict[str, str]] = []
    for code in sorted(universe):
        source_path = c03[code]
        actual = dates_from(source_path)
        lookup_code = code
        upper_override = "20251231"
        if code == "601313.SH":
            actual = {d for d in dates_from(PROBE) if d <= "20180227"}
            source_path = PROBE
            lookup_code = "601360.SH"
            upper_override = "20180227"
        listed, delisted = intervals.get(lookup_code, ("20130107", ""))
        lower = max("20130107", listed or "20130107")
        upper = min("20251231", delisted or "20251231", upper_override)
        expected = {d for d in benchmark if lower <= d <= upper}
        security_id, lineage = stable_id(code)
        for date in sorted(expected | actual):
            observed = date in actual
            c05_state = "NORMAL TRADING OBSERVED" if observed else "UNKNOWN MISSINGNESS"
            c05_basis = (
                f"observed raw C03 row:{source_path.relative_to(ROOT).as_posix()}"
                if observed else
                "benchmark session within C01 listing interval; no C03 row; no qualified C05 evidence"
            )
            refs = [
                source_path.relative_to(ROOT).as_posix(),
                (C06 / "security_union.txt").relative_to(ROOT).as_posix(),
                (RAW / "acquisition_journal.jsonl").relative_to(ROOT).as_posix(),
                IDENTITY.relative_to(ROOT).as_posix(),
            ]
            output.append({
                "stable_security_id": security_id,
                "observation_date": date,
                "historical_ticker_code": code,
                "identifier_lineage_state": lineage,
                "c04_structural_state": "CORPORATE_ACTION STATUS UNRESOLVED",
                "c04_basis": "authoritative C04 universe-wide coverage incomplete; no action cleanliness inferred",
                "c05_structural_state": c05_state,
                "c05_basis": c05_basis,
                "eligibility_rule_version": RULE_VERSION,
                "upstream_artifact_references": ";".join(refs),
                "schema_version": SCHEMA_VERSION,
                "generation_version": "g3b_f2_build_security_date_eligibility.py:v1",
            })
    output.sort(key=lambda x: (x["stable_security_id"], x["observation_date"], x["historical_ticker_code"]))
    keys = [(x["stable_security_id"], x["observation_date"]) for x in output]
    if len(keys) != len(set(keys)):
        raise SystemExit("Non-unique stable_security_id × observation_date grain")
    return output


def write_gzip(path: Path, records: list[dict[str, str]]) -> None:
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            with io.TextIOWrapper(zipped, encoding="utf-8", newline="") as text:
                writer = csv.DictWriter(text, fieldnames=COLUMNS, lineterminator="\n")
                writer.writeheader()
                writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    final = OUT / "security_date_eligibility_sidecar_v1.csv.gz"
    manifest_path = OUT / "manifest.json"
    records = rows()
    with tempfile.TemporaryDirectory() as temp_dir:
        first = Path(temp_dir) / "first.csv.gz"
        second = Path(temp_dir) / "second.csv.gz"
        write_gzip(first, records)
        write_gzip(second, records)
        if sha(first) != sha(second):
            raise SystemExit("Deterministic regeneration failed")
        if final.exists():
            if not args.verify_existing:
                raise SystemExit("Immutable output already exists; use --verify-existing")
            if sha(final) != sha(first):
                raise SystemExit("Existing immutable sidecar differs from deterministic regeneration")
        else:
            final.write_bytes(first.read_bytes())

    upstream = {}
    for path in [RAW / "manifest.json", RAW / "acquisition_journal.jsonl",
                 C06 / "security_union.txt", C06 / "primary_membership.jsonl", IDENTITY, PROBE]:
        upstream[path.relative_to(ROOT).as_posix()] = sha(path)
    counts = defaultdict(int)
    for record in records:
        counts[record["c05_structural_state"]] += 1
    manifest = {
        "artifact": final.name,
        "status": "IMMUTABLE GOVERNANCE METADATA — NON-EMPIRICAL",
        "schema_version": SCHEMA_VERSION,
        "eligibility_rule_version": RULE_VERSION,
        "grain": "stable_security_identity × observation_date",
        "universal_eligible_field": False,
        "row_count": len(records),
        "c05_state_counts": dict(sorted(counts.items())),
        "c04_state": "CORPORATE_ACTION STATUS UNRESOLVED",
        "sha256": sha(final),
        "deterministic_regeneration": "PASS",
        "stable_order": ["stable_security_id", "observation_date", "historical_ticker_code"],
        "upstream_sha256": upstream,
        "prohibited_outputs": ["returns", "relationships", "abnormality", "measurements", "beliefs", "targets", "outcomes", "PnL"],
    }
    encoded = (json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if manifest_path.exists():
        existing = manifest_path.read_bytes()
        if existing != encoded:
            raise SystemExit("Existing immutable manifest differs")
    else:
        manifest_path.write_bytes(encoded)
    print(json.dumps({"sidecar": str(final.relative_to(ROOT)), "rows": len(records),
                      "sha256": manifest["sha256"], "c05_state_counts": manifest["c05_state_counts"],
                      "regeneration": "PASS"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
