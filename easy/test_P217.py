import unittest
from P217 import Solution

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate_basic(self):
        """Test basic functionality"""
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_contains_duplicate_edge_cases(self):
        """Test edge cases"""
        self.assertFalse(self.solution.containsDuplicate([1]))
        self.assertFalse(self.solution.containsDuplicate([]))
        self.assertTrue(self.solution.containsDuplicate([-1, -1]))
        self.assertFalse(self.solution.containsDuplicate([-1, -2, -3]))

    def test_contains_duplicate_alternative_approaches(self):
        """Test alternative approaches"""
        # Test sorting approach
        self.assertTrue(self.solution.containsDuplicate_sorting([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicate_sorting([1, 2, 3, 4]))

        # Test brute force approach
        self.assertTrue(self.solution.containsDuplicate_brute_force([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicate_brute_force([1, 2, 3, 4]))

    def test_consistency_between_approaches(self):
        """Ensure all approaches give same results"""
        test_cases = [
            [1, 2, 3, 1],
            [1, 2, 3, 4],
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            [1],
            [],
            [-1, -1],
            [-1, -2, -3]
        ]

        for nums in test_cases:
            with self.subTest(nums=nums):
                result_hash = self.solution.containsDuplicate(nums)
                result_sort = self.solution.containsDuplicate_sorting(nums)
                result_bf = self.solution.containsDuplicate_brute_force(nums)
                self.assertEqual(result_hash, result_sort)
                self.assertEqual(result_hash, result_bf)

if __name__ == '__main__':
    unittest.main()