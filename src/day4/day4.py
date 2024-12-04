import numpy as np

file_path = 'i:/vscode/adventofcode2024/src/day4/input.txt'
# file_path = 'input.txt'

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


# Part 1

def find_word_in_grid(line, word):
    rows, cols = len(line), len(line[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for row in range(rows):
        for col in range(cols):
            for row_step, col_step in directions:
                if all(0 <= row + i * row_step < rows and 0 <= col + i * col_step < cols and line[row + i * row_step][col + i * col_step] == word[i] for i in range(len(word))):
                    count += 1
    return count

lines = read_input_file(file_path)
word = "XMAS"
count = find_word_in_grid(lines, word)
print(count)

# ANS: 2575

# Part 2
rows = len(lines)
cols = len(lines[0])
grid = np.ndarray((rows, cols), dtype=int)
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        grid[i, j] = ord(char)

total = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if grid[i, j] == ord('A'):
            if (grid[i-1, j-1] == ord('M') and grid[i+1, j+1] == ord('S')) \
                or (grid[i-1, j-1] == ord('S') and grid[i+1, j+1] == ord('M')):            
                if (grid[i-1, j+1] == ord('M') and grid[i+1, j-1] == ord('S')) \
                    or (grid[i-1, j+1] == ord('S') and grid[i+1, j-1] == ord('M')):
                    total += 1

print(total)

# ANS: 2041