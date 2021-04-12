def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [number for number in args[:-1] if number % 2 == 0]
    else:
        return [number for number in args[:-1] if number % 2 == 1]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))