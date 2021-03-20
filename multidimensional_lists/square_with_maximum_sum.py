def read_matrix(is_test= False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        row_count, column_count = map(int, input().split(", "))
        matrix = []
        for r in range(row_count):
            row = [int(num) for num in input().split(", ")]
            matrix.append(row)
        return matrix


def get_biggest_sum(matrix, row_index, column_index, sub_matrix_size):
    biggest_sum = 0
    for r in range(row_index, row_index + sub_matrix_size):
        for c in range(column_index, column_index + sub_matrix_size):
            biggest_sum += matrix[r][c]
    return biggest_sum


def get_sub_matrix_coordinates(matrix, sub_matrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_biggest_sum(matrix, 0 , 0, sub_matrix_size)
    row_count = len(matrix)
    column_count = len(matrix[0])
    for row_index in range(row_count - sub_matrix_size + 1):
        for column_index in range(column_count - sub_matrix_size + 1):
            current_sum = get_biggest_sum(matrix, row_index, column_index, sub_matrix_size)
            if current_sum > best_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = column_index
    return best_row_index, best_column_index


def print_result(matrix, coordinates, sub_matrix_size):
    row_count, column_count = coordinates
    for r in range(row_count, row_count + sub_matrix_size):
        row = []
        for c in range(column_count, column_count + sub_matrix_size):
            row.append(matrix[r][c])
        print(" ".join(str(el) for el in row))
    print(get_biggest_sum(matrix, row_count, column_count, sub_matrix_size))


SUB_MATRIX_SIZE = 2
matrix = read_matrix(is_test=True)
coordinates = get_sub_matrix_coordinates(matrix, SUB_MATRIX_SIZE)
print_result(matrix, coordinates, SUB_MATRIX_SIZE)

