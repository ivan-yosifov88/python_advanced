def print_expressions(numbers, current_result=0, expression=''):
    if not numbers:
        print(f"{expression}={current_result}")
        return
    plus_result = print_expressions(numbers[1:], current_result + numbers[0], f"{expression}+{numbers[0]}")

    minus_result = print_expressions(numbers[1:], current_result - numbers[0], f"{expression}-{numbers[0]}")


numbers_list = list(map(int, input().split(", ")))
print_expressions(numbers_list)