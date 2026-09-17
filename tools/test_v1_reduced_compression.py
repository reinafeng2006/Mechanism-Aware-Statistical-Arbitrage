"""Synthetic exact-byte serial/parallel compression and resume check."""
import gzip
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import v1_final_heldout_reduced_support as r

with tempfile.TemporaryDirectory(prefix='v1-compression-', dir=r.EXT / '_temp') as folder:
    r.EXT = Path(folder)
    payload = bytes(range(256)) * 4096
    paths = [r.EXT / f'{i}.npy' for i in range(4)]
    for path in paths: path.write_bytes(payload)
    with ThreadPoolExecutor(max_workers=4) as pool:
        first = list(pool.map(r.compress_one, paths))
    assert len({x['sha256'] for x in first}) == 1
    for rec in first:
        assert rec['raw_sha256'] == r.sha(paths[0])
    before = [(p.with_suffix('.npy.gz').stat().st_mtime_ns) for p in paths]
    with ThreadPoolExecutor(max_workers=4) as pool:
        second = list(pool.map(r.compress_one, paths))
    assert first == second
    assert before == [p.with_suffix('.npy.gz').stat().st_mtime_ns for p in paths]
    assert all(p.exists() for p in paths)
print('PASS: parallel deterministic bytes, lossless hashes, raw preservation, hash-verified skip')
