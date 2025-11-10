import unittest
from P771 import Solution

class TestNumJewelsInStones(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_jewels_in_stones(self):
        """测试基本宝石与石头计数"""
        self.assertEqual(self.solution.numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(self.solution.numJewelsInStones("z", "ZZ"), 0)
        self.assertEqual(self.solution.numJewelsInStones("Asc", "AAaaBBbbCCccDDdd"), 4)  # 修正：A出现2次，c出现2次，总计4

    def test_empty_jewels_or_stones(self):
        """测试空字符串情况"""
        self.assertEqual(self.solution.numJewelsInStones("", "abc"), 0)
        self.assertEqual(self.solution.numJewelsInStones("abc", ""), 0)
        self.assertEqual(self.solution.numJewelsInStones("", ""), 0)

    def test_single_char_jewels(self):
        """测试单个字符的宝石"""
        self.assertEqual(self.solution.numJewelsInStones("a", "aaaaa"), 5)
        self.assertEqual(self.solution.numJewelsInStones("A", "aaaaa"), 0)
        self.assertEqual(self.solution.numJewelsInStones("Z", "ZZZZZ"), 5)

    def test_case_sensitivity(self):
        """测试大小写敏感性"""
        self.assertEqual(self.solution.numJewelsInStones("aA", "aA"), 2)
        self.assertEqual(self.solution.numJewelsInStones("a", "A"), 0)
        self.assertEqual(self.solution.numJewelsInStones("A", "a"), 0)

    def test_special_characters(self):
        """测试特殊字符"""
        self.assertEqual(self.solution.numJewelsInStones("!@#", "!@#$%^&*"), 3)
        self.assertEqual(self.solution.numJewelsInStones("123", "123456789"), 3)

    def test_duplicate_jewels(self):
        """测试宝石字符串中有重复字符"""
        self.assertEqual(self.solution.numJewelsInStones("aaa", "aaaaa"), 5)
        self.assertEqual(self.solution.numJewelsInStones("aA", "aA"), 2)

if __name__ == '__main__':
    unittest.main()