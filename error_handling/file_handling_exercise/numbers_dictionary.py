def print_error_message_for_non_existing_key():
    print("Number does not exist in dictionary")


def is_number_in_dictionary(dict, number):
    if number in dict:
        return True
    else:
        print_error_message_for_non_existing_key()


numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()

while line != "Remove":
    searched = line
    if is_number_in_dictionary(numbers_dictionary, searched):
        print(numbers_dictionary[searched])
    line = input()

line = input()

while line != "End":
    searched = line
    if is_number_in_dictionary(numbers_dictionary, searched):
        del numbers_dictionary[searched]
    line = input()

print(numbers_dictionary)
