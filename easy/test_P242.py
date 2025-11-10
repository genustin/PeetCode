import unittest
from P242 import Solution

class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram_basic(self):
        """Test basic functionality"""
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))
        self.assertFalse(self.solution.isAnagram("rat", "car"))
        self.assertTrue(self.solution.isAnagram("", ""))
        self.assertTrue(self.solution.isAnagram("hello", "hello"))

    def test_is_anagram_edge_cases(self):
        """Test edge cases"""
        self.assertFalse(self.solution.isAnagram("abc", "abcd"))
        self.assertFalse(self.solution.isAnagram("a", "b"))
        self.assertTrue(self.solution.isAnagram("a", "a"))
        self.assertFalse(self.solution.isAnagram("abc", "ab"))

    def test_is_anagram_alternative_approaches(self):
        """Test alternative approaches"""
        # Test sorting approach
        self.assertTrue(self.solution.isAnagram_sorting("anagram", "nagaram"))
        self.assertFalse(self.solution.isAnagram_sorting("rat", "car"))

        # Test counter approach
        self.assertTrue(self.solution.isAnagram_counter("anagram", "nagaram"))
        self.assertFalse(self.solution.isAnagram_counter("rat", "car"))

    def test_consistency_between_approaches(self):
        """Ensure all approaches give same results"""
        test_cases = [
            ("anagram", "nagaram"),
            ("rat", "car"),
            ("", ""),
            ("hello", "hello"),
            ("abc", "abcd"),
            ("a", "b"),
            ("a", "a"),
            ("abc", "ab")
        ]

        for s, t in test_cases:
            with self.subTest(s=s, t=t):
                result_freq = self.solution.isAnagram(s, t)
                result_sort = self.solution.isAnagram_sorting(s, t)
                result_counter = self.solution.isAnagram_counter(s, t)
                self.assertEqual(result_freq, result_sort)
                self.assertEqual(result_freq, result_counter)

if __name__ == '__main__':
    unittest.main()