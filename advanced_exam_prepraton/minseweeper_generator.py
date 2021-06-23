def get_bobs_position(bombs_count):
    return [input().strip("()") for _ in range(bombs_count)]


def generate_board(size):
    board = []
    for row in range(size):
        board.append([None] * size)
    return board


def draw_mines_on_board(board, size, bombs):
    for bomb in bombs:
        bomb_row, bomb_column = bomb.split(", ")
        bomb_row = int(bomb_row)
        bomb_column = int(bomb_column)
        if in_range(bomb_row, size) and in_range(bomb_column, size):
            board[bomb_row][bomb_column] = "*"

    return board


def in_range(value, max_value):
    if 0 <= value < max_value:
        return True


def get_number(board, row, column, size):
    number = 0
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1)
    ]
    for delta in deltas:
        delta_row, delta_column = delta
        delta_row += row
        delta_column += column
        if in_range(delta_row, size) and in_range(delta_column, size):
            if board[delta_row][delta_column] == "*":
                number += 1
    return number


def generate_numbers_in_board(board, size):

    for row in range(size):
        for column in range(size):
            if board[row][column] is None:
                board[row][column] = get_number(board, row, column, size)
    return board


def print_result(board):
    for row in board:
        print(' '.join(str(el) for el in row))


board_size = int(input())
bombs_count = int(input())

bombs = get_bobs_position(bombs_count)

empty_board = generate_board(board_size)

board = draw_mines_on_board(empty_board, board_size, bombs)

generate_numbers_in_board(board, board_size)

print_result(board)
