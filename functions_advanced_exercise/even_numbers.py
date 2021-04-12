def read_input():
    return [int(number) for number in input().split()]


def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def print_result(even_nums):
    print(even_nums)


numbers_list = read_input()

result = even_numbers(numbers_list)

print_result(result)