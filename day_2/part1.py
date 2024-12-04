def process_line(line):
    increasing_or_decreasing = None
    previous_number = None

    for i, num in enumerate(line.split()):
        num = int(num)
        if i == 1:
            if previous_number > num:
                increasing_or_decreasing = "decreasing"
            elif previous_number < num:
                increasing_or_decreasing = "increasing"
            else:
                return 0

        if increasing_or_decreasing == "decreasing" and previous_number < num:
            return 0
        elif increasing_or_decreasing == "increasing" and previous_number > num:
            return 0

        if previous_number is not None and abs(previous_number - num) > 3 or previous_number == num:
            return 0

        previous_number = num

    return 1

def process_input():
    safe_reports = 0

    with open('input.txt', 'r') as file:
        for line in file:
            safe_reports += process_line(line)

    return safe_reports

print(process_input())


