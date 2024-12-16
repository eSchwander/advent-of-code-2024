import time
import os

memory_map = {}

class Rock:
    def __init__(self, value):
        self.value = value

    def live(self):
        string = str(self.value)
        if string in memory_map:
            return memory_map[string]

        if int(self.value) == 0:
            result = [Rock(str(1))]
        elif len(string) % 2 == 0:
            result = self.split()
        else:
            result = [Rock(str(int(self.value) * 2024))]

        memory_map[string] = result
        return result

    def split(self):
        string = str(self.value)
        halfway_point = len(string) // 2
        left = string[:halfway_point]
        right = string[halfway_point:]
        return Rock(left), Rock(right)

    def __str__(self):
        return str(self.value)

class RockRow:
    def __init__(self, filename):
        self.row = []

        with open(filename) as f:
            for x in f.read().strip().split():
                self.row.append(Rock(x))

    def step(self):
        new_row = []

        for rock in self.row:
            new_row.extend(rock.live())

        self.row = new_row

    def __str__(self):
        string = ''
        for rock in self.row:
            string += str(rock) + ' '
        return string

class FileRockRow:
    def __init__(self, filename):
        self.first_row = []
        self.row_count = []

        with open(filename) as f:
            for x in f.read().strip().split():
                self.first_row.append(Rock(x))

        with open('step_0.txt', 'w+') as f:
            for rock in self.first_row:
                f.write(f'{rock.value}\n')

    def step(self, step_num):
        rock_count = 0

        with open(f'step_{step_num}.txt', 'r') as previous_file:
            if os.path.exists(f'step_{step_num + 1}.txt'):
                os.remove(f'step_{step_num + 1}.txt')

            with open(f'step_{step_num + 1}.txt', 'a') as current_file:
                for line in previous_file:
                    prev_rock = Rock(line.strip())
                    next_rocks = prev_rock.live()
                    rock_count += len(next_rocks)

                    for rock in next_rocks:
                        # with open(f'step_{step_num + 1}.txt', 'a') as current_file:
                        current_file.write(f'{str(rock)}\n')

        self.row_count.append(rock_count)

if __name__ == "__main__":
    start_time = time.time()

    rock_row = RockRow("input.txt")

    for i in range(75):
        step_start_time = time.time()

        # print(f"step {i}")
        # print("num rocks",len(rock_row.row))
        # print("memory map size", len(memory_map.keys()))
        rock_row.step()
        step_end_time = time.time()
        step_runtime = step_end_time - step_start_time
        print(f"step_runtime {i}: {step_runtime} seconds")

    print(f"Runtime: {time.time() - start_time} seconds")

    print(len(rock_row.row))

    # file_rock_row = FileRockRow("input.txt")
    #
    # for i in range(75):
    #     step_start_time = time.time()
    #
    #     file_rock_row.step(i)
    #
    #     step_end_time = time.time()
    #     step_runtime = step_end_time - step_start_time
    #     print(f"step_runtime {i}: {step_runtime} seconds")
    #
    # end_time = time.time()
    # runtime = end_time - start_time
    # print(f"Runtime: {runtime} seconds")
    # print(file_rock_row.row_count[-1])