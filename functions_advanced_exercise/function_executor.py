def func_executor(*args):
    result = []
    for items in args:
        func_name, func_args = items
        result.append(func_name(*func_args))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
