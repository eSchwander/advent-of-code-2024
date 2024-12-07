from collections import defaultdict

class TreeNode:
    def __init__(self, data, children):
        self.data = data
        self.children = children

class PrintQueue:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.content = file.read()

        sections = self.content.split('\n\n')

        self.reverse_rules = defaultdict(set)
        self.rules = defaultdict(set)
        for rule in sections[0].split('\n'):
            prev, curr = rule.split('|')
            self.reverse_rules[int(curr)].add(int(prev))
            self.rules[int(prev)].add(int(curr))

        self.page_orders = []
        for page_order in sections[1].split('\n'):
            self.page_orders.append([int(x) for x in page_order.split(',')])

        self.bad_orders = []
        self.good_orders = []
        self.find_good_and_bad_orders()

    def find_good_and_bad_orders(self):
        for page_order in self.page_orders:
            if self.is_valid_page_order(page_order):
                self.good_orders.append(page_order)
            else:
                self.bad_orders.append(page_order)


    def is_valid_page_order(self, page_order):
        for i, page in enumerate(page_order):
            if i == len(page_order) - 1:
                return True

            if not self.is_valid_page(page, page_order[i + 1:]):
                return False

    def is_valid_page(self, page, pages_to_check):
        for page_to_check in pages_to_check:
            if page_to_check in self.reverse_rules[page]:
                return False

        return True

    def evaluate_good_orders(self):
        middle_page_sum = 0

        for page_order in self.good_orders:
            middle_index = int(len(page_order) / 2)
            middle_page_sum += page_order[middle_index]

        return middle_page_sum
    
    def evaluate_bad_orders(self):
        middle_page_sum = 0
        new_orders = []
        
        for bad_order in self.bad_orders:
            new_order = bad_order.copy()
            while not self.is_valid_page_order(new_order):
                i, j = self.find_indexes_to_swap(new_order)
                if i + j != 0:
                    new_order[i], new_order[j] = new_order[j], new_order[i]
            new_orders.append(new_order)
            middle_index = int(len(new_order) / 2)
            middle_page_sum += new_order[middle_index]

        return middle_page_sum

    def find_indexes_to_swap(self, page_order):
        for i, page in enumerate(page_order):
            for j, page_to_check in enumerate(page_order[:i]):
                if page_to_check not in self.reverse_rules[page]:
                    return i, j

        return -1, -1