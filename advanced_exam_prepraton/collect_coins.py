def get_matrix():
    matrix = []
    row_count = int(input())
    for row in range(row_count):
        matrix.append(input().split())
    return matrix


def get_player_possition(matrix):
    count = len(matrix)
    for row in range(count):
        for column in range(count):
            if matrix[row][column] == "P":
                return row, column


def in_range(end, element):
    if 0 <= element < end:
        return True


def hit_wall(matrix, row, col):
    if matrix[row][col] == "X":
        return True


def is_move_valid(matrix, row, col):
    if in_range(len(matrix), row) and in_range(len(matrix[row]), col) \
            and not hit_wall(matrix, row, col):
        return True


def get_move(command):
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    row_move, col_move = moves[command]
    return row_move, col_move


matrix = get_matrix()
player = get_player_possition(matrix)


player_path = []
total_coins = 0
player_row , player_col = player
command = input()
while command:
    valid_commands = {'up', 'down', 'left', 'right'}
    is_won = True
    if command not in valid_commands:
        command = input()
        continue
    row_move, col_move = get_move(command)
    if not is_move_valid(matrix, player_row + row_move, player_col + col_move):
        if total_coins > 0:
            total_coins /= 2
            total_coins = int(total_coins)
        is_won = False
        break
    player_row += row_move
    player_col += col_move
    total_coins += int(matrix[player_row][player_col])
    player_path.append([player_row, player_col])
    if total_coins >= 100:
        break
    command = input()

if is_won:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")

print("Your path:")
for el in player_path:
    print(f"{el}")



