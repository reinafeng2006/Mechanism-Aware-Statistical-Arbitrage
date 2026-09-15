"""Structural validator for published EV-MAP-B inner A6/G5 execution."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MAN=ROOT/'data/manifests/V1_INNER_EV_MAP_B_A6_G5.json';OUT=ROOT/'data/qa_work/v1/phase1/inner_outputs_v2/ev_a6_g5'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def main():
 m=json.loads(MAN.read_text(encoding='utf-8'));c=json.loads((ROOT/'research/V1_EV_MAP_B_CONTRACT.json').read_text(encoding='utf-8'))
 if m['status']!='IMMUTABLE_COMPLETE' or m['partition_count']!=70:raise SystemExit('manifest incomplete')
 if c['status']!='PUBLISHED_BOUND_TO_PHASE1' or m['ev_map_b']!=c['status']:raise SystemExit('EV-MAP-B binding mismatch')
 for r in m['row_audits']:
  p=OUT/r['candidate']/f"{r['partition']}.ev-map-b.json"
  if sha(p)!=r['sha256']:raise SystemExit('row audit checksum mismatch')
  x=json.loads(p.read_text(encoding='utf-8'))
  if x['m1_evidence_unavailable']!=x['rows'] or x['endogeneity_unavailable']!=x['rows'] or x['flow_motive_unavailable']!=x['rows']:raise SystemExit('global unavailable mismatch')
  if x['future_leakage_present'] or x['future_leakage_unavailable']:raise SystemExit('qualified future-leakage lineage mismatch')
 a6p=OUT/'a6_fit_dispositions.json';g5p=OUT/'g5_disposition.json'
 if sha(a6p)!=m['a6_disposition_sha256'] or sha(g5p)!=m['g5_disposition_sha256']:raise SystemExit('disposition hash mismatch')
 a6=json.loads(a6p.read_text(encoding='utf-8'));g5=json.loads(g5p.read_text(encoding='utf-8'))
 if a6['problem_count']!=4032 or a6['available_fits']!=0 or a6['silent_column_drop']:raise SystemExit('A6 disposition mismatch')
 if g5['trades']!=0 or g5['pnl_created'] or g5['profit_is_mechanism_identification']:raise SystemExit('G5 disposition mismatch')
 if m['of4_accessed'] or m['held_out_accessed'] or m['relationship_rt3_a3_a5_recomputed']:raise SystemExit('scope boundary violated')
 print('PASS: 70 EV-MAP-B row audits, 4,032 A6 rank dispositions, and G5 probe gates are lineage-valid; OF4/held-out denied.')
if __name__=='__main__':main()
