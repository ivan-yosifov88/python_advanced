def read_input(test=False):
    if test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        matrix = []
        row_count, column_count = map(int, input().split(", "))
        for _ in range(row_count):
            row = [int(el) for el in input().split(", ")]
            matrix.append(row)
        return matrix


matrix = read_input()

matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        matrix_sum += row[c]

print(matrix_sum)
print(matrix)
