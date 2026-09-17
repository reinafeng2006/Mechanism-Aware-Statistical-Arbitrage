"""Execute frozen V1 R3 N0/N1 on the checksum-bound 2015-2019 inner input."""
from __future__ import annotations

import hashlib, json, math, os, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
for dep in (ROOT/"data/qa_work/v1/phase1/deps_numba",ROOT/"data/qa_work/v1/phase1/deps"): sys.path.insert(0,str(dep))
import numpy as np  # noqa: E402
from numba import njit,prange,set_num_threads  # noqa: E402
from scipy.optimize import minimize  # noqa: E402

INPUT=ROOT/"data/qa_work/v1/phase1/inner_input_v1.npz"
OUT=ROOT/"data/qa_work/v1/phase1/inner_outputs_v2/relationships/V1-R3-252M"
EXPECTED="360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"
DT=np.dtype([("date_ix","<u2"),("a","<u2"),("b","<u2"),("support","<u2"),("stratum","u1"),("state","u1"),
             ("mu_n1_ab","<f4"),("mu_n1_ba","<f4"),("mu_n0_ab","<f4"),("mu_n0_ba","<f4"),
             ("ps0_a","<f4"),("ps0_b","<f4"),("ps1_a","<f4"),("ps1_b","<f4"),
             ("predsd_ab","<f4"),("predsd_ba","<f4")])

def sha(p:Path)->str:
 h=hashlib.sha256()
 with p.open("rb") as f:
  for c in iter(lambda:f.read(8<<20),b""):h.update(c)
 return h.hexdigest().upper()

@njit(cache=True)
def med(v,n):
 x=np.sort(v[:n].copy());m=n//2
 return x[m] if n%2 else .5*(x[m-1]+x[m])

@njit(cache=True)
def scales(v,n):
 if n<2:return np.nan,np.nan
 m=med(v,n);d=np.empty(n);avg=0.
 for i in range(n):d[i]=abs(v[i]-m);avg+=v[i]
 avg/=n;ss=0.
 for i in range(n):ss+=(v[i]-avg)**2
 a=1.4826*med(d,n);s=math.sqrt(ss/(n-1))
 return (a if math.isfinite(a) and a!=0 else np.nan),(s if math.isfinite(s) and s!=0 else np.nan)

@njit(parallel=True,cache=True)
def stats(pairs,t,h,r,member):
 out=np.full((len(pairs),16),np.nan)
 for z in prange(len(pairs)):
  a=int(pairs[z,0]);b=int(pairs[z,1]);xa=np.empty(h);xb=np.empty(h);n=0;q=t-1
  while q>=0 and n<h:
   if member[q,a] and member[q,b] and math.isfinite(r[q,a]) and math.isfinite(r[q,b]):xa[n]=r[q,a];xb[n]=r[q,b];n+=1
   q-=1
  if n<h:continue
  p0a,p1a=scales(xa,n);p0b,p1b=scales(xb,n)
  if not(math.isfinite(p0a) and math.isfinite(p0b)):continue
  sx=np.sum(xa);sy=np.sum(xb);sxx=np.sum(xa*xa);syy=np.sum(xb*xb);sxy=np.sum(xa*xb)
  out[z,0]=n;out[z,1]=sx;out[z,2]=sy;out[z,3]=sxx;out[z,4]=syy;out[z,5]=sxy
  out[z,6]=p0a;out[z,7]=p0b;out[z,8]=p1a;out[z,9]=p1b
 return out

def ols_fixed(s:np.ndarray,direction:int):
 n=s[:,0];sx=s[:,1] if direction==0 else s[:,2];sy=s[:,2] if direction==0 else s[:,1]
 sxx=s[:,3] if direction==0 else s[:,4];syy=s[:,4] if direction==0 else s[:,3];sxy=s[:,5]
 A=np.array([[n.sum(),sx.sum()],[sx.sum(),sxx.sum()]])
 c=np.array([sy.sum(),sxy.sum()]);beta=np.linalg.solve(A,c)
 yy=syy.sum();sse=yy-2*beta@c+beta@A@beta;df=n.sum()-2
 return beta,max(0.,float(sse/df)),A,c,yy

