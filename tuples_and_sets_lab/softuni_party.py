def guests(regular, vip, count_guests):
    for _ in range(count_guests):
        data = input()
        if len(data) == 8:
            if not data[0].isdigit():
                regular_guests.append(data)
            else:
                vip_guests.append(data)


def check_if_guest(guest , regular , vip):
    if guest in regular_guests:
        regular.remove(guest)
    elif guest in vip:
        vip.remove(guest)


def guests_not_come(regular, vip):
    count = len(regular) + len(vip)
    return count


number_of_guests = int(input())

regular_guests = []
vip_guests = []

guests(regular_guests, vip_guests, number_of_guests)

command = input()

while not command == "END":
    guest_id = command
    if len(guest_id) == 8:
        check_if_guest(guest_id, regular_guests, vip_guests)
    command = input()

print(guests_not_come(regular_guests, vip_guests))
if vip_guests:
    for guest in sorted(vip_guests):
        print(guest)
if regular_guests:
    for guest in sorted(regular_guests):
        print(guest)