class Solution:
    def __init__(self, filename):
        self.filename = filename
        self.grid = []
        self.x_len = None
        self.y_len = None

        with open(filename) as f:
            for line in f:
                row = []
                for c in line.strip():
                    row.append(c)
                self.grid.append(row)

    def part_1(self):
        self.x_len = len(self.grid[0])
        self.y_len = len(self.grid)

        anti_node_grid = []
        for y in range(self.y_len):
            row = []
            for x in range(self.x_len):
                row.append(False)
            anti_node_grid.append(row)

        for y in range(self.y_len):
            for x in range(self.x_len):
                antenna = self.grid[y][x]
                if antenna.isalnum():
                    matches = self.find_matching_antenna(x, y)
                    for match in matches:
                        match_x, match_y = match
                        x_dist = x - match_x
                        y_dist = y - match_y
                        anti_x = x_dist + x
                        anti_y = y_dist + y
                        if 0 <= anti_x < self.x_len and 0 <= anti_y < self.y_len:
                            anti_node_grid[anti_y][anti_x] = True

        answer = 0
        for row in anti_node_grid:
            for x in row:
                if x:
                    answer += 1

        return answer

    def find_matching_antenna(self, antenna_x, antenna_y):
        antenna = self.grid[antenna_y][antenna_x]

        matches = []

        for y in range(self.y_len):
            for x in range(self.x_len):
                if x == antenna_x and y == antenna_y:
                    continue
                if self.grid[y][x] == antenna:
                    matches.append((x, y))

        return matches

def main():
    s = Solution('input.txt')
    print(s.part_1())

if __name__ == '__main__':
    main()