def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for r in range(size):
            row = [int(number) for number in input().split()]
            matrix.append(row)
        return matrix


def primary_diagonal_sum(matrix):
    sum_diagonal = 0
    row = len(matrix)
    for r in range(row):
        sum_diagonal += matrix[r][r]
    return sum_diagonal


matrix = read_matrix()
print(primary_diagonal_sum(matrix))
