from utils.coordinate import Coord


class Guard:
    ordered_facings = ['v', '<', '^', '>']
    facing_to_direction = {
        'v': Coord(0, 1),
        '<': Coord(-1, 0),
        '^': Coord(0, -1),
        '>': Coord(1, 0)
    }
    next_direction = {
        Coord(0, 1): Coord(-1, 0),
        Coord(-1, 0): Coord(0, -1),
        Coord(0, -1): Coord(1, 0),
        Coord(1, 0): Coord(0, 1)
    }

    def __init__(self, starting_x, starting_y, starting_facing):
        self.facings_queue = ['v', '<', '^', '>']
        self.position = Coord(starting_x, starting_y)
        self.turn_to_facing(starting_facing)

    def turn_to_facing(self, new_facing):
        while self.current_facing() != new_facing:
            self.facings_queue.append(self.facings_queue.pop(0))

    def current_facing(self):
        return self.facings_queue[0]

    def current_direction(self):
        return self.facing_to_direction[self.current_facing()]

    def turn(self):
        self.facings_queue.append(self.facings_queue.pop(0))

    def next_position(self):
        return self.position.add(self.current_direction())

    def step(self):
        self.position = self.next_position()

    def move_to(self, coord):
        self.position = Coord(coord.x, coord.y)

class Tile:
    def __init__(self, x, y, blocked):
        self.position = Coord(x, y)
        self.visits = []
        self.blocked = blocked
        self.possible_loop = False

    def add_visit(self, guard):
        self.visits.append(guard.current_direction())

    def num_visits(self):
        return len(self.visits)


class Board:
    obstacle = '#'

    def __init__(self, filename):
        self.string_board = []
        self.tile_grid = []
        self.guard = None
        self.max_x = 0
        self.max_y = 0

        with open(filename) as f:
            for line in f:
                line = line.strip()
                self.string_board.append([x for x in line])

        self.build_board()

    def build_board(self):
        self.max_x = len(self.string_board[0]) - 1
        self.max_y = len(self.string_board) - 1

        for y, row in enumerate(self.string_board):
            tile_row = []
            for x, content in enumerate(row):
                tile = Tile(x, y, content == Board.obstacle)
                tile_row.append(tile)

                if content in Guard.ordered_facings:
                    self.guard = Guard(x, y, content)
                    # tile.add_visit(self.guard)

            self.tile_grid.append(tile_row)

    def get_tile(self, coord):
        x = coord.x
        y = coord.y

        if x < 0 or x > self.max_x or y < 0 or y > self.max_y:
            return None
        return self.tile_grid[y][x]

    def visited_tiles(self):
        visited_tiles = []

        for tile_row in self.tile_grid:
            for tile in tile_row:
                if tile.num_visits() > 0:
                    visited_tiles.append(tile)

        return visited_tiles

    def __str__(self):
        string = ''

        for row in self.tile_grid:
            for tile in row:
                if self.guard.position == tile.position:
                    string += self.guard.current_facing()
                elif tile.blocked:
                    string += self.obstacle
                else:
                    string += '.'
            string += '\n'

        return string

def part_1_solution(filename):
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

    print('solution_1', visited_locations)
    return visited_locations

def part_2_solution(filename):
    board = Board(filename)
    guard = board.guard

    possible_loops = 0

    while True:
        current_tile = board.get_tile(guard.position)
        current_tile.add_visit(guard)

        next_tile = board.get_tile(guard.next_position())

        # Move around the board
        if next_tile is None:
            break
        elif next_tile.blocked:
            guard.turn()
        else:
            guard.step()

        # If the current tile has been visited more than once and if turning would put the guard on a loop. Make a note.
        # if current_tile.num_visits() > 1 and Guard.next_direction[guard.current_direction()] in current_tile.visits:
        #     current_tile.possible_loop = True
        #     possible_loops += 1

    visited_tiles = [tile for tile in board.visited_tiles()]
    for tile in visited_tiles:
        print('testing tile', tile.position)
        loop_board = Board(filename)
        loop_guard = loop_board.guard
        if loop_guard.position == tile.position:
            continue
        tile_to_obstruct = loop_board.get_tile(tile.position)
        tile_to_obstruct.blocked = True


        while True:
            current_tile = loop_board.get_tile(loop_guard.position)

            # Detect loop
            if loop_guard.position == current_tile.position and loop_guard.current_direction() in current_tile.visits:
                possible_loops += 1
                break
            current_tile.add_visit(loop_guard)

            next_tile = loop_board.get_tile(loop_guard.next_position())

            # Move around the board
            if next_tile is None:
                break
            elif next_tile.blocked:
                loop_guard.turn()
            else:
                loop_guard.step()


    print('solution_2')
    print('tiles visited', len(board.visited_tiles()))
    print('possible loops', possible_loops)
    return len(board.visited_tiles()), possible_loops


# part_1_solution('input.txt')
part_2_solution('input.txt')
