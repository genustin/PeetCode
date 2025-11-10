import unittest
from P136 import Solution

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_number(self):
        self.assertEqual(self.solution.singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(self.solution.singleNumber([2, 2, 1]), 1)
        self.assertEqual(self.solution.singleNumber([1]), 1)
        self.assertEqual(self.solution.singleNumber([0, 1, 0]), 1)
        self.assertEqual(self.solution.singleNumber([1, 1, 2, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()