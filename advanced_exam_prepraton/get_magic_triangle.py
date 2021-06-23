def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    if n > 2:
        for number in range(n - len(matrix)):
            previous_row = matrix[-1]
            row = [1]
            for i in range(len(previous_row) - 1):
                result = previous_row[i] + previous_row[i + 1]
                row.append(result)
            row.append(1)
            matrix.append(row)
    return matrix


print(get_magic_triangle(10))