import unittest
from P121 import Solution

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit_basic(self):
        """Test basic functionality"""
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(self.solution.maxProfit([1, 2]), 1)
        self.assertEqual(self.solution.maxProfit([2, 1]), 0)

    def test_max_profit_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.maxProfit([1]), 0)
        self.assertEqual(self.solution.maxProfit([]), 0)
        self.assertEqual(self.solution.maxProfit([1, 1, 1, 1, 1]), 0)
        self.assertEqual(self.solution.maxProfit([3, 2, 6, 5, 0, 3]), 4)

    def test_max_profit_alternative_approaches(self):
        """Test alternative approaches"""
        # Test brute force
        self.assertEqual(self.solution.maxProfit_brute_force([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution.maxProfit_brute_force([7, 6, 4, 3, 1]), 0)

        # Test Kadane's algorithm
        self.assertEqual(self.solution.maxProfit_kadane([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution.maxProfit_kadane([7, 6, 4, 3, 1]), 0)

    def test_consistency_between_approaches(self):
        """Ensure all approaches give same results"""
        test_cases = [
            [7, 1, 5, 3, 6, 4],
            [7, 6, 4, 3, 1],
            [1, 2],
            [2, 1],
            [1],
            [],
            [1, 1, 1, 1, 1],
            [3, 2, 6, 5, 0, 3]
        ]

        for prices in test_cases:
            with self.subTest(prices=prices):
                result_one_pass = self.solution.maxProfit(prices)
                result_bf = self.solution.maxProfit_brute_force(prices)
                result_kadane = self.solution.maxProfit_kadane(prices)
                self.assertEqual(result_one_pass, result_bf)
                self.assertEqual(result_one_pass, result_kadane)

if __name__ == '__main__':
    unittest.main()