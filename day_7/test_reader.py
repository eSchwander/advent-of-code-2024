import unittest

from reader import Reader


class ReaderTest(unittest.TestCase):
    def test_init(self):
        file_name = '1_line_input.txt'
        r = Reader(file_name)
        self.assertEqual(file_name, r.filename)

    def test_init_2(self):
        file_name = 'my_test_input.txt'
        r = Reader(file_name)
        self.assertEqual(file_name, r.filename)

    def test_read_no_content(self):
        r = Reader('abc.txt')
        self.assertRaises(FileNotFoundError, r.read_file)

    def test_build_lines(self):
        r = Reader('1_line_input.txt')
        r.read_file()
        line = r.lines[0]
        self.assertEqual(1, len(r.lines))
        self.assertEqual(10, line.total)
        self.assertEqual([3, 6, 1], line.operands)