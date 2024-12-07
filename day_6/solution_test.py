import unittest

import solution


class SolutionTest(unittest.TestCase):

    def test_sample(self):
        res = solution.solution('test_input.txt')
        self.assertEqual(41, res)
