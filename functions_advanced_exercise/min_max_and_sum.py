def read_input():
    return [int(number) for number in input().split()]


def print_result(numbers):
    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")


number_list = read_input()

print_result(number_list)