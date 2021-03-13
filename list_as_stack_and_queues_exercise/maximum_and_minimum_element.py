number_of_sequence = int(input())
max_elements = []
min_elements = []
stack_with_numbers = []


for _ in range(1, number_of_sequence + 1):
    line = input()
    data = line.split()[0]
    data = int(data)
    if data == 1:
        number = line.split()[1]
        number = int(number)
        if len(max_elements) == 0:
            max_elements.append(number)
        else:
            if max_elements[-1] <= number:
                max_elements.append(number)
        if len(min_elements) == 0:
            min_elements.append(number)
        else:
            if min_elements[-1] >= number:
                min_elements.append(number)
        stack_with_numbers.append(number)
    elif data == 2:
        if len(stack_with_numbers) > 0:
            element_to_remove = stack_with_numbers.pop()
            if element_to_remove == max_elements[-1]:
                max_elements.pop()
            if element_to_remove == min_elements[-1]:
                min_elements.pop()
    elif data == 3:
        if max_elements:
            print(max_elements[-1])
    elif data == 4:
        if min_elements:
            print(min_elements[-1])

while stack_with_numbers:
    if len(stack_with_numbers) > 1:
        print(stack_with_numbers.pop(), end=", ")
    else:
        print(stack_with_numbers.pop())

