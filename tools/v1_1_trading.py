"""One-shot frozen Trading V1.1; validated inner inputs only, no policy search.

One checkpoint per candidate/fold, all three non-selection costs together.
No empirical values on stdout. T09 invalidates the complete book at the first
unqualified held interval; subsequent funding cannot be invented from unknown
NAV. Partial paths are retained privately and never called full-fold returns.
"""
import argparse
import csv
import datetime as dt
import gzip
import hashlib
import json
import math
import os
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
from v1_1_accounting import allocate, exit_trigger
import v1_c04_extend_2025 as x

ROOT = x.ROOT
OUT = Path('D:/MechanismAwareStatArbData/TRADING_V1_1')
POLICY = ROOT/'research/TRADING_V1_1_POLICY.json'
QUAL = ROOT/'data/manifests/TRADING_V1_1_INPUT_QUALIFICATION.json'
SIDECAR = ROOT/'data/qa_work/g3b_f2/security_date_eligibility/v1/security_date_eligibility_sidecar_v1.csv.gz'
BASE = ROOT/'data/qa_work/v1/phase1/inner_outputs_v2'
POLICY_SHA = '851EC63DB822E889F9DC103C87B63BCBAF93EA48810941731686D43CA28A9786'


def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def encode(obj): return (json.dumps(obj, sort_keys=True, indent=2, allow_nan=False)+'\n').encode()


def atomic(p, obj, replace=False):
    p.parent.mkdir(parents=True, exist_ok=True)
    body = encode(obj)
    if p.exists() and not replace:
        if p.read_bytes() != body: raise RuntimeError('immutable output conflict')
        return
    tmp = p.with_name(p.name+'.tmp')
    with tmp.open('wb') as f:
        f.write(body); f.flush(); os.fsync(f.fileno())
    if tmp.read_bytes() != body: raise RuntimeError('temporary verification failed')
    os.replace(tmp, p)


def bindings():
    return {'policy': x.digest(POLICY), 'qualification': x.digest(QUAL),
            'engine': x.digest(Path(__file__)), 'accounting': x.digest(ROOT/'tools/v1_1_accounting.py')}


def specs():
    for c in read(POLICY)['candidates']:
        for y in range(2015, 2020):
            for h in (1, 2): yield c, f'{y}H{h}'


