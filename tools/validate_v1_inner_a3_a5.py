"""Validate V1 inner A3/A5 artifacts without interpreting scientific values."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/a3_a5'
REL=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/relationships'
STATE=ROOT/'data/qa_work/v1/phase1/rt3_state_v1'
INPUT=ROOT/'data/qa_work/v1/phase1/inner_input_v1.npz'
H=(1,5,10,20)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(8<<20),b''):h.update(c)
 return h.hexdigest().upper()
def main():
 source=json.loads((ROOT/'data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json').read_text(encoding='utf-8'))
 dates=np.char.decode(np.load(INPUT,allow_pickle=False)['dates'])
 checked=[]
 for p in source['partitions']:
  c,l=p['candidate'],p['partition'];d=OUT/c;m=d/f'{l}.complete.json';a3p=d/f'{l}.a3.npy';a5p=d/f'{l}.a5.npy'
  if not(m.exists() and a3p.exists() and a5p.exists()):raise SystemExit(f'missing {c}/{l}')
  x=json.loads(m.read_text(encoding='utf-8'))
  if sha(REL/c/f'{l}.npy')!=x['ancestor_relationship_sha256'] or sha(STATE/c/f'{l}.npy')!=x['ancestor_state_sha256']:raise SystemExit(f'ancestor mismatch {c}/{l}')
  if sha(a3p)!=x['a3_sha256'] or sha(a5p)!=x['a5_sha256']:raise SystemExit(f'output mismatch {c}/{l}')
  rel=np.load(REL/c/f'{l}.npy',allow_pickle=False,mmap_mode='r');a3=np.load(a3p,allow_pickle=False,mmap_mode='r');a5=np.load(a5p,allow_pickle=False,mmap_mode='r')
  if a3.shape!=(len(rel),4) or a5.shape!=(len(rel),2,4,5):raise SystemExit(f'shape mismatch {c}/{l}')
  year=int(l[:4]);hi=f'{year}{"0630" if l.endswith("H1") else "1231"}'
  t=rel['date_ix'].astype(np.intp)
  for z,h in enumerate(H):
   invalid=(t+h>=len(dates))|(dates[np.minimum(t+h,len(dates)-1)]>hi)
   if np.any(np.isfinite(a5[invalid,:,z,:])):raise SystemExit(f'boundary leakage {c}/{l}/O{h}')
  checked.append({'candidate':c,'partition':l,'rows':int(len(rel)),'a3_sha256':x['a3_sha256'],'a5_sha256':x['a5_sha256']})
 manifest={'manifest_id':'V1-INNER-A3-A5-1.0','status':'IMMUTABLE_STRUCTURALLY_VALIDATED','partition_count':len(checked),'partitions':checked,'ancestor_relationship_manifest':source['manifest_id'],'rt3_ancestor':'V1-RT3-RELATIONSHIP-STATE-AUGMENTATION-1.0','target_horizon_censoring':'SAME_SEMIANNUAL_INNER_ROLE','interpretation':'NONE','of4_accessed':False,'held_out_accessed':False}
 path=ROOT/'data/manifests/V1_INNER_A3_A5.json'
 if path.exists():
  if json.loads(path.read_text(encoding='utf-8'))!=manifest:raise SystemExit('no-overwrite manifest conflict')
 else:path.write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n',encoding='utf-8')
 print(f"PASS: {len(checked)} immutable A3/A5 inner partitions; semiannual censoring and ancestry verified.")
if __name__=='__main__':main()
