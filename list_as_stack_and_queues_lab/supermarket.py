from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

queue = deque([])

while True:
    data = input()
    if data == END_COMMAND:
        break
    elif data == PAID_COMMAND:
        while queue:
            print(queue.popleft())
    else:
        queue.append(data)

print(f"{len(queue)} people remaining.")
