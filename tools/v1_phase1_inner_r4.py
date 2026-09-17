"""Execute frozen V1 R4 CF-A on checksum-bound 2015-2019 inner data."""
from __future__ import annotations
import concurrent.futures,gc,hashlib,json,math,os,sys,time
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
BDT=np.dtype([('a','<u2'),('b','<u2'),('scale','<f8',(4,)),('fit','<f8',(2,8))])
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
def await_block_futures(pool,items,context):
 pending={item[4]:item for item in items if item[4] is not None};results={};deadline=time.monotonic()+3600.
 while pending:
  if time.monotonic()>=deadline:raise RuntimeError(f'R4 worker timeout context={context} pending={len(pending)}')
  done,_=concurrent.futures.wait(tuple(pending),timeout=5.,return_when=concurrent.futures.FIRST_EXCEPTION)
  workers_state=getattr(pool,'_processes',{}) or {};dead=[(process.pid,process.exitcode) for process in workers_state.values() if process.exitcode not in (None,0)]
  if dead:raise RuntimeError(f'R4 worker terminated context={context} dead={dead} pending={len(pending)}')
  for future in done:
   item=pending.pop(future)
   try:results[item[0]]=future.result()
   except BaseException as exc:raise RuntimeError(f'R4 worker failure context={context}/block-{item[0]:05d} cause={type(exc).__name__}: {exc}') from exc
 return results
def synthetic_abrupt_worker_exit(_):
 os._exit(91)
def atomic_json(path,obj):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.tmp')
 tmp.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n',encoding='utf-8');os.replace(tmp,path)
def atomic_npy(path,arr):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.tmp')
 try:
  with tmp.open('wb') as stream:
   np.save(stream,arr,allow_pickle=False);stream.flush();os.fsync(stream.fileno())
  os.replace(tmp,path)
 finally:
  if tmp.exists():tmp.unlink()
def valid_engineering_checkpoint(payload,marker,expected):
 if not payload.exists() and not marker.exists():return None
 if not(payload.exists() and marker.exists()):raise RuntimeError(f'incomplete engineering checkpoint {payload}')
 meta=json.loads(marker.read_text(encoding='utf-8'))
 if any(meta.get(k)!=v for k,v in expected.items()) or meta.get('sha256')!=sha(payload):raise RuntimeError(f'engineering checkpoint validation failed {payload}')
 return meta
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
def assemble_year(final,month_payloads,sdt):
 total=sum(int(np.load(path,allow_pickle=False,mmap_mode='r').shape[0]) for path in month_payloads);tmp=final.with_suffix(final.suffix+'.tmp')
 if tmp.exists():tmp.unlink()
 out=np.lib.format.open_memmap(tmp,mode='w+',dtype=sdt,shape=(total,));cursor=0
 for path in month_payloads:
  part=np.load(path,allow_pickle=False,mmap_mode='r');out[cursor:cursor+len(part)]=part;cursor+=len(part);del part
 out.flush();del out;os.replace(tmp,final);return total
