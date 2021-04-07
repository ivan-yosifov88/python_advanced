def read_matrix():
    row_count = int(input())

    matrix = []
    for _ in range(row_count):
        row = list(input().strip())
        matrix.append(row)
    return matrix


def is_valid_coordinates(matrix, row, column):
    if row in range(len(matrix)) and column in range(len(matrix[r])):
        return True
    return False


def get_knight_moves(matrix, row, column):
    valid_move = 0
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, -2), (1, -2), (-1, 2)]
    for move in knight_moves:
        row_index, col_index = move
        row_index = int(row_index)
        col_index = int(col_index)
        row_index += row
        col_index += column
        if is_valid_coordinates(matrix, row_index, col_index):
            if matrix[row_index][col_index] == "K":
                valid_move += 1
    return valid_move


matrix = read_matrix()
max_knight_attack = 0
max_row_index = 0
max_col_index = 0
knight = 0
while True:
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "K":
                attack = get_knight_moves(matrix, r, c)
                if attack > max_knight_attack:
                    max_knight_attack = attack
                    max_row_index = r
                    max_col_index = c
    if max_knight_attack == 0:
        break
    matrix[max_row_index][max_col_index] = "0"
    knight += 1
    max_knight_attack = 0

print(knight)