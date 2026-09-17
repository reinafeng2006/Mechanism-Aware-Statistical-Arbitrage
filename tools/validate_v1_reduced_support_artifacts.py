"""Hash/lineage/shape audit only; never print scientific values or recompute units."""
import json
from pathlib import Path
import numpy as np
import v1_final_heldout_reduced_support as r

ACCESS_HASH = 'E7D129135BF189655A5279301069FEA002344FA249F54A59D117C816E6831714'


def audit_input():
    manifest = json.loads((r.EXT / '_metadata/input_manifest.json').read_text())
    actual = r.sha(r.INPUT)
    assert actual == manifest['artifact_sha256'], 'held-out input hash mismatch'
    for candidate in r.CANDIDATES:
        for fold in r.FOLDS:
            marker = json.loads((r.REL / candidate / f'{fold}.complete.json').read_text())
            assert marker['input_sha256'] == actual, 'relationship input lineage mismatch'
    return actual


def audit_r4():
    root = r.STATE / 'V1-R4-63D'
    for fold in ('2024', '2025'):
        ancestor = r.REL / 'V1-R4-63D' / f'{fold}.npy'
        record = json.loads(ancestor.with_suffix('.complete.json').read_text())
        assert r.sha(ancestor) == record['sha256'], 'immutable R4 relationship hash mismatch'
    state = json.loads((root / '2024.complete.json').read_text())
    assert r.sha(root / '2024.npy') == state['sha256'], 'immutable R4-2024 state hash mismatch'
    assert state['equivalence'] == 'PASS_EXACT' and state['shared_field_mismatches'] == 0
    assert state['ancestor_sha256'] == r.sha(r.REL / 'V1-R4-63D' / '2024.npy')
    markers = sorted((root / '_engineering').rglob('*block-*.complete.json'))
    assert len(markers) == 524, 'R4 engineering block count changed'
    for marker in markers:
        meta = json.loads(marker.read_text())
        payload = marker.with_name(marker.name.replace('.complete.json', '.npy'))
        assert r.sha(payload) == meta['sha256'], 'R4 engineering hash mismatch'
    assert not (root / '2025.npy').exists() and not (root / '2025.complete.json').exists()
    assert r.sha(r.ACCESS) == ACCESS_HASH, 'held-out access event changed'
    return 524