def reml_fit(s:np.ndarray,direction:int):
 n=s[:,0];sx=s[:,1] if direction==0 else s[:,2];sy=s[:,2] if direction==0 else s[:,1]
 sxx=s[:,3] if direction==0 else s[:,4];syy=s[:,4] if direction==0 else s[:,3];sxy=s[:,5]
 A=np.empty((len(s),2,2));A[:,0,0]=n;A[:,0,1]=sx;A[:,1,0]=sx;A[:,1,1]=sxx
 c=np.column_stack((sy,sxy));yy=syy
 beta0,r0,_,_,_=ols_fixed(s,direction)
 pair_beta=np.empty((len(s),2));pair_sse=np.empty(len(s));valid=np.ones(len(s),bool)
 for k in range(len(s)):
  try:
   pair_beta[k]=np.linalg.solve(A[k],c[k]);pair_sse[k]=yy[k]-2*pair_beta[k]@c[k]+pair_beta[k]@A[k]@pair_beta[k]
  except np.linalg.LinAlgError:valid[k]=False
 if valid.sum()<2 or not np.isfinite(r0) or r0<0:return None
 cov=np.cov(pair_beta[valid].T,ddof=1);cov=np.asarray(cov,float)
 w,v=np.linalg.eigh((cov+cov.T)/2);cov=(v*np.maximum(w,0.))@v.T
 l00=math.sqrt(max(cov[0,0],0.));l10=(cov[1,0]/l00 if l00>0 else 0.);l11=math.sqrt(max(cov[1,1]-l10*l10,0.))
 start=np.array([l00,l10,l11,max(r0,0.)])
 def pieces(theta):
  L=np.array([[theta[0],0.],[theta[1],theta[2]]]);R=theta[3]
  if not np.isfinite(R) or R<=0:return None
  AL=A@L;B=np.eye(2)[None,:,:]+np.einsum('ji,pjk->pik',L,AL)/R
  det=B[:,0,0]*B[:,1,1]-B[:,0,1]*B[:,1,0]
  if np.any(det<=0)|np.any(~np.isfinite(det)):return None
  inv=np.empty_like(B);inv[:,0,0]=B[:,1,1]/det;inv[:,1,1]=B[:,0,0]/det;inv[:,0,1]=-B[:,0,1]/det;inv[:,1,0]=-B[:,1,0]/det
  middle=np.einsum('pij,pjk,pkl->pil',AL,inv,np.transpose(AL,(0,2,1)))
  xvix=A/R-middle/(R*R)
  ltc=c@L
  xvic=c/R-np.einsum('pij,pjk,pk->pi',AL,inv,ltc)/(R*R)
  yviy=yy/R-np.einsum('pi,pij,pj->p',ltc,inv,ltc)/(R*R)
  M=xvix.sum(0);vsum=xvic.sum(0)
  try:beta=np.linalg.solve(M,vsum)
  except np.linalg.LinAlgError:return None
  sign,ldm=np.linalg.slogdet(M)
  if sign<=0:return None
  quad=yviy.sum()-2*beta@vsum+beta@M@beta
  val=.5*(np.sum(n*np.log(R)+np.log(det))+ldm+quad+(n.sum()-2)*np.log(2*np.pi))
  return val,beta,L,inv,R
 def obj(theta):
  p=pieces(theta);return np.inf if p is None or not np.isfinite(p[0]) else p[0]
 res=minimize(obj,start,method='L-BFGS-B',bounds=((0,None),(None,None),(0,None),(0,None)),options={'maxiter':1000,'ftol':1e-8})
 p=pieces(res.x)
 if not res.success or p is None:return None
 _,beta,L,inv,R=p;post=np.einsum('ij,pjk,kl->pil',L,inv,L.T)
 resid=c-np.einsum('pij,j->pi',A,beta);blup=np.einsum('pij,pj->pi',post,resid)/R
 boundary=bool(res.x[0]==0 or res.x[2]==0 or res.x[3]==0)
 return beta,blup,post,R,boundary

def pairs(mask):
 ids=np.flatnonzero(mask);i,j=np.triu_indices(len(ids),1)
 return np.column_stack((ids[i],ids[j])).astype(np.int16)

