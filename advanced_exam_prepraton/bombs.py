from collections import deque


def is_not_getting_bomb(efect, casing, bombs, bombs_count):
    result = efect + casing
    if result not in bombs.values():
        return True


def action(efect, casing, bombs, bombs_count):

    def get_bomb(efect, casing, bombs):
        for key, values in bombs.items():
            if values == efect + casing:
                return key
    bomb = get_bomb(efect, casing, bombs)
    bombs_count[bomb] += 1


def is_succeed(bombs_count):
    for value in bombs_count.values():
        if not 3 <= value:
            return False
    return True


bombs = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}

bomb_effect = deque(int(x) for x in input().split(", "))

bomb_casing = [int(x) for x in input().split(", ")]

bombs_count = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_effect and bomb_casing:
    effect = int(bomb_effect[0])
    casting = int(bomb_casing[-1])
    if is_not_getting_bomb(effect, casting, bombs, bombs_count):
        bomb_casing[-1] -= 5
    else:
        action(effect, casting, bombs, bombs_count)
        bomb_effect.popleft()
        bomb_casing.pop(-1)
    if is_succeed(bombs_count):
        break
if is_succeed(bombs_count):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")
else:
    print("Bomb Casings: empty")


for key, value in sorted(bombs_count.items()):
    print(f"{key}: {value}")
