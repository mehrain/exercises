import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLastWord(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(self.solution.lengthOfLastWord("one two three"), 5)
        self.assertEqual(self.solution.lengthOfLastWord("Python"), 6)
        self.assertEqual(self.solution.lengthOfLastWord(""), 0)

if __name__ == '__main__':
    unittest.main()