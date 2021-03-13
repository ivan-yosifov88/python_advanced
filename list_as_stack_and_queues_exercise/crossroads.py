from collections import deque

def green_light_cycle(queue, green_light_time, free_window_time, car_pass_safe):
    while queue:
        car = queue[0]
        if len(car) < green_light_time:
            car_pass_safe += 1
            queue.popleft()
            green_light_time -= len(car)
        elif len(car) == green_light_time:
            car_pass_safe += 1
            queue.popleft()
            break
        else:
            free_window_time += green_light_time
            if len(car) <= free_window_time:
                queue.popleft()
                car_pass_safe += 1
                break
            else:
                character_hit = car[free_window_time: free_window_time + 1]
                car_crash = queue.popleft()
                return f"A crash happened!\n{car_crash} was hit at {character_hit}."
    return True, car_pass_safe


green_light_duration = int(input())
free_window_duration = int(input())
END_COMMAND = "END"
GREEN_LIGHT = "green"

car_pass = 0
car_queue = deque()
while True:
    command = input()
    if command == END_COMMAND:
        print("Everyone is safe.")
        print(f"{car_pass} total cars passed the crossroads.")
        break
    elif command == GREEN_LIGHT:
        result = green_light_cycle(car_queue, green_light_duration, free_window_duration, car_pass)
        if result[0] is True:
            car_pass = result[1]
        else:
            print(result)
            break
    else:
        car_model = command
        car_queue.append(car_model)
