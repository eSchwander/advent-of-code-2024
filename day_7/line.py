class Line:
    def __init__(self, line_string):
        total, operands = line_string.strip().split(':')
        self.total = int(total)
        operands = operands.split()
        self.operands = [int(operand) for operand in operands]