"""Materialize frozen PO-C 2020-2023 relationship OF4 without interpretation.

This orchestrator reuses the published inner implementation byte-for-byte except
for temporal role, paths, lineage labels, and annual OF4 partition boundaries.
It writes only to the authorized external root, then losslessly compresses and
checksum-verifies every payload before atomic finalization.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODE = os.environ.get("V1_MATERIALIZATION_ROLE", "OF4").upper()
if MODE not in {"OF4", "FINAL_HELDOUT"}:
    raise RuntimeError(f"unsupported V1 materialization role: {MODE}")
HELDOUT = MODE == "FINAL_HELDOUT"
OF4 = Path(r"D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1" if HELDOUT else r"D:\MechanismAwareStatArbData\OF4")
RUNNER = OF4 / "_generated_runner"
INPUT = OF4 / "input" / "of4_input_v1.npz"
INPUT_TEMP = OF4 / "input" / "of4_input_v1.tmp.npz"
REL = OF4 / "relationships"
STATE = OF4 / "rt3_state"
A3A5 = OF4 / "a3_a5"
INTERMEDIATE_MANIFEST = OF4 / "_metadata" / "relationship_manifest.json"
FINAL_MANIFEST = (OF4 / "_metadata/final_relationship_stage.json") if HELDOUT else (ROOT / "data/manifests/V1_OF4_RELATIONSHIP_STAGE.json")
CANDIDATES = ["V1-R0D-252M", "V1-R0C-126W", "V1-R0L-126W", "V1-R1M-126W", "V1-R1MI-126W", "V1-R3-252M", "V1-R4-63D"]
YEARS = ["2024", "2025"] if HELDOUT else ["2020", "2021", "2022", "2023"]
UPPER = "20251231" if HELDOUT else "20231231"
ROLE_LABEL = "2024-2025_FINAL_HELDOUT_ONLY" if HELDOUT else "2020-2023_OF4_ONLY"
INPUT_ID = "V1-FINAL-HELDOUT-INPUT-1.0" if HELDOUT else "V1-PO-C-OF4-INPUT-1.0"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def replace_required(text: str, old: str, new: str, count: int | None = None) -> str:
    found = text.count(old)
    if found == 0 or (count is not None and found != count):
        raise RuntimeError(f"source binding mismatch: expected {count or 'at least one'} occurrence(s), found {found}: {old[:80]}")
    return text.replace(old, new)


def write_runner(name: str, source: str) -> Path:
    RUNNER.mkdir(parents=True, exist_ok=True)
    path = RUNNER / name
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(source, encoding="utf-8", newline="\n")
    os.replace(temp, path)
    return path


def transform_sources(input_hash: str | None = None) -> dict[str, Path]:
    repo = repr(str(ROOT))
    paths: dict[str, Path] = {}

    src = (ROOT / "tools/v1_phase1_prepare.py").read_text(encoding="utf-8")
    src = replace_required(src, 'ROOT = Path(__file__).resolve().parents[1]', f'ROOT = Path({repo})', 1)
    src = replace_required(src, 'OUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"', f'OUT = Path({repr(str(INPUT_TEMP))})', 1)
    src = replace_required(src, 'MANIFEST = ROOT / "data/manifests/V1_PHASE1_INNER_INPUT.json"', f'MANIFEST = Path({repr(str(OF4 / "_metadata/input_manifest.json"))})', 1)
    src = replace_required(src, 'LOWER, UPPER = "20130107", "20191231"', f'LOWER, UPPER = "20130107", "{UPPER}"', 1)
    src = replace_required(src, 'V1-PHASE1-INNER-INPUT-1.0', INPUT_ID)
    src = replace_required(src, 'IMMUTABLE DERIVED INNER INPUT — NO MODEL OUTPUT', 'IMMUTABLE DERIVED FINAL HELD-OUT INPUT — NO MODEL OUTPUT' if HELDOUT else 'IMMUTABLE DERIVED OF4 INPUT — NO MODEL OUTPUT')
    src = replace_required(src, '"of4_accessed": False', f'"of4_accessed": {str(not HELDOUT)}', 1)
    src = src.replace('"held_out_accessed": False', f'"held_out_accessed": {str(HELDOUT)}')
    src = replace_required(src, 'OUT.relative_to(ROOT).as_posix()', 'str(OUT)', 1)
    paths["prepare"] = write_runner("prepare.py", src)
    if input_hash is None:
        return paths

    start_year, end_year = (2024, 2026) if HELDOUT else (2020, 2024)
    annual_double = f'periods=[(f"{{y}}",f"{{y}}0101",f"{{y}}1231") for y in range({start_year},{end_year})]'
    annual_single = f"periods=[(f'{{y}}',f'{{y}}0101',f'{{y}}1231') for y in range({start_year},{end_year})]"

    src = (ROOT / "tools/v1_phase1_inner_relationships.py").read_text(encoding="utf-8")
    src = replace_required(src, 'ROOT = Path(__file__).resolve().parents[1]', f'ROOT = Path({repo})', 1)
    src = replace_required(src, 'INPUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"', f'INPUT = Path({repr(str(INPUT))})', 1)
    src = replace_required(src, 'OUT = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/relationships"', f'OUT = Path({repr(str(REL))})', 1)
    src = replace_required(src, 'PUBLIC_MANIFEST = ROOT / "data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json"', f'PUBLIC_MANIFEST = Path({repr(str(INTERMEDIATE_MANIFEST))})', 1)
    src = replace_required(src, 'EXPECTED_INPUT_HASH = "360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"', f'EXPECTED_INPUT_HASH = "{input_hash}"', 1)
    src = replace_required(src, 'if dates[-1]>"20191231": raise RuntimeError("input role exceeds authorized 2019 boundary")', f'if dates[-1]>"{UPPER}": raise RuntimeError("input role exceeds authorized boundary")', 1)
    old = 'periods=[(f"{y}H{s}",f"{y}{\'0101\' if s==1 else \'0701\'}",f"{y}{\'0630\' if s==1 else \'1231\'}") for y in range(2015,2020) for s in (1,2)]'
    src = replace_required(src, old, annual_double, 1)
    src = replace_required(src, 'len(entries)<50', 'len(entries)<20', 1)
    src = replace_required(src, 'V1-PHASE1-RELATIONSHIP-OUTPUTS-1.0', 'V1-PO-C-OF4-RELATIONSHIP-OUTPUTS-1.0')
    src = replace_required(src, '2015-2019_INNER_ONLY', ROLE_LABEL)
    src = replace_required(src, '"of4_accessed":False', f'"of4_accessed":{str(not HELDOUT)}')
    src = src.replace('"held_out_accessed":False', f'"held_out_accessed":{str(HELDOUT)}')
    paths["relationships"] = write_runner("v1_phase1_inner_relationships.py", src)

    for key, filename, candidate in (("r3", "v1_phase1_inner_r3.py", "V1-R3-252M"), ("r4", "v1_phase1_inner_r4.py", "V1-R4-63D")):
        src = (ROOT / "tools" / filename).read_text(encoding="utf-8")
        src = replace_required(src, 'ROOT=Path(__file__).resolve().parents[1]', f'ROOT=Path({repo})', 1)
        src = replace_required(src, 'INPUT=ROOT/"data/qa_work/v1/phase1/inner_input_v1.npz"', f'INPUT=Path({repr(str(INPUT))})', 1)
        src = replace_required(src, f'OUT=ROOT/"data/qa_work/v1/phase1/inner_outputs_v2/relationships/{candidate}"', f'OUT=Path({repr(str(REL / candidate))})', 1)
        src = replace_required(src, 'EXPECTED="360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"', f'EXPECTED="{input_hash}"', 1)
        src = replace_required(src, "periods=[(f'{y}H{s}',f'{y}{\"0101\" if s==1 else \"0701\"}',f'{y}{\"0630\" if s==1 else \"1231\"}') for y in range(2015,2020) for s in (1,2)]", annual_single)
        src = replace_required(src, f"ROOT/'data/qa_work/v1/phase1/rt3_state_v1/{candidate}'", f"Path({repr(str(STATE / candidate))})", 1)
        src = replace_required(src, "'of4_accessed':False", f"'of4_accessed':{str(not HELDOUT)}")
        src = src.replace("'held_out_accessed':False", f"'held_out_accessed':{str(HELDOUT)}")
        paths[key] = write_runner(filename, src)

    src = (ROOT / "tools/v1_rt3_state_static.py").read_text(encoding="utf-8")
    src = replace_required(src, 'ROOT=Path(__file__).resolve().parents[1]', f'ROOT=Path({repo})', 1)
    src = replace_required(src, "sys.path.insert(0,str(ROOT/'tools'))", "sys.path.insert(0, str(Path(__file__).resolve().parent))", 1)
    src = replace_required(src, "OUT=ROOT/'data/qa_work/v1/phase1/rt3_state_v1'", f'OUT=Path({repr(str(STATE))})', 1)
    src = replace_required(src, "REL=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/relationships'", f'REL=Path({repr(str(REL))})', 1)
    src = replace_required(src, "if dates[-1]>'20191231'", f"if dates[-1]>'{UPPER}'", 1)
    src = replace_required(src, "periods=[(f'{y}H{s}',f'{y}{\"0101\" if s==1 else \"0701\"}',f'{y}{\"0630\" if s==1 else \"1231\"}') for y in range(2015,2020) for s in (1,2)]", annual_single, 1)
    src = replace_required(src, "'of4_accessed':False", f"'of4_accessed':{str(not HELDOUT)}")
    src = src.replace("'held_out_accessed':False", f"'held_out_accessed':{str(HELDOUT)}")
    paths["static_state"] = write_runner("v1_rt3_state_static.py", src)

    src = (ROOT / "tools/v1_inner_a3_a5.py").read_text(encoding="utf-8")
    src = replace_required(src, 'ROOT = Path(__file__).resolve().parents[1]', f'ROOT = Path({repo})', 1)
    src = replace_required(src, 'INPUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"', f'INPUT = Path({repr(str(INPUT))})', 1)
    src = replace_required(src, 'REL_ROOT = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/relationships"', f'REL_ROOT = Path({repr(str(REL))})', 1)
    src = replace_required(src, 'STATE_ROOT = ROOT / "data/qa_work/v1/phase1/rt3_state_v1"', f'STATE_ROOT = Path({repr(str(STATE))})', 1)
    src = replace_required(src, 'OUT_ROOT = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/a3_a5"', f'OUT_ROOT = Path({repr(str(A3A5))})', 1)
    src = replace_required(src, 'EXPECTED_INPUT = "360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"', f'EXPECTED_INPUT = "{input_hash}"', 1)
    src = replace_required(src, '(ROOT / "data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json")', f'Path({repr(str(INTERMEDIATE_MANIFEST))})', 1)
    src = replace_required(src, 'year = int(label[:4]); half = int(label[-1])\n        partition_hi = f"{year}{\'0630\' if half == 1 else \'1231\'}"', 'year = int(label)\n        partition_hi = f"{year}1231"', 1)
    src = replace_required(src, '"of4_accessed": False', f'"of4_accessed": {str(not HELDOUT)}')
    src = src.replace('"held_out_accessed": False', f'"held_out_accessed": {str(HELDOUT)}')
    paths["a3a5"] = write_runner("v1_inner_a3_a5.py", src)
    return paths


def run(path: Path, *args: str) -> None:
    env = os.environ.copy()
    env["NUMBA_CACHE_DIR"] = str(OF4 / "_numba_cache")
    subprocess.run([sys.executable, str(path), *args], cwd=ROOT, env=env, check=True)


def relationship_manifest(input_hash: str) -> None:
    entries = []
    for candidate in CANDIDATES:
        for year in YEARS:
            marker = REL / candidate / f"{year}.complete.json"
            payload = REL / candidate / f"{year}.npy"
            if not marker.exists() or not payload.exists():
                raise RuntimeError(f"missing relationship checkpoint {candidate}/{year}")
            meta = json.loads(marker.read_text(encoding="utf-8"))
            if sha(payload) != meta["sha256"]:
                raise RuntimeError(f"relationship checksum mismatch {candidate}/{year}")
            entries.append({"candidate": candidate, "partition": year, "artifact": str(payload), "rows": int(meta["rows"]), "sha256": meta["sha256"], "of4_accessed": not HELDOUT, "held_out_accessed": HELDOUT})
    manifest = {"manifest_id": "V1-FINAL-HELDOUT-RELATIONSHIP-OUTPUTS-1.0" if HELDOUT else "V1-PO-C-OF4-RELATIONSHIP-OUTPUTS-1.0", "status": "IMMUTABLE_COMPLETE", "input_sha256": input_hash, "candidate_count": 7, "partition_count": len(CANDIDATES) * len(YEARS), "partitions": entries, "date_role": ROLE_LABEL, "interpretation": "NONE_BEFORE_COMPLETE_MATERIALIZATION", "of4_accessed": not HELDOUT, "held_out_accessed": HELDOUT}
    INTERMEDIATE_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    temp = INTERMEDIATE_MANIFEST.with_suffix(".tmp")
    temp.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, INTERMEDIATE_MANIFEST)


def compress_finalize(input_hash: str, shard: int = 0, shards: int = 1) -> None:
    roots = (REL, STATE, A3A5)
    logical = {p for root in roots for p in root.glob("*/*.npy")}
    logical.update(Path(str(p)[:-3]) for root in roots for p in root.glob("*/*.npy.gz"))
    payloads = sorted(logical)
    expected_payloads = len(CANDIDATES) * len(YEARS) * 4
    if len(payloads) != expected_payloads:
        raise RuntimeError(f"expected {expected_payloads} role payloads, found {len(payloads)}")
    if shards < 1 or shard < 0 or shard >= shards:
        raise RuntimeError("invalid compression shard")
    payloads = [path for index, path in enumerate(payloads) if index % shards == shard]
    records = []
    for source in payloads:
        final = source.with_suffix(source.suffix + ".gz")
        temp = final.with_suffix(final.suffix + ".tmp")
        checkpoint = final.with_suffix(final.suffix + ".complete.json")
        if final.exists() or checkpoint.exists():
            if not (final.exists() and checkpoint.exists()):
                raise RuntimeError(f"incomplete compressed checkpoint: {final}")
            record = json.loads(checkpoint.read_text(encoding="utf-8"))
            if sha(final) != record["sha256"]:
                raise RuntimeError(f"compressed checkpoint hash mismatch: {final}")
            verify = hashlib.sha256()
            with gzip.open(final, "rb") as inp:
                for chunk in iter(lambda: inp.read(8 << 20), b""):
                    verify.update(chunk)
            if verify.hexdigest().upper() != record["raw_sha256"]:
                raise RuntimeError(f"compressed checkpoint roundtrip mismatch: {final}")
            if source.exists():
                source.unlink()
            records.append(record)
            continue
        if not source.exists():
            raise RuntimeError(f"missing uncompressed source: {source}")
        raw_hash = sha(source)
        raw_bytes = source.stat().st_size
        with source.open("rb") as inp, temp.open("wb") as raw_out:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out, compresslevel=9, mtime=0) as out:
                shutil.copyfileobj(inp, out, 8 << 20)
        verify = hashlib.sha256()
        with gzip.open(temp, "rb") as inp:
            for chunk in iter(lambda: inp.read(8 << 20), b""):
                verify.update(chunk)
        if verify.hexdigest().upper() != raw_hash:
            raise RuntimeError(f"lossless validation failed: {source}")
        compressed_hash = sha(temp)
        os.replace(temp, final)
        record = {"logical_path": source.relative_to(OF4).as_posix(), "physical_relative_path": final.relative_to(OF4).as_posix(), "raw_sha256": raw_hash, "sha256": compressed_hash, "raw_bytes": raw_bytes, "compressed_bytes": final.stat().st_size, "compression": "GZIP_DEFLATE_LEVEL9_MTIME0_FILENAME_EMPTY", "validation": "LOSSLESS_ROUNDTRIP_PASS"}
        checkpoint_temp = checkpoint.with_suffix(".tmp")
        checkpoint_temp.write_text(json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        os.replace(checkpoint_temp, checkpoint)
        records.append(record)
        source.unlink()
    if shards != 1:
        print(json.dumps({"compression_shard": shard, "shards": shards, "payload_count": len(records), "result": "PASS", "values_disclosed": False}))
        return
    manifest = {"manifest_id": "V1-FINAL-HELDOUT-RELATIONSHIP-STAGE-1.0" if HELDOUT else "V1-PO-C-OF4-RELATIONSHIP-STAGE-1.0", "status": "IMMUTABLE_COMPLETE_CHECKSUMMED", "po_c_commit": "7fcfd3c9da73c388b3e1ba9219000c6dd2e5c27b", "input_sha256": input_hash, "physical_root": str(OF4), "scientific_identity_independent_of_physical_location": True, "candidate_count": 7, "annual_folds": YEARS, "payload_count": len(records), "payloads": records, "relationship_protocol": "FROZEN_PAIR_A_R0_R1_R3_R4", "a3_a5": "AUTHORIZED_MORPHOLOGY_MATERIALIZED", "a6_g5": "V1_NON_ESTIMABLE_NOT_EXECUTED", "retuning": "NONE", "interpretation": "NONE_BEFORE_THIS_MANIFEST", "held_out": "2024_2025_ACCESSED_AUTHORIZED" if HELDOUT else "2024_2025_SEALED_NOT_ACCESSED", "materialization": "TEMPORARY_WRITE_VALIDATE_CHECKSUM_ATOMIC_FINALIZE", "compression": "DETERMINISTIC_LOSSLESS"}
    FINAL_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    temp = FINAL_MANIFEST.with_suffix(".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(manifest, sort_keys=True, indent=2) + "\n")
    os.replace(temp, FINAL_MANIFEST)
    print(json.dumps({"manifest_id": manifest["manifest_id"], "payload_count": len(records), "result": "PASS", "values_disclosed": False}))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("prepare", "relationships", "state", "a3a5", "compress", "all"))
    parser.add_argument("--candidate", choices=CANDIDATES)
    parser.add_argument("--shard", type=int, default=0)
    parser.add_argument("--shards", type=int, default=1)
    args = parser.parse_args()
    OF4.mkdir(parents=True, exist_ok=True)
    paths = transform_sources()
    if args.stage in ("prepare", "all") and not INPUT.exists():
        INPUT.parent.mkdir(parents=True, exist_ok=True)
        (OF4 / "_metadata").mkdir(parents=True, exist_ok=True)
        if INPUT_TEMP.exists():
            raise RuntimeError(f"incomplete input checkpoint requires controlled cleanup: {INPUT_TEMP}")
        run(paths["prepare"])
        import numpy as np
        with np.load(INPUT_TEMP, allow_pickle=False) as prepared:
            dates = np.char.decode(prepared["dates"])
            if dates[0] != "20130107" or dates[-1] != UPPER or np.any(dates > UPPER):
                raise RuntimeError("role input temporal boundary validation failed")
        prepared_hash = sha(INPUT_TEMP)
        os.replace(INPUT_TEMP, INPUT)
        meta_path = OF4 / "_metadata/input_manifest.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["artifact"] = str(INPUT)
        meta["artifact_sha256"] = prepared_hash
        meta_temp = meta_path.with_suffix(".tmp")
        meta_temp.write_text(json.dumps(meta, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        os.replace(meta_temp, meta_path)
    if not INPUT.exists():
        raise RuntimeError("OF4 input is not materialized")
    input_hash = sha(INPUT)
    paths = transform_sources(input_hash)
    if args.stage in ("relationships", "all"):
        targets = [args.candidate] if args.candidate else CANDIDATES
        for candidate in targets:
            if candidate.startswith(("V1-R0", "V1-R1")):
                run(paths["relationships"], "--candidate", candidate)
            elif candidate == "V1-R3-252M":
                run(paths["r3"])
            else:
                run(paths["r4"])
        if not args.candidate:
            relationship_manifest(input_hash)
    if args.stage in ("state", "all"):
        relationship_manifest(input_hash)
        run(paths["static_state"])
        run(paths["r3"], "--augment-state")
        run(paths["r4"], "--augment-state")
    if args.stage in ("a3a5", "all"):
        relationship_manifest(input_hash)
        run(paths["a3a5"])
    if args.stage in ("compress", "all"):
        compress_finalize(input_hash, args.shard, args.shards)


if __name__ == "__main__":
    main()
