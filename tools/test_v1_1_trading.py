"""Synthetic-only tests. No repository/external market input access."""
import unittest
import numpy as np
from v1_1_trading import Book, signals, encode


def data(n=18,s=3):
    return {'open':np.full((n,s),10.),'close':np.full((n,s),10.),
            'normal':np.ones((n,s),bool),'action':np.zeros((n,s),bool),
            'response_ok':np.ones((n,s),bool),'response':np.zeros((n,s))}


class FrozenTrading(unittest.TestCase):
    def test_entry_next_open_ten_sessions_next_open_exit(self):
        d=data(); b=Book(10); item=((0,1,0),1,.5,1)
        b.day(0,d,[item]); self.assertFalse(b.active)
        for t in range(1,11): b.day(t,d,[])
        self.assertEqual(len(b.active),1)
        self.assertTrue(b.active[(0,1,0)]['exit_pending'])
        b.day(11,d,[]);self.assertFalse(b.active);self.assertEqual(b.counts['exits'],1)
        self.assertAlmostEqual(b.cash,1-.0002)
        encode(b.result())

    def test_existing_shares_not_resized_and_batch_n(self):
        d=data();b=Book(10);p=((0,1,0),1,.5,1);q=((0,2,0),2,.4,1)
        b.day(0,d,[p]);b.day(1,d,[q]);shares=b.active[p[0]]['shares']
        b.day(2,d,[]);self.assertEqual(b.active[p[0]]['shares'],shares)
        self.assertEqual(b.execution_log[-1]['N'],2)

    def test_short_unavailable_not_reversed(self):
        d=data();b=Book(10);b.day(0,d,[((0,1,1),0,.4,-1)]);b.day(1,d,[])
        self.assertFalse(b.active);self.assertEqual(b.counts['source_short_execution_unavailable'],1)

    def test_no_entry_delay_or_carry(self):
        d=data();d['normal'][1,1]=False;b=Book(10)
        b.day(0,d,[((0,1,0),1,.5,1)]);b.day(1,d,[]);b.day(2,d,[])
        self.assertFalse(b.active);self.assertFalse(b.pending)

    def test_action_invalidates_book_not_survivor_renormalized(self):
        d=data();d['action'][2,1]=True;b=Book(10)
        b.day(0,d,[((0,1,0),1,.5,1)]);b.day(1,d,[]);b.day(2,d,[])
        r=b.result();self.assertEqual(r['status'],'ECONOMICALLY_UNAVAILABLE');self.assertIsNone(r['metrics'])
        self.assertEqual(len(r['private_preserved_episode_state']),1)

    def test_zero_crossing_original_anchor(self):
        d=data();d['response'][1,1]=.5;b=Book(10)
        b.day(0,d,[((0,1,0),1,.5,1)]);b.day(1,d,[])
        self.assertTrue(b.active[(0,1,0)]['exit_pending']);b.day(2,d,[]);self.assertFalse(b.active)

    def test_coexistence_and_collision(self):
        dtype=[('a','u2'),('b','u2'),('mu_ab','f4'),('mu_ba','f4')]
        rows=np.array([(0,1,1.,1.)],dtype=dtype);a3=np.array([[-.3,-.3,-.2,-.2]])
        p,c=signals(rows,a3,np.array([1.,1.]));self.assertEqual(p,[])
        self.assertEqual(c['peer_directional_conflict_pairs'],1);self.assertEqual(c['source_directional_conflict_pairs'],1)
        d=data();b=Book(5);b.day(0,d,[((0,1,0),1,.3,1),((0,1,1),0,-.2,1)]);b.day(1,d,[])
        self.assertEqual(b.counts['coexistence_sessions'],1)

    def test_permutation_has_same_economic_allocation(self):
        d=data();p=[((0,1,0),1,.5,1),((0,2,0),2,.5,1),((1,2,1),1,-.3,1)]
        b1,b2=Book(20),Book(20)
        b1.day(0,d,p);b2.day(0,d,list(reversed(p)))
        b1.day(1,d,[]);b2.day(1,d,[])
        self.assertEqual(b1.cash,b2.cash)
        self.assertEqual(b1.active,b2.active)

    def test_terminal_mark_no_fabricated_sale(self):
        d=data();b=Book(10);b.day(0,d,[((0,1,0),1,.5,1)]);b.day(1,d,[],True)
        self.assertEqual(b.result()['metrics']['open_terminal_episodes'],1)
        self.assertEqual(b.counts['exits'],0)


if __name__=='__main__':unittest.main()
