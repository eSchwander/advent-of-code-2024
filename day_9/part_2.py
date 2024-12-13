class Block:
    def __init__(self, length, content):
        self.length = length
        self.content = content

    def is_free(self):
        return self.content == -1

    def expand(self):
        return [self.content] * self.length

    def __str__(self):
        return str(self.expand())

class Part2:
    def __init__(self, filename):
        self.filename = filename
        self.content = None
        self.blocks = []

        with open(filename) as f:
            self.content = f.read().strip()

        self.build_blocks()

    def build_blocks(self):
        for i, c in enumerate(self.content):
            if i % 2 == 0:
                content = i / 2
            else:
                content = -1

            if int(c) != 0:
                self.blocks.append(Block(int(c), int(content)))

    def refactor_blocks(self):
        last_block_index = len(self.blocks) - 1

        while last_block_index > 0:
            # self.print_blocks()
            # print('last_block_index', last_block_index)

            last_block = self.blocks[last_block_index]
            if last_block.is_free():
                last_block_index -= 1
                continue

            current_block_index = 0
            changed_blocks = False
            while current_block_index < last_block_index:
                # self.print_blocks()
                # print('current_block_index', current_block_index)

                current_block = self.blocks[current_block_index]
                if current_block.is_free() and last_block.length <= current_block.length:
                    new_block = Block(last_block.length, last_block.content)
                    last_block.content = -1
                    self.blocks.insert(current_block_index, new_block)
                    current_block.length -= last_block.length
                    changed_blocks = True
                    break

                current_block_index += 1

            if not changed_blocks:
                last_block_index -= 1

    def print_blocks(self):
        print([str(x) for x in self.blocks])

    def checksum(self):
        memory = []
        for block in self.blocks:
            memory.extend(block.expand())

        checksum = 0
        for i, x in enumerate(memory):
            if x != -1:
                checksum += x * i

        return checksum


if __name__ == "__main__":
    p = Part2('input.txt')
    # p.print_blocks()
    p.refactor_blocks()
    # p.print_blocks()
    print(p.checksum())

