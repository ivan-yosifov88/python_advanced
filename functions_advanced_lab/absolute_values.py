def read_input():
    list_of_numbers = [float(num) for num in input().split()]
    return list_of_numbers


def print_result(numbers_list):
    print([abs(num) for num in numbers_list])


numbers = read_input()

print_result(numbers)