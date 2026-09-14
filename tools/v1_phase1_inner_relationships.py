"""Execute frozen V1 R0/R1 relationship candidates on 2015-2019 inner data.

The runner reads the checksum-bound V1 inner input only. It emits compact,
partitioned event-time records for every candidate-eligible unordered pair and
preserves both directions in each record. It never reads OF4 or held-out data,
does not screen pairs, and does not interpret model outputs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for dep in (ROOT / "data/qa_work/v1/phase1/deps_numba", ROOT / "data/qa_work/v1/phase1/deps"):
    sys.path.insert(0, str(dep))

import numpy as np  # noqa: E402
from numba import njit, prange, set_num_threads  # noqa: E402

INPUT = ROOT / "data/qa_work/v1/phase1/inner_input_v1.npz"
INPUT_MANIFEST = ROOT / "data/manifests/V1_PHASE1_INNER_INPUT.json"
OUT = ROOT / "data/qa_work/v1/phase1/inner_outputs_v2/relationships"
PUBLIC_MANIFEST = ROOT / "data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json"
EXPECTED_INPUT_HASH = "360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"

CANDIDATES = {
    "V1-R0D-252M": (252, 2, 0),
    "V1-R0C-126W": (126, 1, 1),
    "V1-R0L-126W": (126, 1, 2),
    "V1-R1M-126W": (126, 1, 3),
    "V1-R1MI-126W": (126, 1, 4),
}

EVENT_DTYPE = np.dtype([
    ("date_ix", "<u2"), ("a", "<u2"), ("b", "<u2"),
    ("support", "<u2"), ("state", "u1"),
    ("representation", "<f4"),
    ("mu_ab", "<f4"), ("mu_ba", "<f4"),
    ("ps0_a", "<f4"), ("ps0_b", "<f4"),
    ("ps1_a", "<f4"), ("ps1_b", "<f4"),
    ("predsd_ab", "<f4"), ("predsd_ba", "<f4"),
])


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


@njit(cache=True)
def _median(values: np.ndarray, n: int) -> float:
    x = np.sort(values[:n].copy())
    m = n // 2
    return x[m] if n % 2 else 0.5 * (x[m - 1] + x[m])


@njit(cache=True)
def _scales(values: np.ndarray, n: int) -> tuple[float, float]:
    if n < 2:
        return np.nan, np.nan
    med = _median(values, n)
    dev = np.empty(n, np.float64)
    ss = 0.0
    mean = 0.0
    for q in range(n):
        mean += values[q]
        dev[q] = abs(values[q] - med)
    mean /= n
    for q in range(n):
        z = values[q] - mean
        ss += z * z
    mad = 1.4826 * _median(dev, n)
    sd = math.sqrt(ss / (n - 1))
    if not math.isfinite(mad) or mad == 0.0:
        mad = np.nan
    if not math.isfinite(sd) or sd == 0.0:
        sd = np.nan
    return mad, sd


@njit(cache=True)
def _ols(x: np.ndarray, y: np.ndarray, n: int) -> tuple[float, float, float, float, bool]:
    if n < 3:
        return np.nan, np.nan, np.nan, np.nan, False
    sx = sy = sxx = sxy = 0.0
    for q in range(n):
        xv, yv = x[q], y[q]
        sx += xv; sy += yv; sxx += xv * xv; sxy += xv * yv
    mx, my = sx / n, sy / n
    sxxc = sxx - sx * sx / n
    if not math.isfinite(sxxc) or sxxc <= 0.0:
        return np.nan, np.nan, np.nan, np.nan, False
    beta = (sxy - sx * sy / n) / sxxc
    alpha = my - beta * mx
    sse = 0.0
    for q in range(n):
        e = y[q] - alpha - beta * x[q]
        sse += e * e
    if n - 2 <= 0:
        return np.nan, np.nan, np.nan, np.nan, False
    var = sse / (n - 2)
    if not (math.isfinite(alpha) and math.isfinite(beta) and math.isfinite(var)) or var < 0.0:
        return np.nan, np.nan, np.nan, np.nan, False
    return alpha, beta, var, sxxc, True


@njit(cache=True)
def _solve3(a: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, bool]:
    det = (a[0,0]*(a[1,1]*a[2,2]-a[1,2]*a[2,1])
           - a[0,1]*(a[1,0]*a[2,2]-a[1,2]*a[2,0])
           + a[0,2]*(a[1,0]*a[2,1]-a[1,1]*a[2,0]))
    if not math.isfinite(det) or abs(det) <= 1e-30:
        return np.empty(3, np.float64), False
    out = np.linalg.solve(a, b)
    return out, bool(np.all(np.isfinite(out)))


@njit(cache=True)
def _factor_fit(x: np.ndarray, m: np.ndarray, q: np.ndarray, n: int, use_industry: bool) -> tuple[np.ndarray, bool]:
    if use_industry:
        if n < 4:
            return np.empty(3, np.float64), False
        ztz = np.zeros((3, 3), np.float64); zty = np.zeros(3, np.float64)
        for p in range(n):
            z0, z1, z2 = 1.0, m[p], q[p]
            zty[0] += x[p]; zty[1] += z1*x[p]; zty[2] += z2*x[p]
            ztz[0,0] += 1.0; ztz[0,1] += z1; ztz[0,2] += z2
            ztz[1,1] += z1*z1; ztz[1,2] += z1*z2; ztz[2,2] += z2*z2
        ztz[1,0]=ztz[0,1]; ztz[2,0]=ztz[0,2]; ztz[2,1]=ztz[1,2]
        return _solve3(ztz, zty)
    if n < 3:
        return np.empty(3, np.float64), False
    alpha, beta, _, _, ok = _ols(m, x, n)
    out = np.zeros(3, np.float64); out[0]=alpha; out[1]=beta
    return out, ok


@njit(cache=True)
def _period_key(date_int: int, cadence: int) -> int:
    if cadence == 2:
        return date_int // 100
    # Gregorian ISO week key, supplied by caller through integer key array for weekly.
    return date_int


@njit(parallel=True, cache=True)
def fit_batch(pairs: np.ndarray, t: int, h: int, kind: int, response: np.ndarray,
              pair_member: np.ndarray, market: np.ndarray, industry: np.ndarray,
              ind_sum: np.ndarray, ind_count: np.ndarray) -> np.ndarray:
    n_pairs = pairs.shape[0]
    out = np.full((n_pairs, 22), np.nan, np.float64)
    for z in prange(n_pairs):
        a, b = int(pairs[z, 0]), int(pairs[z, 1])
        xa=np.empty(h,np.float64); xb=np.empty(h,np.float64); mm=np.empty(h,np.float64)
        qa=np.empty(h,np.float64); qb=np.empty(h,np.float64)
        n=0; qpos=t-1
        while qpos >= 0 and n < h:
            if pair_member[qpos,a] and pair_member[qpos,b]:
                va=response[qpos,a]; vb=response[qpos,b]
                if math.isfinite(va) and math.isfinite(vb):
                    if kind >= 3 and not math.isfinite(market[qpos]):
                        qpos -= 1; continue
                    if kind == 4:
                        ga=int(industry[qpos,a]); gb=int(industry[qpos,b])
                        ca=int(ind_count[qpos,ga]); cb=int(ind_count[qpos,gb])
                        sa=ind_sum[qpos,ga]; sb=ind_sum[qpos,gb]
                        ca -= 1; sa -= va
                        cb -= 1; sb -= vb
                        if ga == gb:
                            ca -= 1; sa -= vb; cb -= 1; sb -= va
                        if ca <= 0 or cb <= 0:
                            qpos -= 1; continue
                        qa[n]=sa/ca; qb[n]=sb/cb
                    xa[n]=va; xb[n]=vb; mm[n]=market[qpos]; n+=1
            qpos-=1
        if n < h:
            continue
        # reverse chronological order does not affect static estimators/path distance
        ps0a,ps1a=_scales(xa,n); ps0b,ps1b=_scales(xb,n)
        if not (math.isfinite(ps0a) and math.isfinite(ps0b)):
            continue
        representation=np.nan
        if kind == 0:
            ca=np.empty(n,np.float64); cb=np.empty(n,np.float64)
            sa=sb=0.0
            for p in range(n-1,-1,-1):
                sa+=xa[p]; sb+=xb[p]; ca[n-1-p]=sa; cb[n-1-p]=sb
            ma=_median(ca,n); mb=_median(cb,n)
            da=np.empty(n,np.float64); db=np.empty(n,np.float64)
            for p in range(n): da[p]=abs(ca[p]-ma); db[p]=abs(cb[p]-mb)
            sca=_median(da,n); scb=_median(db,n)
            if not (math.isfinite(sca) and math.isfinite(scb)) or sca==0.0 or scb==0.0:
                continue
            representation=0.0
            for p in range(n):
                d=(ca[p]-ma)/sca-(cb[p]-mb)/scb; representation+=d*d
            representation/=n
        elif kind == 1:
            aa,bb,_,sxx,ok=_ols(xa,xb,n)
            if not ok: continue
            ma=np.mean(xa[:n]); mb=np.mean(xb[:n]); syy=0.0; sxy=0.0
            for p in range(n): syy+=(xb[p]-mb)**2; sxy+=(xa[p]-ma)*(xb[p]-mb)
            if syy<=0.0: continue
            representation=sxy/math.sqrt(sxx*syy)
        if kind <= 2:
            aab,bab,vab,sxxa,oka=_ols(xa,xb,n)
            aba,bba,vba,sxxb,okb=_ols(xb,xa,n)
            if not (oka and okb): continue
            out[z,0]=aab; out[z,1]=bab; out[z,2]=vab; out[z,3]=sxxa; out[z,4]=np.mean(xa[:n])
            out[z,5]=aba; out[z,6]=bba; out[z,7]=vba; out[z,8]=sxxb; out[z,9]=np.mean(xb[:n])
        else:
            use_industry=kind==4
            fa,oka=_factor_fit(xa,mm,qa,n,use_industry)
            fb,okb=_factor_fit(xb,mm,qb,n,use_industry)
            if not (oka and okb): continue
            ua=np.empty(n,np.float64); ub=np.empty(n,np.float64)
            for p in range(n):
                ua[p]=xa[p]-fa[0]-fa[1]*mm[p]-(fa[2]*qa[p] if use_industry else 0.0)
                ub[p]=xb[p]-fb[0]-fb[1]*mm[p]-(fb[2]*qb[p] if use_industry else 0.0)
            cab,dab,vab,sxxa,oka=_ols(ua,ub,n)
            cba,dba,vba,sxxb,okb=_ols(ub,ua,n)
            if not (oka and okb): continue
            out[z,0]=cab; out[z,1]=dab; out[z,2]=vab; out[z,3]=sxxa; out[z,4]=np.mean(ua[:n])
            out[z,5]=cba; out[z,6]=dba; out[z,7]=vba; out[z,8]=sxxb; out[z,9]=np.mean(ub[:n])
            out[z,15]=fa[0]; out[z,16]=fa[1]; out[z,17]=fa[2]
            out[z,18]=fb[0]; out[z,19]=fb[1]; out[z,20]=fb[2]
        out[z,10]=representation; out[z,11]=ps0a; out[z,12]=ps0b
        out[z,13]=ps1a; out[z,14]=ps1b; out[z,21]=n
    return out


@njit(parallel=True, cache=True)
def materialize_static(pairs: np.ndarray, t: int, h: int, kind: int, params: np.ndarray,
                       response: np.ndarray, pair_member: np.ndarray, market: np.ndarray,
                       industry: np.ndarray, ind_sum: np.ndarray, ind_count: np.ndarray) -> np.ndarray:
    n_pairs=pairs.shape[0]
    out=np.full((n_pairs,10),np.nan,np.float64)
    for z in prange(n_pairs):
        a,b=int(pairs[z,0]),int(pairs[z,1])
        if not (math.isfinite(params[z,0]) and pair_member[t,a] and pair_member[t,b]): continue
        n=int(params[z,21]); ps0a=params[z,11]; ps0b=params[z,12]; ps1a=params[z,13]; ps1b=params[z,14]
        if n<h or not (math.isfinite(ps0a) and math.isfinite(ps0b)): continue
        ra=response[t,a]; rb=response[t,b]
        if not (math.isfinite(ra) and math.isfinite(rb)): continue
        if kind<=2:
            mu_ab=params[z,0]+params[z,1]*ra; mu_ba=params[z,5]+params[z,6]*rb
            ma=params[z,4]; mb=params[z,9]
            pab=math.sqrt(max(0.0,params[z,2]*(1.0+1.0/n+(ra-ma)**2/params[z,3])))
            pba=math.sqrt(max(0.0,params[z,7]*(1.0+1.0/n+(rb-mb)**2/params[z,8])))
            rep=params[z,10]
        else:
            if not math.isfinite(market[t]): continue
            qta=qtb=0.0
            if kind==4:
                ga=int(industry[t,a]); gb=int(industry[t,b]); ca=int(ind_count[t,ga])-1; cb=int(ind_count[t,gb])-1
                sa=ind_sum[t,ga]-ra; sb=ind_sum[t,gb]-rb
                if ga==gb: ca-=1; cb-=1; sa-=rb; sb-=ra
                if ca<=0 or cb<=0: continue
                qta=sa/ca; qtb=sb/cb
            fca=params[z,15]+params[z,16]*market[t]+params[z,17]*qta
            fcb=params[z,18]+params[z,19]*market[t]+params[z,20]*qtb
            ua=ra-fca; ub=rb-fcb
            mu_ab=fcb+params[z,0]+params[z,1]*ua; mu_ba=fca+params[z,5]+params[z,6]*ub
            pab=math.sqrt(max(0.0,params[z,2]*(1.0+1.0/n+(ua-params[z,4])**2/params[z,3])))
            pba=math.sqrt(max(0.0,params[z,7]*(1.0+1.0/n+(ub-params[z,9])**2/params[z,8])))
            rep=np.nan
        out[z,0]=mu_ab; out[z,1]=mu_ba; out[z,2]=ps0a; out[z,3]=ps0b
        out[z,4]=ps1a; out[z,5]=ps1b; out[z,6]=pab; out[z,7]=pba; out[z,8]=rep; out[z,9]=n
    return out


def pairs_for(mask: np.ndarray) -> np.ndarray:
    ids=np.flatnonzero(mask)
    if ids.size<2: return np.empty((0,2),np.int16)
    a,b=np.triu_indices(ids.size,1)
    return np.column_stack((ids[a],ids[b])).astype(np.int16,copy=False)


def iso_week_keys(dates: np.ndarray) -> np.ndarray:
    import datetime as dt
    return np.array([dt.date(int(d[:4]),int(d[4:6]),int(d[6:8])).isocalendar().year*100+
                     dt.date(int(d[:4]),int(d[4:6]),int(d[6:8])).isocalendar().week for d in dates],dtype=np.int32)


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--candidate",choices=sorted(CANDIDATES)); ap.add_argument("--threads",type=int,default=max(1,(os.cpu_count() or 4)-2)); args=ap.parse_args()
    set_num_threads(args.threads)
    if sha(INPUT)!=EXPECTED_INPUT_HASH: raise RuntimeError("inner input checksum mismatch")
    d=np.load(INPUT,allow_pickle=False)
    dates=np.char.decode(d["dates"]); response=d["response"]; member=d["pair_member"]; market=d["benchmark_response"]; industry=d["industry"]
    if dates[-1]>"20191231": raise RuntimeError("input role exceeds authorized 2019 boundary")
    ind_sum=np.zeros((len(dates),36),np.float64); ind_count=np.zeros((len(dates),36),np.int16)
    for g in (34,35):
        m=(industry==g)&member&np.isfinite(response); ind_sum[:,g]=np.where(m,response,0.0).sum(axis=1); ind_count[:,g]=m.sum(axis=1)
    week=iso_week_keys(dates); month=np.array([int(x[:6]) for x in dates],np.int32)
    selected=[args.candidate] if args.candidate else list(CANDIDATES)
    OUT.mkdir(parents=True,exist_ok=True)
    for cid in selected:
        h,cadence,kind=CANDIDATES[cid]; cdir=OUT/cid; cdir.mkdir(exist_ok=True)
        periods=[(f"{y}H{s}",f"{y}{'0101' if s==1 else '0701'}",f"{y}{'0630' if s==1 else '1231'}") for y in range(2015,2020) for s in (1,2)]
        cache={}; active_pkey=-1
        for label,lo,hi in periods:
            final=cdir/f"{label}.npy"; marker=cdir/f"{label}.complete.json"
            write_partition=True
            if final.exists() or marker.exists():
                if not (final.exists() and marker.exists() and sha(final)==json.loads(marker.read_text())["sha256"]): raise RuntimeError(f"incomplete/no-overwrite conflict {label}")
                write_partition=False
            pieces=[]; started=time.perf_counter()
            tids=np.flatnonzero((dates>=lo)&(dates<=hi))
            for t in tids:
                pairs=pairs_for(member[t])
                if not len(pairs): continue
                pkey=int(month[t] if cadence==2 else week[t])
                keys=(pairs[:,0].astype(np.int32)*response.shape[1]+pairs[:,1]).astype(np.int32)
                params=np.full((len(pairs),22),np.nan,np.float64)
                if pkey != active_pkey:
                    fitted=fit_batch(pairs,int(t),h,kind,response,member,market,industry,ind_sum,ind_count)
                    cache={int(k):row.copy() for k,row in zip(keys.tolist(),fitted)}
                    active_pkey=pkey
                    params[:]=fitted
                else:
                    for pos,key in enumerate(keys.tolist()):
                        item=cache.get(int(key))
                        if item is not None: params[pos]=item
                vals=materialize_static(pairs,int(t),h,kind,params,response,member,market,industry,ind_sum,ind_count)
                ok=np.isfinite(vals[:,0])&np.isfinite(vals[:,1])
                if not np.any(ok): continue
                pp=pairs[ok]; vv=vals[ok]; rec=np.empty(len(pp),EVENT_DTYPE)
                rec["date_ix"]=t; rec["a"]=pp[:,0]; rec["b"]=pp[:,1]; rec["support"]=vv[:,9].astype(np.uint16); rec["state"]=1
                rec["representation"]=vv[:,8]; rec["mu_ab"]=vv[:,0]; rec["mu_ba"]=vv[:,1]
                rec["ps0_a"]=vv[:,2]; rec["ps0_b"]=vv[:,3]; rec["ps1_a"]=vv[:,4]; rec["ps1_b"]=vv[:,5]
                rec["predsd_ab"]=vv[:,6]; rec["predsd_ba"]=vv[:,7]
                if write_partition: pieces.append(rec)
            if not write_partition:
                continue
            arr=np.concatenate(pieces) if pieces else np.empty(0,EVENT_DTYPE)
            tmp=final.with_suffix(".tmp.npy"); np.save(tmp,arr,allow_pickle=False); os.replace(tmp,final)
            meta={"candidate":cid,"partition":label,"rows":int(len(arr)),"sha256":sha(final),"input_sha256":EXPECTED_INPUT_HASH,"elapsed_seconds":time.perf_counter()-started,"of4_accessed":False,"held_out_accessed":False}
            marker.write_text(json.dumps(meta,sort_keys=True,indent=2)+"\n",encoding="utf-8")
            print(json.dumps({"candidate":cid,"partition":label,"rows":len(arr),"sha256":meta["sha256"],"elapsed_seconds":round(meta["elapsed_seconds"],2)}),flush=True)
    entries=[]
    for marker in sorted(OUT.glob("*/*.complete.json")):
        entries.append(json.loads(marker.read_text(encoding="utf-8")))
    manifest={"manifest_id":"V1-PHASE1-RELATIONSHIP-OUTPUTS-1.0","status":"IN_PROGRESS" if len(entries)<50 else "IMMUTABLE_COMPLETE","input_sha256":EXPECTED_INPUT_HASH,"partitions":entries,"candidate_universe":"PAIR-A_COMPLETE_PIT_ALL_PAIRS","date_role":"2015-2019_INNER_ONLY","of4_accessed":False,"held_out_accessed":False,"interpretation":"NONE_DURING_MATERIALIZATION"}
    PUBLIC_MANIFEST.write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n",encoding="utf-8")


if __name__=="__main__": main()
