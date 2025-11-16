"""
LeetCode Problem 771: Jewels and Stones
Difficulty: Easy
Category: Strings & Hash Sets
URL: https://leetcode.com/problems/jewels-and-stones/

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.

You want to know how many of your stones are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Approach: Hash Set

        We use a set to store jewel characters for O(1) lookups.
        Then we iterate through stones and count how many are jewels.

        Time Complexity: O(n + m) where n = len(jewels), m = len(stones)
        Space Complexity: O(n) for the jewel set
        """
        jewel_set = set(jewels)  # Use set to store jewel characters for efficient lookup
        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: Basic usage
    jewels = "aA"
    stones = "aAAbbbb"
    result = solution.numJewelsInStones(jewels, stones)
    print(f"Example 1 - jewels: '{jewels}', stones: '{stones}', result: {result}")