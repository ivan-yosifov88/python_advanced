def get_dartboard(size):
    dartboard = []
    for r in range(size):
        dartboard.append(input().split())
    return dartboard


def multiply_sector(row, col, datrboard, size, mulyiply_by):
    up = int(datrboard[size - size][col])
    down = int(datrboard[size - 1][col])
    left = int(datrboard[row][size - 1])
    right = int(datrboard[row][size - size])
    result_points = (up + down + left + right) * mulyiply_by
    return result_points



def in_range(index, size):
    return 0 <= index < size


def swap(players):
    players[0], players[1] = players[1], players[0]
    return players


def reduce_player_points(current_player, points):
    current_player[1] -= points
    return current_player


DARTBOARD_SIZE = 7
INITIAL_POINTS = 501
DOUBLE_SECTOR = 2
TRIPLE_SECTOR = 3

first_player_name, second_player_name = input().split(", ")

datrboard = get_dartboard(DARTBOARD_SIZE)

first_player = [first_player_name, INITIAL_POINTS, 0]

second_player = [second_player_name, INITIAL_POINTS, 0]

trow = input()

players = [first_player, second_player]



while trow:
    is_player_win = False
    result = trow.strip("()")
    row_index, column_index = result.split(", ")
    row_index = int(row_index)
    column_index = int(column_index)

    players[0][2] += 1
    if not in_range(row_index, DARTBOARD_SIZE) or not in_range(column_index, DARTBOARD_SIZE):
        players = swap(players)
        trow = input()
        continue
    if datrboard[row_index][column_index] == "D":
        points = multiply_sector(row_index, column_index, datrboard, DARTBOARD_SIZE, DOUBLE_SECTOR)
        players[0] = reduce_player_points(players[0], points)
    elif datrboard[row_index][column_index] == "T":
        points = multiply_sector(row_index, column_index, datrboard, DARTBOARD_SIZE, TRIPLE_SECTOR)
        reduce_player_points(players[0], points)
    elif datrboard[row_index][column_index] == "B":
        is_player_win = True
        break
    else:
        points = int(datrboard[row_index][column_index])
        reduce_player_points(players[0], points)
    if players[0][1] <= 0:
        is_player_win = True
        break
    players = swap(players)
    trow = input()

if is_player_win:
    name = players[0][0]
    count_turns = players[0][2]
    print(f"{name} won the game with {count_turns} throws!")


