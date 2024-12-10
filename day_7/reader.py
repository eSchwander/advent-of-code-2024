from day_7.line import Line


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []

    def read_file(self):
        self.lines = []
        with open(self.filename) as file:
            for line in file.readlines():
                self.lines.append(Line(line))
