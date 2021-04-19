import re


def word_opener(file_path):
    with open(file_path, 'r') as file:
        words = file.readline().split()
    return words


def text_opener(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    text = re.findall(r'[a-z]+', text, re.IGNORECASE)
    return text


def get_result(words, text):
    result_dict = {}
    for word in words:
        if word in text:
            result_dict[word] = text.count(word)
    return result_dict


def print_result(result_dict):
    sorted_dict = sorted(result_dict.items(), key=lambda x: -x[1])
    for key, value in sorted_dict:
        print(f"{key} - {value}")


word_path = 'words.txt'
text_path = 'input.txt'

word_list = word_opener(word_path)

text_to_check = text_opener(text_path)

result = get_result(word_list, text_to_check)

print_result(result)