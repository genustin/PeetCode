"""
LeetCode Problem 53: Maximum Subarray
Difficulty: Easy
Category: Arrays & Dynamic Programming
URL: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Approach: Kadane's Algorithm (Dynamic Programming)

        We maintain two variables:
        - current_sum: Maximum sum of subarray ending at current position
        - max_sum: Global maximum sum found so far

        For each number, we decide whether to extend the current subarray or start a new one.

        Time Complexity: O(n) - Single pass through the array
        Space Complexity: O(1) - Constant space used

        Key Insights:
        - Local decisions lead to global optimum (optimal substructure)
        - If current element is better than extending previous subarray, start fresh
        - This is a classic example of dynamic programming
        """
        if not nums:
            return 0

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either extend the current subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            # Update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSubArray_divide_conquer(self, nums: List[int]) -> int:
        """
        Alternative Approach: Divide and Conquer

        Divide the array into left and right halves, then combine solutions.
        The maximum subarray can be in left, right, or crossing the midpoint.

        Time Complexity: O(n log n) - Divide and conquer
        Space Complexity: O(log n) - Recursion stack depth

        Key Insights:
        - Demonstrates different algorithmic thinking
        - Useful for understanding divide and conquer patterns
        """
        def divide_and_conquer(left, right):
            if left > right:
                return float('-inf')

            mid = (left + right) // 2

            # Calculate maximum crossing sum
            left_sum = 0
            max_left_sum = float('-inf')
            for i in range(mid, left - 1, -1):
                left_sum += nums[i]
                max_left_sum = max(max_left_sum, left_sum)

            right_sum = 0
            max_right_sum = float('-inf')
            for i in range(mid + 1, right + 1):
                right_sum += nums[i]
                max_right_sum = max(max_right_sum, right_sum)

            crossing_sum = max_left_sum + max_right_sum

            # Recursively solve left and right halves
            left_max = divide_and_conquer(left, mid - 1)
            right_max = divide_and_conquer(mid + 1, right)

            return max(left_max, right_max, crossing_sum)

        return divide_and_conquer(0, len(nums) - 1)

    def maxSubArray_brute_force(self, nums: List[int]) -> int:
        """
        Alternative Approach: Brute Force

        Check all possible subarrays. Demonstrates why better algorithms are needed.

        Time Complexity: O(n²) - All subarrays
        Space Complexity: O(1) - Constant space
        """
        if not nums:
            return 0

        max_sum = float('-inf')
        n = len(nums)

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum


def test_max_subarray():
    """Test function for Maximum Subarray solution"""
    solution = Solution()

    # Test case 1: Basic example
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = solution.maxSubArray(nums1)
    expected1 = 6  # [4, -1, 2, 1]
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"

    # Test case 2: Single element
    nums2 = [1]
    result2 = solution.maxSubArray(nums2)
    expected2 = 1
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"

    # Test case 3: All negative
    nums3 = [-2, -1, -3, -4]
    result3 = solution.maxSubArray(nums3)
    expected3 = -1  # Single element [-1]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"

    # Test case 4: All positive
    nums4 = [1, 2, 3, 4]
    result4 = solution.maxSubArray(nums4)
    expected4 = 10  # Entire array
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"

    # Test case 5: Mixed with positive at end
    nums5 = [5, 4, -1, 7, 8]
    result5 = solution.maxSubArray(nums5)
    expected5 = 23  # Entire array
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"

    print("All Maximum Subarray tests passed!")


if __name__ == "__main__":
    # Run tests
    test_max_subarray()

    # Example usage
    solution = Solution()

    # Example 1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(nums)
    print(f"Example 1 - nums: {nums}")
    print(f"Kadane's algorithm result: {result}")

    # Compare approaches
    result_dc = solution.maxSubArray_divide_conquer(nums)
    result_bf = solution.maxSubArray_brute_force(nums)
    print(f"Divide and conquer result: {result_dc}")
    print(f"Brute force result: {result_bf}")
    print(f"All approaches consistent: {result == result_dc == result_bf}")