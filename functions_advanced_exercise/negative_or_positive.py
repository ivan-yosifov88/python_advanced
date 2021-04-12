def read_input():
    return [int(number)for number in input().split()]


def divide_positive_from_negative(numbers):
    positive_numbers = []
    negative_numbers = []
    for number in numbers:
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
    return positive_numbers, negative_numbers


def print_result(divide_func_result):
    positive_numbers, negative_numbers = divide_func_result
    positive_sum = sum(positive_numbers)
    negative_sum = sum(negative_numbers)
    print(negative_sum)
    print(positive_sum)
    if positive_sum > abs(negative_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


number_list = read_input()

result = divide_positive_from_negative(number_list)

print_result(result)