from unittest import TestCase

from day_8.solution import Solution


class TestSolution(TestCase):
    def test_solution_part_1(self):
        s = Solution('test_input.txt')
        self.assertEqual(14, s.get_the_answer(True))

    def test_solution_part_2(self):
        s = Solution('test_input.txt')
        self.assertEqual(34, s.get_the_answer(False))