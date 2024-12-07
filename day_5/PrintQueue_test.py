import unittest

from day_5.PrintQueue import PrintQueue


class PrintQueueTest(unittest.TestCase):

    def test_evaluate(self):
        pq = PrintQueue('test_input.txt')
        self.assertEqual(143, pq.evaluate_good_orders())

    # def test_evaluate_bad_pages(self):
    #     pq = PrintQueue('test_input.txt')
    #     self.assertEqual(123, pq.evaluate_bad_orders())

    def test_page_to_node(self):
        pq = PrintQueue('test_input.txt')
        self.assertIn(29, pq.page_to_node[47].children)
        self.assertIn(13, pq.page_to_node[47].children)
        self.assertIn(61, pq.page_to_node[47].children)
        self.assertIn(53, pq.page_to_node[47].children)
