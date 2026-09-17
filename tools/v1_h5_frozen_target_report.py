"""Descriptive native-support reporting of immutable A5 component vectors.

No target is recomputed, no event threshold or cross-candidate attribution is
introduced. Uses the frozen within-direction/pair/temporal median hierarchy.
Execution is gated on the complete reduced-support integrity receipt.
"""
import argparse
import gzip
import json
import os
import shutil
import warnings
from pathlib import Path

import numpy as np
import v1_final_heldout_reduced_support as r

ROOT = r.EXT / 'h5_native_target_report_v1'
PROGRESS = ROOT / 'progress.json'
FINAL = ROOT / 'frozen_native_target_vectors.json'
COMPONENTS = ['RT0', 'RT1', 'RT2_abs', 'RT2_signed', 'RT3']
HORIZONS = [1, 5, 10, 20]


def pair_medians(values, starts, ends):
    medians = np.empty(len(starts), np.float64)
    counts = np.zeros(len(starts), np.int64)
    for first in range(0, len(starts), 1024):
        last = min(first + 1024, len(starts))
        width = int(np.max(ends[first:last] - starts[first:last]))
        ix = starts[first:last, None] + np.arange(width)[None, :]
        valid = ix < ends[first:last, None]
        block = values[np.minimum(ix, len(values)-1)].copy()
        valid &= np.isfinite(block)
        block[~valid] = np.nan
        counts[first:last] = valid.sum(axis=1)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', RuntimeWarning)
            medians[first:last] = np.nanmedian(block, axis=1)
    return medians, counts


def specs():
    for role, folds, candidates in [
        ('inner', [f'{y}H{h}' for y in range(2015, 2020) for h in (1, 2)], r.CANDIDATES + ['V1-R4-63D']),
        ('of4', [str(y) for y in range(2020, 2024)], r.CANDIDATES + ['V1-R4-63D']),
        ('heldout', r.FOLDS, r.CANDIDATES),
    ]:
        for candidate in candidates:
            for fold in folds:
                yield role, candidate, fold


def sources(role, candidate, fold):
    if role == 'inner':
        base = r.ROOT / 'data/qa_work/v1/phase1/inner_outputs_v2'
    elif role == 'of4':
        base = Path(r'D:\MechanismAwareStatArbData\OF4')
    else:
        base = r.EXT
    rel = base / 'relationships' / candidate / f'{fold}.npy'
    a5 = base / 'a3_a5' / candidate / f'{fold}.a5.npy'
    return tuple(p if p.exists() else p.with_suffix(p.suffix + '.gz') for p in (rel, a5))


def mmap_source(path, label):
    if path.suffix != '.gz': return np.load(path, mmap_mode='r', allow_pickle=False), None
    temp = ROOT / '_temp' / f'{label}.npy'
    temp.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, 'rb') as inp, temp.open('wb') as out:
        shutil.copyfileobj(inp, out, 8 << 20)
    return np.load(temp, mmap_mode='r', allow_pickle=False), temp


def summarize(role, candidate, fold):
    rel_path, a5_path = sources(role, candidate, fold)
    rel, rel_tmp = mmap_source(rel_path, 'relationship')
    a5, a5_tmp = mmap_source(a5_path, 'a5')
    pairs = (rel['a'].astype(np.uint32) << 10) | rel['b'].astype(np.uint32)
    order = np.argsort(pairs, kind='stable')
    sorted_pairs = pairs[order]
    starts = np.r_[0, np.flatnonzero(np.diff(sorted_pairs)) + 1]
    ends = np.r_[starts[1:], len(order)]
    out = {'role': role, 'candidate': candidate, 'fold': fold, 'native_only': True,
           'population': 'ALL_FROZEN_ELIGIBLE_A5_ROWS_NO_ADDITIONAL_EVENT_THRESHOLD',
           'scale': 'IMMUTABLE_A5_EVENT_TIME_SCALE_UNCHANGED_NOT_H126_A1_RESCALING',
           'cross_candidate_attribution': False, 'directions': {},
           'relationship_sha256': r.sha(rel_path), 'a5_sha256': r.sha(a5_path)}
    for d, direction in enumerate(('AB', 'BA')):
        out['directions'][direction] = {}
        for h, horizon in enumerate(HORIZONS):
            vector = {}
            for c, component in enumerate(COMPONENTS):
                values = a5[order, d, h, c].astype(np.float64)
                medians, counts = pair_medians(values, starts, ends)
                good = medians[np.isfinite(medians)]
                center = float(np.median(good)) if len(good) else None
                vector[component] = {'equal_pair_median': center, 'pair_count': int(len(good)),
                                     'observation_count': int(counts.sum()),
                                     'equal_pair_mad': float(np.median(np.abs(good-center))) if len(good) else None}
                del values
            out['directions'][direction][f'O{horizon}'] = vector
    del rel, a5
    for temp in (rel_tmp, a5_tmp):
        if temp is not None: temp.unlink()
    return out


