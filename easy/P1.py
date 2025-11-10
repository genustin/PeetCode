"""
LeetCode Problem 1: Two Sum
Difficulty: Easy
Category: Arrays & Hash Maps
URL: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Hash Map (One-pass)

        We use a hash map to store each number and its index as we iterate through the array.
        For each number, we calculate the complement (target - current number) and check
        if it exists in our hash map.

        Time Complexity: O(n) - We traverse the list once
        Space Complexity: O(n) - Worst case we store n elements in the hash map

        Key Insights:
        - Using a hash map allows O(1) lookups for complements
        - One-pass approach is more efficient than two-pass
        - We can check and store in the same iteration
        """
        num_map = {}  # Stores number -> index mapping

        for i, num in enumerate(nums):
            complement = target - num

            # Check if complement exists in our map
            if complement in num_map:
                return [num_map[complement], i]

            # Store current number and its index
            num_map[num] = i

        return []  # No solution found (though problem guarantees one solution)

    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Alternative Approach: Brute Force

        This is the naive approach that checks every possible pair.
        Good for understanding the problem but inefficient for large inputs.

        Time Complexity: O(n²) - Nested loops
        Space Complexity: O(1) - No extra space used
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


def test_two_sum():
    """Test function for Two Sum solution"""
    solution = Solution()

    # Test case 1: Basic example
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    expected1 = [0, 1]
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"

    # Test case 2: Negative numbers
    nums2 = [-3, 4, 3, 90]
    target2 = 0
    result2 = solution.twoSum(nums2, target2)
    expected2 = [0, 2]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"

    # Test case 3: Duplicate numbers (but different indices)
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    expected3 = [0, 1]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"

    # Test case 4: Larger array
    nums4 = [1, 2, 3, 4, 5, 6]
    target4 = 11
    result4 = solution.twoSum(nums4, target4)
    expected4 = [4, 5]
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"

    print("All Two Sum tests passed!")


if __name__ == "__main__":
    # Run tests
    test_two_sum()

    # Example usage
    solution = Solution()

    # Example 1
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Example 1 - nums: {nums}, target: {target}, result: {result}")

    # Compare approaches
    result_bf = solution.twoSum_brute_force(nums, target)
    print(f"Brute force result: {result_bf}")
    print(f"Both approaches give same result: {result == result_bf}")