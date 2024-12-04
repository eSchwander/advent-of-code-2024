import re

mul_pattern = r'mul\([0-9]+,[0-9]+\)'
num_pattern = r'[0-9]+'

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def calculate_mul_commands(mul_commands):
     matches = re.findall(mul_pattern, mul_commands)
     total = 0

     for match in matches:
         nums_to_multiply = re.findall(num_pattern, match)

         product = 1
         for num in nums_to_multiply:
            product *= int(num)

         total += product

     return total

def calculate_enabled_commands(enabled_commands):
    total = 0

    for x in enabled_commands:
        total += calculate_mul_commands(x)

    return total

def find_enabled_inputs(input_text):
    enabled = True
    enabled_input = []

    current_input = ''
    for c in input_text:
        current_input += c
        if "don't()" in current_input:
            if enabled:
                enabled_input.append(current_input)
            current_input = ''
            enabled = False
        if "do()" in current_input:
            if enabled:
                enabled_input.append(current_input)
            current_input = ''
            enabled = True

    if enabled:
        enabled_input.append(current_input)

    return enabled_input


content = read_file('input.txt')
enabled_inputs = find_enabled_inputs(content)
part_1_result = calculate_mul_commands(content)
part_2_result = calculate_enabled_commands(enabled_inputs)


# Print the matches
print("part 1", part_1_result)
print("part 2", part_2_result)