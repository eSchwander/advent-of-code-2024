from day_7.operation_tree import OperationTree
from day_7.reader import Reader


class Solution:
    def __init__(self, filename):
        self.reader = Reader(filename)
        self.reader.read_file()

    def part_1(self):
        self.reader.read_file()

        lines = self.reader.lines

        answer = 0
        for line in lines:
            ot = OperationTree(line)
            if ot.tree_contains_total():
                answer += line.total

        return answer

    def part_2(self):

        self.reader.read_file()

        lines = self.reader.lines

        answer = 0
        for line in lines:
            ot = OperationTree(line, ['mult', 'add', 'concat'])
            if ot.tree_contains_total():
                answer += line.total

        return answer

def main():
    print('part_1', Solution('input.txt').part_1())
    print('part_2', Solution('input.txt').part_2())

if __name__ == '__main__':
    main()