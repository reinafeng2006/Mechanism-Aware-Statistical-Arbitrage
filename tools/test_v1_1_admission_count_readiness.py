"""Invented exact-rational accounting witness; no files/data/PnL are read."""
from fractions import Fraction as F


def main():
    nav, surviving, cash, cost = F(1), F(2, 5), F(3, 5), F(1, 1000)
    alternatives = {
        "batch_count": (F(1, 22), F(1, 22)),
        "snapshot_single_proposal_count": (F(1, 21), F(1, 21)),
        "sequential_count": (F(1, 21), F(1, 22)),
    }
    for sizes in alternatives.values():
        assert all(0 < x <= F(1, 10) * nav for x in sizes)
        assert surviving + sum(sizes) <= nav
        assert sum(sizes) * (1 + cost) < cash
    assert len(set(alternatives.values())) == 3
    assert alternatives["sequential_count"] != tuple(reversed(alternatives["sequential_count"]))
    print("PASS: synthetic count-binding witness; 3 feasible distinct allocations; no data or PnL access")


if __name__ == "__main__":
    main()
