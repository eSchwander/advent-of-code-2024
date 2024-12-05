import re

class WordCounter:
    def __init__(self, filename, word):
        self.word_search = []
        self.word = word
        self.word_length = len(word)

        self.rows = []
        self.cols = []
        self.zigs = [] # diagonals from NW to SE
        self.zags = [] # diagonals from SW to NE


        with open(filename, 'r') as file:
            for line in file:
                self.word_search.append(line.strip())

        self.y_len = len(self.word_search)
        self.x_len = len(self.word_search[0])

        self.get_rows()
        self.get_cols()
        self.get_zigs()
        self.get_zags()

    def get_rows(self):
        if self.x_len < self.word_length:
            return

        self.rows = self.word_search

    def get_cols(self):
        if self.y_len < self.word_length:
            return

        for x in range(self.x_len):
            col = ''
            for y in range(self.y_len):
                col += self.word_search[y][x]
            self.cols.append(col)

    def get_zigs(self):
        for start_x in range(self.x_len):
            zig = self.get_zig(start_x, 0)

            if len(zig) >= self.word_length:
                self.zigs.append(zig)

        for i, start_y in enumerate(range(self.y_len)):
            # Skip the first zig, it should have been captured above
            if i == 0:
                continue

            zig = self.get_zig(0, start_y)

            if len(zig) >= self.word_length:
                self.zigs.append(zig)

    def get_zig(self, x, y):
        zig = ''
        while x < self.x_len and y < self.y_len:
            zig += self.word_search[y][x]
            x += 1
            y += 1
        return zig

    def get_zags(self):
        for start_x in range(self.x_len):
            zag = self.get_zag(start_x, self.y_len - 1)

            if len(zag) >= self.word_length:
                self.zags.append(zag)

        for i, start_y in enumerate(reversed(range(self.y_len))):
            # Skip the first zag, it should have been captured above
            if i == 0:
                continue

            zag = self.get_zag(0, start_y)

            if len(zag) >= self.word_length:
                self.zags.append(zag)

    def get_zag(self, x, y):
        zag = ''
        while x < self.x_len and y >= 0:
            zag += self.word_search[y][x]
            x += 1
            y -= 1
        return zag

    def count_word_matches(self):
        all_strings_to_match = []
        all_strings_to_match.extend(self.rows)
        all_strings_to_match.extend(self.cols)
        all_strings_to_match.extend(self.zigs)
        all_strings_to_match.extend(self.zags)
        all_strings_to_match.extend([word[::-1] for word in self.rows])
        all_strings_to_match.extend([word[::-1] for word in self.cols])
        all_strings_to_match.extend([word[::-1] for word in self.zigs])
        all_strings_to_match.extend([word[::-1] for word in self.zags])

        matches = []
        for string in all_strings_to_match:
            matches.extend(re.findall(self.word, string))

        return len(matches)

