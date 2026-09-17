"""Exact synthetic support/summary/comparison equality for lossless mmap loading."""
import gzip
import subprocess
import tempfile
import types
from pathlib import Path
import numpy as np
import v1_a1_h126_synthesis_batch as current

original = types.ModuleType('original_synthesis')
original.__file__ = str(Path(current.__file__))
source = subprocess.check_output(['git','show','f162365:tools/v1_a1_h126_synthesis_batch.py'], cwd=current.ROOT, text=True)
exec(compile(source, original.__file__, 'exec'), original.__dict__)
scratch = Path(r'D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1\_temp')
with tempfile.TemporaryDirectory(prefix='synthesis-mmap-', dir=scratch) as folder:
    base = Path(folder); layers = base / 'layers'; records = []
    candidates = ['SYNTHETIC-A','SYNTHETIC-B']; rng = np.random.default_rng(911)
    dt = np.dtype([(x,'<u2') for x in ('date_ix','a','b')] + [(x,'<f4') for x in current.FIELDS])
    for candidate in candidates:
        arr = np.zeros(60, dt)
        arr['date_ix'] = np.repeat(np.arange(20),3)
        arr['a'] = np.tile([0,0,1],20); arr['b'] = np.tile([1,2,2],20)
        for field in current.FIELDS: arr[field] = rng.normal(size=60)
        arr['loss_abs_ab'][3 if candidate == candidates[0] else 5] = np.nan
        raw = base / f'{candidate}.npy'; np.save(raw,arr,allow_pickle=False)
        path = layers / 'heldout' / candidate / '2025.npy.gz'; path.parent.mkdir(parents=True)
        with raw.open('rb') as inp, path.open('wb') as dest:
            with gzip.GzipFile(filename='', mode='wb',fileobj=dest,mtime=0) as out: out.write(inp.read())
        records.append({'role':'heldout','candidate':candidate,'partition':'2025','sha256':current.sha(path),'raw_sha256':current.sha(raw)})
    manifest = base / 'manifest.json'; current.write_json_atomic(manifest, {'records':records})
    for module, name in ((original,'original'),(current,'mmap')):
        module.CANDIDATES = candidates; module.FOLDS = [('heldout','2025')]
        module.LAYER_ROOT = layers; module.LAYER_MANIFEST = manifest
        module.WORK_ROOT = base / name; module.UNITS_ROOT = module.WORK_ROOT / 'units'
        for spec in module.unit_specs():
            {'support':module.support_unit,'summary':module.summary_unit,'comparison':module.comparison_unit}[spec['kind']](spec,module.unit_path(spec))
    for spec in current.unit_specs():
        assert current.sha(current.unit_path(spec)) == original.sha(original.unit_path(spec))
    cache = current.WORK_ROOT / '_input_cache/heldout/SYNTHETIC-A/2025.npy'
    stamp = cache.stat().st_mtime_ns
    arr = current.load_layer('heldout','SYNTHETIC-A','2025'); assert isinstance(arr,np.memmap)
    assert stamp == cache.stat().st_mtime_ns
    del arr
print('PASS: mmap support, summaries and comparison bytes equal published implementation; cache hash-verified and reused')
