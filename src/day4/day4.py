def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for row in range(rows):
        for col in range(cols):
            for row_step, col_step in directions:
                if all(0 <= row + i * row_step < rows and 0 <= col + i * col_step < cols and grid[row + i * row_step][col + i * col_step] == word[i] for i in range(len(word))):
                    count += 1
    return count

file_path = 'i:/vscode/adventofcode2024/src/day4/input.txt'
grid = read_input_file(file_path)
word = "XMAS"
count = find_word_in_grid(grid, word)
print(count)

# ANS: 2575

# Part 2

def find_x_mas_in_grid(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    # Define the relative positions for the X-MAS pattern
    patterns = [
        [(0, 0), (1, -1), (2, -2), (1, 1), (2, 2)],  # Diagonal down-right and up-left
        [(0, 0), (1, 1), (2, 2), (1, -1), (2, -2)],  # Diagonal down-left and up-right
        [(0, 0), (-1, -1), (-2, -2), (-1, 1), (-2, 2)],  # Diagonal up-right and down-left
        [(0, 0), (-1, 1), (-2, 2), (-1, -1), (-2, -2)]  # Diagonal up-left and down-right
    ]
    for row in range(rows):
        for col in range(cols):
            for pattern in patterns:
                match = True
                for i, (dr, dc) in enumerate(pattern):
                    new_row = row + dr
                    new_col = col + dc

                    # Check if the new position is within the grid boundaries
                    if not (0 <= new_row < rows and 0 <= new_col < cols):
                        match = False
                        break

                    # Check if the character matches the expected 'MAS' character
                    expected_char = 'MAS'[i % 3]
                    if grid[new_row][new_col] != expected_char:
                        match = False
                        break

                if match:
                    count += 1
    return count

x_mas_count = find_x_mas_in_grid(grid)
print(x_mas_count)