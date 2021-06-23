def get_board(size):
    board = []

    for _ in range(size):
        board.append(input().split())
    return board


def get_king_position(board, size):
    for row in range(size):
        for column in range(size):
            if board[row][column] == "K":
                return row, column


def in_range(value, max_value):
    if 0 <= value < max_value:
        return True
    return False


def get_queens(king_position, board, delta):
    max_row = len(board)
    max_column = len(board[0])
    row, column = king_position
    delta_row, delta_column = delta
    while True:
        if not in_range(row, max_row) or not in_range(column, max_column):
            return None
        if board[row][column] == "Q":
            return [row, column]
        row += delta_row
        column += delta_column


def get_queens_positions(king_position, board):
    queens_list = []
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
    ]
    for delta in deltas:
        delta_row , delta_column = delta
        queens_list.append(get_queens(king_position, board, delta))
    return [queen for queen in queens_list if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print("The king is safe!")


BOARD_SIZE = 8

board = get_board(BOARD_SIZE)

king_position = get_king_position(board, BOARD_SIZE)

queens_capture_king = get_queens_positions(king_position, board)

print_result(queens_capture_king)

