"""Compare bounded H126 serialization byte-for-byte with published arithmetic."""
import subprocess
import tempfile
import types
from pathlib import Path
import numpy as np
import v1_a1_h126_candidate_neutral as current

original = types.ModuleType('original_h126')
original.__file__ = str(Path(current.__file__))
source = subprocess.check_output(['git', 'show', 'f162365:tools/v1_a1_h126_candidate_neutral.py'], cwd=current.ROOT, text=True)
exec(compile(source, original.__file__, 'exec'), original.__dict__)
scratch = Path(r'D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1\_temp')
with tempfile.TemporaryDirectory(prefix='h126-equivalence-', dir=scratch) as folder:
    base = Path(folder); rel = base / 'relationships'
    candidates = ['V1-R0C-126W', 'V1-R3-252M']
    dt = np.dtype([(x, '<u2') for x in ('date_ix', 'a', 'b')] + [(x, '<f4') for x in ('ps0_a','ps0_b','ps1_a','ps1_b','mu_ab','mu_ba')])
    rng = np.random.default_rng(773)
    rows = [(t,a,b) for t in range(20) for a,b in ((0,1),(0,2),(1,2))]
    arr = np.zeros(len(rows), dt)
    for i, row in enumerate(rows): arr[i]['date_ix'], arr[i]['a'], arr[i]['b'] = row
    for field in ('ps0_a','ps0_b','ps1_a','ps1_b'): arr[field] = rng.uniform(.1,2.,len(arr))
    arr['mu_ab'] = rng.normal(size=len(arr)); arr['mu_ba'] = rng.normal(size=len(arr))
    arr['ps0_a'][10] = 0; arr['ps1_b'][11] = np.nan; arr['ps0_b'][12] = np.inf
    arr['ps0_a'][13] = 1e-20; arr['ps1_b'][14] = 1e-15
    arr = arr[rng.permutation(len(arr))]
    for candidate in candidates:
        path = rel / candidate / '2025.npy'; path.parent.mkdir(parents=True)
        if candidate == candidates[0]: payload = arr
        else:
            ndt = np.dtype([(name.replace('mu_', 'mu_n1_') if name.startswith('mu_') else name, arr.dtype[name]) for name in arr.dtype.names])
            payload = np.empty(len(arr), ndt)
            for name in arr.dtype.names: payload[name.replace('mu_', 'mu_n1_') if name.startswith('mu_') else name] = arr[name]
            payload['b'][0] = 4
        np.save(path, payload, allow_pickle=False)
    response = rng.normal(size=(30,5)); response[4,1] = np.nan
    original.OF4_REL = current.OF4_REL = rel
    original.CANDIDATES = current.CANDIDATES = candidates
    original.EXT = base / 'original'; current.EXT = base / 'bounded'; current.CHUNK_ROWS = 7
    expected = original.build_partition('heldout','2025',response)
    actual = current.build_partition('heldout','2025',response)
    for old, new in zip(expected, actual):
        assert old['sha256'] == new['sha256'] and old['raw_sha256'] == new['raw_sha256']
        assert old['rows'] == new['rows']
print('PASS: bounded H126 raw and gzip bytes exactly match published full-partition implementation')
