from collections import deque

row_count, column_count = map(int, input().split())

text = deque(input())

matrix = []

for r in range(row_count):
    row = deque()
    for c in range(column_count):
        if r % 2 == 0:
            symbol = text.popleft()
            row.append(symbol)
            text.append(symbol)
        else:
            symbol = text.popleft()
            row.appendleft(symbol)
            text.append(symbol)
    matrix.append(row)

for r in range(row_count):
    for c in range(column_count):
        print(''.join(matrix[r][c]), end="")
    print()