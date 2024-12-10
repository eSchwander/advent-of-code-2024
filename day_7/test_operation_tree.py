import unittest

from operation_tree import OperationTree
from line import Line


class OperationTreeTest(unittest.TestCase):
    def test_calculate_one(self):
        line = Line('10: 3 6 1')
        ot = OperationTree(line)
        self.assertTrue(ot.tree_contains_total())

    def test_calculate_two(self):
        line = Line('4: 2 2')
        ot = OperationTree(line)
        self.assertTrue(ot.tree_contains_total())
