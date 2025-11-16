"""
LeetCode Problem 242: Valid Anagram
Difficulty: Easy
Category: Strings & Hash Maps
URL: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.
"""

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach: Frequency Counting with Hash Map

        Count the frequency of each character in both strings and compare the counts.

        Time Complexity: O(n) - Where n is the length of the strings
        Space Complexity: O(1) - Since we only store 26 characters (constant space)

        Key Insights:
        - Anagrams must have the same character frequencies
        - We can use a dictionary or array to count frequencies
        - Early return if lengths differ
        """
        # Early return if lengths differ
        if len(s) != len(t):
            return False

        # Use array for frequency counting (since we only have 26 lowercase letters)
        freq = [0] * 26

        # Count frequencies in s
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Subtract frequencies for t
        for char in t:
            freq[ord(char) - ord('a')] -= 1

        # Check if all frequencies are zero
        for count in freq:
            if count != 0:
                return False

        return True

    def isAnagram_sorting(self, s: str, t: str) -> bool:
        """
        Alternative Approach: Sorting

        Sort both strings and compare if they are equal.

        Time Complexity: O(n log n) - Due to sorting
        Space Complexity: O(n) - For storing sorted strings
        """
        return sorted(s) == sorted(t)

    def isAnagram_counter(self, s: str, t: str) -> bool:
        """
        Alternative Approach: Using Collections Counter

        Use Python's built-in Counter for concise code.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        from collections import Counter
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: Basic usage
    s, t = "anagram", "nagaram"
    result = solution.isAnagram(s, t)
    print(f"Example 1 - s: '{s}', t: '{t}', is anagram: {result}")

    # Example 2: Compare approaches
    result_sort = solution.isAnagram_sorting(s, t)
    result_counter = solution.isAnagram_counter(s, t)
    print(f"Sorting approach: {result_sort}")
    print(f"Counter approach: {result_counter}")
    print(f"All approaches consistent: {result == result_sort == result_counter}")