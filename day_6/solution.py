class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_coord):
        return Coord(self.x + other_coord.x, self.y + other_coord.y)


def solution(filename):
    patrol_map = []
    guard_position = Coord(0, 0)
    facings = ['v', '<', '^', '>']
    facing_to_direction = {'v': Coord(0, 1), '<': Coord(-1, 0), '^': Coord(0, -1), '>': Coord(1, 0)}

    # Read input
    with open(filename) as f:
        for line in f:
            line = line.strip()
            patrol_map.append([x for x in line])

    # Find guard position and facing
    for y, row in enumerate(patrol_map):
        for x, c in enumerate(row):
            if c in facings:
                guard_position = Coord(x, y)
                while c != facings[0]:
                    facings.append(facings.pop(0))

    # Loop until the guard is off the map
    max_x = len(patrol_map[0])
    max_y = len(patrol_map)
    while True:
        next_position = guard_position.add(facing_to_direction[facings[0]])

        # End loop if next position is off the map
        if next_position.x == -1 or next_position.x == max_x or next_position.y == -1 or next_position.y == max_y:
            break

        next_position_content = patrol_map[next_position.y][next_position.x]

        if next_position_content == '#':
            facings.append(facings.pop(0))
            patrol_map[guard_position.y][guard_position.x] = facings[0]
        elif next_position_content in ['.', 'X']:
            patrol_map[guard_position.y][guard_position.x] = 'X'
            patrol_map[next_position.y][next_position.x] = facings[0]
            guard_position = next_position

        # Format and print the map
        # map_string = ''
        # for row in patrol_map:
        #     for col in row:
        #         map_string += col
        #     map_string += '\n'
        # print(map_string)

    visited_locations = 1
    for row in patrol_map:
        for c in row:
            if c == 'X':
                visited_locations += 1

    return visited_locations

print(solution('input.txt'))