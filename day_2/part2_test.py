import unittest
import part2

class TestProcessReport(unittest.TestCase):

    def test_ascending(self):
        report = [1,2,3,4,5]
        self.assertTrue(part2.is_report_valid(report))

    def test_ascending_gap_first(self):
        report = [1,5,6,7,8]
        self.assertTrue(part2.is_report_valid(report))

    def test_ascending_gap_middle(self):
        report = [1,2,6,3,4]
        self.assertTrue(part2.is_report_valid(report))

    def test_ascending_gap_last(self):
        report = [1,2,3,4,10]
        self.assertTrue(part2.is_report_valid(report))

    def test_ascending_bad_order_last(self):
        report = [1,2,3,4,3]
        self.assertTrue(part2.is_report_valid(report))

    def test_ascending_bad_order_first(self):
        report = [3,2,3,4,5]
        self.assertTrue(part2.is_report_valid(report))

    def test_descending(self):
        report = [5,4,3,2,1]
        self.assertTrue(part2.is_report_valid(report))

    def test_descending_gap_first(self):
        report = [10,4,3,2,1]
        self.assertTrue(part2.is_report_valid(report))

    def test_descending_gap_middle(self):
        report = [10,9,1,8,7]
        self.assertTrue(part2.is_report_valid(report))

    def test_descending_gap_last(self):
        report = [10,9,8,1]
        self.assertTrue(part2.is_report_valid(report))

    def test_descending_bad_order_last(self):
        report = [10,9,8,9]
        self.assertTrue(part2.is_report_valid(report))

    def test_descending_bad_order_first(self):
        report = [9,10,9,8]
        self.assertTrue(part2.is_report_valid(report))

    def test_duplicates_ascending(self):
        report = [1,2,2,3,4]
        self.assertTrue(part2.is_report_valid(report))

    def test_duplicates_descending(self):
        report = [4,3,3,2,1]
        self.assertTrue(part2.is_report_valid(report))
        
    def test_too_many_duplicates_ascending(self):
        report = [1,2,2,2,3,4]
        self.assertFalse(part2.is_report_valid(report))
        
    def test_gaps_ascending(self):
        report = [1,5,9,10]
        self.assertFalse(part2.is_report_valid(report))
        
    def test_too_many_duplicates_descending(self):
        report = [4,3,2,2,2,1]
        self.assertFalse(part2.is_report_valid(report))
        
    def test_gaps_descending(self):
        report = [10,9,5,1]
        self.assertFalse(part2.is_report_valid(report))


if __name__ == '__main__':
    unittest.main()