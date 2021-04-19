from os import listdir


def get_content():
    return listdir()


def get_content_as_dictionary(content):
    report = {}
    for file in content:
        file, separator, extension = file.partition(".")
        if extension not in report:
            report[extension] = []
        report[extension].append(file)
    return report


def print_result(file_dict):
    sorted_file_dict = sorted(file_dict.items(), key=lambda x: (x[1], x[0]))
    for key, value in sorted_file_dict:
        print(f".{key}")
        for val in value:
            print(f"- - - {val}")


file_content = get_content()

file_dictionary = get_content_as_dictionary(file_content)

print_result(file_dictionary)

