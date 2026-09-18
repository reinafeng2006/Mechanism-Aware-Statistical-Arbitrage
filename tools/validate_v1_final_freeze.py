"""Final checksum snapshot; no model or trading recomputation."""
import argparse
import json
import platform
from pathlib import Path
import numpy as np
import v1_1_trading as t
import v1_c04_extend_2025 as x

MAN=t.ROOT/'research/V1_FINAL_FREEZE.json'
PATHS=['research/TRADING_V1_1_POLICY.json','research/V1_TERMINAL_MODEL_REGISTRY.json',
 'research/V1_FINAL_HELDOUT_COMPLETION.json','research/NEXT_ACTION.json',
 'data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json','data/manifests/TRADING_V1_1_INPUT_QUALIFICATION.json',
 'data/manifests/C04_A_THROUGH_2025_V1.json','data/manifests/C04_A_THROUGH_2025_V2.json',
 'data/manifests/C04_A_THROUGH_2025_FINAL_AUDIT.json','data/manifests/C04_A_OFFICIAL_CALENDAR_V1.json',
 'docs/stages/G5/V1_FINAL_RESEARCH_TRADING_SYNTHESIS.md','docs/stages/G5/V1_1_FINAL_ECONOMIC_EVIDENCE.md',
 'docs/stages/G5/V1_1_FINAL_INPUT_QUALIFICATION.md','docs/decisions/V1_FINAL_FREEZE.md',
 'docs/stages/G4/V2_FINAL_LIMITATIONS_REGISTER.md','tools/v1_1_trading.py','tools/v1_1_accounting.py',
 'tools/test_v1_1_trading.py','tools/test_v1_1_accounting.py','tools/v1_1_final_report.py',
 'tools/v1_1_input_qualification.py','tools/v1_c04_final_audit.py','tools/validate_v1_final_freeze.py']


def main(build=False):
    e=t.read(t.ROOT/'data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json')
    if len(e['units'])!=60 or len(e['book_cost_fold_ledger'])!=288:raise RuntimeError('closure scope')
    for u in e['units']:
        if not t.completed(u['candidate'],u['fold']) or x.digest(u['path'])!=u['sha256']:raise RuntimeError('unit hash')
    ledger=e['book_cost_fold_ledger']
    if sum(r['status']=='ECONOMICALLY_UNAVAILABLE' for r in ledger)!=180 or sum(r['status']=='ECONOMICALLY_UNAVAILABLE_INPUT_LINEAGE' for r in ledger)!=108:raise RuntimeError('unavailable ledger')
    if any(r['metrics'] is not None for r in ledger):raise RuntimeError('unexpected complete result')
    if len({(r['candidate'],r['fold'],r['cost_bps']) for r in ledger})!=288:raise RuntimeError('duplicate/missing book')
    x.validate_manifest(t.read(t.ROOT/'data/manifests/C04_A_THROUGH_2025_V2.json'))
    old=t.read(t.ROOT/'research/V1_FINAL_HELDOUT_COMPLETION.json');ext=[]
    for r in old['external_artifacts'].values():
        p=Path(old['external_root'])/r['path']
        if x.digest(p)!=r['sha256']:raise RuntimeError('immutable research/access receipt mismatch')
        ext.append({'path':str(p),'sha256':r['sha256']})
    for r in old['repository_artifacts'].values():
        if x.digest(t.ROOT/r['path'])!=r['sha256']:raise RuntimeError('immutable repository evidence mismatch')
    for r in [e['external_validation'],e['inspection_event']]:
        if x.digest(r['path'])!=r['sha256']:raise RuntimeError('reveal lineage')
        ext.append(r)
    if t.read(t.ROOT/'research/NEXT_ACTION.json')['action']['action_id']!='NONE':raise RuntimeError('execution not closed')
    result={'freeze_id':'RESEARCH-TRADING-V1-FINAL-FREEZE-2026-09-18',
     'status':'RESEARCH + TRADING V1 COMPLETE / FINAL FROZEN',
     'meaning':'TERMINAL_WORKFLOW_WITH_MATERIAL_EVIDENCE_UNAVAILABILITY_NOT_SUCCESSFUL_FULL_PERIOD_ECONOMIC_VALIDATION',
     'core_fingerprint':'3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616',
     'expected_tag':'v1-final-frozen-2026-09-18','one_shot_engine_commit':'25ca18a',
     'python':platform.python_version(),'numpy':np.__version__,
     'h4':'COMPUTATION-INCOMPLETE / NO FINAL HELD-OUT DISPOSITION','h6':e['h6_disposition'],
     'a6_g5':'V1_NON_ESTIMABLE_NOT_EXECUTED',
     'later_research_c04_qualification':'HISTORICAL_DESCRIPTIVE_NOT_VALIDATED_UNDER_COMPLETED_EXCLUSION_CONTRACT',
     'trading_units':60,'computed_inner_cost_folds':180,'uncomputed_later_cost_folds':108,
     'complete_evaluable_cost_folds':0,'r4_engineering_blocks_preserved':524,
     'large_artifact_root':str(t.OUT),
     'repository_artifacts':[{'path':p,'sha256':x.digest(t.ROOT/p)} for p in PATHS],
     'external_artifacts':ext,'unit_hash_manifest':'data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json',
     'no_v2_execution':True,'no_further_acquisition':True,'no_policy_retuning':True,
     'reproduction_boundary':'Validation only in V1; one-shot runner refuses after closure; never recompute valid completed units'}
    if build:t.atomic(MAN,result)
    if t.read(MAN)!=result:raise RuntimeError('final snapshot mismatch')
    print(json.dumps({'result':'PASS','units':60,'dispositions':288,'manifest_sha256':x.digest(MAN)}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--build',action='store_true');a=p.parse_args();main(a.build)
