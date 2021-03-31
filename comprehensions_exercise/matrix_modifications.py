def is_coordinates_are_valid(matrix, r_index, c_index):
    if 0 <= r_index < len(matrix) and 0 <= c_index < len(matrix[0]):
        return True
    print("Invalid coordinates")
    return False


def add_command(matrix, r_index, c_index, value):
    if is_coordinates_are_valid(matrix, r_index, c_index):
        matrix[r_index][c_index] += value
    return matrix


def subtract_command(matrx, r_index, c_index, value):
    if is_coordinates_are_valid(matrx, r_index, c_index):
        matrix[r_index][c_index] -= value
    return matrix


def print_result(matrix):
    # for row in matrix:
    #     for c in row:
    #         print(c, end=" ")
    #     print()
    result = [print(' '.join(str(el) for el in row)) for row in matrix]


def read_matrix():
    row_count = int(input())
    # matrix = []
    #
    # for _ in range(row_count):
    #     row = [int(x) for x in input().split()]
    #     matrix.append(row)
    matrix = [[int(x) for x in input().split()] for _ in range(row_count)]
    return matrix


matrix = read_matrix()

while True:
    data = input()
    if data == "END":
        break
    command, row, column, value = data.split()
    row = int(row)
    column = int(column)
    value = int(value)
    if command == "Add":
        add_command(matrix, row, column, value)
    elif command  == "Subtract":
        subtract_command(matrix, row, column, value)

print_result(matrix)
