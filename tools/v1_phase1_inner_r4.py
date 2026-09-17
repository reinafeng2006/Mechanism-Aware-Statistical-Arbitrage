"""Execute frozen V1 R4 CF-A on checksum-bound 2015-2019 inner data."""
from __future__ import annotations
import concurrent.futures,hashlib,json,math,os,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for dep in (ROOT/"data/qa_work/v1/phase1/deps_numba",ROOT/"data/qa_work/v1/phase1/deps"):sys.path.insert(0,str(dep))
import numpy as np  # noqa:E402
from numba import njit,prange,set_num_threads  # noqa:E402
from scipy.optimize import minimize  # noqa:E402
INPUT=ROOT/"data/qa_work/v1/phase1/inner_input_v1.npz";EXPECTED="360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916"
OUT=ROOT/"data/qa_work/v1/phase1/inner_outputs_v2/relationships/V1-R4-63D"
DT=np.dtype([("date_ix","<u2"),("a","<u2"),("b","<u2"),("support","<u2"),("state_ab","u1"),("state_ba","u1"),
             ("mu_ab","<f4"),("mu_ba","<f4"),("ps0_a","<f4"),("ps0_b","<f4"),("ps1_a","<f4"),("ps1_b","<f4"),
             ("predsd_ab","<f4"),("predsd_ba","<f4")])
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(8<<20),b''):h.update(c)
 return h.hexdigest().upper()
@njit(cache=True)
def med(v,n):
 x=np.sort(v[:n].copy());m=n//2
 return x[m] if n%2 else .5*(x[m-1]+x[m])
@njit(cache=True)
def scale(v,n):
 m=med(v,n);d=np.empty(n);avg=0.
 for i in range(n):d[i]=abs(v[i]-m);avg+=v[i]
 avg/=n;ss=0.
 for i in range(n):ss+=(v[i]-avg)**2
 a=1.4826*med(d,n);s=math.sqrt(ss/(n-1))
 return (a if math.isfinite(a) and a!=0 else np.nan),(s if math.isfinite(s) and s!=0 else np.nan)
@njit(parallel=True,cache=True)
def sequences(pairs,t,r,member):
 h=63;out=np.full((len(pairs),h,2),np.nan);meta=np.full((len(pairs),4),np.nan)
 for z in prange(len(pairs)):
  a=int(pairs[z,0]);b=int(pairs[z,1]);n=0;q=t-1
  while q>=0 and n<h:
   if member[q,a] and member[q,b] and math.isfinite(r[q,a]) and math.isfinite(r[q,b]):out[z,h-1-n,0]=r[q,a];out[z,h-1-n,1]=r[q,b];n+=1
   q-=1
  if n==h:
   meta[z,0],meta[z,2]=scale(out[z,:,0],h);meta[z,1],meta[z,3]=scale(out[z,:,1],h)
 return out,meta
def nll(theta,x,y,alpha,beta0,p0):
 q,r=float(theta[0]),float(theta[1]);beta=beta0;p=p0;loss=0.
 for xx,yy in zip(x,y):
  pp=p+q;v=xx*xx*pp+r
  if not np.isfinite(v) or v<=0:return np.inf
  e=yy-alpha-beta*xx;loss+=.5*(np.log(2*np.pi*v)+e*e/v);k=pp*xx/v;beta+=k*e;p=max(0.,(1-k*xx)*pp)
 return float(loss)
def fit_one(args):
 x,y=args;X=np.column_stack((np.ones(63),x))
 try:coef=np.linalg.solve(X.T@X,X.T@y)
 except np.linalg.LinAlgError:return (np.nan,)*7+(0,)
 e=y-X@coef;r0=float(e@e/61);den=float(np.sum((x-x.mean())**2))
 if not(np.isfinite(r0) and r0>=0 and den>0):return (np.nan,)*7+(0,)
 p0=r0/den
 res=minimize(nll,np.array([.01*r0,r0]),args=(x,y,float(coef[0]),float(coef[1]),p0),method='L-BFGS-B',bounds=((0,None),(0,None)),options={'maxiter':1000,'ftol':1e-8})
 if not(res.success and np.isfinite(res.fun) and np.all(np.isfinite(res.x))):return (np.nan,)*7+(0,)
 q,rv=map(float,res.x);boundary=int(q==0 or rv==0)
 return float(coef[0]),float(coef[1]),float(p0),q,rv,float(r0),float(res.fun),1|2*boundary