def main():
 set_num_threads(max(1,(os.cpu_count() or 4)-2))
 if sha(INPUT)!=EXPECTED:raise RuntimeError('input checksum mismatch')
 d=np.load(INPUT,allow_pickle=False);dates=np.char.decode(d['dates']);r=d['response'];member=d['pair_member'];ind=d['industry']
 OUT.mkdir(parents=True,exist_ok=True);cache={};active=-1
 periods=[(f'{y}H{s}',f'{y}{"0101" if s==1 else "0701"}',f'{y}{"0630" if s==1 else "1231"}') for y in range(2015,2020) for s in (1,2)]
 for label,lo,hi in periods:
  final=OUT/f'{label}.npy';marker=OUT/f'{label}.complete.json';write=not(final.exists() or marker.exists())
  if not write and not(final.exists() and marker.exists() and sha(final)==json.loads(marker.read_text())['sha256']):raise RuntimeError('no-overwrite conflict')
  chunks=[];started=time.perf_counter()
  for t in np.flatnonzero((dates>=lo)&(dates<=hi)):
   pp=pairs(member[t]);key=int(dates[t][:6]);ids=(pp[:,0].astype(np.int32)*r.shape[1]+pp[:,1]).astype(np.int32)
   if key!=active:
    st=stats(pp,int(t),252,r,member);ok=np.isfinite(st[:,0]);new={}
    strata=np.where((ind[t,pp[:,0]]==34)&(ind[t,pp[:,1]]==34),0,np.where((ind[t,pp[:,0]]==35)&(ind[t,pp[:,1]]==35),1,2))
    for g in (0,1,2):
     loc=np.flatnonzero(ok&(strata==g))
     if len(loc)<2:continue
     ss=st[loc]
     fits=[reml_fit(ss,dn) for dn in (0,1)]
     if any(x is None for x in fits):continue
     n0=[ols_fixed(ss,dn)[0] for dn in (0,1)]
     for q,pos in enumerate(loc):
      row=np.full(20,np.nan);row[0]=g;row[1]=st[pos,0];row[2:6]=st[pos,6:10]
      for dn,base in ((0,6),(1,13)):
       beta,blup,post,R,boundary=fits[dn];coef=beta+blup[q]
       row[base]=coef[0];row[base+1]=coef[1];row[base+2]=R;row[base+3]=post[q,0,0];row[base+4]=post[q,0,1];row[base+5]=post[q,1,1];row[base+6]=1. if boundary else 0.
      new[int(ids[pos])]=(row,n0[0].copy(),n0[1].copy())
    cache=new;active=key
   if not write:continue
   recs=[]
   for pos,k in enumerate(ids.tolist()):
    item=cache.get(int(k))
    if item is None:continue
    row,n0ab,n0ba=item;a=int(pp[pos,0]);b=int(pp[pos,1]);ra=r[t,a];rb=r[t,b]
    if not(math.isfinite(ra) and math.isfinite(rb)):continue
    pab=math.sqrt(max(0.,row[8]+row[9]+2*ra*row[10]+ra*ra*row[11]))
    pba=math.sqrt(max(0.,row[15]+row[16]+2*rb*row[17]+rb*rb*row[18]))
    recs.append((t,a,b,int(row[1]),int(row[0]),1|(2 if row[12] or row[19] else 0),row[6]+row[7]*ra,row[13]+row[14]*rb,n0ab[0]+n0ab[1]*ra,n0ba[0]+n0ba[1]*rb,row[2],row[3],row[4],row[5],pab,pba))
   if recs:chunks.append(np.array(recs,dtype=DT))
  if not write:continue
  arr=np.concatenate(chunks) if chunks else np.empty(0,DT);tmp=final.with_suffix('.tmp.npy');np.save(tmp,arr,allow_pickle=False);os.replace(tmp,final)
  meta={'candidate':'V1-R3-252M','partition':label,'rows':len(arr),'sha256':sha(final),'input_sha256':EXPECTED,'elapsed_seconds':time.perf_counter()-started,'hyperparameter_uncertainty':'OMITTED_LABELLED','of4_accessed':False,'held_out_accessed':False}
  marker.write_text(json.dumps(meta,sort_keys=True,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:meta[k] for k in ('candidate','partition','rows','sha256','elapsed_seconds')}),flush=True)

