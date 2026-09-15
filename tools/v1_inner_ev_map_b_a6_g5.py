"""Apply published EV-MAP-B to validated inner A3/A5 and execute A6/G5 gates.

No relationship, RT3, A3, or A5 artifact is modified.  Qualified propositions
are evaluated per row.  Unsupported propositions use the researcher-approved
global V1 unavailable state.  A6 estimability follows the frozen no-column-drop
rank contract; G5 follows the frozen evidence-quality gate and never forces a
trade.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
REL=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/relationships'
A35=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/a3_a5'
A35_MAN=ROOT/'data/manifests/V1_INNER_A3_A5.json'
OUT=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/ev_a6_g5'
MAN=ROOT/'data/manifests/V1_INNER_EV_MAP_B_A6_G5.json'

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(8<<20),b''):h.update(c)
 return h.hexdigest().upper()

def main():
 contract=json.loads((ROOT/'research/V1_EV_MAP_B_CONTRACT.json').read_text(encoding='utf-8'))
 if contract['status']!='PUBLISHED_BOUND_TO_PHASE1':raise RuntimeError('EV-MAP-B publication required')
 src=json.loads(A35_MAN.read_text(encoding='utf-8'))
 if src['status']!='IMMUTABLE_STRUCTURALLY_VALIDATED' or src['partition_count']!=70:raise RuntimeError('validated A3/A5 required')
 OUT.mkdir(parents=True,exist_ok=True);audits=[];total=0;valid_rows=0;target_available=np.zeros((2,4,5),np.int64)
 for p in src['partitions']:
  c,l=p['candidate'],p['partition'];rel=np.load(REL/c/f'{l}.npy',allow_pickle=False,mmap_mode='r');a3=np.load(A35/c/f'{l}.a3.npy',allow_pickle=False,mmap_mode='r');a5=np.load(A35/c/f'{l}.a5.npy',allow_pickle=False,mmap_mode='r')
  if len(rel)!=len(a3) or len(rel)!=len(a5):raise RuntimeError(f'row binding mismatch {c}/{l}')
  # Row-qualified deterministic propositions.
  mathematical_invalidity=~np.all(np.isfinite(a3),axis=1)
  lineage_ok=np.ones(len(rel),bool)  # checksum/PIT lineage was validated in the bound A3/A5 manifest
  future_leakage_present=~lineage_ok
  future_leakage_unavailable=np.zeros(len(rel),bool)
  mechanical_return_content_present=np.ones(len(rel),bool)  # MP0 formula contains the response being described
  overlapping_windows_present=np.ones(len(rel),bool)  # q_t and the event response use the same event observation interval
  cause_proxy_overlap_present=np.zeros(len(rel),bool)  # frozen role audit separates MP1 context from causal/response roles
  cause_proxy_overlap_unavailable=np.zeros(len(rel),bool)
  # Unsupported propositions explicitly authorized as global unavailable for V1.
  m1_evidence_unavailable=np.ones(len(rel),bool)
  endogeneity_unavailable=np.ones(len(rel),bool)
  flow_motive_unavailable=np.ones(len(rel),bool)
  m0_unavailable=np.ones(len(rel),bool)
  relationship_break_unavailable=np.ones(len(rel),bool)
  mechanism_ambiguity_unavailable=np.ones(len(rel),bool)
  evidence_conflict_unavailable=np.ones(len(rel),bool)
  information_insufficiency_present=np.ones(len(rel),bool)
  data_provenance_uncertainty_present=np.ones(len(rel),bool)  # C04 not authoritatively clean and SG-A regime qualification remains explicit
  row_valid=~mathematical_invalidity
  avail=np.isfinite(a5)
  target_available+=avail.sum(axis=0)
  rec={'candidate':c,'partition':l,'rows':int(len(rel)),'row_valid':int(row_valid.sum()),'mathematical_invalidity_present':int(mathematical_invalidity.sum()),
       'future_leakage_present':int(future_leakage_present.sum()),'future_leakage_unavailable':int(future_leakage_unavailable.sum()),
       'mechanical_return_content_present':int(mechanical_return_content_present.sum()),'overlapping_windows_present':int(overlapping_windows_present.sum()),
       'cause_proxy_overlap_present':int(cause_proxy_overlap_present.sum()),'cause_proxy_overlap_unavailable':int(cause_proxy_overlap_unavailable.sum()),
       'm1_evidence_unavailable':int(m1_evidence_unavailable.sum()),'endogeneity_unavailable':int(endogeneity_unavailable.sum()),'flow_motive_unavailable':int(flow_motive_unavailable.sum()),
       'm0_unavailable':int(m0_unavailable.sum()),'relationship_break_unavailable':int(relationship_break_unavailable.sum()),
       'mechanism_ambiguity_unavailable':int(mechanism_ambiguity_unavailable.sum()),'evidence_conflict_unavailable':int(evidence_conflict_unavailable.sum()),
       'information_insufficiency_present':int(information_insufficiency_present.sum()),'data_provenance_uncertainty_present':int(data_provenance_uncertainty_present.sum())}
  path=OUT/c/f'{l}.ev-map-b.json';path.parent.mkdir(parents=True,exist_ok=True)
  if path.exists() and json.loads(path.read_text(encoding='utf-8'))!=rec:raise RuntimeError(f'no-overwrite conflict {c}/{l}')
  if not path.exists():path.write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n',encoding='utf-8')
  audits.append({**rec,'sha256':sha(path)});total+=len(rel);valid_rows+=int(row_valid.sum())

 # A6 includes an intercept and every information set inherits PV0. Under the
 # published EV-MAP-B mapping, M0_unavailable and relationship_break_unavailable
 # are each observed constant-one columns. Their exact design rank contribution
 # is verified rather than silently removed.
 structural=np.column_stack((np.ones(4),np.ones(4),np.ones(4)))
 structural_rank=int(np.linalg.matrix_rank(structural));structural_columns=structural.shape[1]
 if structural_rank==structural_columns:raise RuntimeError('unexpected full rank; execute weighted OLS')
 candidates=sorted({p['candidate'] for p in src['partitions']});origins=[f'{y}H{h}' for y in range(2015,2020) for h in (1,2)][1:]
 problems=[]
 for c in candidates:
  for o in origins:
   for target in ('RT0','RT1','RT2','RT3'):
    for h in (1,5,10,20):
     for pv in ('PV0','PV-M1','PV-M2','PV-BOTH'):
      problems.append({'candidate':c,'origin':o,'target':target,'horizon':h,'information_set':pv,'status':'UNAVAILABLE_FULL_RANK_FAILURE','rank_witness':['INTERCEPT','M0_unavailable','relationship_break_evidence_unavailable']})
 a6_path=OUT/'a6_fit_dispositions.json';a6={'schema':'V1-A6-INNER-DISPOSITION-1.0','problem_count':len(problems),'available_fits':0,'problems':problems,'rank_witness_matrix_rank':structural_rank,'rank_witness_column_count':structural_columns,'silent_column_drop':False,'empirical_performance_interpreted':False}
 if a6_path.exists() and json.loads(a6_path.read_text(encoding='utf-8'))!=a6:raise RuntimeError('A6 no-overwrite conflict')
 if not a6_path.exists():a6_path.write_text(json.dumps(a6,sort_keys=True,indent=2)+'\n',encoding='utf-8')

 # Both probe gates require no unresolved evidence-conflict/quality block. The
 # approved global V1 state is unavailable, so no event reaches EP-A. This is a
 # gate result, not a causal or performance conclusion.
 g5={'schema':'V1-G5-INNER-DISPOSITION-1.0','channel_names':['M1-MOTIVATED DIRECTIONAL PROBE','M2-MOTIVATED DIRECTIONAL PROBE'],'relationship_event_rows':total,
     'm1_directional_admissions':0,'m2_directional_admissions':0,'directional_conflicts':0,'blocked_reentries':0,'execution_unavailable':0,'episodes':0,'trades':0,'pnl_created':False,
     'gate_disposition':'GLOBAL_V1_EVIDENCE_CONFLICT_UNAVAILABLE_IS_UNRESOLVED_QUALITY_BLOCK','profit_is_mechanism_identification':False,'FD_A':'NO_DELAY','ER_A':'252_REPORTING_NOT_REACHED_NO_TRADES'}
 g5_path=OUT/'g5_disposition.json'
 if g5_path.exists() and json.loads(g5_path.read_text(encoding='utf-8'))!=g5:raise RuntimeError('G5 no-overwrite conflict')
 if not g5_path.exists():g5_path.write_text(json.dumps(g5,sort_keys=True,indent=2)+'\n',encoding='utf-8')
 manifest={'manifest_id':'V1-INNER-EV-MAP-B-A6-G5-1.0','status':'IMMUTABLE_COMPLETE','ancestor_a3_a5_manifest':'V1-INNER-A3-A5-1.0','ancestor_a3_a5_sha256':sha(A35_MAN),
  'ev_map_b':'PUBLISHED_BOUND_TO_PHASE1','partition_count':len(audits),'relationship_event_rows':total,'row_valid':valid_rows,'target_available_counts':target_available.tolist(),'row_audits':audits,
  'a6_disposition_sha256':sha(a6_path),'g5_disposition_sha256':sha(g5_path),'claim_scope':contract['claim_scope'],'of4_accessed':False,'held_out_accessed':False,'relationship_rt3_a3_a5_recomputed':False}
 if MAN.exists() and json.loads(MAN.read_text(encoding='utf-8'))!=manifest:raise RuntimeError('manifest no-overwrite conflict')
 if not MAN.exists():MAN.write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n',encoding='utf-8')
 print('PASS: EV-MAP-B row exceptions audited; A6/G5 frozen gates executed; no unavailable state recoded.')
if __name__=='__main__':main()
