import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_part_1_solution_sample(self):
        self.assertEqual(3749, Solution('test_input.txt').part_1())

    def test_part_1_solution_my_sample(self):
        self.assertEqual(14, Solution('my_test_input.txt').part_1())
