from collections import deque

water_starting_quantity = int(input())

START_COMMAND = "Start"
END_COMMAND = "End"

people_queue = deque()
while True:
    command = input()
    if command == START_COMMAND:
        break
    else:
        people = command
        people_queue.append(people)

dispenser_queue = deque()
while True:
    command = input()
    if command == END_COMMAND:
        break
    elif command.split()[0] == "refill":
        quantity_to_refill = command.split()[1]
        quantity_to_refill = int(quantity_to_refill)
        water_starting_quantity += quantity_to_refill
    else:
        liters = int(command)
        if liters <= water_starting_quantity:
            water_starting_quantity -= liters
            print(f"{people_queue.popleft()} got water")
        else:
            print(f"{people_queue.popleft()} must wait" )

print(f"{water_starting_quantity} liters left")



