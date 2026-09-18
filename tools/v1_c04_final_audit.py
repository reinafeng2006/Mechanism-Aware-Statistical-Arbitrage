"""Final offline C04 audit. No network, prices, signals or PnL."""
import datetime as dt
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
import v1_c04_extend_2025 as x

PUBLIC = x.ROOT / 'data/manifests/C04_A_THROUGH_2025_FINAL_AUDIT.json'


def audit():
    source = x.ROOT / 'data/manifests/C04_A_THROUGH_2025_V2.json'
    m = json.loads(source.read_text(encoding='utf-8'))
    x.validate_manifest(m)
    errors = []
    groups = defaultdict(list)
    identifier_failures = []
    for r in m['raw_artifacts']:
        if 'sse_current_' not in r['file']: continue
        p = json.loads(Path(r['file']).read_text(encoding='utf-8'))
        rows = p['result']; ph = p['pageHelp']
        if rows != ph['data']: errors.append('SSE row view mismatch')
        groups[(r['kind'], r['year'], r['board'])].append((r['page'], len(rows), ph['total']))
        key = 'COMPANY_CODE' if r['kind'] == 'rights' else 'A_STOCK_CODE'
        for row in rows:
            if not re.fullmatch(r'6\d{5}', str(row.get(key, '')).strip()):
                identifier_failures.append({'file': r['file'], 'field': key})
    if len(groups) != 24: errors.append('SSE successor scope count')
    for key, parts in groups.items():
        totals = {int(t) for _, _, t in parts}
        if len(totals) != 1 or sum(n for _, n, _ in parts) != next(iter(totals)) or sorted(p for p, _, _ in parts) != list(range(1, len(parts)+1)):
            errors.append('SSE incomplete pagination ' + str(key))
    sz = [c for c in m['coverage'] if c['source'] == 'SZSE_OFFICIAL']
    if {c['period'] for c in sz} != {f'{y}-{mm:02}' for y in range(2020, 2026) for mm in range(1, 13)}:
        errors.append('SZSE monthly scope')
    if m['failures'] or m['unavailable_scope'] or m['ambiguous_effective_date_records']:
        errors.append('source/schema/date unavailable')
    if identifier_failures: errors.append('SSE identifier failures')
    # Historical dividend/bonus modules cover 2020/21. Successor empty 2020/21
    # requests are NOT substituted for that historical evidence.
    inventory = json.loads(x.PUBLIC.read_text(encoding='utf-8'))
    for y in (2020, 2021):
        for kind in ('dividend', 'bonus'):
            rr = [r for r in inventory['raw_artifacts'] if r.get('year') == y and r.get('kind') == kind]
            if not rr: errors.append('missing historical handoff source')
    ancestor = json.loads(x.ANCESTOR.read_text(encoding='utf-8'))
    original = [json.loads(l) for l in (x.ROOT / ancestor['normalized_action_calendar']['file']).read_text(encoding='utf-8').splitlines()]
    actions = [json.loads(l) for l in Path(m['normalized_action_calendar']['file']).read_text(encoding='utf-8').splitlines()]
    if actions[:len(original)] != original: errors.append('original action rows changed')
    if len(actions) != m['normalized_action_calendar']['rows']: errors.append('action count')
    if any(a['historical_ticker'] not in m['universe'] or not a.get('effective_ex_date') for a in actions):
        errors.append('action identifier/effective date')
    result = {
        'audit_id': 'C04-A-THROUGH-2025-FINAL-AUDIT-1.0',
        'audit_time_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'source_manifest': str(source), 'source_manifest_sha256': x.digest(source),
        'ancestor_manifest_sha256': x.digest(x.ANCESTOR),
        'policy_sha256': x.digest(x.ROOT / 'research/TRADING_V1_1_POLICY.json'),
        'status': 'PASS_BOUNDED_C04_A_CONTRACT' if not errors else 'QUALIFICATION_INCOMPLETE',
        'errors': errors, 'identifier_failures': identifier_failures,
        'universe_count': len(m['universe']), 'exchange_security_counts': dict(Counter(t[-2:] for t in m['universe'])),
        'action_rows': len(actions), 'raw_artifacts_verified': len(m['raw_artifacts']),
        'normalized_action_calendar': m['normalized_action_calendar'], 'exclusion_calendar': m['exclusion_calendar'],
        'coverage': [
            {'exchange': 'SZSE', 'dates': '2020-01-01/2025-12-31', 'security_scope': 'All 447 frozen SZSE securities', 'source': '72 official monthly action tables'},
            {'exchange': 'SSE', 'dates': '2020-01-01/2021-12-31', 'security_scope': 'All 304 frozen SSE securities', 'source': 'historical dividend/bonus plus official successor rights, boards 1 and 2'},
            {'exchange': 'SSE', 'dates': '2022-01-01/2025-12-31', 'security_scope': 'All 304 frozen SSE securities', 'source': 'explicitly linked official successor dividend/bonus/rights tables'}],
        'positive_action_coverage': 'QUALIFIED_BOUNDED_TABLE_LINEAGE' if not errors else 'INCOMPLETE',
        'negative_no_action_coverage': 'NO_IDENTIFIED_ACTION_UNDER_V1_CALENDAR_ONLY; NOT_EXHAUSTIVE_NEGATIVE_INFERENCE',
        'authoritative_action_clean': False,
        'qualification_meaning': 'Original frozen two-state C04-A exclusion contract; not a new exhaustive no-action contract',
        'historical_handoff': 'Historical module documented cutoff 2022-01-07; full 2022 successor table used; empty successor 2020/21 tables do not establish negative coverage',
        'supersession': 'Inventory V1 retrieval completeness and V2 trading_ready are not standalone accounting qualification; this consolidated audit controls',
        'publication_time_missing': 'Retained unavailable; retrieval timestamps never used as historical availability',
        't09': 'Identified action without qualified entitlement treatment makes affected episode/portfolio interval unavailable; no fabricated adjusted prices or survivor renormalization',
        'acquisition_closed_for_v1': True, 'pnl_computed_or_inspected': False,
        'core_or_ancestor_overwritten': False,
    }
    if PUBLIC.exists():
        old = json.loads(PUBLIC.read_text(encoding='utf-8'))
        for k in result:
            if k != 'audit_time_utc' and result[k] != old[k]: raise RuntimeError('final audit changed: '+k)
    else:
        x.atomic(PUBLIC, (json.dumps(result, indent=2, sort_keys=True)+'\n').encode())
    print(json.dumps({'status': result['status'], 'errors': errors, 'actions': len(actions), 'hash': x.digest(PUBLIC), 'pnl_accessed': False}))
    if errors: raise SystemExit(2)


if __name__ == '__main__': audit()
