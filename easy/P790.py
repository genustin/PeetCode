"""
LeetCode Problem 709: To Lower Case
Difficulty: Easy
Category: Strings
URL: https://leetcode.com/problems/to-lower-case/

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Approach: Built-in Method

        Use Python's built-in str.lower() method for simplicity and efficiency.

        Time Complexity: O(n) - Single pass through the string
        Space Complexity: O(n) - New string created
        """
        return s.lower()


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: Basic usage
    s = "AbCdEfG1"
    result = solution.toLowerCase(s)
    print(f"Example 1 - s: '{s}', toLowerCase: '{result}'")