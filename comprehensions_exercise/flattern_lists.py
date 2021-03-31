list_of_numbers = input().split("|")

# while list_of_numbers:
#     removed_element = list_of_numbers.pop()
#     removed_element = removed_element.split()
#     for el in removed_element:
#         print(el, end=" ")
for i in range(len(list_of_numbers) - 1, - 1, - 1):
    current_list = list_of_numbers[i].split()
    for num in current_list:
        print(num, end=" ")



