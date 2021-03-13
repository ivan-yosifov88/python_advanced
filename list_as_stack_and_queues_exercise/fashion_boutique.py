clothes_in_box = [int(number) for number in input().split()]
capacity = int(input())

rack = 1
clothes_for_current_rack = 0
while clothes_in_box:
    clothes = clothes_in_box.pop()
    if clothes_for_current_rack + clothes <= capacity:
        clothes_for_current_rack += clothes
    else:
        clothes_for_current_rack = clothes
        rack += 1
print(rack)

