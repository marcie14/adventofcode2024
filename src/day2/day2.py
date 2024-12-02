import csv

with open('i:/vscode/adventofcode2024/src/day2/input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
    not_safe_count = 0

    for line in data:
        report = [int(x) for x in line]
        diff = [report[i] - report[i-1] for i in range(1, len(report))]
        
        # Check if all between 1 and 3
        valid_diff = all(1 <= abs(x) <= 3 for x in diff)
        
        # Check if all strictly increasing or decreasing
        increasing = all(x > 0 for x in diff)
        decreasing = all(x < 0 for x in diff)
        
        # safe if it is either increasing or strictly decreasing
        if not (valid_diff and (increasing or decreasing)):
            not_safe_count += 1

    safe_count = len(data) - not_safe_count
    print(safe_count)
    
    # ANS: 269