def load_inputs():
    q = read(QUAL)
    r = next(r for r in q['roles'] if r['role'] == 'inner')
    if r['status'] != 'PASS' or x.digest(r['input']) != r['sha256']: raise RuntimeError('inner lineage unqualified')
    with np.load(r['input'], allow_pickle=False) as f: data = {k:f[k] for k in f.files}
    dates = np.char.decode(data['dates']); codes = np.char.decode(data['codes'])
    di = {str(v):i for i,v in enumerate(dates)}; ci = {str(v):i for i,v in enumerate(codes)}
    normal = np.zeros(data['open'].shape, bool)
    suspended = np.zeros_like(normal)
    with gzip.open(SIDECAR, 'rt', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            t, s = di.get(row['observation_date']), ci.get(row['historical_ticker_code'])
            if t is None or s is None: continue
            identity = row['identifier_lineage_state'] == 'DIRECT C01/C03 IDENTIFIER'
            normal[t,s] = identity and row['c05_structural_state'] == 'NORMAL TRADING OBSERVED'
            # No guessed suspension labels or price carries: missing qualified
            # valuation still makes the portfolio interval unavailable.
            suspended[t,s] = identity and row['c05_structural_state'] == 'OFFICIAL SUSPENSION CONFIRMED'
    audit = read(ROOT/'data/manifests/C04_A_THROUGH_2025_FINAL_AUDIT.json')
    action = np.zeros_like(normal)
    for line in Path(audit['exclusion_calendar']['file']).read_text(encoding='utf-8').splitlines():
        row = json.loads(line); t = di.get(row['effective_ex_date'].replace('-', '')); s = ci.get(row['historical_ticker'])
        if t is not None and s is not None: action[t,s] = True
    # Exact candidate-neutral MP1 H126/U1W. History is appended only AFTER
    # evaluating the current event; no expanding/fallback reference.
    mp1 = np.full_like(data['amount'], np.nan)
    qualified = normal & ~action & np.isfinite(data['amount']) & np.isfinite(data['volume']) & (data['amount']>0) & (data['volume']>0)
    ratio = np.divide(data['amount'], data['volume'], out=np.full_like(mp1, np.nan), where=qualified)
    qualified &= np.isfinite(ratio) & (ratio>0)
    weeks = [dt.datetime.strptime(str(d), '%Y%m%d').isocalendar()[:2] for d in dates]
    for s in range(len(codes)):
        hist = []; last_week = None; reference = np.nan
        for t in range(len(dates)):
            if not qualified[t,s]: continue
            if weeks[t] != last_week:
                reference = float(np.median(hist[-126:])) if len(hist)>=126 else np.nan
                last_week = weeks[t]
            if np.isfinite(reference) and reference>0: mp1[t,s] = math.log(ratio[t,s]/reference)
            hist.append(float(ratio[t,s]))
    return {**data, 'date_text': dates, 'normal': normal, 'suspended': suspended, 'action': action, 'mp1': mp1}


def signals(rows, a3, mp1):
    """Return original-anchor proposals; never reads future A5 targets."""
    valid = np.all(np.isfinite(a3), axis=1)
    names = rows.dtype.names
    ma = rows['mu_n1_ab' if 'mu_n1_ab' in names else 'mu_ab'].astype(float)
    mb = rows['mu_n1_ba' if 'mu_n1_ba' in names else 'mu_ba'].astype(float)
    a, b = rows['a'].astype(int), rows['b'].astype(int)
    # A3 columns are immutable departures/scaled departures. Source of AB is
    # a, so its excess/MP0 are the reverse directional A3 columns.
    ga, gb = -a3[:,0].astype(float), -a3[:,2].astype(float)
    peer_a = valid & np.isfinite(ma) & (ma!=0) & (np.sign(ma)*ga>0)
    peer_b = valid & np.isfinite(mb) & (mb!=0) & (np.sign(mb)*gb>0)
    source_a = valid & (a3[:,2]!=0) & (a3[:,3]!=0) & np.isfinite(mp1[a]) & (mp1[a]>0)
    source_b = valid & (a3[:,0]!=0) & (a3[:,1]!=0) & np.isfinite(mp1[b]) & (mp1[b]>0)
    proposals = []; counts = Counter()
    for ch, left, right, sl, sr, al, ar in [
        (0, peer_a, peer_b, b, a, ga, gb),
        (1, source_a, source_b, a, b, a3[:,2], a3[:,0])]:
        label = 'peer' if ch==0 else 'source'
        counts[label+'_directional_eligible'] += int(left.sum()+right.sum())
        collision = left & right
        counts[label+'_directional_conflict_pairs'] += int(collision.sum())
        for mask, secs, anchors in ((left & ~right, sl, al), (right & ~left, sr, ar)):
            for i in np.flatnonzero(mask):
                anchor = float(anchors[i]); direction = (1 if anchor>0 else -1)*(1 if ch==0 else -1)
                proposals.append(((int(a[i]),int(b[i]),ch), int(secs[i]), anchor, direction))
    counts['source_mp1_unavailable_directional'] = int((valid & ~np.isfinite(mp1[a])).sum()+(valid & ~np.isfinite(mp1[b])).sum())
    return proposals, counts


class Book:
    def __init__(self, bps):
        self.bps=bps; self.cost=bps/10000.; self.cash=1.; self.active={}; self.pending=[]
        self.path=[1.]; self.days=[]; self.counts=Counter(); self.turnover=0.; self.fees=0.; self.status='QUALIFIED'
        self.failure=None; self.execution_log=[]; self.gross=[]; self.net=[]; self.open_episodes=0

    def fail(self, t, reason, securities):
        self.status='ECONOMICALLY_UNAVAILABLE'; self.failure={'date_ix':int(t),'reason':reason,'securities':sorted(set(map(int,securities)))}

    def day(self, t, data, new_signals, last_day=False):
        if self.status!='QUALIFIED': return
        op=data['open'][t]; cp=data['close'][t]; normal=data['normal'][t]; act=data['action'][t]
        # Do not expost delete an affected holding and reallocate survivors.
        held=[e['security'] for e in self.active.values()]
        bad=[s for s in held if act[s]]
        if bad: self.fail(t,'C04_ACTION_WITHOUT_QUALIFIED_ENTITLEMENT',bad); return
        bad=[s for s in held if not normal[s] or not np.isfinite(op[s]) or op[s]<=0]
        if bad: self.fail(t,'UNQUALIFIED_HELD_OPEN_PRICE_OR_C05_ID',bad); return
        old_active=len(self.active)
        existing=defaultdict(float); exits=defaultdict(float); exit_keys=[]
        for key,e in self.active.items():
            value=e['shares']*float(op[e['security']])
            if e['exit_pending']: exits[e['security']]+=value; exit_keys.append(key)
            else: existing[e['security']]+=value
        pre=self.cash+math.fsum(existing.values())+math.fsum(exits.values())
        available=[]
        for key,s,anchor,direction in self.pending:
            ch='peer' if key[2]==0 else 'source'
            if direction<0: self.counts[ch+'_short_execution_unavailable']+=1; continue
            if not normal[s] or act[s] or not np.isfinite(op[s]) or op[s]<=0:
                self.counts[ch+'_entry_execution_unavailable']+=1; continue
            available.append((key,s,anchor))
        plan=allocate(pre,self.cash+math.fsum(exits.values()),dict(existing),dict(exits),[s for _,s,_ in available],old_active-len(exit_keys),self.cost)
        for key in exit_keys: del self.active[key]
        self.counts['exits']+=len(exit_keys)
        for key,s,anchor in available:
            ch='peer' if key[2]==0 else 'source'; size=plan['per_proposal_by_security'][s]
            if size<=0: self.counts[ch+'_funding_unavailable']+=1; continue
            if key in self.active: raise RuntimeError('episode identity overlap')
            self.active[key]={'security':s,'shares':size/float(op[s]),'anchor':anchor,'cum':0.,'sessions':0,'exit_pending':False}
            self.counts[ch+'_entries']+=1
        self.cash=plan['cash']; self.fees+=plan['fee']
        traded=math.fsum(abs(plan['purchases'].get(k,0)-exits.get(k,0)) for k in sorted(set(exits)|set(plan['purchases'])))
        self.turnover+=traded/pre
        if traded or available:
            self.execution_log.append({'date_ix':int(t),'A':old_active-len(exit_keys),'B':plan['B'],'N':plan['N'],
                                       'cash_after':self.cash,'fee':plan['fee'],'net_turnover_notional':traded})
        self.pending=[]
        bad=[e['security'] for e in self.active.values() if not normal[e['security']] or not np.isfinite(cp[e['security']]) or cp[e['security']]<=0]
        if bad: self.fail(t,'UNQUALIFIED_HELD_CLOSE_PRICE_OR_C05_ID',bad); return
        marked=defaultdict(float)
        for e in self.active.values(): marked[e['security']]+=e['shares']*float(cp[e['security']])
        nav=self.cash+math.fsum(marked.values())
        if not math.isfinite(nav) or nav<=0: self.fail(t,'UNQUALIFIED_BOOK_NAV',[]); return
        gross=math.fsum(marked.values())/nav
        self.gross.append(gross); self.net.append(gross)
        if gross>1 or any(v/nav>.1 for v in marked.values()): self.counts['passive_cap_drift_sessions']+=1
        if any(k[2]==0 for k in self.active) and any(k[2]==1 for k in self.active): self.counts['coexistence_sessions']+=1
        for key,e in self.active.items():
            s=e['security']
            if not data['response_ok'][t,s] or not np.isfinite(data['response'][t,s]):
                self.fail(t,'UNQUALIFIED_HELD_RESPONSE_INTERVAL',[s]); return
            e['cum']+=float(data['response'][t,s]); e['sessions']+=1
            if exit_trigger(e['anchor'],e['cum'],key[2],e['sessions']): e['exit_pending']=True
        self.path.append(nav); self.days.append(int(t))
        for item in new_signals:
            key=item[0]; ch='peer' if key[2]==0 else 'source'
            if key in self.active: self.counts[ch+'_blocked_reentry']+=1
            elif last_day: self.counts[ch+'_no_in_fold_entry_open']+=1
            else: self.pending.append(item)
        self.open_episodes=len(self.active)

    def result(self):
        metrics=None
        if self.status=='QUALIFIED':
            v=np.asarray(self.path); r=v[1:]/v[:-1]-1; n=len(r)
            sd=float(np.std(r,ddof=1)) if n>1 else None
            metrics={'net_cumulative_return':float(v[-1]-1), 'raw_pnl_before_charged_costs_same_executed_path':float(v[-1]-1+self.fees),
                     'annualized_return_252':float(v[-1]**(252/n)-1) if n else None,
                     'annualized_volatility':sd*math.sqrt(252) if sd is not None else None,
                     'zero_rate_sharpe':float(np.mean(r)/sd*math.sqrt(252)) if sd and sd>0 else None,
                     'maximum_drawdown':float(np.max(1-v/np.maximum.accumulate(v))),
                     'turnover_sum_net_notional_over_pre_nav':self.turnover,'charged_costs':self.fees,
                     'terminal_cash':self.cash,'terminal_gross_and_net':self.gross[-1] if self.gross else 0.,'open_terminal_episodes':self.open_episodes}
        return {'cost_bps':self.bps,'status':self.status,'unavailable':self.failure,'metrics':metrics,
                'coverage_until_first_unavailable_interval':dict(self.counts),'qualified_marked_sessions':len(self.days),
                'coverage_after_unavailable': 'NOT_COMPUTED_UNKNOWN_NAV_NO_RENORMALIZATION' if self.failure else 'COMPLETE',
                'private_qualified_prefix_nav':self.path,'private_qualified_prefix_date_ix':self.days,'execution_log':self.execution_log,
                'private_preserved_episode_state':[{'identity':list(k),**e} for k,e in sorted(self.active.items())]}


def completed(c, fold):
    uid=c+'__'+fold; marker=OUT/'units'/(uid+'.sha256.json'); path=OUT/'units'/(uid+'.json')
    if not marker.exists():
        if path.exists(): raise RuntimeError('unverified finalized output; do not recompute/overwrite')
        return False
    m=read(marker)
    if x.digest(path)!=m['sha256'] or m['bindings']!=bindings(): raise RuntimeError('checkpoint hash/binding mismatch')
    return True


def progress():
    done=[c+'__'+f for c,f in specs() if completed(c,f)]
    atomic(OUT/'progress.json',{'completed_units':len(done),'total_units':60,'units':done,'bindings':bindings()},replace=True)
    return len(done)


def run():
    a=read(ROOT/'research/NEXT_ACTION.json')['action']
    if a['status']!='AUTHORIZED' or a['action_id']!='TRADING-V1-1-BATCH-EXECUTION' or x.digest(POLICY)!=POLICY_SHA: raise RuntimeError('authority/policy failure')
    q=read(QUAL)
    if any(r['status']=='PASS' for r in q['roles'] if r['role']!='inner'): raise RuntimeError('this engine is restricted to qualified inner')
    event=OUT/'execution_event.json'
    if not event.exists(): atomic(event,{'event':'ONE_SHOT_TRADING_V1_1_START','time_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'bindings':bindings(),'pnl_inspection_permitted':False})
    elif read(event)['bindings']!=bindings(): raise RuntimeError('one-shot execution bindings changed')
    data=load_inputs()
    rm=read(ROOT/'data/manifests/V1_PHASE1_RELATIONSHIP_OUTPUTS.json')
    am=read(ROOT/'data/manifests/V1_INNER_A3_A5.json')
    for c,fold in specs():
        if completed(c,fold): print(json.dumps({'unit':c+'__'+fold,'status':'HASH_VERIFY_SKIP'}),flush=True); continue
        rp=BASE/'relationships'/c/(fold+'.npy'); ap=BASE/'a3_a5'/c/(fold+'.a3.npy')
        rr=next(r for r in rm['partitions'] if r['candidate']==c and r['partition']==fold)
        ar=next(r for r in am['partitions'] if r['candidate']==c and r['partition']==fold)
        rh=x.digest(rp); ah=x.digest(ap)
        if rh!=rr['sha256'] or ah!=ar['a3_sha256']: raise RuntimeError('immutable scientific ancestor hash mismatch')
        rel=np.load(rp,mmap_mode='r',allow_pickle=False); a3=np.load(ap,mmap_mode='r',allow_pickle=False)
        if len(rel)!=len(a3): raise RuntimeError('A3 row lineage mismatch')
        order=np.argsort(rel['date_ix'],kind='stable'); ix=rel['date_ix'][order]
        year=fold[:4]; half=int(fold[-1]); lower=year+('0101' if half==1 else '0701'); upper=year+('0630' if half==1 else '1231')
        days=np.flatnonzero((data['date_text']>=lower)&(data['date_text']<=upper))
        books=[Book(b) for b in read(POLICY)['cost_bps']]; counts=Counter()
        for t in days:
            if all(b.status!='QUALIFIED' for b in books): break
            left,right=np.searchsorted(ix,t,side='left'),np.searchsorted(ix,t,side='right')
            ids=order[left:right]
            proposals, cc=signals(rel[ids],a3[ids],data['mp1'][t]); counts.update(cc)
            for b in books: b.day(int(t),data,proposals,t==days[-1])
        result={'candidate':c,'fold':fold,'role':'inner','bindings':bindings(),'relationship_sha256':rh,'a3_sha256':ah,
                'signal_counts_until_all_books_unavailable':dict(counts),'books':[b.result() for b in books],
                'interpretation':'EXPLORATORY_MORPHOLOGY_NOT_MECHANISM','expected_fold_sessions':len(days),
                'no_post_failure_capital_reset':True}
        path=OUT/'units'/(c+'__'+fold+'.json'); atomic(path,result)
        atomic(path.with_suffix('.sha256.json'),{'sha256':x.digest(path),'bindings':bindings()})
        print(json.dumps({'unit':c+'__'+fold,'status':'FINALIZED_HASHED','completed':progress(),'total':60}),flush=True)
    validate()


def validate():
    count=progress()
    if count!=60: raise RuntimeError('incomplete one-shot execution')
    for c,f in specs():
        r=read(OUT/'units'/(c+'__'+f+'.json'))
        if [b['cost_bps'] for b in r['books']]!=[5,10,20]: raise RuntimeError('cost coverage')
        for b in r['books']:
            if b['status']=='ECONOMICALLY_UNAVAILABLE' and (b['metrics'] is not None or not b['unavailable']): raise RuntimeError('unavailable metrics fabricated')
            if b['status']=='QUALIFIED' and b['qualified_marked_sessions']!=r['expected_fold_sessions']: raise RuntimeError('partial book presented as complete')
            if any(e['cash_after']<0 or e['N']!=e['A']+e['B'] for e in b['execution_log']): raise RuntimeError('accounting invariant')
    receipt={'status':'PASS','units':count,'cost_books':180,'bindings':bindings(),'pnl_disclosure_authorized_after_receipt':True}
    atomic(OUT/'validation.json',receipt)
    print(json.dumps({'validation':'PASS','units':count,'pnl_values_disclosed':False}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['run','resume','status','validate']);a=p.parse_args()
    if a.command=='status': print(json.dumps({'completed':progress(),'total':60}))
    elif a.command=='validate':validate()
    else:run()