def fit_chunk(args):
 xa,xb=args;out=np.empty((2*len(xa),8))
 for i in range(len(xa)):
  out[2*i]=fit_one((xa[i],xb[i]));out[2*i+1]=fit_one((xb[i],xa[i]))
 return out
def run_fit_tasks(pool,tasks,context,worker=fit_chunk):
 futures=[pool.submit(worker,task) for task in tasks];pending=set(futures);deadline=time.monotonic()+3600.;results={}
 while pending:
  if time.monotonic()>=deadline:
   for future in pending:future.cancel()
   raise RuntimeError(f'R4 worker timeout context={context} pending={len(pending)}')
  done,pending=concurrent.futures.wait(pending,timeout=5.,return_when=concurrent.futures.FIRST_EXCEPTION)
  for future in done:
   try:results[futures.index(future)]=future.result()
   except BaseException as exc:
    for item in pending:item.cancel()
    raise RuntimeError(f'R4 worker failure context={context} pending={len(pending)} cause={type(exc).__name__}: {exc}') from exc
  workers_state=getattr(pool,'_processes',{}) or {}
  dead=[(process.pid,process.exitcode) for process in workers_state.values() if process.exitcode is not None]
  if dead and pending:
   for future in pending:future.cancel()
   raise RuntimeError(f'R4 worker terminated context={context} dead={dead} pending={len(pending)}')
 return [results[index] for index in range(len(futures))]
def synthetic_abrupt_worker_exit(_):
 os._exit(91)
def valid_state_checkpoint(final,marker,candidate,label,ancestor):
 if not final.exists() and not marker.exists():return None
 if not(final.exists() and marker.exists()):raise RuntimeError(f'incomplete state checkpoint {candidate}/{label}')
 meta=json.loads(marker.read_text(encoding='utf-8'))
 required=(meta.get('candidate')==candidate and meta.get('partition')==label and meta.get('equivalence')=='PASS_EXACT' and
           meta.get('shared_field_mismatches')==0 and sha(final)==meta.get('sha256') and sha(ancestor)==meta.get('ancestor_sha256'))
 if not required:raise RuntimeError(f'state checkpoint validation failed {candidate}/{label}')
 return meta
def pairs(mask):
 ids=np.flatnonzero(mask);i,j=np.triu_indices(len(ids),1);return np.column_stack((ids[i],ids[j])).astype(np.int16)
