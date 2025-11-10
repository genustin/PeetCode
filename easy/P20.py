"""
LeetCode Problem 20: Valid Parentheses
Difficulty: Easy
Category: Strings & Stack
URL: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach: Stack

        Use a stack to track opening brackets. When we encounter a closing bracket,
        it must match the most recent opening bracket.

        Time Complexity: O(n) - Single pass through the string
        Space Complexity: O(n) - Worst case stack size

        Key Insights:
        - Stack is perfect for matching nested structures
        - Early return if string length is odd
        - Use dictionary for bracket mapping
        """
        # Early return for odd length strings
        if len(s) % 2 != 0:
            return False

        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                # Closing bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket
                stack.append(char)

        # Valid if stack is empty (all brackets matched)
        return len(stack) == 0

    def isValid_optimized(self, s: str) -> bool:
        """
        Alternative Approach: Optimized Stack with Early Returns

        Same stack approach but with additional early returns for invalid cases.
        """
        if len(s) % 2 != 0:
            return False

        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                # Closing bracket
                if not stack:  # No opening bracket to match
                    return False
                if stack[-1] != bracket_map[char]:  # Mismatch
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)

        return len(stack) == 0


def test_is_valid():
    """Test function for Valid Parentheses solution"""
    solution = Solution()

    # Test case 1: Valid parentheses
    s1 = "()"
    result1 = solution.isValid(s1)
    assert result1 == True, f"Test 1 failed: expected True, got {result1}"

    # Test case 2: Valid mixed brackets
    s2 = "()[]{}"
    result2 = solution.isValid(s2)
    assert result2 == True, f"Test 2 failed: expected True, got {result2}"

    # Test case 3: Invalid order
    s3 = "(]"
    result3 = solution.isValid(s3)
    assert result3 == False, f"Test 3 failed: expected False, got {result3}"

    # Test case 4: Invalid nesting
    s4 = "([)]"
    result4 = solution.isValid(s4)
    assert result4 == False, f"Test 4 failed: expected False, got {result4}"

    # Test case 5: Valid nesting
    s5 = "{[]}"
    result5 = solution.isValid(s5)
    assert result5 == True, f"Test 5 failed: expected True, got {result5}"

    # Test case 6: Empty string
    s6 = ""
    result6 = solution.isValid(s6)
    assert result6 == True, f"Test 6 failed: expected True, got {result6}"

    # Test case 7: Odd length
    s7 = "(["
    result7 = solution.isValid(s7)
    assert result7 == False, f"Test 7 failed: expected False, got {result7}"

    print("All Valid Parentheses tests passed!")


if __name__ == "__main__":
    # Run tests
    test_is_valid()

    # Example usage
    solution = Solution()

    # Example 1
    s = "()[]{}"
    result = solution.isValid(s)
    print(f"Example 1 - s: '{s}', is valid: {result}")

    # Compare approaches
    result_opt = solution.isValid_optimized(s)
    print(f"Optimized approach: {result_opt}")
    print(f"Both approaches consistent: {result == result_opt}")