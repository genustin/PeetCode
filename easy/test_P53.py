import unittest
from P53 import Solution

class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_subarray_basic(self):
        """Test basic functionality"""
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.solution.maxSubArray([1]), 1)
        self.assertEqual(self.solution.maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_max_subarray_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.maxSubArray([-2, -1, -3, -4]), -1)
        self.assertEqual(self.solution.maxSubArray([1, 2, 3, 4]), 10)
        self.assertEqual(self.solution.maxSubArray([-1, -2, -3, -4]), -1)

    def test_max_subarray_alternative_approaches(self):
        """Test alternative approaches"""
        # Test divide and conquer
        self.assertEqual(self.solution.maxSubArray_divide_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.solution.maxSubArray_divide_conquer([1]), 1)

        # Test brute force
        self.assertEqual(self.solution.maxSubArray_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.solution.maxSubArray_brute_force([1]), 1)

    def test_consistency_between_approaches(self):
        """Ensure all approaches give same results"""
        test_cases = [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            [1],
            [5, 4, -1, 7, 8],
            [-2, -1, -3, -4],
            [1, 2, 3, 4],
            [-1, -2, -3, -4]
        ]

        for nums in test_cases:
            with self.subTest(nums=nums):
                result_kadane = self.solution.maxSubArray(nums)
                result_dc = self.solution.maxSubArray_divide_conquer(nums)
                result_bf = self.solution.maxSubArray_brute_force(nums)
                self.assertEqual(result_kadane, result_dc)
                self.assertEqual(result_kadane, result_bf)

if __name__ == '__main__':
    unittest.main()