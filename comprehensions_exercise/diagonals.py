def read_matrix():
    # matrix = []
    row_count = int(input())
    # for _ in range(row_count):
    #     row = input().split(", ")
    matrix = [[int(el) for el in input().split(", ")] for _ in range(row_count)]
    return matrix


def get_first_diagonal_sum(matrix):
    first_sum = [matrix[r][r] for r in range(len(matrix))]
    return first_sum


def get_second_diagonal_sum(matrix):
    second_sum = [matrix[r][len(matrix) - 1 - r] for r in range((len(matrix)))]
    return second_sum


matrix = read_matrix()
first_diagonal = get_first_diagonal_sum(matrix)
second_diagonal = get_second_diagonal_sum(matrix)
print(f"First diagonal: {', '.join(str(el) for el in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(el) for el in second_diagonal)}. Sum: {sum(second_diagonal)}")
