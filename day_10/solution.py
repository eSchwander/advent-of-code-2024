class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Node:
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord
        self.neighbors = []

    def get_next_steps(self):
        next_steps = []

        for neighbor in self.neighbors:
            if neighbor.value == self.value + 1:
                next_steps.append(neighbor)

        return next_steps

    def find_trail_ends(self):
        trail_ends = set()

        if self.value != 0:
            return trail_ends

        steps = self.get_next_steps()
        while len(steps) > 0:
            step = steps.pop(0)
            if step.value == 9:
                trail_ends.add(str(step.coord))
            else:
                steps.extend(step.get_next_steps())

        return trail_ends

    def count_all_trails(self):
        score = 0

        if self.value != 0:
            return score

        steps = self.get_next_steps()
        while len(steps) > 0:
            step = steps.pop(0)
            if step.value == 9:
                score += 1
            else:
                steps.extend(step.get_next_steps())

        return score

    def determine_score(self):
        return len(self.find_trail_ends())

    def __str__(self):
        return f"{self.value} {self.coord}"


class MatrixBuilder:
    def __init__(self, array):
        self.array = array
        self.matrix = Matrix()
        matrix_array = self.matrix.array

        for y, row in enumerate(array):
            matrix_array.append([])
            current_row = matrix_array[y]

            for x, element in enumerate(row):
                current_row.append(Node(element, Coord(x, y)))

        for y, row in enumerate(matrix_array):
            for x, node in enumerate(row):
                neighbors = node.neighbors

                if y != 0:
                    neighbors.append(matrix_array[y - 1][x])
                if y != len(array) - 1:
                    neighbors.append(matrix_array[y + 1][x])
                if x != 0:
                    neighbors.append(matrix_array[y][x - 1])
                if x != len(array[y]) - 1:
                    neighbors.append(matrix_array[y][x + 1])


class Matrix:
    def __init__(self):
        self.array = []

    def find_roots(self):
        roots = []

        for row in self.array:
            for node in row:
                if node.value == 0:
                    roots.append(node)

        return roots

    def find_part_1_score(self):
        score = 0
        roots = self.find_roots()

        for root in roots:
            score += root.determine_score()
        return score

    def find_part_2_score(self):
        score = 0
        roots = self.find_roots()

        for root in roots:
            score += root.count_all_trails()
        return score

    def __str__(self):
        string = ''
        for row in self.array:
            for node in row:
                string += str(node.value)
            string += '\n'
        return string


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.array = []

        with open(self.filename) as file:
            lines = file.readlines()

            for line in lines:
                current_row = []
                self.array.append(current_row)
                for c in line.strip():
                    current_row.append(int(c))


if __name__ == '__main__':
    fr = FileReader('input.txt')
    print(fr.array)
    mb = MatrixBuilder(fr.array)
    print(mb.array)
    print(mb.matrix)

    matrix = mb.matrix

    roots = matrix.find_roots()

    print(matrix.find_part_1_score())
    print(matrix.find_part_2_score())
