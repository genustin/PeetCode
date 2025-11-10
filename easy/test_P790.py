import unittest
from P790 import Solution

class TestToLowerCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_lowercase_conversion(self):
        """测试基本大小写转换"""
        self.assertEqual(self.solution.toLowerCase("Hello"), "hello")
        self.assertEqual(self.solution.toLowerCase("AbCdEfG1"), "abcdefg1")
        self.assertEqual(self.solution.toLowerCase("ABC"), "abc")

    def test_already_lowercase(self):
        """测试已经是小写的字符串"""
        self.assertEqual(self.solution.toLowerCase("hello"), "hello")
        self.assertEqual(self.solution.toLowerCase("abc123"), "abc123")
        self.assertEqual(self.solution.toLowerCase("lowercase"), "lowercase")

    def test_empty_string(self):
        """测试空字符串"""
        self.assertEqual(self.solution.toLowerCase(""), "")

    def test_single_character(self):
        """测试单个字符"""
        self.assertEqual(self.solution.toLowerCase("A"), "a")
        self.assertEqual(self.solution.toLowerCase("Z"), "z")
        self.assertEqual(self.solution.toLowerCase("a"), "a")
        self.assertEqual(self.solution.toLowerCase("1"), "1")

    def test_mixed_characters(self):
        """测试混合字符"""
        self.assertEqual(self.solution.toLowerCase("Hello World!"), "hello world!")
        self.assertEqual(self.solution.toLowerCase("ABC123XYZ"), "abc123xyz")
        self.assertEqual(self.solution.toLowerCase("Test@Example.Com"), "test@example.com")

    def test_special_characters_and_numbers(self):
        """测试特殊字符和数字"""
        self.assertEqual(self.solution.toLowerCase("!@#$%"), "!@#$%")
        self.assertEqual(self.solution.toLowerCase("12345"), "12345")
        self.assertEqual(self.solution.toLowerCase("TEST123"), "test123")

    def test_unicode_characters(self):
        """测试Unicode字符"""
        self.assertEqual(self.solution.toLowerCase("测试"), "测试")
        self.assertEqual(self.solution.toLowerCase("ÉÉÉ"), "ééé")

if __name__ == '__main__':
    unittest.main()