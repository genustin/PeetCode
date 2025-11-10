import unittest
from P344 import Solution

class TestReverseString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse_string_basic(self):
        """测试基本字符串反转"""
        self.assertEqual(self.solution.reverseString("hello"), "olleh")
        self.assertEqual(self.solution.reverseString("abcdefg"), "gfedcba")
        self.assertEqual(self.solution.reverseString("12345"), "54321")

    def test_reverse_string_empty(self):
        """测试空字符串"""
        self.assertEqual(self.solution.reverseString(""), "")

    def test_reverse_string_single_char(self):
        """测试单个字符"""
        self.assertEqual(self.solution.reverseString("a"), "a")
        self.assertEqual(self.solution.reverseString("z"), "z")

    def test_reverse_string_with_spaces(self):
        """测试包含空格的字符串"""
        self.assertEqual(self.solution.reverseString("hello world"), "dlrow olleh")
        self.assertEqual(self.solution.reverseString("a b c"), "c b a")

    def test_reverse_string_special_chars(self):
        """测试特殊字符"""
        self.assertEqual(self.solution.reverseString("!@#$%"), "%$#@!")
        self.assertEqual(self.solution.reverseString("测试"), "试测")

if __name__ == '__main__':
    unittest.main()