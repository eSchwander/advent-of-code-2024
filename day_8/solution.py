class Solution:
    def __init__(self, filename):
        self.filename = filename
        self.grid = []
        self.x_len = None
        self.y_len = None
        self.anti_node_grid = []

        with open(filename) as f:
            for line in f:
                row = []
                for c in line.strip():
                    row.append(c)
                self.grid.append(row)

    def get_the_answer(self, part_1):
        self.x_len = len(self.grid[0])
        self.y_len = len(self.grid)

        self.anti_node_grid = []
        for y in range(self.y_len):
            row = []
            for x in range(self.x_len):
                row.append(False)
            self.anti_node_grid.append(row)

        for y in range(self.y_len):
            for x in range(self.x_len):
                antenna = self.grid[y][x]
                if antenna.isalnum():
                    matches = self.find_matching_antenna(x, y)
                    for match in matches:
                        match_x, match_y = match
                        if not part_1:
                            self.anti_node_grid[match_y][match_x] = True
                        x_dist = x - match_x
                        y_dist = y - match_y
                        self.add_antis(x, y, x_dist, y_dist, part_1)

        answer = 0
        for row in self.anti_node_grid:
            formatted_row = ['#' if x else '.' for x in row]
            print(''.join(formatted_row))
            for x in row:
                if x:
                    answer += 1

        print('_____________')

        return answer

    def add_antis(self, current_x, current_y, x_dist, y_dist, part_1):
        anti_x = x_dist + current_x
        anti_y = y_dist + current_y

        if 0 <= anti_x < self.x_len and 0 <= anti_y < self.y_len:
            self.anti_node_grid[anti_y][anti_x] = True
            if part_1:
                return
            self.add_antis(anti_x, anti_y, x_dist, y_dist, False)

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
    print(s.get_the_answer(True))
    print(s.get_the_answer(False))

if __name__ == '__main__':
    main()