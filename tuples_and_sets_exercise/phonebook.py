data = input()

phonebook = {}
while not data.isdigit():
    name, phone_number = data.split("-")
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(phone_number)
    data = input()

for _ in range(int(data)):
    contact_name = input()
    if contact_name in phonebook:
        print(f"{contact_name} -> {phonebook[contact_name][-1]}")
    else:
        print(f"Contact {contact_name} does not exist.")