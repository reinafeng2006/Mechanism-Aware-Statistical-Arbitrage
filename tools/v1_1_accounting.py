"""Frozen Option A allocation. Pure functions; no empirical IO or selection."""
from __future__ import annotations

import math
from collections import Counter


def allocate(nav, cash_after_exit_proceeds, existing, exits, proposal_securities, active_count, cost):
    """Return equal-within-security proposal notionals and actual NET trade cost.

    Existing/exits are marked positive security notionals at the same open.
    V_pre is before the simultaneous net execution's fee. Exit proceeds are
    available; fees are charged once on abs(new purchases - qualified exits).
    No survivor target is generated. Sorting is numerical reproducibility only.
    """
    if not math.isfinite(nav) or nav <= 0 or not (0 <= cost < 1):
        raise ValueError('unqualified NAV/cost')
    if active_count < 0 or cash_after_exit_proceeds < 0:
        raise ValueError('invalid book state')
    for values in (existing, exits):
        if any(not math.isfinite(v) or v < 0 for v in values.values()):
            raise ValueError('unqualified holding')
    counts = Counter(proposal_securities)
    b = sum(counts.values())
    n = active_count + b
    raw = nav / n if b else 0.0
    buys = {k: min(counts[k]*raw, max(0.0, .1*nav-existing.get(k, 0.0))) for k in sorted(counts)}
    total = math.fsum(buys.values())
    gross_capacity = max(0.0, nav-math.fsum(existing[k] for k in sorted(existing)))
    upper = min(1.0, gross_capacity/total) if total else 0.0
    keys = sorted(set(buys) | set(exits))

    def fee(scale):
        return cost*math.fsum(abs(scale*buys.get(k, 0.0)-exits.get(k, 0.0)) for k in keys)

    def cash(scale):
        return cash_after_exit_proceeds-scale*total-fee(scale)

    if cash(0.0) < 0:
        raise ValueError('qualified exits cannot fund their actual transaction cost')
    scale = upper
    if cash(upper) < 0:
        # Cash is strictly decreasing when total>0 and cost<1. Solve its
        # piecewise-linear root, not a tolerance/quantile/optimization search.
        knots = sorted({0.0, upper} | {exits.get(k, 0.0)/v for k, v in buys.items()
                       if v > 0 and 0 < exits.get(k, 0.0)/v < upper})
        for lo, hi in zip(knots, knots[1:]):
            clo, chi = cash(lo), cash(hi)
            if chi <= 0:
                scale = lo + (hi-lo)*clo/(clo-chi)
                break
    # Floating representation must not turn exact nonnegative cash negative.
    # Directed rounding toward the feasible set is not a policy size threshold.
    while scale > 0 and cash(scale) < 0:
        scale = math.nextafter(scale, 0.0)
    per_security = {k: scale*v/counts[k] for k, v in buys.items()}
    return {'per_proposal_by_security': per_security, 'N': n, 'B': b,
            'raw': raw, 'scale': scale, 'fee': fee(scale), 'cash': cash(scale),
            'purchases': {k: scale*v for k, v in buys.items()}}


def exit_trigger(anchor, cumulative, channel, eligible_holding_sessions):
    if not all(math.isfinite(x) for x in (anchor, cumulative)) or anchor == 0:
        raise ValueError('invalid original anchor/response')
    residual = anchor-cumulative if channel == 0 else anchor+cumulative
    return anchor*residual <= 0 or eligible_holding_sessions >= 10
