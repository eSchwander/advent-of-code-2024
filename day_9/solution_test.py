from unittest import TestCase

from solution import Solution

class SolutionTest(TestCase):
    def test_solution_sample(self):
        s = Solution('test_input.txt')
        self.assertEqual(1928, s.checksum)

    def test_solution(self):
        s = Solution('input.txt')
        self.assertEqual(6398252054886, s.checksum)