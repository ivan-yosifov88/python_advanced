categories_list = input().split(", ")
number_of_lines = int(input())

bunker = {}
for category in categories_list:
    bunker[category] = {'item': [], 'quantity': 0, 'quality': 0}

for _ in range(number_of_lines):
    current_category, item, info = input().split(' - ')
    info_one, info_two = info.split(";")
    _, quantity_value = info_one.split(":")
    _, quality_value = info_two.split(":")

    if current_category in bunker:
        bunker[current_category]['item'].append(item)
        bunker[current_category]['quantity'] += int(quantity_value)
        bunker[current_category]['quality'] += int(quality_value)
sum_quantity = 0
items_count = len(categories_list)
sum_quality = 0
for values in bunker.values():
    sum_quantity += values['quantity']
    sum_quality += values['quality']
print(f"Count of items: {sum_quantity}")
print(f"Average quality: {sum_quality/items_count:.2f}")
for key, value in bunker.items():
    print(f"{key} -> {', '.join(value['item'])}")

