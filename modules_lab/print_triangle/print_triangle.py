def row_triangle(r):
    row = []
    for c in range(1, r + 1):
        row.append(str(c))
    print(' '.join(row))


def print_triangle(n):
    for r in range(1, n + 1):
        row_triangle(r)

    for r in range(n - 1, 0, -1):
        row_triangle(r)