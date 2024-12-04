def is_modified_report_valid(report, skip_index):
    previous_number = None

    for i, num in enumerate(report):
        if skip_index == i:
            continue
        if previous_number is not None and (abs(previous_number - num) > 3 or previous_number >= num):
            return False
        previous_number = num

    return True

def process_report(report):
    for i, num in enumerate(report):
        if is_modified_report_valid(report, i):
            return True
    return False

def is_report_valid(report):
    if process_report(report):
        return True

    report.reverse()
    if process_report(report):
        return True

    return False

def create_report(report):
    report = report.strip()
    report = report.split()
    return [int(x) for x in report]

def process_input():
    safe_reports = 0

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            report = create_report(line)

            if is_report_valid(report):
                safe_reports += 1

    return safe_reports

if __name__ == "__main__":
    print(process_input())
