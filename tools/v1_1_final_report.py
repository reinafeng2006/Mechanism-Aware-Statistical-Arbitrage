"""Reveal only validated complete-fold metrics; retain unavailable scope."""
import datetime as dt
import json
from collections import Counter
from pathlib import Path
import v1_1_trading as t
import v1_c04_extend_2025 as x

PUBLIC = t.ROOT/'data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json'
DOC = t.ROOT/'docs/stages/G5/V1_1_FINAL_ECONOMIC_EVIDENCE.md'


def main():
    t.validate()
    receipt=t.read(t.OUT/'validation.json')
    if receipt['status']!='PASS' or receipt['bindings']!=t.bindings(): raise RuntimeError('reveal gate failed')
    event=t.OUT/'first_result_inspection_event.json'
    if not event.exists():t.atomic(event,{'time_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'validation_sha256':x.digest(t.OUT/'validation.json'),'scope':'Complete-fold metrics and coverage only; no partial-prefix return interpretation'})
    units=[]; ledger=[]; stats=[]
    for c,f in t.specs():
        p=t.OUT/'units'/(c+'__'+f+'.json');r=t.read(p)
        units.append({'candidate':c,'fold':f,'path':str(p),'sha256':x.digest(p),'marker_sha256':x.digest(p.with_suffix('.sha256.json'))})
        for b in r['books']:
            ledger.append({'candidate':c,'fold':f,'role':'inner','cost_bps':b['cost_bps'],'status':b['status'],
                           'metrics':b['metrics'],'unavailable':b['unavailable'],
                           'coverage':b['coverage_until_first_unavailable_interval'],
                           'qualified_marked_sessions':b['qualified_marked_sessions'],
                           'expected_fold_sessions':r['expected_fold_sessions'],
                           'coverage_after_unavailable':b['coverage_after_unavailable']})
        stats.append({'candidate':c,'fold':f,**r['signal_counts_until_all_books_unavailable']})
    for c in t.read(t.POLICY)['candidates']:
        for y in range(2020,2026):
            for bps in (5,10,20):
                ledger.append({'candidate':c,'fold':str(y),'role':'of4' if y<2024 else 'heldout','cost_bps':bps,
                               'status':'ECONOMICALLY_UNAVAILABLE_INPUT_LINEAGE','metrics':None,
                               'coverage':'NOT_COMPUTED_UNQUALIFIED_IMMUTABLE_C04_RESPONSE_ANCESTRY'})
    qualified=sum(r['status']=='QUALIFIED' for r in ledger)
    result={'evidence_id':'TRADING-V1-1-FINAL-EVIDENCE-1.0','status':'VALIDATED_TERMINAL_WITH_EXPLICIT_UNAVAILABLE_SCOPE',
            'h6_disposition':'LIMITED_INNER_EXPLORATORY_EVIDENCE_ONLY_NO_FULL_PERIOD_DISPOSITION' if qualified else 'ECONOMICALLY_UNAVAILABLE_NO_COMPLETE_FOLD_H6_DISPOSITION',
            'policy_sha256':x.digest(t.POLICY),'input_qualification_sha256':x.digest(t.QUAL),
            'external_validation':{'path':str(t.OUT/'validation.json'),'sha256':x.digest(t.OUT/'validation.json')},
            'inspection_event':{'path':str(event),'sha256':x.digest(event)},
            'units':units,'book_cost_fold_ledger':ledger,'signal_coverage_prefixes':stats,
            'total_book_cost_fold_dispositions':len(ledger),'qualified_complete_cost_folds':qualified,
            'unavailable_metrics_are_zero':False,'partial_prefix_returns_reported_as_complete':False,
            'coverage_caveat':'Coverage counts stop at first unknown portfolio NAV per cost-book; later opportunities/funding and full-fold rates are unavailable, not zero.',
            'raw_metric_caveat':'Raw PnL adds paid costs to the same realized execution path; not a reallocated frictionless counterfactual.',
            'cross_fold_aggregation':'NONE_NO_NEW_TRADING_AGGREGATION_RULE','optimization_or_rescue':False,
            'original_a6_g5':'V1_NON_ESTIMABLE_NOT_EXECUTED','v2_executed':False}
    t.atomic(PUBLIC,result)
    lines=['# Trading V1.1 final economic evidence','',
           'Status: **TERMINAL / VALIDATED WITH EXPLICIT UNAVAILABLE SCOPE**.','',
           f"H6: `{result['h6_disposition']}`.",'',
           'One-shot inner execution: 60 candidate/fold checkpoints, all 180 cost-books validated before first disclosure. '+
           'The ledger also records 108 uncomputed OF4/held-out cost-fold books as input-lineage unavailable. '+
           'Unavailable is not zero return, a losing trade, or a supported/rejected profitability hypothesis.','',
           'No complete-book metric is inferred from a qualified prefix. No book is restarted or survivor-renormalized after an unqualified held interval. '+
           'No new across-fold mean/median, ranking, p-value, threshold or winner is introduced.','',
           '## All six books and all three frozen costs','',
           '| Candidate | Cost bps | Inner complete / 10 | Inner unavailable / 10 | OF4 / held-out | Peer / source entries observed | Short unavailable observed | Funding unavailable observed | Coexistence sessions observed |',
           '|---|---:|---:|---:|---|---|---:|---:|---:|']
    for c in t.read(t.POLICY)['candidates']:
        for bps in (5,10,20):
            rr=[r for r in ledger if r['candidate']==c and r['role']=='inner' and r['cost_bps']==bps]
            cc=Counter()
            for r in rr:cc.update(r['coverage'])
            n=sum(r['status']=='QUALIFIED' for r in rr)
            lines.append(f"| {c} | {bps} | {n} | {10-n} | Unavailable / unavailable | {cc['peer_entries']} / {cc['source_entries']} | {cc['peer_short_execution_unavailable']+cc['source_short_execution_unavailable']} | {cc['peer_funding_unavailable']+cc['source_funding_unavailable']} | {cc['coexistence_sessions']} |")
    lines += ['', '**Coverage is observed prefix coverage, not full-period deployability.** '+
              'The checksum-bound ledger retains channel-specific entry, blocked re-entry, entry-execution-unavailable, funding-unavailable, '+
              'short-unavailable, conflict, MP1-unavailable and coexistence counts. Counts after the first unevaluable portfolio interval are not fabricated.','',
              '## Qualified complete-fold returns only','',
              '| Candidate | Fold | Cost bps | Net cumulative | Annualized return | Annualized vol | Sharpe | Maximum drawdown | Turnover | Open terminal episodes |',
              '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in ledger:
        if r['status']!='QUALIFIED':continue
        m=r['metrics'];fmt=lambda v:'Unavailable' if v is None else f'{v:.10g}'
        lines.append('| '+' | '.join([r['candidate'],r['fold'],str(r['cost_bps'])]+[fmt(m[k]) for k in ['net_cumulative_return','annualized_return_252','annualized_volatility','zero_rate_sharpe','maximum_drawdown','turnover_sum_net_notional_over_pre_nav','open_terminal_episodes']])+' |')
    if not qualified:lines.append('| All six books | All inner folds | 5 / 10 / 20 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable as full-fold metric | Preserved in private checkpoint state |')
    reasons=Counter(r['unavailable']['reason'] for r in ledger if r.get('unavailable'))
    lines += ['','## Unavailable accounting scope','',
              '| Reason | Cost-fold books |','|---|---:|']+[f'| {k} | {v} |' for k,v in sorted(reasons.items())]
    lines += ['| Immutable post-2019 input C04 exclusion mismatch | 108 |','',
              'The official calendar itself passed the original bounded C04-A exclusion contract. '+
              'However, the later model-input masks omit newly identified action exclusions; a trading overlay cannot retroactively qualify those immutable predictions. '+
              'Inner T09 failures and exact date/security indices are retained in the evidence ledger. '+
              'No entitlement, adjusted-price substitution, borrowing or delayed-entry search was invented.','',
              'Both channels remain morphology-only economic probes, not M1/M2/M0 identification. '+
              'Original A6/G5 stays V1 NON-ESTIMABLE / NOT EXECUTED. H4 remains computationally incomplete.','',
              '[Complete checksum-bound evidence ledger](../../../data/manifests/TRADING_V1_1_FINAL_EVIDENCE.json). '+
              '[Input qualification and later-book limitation](V1_1_FINAL_INPUT_QUALIFICATION.md).','']
    x.atomic(DOC,'\n'.join(lines).encode('utf-8'))
    print(json.dumps({'report':str(DOC),'h6':result['h6_disposition'],'complete_cost_folds':qualified,'total_dispositions':len(ledger),'unavailable_reasons':dict(reasons)}))


if __name__=='__main__':main()
