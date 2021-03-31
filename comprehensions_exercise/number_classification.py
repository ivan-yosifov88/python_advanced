num_list = input().split(", ")
positive_numbers = [num for num in num_list if int(num) >= 0]
negative_numbers = [num for num in num_list if int(num) < 0]
even_numbers = [num for num in num_list if int(num) % 2 == 0]
odd_numbers = [num for num in num_list if int(num) % 2 == 1]
print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")