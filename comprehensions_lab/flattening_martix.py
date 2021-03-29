# If a want to create matrix and then transform it.
# def read_matrix():
#     row_count = int(input())
#     # matrix = []
#     # for _ in range(row_count):
#     #     row = list(map(int, input().split(", ")))
#     #     matrix.append(row)
#     # matrix = [list(map(int, input().split(", "))) for _ in range(row_count)]
#     matrix = [[int(x) for x in input().split(", ")] for _ in range(row_count)]
#     return matrix
# def get_flattened_version(matrix):
#     result = [x for r in range(len(matrix)) for x in matrix[r]]
#     return result

def get_flattened_version():
    row_count = int(input())
    result = [int(x) for _ in range(row_count) for x in input().split(", ") ]
    return result
# matrix = read_matrix()
# flattened_version = get_flattened_version(matrix)
print(get_flattened_version())
