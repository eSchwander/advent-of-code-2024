import unittest
import WordCounter
from day_4.WordCounter import WordCounter


class TestWordCounter(unittest.TestCase):

    def test_rows(self):
        counter = WordCounter('rows_cols_zigs_zags_test.txt', 'XMAS')
        expected_rows = ['ABCD','EFGH','IJKL','MNOP']
        self.assertEqual(counter.rows, expected_rows)

    def test_cols(self):
        counter = WordCounter('rows_cols_zigs_zags_test.txt', 'XMAS')
        expected_cols = ['AEIM','BFJN','CGKO','DHLP']
        self.assertEqual(counter.cols, expected_cols)

    def test_zigs(self):
        counter = WordCounter('rows_cols_zigs_zags_test.txt', 'XMAS')
        expected_zigs = ['AFKP']
        self.assertEqual(counter.zigs, expected_zigs)

    def test_zags(self):
        counter = WordCounter('rows_cols_zigs_zags_test.txt', 'XMAS')
        expected_zags = ['MJGD']
        self.assertEqual(counter.zags, expected_zags)

    def test_count(self):
        counter = WordCounter('test_input.txt', 'XMAS')
        self.assertEqual(counter.count_word_matches(), 8)

    def test_count_2(self):
        counter = WordCounter('test_input_2.txt', 'XMAS')
        self.assertEqual(counter.count_word_matches(), 18)

    def test_count_row(self):
        counter = WordCounter('row_test.txt', 'XMAS')
        self.assertEqual(counter.count_word_matches(), 4)

    def test_count_col(self):
        counter = WordCounter('col_test.txt', 'XMAS')
        self.assertEqual(counter.count_word_matches(), 2)

    def test_count_zig(self):
        counter = WordCounter('zig_test.txt', 'XMAS')
        self.assertEqual(counter.count_word_matches(), 2)

    def test_count_zag(self):
        counter = WordCounter('zag_test.txt', 'XMAS')
        self.assertEqual(counter.count_word_matches(), 2)

if __name__ == '__main__':
    unittest.main()