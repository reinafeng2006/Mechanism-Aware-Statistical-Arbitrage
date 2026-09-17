"""Non-empirical reporting/gate test, using only deterministic invented values."""
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import v1_final_research_evidence_checkpoint as e


def source(roles):
    comparisons, summaries, temporal = [], [], {}
    candidates = e.r.CANDIDATES + ['V1-R4-63D']
    for role, folds in roles:
        for hyp, (_, left, right) in e.BINDINGS.items():
            if role == 'heldout' and hyp == 'H4': continue
            key = left+'__'+right
            metrics = {f: {'temporal_median_of_fold_equal_pair_median_differences': -0.25,
                           'fold_count': len(folds)} for f in e.r.FIELDS}
            if role == 'heldout': temporal[key] = metrics
            else: temporal.setdefault(key, {})[role] = metrics
            for fold in folds:
                comparisons.append({'left': left, 'right': right, 'role': role, 'fold': fold,
                    'metrics': {f: {'right_minus_left_equal_pair_median': -0.25,
                                   'pair_count': 4, 'observation_count': 20} for f in e.r.FIELDS}})
        for candidate in candidates[:6] if role == 'heldout' else candidates:
            for fold in folds:
                summaries.append({'role': role, 'fold': fold, 'candidate': candidate,
                                  'support': {'native_rows': 24, 'common_rows': 20},
                                  **{scope: {f: {'equal_pair_median': 0.5, 'equal_pair_mad': 0.125}
                                             for f in e.r.FIELDS} for scope in ('common','native')}})
    return {'pairwise_common_support': comparisons, 'results': summaries,
            'temporal_median_vector': {'pairwise': temporal}}


def main():
    missing = source([('heldout',['2024','2025'])])
    left,right = e.BINDINGS['H1'][1:]
    missing['pairwise_common_support'][0]['metrics']['loss_abs_ab']['right_minus_left_equal_pair_median'] = None
    missing['temporal_median_vector']['pairwise'][left+'__'+right]['loss_abs_ab']['temporal_median_of_fold_equal_pair_median_differences'] = None
    unavailable = e.extract(missing,left,right,'heldout')['loss_abs_ab']
    assert unavailable['temporal_median'] is None and unavailable['unavailable_folds'] == 1
    assert unavailable['fold_range'] == [None,None]
    missing['pairwise_common_support'][0]['metrics']['loss_abs_ab']['right_minus_left_equal_pair_median'] = float('nan')
    missing['temporal_median_vector']['pairwise'][left+'__'+right]['loss_abs_ab']['temporal_median_of_fold_equal_pair_median_differences'] = float('nan')
    assert e.extract(missing,left,right,'heldout')['loss_abs_ab']['temporal_median'] is None
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        old, final, target, receipt, out, doc = [root / x for x in
            ('old.json', 'final.json', 'targets.json', 'reduced_support_final_validation.json', 'out.json', 'out.md')]
        e.r.atomic_json(old, source([('inner', [f'{y}H{h}' for y in range(2015,2020) for h in (1,2)]),
                                    ('of4', [str(y) for y in range(2020,2024)])]))
        e.r.atomic_json(final, source([('heldout', ['2024','2025'])]))
        h5results = []
        for role,candidate,fold in e.h5.specs():
            cell = {'equal_pair_median': 0.125, 'pair_count': 4, 'observation_count': 20, 'equal_pair_mad': 0.0625}
            h5results.append({'role':role, 'candidate':candidate, 'fold':fold,
                'directions': {d: {f'O{h}': {c: cell for c in e.h5.COMPONENTS} for h in e.h5.HORIZONS} for d in ('AB','BA')}})
        e.r.atomic_json(target, {'results':h5results})
        e.r.atomic_json(receipt, {'result':'PASS', 'final_sha256': e.r.sha(final)})
        with patch.multiple(e, OLD=old, OLD_HASH=e.r.sha(old), OUT=out, DOC=doc, ANCESTOR_MANIFESTS={'synthetic':old}), \
             patch.multiple(e.r, CONTROL=root, FINAL=final, ACCESS=old), \
             patch.multiple(e.h5, FINAL=target, validate=lambda: None):
            e.main()
            result = json.loads(out.read_text())
            assert result['hypotheses']['H4']['heldout']['status'] == e.H4
            assert result['hypotheses']['H1']['heldout']['loss_abs_ab']['negative_folds'] == 2
            assert len(result['h5_native_component_temporal_vectors']) == 800
            assert 'TRADING V1.1 SINGLE DECISION REQUIRED' in doc.read_text(encoding='utf-8')
            times = (out.stat().st_mtime_ns, doc.stat().st_mtime_ns)
            e.main()
            assert times == (out.stat().st_mtime_ns, doc.stat().st_mtime_ns), 'valid report was rewritten'
            e.r.atomic_json(receipt, {'result':'PASS', 'final_sha256':'invalid'})
            try: e.main()
            except AssertionError: pass
            else: raise AssertionError('invalid final hash was not rejected')
    print('PASS: synthetic reporting, role separation, H4 disposition and integrity gate; no scientific inputs accessed')


if __name__ == '__main__': main()
