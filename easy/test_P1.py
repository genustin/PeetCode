import unittest
from P1 import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum_basic(self):
        """Test basic functionality with standard inputs"""
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_two_sum_negative_numbers(self):
        """Test cases with negative numbers"""
        self.assertEqual(self.solution.twoSum([-3, 4, 3, 90], 0), [0, 2])
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_two_sum_edge_cases(self):
        """Test edge cases"""
        # Single element (shouldn't happen per problem constraints)
        # self.assertEqual(self.solution.twoSum([5], 5), [])

        # Large target
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5, 6], 11), [4, 5])

    def test_two_sum_brute_force(self):
        """Test brute force approach for comparison"""
        self.assertEqual(self.solution.twoSum_brute_force([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum_brute_force([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum_brute_force([3, 3], 6), [0, 1])

    def test_consistency_between_approaches(self):
        """Ensure both approaches give same results"""
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([-3, 4, 3, 90], 0),
            ([1, 2, 3, 4, 5, 6], 11)
        ]

        for nums, target in test_cases:
            with self.subTest(nums=nums, target=target):
                result_hash = self.solution.twoSum(nums, target)
                result_bf = self.solution.twoSum_brute_force(nums, target)
                self.assertEqual(result_hash, result_bf)

if __name__ == '__main__':
    unittest.main()