def augment_state(smoke_blocks=0):
 workers=min(4,max(1,int(os.environ.get('V1_R4_WORKERS','4'))));set_num_threads(1)
 if sha(INPUT)!=EXPECTED:raise RuntimeError('input checksum mismatch')
 d=np.load(INPUT,allow_pickle=False);dates=np.char.decode(d['dates']);r=d['response'];member=d['pair_member'];nsec=r.shape[1]
 state_root=ROOT/'data/qa_work/v1/phase1/rt3_state_v1/V1-R4-63D';state_root.mkdir(parents=True,exist_ok=True)
 sdt=np.dtype([('date_ix','<u2'),('a','<u2'),('b','<u2'),('state_ab','u1'),('state_ba','u1'),('alpha_ab','<f8'),('beta_ab','<f8'),('p_ab','<f8'),('q_ab','<f8'),('r_ab','<f8'),('alpha_ba','<f8'),('beta_ba','<f8'),('p_ba','<f8'),('q_ba','<f8'),('r_ba','<f8')])
 active=np.zeros((nsec,nsec),bool);alpha=np.full((nsec,nsec,2),np.nan);beta=np.full_like(alpha,np.nan);pv=np.full_like(alpha,np.nan);qv=np.full_like(alpha,np.nan);rv=np.full_like(alpha,np.nan);states=np.zeros((nsec,nsec,2),np.uint8)
 ps0a=np.full((nsec,nsec),np.nan);ps0b=np.full_like(ps0a,np.nan);ps1a=np.full_like(ps0a,np.nan);ps1b=np.full_like(ps0a,np.nan);current_month=-1
 periods=[(f'{y}H{s}',f'{y}{"0101" if s==1 else "0701"}',f'{y}{"0630" if s==1 else "1231"}') for y in range(2015,2020) for s in (1,2)];summary=[]
 completed_new_blocks=0
 with concurrent.futures.ProcessPoolExecutor(max_workers=workers,max_tasks_per_child=64) as pool:
  for label,lo,hi in periods:
   final=state_root/f'{label}.npy';marker=state_root/f'{label}.complete.json'
   prior=valid_state_checkpoint(final,marker,'V1-R4-63D',label,OUT/f'{label}.npy')
   if prior is not None:
    summary.append(prior);continue
   ancestor=OUT/f'{label}.npy';ancestor_sha=sha(ancestor);original=np.load(ancestor,allow_pickle=False,mmap_mode='r');engineering=state_root/'_engineering'/label;engineering.mkdir(parents=True,exist_ok=True);month_payloads=[]
   year_days=np.flatnonzero((dates>=lo)&(dates<=hi));months=sorted(set(int(dates[t][:6]) for t in year_days))
   for month in months:
    month_payload=engineering/f'month-{month}.npy';month_marker=engineering/f'month-{month}.complete.json';month_expected={'kind':'R4_STATE_MONTH','candidate':'V1-R4-63D','partition':label,'month':month,'ancestor_sha256':ancestor_sha,'input_sha256':EXPECTED,'shared_field_mismatches':0,'equivalence':'PASS_EXACT'}
    if valid_engineering_checkpoint(month_payload,month_marker,month_expected) is not None:month_payloads.append(month_payload);continue
    days=[int(t) for t in year_days if int(dates[t][:6])==month];t0=days[0];pp=pairs(member[t0]);block_payloads=[]
    starts=list(range(0,len(pp),256));starts=starts[:smoke_blocks] if smoke_blocks else starts;block_paths={}
    cursor_block=0
    while cursor_block<len(starts):
     width=min(workers,len(starts)-cursor_block)
     if smoke_blocks:width=min(width,max(1,smoke_blocks-completed_new_blocks))
     pending=[]
     for block in range(cursor_block,cursor_block+width):
      start=starts[block];payload=engineering/f'{month}-block-{block:05d}.npy';block_marker=engineering/f'{month}-block-{block:05d}.complete.json';expected={'kind':'R4_FIT_BLOCK','candidate':'V1-R4-63D','partition':label,'month':month,'block':block,'pair_start':start,'pair_stop':min(start+256,len(pp)),'ancestor_sha256':ancestor_sha,'input_sha256':EXPECTED};block_paths[block]=payload
      if valid_engineering_checkpoint(payload,block_marker,expected) is not None:continue
      seq,sc=sequences(pp[start:start+256],int(t0),r,member);ok=np.isfinite(sc[:,0])&np.isfinite(sc[:,1]);use=pp[start:start+256][ok];seq=seq[ok];sc=sc[ok]
      future=pool.submit(fit_chunk,(seq[:,:,0],seq[:,:,1])) if len(seq) else None;pending.append((block,payload,block_marker,expected,future,use,sc));del seq
     batch_results=await_block_futures(pool,pending,f'state/{label}/{month}')
     for block,payload,block_marker,expected,future,use,sc in pending:
      fits=batch_results[block] if future is not None else np.empty((0,8))
      arr=np.empty(len(use),BDT);arr['a']=use[:,0];arr['b']=use[:,1];arr['scale']=sc;arr['fit']=fits.reshape(len(use),2,8);atomic_npy(payload,arr);atomic_json(block_marker,{**expected,'rows':len(arr),'sha256':sha(payload),'status':'ENGINEERING_PARTIAL_NOT_SCIENTIFIC_OUTPUT'});completed_new_blocks+=1;del fits,arr,use,sc;gc.collect()
     cursor_block+=width
    if smoke_blocks:
     print(json.dumps({'status':'BOUNDED_ENGINEERING_SMOKE_COMPLETE','validated_blocks':len(starts),'new_blocks':completed_new_blocks,'scientific_values_exposed':False}),flush=True);return
    block_payloads=[block_paths[block] for block in range(len(starts))]
    active[:]=False;alpha[:]=np.nan;beta[:]=np.nan;pv[:]=np.nan;qv[:]=np.nan;rv[:]=np.nan;states[:]=0
    for payload in block_payloads:
     block_data=np.load(payload,allow_pickle=False)
     for row in block_data:
      a=int(row['a']);b=int(row['b']);ab=row['fit'][0];ba=row['fit'][1]
      if ab[7]>0 and ba[7]>0:
       active[a,b]=True;alpha[a,b]=[ab[0],ba[0]];beta[a,b]=[ab[1],ba[1]];pv[a,b]=[ab[2],ba[2]];qv[a,b]=[ab[3],ba[3]];rv[a,b]=[ab[4],ba[4]];states[a,b]=[int(ab[7]),int(ba[7])];ps0a[a,b],ps0b[a,b],ps1a[a,b],ps1b[a,b]=row['scale']
     del block_data
    month_chunks=[];month_start=int(np.searchsorted(original['date_ix'],days[0],'left'));month_cursor=month_start
    for t in days:
     pp=pairs(member[t]);ai,bi=np.nonzero(active);pv[ai,bi]+=qv[ai,bi];cur=active[pp[:,0],pp[:,1]] if len(pp) else np.empty(0,bool);use=pp[cur]
     if len(use):
      a=use[:,0];b=use[:,1];xa=r[t,a];xb=r[t,b];muab=alpha[a,b,0]+beta[a,b,0]*xa;muba=alpha[a,b,1]+beta[a,b,1]*xb;sdab=np.sqrt(np.maximum(0.,xa*xa*pv[a,b,0]+rv[a,b,0]));sdba=np.sqrt(np.maximum(0.,xb*xb*pv[a,b,1]+rv[a,b,1]))
      rec=np.empty(len(use),DT);rec['date_ix']=t;rec['a']=a;rec['b']=b;rec['support']=63;rec['state_ab']=states[a,b,0];rec['state_ba']=states[a,b,1];rec['mu_ab']=muab;rec['mu_ba']=muba;rec['ps0_a']=ps0a[a,b];rec['ps0_b']=ps0b[a,b];rec['ps1_a']=ps1a[a,b];rec['ps1_b']=ps1b[a,b];rec['predsd_ab']=sdab;rec['predsd_ba']=sdba
      old=original[month_cursor:month_cursor+len(rec)]
      for name in DT.names:
       same=np.array_equal(rec[name],old[name],equal_nan=True) if rec[name].dtype.kind=='f' else np.array_equal(rec[name],old[name])
       if not same:raise RuntimeError(f'R4 equivalence mismatch {label}/{month}/{name}')
      month_cursor+=len(rec);sr=np.empty(len(use),sdt);sr['date_ix']=t;sr['a']=a;sr['b']=b;sr['state_ab']=states[a,b,0];sr['state_ba']=states[a,b,1];sr['alpha_ab']=alpha[a,b,0];sr['beta_ab']=beta[a,b,0];sr['p_ab']=pv[a,b,0];sr['q_ab']=qv[a,b,0];sr['r_ab']=rv[a,b,0];sr['alpha_ba']=alpha[a,b,1];sr['beta_ba']=beta[a,b,1];sr['p_ba']=pv[a,b,1];sr['q_ba']=qv[a,b,1];sr['r_ba']=rv[a,b,1];month_chunks.append(sr)
      eab=xb-muab;k=pv[a,b,0]*xa/(xa*xa*pv[a,b,0]+rv[a,b,0]);beta[a,b,0]+=k*eab;pv[a,b,0]=np.maximum(0.,(1-k*xa)*pv[a,b,0]);eba=xa-muba;k=pv[a,b,1]*xb/(xb*xb*pv[a,b,1]+rv[a,b,1]);beta[a,b,1]+=k*eba;pv[a,b,1]=np.maximum(0.,(1-k*xb)*pv[a,b,1])
    month_end=int(np.searchsorted(original['date_ix'],days[-1],'right'))
    if month_cursor!=month_end:raise RuntimeError(f'R4 monthly row mismatch {label}/{month}')
    month_arr=np.concatenate(month_chunks) if month_chunks else np.empty(0,sdt);atomic_npy(month_payload,month_arr);atomic_json(month_marker,{**month_expected,'rows':len(month_arr),'sha256':sha(month_payload),'shared_rows_verified':month_cursor-month_start,'shared_field_mismatches':0,'equivalence':'PASS_EXACT','status':'ENGINEERING_PARTIAL_NOT_SCIENTIFIC_OUTPUT'});month_payloads.append(month_payload);del month_chunks,month_arr;gc.collect()
   rows=assemble_year(final,month_payloads,sdt)
   meta={'candidate':'V1-R4-63D','partition':label,'rows':rows,'sha256':sha(final),'ancestor_sha256':ancestor_sha,'shared_rows_verified':rows,'shared_field_mismatches':0,'equivalence':'PASS_EXACT','of4_accessed':False,'held_out_accessed':False};atomic_json(marker,meta);summary.append(meta);print(json.dumps({'candidate':'V1-R4-63D','partition':label,'state_rows':rows,'equivalence':'PASS_EXACT','sha256':meta['sha256']}),flush=True)
 (state_root/'summary.json').write_text(json.dumps({'schema':'RT3-STATE-R4-1.0','partitions':summary},sort_keys=True,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
 if '--augment-state-smoke-blocks' in sys.argv:augment_state(int(sys.argv[sys.argv.index('--augment-state-smoke-blocks')+1]))
 elif '--augment-state' in sys.argv:augment_state()
 else:main()
