from collections import deque

game_players = deque(input().split())

number_of_toss = int(input())

while len(game_players) > 1:
    for _ in range(number_of_toss - 1):
        game_players.append(game_players.popleft())
    print(f"Removed {game_players.popleft()}")

print(f"Last is {game_players.popleft()}")