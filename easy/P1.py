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


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: Basic usage
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Example 1 - nums: {nums}, target: {target}, result: {result}")

    # Example 2: Compare approaches
    result_bf = solution.twoSum_brute_force(nums, target)
    print(f"Brute force result: {result_bf}")
    print(f"Both approaches give same result: {result == result_bf}")