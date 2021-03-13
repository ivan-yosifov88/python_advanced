from collections import deque


def safe_unlocking(bullets, safe_lock, barrel, bullets_shoot):
    for shoot in range(barrel):
        # if not bullets:
        #     break
        bullet = bullets.pop()
        bullets_shoot += 1
        # if not safe_lock:
        #     break
        if bullet <= safe_lock[0]:
            safe_lock.popleft()
            print("Bang!")
        else:
            print("Ping!")
        if not bullets:
            break
        if not safe_lock:
            break
    if bullets and shoot + 1 == barrel:
        print("Reloading!")
    return bullets_shoot


price_of_bullet = int(input())
gun_barrel_size = int(input())

bullets_power_stack = [int(number) for number in input().split()]
locks = deque(int(num) for num in input().split())
value_of_the_intelligence = int(input())
bullets_shoot = 0

while True:
    if not locks:
        earned_money = value_of_the_intelligence - bullets_shoot * price_of_bullet
        print(f"{len(bullets_power_stack)} bullets left. Earned ${earned_money}")
        break
    elif len(bullets_power_stack) == 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    else:
        bullets_shoot = safe_unlocking(bullets_power_stack, locks, gun_barrel_size, bullets_shoot)
