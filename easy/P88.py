"""
LeetCode Problem 88: Merge Sorted Array
Difficulty: Easy
Category: Arrays & Two Pointers
URL: https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored.
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Approach: Three Pointers (Backward Merge)

        We start from the end of both arrays and merge backwards. This avoids
        overwriting elements in nums1 that haven't been processed yet.

        Time Complexity: O(m + n) - Single pass through both arrays
        Space Complexity: O(1) - No extra space used

        Key Insights:
        - Merge from the end to avoid overwriting
        - Use three pointers: one for nums1, one for nums2, one for current position
        - Handle remaining elements after one array is exhausted
        """
        # Pointers starting from the end
        p1 = m - 1  # Last valid element in nums1
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Current position to fill in nums1

        # Merge from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them
        # (No need to copy remaining nums1 elements as they're already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

    def merge_extra_space(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Alternative Approach: Using Extra Space

        Create a new array to store the merged result, then copy back to nums1.
        Demonstrates a simpler approach but uses extra space.

        Time Complexity: O(m + n)
        Space Complexity: O(m + n)
        """
        merged = []
        p1, p2 = 0, 0

        # Merge using two pointers from the start
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        # Add remaining elements
        while p1 < m:
            merged.append(nums1[p1])
            p1 += 1

        while p2 < n:
            merged.append(nums2[p2])
            p2 += 1

        # Copy back to nums1
        for i in range(len(merged)):
            nums1[i] = merged[i]


def test_merge():
    """Test function for Merge Sorted Array solution"""
    solution = Solution()

    # Test case 1: Basic example
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    expected = [1, 2, 2, 3, 5, 6]
    assert nums1 == expected, f"Test 1 failed: expected {expected}, got {nums1}"

    # Test case 2: nums1 empty
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    expected = [1]
    assert nums1 == expected, f"Test 2 failed: expected {expected}, got {nums1}"

    # Test case 3: nums2 empty
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    expected = [1]
    assert nums1 == expected, f"Test 3 failed: expected {expected}, got {nums1}"

    # Test case 4: Both arrays have elements
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    expected = [1, 2, 3, 4, 5, 6]
    assert nums1 == expected, f"Test 4 failed: expected {expected}, got {nums1}"

    print("All Merge Sorted Array tests passed!")


if __name__ == "__main__":
    # Run tests
    test_merge()

    # Example usage
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(f"Before merge - nums1: {nums1}, nums2: {nums2}")
    solution.merge(nums1, m, nums2, n)
    print(f"After merge - nums1: {nums1}")

    # Test with extra space approach
    nums1_extra = [1, 2, 3, 0, 0, 0]
    solution.merge_extra_space(nums1_extra, m, nums2, n)
    print(f"Extra space approach: {nums1_extra}")
    print(f"Both approaches give same result: {nums1 == nums1_extra}")