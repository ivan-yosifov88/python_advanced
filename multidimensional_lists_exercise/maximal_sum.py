def read_matrix(is_test= False):
    if is_test:
        return [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4],
        ]
    else:
        matrix_row, matrix_column = map(int, input().split())
        matrix = []

        for r in range(matrix_row):
            row = [int(x) for x in input().split()]
            matrix.append(row)
    return matrix


def get_sum_of_sub_matrix(matrix, sub_matrix_size, r_index, c_index):
    current_sum = 0
    for r in range(r_index, r_index + sub_matrix_size):
        for c in range(c_index, c_index + sub_matrix_size):
            current_sum += matrix[r][c]
    return current_sum


def get_sub_matrix_indices_and_sum(matrix, sub_matrix_size):
    row_count = len(matrix)
    column_count = len(matrix[0])
    max_row_index = 0
    max_column_index = 0
    best_sum = get_sum_of_sub_matrix(matrix, sub_matrix_size, 0 , 0)
    for row_index in range(row_count - sub_matrix_size + 1):
        for column_index in range(column_count - sub_matrix_size + 1):
            sub_matrix_sum = get_sum_of_sub_matrix(matrix, sub_matrix_size, row_index, column_index)
            if sub_matrix_sum > best_sum:
                best_sum = sub_matrix_sum
                max_row_index = row_index
                max_column_index = column_index
    return max_row_index, max_column_index, best_sum


def print_result(matrix, r_index, c_index, best_sum, sub_matrix_size):
    print(f"Sum = {best_sum}")
    sub_matrix = []
    for r in range(r_index, r_index + sub_matrix_size):
        row = []
        for c in range(c_index, c_index + sub_matrix_size):
            row.append(matrix[r][c])
        print(' '.join(str(el) for el in row))


SUB_MATRIX_SIZE = 3

matrix = read_matrix()
biggest_row_index, biggest_column_index, sum_sub_matrix = get_sub_matrix_indices_and_sum(matrix, SUB_MATRIX_SIZE)
print_result(matrix, biggest_row_index, biggest_column_index,  sum_sub_matrix, SUB_MATRIX_SIZE)

