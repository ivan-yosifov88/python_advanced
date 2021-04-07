def read_matrix(size):
    matrix = []
    for _ in range(size):
        row = input().split()
        matrix.append(row)
    return matrix


def get_commands_as_indices(command_list):
    """
    :param command_list:
    :return: new list with row and col tuples
    """
    new_command_list = []
    for command in command_list:
        if command == "up":
            result = (-1, 0)
        elif command == "down":
            result = (1, 0)
        elif command == "left":
            result = (0, -1)
        elif command == "right":
            result = (0, 1)
        new_command_list.append(result)
    return new_command_list


def get_all_coal_count(matrix):
    coal = 0
    for row in matrix:
        for el in row:
            if el == "c":
                coal += 1
    return coal


def get_start_indices(matrix, matrix_size):
    for r in range(matrix_size):
        for c in range(matrix_size):
            if matrix[r][c] == "s":
                return r, c


def is_valid_move(matrix, r_index, c_index):
    if r_index in range(len(matrix)) and c_index in range(len(matrix)):
        return True
    return False


def get_command_result(matrix, row, column, command_list, coal_count):
    for command in command_list:
        row_index, col_index = command
        row += row_index
        column += col_index
        if is_valid_move(matrix, row, column):
            if matrix[row][column] == "c":
                coal_count -= 1
                if coal_count == 0:
                    return f"You collected all coals! ({row}, {column})"
                matrix[row][column] = "*"
            elif matrix[row][column] == "e":
                return f"Game over! ({row}, {column})"
        else:
            row -= row_index
            column -= col_index
    return f"{coal_count} coals left. ({row}, {column})"


size_of_field = int(input())

commands = input().split()

matrix = read_matrix(size_of_field)

commands_indices = get_commands_as_indices(commands)

coal_total_count = get_all_coal_count(matrix)

start_row_index, start_col_index = get_start_indices(matrix, size_of_field)

print(get_command_result(matrix, start_row_index, start_col_index, commands_indices, coal_total_count))
