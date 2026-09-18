"""Eligibility-only audit: no prices, predictions, outcomes or PnL read."""
import json
from collections import Counter
from pathlib import Path
import numpy as np
import v1_c04_extend_2025 as x

PUBLIC = x.ROOT / 'data/manifests/TRADING_V1_1_INPUT_QUALIFICATION.json'


def main():
    audit_path = x.ROOT / 'data/manifests/C04_A_THROUGH_2025_FINAL_AUDIT.json'
    audit = json.loads(audit_path.read_text(encoding='utf-8'))
    if audit['status'] != 'PASS_BOUNDED_C04_A_CONTRACT': raise RuntimeError('C04 audit not passed')
    rows = [json.loads(l) for l in Path(audit['exclusion_calendar']['file']).read_text(encoding='utf-8').splitlines()]
    specs = [('inner', x.ROOT/'data/qa_work/v1/phase1/inner_input_v1.npz', '360E6E20E359BFF58F66E8E05FCD43E762160B3F47F24B59318E4EBF041F3916'),
             ('of4', Path('D:/MechanismAwareStatArbData/OF4/input/of4_input_v1.npz'), None),
             ('heldout', Path('D:/MechanismAwareStatArbData/FINAL_HELDOUT_V1/input/of4_input_v1.npz'), None)]
    results = []
    for role, path, expected in specs:
        if expected is None:
            meta = json.loads((path.parent.parent/'_metadata/input_manifest.json').read_text(encoding='utf-8'))
            expected = meta['artifact_sha256']
        if x.digest(path) != expected: raise RuntimeError('immutable input hash mismatch')
        with np.load(path, allow_pickle=False) as d:
            ds = {str(v): i for i, v in enumerate(np.char.decode(d['dates']))}
            cs = {str(v): i for i, v in enumerate(np.char.decode(d['codes']))}
            ok = d['response_ok']
        gaps = sorted({(r['historical_ticker'], r['effective_ex_date']) for r in rows
                       if r['historical_ticker'] in cs and r['effective_ex_date'].replace('-', '') in ds
                       and ok[ds[r['effective_ex_date'].replace('-', '')], cs[r['historical_ticker']]]})
        results.append({'role': role, 'input': str(path), 'sha256': expected,
                        'status': 'PASS' if not gaps else 'UNQUALIFIED_IMMUTABLE_RESPONSE_ELIGIBILITY_ANCESTRY',
                        'mismatch_count': len(gaps), 'mismatches_by_year': dict(Counter(date[:4] for _, date in gaps)),
                        'affected_security_count': len({code for code, _ in gaps}),
                        'mismatched_security_dates': [{'security': c, 'date': d} for c, d in gaps]})
    result = {'qualification_id': 'TRADING-V1-1-INPUT-QUALIFICATION-1.0',
              'c04_audit_sha256': x.digest(audit_path), 'roles': results,
              'disposition': 'Execute independently qualified inner scope only. Later complete books unavailable: immutable prediction input eligibility does not implement newly qualified C04 exclusions; no refit or silent repair authorized.',
              'rule': 'Pre-execution full input-lineage qualification, not outcome-based episode selection',
              'research_ancestor_consequence': 'Published OF4/held-out vectors remain immutable historical descriptive outputs under their original incomplete C04 calendar; not validated confirmation under the through-2025 exclusion contract.',
              'pnl_computed_or_inspected': False, 'upstream_recomputed': False}
    body = (json.dumps(result, indent=2, sort_keys=True)+'\n').encode()
    x.atomic(PUBLIC, body)
    print(json.dumps({'result': 'QUALIFIED_INNER_ONLY', 'roles': [{k:v for k,v in r.items() if k != 'mismatched_security_dates'} for r in results], 'pnl_accessed': False}))


if __name__ == '__main__': main()
