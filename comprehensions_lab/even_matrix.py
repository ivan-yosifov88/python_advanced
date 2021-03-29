def read_matrix():
    number_of_rows = int(input())
    matrix = [[int(x) for x in input().split(", ")] for _ in range(number_of_rows)]
    return matrix


def get_even_matrix(matrix):
    # even_matrix = []
    # for r in range(len(matrix)):
    #     row = []
    #     for el in matrix[r]:
    #         if int(el) % 2 == 0:
    #             row.append(int(el))
    #     even_matrix.append(row)
    #
    even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
    # This is better solution
    # even_matrix = []
    # for row in matrix:
    #     for x in row:
    #         if x % 2 == 0:
    #             even_matrix.append(x)
    return even_matrix


def print_result(even_matrix):
    return print(even_matrix)


matrix = read_matrix()
even_matrix = get_even_matrix(matrix)
print_result(even_matrix)
