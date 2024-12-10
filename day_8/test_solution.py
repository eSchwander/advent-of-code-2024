from unittest import TestCase

from day_8.solution import Solution


class TestSolution(TestCase):
    def test_solution(self):
        s = Solution('test_input.txt')
        self.assertEqual(14, s.part_1())