"""
LeetCode Problem 344: Reverse String
Difficulty: Easy
Category: Strings & Two Pointers
URL: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Approach: Two Pointers

        Use two pointers starting from the beginning and end of the array,
        swapping characters until they meet in the middle.

        Time Complexity: O(n) - Single pass through half the array
        Space Complexity: O(1) - In-place modification
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString_pythonic(self, s: List[str]) -> None:
        """
        Alternative Approach: Pythonic

        Use Python's built-in reverse method.
        """
        s.reverse()

    def reverseString_slicing(self, s: str) -> str:
        """
        Alternative Approach: String Slicing

        For educational purposes - demonstrates Python string slicing.
        Note: This returns a new string rather than modifying in-place.
        """
        return s[::-1]  # [start:stop:step]


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: In-place reversal
    s_list = list("abcdefg")
    print(f"Original list: {s_list}")
    solution.reverseString(s_list)
    print(f"Reversed list: {s_list}")

    # Example 2: Compare approaches
    s_list2 = list("hello")
    solution.reverseString_pythonic(s_list2)
    print(f"Pythonic reverse: {s_list2}")

    # Example 3: String slicing (educational)
    s_str = "abcdefg"
    result = solution.reverseString_slicing(s_str)
    print(f"String slicing: '{s_str}' -> '{result}'")