"""Migration inventory only: stat payloads; read declared JSON metadata, never results.

Writes a generated metadata catalog, not scientific output. No payload loading,
decompression, fitting, trading, acquisition or repair. Hashes for large payloads
are recorded prior receipts, NOT a fresh full-payload validation.
"""
from __future__ import annotations
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EXTERNAL = Path(r"D:\MechanismAwareStatArbData")
OUT = REPO / "research/migration/EXTERNAL_ARTIFACT_INVENTORY.json"
HEX = re.compile(r"^[0-9a-fA-F]{64}$")


def locator(value):
    normalized = str(value).replace('\\', '/')
    for root, token in [(str(EXTERNAL).replace('\\', '/'), 'external://'),
                        (str(REPO).replace('\\', '/'), 'repo://')]:
        if normalized.lower().startswith(root.lower() + '/'):
            return token + normalized[len(root) + 1:]
    return normalized


def hash_records(obj, pointer=''):
    """Only hashes and adjacent path fields leave the metadata parser."""
    found = []
    if isinstance(obj, dict):
        paths = {k: locator(v) for k, v in obj.items()
                 if isinstance(v, str) and any(x in k.lower() for x in
                    ('path', 'artifact', 'file', 'root')) and not HEX.fullmatch(v)
                 and ('/' in v or '\\' in v or '.' in v)}
        for key, value in obj.items():
            child = pointer + '/' + str(key).replace('~', '~0').replace('/', '~1')
            if isinstance(value, str) and HEX.fullmatch(value):
                found.append({'pointer': child, 'sha256': value.upper(),
                              'path_context': paths})
            elif isinstance(value, (dict, list)):
                found.extend(hash_records(value, child))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            if isinstance(value, (dict, list)):
                found.extend(hash_records(value, pointer + '/' + str(index)))
    return found


def main():
    catalog = {'schema': 'MIGRATION-METADATA-INVENTORY-1.0',
               'created_utc': datetime.now(timezone.utc).isoformat(),
               'physical_roots': {'external://': str(EXTERNAL), 'repo://': str(REPO)},
               'boundary': 'Metadata only; no scientific payload content read. '
               'Receipt hashes are prior expected hashes, not newly verified payload hashes.',
               'payload_backup_in_git': False, 'families': [], 'metadata_receipts': []}
    for root in [*sorted(EXTERNAL.iterdir()), REPO/'data/raw', REPO/'data/qa_work']:
        if not root.is_dir():
            continue
        files = [{'logical_locator': locator(p), 'bytes': p.stat().st_size}
                 for p in sorted(root.rglob('*')) if p.is_file()]
        catalog['families'].append({'root': locator(root), 'file_count': len(files),
                                    'bytes': sum(f['bytes'] for f in files), 'files': files})
    # Existing canonical manifest/control schemas; never external unit result JSON.
    metadata = list((REPO/'data/manifests').glob('*.json'))
    metadata += [REPO/'research'/x for x in
                 ['V1_FINAL_FREEZE.json', 'V1_FINAL_HELDOUT_COMPLETION.json',
                  'V1_OF4_EXTERNAL_STORAGE_CONTRACT.json']]
    metadata += list((EXTERNAL/'OF4/_metadata').glob('*.json'))
    metadata += list((EXTERNAL/'FINAL_HELDOUT_V1/_metadata').glob('*.json'))
    metadata += list((EXTERNAL/'FINAL_HELDOUT_V1/_control').glob('*.json'))
    metadata += list(EXTERNAL.rglob('*.sha256.json'))
    metadata += list(EXTERNAL.rglob('*.complete.json'))
    # Progress documents hold unit identity/hash ledgers; export only hash/path keys.
    metadata += list(EXTERNAL.rglob('progress.json'))
    for path in sorted(set(metadata)):
        if not path.is_file():
            raise RuntimeError('Missing declared metadata: ' + locator(path))
        raw = path.read_bytes()
        obj = json.loads(raw.decode('utf-8-sig'))
        catalog['metadata_receipts'].append({
            'logical_locator': locator(path), 'bytes': len(raw),
            'metadata_sha256_verified_now': hashlib.sha256(raw).hexdigest().upper(),
            'top_level_keys': sorted(obj) if isinstance(obj, dict) else ['ARRAY'],
            'recorded_hash_bindings': hash_records(obj)})
    catalog['generated_runner_source_hashes'] = [
        {'logical_locator': locator(p),
         'sha256': hashlib.sha256(p.read_bytes()).hexdigest().upper()}
        for p in sorted(EXTERNAL.glob('*/_generated_runner/*.py'))]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps({'status': 'PASS_METADATA_ONLY', 'output': locator(OUT),
                      'families': [{k: v for k, v in f.items() if k != 'files'}
                                   for f in catalog['families']],
                      'metadata_receipts': len(catalog['metadata_receipts']),
                      'recorded_hash_bindings': sum(len(x['recorded_hash_bindings'])
                                                   for x in catalog['metadata_receipts'])}))


if __name__ == '__main__':
    main()
