"""Materialize frozen V1 A3/A5 inner-development artifacts.

The output matrices are row-index bound to the immutable relationship
partitions.  They contain no duplicated identifiers and never modify their
ancestors.  No values are printed or summarized; stdout contains only lineage,
row counts, hashes, and availability counts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"
REL_ROOT = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/relationships"
STATE_ROOT = ROOT / "data/qa_work/v1/phase1/rt3_state_v1"
OUT_ROOT = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/a3_a5"
EXPECTED_INPUT = "360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"
HORIZONS = (1, 5, 10, 20)
A3_FIELDS = ("departure_ab", "scaled_departure_ab", "departure_ba", "scaled_departure_ba")
A5_FIELDS = ("RT0", "RT1", "RT2_abs", "RT2_signed", "RT3")


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def candidate_kind(candidate: str) -> str:
    if candidate == "V1-R3-252M":
        return "r3"
    if candidate == "V1-R4-63D":
        return "r4"
    return "static"


def state_index(state: np.ndarray) -> dict[int, list[tuple[int, np.void]]]:
    """Index refresh state by date; values stay as numpy records."""
    out: dict[int, list[tuple[int, np.void]]] = {}
    for row in state:
        key = int(row["a"]) * 750 + int(row["b"])
        out.setdefault(int(row["date_ix"]), []).append((key, row))
    return out


def future_mu_static(row: np.void, source: np.ndarray, peer: np.ndarray,
                     market: np.ndarray, industry: np.ndarray,
                     ind_sum: np.ndarray, ind_count: np.ndarray,
                     a: int, b: int, future_ix: np.ndarray, direction: int) -> np.ndarray:
    p = row["params"]
    kind = int(row["kind"])
    if kind <= 2:
        alpha, beta = (p[0], p[1]) if direction == 0 else (p[5], p[6])
        return alpha + beta * source
    fa, fb = p[15:18], p[18:21]
    out = np.full(len(future_ix), np.nan, np.float64)
    for z, q in enumerate(future_ix):
        if not (np.isfinite(source[z]) and np.isfinite(peer[z]) and np.isfinite(market[q])):
            continue
        ga, gb = int(industry[q, a]), int(industry[q, b])
        qa = qb = 0.0
        if kind == 4:
            ca, cb = int(ind_count[q, ga]) - 1, int(ind_count[q, gb]) - 1
            sa, sb = ind_sum[q, ga] - source[z], ind_sum[q, gb] - peer[z]
            if ga == gb:
                ca -= 1; cb -= 1; sa -= peer[z]; sb -= source[z]
            if ca <= 0 or cb <= 0:
                continue
            qa, qb = sa / ca, sb / cb
        fca = fa[0] + fa[1] * market[q] + fa[2] * qa
        fcb = fb[0] + fb[1] * market[q] + fb[2] * qb
        if direction == 0:
            out[z] = fcb + p[0] + p[1] * (source[z] - fca)
        else:
            out[z] = fca + p[5] + p[6] * (source[z] - fcb)
    return out


def future_mu_r3(row: np.void, source: np.ndarray, direction: int) -> np.ndarray:
    p = row["params"]
    alpha, beta = (p[6], p[7]) if direction == 0 else (p[13], p[14])
    return alpha + beta * source


def future_mu_r4(row: np.void, source: np.ndarray, direction: int) -> np.ndarray:
    if direction == 0:
        return float(row["alpha_ab"]) + float(row["beta_ab"]) * source
    return float(row["alpha_ba"]) + float(row["beta_ba"]) * source


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate")
    ap.add_argument("--partition")
    args = ap.parse_args()
    if sha(INPUT) != EXPECTED_INPUT:
        raise RuntimeError("inner input checksum mismatch")
    data = np.load(INPUT, allow_pickle=False)
    dates = np.char.decode(data["dates"])
    response = data["response"]
    member = data["pair_member"]
    market = data["benchmark_response"]
    industry = data["industry"]
    ind_sum = np.zeros((len(dates), 36), np.float64)
    ind_count = np.zeros((len(dates), 36), np.int16)
    for g in (34, 35):
        mask = (industry == g) & member & np.isfinite(response)
        ind_sum[:, g] = np.where(mask, response, 0.0).sum(1)
        ind_count[:, g] = mask.sum(1)

    manifest = json.loads((ROOT / "data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json").read_text(encoding="utf-8"))
    parts = sorted(manifest["partitions"], key=lambda x: (x["candidate"], x["partition"]))
    parts = [p for p in parts if (not args.candidate or p["candidate"] == args.candidate)
             and (not args.partition or p["partition"] == args.partition)]
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    summary = []
    for meta in parts:
        candidate, label = meta["candidate"], meta["partition"]
        year = int(label[:4]); half = int(label[-1])
        partition_hi = f"{year}{'0630' if half == 1 else '1231'}"
        rel_path = REL_ROOT / candidate / f"{label}.npy"
        if sha(rel_path) != meta["sha256"]:
            raise RuntimeError(f"relationship checksum mismatch {candidate}/{label}")
        out_dir = OUT_ROOT / candidate
        out_dir.mkdir(exist_ok=True)
        a3_path, a5_path = out_dir / f"{label}.a3.npy", out_dir / f"{label}.a5.npy"
        marker = out_dir / f"{label}.complete.json"
        if a3_path.exists() or a5_path.exists() or marker.exists():
            if a3_path.exists() and a5_path.exists() and marker.exists():
                old = json.loads(marker.read_text(encoding="utf-8"))
                if sha(a3_path) == old["a3_sha256"] and sha(a5_path) == old["a5_sha256"]:
                    print(json.dumps({"candidate": candidate, "partition": label, "status": "CHECKPOINT_VERIFIED"}), flush=True)
                    summary.append(old)
                    continue
            raise RuntimeError(f"no-overwrite conflict {candidate}/{label}")
        rel = np.load(rel_path, allow_pickle=False, mmap_mode="r")
        state_path = STATE_ROOT / candidate / f"{label}.npy"
        state = np.load(state_path, allow_pickle=False, mmap_mode="r")
        if candidate_kind(candidate) == "r4" and len(state) != len(rel):
            raise RuntimeError(f"R4 state row mismatch {candidate}/{label}")
        refresh = None if candidate_kind(candidate) == "r4" else state_index(state)
        active: dict[int, np.void] = {}
        a3 = np.lib.format.open_memmap(a3_path.with_suffix(".tmp.npy"), mode="w+", dtype="<f4", shape=(len(rel), 4))
        a5 = np.lib.format.open_memmap(a5_path.with_suffix(".tmp.npy"), mode="w+", dtype="<f4", shape=(len(rel), 2, 4, 5))
        a3[:] = np.nan; a5[:] = np.nan
        pos = 0; available = np.zeros((2, 4, 5), np.int64)
        while pos < len(rel):
            t = int(rel[pos]["date_ix"])
            end = pos + 1
            while end < len(rel) and int(rel[end]["date_ix"]) == t:
                end += 1
            if refresh is not None:
                for key, row in refresh.get(t, ()):
                    active[key] = row
            block = rel[pos:end]
            aa, bb = block["a"].astype(np.intp), block["b"].astype(np.intp)
            ra, rb = response[t, aa], response[t, bb]
            muab = block["mu_ab"].astype(np.float64) if "mu_ab" in rel.dtype.names else block["mu_n1_ab"].astype(np.float64)
            muba = block["mu_ba"].astype(np.float64) if "mu_ba" in rel.dtype.names else block["mu_n1_ba"].astype(np.float64)
            sa, sb = block["ps0_a"].astype(np.float64), block["ps0_b"].astype(np.float64)
            dab, dba = rb - muab, ra - muba
            a3[pos:end] = np.column_stack((dab, dab / sb, dba, dba / sa))
            if candidate_kind(candidate) == "r4":
                aligned = state[pos:end]
                state_ok = np.ones(len(block), bool)
            else:
                rows = [active.get(int(a) * 750 + int(b)) for a, b in zip(aa, bb)]
                state_ok = np.array([x is not None for x in rows])
                aligned = np.empty(len(block), state.dtype)
                if np.any(state_ok): aligned[state_ok] = np.array([x for x in rows if x is not None], dtype=state.dtype)
            for hz, h in enumerate(HORIZONS):
                qix = np.arange(t + 1, t + h + 1)
                if qix[-1] >= len(dates) or dates[qix[-1]] > partition_hi:
                    continue
                xa, xb = response[qix[:, None], aa[None, :]], response[qix[:, None], bb[None, :]]
                valid = state_ok & np.all(member[qix[:, None], aa] & member[qix[:, None], bb], axis=0) & np.all(np.isfinite(xa) & np.isfinite(xb), axis=0)
                for direction in (0, 1):
                    source, peer = (xa, xb) if direction == 0 else (xb, xa)
                    scale_peer, scale_source = (sb, sa) if direction == 0 else (sa, sb)
                    gap = (muab - rb) if direction == 0 else (muba - ra)
                    excess = dba if direction == 0 else dab
                    peer_sum, source_sum = peer.sum(axis=0), source.sum(axis=0)
                    mu_path = np.full_like(peer, np.nan)
                    if np.any(state_ok):
                        if candidate_kind(candidate) == "static":
                            p = aligned["params"]
                            kind = aligned["kind"].astype(int)
                            if direction == 0:
                                alpha, beta = p[:, 0], p[:, 1]
                            else:
                                alpha, beta = p[:, 5], p[:, 6]
                            plain = kind <= 2
                            mu_path[:, plain] = alpha[plain] + beta[plain] * source[:, plain]
                            fact = ~plain & state_ok
                            if np.any(fact):
                                fca = p[fact, 15][None, :] + p[fact, 16][None, :] * market[qix, None]
                                fcb = p[fact, 18][None, :] + p[fact, 19][None, :] * market[qix, None]
                                mi = kind[fact] == 4
                                if np.any(mi):
                                    loc = np.flatnonzero(fact)[mi]; ga = industry[qix[:, None], aa[loc]]; gb = industry[qix[:, None], bb[loc]]
                                    ca = ind_count[qix[:, None], ga] - 1; cb = ind_count[qix[:, None], gb] - 1
                                    sxa = ind_sum[qix[:, None], ga] - xa[:, loc]; sxb = ind_sum[qix[:, None], gb] - xb[:, loc]
                                    same = ga == gb; ca -= same; cb -= same; sxa -= np.where(same, xb[:, loc], 0); sxb -= np.where(same, xa[:, loc], 0)
                                    qa = np.where(ca > 0, sxa / ca, np.nan); qb = np.where(cb > 0, sxb / cb, np.nan)
                                    fca[:, mi] += p[loc, 17][None, :] * qa; fcb[:, mi] += p[loc, 20][None, :] * qb
                                if direction == 0: mu_path[:, fact] = fcb + p[fact, 0][None, :] + p[fact, 1][None, :] * (source[:, fact] - fca)
                                else: mu_path[:, fact] = fca + p[fact, 5][None, :] + p[fact, 6][None, :] * (source[:, fact] - fcb)
                        elif candidate_kind(candidate) == "r3":
                            p = aligned["params"]
                            alpha, beta = (p[:, 6], p[:, 7]) if direction == 0 else (p[:, 13], p[:, 14])
                            mu_path[:] = alpha + beta * source
                        else:
                            alpha, beta = (aligned["alpha_ab"], aligned["beta_ab"]) if direction == 0 else (aligned["alpha_ba"], aligned["beta_ba"])
                            mu_path[:] = alpha + beta * source
                    vals = np.column_stack((
                        np.sign(gap) * peer_sum / scale_peer,
                        -np.sign(excess) * source_sum / scale_source,
                        np.abs(gap - peer_sum) / scale_peer,
                        (gap - peer_sum) / scale_peer,
                        np.median(np.abs(peer - mu_path), axis=0) / scale_peer,
                    ))
                    vals[~valid] = np.nan
                    a5[pos:end, direction, hz] = vals
                    available[direction, hz] += np.isfinite(vals).sum(axis=0)
            pos = end
        a3.flush(); a5.flush(); del a3, a5
        os.replace(a3_path.with_suffix(".tmp.npy"), a3_path)
        os.replace(a5_path.with_suffix(".tmp.npy"), a5_path)
        record = {
            "candidate": candidate, "partition": label, "rows": int(len(rel)),
            "ancestor_relationship_sha256": meta["sha256"], "ancestor_state_sha256": sha(state_path),
            "a3_sha256": sha(a3_path), "a5_sha256": sha(a5_path),
            "a3_fields": A3_FIELDS, "a5_shape": ["row", "direction_ab_ba", "O1_O5_O10_O20", "RT0_RT1_RT2ABS_RT2SIGNED_RT3"],
            "available_counts": available.tolist(), "of4_accessed": False, "held_out_accessed": False,
        }
        marker.write_text(json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        summary.append(record)
        print(json.dumps({"candidate": candidate, "partition": label, "rows": len(rel), "status": "COMPLETE"}), flush=True)
    if not args.candidate and not args.partition:
        (OUT_ROOT / "summary.json").write_text(json.dumps({
            "schema": "V1-INNER-A3-A5-1.0", "status": "IMMUTABLE_COMPLETE", "partitions": summary,
            "input_sha256": EXPECTED_INPUT, "relationship_manifest": manifest["manifest_id"],
            "rt3_manifest": "V1-RT3-RELATIONSHIP-STATE-AUGMENTATION-1.0",
            "empirical_interpretation": "NONE_DURING_MATERIALIZATION", "of4_accessed": False, "held_out_accessed": False,
        }, sort_keys=True, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
