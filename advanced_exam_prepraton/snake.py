def get_board():
    board = []
    size = int(input())
    for _ in range(size):
        board.append(list(input()))
    return board


def get_snake_position(board):
    row_count = len(board)
    column_count = len(board[0])
    for row_index in range(row_count):
        for column_index in range(column_count):
            if board[row_index][column_index] == "S":
                return row_index, column_index


def get_lair_coordinates(board):
    lair = []
    row_count = len(board)
    column_count = len(board[0])
    for row_index in range(row_count):
        for column_index in range(column_count):
            if board[row_index][column_index] == "B":
                lair.append((row_index, column_index))
    return lair


def snake_in_range(board, row, column):
    row_size = len(board)
    column_size = len(board[0])
    if 0 <= row < row_size and 0 <= column < column_size:
        return True


def make_move(move):

    moves = {
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0)
    }
    return moves[move]


def print_board(board):
    for row in board:
        print(''.join(row))


board = get_board()

snake_start_position = get_snake_position(board)

snake_position = snake_start_position

lair = get_lair_coordinates(board)

food_eaten = 0

snake_row, snake_column = snake_position

command = input()
while command:
    row_move, column_move = make_move(command)
    board[snake_row][snake_column] = "."
    if not snake_in_range(board, snake_row + row_move, snake_column + column_move):
        print("Game over!")
        break
    snake_row += row_move
    snake_column += column_move
    if board[snake_row][snake_column] == "B":
        board[snake_row][snake_column] = "."
        snake_row, snake_column = lair[1]
    if board[snake_row][snake_column] == "*":
        food_eaten += 1
    board[snake_row][snake_column] = "S"

    if 10 <= food_eaten:
        print("You won! You fed the snake.")
        break
    command = input()
print(f"Food eaten: {food_eaten}")
print_board(board)