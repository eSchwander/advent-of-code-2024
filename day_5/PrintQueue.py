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

        self.page_to_node = {}
        for page_num in self.rules:
            self.page_to_node[page_num] = self.build_order_tree_node(page_num)

    def build_order_tree_node(self, page):
        node = TreeNode(page, {})

        # If the page is not in rules, it has no children
        if page not in self.rules:
            return node

        if page in self.page_to_node:
            return self.page_to_node[page]

        # Build the tree
        for following_page in self.rules[page]:
            node.children[following_page] = self.build_order_tree_node(following_page)
        return node

    def find_good_and_bad_orders(self):
        for page_order in self.page_orders:
            if self.validate_page_order(page_order):
                self.good_orders.append(page_order)
            else:
                self.bad_orders.append(page_order)


    def validate_page_order(self, page_order):
        for i, page in enumerate(page_order):
            if i == len(page_order) - 1:
                return True

            if not self.validate_page(page, page_order[i+1:]):
                return False

    def validate_page(self, page, pages_to_check):
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