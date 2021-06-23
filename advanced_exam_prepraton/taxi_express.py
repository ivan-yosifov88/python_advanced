from _collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = [int(x) for x in input().split(", ")]


total_time = 0
while customers and taxis:
    if customers[0] <= taxis[-1]:
        time = customers.popleft()
        taxis.pop()
        total_time += time
    else:
        taxis.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")