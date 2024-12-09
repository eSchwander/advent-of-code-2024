import unittest

import solution


class SolutionTest(unittest.TestCase):

    def test_sample_p1(self):
        res = solution.part_1_solution('test_input.txt')
        self.assertEqual(41, res)


    def test_sample_p2(self):
        p1, p2 = solution.part_2_solution('test_input.txt')
        self.assertEqual(41, p1)
        self.assertEqual(6, p2)
