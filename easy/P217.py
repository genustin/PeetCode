"""
LeetCode Problem 217: Contains Duplicate
Difficulty: Easy
Category: Arrays & Hash Sets
URL: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach: Hash Set

        We use a set to track numbers we've seen. If we encounter a number that's already
        in the set, we know there's a duplicate.

        Time Complexity: O(n) - Single pass through the array
        Space Complexity: O(n) - Worst case we store all n elements in the set

        Key Insights:
        - Sets provide O(1) average case lookup and insertion
        - Early return when duplicate is found improves average case performance
        - More efficient than sorting for this specific problem
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

    def containsDuplicate_sorting(self, nums: List[int]) -> bool:
        """
        Alternative Approach: Sorting

        Sort the array first, then check adjacent elements for duplicates.
        Good for understanding different approaches but less efficient.

        Time Complexity: O(n log n) - Due to sorting
        Space Complexity: O(1) - If we sort in-place, O(n) if we create a copy
        """
        nums_sorted = sorted(nums)

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1]:
                return True

        return False

    def containsDuplicate_brute_force(self, nums: List[int]) -> bool:
        """
        Alternative Approach: Brute Force

        Check every possible pair. Demonstrates the naive approach.
        Only useful for understanding why better approaches are needed.

        Time Complexity: O(n²) - Nested loops
        Space Complexity: O(1) - No extra space
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


def test_contains_duplicate():
    """Test function for Contains Duplicate solution"""
    solution = Solution()

    # Test case 1: Array with duplicates
    nums1 = [1, 2, 3, 1]
    result1 = solution.containsDuplicate(nums1)
    assert result1 == True, f"Test 1 failed: expected True, got {result1}"

    # Test case 2: Array without duplicates
    nums2 = [1, 2, 3, 4]
    result2 = solution.containsDuplicate(nums2)
    assert result2 == False, f"Test 2 failed: expected False, got {result2}"

    # Test case 3: Large array with duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result3 = solution.containsDuplicate(nums3)
    assert result3 == True, f"Test 3 failed: expected True, got {result3}"

    # Test case 4: Single element
    nums4 = [1]
    result4 = solution.containsDuplicate(nums4)
    assert result4 == False, f"Test 4 failed: expected False, got {result4}"

    # Test case 5: Empty array
    nums5 = []
    result5 = solution.containsDuplicate(nums5)
    assert result5 == False, f"Test 5 failed: expected False, got {result5}"

    print("All Contains Duplicate tests passed!")


if __name__ == "__main__":
    # Run tests
    test_contains_duplicate()

    # Example usage
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 1]
    result = solution.containsDuplicate(nums)
    print(f"Example 1 - nums: {nums}, contains duplicate: {result}")

    # Compare approaches
    result_sort = solution.containsDuplicate_sorting(nums)
    result_bf = solution.containsDuplicate_brute_force(nums)
    print(f"Sorting approach: {result_sort}")
    print(f"Brute force approach: {result_bf}")
    print(f"All approaches consistent: {result == result_sort == result_bf}")