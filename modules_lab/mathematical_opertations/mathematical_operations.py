from .expressions import *


def mathematical_operations(x, y, sign):
    if sign == "/":
        result = divide(x, y)
    elif sign == "*":
        result = multiply(x, y)
    elif sign == "-":
        result = subtract(x, y)
    elif sign == "+":
        result = add(x, y)
    elif sign == "^":
        result = power(x, y)
    return f"{result:.2f}"
