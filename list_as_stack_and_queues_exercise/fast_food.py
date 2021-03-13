from collections import deque

food_quantity = int(input())
orders_quantity = deque(int(number) for number in input().split())
biggest_order = max(orders_quantity)
is_order_complete = True

while orders_quantity:
    if orders_quantity[0] <= food_quantity:
        order = orders_quantity.popleft()
        food_quantity -= order
        # if order > biggest_order:
        #     biggest_order = order
    else:
        is_order_complete = False
        break
print(biggest_order)
if is_order_complete:
    print("Orders complete")
else:
    print("Orders left:", end=" ")
    while orders_quantity:
        print(f"{orders_quantity.popleft()}", end=" ")