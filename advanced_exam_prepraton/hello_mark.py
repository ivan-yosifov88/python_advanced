def get_field(size):
    field = []
    for i in range(size):
        row = list(input())
        field.append(row)
    return field


def get_commands():
    commands = []
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, - 1)
    }
    number_of_commands = int(input())

    for line in range(number_of_commands):
        current_command = input()
        if current_command in directions:
            commands.append(directions[current_command])

    return commands


def get_player_position(field):
    size = len(field)
    for row in range(size):
        for column in range(size):
            if field[row][column] == "P":
                return row, column


def in_range(row, column, field):
    size = len(field)
    if 0 <= row < size and 0 <= column < size:
        return True


def player_move(move, row, column ,field, text):
    r, c = move
    if in_range(row + r, column + c, field):
        field[row][column] = "-"
        row += r
        column += c
        if not field[row][column] == "-":
            text.append(field[row][column])
            field[row][column] = "P"
    else:
        if text:
            text.pop()
    return row, column


def print_text(text):
    print(''.join(text))


def print_field(field):
    for row in field:
        print(''.join(row))


text = list(input())

field_size = int(input())

field = get_field(field_size)

commands = get_commands()

row, column = get_player_position(field)

for move in commands:
    row, column = player_move(move, row, column, field, text)


print_text(text)

print_field(field)
