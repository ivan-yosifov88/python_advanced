def read_matrix(row):
    matrix = []
    for r in range(row):
        current_row = list(input())
        matrix.append(current_row)
    return matrix


def get_start_indices(matrix, row, col):
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == "P":
                return r, c


def get_move_indices(command_string):
    command_indices = []
    for element in command_string:
        if element == "U":
            result = (-1, 0)
        elif element == "D":
            result = (1, 0)
        elif element == "L":
            result = (0, -1)
        elif element == "R":
            result = (0, 1)
        command_indices.append(result)
    return command_indices


def is_player_reach_end(matrix, r_index, c_index):
    if r_index not in range(len(matrix)) or c_index not in range(len(matrix[r_index])):
        is_wins = True
        return True
    return False


def is_player_reached_bunny(matrix, r_index, c_index):
    if matrix[r_index][c_index] == "B":
        return True
    return False


def get_bunnies_count(matrix):
    bunnies_positions = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "B":
                bunnies_positions.append((r, c))
    return bunnies_positions


def change_matrix_field(matrix, is_player_dies=False):
    moves = get_move_indices("UDLR")
    bunnies_positions = get_bunnies_count(matrix)
    for bunny in bunnies_positions:
        bunny_row, bunny_col = bunny
        for move in moves:
            r_index, c_index = move
            if + r_index + bunny_row in range(len(matrix)) and c_index + bunny_col in range(len(matrix[0])):
                if matrix[r_index + bunny_row][c_index + bunny_col] == "P":
                    matrix[r_index + bunny_row][c_index + bunny_col] = "B"
                    is_player_dies = True
                elif matrix[r_index + bunny_row][c_index + bunny_col] == "B":
                    pass
                else:
                    matrix[r_index + bunny_row][c_index + bunny_col] = "B"
    if is_player_dies:
        return True
    return False


def get_result(matrix, moves, start_row, start_col):
    is_player_wins = False
    is_player_dies = False
    for move in moves:
        row_index, col_index = move
        start_row += row_index
        start_col += col_index
        if is_player_reach_end(matrix, start_row, start_col):
            start_row -= row_index
            start_col -= col_index
            is_player_wins = True
            matrix[start_row][start_col] = "."
        elif is_player_reached_bunny(matrix, start_row, start_col):
            is_player_dies = True
        else:
            matrix[start_row][start_col] = "P"
            matrix[start_row - row_index][start_col - col_index] = "."
        if change_matrix_field(matrix):
            is_player_dies = True
        if is_player_wins:
            return f"won: {start_row} {start_col}"
        elif is_player_dies:
            return f"dead: {start_row} {start_col}"


row_count, col_count = map(int, input().split())

matrix = read_matrix(row_count)

commands = input()

start_player_row, start_player_column = get_start_indices(matrix, row_count, col_count)

moves_as_indices = get_move_indices(commands)

result = get_result(matrix, moves_as_indices, start_player_row, start_player_column)

for row in matrix:
    for element in row:
        print(element, end="")
    print()
print(result)
