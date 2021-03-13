from datetime import datetime, timedelta

from collections import deque

robots = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")

details_line = deque()

robots_on_the_line = {}

for robot in robots:
    current_robot, processing_time = robot.split("-")
    robots_on_the_line[current_robot] = {"processing_time": int(processing_time), "free_at": 0}

while True:
    details = input()
    if details == "End":
        break
    details_line.append(details)

current_time = 0
while details_line:
    current_time += 1
    current_detail = details_line.popleft()
    for r in robots_on_the_line:
        if robots_on_the_line[r]["free_at"] <= current_time:
            print(f"{r} - {current_detail} [{(time + timedelta(seconds=current_time)).strftime('%H:%M:%S')}]")
            robots_on_the_line[r]["free_at"] = current_time + robots_on_the_line[r]["processing_time"]
            break
    else:
        details_line.append(current_detail)


