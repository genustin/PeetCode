import unittest
from P88 import Solution

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_basic(self):
        """Test basic functionality"""
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_merge_edge_cases(self):
        """Test edge cases"""
        # nums1 empty
        nums1 = [0]
        nums2 = [1]
        self.solution.merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

        # nums2 empty
        nums1 = [1]
        nums2 = []
        self.solution.merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

        # nums2 elements come before nums1
        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_merge_alternative_approaches(self):
        """Test alternative approaches"""
        # Test extra space approach
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.solution.merge_extra_space(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_consistency_between_approaches(self):
        """Ensure both approaches give same results"""
        test_cases = [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
            ([0], 0, [1], 1),
            ([1], 1, [], 0),
            ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
        ]

        for nums1, m, nums2, n in test_cases:
            with self.subTest(nums1=nums1, m=m, nums2=nums2, n=n):
                # Make copies for each approach
                nums1_copy1 = nums1.copy()
                nums1_copy2 = nums1.copy()

                # Test both approaches
                self.solution.merge(nums1_copy1, m, nums2, n)
                self.solution.merge_extra_space(nums1_copy2, m, nums2, n)

                self.assertEqual(nums1_copy1, nums1_copy2)

if __name__ == '__main__':
    unittest.main()