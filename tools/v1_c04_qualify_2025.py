"""Official C04 successor-schema qualification, not a provider/taxonomy change."""
import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urlencode
import v1_c04_extend_2025 as x

VERSION = 'C04-A-OFFICIAL-CALENDAR-THROUGH-2025-V2'
PUBLIC = x.ROOT / 'data/manifests/C04_A_THROUGH_2025_V2.json'
SCRIPT = 'https://www.sse.com.cn/xhtml/home/2021public/querySearch/search_stockData_2021.js'
QUERIES = {'dividend': 'COMMON_SSE_SJ_GPSJ_FHSG_SSGSFHQK_L', 'bonus': 'COMMON_SSE_SJ_GPSJ_FHSG_SG_L', 'rights': 'COMMON_SSE_SJ_GPSJ_MJZJ_PG_ZBAKCB_L'}


def acquire(kind, year, board):
    raw, actions, page_no, expected, downloaded = [], [], 1, None, 0
    while True:
        params = {'isPagination': 'true', 'sqlId': QUERIES[kind], 'pageHelp.pageSize': '2000',
                  'pageHelp.pageNo': page_no, 'pageHelp.beginPage': page_no, 'pageHelp.endPage': page_no, 'pageHelp.cacheSize': 1}
        if kind == 'dividend': params.update(CONDITION_AG=1, A_REG_DATE=year)
        else: params['SEARCH_YEAR'] = year
        if kind == 'rights': params['LIST_BOARD'] = board
        url = x.old.SSE_QUERY + '?' + urlencode(sorted(params.items()))
        body, headers = x.fetch(url, 'https://www.sse.com.cn/market/stockdata/dividends/bonus/')
        artifact = x.write_raw(f'sse_current_{kind}_{year}_b{board}_p{page_no}.json', body)
        payload = json.loads(body.decode('utf-8'))
        page = payload.get('pageHelp') or {}
        if page.get('total') is None or int(page.get('pageNo', -1)) != page_no:
            raise RuntimeError('official pagination metadata unavailable')
        rows = payload.get('result')
        if not isinstance(rows, list): raise RuntimeError('official result schema unavailable')
        if page.get('data') is not None and page['data'] != rows: raise RuntimeError('official row views disagree')
        total = int(page['total'])
        if expected is not None and expected != total: raise RuntimeError('table changed during pagination')
        expected = total; downloaded += len(rows)
        raw.append({'source': 'SSE_OFFICIAL', 'kind': kind, 'year': year, 'board': board, 'page': page_no,
                    'url': url, 'rows': len(rows), 'official_total': total, 'status': 'OK', **artifact})
        for r in rows:
            if kind == 'dividend':
                required = ['A_STOCK_CODE', 'A_REG_DATE', 'A_DIV_DATE', 'A_BEFR_TAX_DIV']
                code, effective, record = r.get('A_STOCK_CODE'), r.get('A_DIV_DATE'), r.get('A_REG_DATE')
                types, terms = ['CASH_DIVIDEND'], {'pre_tax_per_share': r.get('A_BEFR_TAX_DIV')}
            elif kind == 'bonus':
                required = ['A_STOCK_CODE', 'A_REG_DATE', 'A_DERIGHTS_DATE', 'BONUS_RATIO', 'CONVERT_RATIO']
                code, effective, record = r.get('A_STOCK_CODE'), r.get('A_DERIGHTS_DATE'), r.get('A_REG_DATE')
                types, terms = ['BONUS_OR_CAPITALIZATION'], {'bonus_rate_per_10': r.get('BONUS_RATIO'), 'capitalization_rate_per_10': r.get('CONVERT_RATIO')}
            else:
                required = ['COMPANY_CODE', 'REG_DATE', 'DERIGHTS_DATE', 'RIGHTS_PRICE', 'RIGHTS_RATIO']
                code, effective, record = r.get('COMPANY_CODE'), r.get('DERIGHTS_DATE'), r.get('REG_DATE')
                types, terms = ['RIGHTS_ISSUE'], {'rights_price': r.get('RIGHTS_PRICE'), 'rights_ratio_per_10': r.get('RIGHTS_RATIO')}
            if any(k not in r for k in required): raise RuntimeError(f'{kind} action schema mismatch')
            if kind == 'bonus' and r['BONUS_RATIO'] == '-' and r['CONVERT_RATIO'] == '-':
                continue  # exact exclusion in official rendered bonus table
            code = str(code).strip()
            actions.append({'calendar_version': VERSION, 'source': 'SSE_OFFICIAL', 'source_url': url,
                            'source_artifact': artifact['file'], 'source_artifact_sha256': artifact['sha256'],
                            'source_archive_year': year, 'source_board': board, 'security_code': code,
                            'historical_ticker': code + '.SH', 'action_types': types,
                            'record_date': x.old.normalized_date(record), 'effective_ex_date': x.old.normalized_date(effective),
                            'action_publication_date': None, 'action_publication_time_quality': 'NOT_PRESENT_IN_OFFICIAL_TABLE',
                            'terms': terms, 'eligibility_effect': 'IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED' if x.old.normalized_date(effective) else 'EFFECTIVE DATE UNRESOLVED — NO CLEAN INTERVAL INFERENCE'})
        if downloaded == expected: break
        if downloaded > expected or not rows: raise RuntimeError('pagination incomplete/overlapping')
        page_no += 1
    return raw, actions


