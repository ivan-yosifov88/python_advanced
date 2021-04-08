from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)
    elif operator == "/":
        return reduce(lambda x, y: x / y, args)


# def operate(operator, *args):
#     if operator == "+":
#         result = sum(args)
#     elif operator == "-":
#         result = args[0]
#         for num in args[1:]:
#             result -= num
#     elif operator == "*":
#         result = 1
#         for num in args:
#             result *= num
#     elif operator == "/":
#         result = args[0]
#         for num in args[1:]:
#             result /= num
#     return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 6, 2))
print(operate("-", 3, 4))