def main():
    audit_r4()
    audit_input()
    p = r.load_progress()
    assert p['state'] == 'COMPLETE', 'pipeline incomplete'
    r.preflight()
    with np.load(r.INPUT, allow_pickle=False) as source:
        dates = np.char.decode(source['dates'])
    stage = json.loads(r.STAGE_MANIFEST.read_text())
    assert len(stage['payloads']) == 48
    raw_hashes = {x['logical_path']: x['raw_sha256'] for x in stage['payloads']}
    for rec in stage['payloads']:
        path = r.EXT / rec['physical_relative_path']
        assert r.sha(path) == rec['sha256'], 'compressed hash mismatch'
        assert r.compressed_raw_sha(path) == rec['raw_sha256'], 'lossless hash mismatch'
        raw = r.EXT / rec['logical_path']
        if raw.exists(): assert r.sha(raw) == rec['raw_sha256'], 'raw ancestor changed'
        family = Path(rec['logical_path']).parts[0]
        if family in ('relationships', 'rt3_state'):
            original = json.loads(raw.with_suffix('.complete.json').read_text())
            assert original['sha256'] == rec['raw_sha256'], 'original checkpoint lineage mismatch'
            assert original['held_out_accessed'] is True
            if family == 'rt3_state':
                assert original['equivalence'] == 'PASS_EXACT' and original['shared_field_mismatches'] == 0
                relation_key = f"relationships/{original['candidate']}/{original['partition']}.npy"
                assert original['ancestor_sha256'] == raw_hashes[relation_key], 'RT3 ancestry mismatch'
    for candidate in r.CANDIDATES:
        for fold in r.FOLDS:
            r.verify_checkpoint(r.A3A5, candidate, fold, 'a3a5')
            marker = json.loads((r.A3A5 / candidate / f'{fold}.complete.json').read_text())
            assert r.sha(r.REL / candidate / f'{fold}.npy') == marker['ancestor_relationship_sha256']
            assert r.sha(r.STATE / candidate / f'{fold}.npy') == marker['ancestor_state_sha256']
            rows = marker['rows']
            for tag, shape in [('a3', (rows, 4)), ('a5', (rows, 2, 4, 5))]:
                array = np.load(r.A3A5 / candidate / f'{fold}.{tag}.npy', mmap_mode='r', allow_pickle=False)
                assert array.shape == shape and array.dtype == np.dtype('<f4'), 'A3/A5 schema mismatch'
            rel = np.load(r.REL / candidate / f'{fold}.npy', mmap_mode='r', allow_pickle=False)
            for start in range(0, rows, 100000):
                end = min(rows, start + 100000)
                t = rel['date_ix'][start:end].astype(np.intp)
                assert np.all((dates[t] >= fold+'0101') & (dates[t] <= fold+'1231')), 'fold role mismatch'
                for h, horizon in enumerate((1, 5, 10, 20)):
                    invalid = (t+horizon >= len(dates)) | (dates[np.minimum(t+horizon, len(dates)-1)] > fold+'1231')
                    assert not np.any(np.isfinite(array[start:end][invalid, :, h, :])), 'A5 target crosses fold boundary'
            del rel, array
    layer = json.loads(r.LAYER_MANIFEST.read_text())
    expected = {(c, f) for c in r.CANDIDATES for f in r.FOLDS}
    assert {(x['candidate'], x['partition']) for x in layer['records']} == expected
    for rec in layer['records']:
        assert r.sha(Path(rec['physical_path'])) == rec['sha256']
        assert r.compressed_raw_sha(Path(rec['physical_path'])) == rec['raw_sha256']
        assert r.sha(Path(rec['ancestor_artifact'])) == rec['ancestor_sha256']
        assert r.sha(Path(rec['scale_lineage_artifact'])) == rec['scale_lineage_sha256']
        assert rec['scale_version'] == 'V1-A1-H126-CN-SCALE-LOSS-1.0'
        assert 'V1-R0C-126W' in rec['scale_lineage_artifact']
    syn = r.configure_synthesis()
    sp = json.loads(syn.PROGRESS.read_text())
    specs = syn.unit_specs()
    assert set(sp['units']) == {s['id'] for s in specs} and sp['completed'] == 44
    assert sp['held_out_accessed'] is True, 'held-out synthesis access metadata mismatch'
    assert sp['layer_manifest_sha256'] == r.sha(r.LAYER_MANIFEST)
    for spec in specs:
        rec = sp['units'][spec['id']]
        assert Path(rec['path']) == syn.unit_path(spec)
        assert r.sha(syn.unit_path(spec)) == rec['sha256']
        assert syn.unit_path(spec).stat().st_size == rec['bytes']
        if spec['kind'] != 'support':
            metadata = json.loads(syn.unit_path(spec).read_text())
            for field in ('role', 'fold', 'candidate', 'left', 'right'):
                if field in spec: assert metadata[field] == spec[field], 'synthesis unit identity mismatch'
    assert r.sha(r.FINAL) == p['final_sha256'] == sp['final_sha256']
    receipt = {'validation_id': 'V1-REDUCED-SUPPORT-FINAL-INTEGRITY-1.0', 'result': 'PASS',
               'a3a5_units': 12, 'compressed_payloads': 48, 'h126_partitions': 12, 'synthesis_units': 44,
               'r4_engineering_blocks_preserved': 524, 'access_sha256': ACCESS_HASH,
               'final_sha256': r.sha(r.FINAL), 'layer_manifest_sha256': r.sha(r.LAYER_MANIFEST),
               'stage_manifest_sha256': r.sha(r.STAGE_MANIFEST), 'scientific_values_exposed': False}
    r.atomic_json(r.CONTROL / 'reduced_support_final_validation.json', receipt)
    print(json.dumps(receipt))


if __name__ == '__main__': main()
