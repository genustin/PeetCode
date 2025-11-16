"""
LeetCode Problem 136: Single Number
Difficulty: Easy
Category: Arrays & Bit Manipulation
URL: https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation (XOR)

        We use the XOR operation which has these properties:
        - a ^ a = 0
        - a ^ 0 = a
        - XOR is commutative and associative

        So when we XOR all numbers together, pairs will cancel out (become 0)
        and the single number will remain.

        Time Complexity: O(n) - Single pass through the array
        Space Complexity: O(1) - Constant space used
        """
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: Basic usage
    nums = [4, 1, 2, 1, 2]
    result = solution.singleNumber(nums)
    print(f"Example 1 - nums: {nums}, single number: {result}")