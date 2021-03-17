number_of_names = int(input())

set_names = set()

for _ in range(number_of_names):
    names = input()
    set_names.add(names)

for name in set_names:
    print(name)