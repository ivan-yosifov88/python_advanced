def get_missing_number(numbers):
    numbers_list = sorted(numbers)
    for i in range(len(numbers_list) - 1):
        current_number = numbers_list[i]
        next_number = numbers_list[i + 1]
        if not current_number + 1 == next_number:
            return abs(current_number + 1)


def get_numbers_dict(*args):
    numbers = {}
    for number in args:
        if number not in numbers:
            numbers[number] = 0
        numbers[number] += 1
    return numbers


def get_sorted_duplicates(numbers):
    return sorted(key for key, value in numbers.items() if value > 1)


def numbers_searching(*args):
    numbers = get_numbers_dict(*args)
    missing_number = get_missing_number(numbers)
    numbers_sequence = get_sorted_duplicates(numbers)
    return [missing_number, numbers_sequence]



print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(1, 2, 4, 2, 5, 4))