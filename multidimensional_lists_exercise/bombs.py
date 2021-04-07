def read_matrix():
    rows_count = int(input())
    matrix = []
    for row in range(rows_count):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def read_bombs():
    bombs = input().split()
    return bombs


def get_bomb_range(matrix, row, col):
    if row == 0:
        start_row = row
        if len(matrix) > 1:
            end_row = row + 2
        else:
            end_row = row
    elif row == len(matrix) - 1:
        end_row = row + 1
        if len(matrix) > 1:
            start_row = row - 1
        else:
            start_row = row
    elif 0 < row < len(matrix) - 1:
        start_row = row - 1
        end_row = row + 2
    if col == 0:
        start_col = col
        if len(matrix[row]) > 1:
            end_col = col + 2
        else:
            end_col = col
    elif col == len(matrix[row]) - 1:
        end_col = col + 1
        if len(matrix[row]) > 1:
            start_col = col - 1
        else:
            start_col = col
    elif 0 < col < len(matrix[row]) - 1:
        start_col = col - 1
        end_col = col + 2

    return start_row, end_row, start_col, end_col


def bomb_explosion(matrix, coordinates):
    for bomb in coordinates:
        row, col = map(int, bomb.split(","))

        if matrix[row][col] > 0:
            bomb_power = matrix[row][col]
            matrix[row][col] = 0
            row_start_index, row_end_index, col_start_index, col_end_index = get_bomb_range(matrix, row, col)
            for r in range(row_start_index, row_end_index):
                for c in range(col_start_index, col_end_index):
                    if matrix[r][c] > 0:
                        matrix[r][c] -= bomb_power
    return matrix


def print_result(matrix):
    count_of_positive_numbers = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 0:
                count_of_positive_numbers.append(matrix[r][c])
    print(f"Alive cells: {len(count_of_positive_numbers)}")
    print(f"Sum: {sum(count_of_positive_numbers)}")

    for r in matrix:
        print(*r)


matrix = read_matrix()
bombs_coordinates = read_bombs()
matrix_after_explosion = bomb_explosion(matrix, bombs_coordinates)
print_result(matrix)