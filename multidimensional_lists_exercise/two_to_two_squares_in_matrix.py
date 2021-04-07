def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'B', 'D'],
            ['E', 'B', 'B', 'B'],
            ['I', 'J', 'B', 'B'],
        ]
    else:
        row_count, column_count = map(int, input().split())
        matrix = []
        for r in range(row_count):
            row = input().split()
            matrix.append(row)
        return matrix


def is_matrix_elements_equal(s_matrix):
    if s_matrix.count(s_matrix[0][0]) == 4:
        return s_matrix


def get_sub_matrix(matrix, r_index, c_index, sub_matrix_size):
    sub_matrix = []
    for r in range(r_index, r_index + sub_matrix_size):
        for c in range(c_index, c_index + sub_matrix_size):
            sub_matrix.append(matrix[r][c])
    return sub_matrix


def get_list_sub_matrix(matrix, sub_matrix_size):
    list_of_sub_matrix = []
    r_count = len(matrix)
    c_count = len(matrix[0])
    for row_index in range(r_count - sub_matrix_size + 1):
        for column_index in range(c_count - sub_matrix_size + 1):
            result = get_sub_matrix(matrix, row_index, column_index, sub_matrix_size)
            sub_matrix = is_matrix_elements_equal(result)
            if sub_matrix:
                list_of_sub_matrix.append(sub_matrix)
    return list_of_sub_matrix


def get_valid_sub_matrix_count(sub_list):
    result_dict = {}
    for element in sub_list:
        if element[0] not in result_dict:
            result_dict[element[0]] = 0
        result_dict[element[0]] += 1
    return result_dict


def print_result(valid_count_sub_matrix):
    max_value = 0
    for value in valid_count_sub_matrix.values():
        if value > max_value:
            max_value = value
    print(max_value)


SUB_MATRIX_SIZE = 2

matrix = read_matrix()
list_of_sub_matrix = get_list_sub_matrix(matrix, SUB_MATRIX_SIZE)
sub_matrix_valid_count = get_valid_sub_matrix_count(list_of_sub_matrix)
print_result(sub_matrix_valid_count)
