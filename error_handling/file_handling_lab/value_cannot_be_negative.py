class ValueCannotBeNegative(Exception):
    """
    Raise exception when value is below zero
    """
    pass


count_of_numbers = 5

for number in range(count_of_numbers):
    number = int(input())
    if 0 <= number:
        pass
    else:
        raise ValueCannotBeNegative
