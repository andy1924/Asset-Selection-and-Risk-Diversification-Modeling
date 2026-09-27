import unittest

from portfolio_risk.model import (
    REGION_COUNTS, count_sets, inclusion_exclusion, make_assets,
    policy, policy_cnf, truth_table,
)


class PortfolioDemoTests(unittest.TestCase):
    def test_all_regions_and_inclusion_exclusion(self):
        assets = make_assets()
        counts = count_sets(assets)
        self.assertEqual(len(assets), 50)
        self.assertEqual((counts["A"], counts["B"], counts["C"]), (18, 15, 14))
        self.assertEqual((counts["AB"], counts["AC"], counts["BC"], counts["ABC"]),
                         (7, 6, 4, 3))
        self.assertEqual(sum(REGION_COUNTS.values()), 50)
        self.assertEqual(inclusion_exclusion(counts), counts["union_direct"])
        self.assertEqual(counts["union_direct"], 33)

    def test_policy_and_cnf_exhaustively(self):
        rows = truth_table()
        self.assertEqual(len(rows), 8)
        self.assertEqual(sum(accepted for _, _, _, accepted in rows), 4)
        for p, q, r, result in rows:
            self.assertEqual(result, policy_cnf(p, q, r))
        self.assertFalse(policy(True, True, True))
        self.assertTrue(policy(True, False, False))


if __name__ == "__main__":
    unittest.main()
