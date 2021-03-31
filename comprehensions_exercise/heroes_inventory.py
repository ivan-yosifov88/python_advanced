heroes = input().split(", ")

heroes_dict = {}

for hero in heroes:
    heroes_dict[hero] = {"items": [], "cost": 0}

command = input()

while not command == "End":
    hero_name, item, cost = command.split("-")
    if hero_name in heroes_dict:
        if item not in heroes_dict[hero_name]["items"]:
            heroes_dict[hero_name]["items"].append(item)
            heroes_dict[hero_name]["cost"] += int(cost)
    command = input()

for key, value in heroes_dict.items():
    print(f"{key} -> Items: {len(value['items'])}, Cost: {value['cost']}")