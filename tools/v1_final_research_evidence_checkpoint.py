"""Render only validated frozen aggregates; never fit or select a candidate."""
import json
from pathlib import Path

import numpy as np
import v1_final_heldout_reduced_support as r
import v1_h5_frozen_target_report as h5

OLD = r.ROOT / 'data/manifests/V1_PRE_HELD_OUT_A1_SYNTHESIS.json'
OLD_HASH = '6228A8EE392B939B12020F047CA41A44A472E1218721A9B11D7C23B2CB685796'
OUT = r.ROOT / 'data/manifests/V1_FINAL_HELDOUT_EVIDENCE_CHECKPOINT.json'
DOC = r.ROOT / 'docs/stages/G4/V1_FINAL_H1_H5_HELDOUT_EVIDENCE_CHECKPOINT.md'
BINDINGS = {
    'H1': ('Market adjustment', 'V1-R0L-126W', 'V1-R1M-126W'),
    'H2': ('Industry adjustment', 'V1-R1M-126W', 'V1-R1MI-126W'),
    'H3': ('Hierarchical pooling', 'V1-R0D-252M', 'V1-R3-252M'),
    'H4': ('Dynamic adaptation', 'V1-R0L-126W', 'V1-R4-63D'),
}
H4 = 'COMPUTATION-INCOMPLETE / NO FINAL HELD-OUT DISPOSITION'


def number(x):
    return 'unavailable' if x is None or not np.isfinite(x) else f'{x:.8g}'


def vector(x, squared=False):
    prefix = 'loss_sq_' if squared else 'loss_abs_'
    return ' / '.join(number(x[prefix + d]['temporal_median']) for d in ('ab', 'ba'))


def extract(source, left, right, role):
    items = [x for x in source['pairwise_common_support']
             if x['left'] == left and x['right'] == right and x['role'] == role]
    assert items, 'missing registered comparison'
    result = {}
    for field in r.FIELDS:
        vals = [x['metrics'][field]['right_minus_left_equal_pair_median'] for x in items]
        assert all(v is not None and np.isfinite(v) for v in vals)
        center = float(np.median(vals))
        recorded = source['temporal_median_vector']['pairwise'][left+'__'+right]
        if role != 'heldout': recorded = recorded[role]
        assert center == recorded[field]['temporal_median_of_fold_equal_pair_median_differences']
        result[field] = {'temporal_median': center,
                         'fold_vector': [{'fold': x['fold'], 'difference': v,
                                          'pair_count': x['metrics'][field]['pair_count'],
                                          'observation_count': x['metrics'][field]['observation_count']}
                                         for x, v in zip(items, vals)],
                         'negative_folds': sum(v < 0 for v in vals),
                         'zero_folds': sum(v == 0 for v in vals),
                         'positive_folds': sum(v > 0 for v in vals),
                         'fold_count': len(vals),
                         'fold_range': [min(vals), max(vals)],
                         'dispersion_note': 'Range and complete frozen fold vector; no new decision cutoff.'}
    return result


