from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches_count = 0
while females and males:
    if females[0] <= 0:
        females.popleft()
    elif males[-1] <= 0:
        males.pop(-1)
    elif females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
        else:
            break
    elif males[-1] % 25 == 0:
        males.pop(-1)
        if males:
            males.pop(-1)
        else:
            break
    elif females[0] == males[-1]:
        matches_count += 1
        females.popleft()
        males.pop(-1)
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches_count}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(str(num) for num in males[::-1])}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(num) for num in females)}")