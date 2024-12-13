class Solution:
    def __init__(self, filename):
        self.input_string = ''
        self.memory = []
        self.block_memory = []

        with open(filename, 'r') as f:
            self.input_string = f.read()

        current_id = 0
        for i, c in enumerate(self.input_string):
            for x in range(int(c)):
                if i % 2 == 0:
                    self.memory.append(current_id)
                else:
                    self.memory.append(-1)
            if i % 2 == 0:
                self.block_memory.append(str(current_id) * int(c))
                current_id += 1
            else:
                self.block_memory.append('.' * int(c))


        num_used_memory = 0
        for x in self.memory:
            if x != -1:
                num_used_memory += 1


        current_memory_i = 0
        end_i = len(self.memory) - 1
        while end_i >= num_used_memory:
            while self.memory[current_memory_i] != -1:
                current_memory_i += 1

            if self.memory[end_i] != -1:
                self.memory[end_i], self.memory[current_memory_i] = self.memory[current_memory_i], self.memory[end_i]

            end_i -= 1

        self.checksum = 0
        for i, x in enumerate(self.memory):
            if x == -1:
                break
            self.checksum += x * i

if __name__ == '__main__':
    s = Solution('input.txt')
    print(s.checksum)