from mathematical_opertations import mathematical_operations


expression = input()

first_number, sign, second_number = expression.split()
first_number = float(first_number)
second_number = int(second_number)

result = mathematical_operations.mathematical_operations(first_number, second_number, sign)

print(result)