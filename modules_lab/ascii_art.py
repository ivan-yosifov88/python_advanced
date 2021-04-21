from pyfiglet import figlet_format, print_figlet
from termcolor import colored


def print_art(message_to_transform):
    ascii_art = figlet_format(message_to_transform)
    print(ascii_art)


message = input()


# print(colored(figlet_format(message, font='doh'), color="blue"))

print_art(message)
