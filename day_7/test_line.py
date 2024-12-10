import unittest

from line import Line


class LineTest(unittest.TestCase):
    def test_line_init(self):
        line = Line('10: 4 2')
        self.assertEqual(10, line.total)
        self.assertEqual([4, 2], line.operands)

    def test_line_init_2(self):
        line = Line('10: 4 2 1')
        self.assertEqual(10, line.total)
        self.assertEqual([4, 2, 1], line.operands)
