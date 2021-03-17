number_of_lines = int(input())

chemicals_elements_set = set()
for _ in range(number_of_lines):
    line = input().split()
    chemicals_elements_set.update(line)
print("\n".join(chemicals_elements_set))