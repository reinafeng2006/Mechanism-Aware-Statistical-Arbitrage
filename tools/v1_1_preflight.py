"""Read-only Trading V1.1 policy/C04 prerequisite audit; never reads market values."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    policy_path = ROOT / 'research/TRADING_V1_1_POLICY.json'
    manifest_path = ROOT / 'data/manifests/C04_A_OFFICIAL_CALENDAR_V1.json'
    policy = json.loads(policy_path.read_text(encoding='utf-8'))
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if policy['policy_id'] != 'TRADING-V1.1-MORPHOLOGY-OPTION-A-BATCH-1.0':
        raise RuntimeError('policy identity mismatch')
    if len(policy['candidates']) != 6 or 'V1-R4-63D' in policy['candidates']:
        raise RuntimeError('candidate scope mismatch')
    expected = manifest['exclusion_calendar']['sha256']
    actual = hashlib.sha256((ROOT / manifest['exclusion_calendar']['file']).read_bytes()).hexdigest().upper()
    if actual != expected or not manifest['validated']:
        raise RuntimeError('C04 integrity/validation mismatch')
    last = manifest['calendar_scope']['last_archive_period']
    blocked = [role for role, required in [('inner', '2019-12'), ('of4', '2023-12'), ('heldout', '2025-12')]
               if last < required]
    print(json.dumps({'policy_sha256': hashlib.sha256(policy_path.read_bytes()).hexdigest().upper(),
                      'c04_manifest_sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest().upper(),
                      'c04_exclusion_hash_pass': True, 'qualified_calendar_last_archive_period': last,
                      'coverage_failed_roles': blocked,
                      'result': 'BLOCKED_C04_TEMPORAL_COVERAGE' if blocked else 'C04_DATE_COVERAGE_PASS_OTHER_INPUT_CHECKS_STILL_REQUIRED',
                      'pnl_computed_or_inspected': False}))
    return 2 if blocked else 0


if __name__ == '__main__':
    raise SystemExit(main())
