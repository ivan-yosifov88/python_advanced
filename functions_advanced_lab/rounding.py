def read_input():
    number_list = [float(number) for number in input().split()]
    return number_list


def print_result(numbers):
    print([round(number) for number in numbers])


list_numbers = read_input()

print_result(list_numbers)