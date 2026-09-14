"""Validate hashes/schema/role boundaries of V1 inner relationship outputs only."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/qa_work/v1/phase1/inner_outputs_v2/relationships"
MANIFEST=ROOT/"data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json"
CANDIDATES=["V1-R0D-252M","V1-R0C-126W","V1-R0L-126W","V1-R1M-126W","V1-R1MI-126W","V1-R3-252M","V1-R4-63D"]
PARTS=[f"{y}H{s}" for y in range(2015,2020) for s in (1,2)]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(8<<20),b''):h.update(c)
 return h.hexdigest().upper()
def main():
 entries=[];fail=[]
 for c in CANDIDATES:
  for part in PARTS:
   p=BASE/c/f"{part}.npy";m=BASE/c/f"{part}.complete.json"
   if not p.exists() or not m.exists():fail.append(f"missing:{c}:{part}");continue
   meta=json.loads(m.read_text(encoding='utf-8'));actual=sha(p)
   if actual!=meta.get('sha256'):fail.append(f"hash:{c}:{part}")
   a=np.load(p,mmap_mode='r',allow_pickle=False)
   required={'date_ix','a','b','support'}
   if not required.issubset(a.dtype.names or ()):fail.append(f"schema:{c}:{part}")
   entries.append({'candidate':c,'partition':part,'artifact':p.relative_to(ROOT).as_posix(),'rows':int(len(a)),'sha256':actual,'input_sha256':meta.get('input_sha256'),'of4_accessed':False,'held_out_accessed':False})
 manifest={'manifest_id':'V1-PHASE1-RELATIONSHIP-OUTPUTS-2.0','status':'IMMUTABLE_COMPLETE' if not fail else 'FAIL','input_manifest':'V1-PHASE1-INNER-INPUT-1.0','input_sha256':'360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916','candidate_count':len(CANDIDATES),'partition_count':len(entries),'partitions':entries,'date_role':'2015-2019_INNER_ONLY','interpretation':'NONE_BEFORE_COMPLETE_MATERIALIZATION','of4_accessed':False,'held_out_accessed':False,'superseded_engineering_trial':'data/qa_work/v1/phase1/inner_outputs_v1 retained; not qualified because refresh was pair-local rather than global-calendar'}
 MANIFEST.write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n',encoding='utf-8')
 if fail:raise SystemExit(json.dumps({'result':'FAIL','failures':fail}))
 print(json.dumps({'manifest_id':manifest['manifest_id'],'candidate_count':len(CANDIDATES),'partition_count':len(entries),'result':'PASS','values_disclosed':False}))
if __name__=='__main__':main()
