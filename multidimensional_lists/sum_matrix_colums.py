def read_matrix(is_test = False):
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
            row = [int(num) for num in input().split()]
            matrix.append(row)
        return matrix


def matrix_column_sum(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    columns_sums = [0] * column_count
    for c in range(column_count):
        for r in range(row_count):
            columns_sums[c] += matrix[r][c]
    return columns_sums


def print_result(sums):
    [print(el) for el in sums]


matrix = read_matrix()
sums_list = matrix_column_sum(matrix)
print_result(sums_list)

