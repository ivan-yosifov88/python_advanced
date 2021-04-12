def read_input():
    return [int(number) for number in input().split()]


def sort_func(numbers):
    return sorted(numbers)


def print_result(sort_numbers):
    print(sort_numbers)


number_list = read_input()

result = sort_func(number_list)

print_result(result)