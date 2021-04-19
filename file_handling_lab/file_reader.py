numbers_sum = 0

with open('numbers.txt', "r") as file:
    for number in file:
        numbers_sum += int(number)

print(numbers_sum)