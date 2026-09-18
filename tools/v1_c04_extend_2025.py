"""Bounded official C04-A descendant; no prices, signals, candidates or PnL.

Reuse the frozen row parsers/taxonomy. Only archive range and physical location
change. Requests are checkpointed by URL/hash, never overwritten on resume.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import inspect
import json
import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import v1_c04_official_action_calendar as old

ROOT = old.ROOT
OUT = Path(r'D:\MechanismAwareStatArbData\C04_THROUGH_2025_V1')
ANCESTOR = ROOT / 'data/manifests/C04_A_OFFICIAL_CALENDAR_V1.json'
PUBLIC = ROOT / 'data/manifests/C04_A_THROUGH_2025_V1.json'
VERSION = 'C04-A-OFFICIAL-CALENDAR-THROUGH-2025-V1'
HOSTS = {'query.sse.com.cn', 'www.sse.com.cn', 'www.szse.cn', 'docs.static.szse.cn'}
NETWORK_FETCH = old.fetch


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(8 << 20), b''): h.update(b)
    return h.hexdigest().upper()


def atomic(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != body: raise RuntimeError(f'immutable conflict: {path}')
        return
    tmp = path.with_name(path.name + '.tmp')
    with tmp.open('wb') as f:
        f.write(body); f.flush(); os.fsync(f.fileno())
    if tmp.read_bytes() != body: raise RuntimeError('temporary write mismatch')
    os.replace(tmp, path)


def fetch(url, referer, attempts=4):
    if urlparse(url).hostname not in HOSTS: raise RuntimeError('unapproved source host')
    key = hashlib.sha256(url.encode()).hexdigest()
    path = OUT / 'transport' / (key + '.body')
    marker = path.with_suffix('.json')
    if marker.exists():
        meta = json.loads(marker.read_text())
        if meta['url'] != url or digest(path) != meta['sha256']: raise RuntimeError('transport hash mismatch')
        return path.read_bytes(), meta['headers']
    action = json.loads((ROOT / 'research/NEXT_ACTION.json').read_text(encoding='utf-8'))['action']
    budget = action.get('final_c04_budget')
    if budget and dt.datetime.now(dt.timezone.utc) >= dt.datetime.fromisoformat(budget['cutoff']):
        raise RuntimeError('Final C04 acquisition budget exhausted; no additional fetch permitted')
    body, headers = NETWORK_FETCH(url, referer, attempts)
    atomic(path, body)
    meta = {'url': url, 'referer': referer, 'sha256': digest(path), 'bytes': len(body),
            'retrieved_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'headers': headers}
    atomic(marker, old.canonical_json_bytes(meta))
    return body, headers


def write_raw(name, body):
    path = OUT / 'raw' / name
    atomic(path, body)
    return {'file': str(path), 'bytes': len(body), 'sha256': digest(path)}


def bind_parsers():
    old.VERSION = VERSION
    old.START_PERIOD, old.END_PERIOD = '2020-01', '2025-12'
    old.fetch, old.write_raw = fetch, write_raw
    sse = inspect.getsource(old.acquire_sse)
    if sse.count('range(2012, 2020)') != 1: raise RuntimeError('SSE range binding changed')
    sse = sse.replace('def acquire_sse(universe: set[str])', 'def acquire_sse_page(universe: set[str], selected_year, selected_kind, page_no=1)')
    sse = sse.replace('range(2012, 2020)', '(selected_year,)')
    sse = sse.replace('for kind in ("dividend", "bonus", "rights"):', 'for kind in (selected_kind,):')
    sse = sse.replace('url = sse_url(kind, year)', 'url = page_url(kind, year, page_no)')
    sse = sse.replace('f"sse_{kind}_{year}.json"', 'f"sse_{kind}_{year}_p{page_no}.json"')
    old.page_url = page_url
    exec(compile(sse, '<frozen-sse-paginated-range-extension>', 'exec'), old.__dict__)
    szse = inspect.getsource(old.acquire_szse)
    if szse.count('expected_periods = 85') != 1: raise RuntimeError('SZSE range binding changed')
    exec(compile(szse.replace('expected_periods = 85', 'expected_periods = 72'), '<frozen-szse-range-extension>', 'exec'), old.__dict__)


def page_url(kind, year, page):
    parsed = urlparse(old.sse_url(kind, year))
    query = parse_qs(parsed.query)
    for key in ('pageHelp.pageNo', 'pageHelp.beginPage', 'pageHelp.endPage'):
        query[key] = [str(page)]
    return urlunparse(parsed._replace(query=urlencode(query, doseq=True)))


def acquire_sse(universe):
    raw, actions, failures = [], [], []
    for year in range(2020, 2026):
        for kind in ('dividend', 'bonus', 'rights'):
            first, aa, ff = old.acquire_sse_page(universe, year, kind)
            raw += first; actions += aa; failures += ff
            if not first: continue
            page = json.loads(Path(first[0]['file']).read_text(encoding='utf-8')).get('pageHelp') or {}
            total, count = page.get('total'), len(page.get('data') or [])
            if total is None or (int(total) > 0 and count == 0): continue
            pages = (int(total)+count-1)//count if count else 1
            for number in range(2, pages+1):
                rr, aa, ff = old.acquire_sse_page(universe, year, kind, number)
                raw += rr; actions += aa; failures += ff
    return raw, actions, failures


def validate_manifest(m):
    errors = []
    if digest(ANCESTOR) != m['ancestor_manifest_sha256']: errors.append('ancestor_manifest')
    for r in m['raw_artifacts']:
        p = Path(r['file']); p = p if p.is_absolute() else ROOT / p
        if digest(p) != r['sha256'] or p.stat().st_size != r['bytes']: errors.append('raw_hash')
        if urlparse(r['url']).hostname not in HOSTS: errors.append('source_host')
    for key in ('normalized_action_calendar', 'exclusion_calendar'):
        r = m[key]
        if digest(r['file']) != r['sha256']: errors.append(key)
    if m['authoritative_action_clean'] or m['pnl_computed_or_inspected']: errors.append('boundary')
    if errors: raise RuntimeError('C04 descendant integrity failure: ' + ','.join(errors))


def run():
    action = json.loads((ROOT / 'research/NEXT_ACTION.json').read_text())['action']
    if action['status'] != 'AUTHORIZED' or not action.get('c04_extension_authorization'):
        raise RuntimeError('explicit C04 extension authority required')
    if PUBLIC.exists():
        m = json.loads(PUBLIC.read_text(encoding='utf-8')); validate_manifest(m)
        print(json.dumps({'result': m['qualification_status'], 'checkpoint': 'HASH_VERIFIED_SKIP'}))
        return 0 if m['qualification_status'] == 'QUALIFIED_BOUNDED_C04_COVERAGE' else 2
    ancestor = json.loads(ANCESTOR.read_text(encoding='utf-8'))
    if ancestor['calendar_scope']['last_archive_period'] != '2019-12' or not ancestor['validated']:
        raise RuntimeError('ancestor qualification mismatch')
    acquired = json.loads(old.ACQUISITION_MANIFEST.read_text(encoding='utf-8'))
    tickers = sorted({str(e.get('params', {}).get('ts_code', '')) for e in acquired['events']
                      if e.get('contract') == 'C03' and old.re.fullmatch(r'\d{6}\.(SH|SZ)', str(e.get('params', {}).get('ts_code', '')))})
    if len(tickers) != 751: raise RuntimeError('complete frozen universe mismatch')
    universe = {x[:6] for x in tickers}
    bind_parsers()
    print(json.dumps({'stage': 'SSE_OFFICIAL_18_YEAR_KIND_REQUESTS', 'universe': len(tickers)}), flush=True)
    sr, sa, sf = acquire_sse(universe)
    print(json.dumps({'stage': 'SZSE_OFFICIAL_72_MONTHS', 'sse_failures': len(sf)}), flush=True)
    try:
        zr, za, zf = old.acquire_szse(universe)
    except Exception as exc:
        zr, za, zf = [], [], [{'source': 'SZSE_OFFICIAL', 'period': '2020-01/2025-12', 'error_type': type(exc).__name__, 'error_detail': str(exc)[:240]}]
    failures = sf + zf
    # Do not infer full official-table coverage merely from a successful HTTP response.
    coverage = []
    for year in range(2020, 2026):
        for kind in ('dividend', 'bonus', 'rights'):
            records = [r for r in sr if r.get('year') == year and r.get('kind') == kind]
            state = 'UNAVAILABLE_SOURCE'
            if records:
                pages = [(json.loads(Path(r['file']).read_text(encoding='utf-8')).get('pageHelp') or {}) for r in records]
                totals = {int(p['total']) for p in pages if p.get('total') is not None}
                downloaded = sum(len(p.get('data') or []) for p in pages)
                observed_pages = {int(p.get('pageNo', -1)) for p in pages}
                if len(totals) == 1 and len(pages) == len(records) and observed_pages == set(range(1, len(pages)+1)) and downloaded == next(iter(totals)) and all(p.get('total') is not None for p in pages):
                    state = 'QUALIFIED_BOUNDED_ACTION_TABLE'
                else:
                    failures.append({'source': 'SSE_OFFICIAL', 'year': year, 'kind': kind,
                                     'error_type': 'TABLE_COMPLETENESS_UNPROVEN', 'totals': sorted(totals),
                                     'downloaded_rows': downloaded})
            coverage.append({'source': 'SSE_OFFICIAL', 'year': year, 'kind': kind, 'state': state})
    for year in range(2020, 2026):
        for month in range(1, 13):
            period = f'{year}-{month:02d}'
            records = [r for r in zr if r.get('period') == period and r.get('kind') == 'monthly_action_table']
            state = 'QUALIFIED_BOUNDED_ACTION_TABLE' if len(records) == 1 and not any(f.get('period') == period for f in zf) else 'UNAVAILABLE_SOURCE'
            coverage.append({'source': 'SZSE_OFFICIAL', 'period': period, 'kind': 'dividend_bonus_rights', 'state': state})
    original = [json.loads(line) for line in (ROOT / ancestor['normalized_action_calendar']['file']).read_text(encoding='utf-8').splitlines()]
    # Preserve inherited rows exactly; new rows keep missing publication fields unavailable.
    actions = original + sorted(sa + za, key=lambda a: (a['historical_ticker'], str(a.get('effective_ex_date')), a['source_artifact']))
    exclusions = []
    for a in actions:
        if not a.get('effective_ex_date'): continue
        exclusions.append({'calendar_version': VERSION, 'historical_ticker': a['historical_ticker'],
                           'effective_ex_date': a['effective_ex_date'], 'action_types': a['action_types'],
                           'interval_rule': 'EXCLUDE_CLOSE_TO_CLOSE_INTERVAL_(PREVIOUS_ELIGIBLE_SESSION,CURRENT_SESSION]_CONTAINING_EFFECTIVE_EX_DATE',
                           'state': 'IDENTIFIED CORPORATE ACTION — V1 INTERVAL EXCLUDED', 'source': a['source'],
                           'source_artifact': a['source_artifact'], 'source_artifact_sha256': a['source_artifact_sha256']})
    records = {}
    for key, rows, filename in [('normalized_action_calendar', actions, 'official_action_calendar.jsonl'), ('exclusion_calendar', exclusions, 'v1_exclusion_calendar.jsonl')]:
        path = OUT / 'derived' / filename
        atomic(path, b''.join(old.canonical_json_bytes(r) for r in rows))
        records[key] = {'file': str(path), 'bytes': path.stat().st_size, 'sha256': digest(path), 'rows': len(rows)}
    missing = [c for c in coverage if c['state'] != 'QUALIFIED_BOUNDED_ACTION_TABLE']
    unresolved = [{'historical_ticker': a['historical_ticker'], 'source_artifact': a['source_artifact'], 'source_archive_period': a.get('source_archive_period')} for a in sa + za if not a.get('effective_ex_date')]
    m = {'manifest_id': VERSION, 'ancestor_manifest': str(ANCESTOR), 'ancestor_manifest_sha256': digest(ANCESTOR),
         'parser_source_sha256': digest(Path(old.__file__)), 'qualification_time_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
         'universe': tickers, 'universe_count': len(tickers), 'requested_coverage': '2013-01-07/2025-12-31',
         'extension_archives': '2020-01/2025-12', 'coverage': coverage, 'unavailable_scope': missing,
         'raw_artifacts': ancestor['raw_artifacts'] + sr + zr, 'failures': failures, 'ambiguous_effective_date_records': unresolved,
         'qualification_status': 'QUALIFIED_BOUNDED_C04_COVERAGE' if not failures and not missing and not unresolved else 'QUALIFICATION_INCOMPLETE',
         'qualified_no_action': 'NO_IDENTIFIED_ACTION_UNDER_QUALIFIED_BOUNDED_SOURCE_TABLES_ONLY',
         'authoritative_action_clean': False, 'pnl_computed_or_inspected': False, 'old_calendar_overwritten': False,
         'source_contracts': ancestor['source_contract'], 'nonclaim': ancestor['nonclaim'], **records}
    validate_manifest(m)
    body = (json.dumps(m, ensure_ascii=False, indent=2, sort_keys=True)+'\n').encode('utf-8')
    atomic(OUT / 'manifest.json', body); atomic(PUBLIC, body)
    print(json.dumps({'result': m['qualification_status'], 'qualified_extension_scopes': len(coverage)-len(missing),
                      'total_extension_scopes': len(coverage), 'failures': len(failures),
                      'unresolved_records': len(unresolved), 'manifest_sha256': digest(PUBLIC)}), flush=True)
    return 0 if m['qualification_status'] == 'QUALIFIED_BOUNDED_C04_COVERAGE' else 2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['run', 'validate'])
    args = parser.parse_args()
    if args.command == 'validate':
        m = json.loads(PUBLIC.read_text(encoding='utf-8')); validate_manifest(m)
        print(json.dumps({'integrity': 'PASS', 'qualification': m['qualification_status'], 'pnl_accessed': False}))
    else:
        raise SystemExit(run())
