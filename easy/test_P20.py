import unittest
from P20 import Solution

class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_valid_basic(self):
        """Test basic functionality"""
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        self.assertTrue(self.solution.isValid("{[]}"))

    def test_is_valid_edge_cases(self):
        """Test edge cases"""
        self.assertTrue(self.solution.isValid(""))
        self.assertFalse(self.solution.isValid("(["))
        self.assertFalse(self.solution.isValid(")"))
        self.assertFalse(self.solution.isValid("("))
        self.assertTrue(self.solution.isValid("([]){}"))

    def test_is_valid_optimized_approach(self):
        """Test optimized approach"""
        self.assertTrue(self.solution.isValid_optimized("()"))
        self.assertTrue(self.solution.isValid_optimized("()[]{}"))
        self.assertFalse(self.solution.isValid_optimized("(]"))
        self.assertFalse(self.solution.isValid_optimized("([)]"))

    def test_consistency_between_approaches(self):
        """Ensure both approaches give same results"""
        test_cases = [
            "()",
            "()[]{}",
            "(]",
            "([)]",
            "{[]}",
            "",
            "([",
            ")",
            "(",
            "([]){}"
        ]

        for s in test_cases:
            with self.subTest(s=s):
                result_standard = self.solution.isValid(s)
                result_optimized = self.solution.isValid_optimized(s)
                self.assertEqual(result_standard, result_optimized)

if __name__ == '__main__':
    unittest.main()