def run():
    action = json.loads((x.ROOT / 'research/NEXT_ACTION.json').read_text())['action']
    if action['status'] != 'AUTHORIZED' or not action.get('c04_extension_authorization'): raise RuntimeError('C04 authority required')
    if PUBLIC.exists():
        m = json.loads(PUBLIC.read_text(encoding='utf-8')); x.validate_manifest(m)
        print(json.dumps({'result': m['qualification_status'], 'checkpoint': 'HASH_VERIFY_SKIP'})); return
    inventory = json.loads(x.PUBLIC.read_text(encoding='utf-8')); x.validate_manifest(inventory)
    script_body, _ = x.fetch(SCRIPT, 'https://www.sse.com.cn/market/stockdata/dividends/bonus/')
    if any(q.encode() not in script_body for q in QUERIES.values()): raise RuntimeError('official query provenance mismatch')
    universe = set(inventory['universe'])
    # Legacy SSE tables are historical only; preserve them for ancestry, not as
    # evidence of negative coverage after their documented January 2022 cutoff.
    actions = [json.loads(line) for line in Path(inventory['normalized_action_calendar']['file']).read_text(encoding='utf-8').splitlines()]
    original_count = json.loads(x.ANCESTOR.read_text(encoding='utf-8'))['normalized_action_rows']
    original = actions[:original_count]
    extension = [a for a in actions[original_count:] if a['source'] == 'SZSE_OFFICIAL']
    # Historical 2020/2021 identified actions remain positive-only evidence.
    extension += [a for a in actions[original_count:] if a['source'] == 'SSE_OFFICIAL']
    raw, failures, coverage = list(inventory['raw_artifacts']), [], []
    for year in range(2020, 2026):
        for kind in ('dividend', 'bonus', 'rights'):
            for board in ((1, 2) if kind == 'rights' else (0,)):
                print(json.dumps({'source': 'SSE_OFFICIAL_SUCCESSOR', 'year': year, 'kind': kind, 'board': board}), flush=True)
                try:
                    rr, aa = acquire(kind, year, board)
                    raw.extend(rr); extension.extend(a for a in aa if a['historical_ticker'] in universe)
                    coverage.append({'source': 'SSE_OFFICIAL', 'year': year, 'kind': kind, 'board': board, 'state': 'QUALIFIED_BOUNDED_ACTION_TABLE', 'official_rows': sum(r['rows'] for r in rr)})
                except Exception as exc:
                    failures.append({'source': 'SSE_OFFICIAL', 'year': year, 'kind': kind, 'board': board, 'error_type': type(exc).__name__, 'detail': str(exc)[:300]})
                    coverage.append({'source': 'SSE_OFFICIAL', 'year': year, 'kind': kind, 'board': board, 'state': 'UNAVAILABLE_SOURCE'})
    # Independently bind the old SZSE positional parser to the official header.
    expected_headers = {0: 'code', 2: 'bonusshs', 3: 'bps', 4: 'cashdiv', 5: 'dps', 6: 'rtsissues', 7: 'rps', 8: 'plapri', 10: 'exdate', 11: 'regdate'}
    for c in inventory['coverage']:
        if c['source'] != 'SZSE_OFFICIAL': continue
        c = dict(c)
        rr = [r for r in inventory['raw_artifacts'] if r.get('period') == c['period'] and r.get('kind') == 'monthly_action_table']
        if len(rr) != 1: c['state'] = 'UNAVAILABLE_SOURCE'
        else:
            table = x.old.RowParser(); table.feed(x.old.decode_html(Path(rr[0]['file']).read_bytes(), {}))
            headers = [[re.sub('[^a-z]', '', cell.lower()) for cell in row] for row in table.rows]
            if not any(len(row) >= 12 and all(row[i] == value for i, value in expected_headers.items()) for row in headers):
                c['state'] = 'UNAVAILABLE_SCHEMA'; failures.append({'source': 'SZSE_OFFICIAL', 'period': c['period'], 'error_type': 'HEADER_MAPPING_UNVERIFIED'})
        coverage.append(c)
    combined = original + extension
    exclusions = [{'calendar_version': VERSION, 'historical_ticker': a['historical_ticker'], 'effective_ex_date': a['effective_ex_date'],
                   'action_types': a['action_types'], 'interval_rule': 'EXCLUDE_CLOSE_TO_CLOSE_INTERVAL_(PREVIOUS_ELIGIBLE_SESSION,CURRENT_SESSION]_CONTAINING_EFFECTIVE_EX_DATE',
                   'state': 'IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED', 'source': a['source'],
                   'source_artifact': a['source_artifact'], 'source_artifact_sha256': a['source_artifact_sha256']} for a in combined if a.get('effective_ex_date')]
    records = {}
    for key, rows, name in [('normalized_action_calendar', combined, 'official_action_calendar.jsonl'), ('exclusion_calendar', exclusions, 'v1_exclusion_calendar.jsonl')]:
        path = x.OUT / 'qualified_v2' / name; x.atomic(path, b''.join(x.old.canonical_json_bytes(r) for r in rows))
        records[key] = {'file': str(path), 'bytes': path.stat().st_size, 'sha256': x.digest(path), 'rows': len(rows)}
    ambiguous = [{'historical_ticker': a['historical_ticker'], 'scope': a.get('source_archive_year', a.get('source_archive_period')), 'source_artifact': a['source_artifact']} for a in extension if not a.get('effective_ex_date')]
    missing = [c for c in coverage if c['state'] != 'QUALIFIED_BOUNDED_ACTION_TABLE']
    m = {**inventory, **records, 'manifest_id': VERSION, 'raw_artifacts': raw, 'coverage': coverage,
         'acquisition_inventory_sha256': x.digest(x.PUBLIC), 'supersedes_inventory_coverage_claim': True,
         'official_successor_schema_url': SCRIPT, 'official_successor_schema_sha256': x.old.sha256(script_body),
         'qualification_time_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'failures': failures,
         'unavailable_scope': missing, 'ambiguous_effective_date_records': ambiguous,
         'qualification_status': 'QUALIFICATION_INCOMPLETE' if missing or failures else 'QUALIFIED_BOUNDED_C04_COVERAGE_WITH_EXPLICIT_UNAVAILABLE_RECORDS' if ambiguous else 'QUALIFIED_BOUNDED_C04_COVERAGE',
         'legacy_sse_empty_post2021_tables': 'NOT_NEGATIVE_COVERAGE_USE_OFFICIAL_SUCCESSOR_TABLES',
         'trading_ready': not missing and not failures and not ambiguous}
    x.validate_manifest(m)
    body = (json.dumps(m, ensure_ascii=False, sort_keys=True, indent=2)+'\n').encode('utf-8')
    x.atomic(x.OUT / 'qualified_v2/manifest.json', body); x.atomic(PUBLIC, body)
    print(json.dumps({'result': m['qualification_status'], 'scopes': len(coverage), 'unavailable_scopes': len(missing), 'ambiguous_records': len(ambiguous), 'failures': len(failures), 'manifest_sha256': x.digest(PUBLIC)}), flush=True)


if __name__ == '__main__': run()
