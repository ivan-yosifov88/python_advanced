from collections import deque

cup_for_fill = deque(map(int, input().split()))
bottles_stack = list(map(int, input().split()))

wasted_water = 0
is_bottles_over = False

while cup_for_fill:
    if not bottles_stack:
        is_bottles_over = True
        break
    bottle = bottles_stack.pop()
    if bottle < cup_for_fill[0]:
        cup_for_fill[0] -= bottle
    else:
        wasted_water += bottle - cup_for_fill[0]
        cup_for_fill.popleft()
if is_bottles_over:
    print("Cups: ", end="")
    while cup_for_fill:
        print(cup_for_fill.popleft(), end=" ")
else:
    print(f"Bottles: ", end="")
    while bottles_stack:
        print(bottles_stack.pop(), end=" ")
print()
print(f"Wasted litters of water: {wasted_water}")