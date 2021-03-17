list_of_numbers = [float(num) for num in input().split()]

numbers_and_occurrences = {}
for number in list_of_numbers:
    if number not in numbers_and_occurrences:
        numbers_and_occurrences[number] = 0
    numbers_and_occurrences[number] += 1
for key, value in numbers_and_occurrences.items():
    print(f"{key} - {value} times")