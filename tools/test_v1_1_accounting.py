"""Synthetic pre-PnL tests; no scientific inputs or output values."""
import itertools
import math
import unittest
from v1_1_accounting import allocate, exit_trigger


class AccountingTests(unittest.TestCase):
    def test_batch_count_and_survivors(self):
        existing = {i: .02 for i in range(20)}
        before = existing.copy()
        r = allocate(1., .6, existing, {}, [30, 31], 20, .001)
        self.assertEqual(r['N'], 22)
        self.assertEqual(r['per_proposal_by_security'], {30: 1/22, 31: 1/22})
        self.assertEqual(existing, before)

    def test_permutation_invariance_and_security_cap(self):
        results = [allocate(1., .3, {0: .09, 3: .61}, {}, p, 2, .002)
                   for p in itertools.permutations([0, 0, 1, 2])]
        self.assertTrue(all(r == results[0] for r in results))
        self.assertAlmostEqual(results[0]['purchases'][0], .01)
        self.assertAlmostEqual(results[0]['purchases'][1], .1)
        self.assertGreater(results[0]['cash'], 0)

    def test_no_cap_redistribution(self):
        r = allocate(1., 1., {}, {}, [0, 0, 1], 0, .001)
        self.assertEqual(r['purchases'], {0: .1, 1: .1})
        self.assertAlmostEqual(r['per_proposal_by_security'][0], .05)

    def test_common_cash_scale_maximal(self):
        r = allocate(1., .1, {5: .9}, {}, [0, 1], 1, .002)
        self.assertGreaterEqual(r['cash'], 0)
        self.assertAlmostEqual(sum(r['purchases'].values()), .1/1.002)
        self.assertEqual(r['purchases'][0], r['purchases'][1])

    def test_passive_drift_no_sale_no_funding(self):
        holdings = {0: 1.1}
        r = allocate(1., 0., holdings, {}, [0, 1], 1, .001)
        self.assertEqual(r['purchases'], {0: 0., 1: 0.})
        self.assertEqual(holdings, {0: 1.1})

    def test_net_cost_not_gross_episode_cost(self):
        r = allocate(1., 1., {}, {0: .1}, [0], 0, .001)
        self.assertEqual(r['purchases'][0], .1)
        self.assertEqual(r['fee'], 0.)
        r = allocate(1., .1, {}, {0: .1}, [], 0, .001)
        self.assertAlmostEqual(r['fee'], .0001)
        self.assertAlmostEqual(r['cash'], .0999)

    def test_exits_both_signs_and_clock(self):
        for sign in (-1, 1):
            self.assertFalse(exit_trigger(sign, .5*sign, 0, 1))
            self.assertTrue(exit_trigger(sign, sign, 0, 1))
            self.assertTrue(exit_trigger(sign, -sign, 1, 1))
            self.assertFalse(exit_trigger(sign, 0., 1, 9))
            self.assertTrue(exit_trigger(sign, 0., 1, 10))

    def test_no_epsilon_size_threshold(self):
        r = allocate(1., 1e-20, {}, {}, [0], 0, .001)
        self.assertGreater(r['purchases'][0], 0.)
        self.assertGreaterEqual(r['cash'], 0.)


if __name__ == '__main__':
    unittest.main()