def main():
 workers=min(8,max(1,(os.cpu_count() or 4)//2));set_num_threads(max(1,(os.cpu_count() or 4)-workers))
 if sha(INPUT)!=EXPECTED:raise RuntimeError('input checksum mismatch')
 d=np.load(INPUT,allow_pickle=False);dates=np.char.decode(d['dates']);r=d['response'];member=d['pair_member'];nsec=r.shape[1]
 OUT.mkdir(parents=True,exist_ok=True)
 active=np.zeros((nsec,nsec),bool);alpha=np.full((nsec,nsec,2),np.nan);beta=np.full_like(alpha,np.nan);pv=np.full_like(alpha,np.nan);qv=np.full_like(alpha,np.nan);rv=np.full_like(alpha,np.nan);states=np.zeros((nsec,nsec,2),np.uint8)
 ps0a=np.full((nsec,nsec),np.nan);ps0b=np.full_like(ps0a,np.nan);ps1a=np.full_like(ps0a,np.nan);ps1b=np.full_like(ps0a,np.nan)
 current_month=-1
 periods=[(f'{y}H{s}',f'{y}{"0101" if s==1 else "0701"}',f'{y}{"0630" if s==1 else "1231"}') for y in range(2015,2020) for s in (1,2)]
 with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
  for label,lo,hi in periods:
   final=OUT/f'{label}.npy';marker=OUT/f'{label}.complete.json';write=not(final.exists() or marker.exists())
   if not write and not(final.exists() and marker.exists() and sha(final)==json.loads(marker.read_text())['sha256']):raise RuntimeError('no-overwrite conflict')
   chunks=[];started=time.perf_counter();monthly=[]
   for t in np.flatnonzero((dates>=lo)&(dates<=hi)):
    pp=pairs(member[t]);month=int(dates[t][:6])
    if month!=current_month:
     seq,sc=sequences(pp,int(t),r,member);ok=np.isfinite(sc[:,0])&np.isfinite(sc[:,1]);use=pp[ok];seq=seq[ok];sc=sc[ok]
     active[:]=False;alpha[:]=np.nan;beta[:]=np.nan;pv[:]=np.nan;qv[:]=np.nan;rv[:]=np.nan;states[:]=0
     batch=256;tasks=[(seq[k:k+batch,:,0],seq[k:k+batch,:,1]) for k in range(0,len(seq),batch)]
     results=run_fit_tasks(pool,tasks,f'relationship/{label}/{month}');fits=np.vstack(results) if results else np.empty((0,8))
     for pos,(a,b) in enumerate(use):
      ab=fits[2*pos];ba=fits[2*pos+1]
      if ab[7]>0 and ba[7]>0:
       a=int(a);b=int(b);active[a,b]=True
       alpha[a,b]=[ab[0],ba[0]];beta[a,b]=[ab[1],ba[1]];pv[a,b]=[ab[2],ba[2]];qv[a,b]=[ab[3],ba[3]];rv[a,b]=[ab[4],ba[4]];states[a,b]=[int(ab[7]),int(ba[7])]
       ps0a[a,b],ps0b[a,b],ps1a[a,b],ps1b[a,b]=sc[pos]
     monthly.append({'month':month,'pairs_attempted':int(len(pp)),'pairs_available':int(active.sum())})
     current_month=month
    ai,bi=np.nonzero(active);pv[ai,bi]+=qv[ai,bi]
    cur=active[pp[:,0],pp[:,1]] if len(pp) else np.empty(0,bool);use=pp[cur]
    if len(use):
     a=use[:,0];b=use[:,1];xa=r[t,a];xb=r[t,b]
     muab=alpha[a,b,0]+beta[a,b,0]*xa;muba=alpha[a,b,1]+beta[a,b,1]*xb
     sdab=np.sqrt(np.maximum(0.,xa*xa*pv[a,b,0]+rv[a,b,0]));sdba=np.sqrt(np.maximum(0.,xb*xb*pv[a,b,1]+rv[a,b,1]))
     if write:
      rec=np.empty(len(use),DT);rec['date_ix']=t;rec['a']=a;rec['b']=b;rec['support']=63;rec['state_ab']=states[a,b,0];rec['state_ba']=states[a,b,1]
      rec['mu_ab']=muab;rec['mu_ba']=muba;rec['ps0_a']=ps0a[a,b];rec['ps0_b']=ps0b[a,b];rec['ps1_a']=ps1a[a,b];rec['ps1_b']=ps1b[a,b];rec['predsd_ab']=sdab;rec['predsd_ba']=sdba;chunks.append(rec)
     # evaluate then update; both responses are qualified by current pair membership
     eab=xb-muab;k=pv[a,b,0]*xa/(xa*xa*pv[a,b,0]+rv[a,b,0]);beta[a,b,0]+=k*eab;pv[a,b,0]=np.maximum(0.,(1-k*xa)*pv[a,b,0])
     eba=xa-muba;k=pv[a,b,1]*xb/(xb*xb*pv[a,b,1]+rv[a,b,1]);beta[a,b,1]+=k*eba;pv[a,b,1]=np.maximum(0.,(1-k*xb)*pv[a,b,1])
   if not write:continue
   arr=np.concatenate(chunks) if chunks else np.empty(0,DT);tmp=final.with_suffix('.tmp.npy');np.save(tmp,arr,allow_pickle=False);os.replace(tmp,final)
   meta={'candidate':'V1-R4-63D','partition':label,'rows':len(arr),'sha256':sha(final),'input_sha256':EXPECTED,'monthly_fits':monthly,'elapsed_seconds':time.perf_counter()-started,'of4_accessed':False,'held_out_accessed':False}
   marker.write_text(json.dumps(meta,sort_keys=True,indent=2)+'\n',encoding='utf-8');print(json.dumps({'candidate':meta['candidate'],'partition':label,'rows':len(arr),'sha256':meta['sha256'],'elapsed_seconds':meta['elapsed_seconds'],'monthly_origins':len(monthly)}),flush=True)
def augment_state():
 workers=min(8,max(1,(os.cpu_count() or 4)//2));set_num_threads(max(1,(os.cpu_count() or 4)-workers))
 if sha(INPUT)!=EXPECTED:raise RuntimeError('input checksum mismatch')
 d=np.load(INPUT,allow_pickle=False);dates=np.char.decode(d['dates']);r=d['response'];member=d['pair_member'];nsec=r.shape[1]
 state_root=ROOT/'data/qa_work/v1/phase1/rt3_state_v1/V1-R4-63D';state_root.mkdir(parents=True,exist_ok=True)
 sdt=np.dtype([('date_ix','<u2'),('a','<u2'),('b','<u2'),('state_ab','u1'),('state_ba','u1'),('alpha_ab','<f8'),('beta_ab','<f8'),('p_ab','<f8'),('q_ab','<f8'),('r_ab','<f8'),('alpha_ba','<f8'),('beta_ba','<f8'),('p_ba','<f8'),('q_ba','<f8'),('r_ba','<f8')])
 active=np.zeros((nsec,nsec),bool);alpha=np.full((nsec,nsec,2),np.nan);beta=np.full_like(alpha,np.nan);pv=np.full_like(alpha,np.nan);qv=np.full_like(alpha,np.nan);rv=np.full_like(alpha,np.nan);states=np.zeros((nsec,nsec,2),np.uint8)
 ps0a=np.full((nsec,nsec),np.nan);ps0b=np.full_like(ps0a,np.nan);ps1a=np.full_like(ps0a,np.nan);ps1b=np.full_like(ps0a,np.nan);current_month=-1
 periods=[(f'{y}H{s}',f'{y}{"0101" if s==1 else "0701"}',f'{y}{"0630" if s==1 else "1231"}') for y in range(2015,2020) for s in (1,2)];summary=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
  for label,lo,hi in periods:
   final=state_root/f'{label}.npy';marker=state_root/f'{label}.complete.json'
   prior=valid_state_checkpoint(final,marker,'V1-R4-63D',label,OUT/f'{label}.npy')
   if prior is not None:
    summary.append(prior);continue
   original=np.load(OUT/f'{label}.npy',allow_pickle=False,mmap_mode='r');cursor=0;chunks=[]
   for t in np.flatnonzero((dates>=lo)&(dates<=hi)):
    pp=pairs(member[t]);month=int(dates[t][:6])
    if month!=current_month:
     seq,sc=sequences(pp,int(t),r,member);ok=np.isfinite(sc[:,0])&np.isfinite(sc[:,1]);use=pp[ok];seq=seq[ok];sc=sc[ok]
     active[:]=False;alpha[:]=np.nan;beta[:]=np.nan;pv[:]=np.nan;qv[:]=np.nan;rv[:]=np.nan;states[:]=0
     batch=256;tasks=[(seq[k:k+batch,:,0],seq[k:k+batch,:,1]) for k in range(0,len(seq),batch)];results=run_fit_tasks(pool,tasks,f'state/{label}/{month}');fits=np.vstack(results) if results else np.empty((0,8))
     for pos,(a,b) in enumerate(use):
      ab=fits[2*pos];ba=fits[2*pos+1]
      if ab[7]>0 and ba[7]>0:
       a=int(a);b=int(b);active[a,b]=True;alpha[a,b]=[ab[0],ba[0]];beta[a,b]=[ab[1],ba[1]];pv[a,b]=[ab[2],ba[2]];qv[a,b]=[ab[3],ba[3]];rv[a,b]=[ab[4],ba[4]];states[a,b]=[int(ab[7]),int(ba[7])];ps0a[a,b],ps0b[a,b],ps1a[a,b],ps1b[a,b]=sc[pos]
     current_month=month
    ai,bi=np.nonzero(active);pv[ai,bi]+=qv[ai,bi];cur=active[pp[:,0],pp[:,1]] if len(pp) else np.empty(0,bool);use=pp[cur]
    if len(use):
     a=use[:,0];b=use[:,1];xa=r[t,a];xb=r[t,b];muab=alpha[a,b,0]+beta[a,b,0]*xa;muba=alpha[a,b,1]+beta[a,b,1]*xb;sdab=np.sqrt(np.maximum(0.,xa*xa*pv[a,b,0]+rv[a,b,0]));sdba=np.sqrt(np.maximum(0.,xb*xb*pv[a,b,1]+rv[a,b,1]))
     rec=np.empty(len(use),DT);rec['date_ix']=t;rec['a']=a;rec['b']=b;rec['support']=63;rec['state_ab']=states[a,b,0];rec['state_ba']=states[a,b,1];rec['mu_ab']=muab;rec['mu_ba']=muba;rec['ps0_a']=ps0a[a,b];rec['ps0_b']=ps0b[a,b];rec['ps1_a']=ps1a[a,b];rec['ps1_b']=ps1b[a,b];rec['predsd_ab']=sdab;rec['predsd_ba']=sdba
     old=original[cursor:cursor+len(rec)]
     for name in DT.names:
      same=np.array_equal(rec[name],old[name],equal_nan=True) if rec[name].dtype.kind=='f' else np.array_equal(rec[name],old[name])
      if not same:raise RuntimeError(f'R4 equivalence mismatch {label}/{name}')
     cursor+=len(rec)
     sr=np.empty(len(use),sdt);sr['date_ix']=t;sr['a']=a;sr['b']=b;sr['state_ab']=states[a,b,0];sr['state_ba']=states[a,b,1];sr['alpha_ab']=alpha[a,b,0];sr['beta_ab']=beta[a,b,0];sr['p_ab']=pv[a,b,0];sr['q_ab']=qv[a,b,0];sr['r_ab']=rv[a,b,0];sr['alpha_ba']=alpha[a,b,1];sr['beta_ba']=beta[a,b,1];sr['p_ba']=pv[a,b,1];sr['q_ba']=qv[a,b,1];sr['r_ba']=rv[a,b,1];chunks.append(sr)
     eab=xb-muab;k=pv[a,b,0]*xa/(xa*xa*pv[a,b,0]+rv[a,b,0]);beta[a,b,0]+=k*eab;pv[a,b,0]=np.maximum(0.,(1-k*xa)*pv[a,b,0]);eba=xa-muba;k=pv[a,b,1]*xb/(xb*xb*pv[a,b,1]+rv[a,b,1]);beta[a,b,1]+=k*eba;pv[a,b,1]=np.maximum(0.,(1-k*xb)*pv[a,b,1])
   if cursor!=len(original):raise RuntimeError(f'R4 row mismatch {label}')
   arr=np.concatenate(chunks) if chunks else np.empty(0,sdt);tmp=final.with_suffix('.tmp.npy');np.save(tmp,arr,allow_pickle=False);os.replace(tmp,final)
   meta={'candidate':'V1-R4-63D','partition':label,'rows':len(arr),'sha256':sha(final),'ancestor_sha256':sha(OUT/f'{label}.npy'),'shared_rows_verified':cursor,'shared_field_mismatches':0,'equivalence':'PASS_EXACT','of4_accessed':False,'held_out_accessed':False};marker.write_text(json.dumps(meta,sort_keys=True,indent=2)+'\n',encoding='utf-8');summary.append(meta);print(json.dumps({'candidate':'V1-R4-63D','partition':label,'state_rows':len(arr),'equivalence':'PASS_EXACT','sha256':meta['sha256']}),flush=True)
 (state_root/'summary.json').write_text(json.dumps({'schema':'RT3-STATE-R4-1.0','partitions':summary},sort_keys=True,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
 if '--augment-state' in sys.argv:augment_state()
 else:main()
