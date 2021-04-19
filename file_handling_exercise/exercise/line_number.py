import re


def count_of_letters(current_line):
    letter_pattern = r'[a-zA-z]'
    return len(re.findall(letter_pattern, current_line))


def count_of_punctuation_marks(current_line):
    punctuation_pattern = r'[-,.!?\']'
    return len(re.findall(punctuation_pattern, current_line))


file_path = 'text.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        print(f"Line {i + 1} {line} ({count_of_letters(line)})({count_of_punctuation_marks(line)})")


