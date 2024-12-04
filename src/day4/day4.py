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

# file_path = 'i:/vscode/adventofcode2024/src/day4/input.txt'
file_path = 'input.txt'
grid = read_input_file(file_path)
word = "XMAS"
count = find_word_in_grid(grid, word)
print(count)

# ANS: 2575

# Part 2

def count_x_mas_patterns(file_path):
    # Read the word search grid from the input file
    with open(file_path, 'r') as f:
        grid = [line.strip() for line in f.readlines()]
    
    # Add padding of '.' characters around the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    padded_grid = (
        ["." * (cols + 2)] +  # Top padding
        ["." + row + "." for row in grid] +  # Side padding for each row
        ["." * (cols + 2)]  # Bottom padding
    )

    padded_rows = len(padded_grid)
    padded_cols = len(padded_grid[0])
    count = 0

    # Helper function to check diagonals for "X-MAS"
    def is_x_mas(i, j):
        # Top-left to bottom-right diagonal
        top_left = padded_grid[i - 1][j - 1:j + 2]
        bottom_right = padded_grid[i + 1][j - 1:j + 2][::-1]
        
        # Top-right to bottom-left diagonal
        top_right = padded_grid[i - 1][j - 1:j + 2][::-1]
        bottom_left = padded_grid[i + 1][j - 1:j + 2]

        return (
            (top_left in ("MAS", "SAM") and bottom_right in ("MAS", "SAM")) or
            (top_right in ("MAS", "SAM") and bottom_left in ("MAS", "SAM"))
        )

    # Iterate through the grid (excluding the padding)
    for i in range(1, padded_rows - 1):  # Avoid padded edges
        for j in range(1, padded_cols - 1):
            if padded_grid[i][j] == 'A' and is_x_mas(i, j):
                count += 1

    return count


# Path to the input file
input_file = "input.txt"

# Call the function and print the result
result = count_x_mas_patterns(input_file)
print(f"Number of X-MAS patterns found: {result}")