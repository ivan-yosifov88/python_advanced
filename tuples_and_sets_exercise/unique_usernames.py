number_of_users = int(input())

usernames = set()

for _ in range(number_of_users):
    user = input()
    usernames.add(user)
print("\n".join(usernames))