def main():
    receipt = json.loads((r.CONTROL / 'reduced_support_final_validation.json').read_text())
    assert receipt['result'] == 'PASS' and receipt['final_sha256'] == r.sha(r.FINAL)
    assert r.sha(OLD) == OLD_HASH
    h5.validate()
    old, final = json.loads(OLD.read_text()), json.loads(r.FINAL.read_text())
    target = json.loads(h5.FINAL.read_text())
    results = {}
    for hyp, (name, left, right) in BINDINGS.items():
        result = {'name': name, 'reference': left, 'candidate': right,
                  'inner': extract(old, left, right, 'inner'),
                  'of4': extract(old, left, right, 'of4')}
        if hyp == 'H4':
            result['heldout'] = {'status': H4, 'reason': 'FINAL_DAY_COMPUTATIONAL_BUDGET_EXHAUSTION',
                                 'engineering_blocks': 524, 'scientific_evidence': False}
        else:
            result['heldout'] = extract(final, left, right, 'heldout')
        results[hyp] = result
    # Each candidate/direction/component/horizon remains separate; no pooled score.
    target_temporal = []
    for role in ('inner', 'of4', 'heldout'):
        for candidate in r.CANDIDATES + ([] if role == 'heldout' else ['V1-R4-63D']):
            items = [x for x in target['results'] if x['role'] == role and x['candidate'] == candidate]
            assert len(items) == {'inner': 10, 'of4': 4, 'heldout': 2}[role]
            for direction in ('AB', 'BA'):
                for horizon in h5.HORIZONS:
                    for component in h5.COMPONENTS:
                        cells = [x['directions'][direction][f'O{horizon}'][component] for x in items]
                        vals = [x['equal_pair_median'] for x in cells]
                        valid = all(v is not None and np.isfinite(v) for v in vals)
                        target_temporal.append({'role': role, 'candidate': candidate,
                            'direction': direction, 'horizon': horizon, 'component': component,
                            'temporal_median': float(np.median(vals)) if valid else None,
                            'folds': [{'fold': x['fold'], **cell} for x, cell in zip(items, cells)],
                            'native_support_only': True, 'no_predictive_or_mechanism_claim': True})
    out = {'checkpoint_id': 'V1-FINAL-H1-H5-REDUCED-SUPPORT-EVIDENCE-1.0',
           'status': 'RESEARCH_EVIDENCE_COMPLETE_TRADING_POLICY_DECISION_REQUIRED',
           'scientific_results_are_descriptive': True,
           'support_architecture': {'inner_of4_candidates': 7, 'heldout_candidates': 6,
                                    'r4_excluded_reason': 'COMPUTATION_INCOMPLETE_NOT_ADVERSE_EVIDENCE'},
           'source_hashes': {'inner_of4_a1': OLD_HASH, 'heldout_a1': r.sha(r.FINAL),
                             'h5_vectors': r.sha(h5.FINAL),
                             'validation_receipt': r.sha(r.CONTROL / 'reduced_support_final_validation.json'),
                             'heldout_access_event': r.sha(r.ACCESS)},
           'hypotheses': results, 'h5_native_component_temporal_vectors': target_temporal,
           'a1_candidate_fold_summaries': old['results'] + final['results'],
           'h5_disposition': 'DESCRIPTIVE_NATIVE_RESOLUTION_COMPONENTS_ONLY_NO_A6_PREDICTIVE_DISPOSITION',
           'a6_g5': 'V1_NON_ESTIMABLE_NOT_EXECUTED',
           'uncertainty': 'NOT_ESTIMATED_NO_NEW_P_VALUES_OR_CONFIDENCE_INTERVALS',
           'multiplicity': 'NO_NEW_PROCEDURE_OR_THRESHOLD_NO_SIGNIFICANCE_CLAIMS',
           'severe_failure': 'NO_NUMERICAL_SEVERE_FAILURE_THRESHOLD_FROZEN_NO_INVENTED_FLAG',
           'ranking': 'NO_UNIQUE_WINNER_FORCED', 'trading_pnl_accessed': False}
    r.atomic_json(OUT, out)
    lines = ['# FINAL H1–H5 HELD-OUT EVIDENCE CHECKPOINT', '',
        'Status: **FINAL RESEARCH EVIDENCE / TRADING V1.1 SINGLE DECISION REQUIRED**.', '',
        'The original seven-candidate architecture is preserved as design history. Final held-out evidence uses the authorized **six-candidate** exact intersection because R4-2025 is computationally missing. It is not seven-candidate confirmation. Inner and OF4 retain their original seven-candidate intersections; support changes prohibit treating between-role magnitudes as a controlled change in performance.', '',
        'All findings below are descriptive. No new p-value, confidence interval, significance threshold, multiplicity procedure, ranking or winner rule is introduced. A lower paired loss does not itself establish statistical significance or structural admissibility.', '',
        '## H1–H5 closure table', '',
        'Cells for H1–H4 show the frozen temporal median of fold-level equal-pair medians of **candidate minus reference** absolute-loss differences, `AB / BA`. Negative means lower candidate loss. This is a paired-difference median, not subtraction of independently summarized candidate medians.', '',
        '| Hypothesis | Inner | OF4 | Final Held-Out | Final Disposition |',
        '|---|---|---|---|---|']
    for hyp, result in results.items():
        held = H4 if hyp == 'H4' else vector(result['heldout'])
        if hyp == 'H4': disposition = H4
        else:
            h = result['heldout']
            lower = all(h['loss_abs_'+d]['temporal_median'] < 0 for d in ('ab', 'ba'))
            higher = all(h['loss_abs_'+d]['temporal_median'] > 0 for d in ('ab', 'ba'))
            disposition = ('Lower descriptive central loss in both directions' if lower else
                           'Higher descriptive central loss in both directions' if higher else
                           'Mixed/tied directional central evidence') + '; no inferential or unique-winner claim'
        lines.append(f'| {hyp} {result["name"]} | {vector(result["inner"])} | {vector(result["of4"])} | {held} | {disposition} |')
    lines += ['| H5 resolution O1/O5/O10/O20 | Native component vectors, all seven candidates | Native component vectors, all seven candidates | Native component vectors, six candidates; see horizon table | Descriptive resolution morphology only; no binary resolution or A6 predictive/mechanism disposition |', '',
        'H4 is terminal solely because of final-day computational-budget exhaustion. Its 524 hash-valid engineering blocks are lineage/future-continuation artifacts, not scientific final-held-out evidence. No support/non-support conclusion is drawn from incompleteness.', '',
        '## Candidate identities and exact comparison bindings', '',
        '| Identity | Frozen specification |', '|---|---|',
        '| V1-R0D-252M | R0-DIST with matched linear bridge; H252/U1M |',
        '| V1-R0C-126W | Pearson R0-CORR with matched linear bridge; H126/U1W |',
        '| V1-R0L-126W | OLS R0-LIN; H126/U1W |',
        '| V1-R1M-126W | Market-adjusted two-stage OLS; H126/U1W |',
        '| V1-R1MI-126W | Matched market-plus-industry two-stage OLS; H126/U1W |',
        '| V1-R3-252M | P0 Gaussian EB random intercept/slope, REML, N-ZERO; H252/U1M |',
        '| V1-R4-63D | Static-intercept/random-walk-slope Kalman, PIT-ML Q/R; H63/U1D; historical evidence only here |', '',
        'Bindings: H1 R1-M minus R0-L; H2 R1-MI minus R1-M; H3 R3 minus R0-D matched bridge; historical H4 R4 minus R0-L. No comparator was rebound after access. R0-C/R0-L share the frozen executable linear bridge; the pre-access implementation/lineage audit recorded their equality as specification-consistent.', '',
        '## Held-out annual effects, directional consistency and dispersion', '',
        'Absolute loss uses candidate-neutral H126 `1.4826 × MAD`. Squared-loss robustness uses the frozen H126 sample-SD (`ddof=1`) normalization. These are distinct frozen normalizations, not a new post-access choice. H126 histories are qualified PIT observations strictly before the evaluated event, independent of candidate model-estimation histories.', '',
        '| Hypothesis / year | Absolute Δ AB | Absolute Δ BA | Squared Δ AB | Squared Δ BA | Common rows / pairs |',
        '|---|---:|---:|---:|---:|---|']
    for hyp in ('H1', 'H2', 'H3'):
        result = results[hyp]['heldout']
        for i in range(2):
            cells = [result[f]['fold_vector'][i] for f in r.FIELDS]
            lines.append('| '+f'{hyp} / {cells[0]["fold"]} | '+' | '.join(number(x['difference']) for x in cells)+f' | {cells[0]["observation_count"]:,} / {cells[0]["pair_count"]:,} |')
    lines += ['', '| Hypothesis / metric | Temporal Δ AB / BA | Negative folds AB / BA | Fold range AB | Fold range BA |', '|---|---|---|---|---|']
    for hyp in ('H1', 'H2', 'H3'):
        for square in (False, True):
            res = results[hyp]['heldout']; prefix = 'loss_sq_' if square else 'loss_abs_'
            a, b = res[prefix+'ab'], res[prefix+'ba']
            lines.append(f'| {hyp} / {"squared" if square else "absolute"} | {vector(res, square)} | {a["negative_folds"]}/2 / {b["negative_folds"]}/2 | {number(a["fold_range"][0])} to {number(a["fold_range"][1])} | {number(b["fold_range"][0])} to {number(b["fold_range"][1])} |')
    lines += ['', 'Full inner and OF4 fold vectors, signs, ranges and paired counts are retained in the [checksum-bound evidence manifest](../../../data/manifests/V1_FINAL_HELDOUT_EVIDENCE_CHECKPOINT.json). Roles and directions are never pooled; the two annual held-out observations provide a limited temporal assessment, not estimated uncertainty.', '',
        '## Native coverage and common-support attrition', '',
        '| Candidate / year | Native rows | Six-candidate common rows | Native minus common | Common/native |', '|---|---:|---:|---:|---:|']
    for x in final['results']:
        n, c = x['support']['native_rows'], x['support']['common_rows']
        lines.append(f'| {x["candidate"]} / {x["fold"]} | {n:,} | {c:,} | {n-c:,} | {c/n:.6%} |' if n else f'| {x["candidate"]} / {x["fold"]} | 0 | {c:,} | 0 | unavailable |')
    lines += ['', '| Candidate / year | Common absolute loss AB / BA | Native absolute loss AB / BA | Common equal-pair MAD AB / BA |', '|---|---|---|---|']
    for x in final['results']:
        common = ' / '.join(number(x['common']['loss_abs_'+d]['equal_pair_median']) for d in ('ab','ba'))
        native = ' / '.join(number(x['native']['loss_abs_'+d]['equal_pair_median']) for d in ('ab','ba'))
        dispersion = ' / '.join(number(x['common']['loss_abs_'+d]['equal_pair_mad']) for d in ('ab','ba'))
        lines.append(f'| {x["candidate"]} / {x["fold"]} | {common} | {native} | {dispersion} |')
    lines += ['', 'Native counts describe deployability; attribution uses only the exact common intersection. Counts above are valid bidirectional H126 loss rows, not a claim that all original observations were eligible. The manifest preserves per-field pair/observation counts, native and common loss centers and dispersion for every candidate/fold. No near-zero threshold or support cutoff was added.', '',
        '## H5: O1/O5/O10/O20 native resolution-component evidence', '',
        'These summaries describe existing immutable A5 targets, not fitted resolution predictions, mechanism labels or a new abnormality trigger. Population: all frozen eligible A5 rows, with unavailable targets excluded componentwise under their existing finite-support rule. Within-pair exact medians give equal pair influence; directions, candidates, components, horizons and temporal roles remain separate. No candidate is selected for reporting.', '',
        'A5 retains its **original event-time scale fields** and immutable targets. The H126 amendment changed the separate A1 loss layer, not A3/A5. Therefore these native target magnitudes are not canonical H126 cross-candidate loss attribution and must not be ranked across candidates. RT0 positive = motion along the frozen peer gap; RT1 positive = motion opposite source excess; RT2 absolute/signed = remaining anchored gap; RT3 = original-state continuation residual. None supplies a binary resolved/unresolved label.', '',
        '| Candidate / direction / horizon | Inner RT0; RT1; RT2 abs; RT2 signed; RT3 | OF4 vector | Held-out vector |', '|---|---|---|---|']
    lookup = {(x['role'], x['candidate'], x['direction'], x['horizon'], x['component']): x for x in target_temporal}
    for candidate in r.CANDIDATES + ['V1-R4-63D']:
        for direction in ('AB', 'BA'):
            for horizon in h5.HORIZONS:
                cells = []
                for role in ('inner', 'of4', 'heldout'):
                    cells.append('unavailable — H4 computational cutoff' if role == 'heldout' and candidate == 'V1-R4-63D' else
                                 '; '.join(number(lookup[role,candidate,direction,horizon,c]['temporal_median']) for c in h5.COMPONENTS))
                lines.append(f'| {candidate} / {direction} / O{horizon} | '+' | '.join(cells)+' |')
    lines += ['', 'The evidence manifest retains every H5 fold-level component, equal-pair dispersion and native pair/observation count, including horizon-specific support loss. These target descriptions do not test A6 incremental predictive value. `A6/G5 = V1 NON-ESTIMABLE / NOT EXECUTED` is an evidence/data-availability limitation, not negative trading performance.', '',
        '## SR0, SR1, diagnostics and unavailable quantities', '',
        '- Hash/lineage, PIT-version binding, exact support implementation, lossless materialization and temporal-censoring checks passed. This is engineering/structural validation, not proof of predictive adequacy.',
        '- No new candidate-level SR0 inadmissibility is manufactured from a large loss, weak effect, small scale or R4 timeout. Existing row-level unavailable/invalid states remain excluded under the frozen rules.',
        '- Numerical severe-failure cutoffs were not frozen; no severe-failure count or pass/fail is invented. Convergence/boundary quality is not inferred from a successful checksum. Aggregate estimator-boundary/convergence rates are not computed in this checkpoint and remain unavailable.',
        '- No comparative p-values/confidence intervals are computed. The unexecuted A6 two-horizon inference family is not transferred to relationship comparisons or descriptive A5 targets. No significance claim or multiplicity-adjusted winner is asserted.',
        '- SR1 consists of the separate magnitude, direction, dispersion, support and robustness vectors. Descriptive improvements may coexist with baseline retention, insufficient differentiation and unresolved limitations. R1-MI is not declared a unique winner.', '',
        '## Integrity and handoff', '',
        'Validation: 12 A3/A5 units; 48 compressed payloads with lossless/raw-hash checks; 12 H126 partitions; 44/44 synthesis units; 110/110 native H5 reporting units. The immutable historical relationship/RT3/A3/A5/OF4/H126 ancestors were verified; all 524 R4 engineering hashes and the irreversible held-out access event are preserved.', '',
        f'Canonical held-out A1 SHA-256: `{r.sha(r.FINAL)}`.', '',
        f'Native H5 vector SHA-256: `{r.sha(h5.FINAL)}`.', '',
        f'Evidence-manifest SHA-256: `{r.sha(OUT)}`.', '',
        'Next and only researcher decision: [Trading V1.1 consolidated policy package](../G5/V1_1_FINAL_SINGLE_POLICY_CHECKPOINT.md). No trading PnL has been computed/inspected, and no final V1 conclusions or release tag are asserted before that decision and its authorized economic execution.', '',
        '`FINAL H1–H5 HELD-OUT EVIDENCE COMPLETE / TRADING V1.1 SINGLE DECISION REQUIRED`', '']
    DOC.parent.mkdir(parents=True, exist_ok=True)
    temp = DOC.with_suffix('.md.tmp'); temp.write_text('\n'.join(lines), encoding='utf-8'); temp.replace(DOC)
    print(json.dumps({'result': 'PASS', 'evidence_manifest_sha256': r.sha(OUT), 'document_sha256': r.sha(DOC),
                      'trading_pnl_accessed': False, 'r4_execution': False}))


if __name__ == '__main__': main()
