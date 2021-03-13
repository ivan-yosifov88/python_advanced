from collections import  deque

petrol_pumps = int(input())

amount_of_petrol = deque()
distance_to_next_petrol_pump = deque()

for pumps in range(petrol_pumps):
    petrol, distance = input().split()
    amount_of_petrol.append(int(petrol))
    distance_to_next_petrol_pump.append(int(distance))

for index in range(petrol_pumps):
    if amount_of_petrol[0] < distance_to_next_petrol_pump[0]:
        amount_of_petrol.append(amount_of_petrol.popleft())
        distance_to_next_petrol_pump.append(distance_to_next_petrol_pump.popleft())
        continue
    fuel_tank = 0
    for i in range(petrol_pumps):
        fuel_tank += amount_of_petrol[i]
        fuel_tank -= distance_to_next_petrol_pump[i]
        if fuel_tank < 0:
            break
    if fuel_tank >= 0:
        print(index)
        break
    else:
        amount_of_petrol.append(amount_of_petrol.popleft())
        distance_to_next_petrol_pump.append(distance_to_next_petrol_pump.popleft())