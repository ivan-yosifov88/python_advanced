def print_combinations(names, chairs, combinations=[]):
    if len(combinations) == chairs:
        print(*combinations, sep=", ")
        return
    for index in range(len(names)):
        combinations.append(names[index])
        print_combinations(names[index + 1:], chairs)
        combinations.pop()


peoples = input().split(", ")
number_of_chairs = int(input())
print_combinations(peoples, number_of_chairs)


