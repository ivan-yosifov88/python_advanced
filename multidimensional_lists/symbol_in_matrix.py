def read_matrix(is_test= False):
    if is_test:
        return [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["X", "!", "@"],
        ]
    else:
        row_count = int(input())
        matrix = []
        for r in range(row_count):
            row = [element for element in input()]
            matrix.append(row)
        return matrix


def get_symbol_position(matrix):
    symbol = input()
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if symbol in matrix[r][c]:
                return r, c
    return f"{symbol} does not occur in the matrix"


matrix = read_matrix()
print(get_symbol_position(matrix))
