class Node:
    def __init__(self, value):
        self.value = value
        self.mult = None
        self.add = None
        self.concat = None

    def has_children(self):
        return self.mult is not None or self.add is not None or self.concat is not None

class OperationTree:
    def __init__(self, line, tree_operations=None):
        self.line = line
        self.root = None
        self.build_tree(tree_operations)


    def build_tree(self, operations=None):
        if operations is None:
            operations = ['mult', 'add']

        self.root = Node(self.line.operands[0])

        for operation in operations:
            self.build_next_node(self.root, 1, operation, operations)

    def build_next_node(self, prev_node, level, current_operation, possible_operations):
        if level == len(self.line.operands):
            return

        if current_operation == "mult":
            node = Node(prev_node.value * self.line.operands[level])
            prev_node.mult = node
        elif current_operation == "add":
            node = Node(prev_node.value + self.line.operands[level])
            prev_node.add = node
        else:
            value = int(str(prev_node.value) + str(self.line.operands[level]))
            node = Node(value)
            prev_node.concat = node

        for operation in possible_operations:
            self.build_next_node(node, level + 1, operation, possible_operations)

    def tree_contains_total(self):
        nodes_to_check = [self.root]

        while len(nodes_to_check) > 0:
            node = nodes_to_check.pop()

            if node is None:
                continue

            nodes_to_check.extend([node.mult, node.add, node.concat])

            if not node.has_children() and node.value == self.line.total:
                print('contains total', self.line.total)
                return True

        return False
