import re


def replace_symbols(current_line):
    pattern = r"[-,.!?]"
    return re.sub(pattern, '@', current_line)


text = []
with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in range(len(lines)):
        if line % 2 == 0:
            replaced_string = replace_symbols(lines[line]).split()
            reversed_line = ' '.join(replaced_string[::-1])
            result = ''.join(reversed_line)
            print(result)