def build():
    receipt = json.loads((r.CONTROL / 'reduced_support_final_validation.json').read_text())
    if receipt['result'] != 'PASS' or r.sha(r.FINAL) != receipt['final_sha256']:
        raise RuntimeError('complete held-out integrity receipt required before target reporting')
    p = json.loads(PROGRESS.read_text()) if PROGRESS.exists() else {'units': {}, 'completed': 0, 'total': 110}
    for role, candidate, fold in specs():
        uid = f'{role}__{candidate}__{fold}'
        dest = ROOT / 'units' / f'{uid}.json'
        if uid in p['units']:
            if r.sha(dest) != p['units'][uid]['sha256']: raise RuntimeError('H5 report checkpoint hash mismatch')
            continue
        if dest.exists(): raise RuntimeError('unbound H5 report unit requires controlled recovery')
        r.atomic_json(dest, summarize(role, candidate, fold))
        p['units'][uid] = {'path': str(dest), 'sha256': r.sha(dest)}
        p['completed'] = len(p['units']); r.atomic_json(PROGRESS, p)
        print(json.dumps({'completed': p['completed'], 'total': 110, 'scientific_values_exposed': False}), flush=True)
    results = [json.loads(Path(x['path']).read_text()) for x in p['units'].values()]
    r.atomic_json(FINAL, {'report_id': 'V1-H5-FROZEN-NATIVE-TARGET-VECTORS-1.0', 'results': results,
                         'inference': 'DESCRIPTIVE_ONLY_NO_BINARY_RESOLUTION_THRESHOLD_OR_SIGNIFICANCE_TEST',
                         'roles_separate': True, 'components_and_horizons_separate': True})
    p['final_sha256'] = r.sha(FINAL); p['state'] = 'COMPLETE'; r.atomic_json(PROGRESS, p)


def synthetic_test():
    values = np.array([2., np.nan, 0., 9., 3., 6., np.inf])
    got, counts = pair_medians(values, np.array([0, 3, 6]), np.array([3, 6, 7]))
    assert np.array_equal(got[:2], np.array([1., 6.])) and np.isnan(got[2])
    assert np.array_equal(counts, np.array([2, 3, 0]))
    assert len(list(specs())) == 110
    rng = np.random.default_rng(713)
    sizes = rng.integers(1, 31, 2500)
    starts = np.r_[0, np.cumsum(sizes)[:-1]]; ends = np.cumsum(sizes)
    values = rng.normal(size=int(ends[-1])); values[::7] = np.nan
    got, counts = pair_medians(values, starts, ends)
    expected = []
    for start, end in zip(starts, ends):
        finite = values[start:end][np.isfinite(values[start:end])]
        expected.append(np.median(finite) if len(finite) else np.nan)
    assert np.array_equal(got, np.array(expected), equal_nan=True)
    print('PASS: synthetic exact odd/even/finite native pair medians; no scientific inputs accessed')


def validate():
    p = json.loads(PROGRESS.read_text())
    expected = {f'{a}__{b}__{c}' for a, b, c in specs()}
    assert p['state'] == 'COMPLETE' and set(p['units']) == expected
    for rec in p['units'].values():
        assert r.sha(Path(rec['path'])) == rec['sha256']
    assert r.sha(FINAL) == p['final_sha256']
    print(json.dumps({'result': 'PASS', 'units': 110, 'final_sha256': p['final_sha256'], 'scientific_values_exposed': False}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('command', choices=['build', 'validate', 'synthetic-test']); args = parser.parse_args()
    {'build': build, 'validate': validate, 'synthetic-test': synthetic_test}[args.command]()
