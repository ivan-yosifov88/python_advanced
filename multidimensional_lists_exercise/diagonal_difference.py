def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        matrix_size = int(input())
        matrix = []
        for r in range(matrix_size):
            row = [int(num) for num in input().split()]
            matrix.append(row)
        return matrix


def get_primary_diagonal_sum(matrix):
    primary_sum = 0
    row_count = len(matrix)
    for r in range(row_count):
        primary_sum += matrix[r][r]
    return primary_sum


def get_secondary_diagonal_sum(matrix):
    secondary_sum = 0
    row_count = len(matrix)
    for r in range(row_count):
        secondary_sum += matrix[r][row_count - 1 - r]
    return secondary_sum


def print_result(prime, second):
    print(abs(prime - second))


matrix = read_matrix()
primary_diagonal = get_primary_diagonal_sum(matrix)
secondary_diagonal = get_secondary_diagonal_sum(matrix)
print_result(primary_diagonal, secondary_diagonal)