def augment_state():
 set_num_threads(max(1,(os.cpu_count() or 4)-2))
 if sha(INPUT)!=EXPECTED:raise RuntimeError('input checksum mismatch')
 d=np.load(INPUT,allow_pickle=False);dates=np.char.decode(d['dates']);r=d['response'];member=d['pair_member'];ind=d['industry']
 state_root=ROOT/'data/qa_work/v1/phase1/rt3_state_v1/V1-R3-252M';state_root.mkdir(parents=True,exist_ok=True)
 sdt=np.dtype([('date_ix','<u2'),('a','<u2'),('b','<u2'),('stratum','u1'),('state','u1'),('params','<f8',(24,))])
 cache={};active=-1;periods=[(f'{y}H{s}',f'{y}{"0101" if s==1 else "0701"}',f'{y}{"0630" if s==1 else "1231"}') for y in range(2015,2020) for s in (1,2)]
 summary=[]
 for label,lo,hi in periods:
  final=state_root/f'{label}.npy';marker=state_root/f'{label}.complete.json'
  if final.exists() or marker.exists():
   if not(final.exists() and marker.exists()):raise RuntimeError(f'incomplete state checkpoint V1-R3-252M/{label}')
   meta=json.loads(marker.read_text(encoding='utf-8'))
   valid=(meta.get('candidate')=='V1-R3-252M' and meta.get('partition')==label and meta.get('equivalence')=='PASS_EXACT' and
          meta.get('shared_field_mismatches')==0 and sha(final)==meta.get('sha256') and sha(OUT/f'{label}.npy')==meta.get('ancestor_sha256'))
   if not valid:raise RuntimeError(f'state checkpoint validation failed V1-R3-252M/{label}')
   summary.append(meta);continue
  original=np.load(OUT/f'{label}.npy',allow_pickle=False,mmap_mode='r');cursor=0;state_chunks=[]
  for t in np.flatnonzero((dates>=lo)&(dates<=hi)):
   pp=pairs(member[t]);key=int(dates[t][:6]);ids=(pp[:,0].astype(np.int32)*r.shape[1]+pp[:,1]).astype(np.int32)
   if key!=active:
    st=stats(pp,int(t),252,r,member);ok=np.isfinite(st[:,0]);new={};strata=np.where((ind[t,pp[:,0]]==34)&(ind[t,pp[:,1]]==34),0,np.where((ind[t,pp[:,0]]==35)&(ind[t,pp[:,1]]==35),1,2))
    srows=[]
    for g in (0,1,2):
     loc=np.flatnonzero(ok&(strata==g))
     if len(loc)<2:continue
     ss=st[loc];fits=[reml_fit(ss,dn) for dn in (0,1)]
     if any(x is None for x in fits):continue
     n0=[ols_fixed(ss,dn)[0] for dn in (0,1)]
     for q,pos in enumerate(loc):
      row=np.full(20,np.nan);row[0]=g;row[1]=st[pos,0];row[2:6]=st[pos,6:10]
      for dn,base in ((0,6),(1,13)):
       beta,blup,post,R,boundary=fits[dn];coef=beta+blup[q];row[base]=coef[0];row[base+1]=coef[1];row[base+2]=R;row[base+3]=post[q,0,0];row[base+4]=post[q,0,1];row[base+5]=post[q,1,1];row[base+6]=1. if boundary else 0.
      new[int(ids[pos])]=(row,n0[0].copy(),n0[1].copy());srows.append((t,int(pp[pos,0]),int(pp[pos,1]),g,1|(2 if row[12] or row[19] else 0),np.r_[row,n0[0],n0[1]]))
    if srows:state_chunks.append(np.array(srows,dtype=sdt))
    cache=new;active=key
   recs=[]
   for pos,k in enumerate(ids.tolist()):
    item=cache.get(int(k))
    if item is None:continue
    row,n0ab,n0ba=item;a=int(pp[pos,0]);b=int(pp[pos,1]);ra=r[t,a];rb=r[t,b]
    if not(math.isfinite(ra) and math.isfinite(rb)):continue
    pab=math.sqrt(max(0.,row[8]+row[9]+2*ra*row[10]+ra*ra*row[11]));pba=math.sqrt(max(0.,row[15]+row[16]+2*rb*row[17]+rb*rb*row[18]))
    recs.append((t,a,b,int(row[1]),int(row[0]),1|(2 if row[12] or row[19] else 0),row[6]+row[7]*ra,row[13]+row[14]*rb,n0ab[0]+n0ab[1]*ra,n0ba[0]+n0ba[1]*rb,row[2],row[3],row[4],row[5],pab,pba))
   if recs:
    rec=np.array(recs,dtype=DT);old=original[cursor:cursor+len(rec)]
    for name in DT.names:
     if rec[name].dtype.kind=='f':same=np.array_equal(rec[name],old[name],equal_nan=True)
     else:same=np.array_equal(rec[name],old[name])
     if not same:raise RuntimeError(f'R3 equivalence mismatch {label}/{name}')
    cursor+=len(rec)
  if cursor!=len(original):raise RuntimeError(f'R3 row mismatch {label}')
  arr=np.concatenate(state_chunks) if state_chunks else np.empty(0,sdt);tmp=final.with_suffix('.tmp.npy');np.save(tmp,arr,allow_pickle=False);os.replace(tmp,final)
  meta={'candidate':'V1-R3-252M','partition':label,'rows':len(arr),'sha256':sha(final),'ancestor_sha256':sha(OUT/f'{label}.npy'),'shared_rows_verified':cursor,'shared_field_mismatches':0,'equivalence':'PASS_EXACT','of4_accessed':False,'held_out_accessed':False};marker.write_text(json.dumps(meta,sort_keys=True,indent=2)+'\n',encoding='utf-8');summary.append(meta);print(json.dumps({'candidate':'V1-R3-252M','partition':label,'state_rows':len(arr),'equivalence':'PASS_EXACT','sha256':meta['sha256']}),flush=True)
 (state_root/'summary.json').write_text(json.dumps({'schema':'RT3-STATE-R3-1.0','partitions':summary},sort_keys=True,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
 if '--augment-state' in sys.argv:augment_state()
 else:main()
