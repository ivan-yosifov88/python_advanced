def read_matrix():
    row_index, column_index = map(int, input().split())
    matrix = []
    for r in range(row_index):
        row = input().split()
        matrix.append(row)
    return matrix


def swap_command(indices, matrix):
    row_one, col_one, row_two, col_two = indices
    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
    for r in range(len(matrix)):
        print(' '.join(str(el) for el in matrix[r]))


def input_validator(data, matrix):
    command = data.split()[0]
    if not command == "swap":
        return False
    coordinates = data.split()[1:]
    if not len(coordinates) == 4:
        return False
    coordinates = [int(x) for x in coordinates]
    first_row, first_column, second_row, second_column = coordinates
    if not (0 <= first_row < len(matrix) and 0 <= second_row < len(matrix) and 0 <= first_column < len(
            matrix[0]) and 0 <= second_column < len(matrix[0])):
        return False
    else:
        return coordinates


matrix = read_matrix()

END_COMMAND = "END"

while True:
    data = input()
    if data == END_COMMAND:
        break
    is_valid_input = input_validator(data, matrix)
    if is_valid_input:
        swap_command(is_valid_input, matrix)
    else:
        print("Invalid input!")
        continue
