class Person:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


def initialize_board(size):
    size *= size
    for r in range(1, size + 1):
        print(f"| {r} ", end="")
        if r % 3 == 0:
            print("|")


def initialize_players():
    player_two_symbol = None
    print("Player one name: ", end=" ")
    first_player = input()
    print("Player two name: ", end=" ")
    second_player = input()
    print(f"{first_player} would you like to play with 'X' or '0'?", end=" ")

    while True:
        player_one_symbol = input()
        valid_symbols = ("X", "0")
        if player_one_symbol == valid_symbols[0]:
            player_two_symbol = valid_symbols[1]
            break
        elif player_one_symbol == valid_symbols[1]:
            player_two_symbol = valid_symbols[0]
            break
        else:
            print(f"{first_player} would you like to play with 'X' or '0'?", end=" ")

    print("This is the numeration of the board:")
    return first_player, second_player, player_one_symbol, player_two_symbol


def print_message(player):
    print(f"{player.name} choose a free position [1-9]")


def draw_board(board):
    for row in board:
        r = []
        for cell in row:
            if cell is None:
                cell = " "
            print(f"| {cell} ", end="")
        print("|")

    return board


def get_board(size):
    board = []
    for r in range(size):
        board.append([None] * size)
    return board


def print_invalid_move(player_move):
    print(f"{player_move} is invalid move!")


def is_move_is_valid(player_move, board):
    if player_move.isdigit() and int(player_move) in range(1, 10):
        if is_position_free(int(player_move), board):
            return True
    else:
        print_invalid_move(player_move)
        return False


def print_position_is_not_free_messadge(player_move):
    print(f"{player_move} is not free")


def is_position_free(player_move, board):
    row, column = get_coordinates_of_move(player_move, board)
    if board[row][column] is None:
        return True
    print_position_is_not_free_messadge(player_move)
    return False


def get_coordinates_of_move(player_move, board):
    size = len(board)
    row = (player_move - 1) // size
    column = (player_move - 1) % size
    return row, column


def make_move(player, board):
    while True:
        player_move = input()
        if is_move_is_valid(player_move, board):
            player_move = int(player_move)
            row, column = get_coordinates_of_move(player_move, board)
            board[row][column] = player.mark
            return board
        else:
            print_message(player)


def horizontal_win(board, player):
    size = len(board)
    for r in range(size):
        counter = 0
        for c in range(size):
            if board[r][c] == player.mark:
                counter += 1
            if counter == 3:
                return True
    return False


def vertical_win(board, player):
    size = len(board)
    for c in range(size):
        counter = 0
        for r in range(size):
            if board[r][c] == player.mark:
                counter += 1
            if counter == 3:
                return True
    return False


def main_diagonal(board, player):
    size = len(board)
    for i in range(size):
        if not board[i][i] == player.mark:
            return False
    return True


def anti_diagonal(board, player):
    size = len(board)
    for i in range(size):
        if not board[i][size - i - 1] == player.mark:
            return False
    return True


def player_win_game(board, player):
    if horizontal_win(board, player) or \
            vertical_win(board, player) or \
            main_diagonal(board, player) or \
            anti_diagonal(board, player):
        return True


def print_player_start(player):
    print(f"{first_player} starts first!")


def print_winner(player):
    print(f"{player.name} won!")


def is_no_moves(board):
    for row in board:
        for cell in row:
            if cell is None:
                return True


def play_game(board, *players):
    current_player, next_player = players
    while True:
        print_message(current_player)
        make_move(current_player, board)
        draw_board(board)
        if player_win_game(board, current_player):
            print_winner(current_player)
            break
        if not is_no_moves(board):
            print("Nobody wins!")
            break
        current_player, next_player = next_player, current_player


BOARD_SIZE = 3

first_player, second_player, player_one_symbol, player_two_symbol = initialize_players()
player_one = Person(first_player, player_one_symbol)
player_two = Person(second_player, player_two_symbol)

initialize_board(BOARD_SIZE)

print_player_start(player_one)

board = get_board(BOARD_SIZE)

play_game(board, player_one, player_two)

