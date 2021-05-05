from random import sample

BOARD_ROWS = 6
BOARD_COLUMNS = 7


def random_chose_start_player(players):
    return sample(players, len(players))


def initialise_board(row, col):
    empty_board = []
    for r in range(row):
        empty_board.append([0] * col)
    return empty_board


def print_player_message(player):
    print(f"{player}, please choose a column")


def print_board(board):
    for row in board:
        print(row)


def make_move(column, board, player):
    row = len(board)
    for r in range(row - 1, -1, -1):
        if board[r][column - 1] == 0:
            board[r][column - 1] = int(player.split()[1])
            return board, r


def players_new_row(players):
    players[0], players[1] = players[1], players[0]
    return players


def is_valid_move(board, col):
    row = len(board)
    if col.isdigit() and 0 <= int(col) - 1 <= row:
        return True
    else:
        return False


def get_player_symbol_as_int(player):
    _, symbol = player.split()
    return int(symbol)


def horizontal_win(row, board, player):
    symbol = get_player_symbol_as_int(player)
    counter = 0
    for r in board[row]:
        if r == symbol:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


def vertical_win(column, board, player):
    symbol = get_player_symbol_as_int(player)
    counter = 0
    for i in range(len(board)):
        if board[i][column - 1] == symbol:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


def left_diagonal_win(row, col, board, player):
    symbol = get_player_symbol_as_int(player)
    col -= 1
    counter = 0
    row_count = len(board)
    col_count = len(board[0])
    diagonal_row_index = None
    diagonal_col_index = None
    row_end = None
    if row == col:
        diagonal_row_index = 0
        diagonal_col_index = 0
        row_end = row_count
    elif row > col:
        diagonal_row_index = row - col
        diagonal_col_index = 0
        row_end = row_count - diagonal_row_index
    elif row < col:
        diagonal_row_index = 0
        diagonal_col_index = col - row
        row_end = col_count - diagonal_col_index

    for i in range(row_end):
        r = diagonal_row_index + i
        c = diagonal_col_index + i
        if board[r][c] == symbol:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


def right_diagonal_win(row, col, board, player):
    symbol = get_player_symbol_as_int(player)
    col -= 1
    counter = 0
    row_count = len(board)
    col_count = len(board[0])
    diagonal_row_index = None
    diagonal_col_index = None
    row_end = None
    row = row_count - row - 1
    if row == col:
        diagonal_row_index = row_count - 1
        diagonal_col_index = 0
        row_end = row_count
    elif row > col:
        diagonal_row_index = row_count - 1 - row - col
        diagonal_col_index = 0
        row_end = row_count - row - col
    elif row < col:
        diagonal_row_index = row_count - 1
        diagonal_col_index = col - row
        row_end = col_count - diagonal_col_index

    for i in range(row_end):
        r = diagonal_row_index - i
        c = diagonal_col_index + i
        if board[r][c] == symbol:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


def win_condition(board, player, row, column):
    if horizontal_win(row, board, player) or \
            vertical_win(column, board, player) or \
            left_diagonal_win(row, column, board, player) or \
            right_diagonal_win(row, column, board, player):
        return True


def has_column_place(board, column):
    rows = len(board)
    counter = 0
    for r in range(rows):
        if board[r][column - 1] == 0:
            counter += 1
    if counter > 0:
        return True


def start_new_game(column):
    if column == "Reset":
        return play_game(players, board = initialise_board(row=BOARD_ROWS, col=BOARD_COLUMNS))


def play_game(players, board):
    current_player = players[0]
    print_player_message(current_player)
    column = input()
    start_new_game(column)
    if is_valid_move(board, column):
        column = int(column)
        if has_column_place(board, column):
            board, row = make_move(column, board, current_player)
            if win_condition(board, current_player, row, column):
                print_board(board)
                print(f"The winner is {current_player}")
                return
            print_board(board)
            players_new_row(players)
            play_game(players, board)
        else:
            print(f"The column {column} is full!\nTry another one column!")
            play_game(players, board)
    else:
        print("Invalid column!\nThe column must be an integer!")
        play_game(players, board)


players = ['Player 1', 'Player 2']

players = random_chose_start_player(players)

board = initialise_board(row=BOARD_ROWS, col=BOARD_COLUMNS)

play_game(players, board)

# TODO What happened when the board is fill and there are no winner
# TODO this is valid condition for a rectangle matrix with r < c
