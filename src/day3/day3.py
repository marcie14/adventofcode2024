import re


with open("i:/vscode/adventofcode2024/src/day3/input.txt", "r") as file:
    corrupted_memory = file.read()

    pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

    matches = re.findall(pattern, corrupted_memory)

    total_sum = sum(int(x) * int(y) for x, y in matches)

print(total_sum)

# ANS: 180233229

do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"
mul_pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

enabled = True
total_sum_with_conditions = 0

for match in re.finditer(rf'{do_pattern}|{dont_pattern}|{mul_pattern}', corrupted_memory):
    if match.group() == 'do()':
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = re.findall(r'\d{1,3}', match.group())
            total_sum_with_conditions += int(x) * int(y)

print(total_sum_with_conditions)

# ANS: 95411583