from collections import deque

pizza_orders = deque([int(el) for el in input().split(', ')])

employees_pizza_making = [int(el) for el in input().split(', ')]

total_pizzas = 0


def is_order_valid(order):
    if 0 < order <= 10:
        return True


def get_pizzas_count(pizza, count_capacity):
    if count_capacity >= pizza:
        return pizza
    return count_capacity


while True:
    is_all_orders_completed = False
    is_no_employees = False
    if not employees_pizza_making:
        is_no_employees = True
        break
    if not pizza_orders:
        is_all_orders_completed = True
        break
    current_order = pizza_orders[0]
    if not is_order_valid(current_order):
        pizza_orders.popleft()
        continue
    total_pizzas += get_pizzas_count(pizza_orders[0], employees_pizza_making[-1])
    if employees_pizza_making[-1] - current_order >= 0:
        pizza_orders.popleft()
        employees_pizza_making.pop()
    else:
        pizza_orders[0] -= employees_pizza_making[-1]
        employees_pizza_making.pop()

if is_all_orders_completed:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(employee) for employee in employees_pizza_making)}")

if is_no_employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(order) for order in pizza_orders)}")
