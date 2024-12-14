class Node:
    def __init__(self, value, up, down, left, right):
        self.value = value
        self.up = up
        self.down = down
        self.left = left
        self.right = right

class GraphBuilder:
    def __init__(self, array):
        self.array = array
        self.roots = []

        for y, row in enumerate(array):
            for x, element in enumerate(row):
                up = None
                down = None
                left = None
                right = None

                if y != 0:
                    up = array[y - 1][x] - element
                if y != len(array) - 1:
                    down = array[y+1][x] - element
                if x != 0:
                    left = array[y][x - 1] - element
                if x != len(array[y]) - 1:
                    right = array[y][x + 1] - element

