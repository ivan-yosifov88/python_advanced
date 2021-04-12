def read_numbers():
    return [int(number) for number in input().split()]


def even_odd_command(numbers):
    even_numbers_sum = 0
    odd_numbers_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers_sum += number
        else:
            odd_numbers_sum += number
    return even_numbers_sum, odd_numbers_sum
        

def print_result(result, current_command, numbers):
    even_sum, odd_sum = result
    if current_command == "Even":
        even_sum *= len(numbers)
        print(even_sum)
    elif current_command == "Odd":
        odd_sum *= len(numbers)
        print(odd_sum)


command = input()

number_list = read_numbers()

result = even_odd_command(number_list)

print_result(result, command, number_list)