from os import remove


def create_file_command(file_name):
    with open(file_name, 'w') as file:
        return file.write("")


def add_file_command(file_name, content):
    with open(file_name, 'a') as file:
        result = (file.write(content), file.write('\n'))
    return result


def replace_file_command(file_name, old_string, new_string):
    try:
        with open(file_name, 'r+') as file:
            text = file.read()
            if old_string in text:
                text = text.replace(old_string, new_string)
                file.seek(0)
                return file.write(text)
    except FileNotFoundError:
        print("An error occurred")


def delete_file_command(file_name):
    try:
        remove(file_name)
        return
    except FileNotFoundError:
        print("An error occurred")


# create_file_command("file.txt",)
# add_file_command('file.txt', 'First Line')
# add_file_command('file.txt', 'Second Line')
# replace_file_command('random.txt', 'some', 'first')
# replace_file_command('file.txt', 'First', '1st')
# delete_file_command('random.txt')
# delete_file_command('file.txt')

#
# def read_commands():
#     data = input()
#     while not data == "End":
#         command, command_data = data.split('-')[0], data.split('-')[1:]
#         command_action(command_holder, command, command_data)
#         data = input()


def command_action(command_dict, current_command, command_info):
    return command_dict[current_command](*command_info)


command_holder = {
    'Create': create_file_command,
    'Add': add_file_command,
    'Replace': replace_file_command,
    'Delete': delete_file_command
}

# read_commands()

data = input()

while not data == "End":
    command, command_data = data.split('-')[0], data.split('-')[1:]
    command_action(command_holder, command, command_data)
    data = input()
