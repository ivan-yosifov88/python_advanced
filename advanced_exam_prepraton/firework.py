from collections import deque


def is_fireworks_enough(fireworks):
    for el in fireworks.values():
        if el < 3:
            return False
    return True


def is_less_or_equal_to_zero(index, seq):
    if seq[index] <= 0:
        return True


def remove_elements(effect, power):
    effect.popleft()
    power.pop()


firework_effect = deque([int(el) for el in input().split(', ')])

explosive_power = [int(el) for el in input().split(', ')]

fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}

while firework_effect and explosive_power and not is_fireworks_enough(fireworks):
    if is_less_or_equal_to_zero(0, firework_effect):
        firework_effect.popleft()
        continue
    if is_less_or_equal_to_zero(-1, explosive_power):
        explosive_power.pop()
        continue
    sum_of_fireworks = firework_effect[0] + explosive_power[-1]
    if sum_of_fireworks % 3 == 0 and sum_of_fireworks % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
        remove_elements(firework_effect, explosive_power)
    elif sum_of_fireworks % 3 == 0:
        fireworks['Palm Fireworks'] += 1
        remove_elements(firework_effect, explosive_power)
    elif sum_of_fireworks % 5 == 0:
        fireworks['Willow Fireworks'] += 1
        remove_elements(firework_effect, explosive_power)

    else:
        # firework_effect[0] -= 1
        firework_effect.append(firework_effect.popleft() -1)

if is_fireworks_enough(fireworks):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effect)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")

for firework, count in fireworks.items():
    print(f"{firework}: {count}")

