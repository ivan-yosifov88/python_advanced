from math import log


def get_log():
    number = int(input())
    log_base = input()
    if log_base == 'natural':
        base = log(number)
    elif log_base.isdigit():
        base = int(log_base)
        base = log(number, base)
    return base


def print_result(result):
    print(f"{base_result:.2f}")


base_result = get_log()

print_result(base_result)