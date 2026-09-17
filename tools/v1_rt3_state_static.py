"""RT3-A deterministic replay for frozen R0/R1 static candidates.

Creates refresh-state companions only. Existing relationship outputs are opened
read-only and every replayed common field is compared exactly before a state
partition is committed. No research values are printed.
"""
from __future__ import annotations

import hashlib, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import v1_phase1_inner_relationships as rel  # noqa:E402
import numpy as np  # noqa:E402

OUT=ROOT/'data/qa_work/v1/phase1/rt3_state_v1'
REL=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/relationships'
STATE=np.dtype([('date_ix','<u2'),('a','<u2'),('b','<u2'),('support','<u2'),('kind','u1'),('params','<f8',(22,))])

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(8<<20),b''):h.update(c)
 return h.hexdigest().upper()

def equal_fields(a,b):
 if a.dtype!=b.dtype or a.shape!=b.shape:return False,'schema_or_shape'
 for n in a.dtype.names:
  x,y=a[n],b[n]
  if x.dtype.kind=='f':
   if not np.array_equal(x,y,equal_nan=True):return False,n
  elif not np.array_equal(x,y):return False,n
 return True,''

def main():
 if rel.sha(rel.INPUT)!=rel.EXPECTED_INPUT_HASH:raise RuntimeError('input checksum mismatch')
 d=np.load(rel.INPUT,allow_pickle=False);dates=np.char.decode(d['dates']);response=d['response'];member=d['pair_member'];market=d['benchmark_response'];industry=d['industry']
 if dates[-1]>'20191231':raise RuntimeError('role boundary exceeded')
 ind_sum=np.zeros((len(dates),36),np.float64);ind_count=np.zeros((len(dates),36),np.int16)
 for g in (34,35):
  m=(industry==g)&member&np.isfinite(response);ind_sum[:,g]=np.where(m,response,0.).sum(1);ind_count[:,g]=m.sum(1)
 week=rel.iso_week_keys(dates);month=np.array([int(x[:6]) for x in dates],np.int32)
 OUT.mkdir(parents=True,exist_ok=True);summary=[]
 periods=[(f'{y}H{s}',f'{y}{"0101" if s==1 else "0701"}',f'{y}{"0630" if s==1 else "1231"}') for y in range(2015,2020) for s in (1,2)]
 for cid,(h,cadence,kind) in rel.CANDIDATES.items():
  cdir=OUT/cid;cdir.mkdir(exist_ok=True);cache={};active=-1
  for label,lo,hi in periods:
   final=cdir/f'{label}.npy';marker=cdir/f'{label}.complete.json'
   if final.exists() or marker.exists():
    if not(final.exists() and marker.exists()):raise RuntimeError(f'incomplete state checkpoint {cid}/{label}')
    meta=json.loads(marker.read_text(encoding='utf-8'))
    valid=(meta.get('candidate')==cid and meta.get('partition')==label and meta.get('equivalence')=='PASS_EXACT' and
           meta.get('shared_field_mismatches')==0 and sha(final)==meta.get('sha256') and sha(REL/cid/f'{label}.npy')==meta.get('ancestor_sha256'))
    if not valid:raise RuntimeError(f'state checkpoint validation failed {cid}/{label}')
    summary.append(meta);continue
   original=np.load(REL/cid/f'{label}.npy',allow_pickle=False,mmap_mode='r');cursor=0;states=[];mismatch=0;bad=''
   for t in np.flatnonzero((dates>=lo)&(dates<=hi)):
    pairs=rel.pairs_for(member[t]);pkey=int(month[t] if cadence==2 else week[t]);keys=(pairs[:,0].astype(np.int32)*response.shape[1]+pairs[:,1]).astype(np.int32)
    params=np.full((len(pairs),22),np.nan,np.float64)
    if pkey!=active:
     fitted=rel.fit_batch(pairs,int(t),h,kind,response,member,market,industry,ind_sum,ind_count);cache={int(k):row.copy() for k,row in zip(keys.tolist(),fitted)};active=pkey;params[:]=fitted
     okstate=np.isfinite(fitted[:,0]);sr=np.empty(int(okstate.sum()),STATE);sr['date_ix']=t;sr['a']=pairs[okstate,0];sr['b']=pairs[okstate,1];sr['support']=fitted[okstate,21].astype(np.uint16);sr['kind']=kind;sr['params']=fitted[okstate];states.append(sr)
    else:
     for pos,key in enumerate(keys.tolist()):
      item=cache.get(int(key))
      if item is not None:params[pos]=item
    vals=rel.materialize_static(pairs,int(t),h,kind,params,response,member,market,industry,ind_sum,ind_count);ok=np.isfinite(vals[:,0])&np.isfinite(vals[:,1])
    if not np.any(ok):continue
    pp=pairs[ok];vv=vals[ok];rec=np.empty(len(pp),rel.EVENT_DTYPE);rec['date_ix']=t;rec['a']=pp[:,0];rec['b']=pp[:,1];rec['support']=vv[:,9].astype(np.uint16);rec['state']=1;rec['representation']=vv[:,8];rec['mu_ab']=vv[:,0];rec['mu_ba']=vv[:,1];rec['ps0_a']=vv[:,2];rec['ps0_b']=vv[:,3];rec['ps1_a']=vv[:,4];rec['ps1_b']=vv[:,5];rec['predsd_ab']=vv[:,6];rec['predsd_ba']=vv[:,7]
    old=original[cursor:cursor+len(rec)];same,bad=equal_fields(rec,old)
    if not same:mismatch+=1;break
    cursor+=len(rec)
   if mismatch or cursor!=len(original):raise RuntimeError(f'equivalence mismatch {cid}/{label} field={bad} blocks={mismatch} replay={cursor} original={len(original)}')
   arr=np.concatenate(states) if states else np.empty(0,STATE);tmp=final.with_suffix('.tmp.npy');np.save(tmp,arr,allow_pickle=False);os.replace(tmp,final)
   meta={'candidate':cid,'partition':label,'rows':int(len(arr)),'sha256':sha(final),'ancestor_sha256':sha(REL/cid/f'{label}.npy'),'shared_field_mismatches':0,'shared_rows_verified':int(cursor),'equivalence':'PASS_EXACT','of4_accessed':False,'held_out_accessed':False};marker.write_text(json.dumps(meta,sort_keys=True,indent=2)+'\n',encoding='utf-8');summary.append(meta)
   print(json.dumps({'candidate':cid,'partition':label,'state_rows':len(arr),'equivalence':'PASS_EXACT','sha256':meta['sha256']}),flush=True)
 (OUT/'static_summary.json').write_text(json.dumps({'schema':'RT3-STATE-STATIC-1.0','partitions':summary},sort_keys=True,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
