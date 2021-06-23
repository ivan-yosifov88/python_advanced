from collections import deque


def get_best_result(ll):
    return sum([ll[i]*i for i in range(len(ll))])


def best_list_pureness(*test):
    ll, rotations = test
    ll = deque(ll)
    best_result = get_best_result(ll)
    best_rotation = 0
    for rotation in range(1, rotations+ 1 ):
        element = ll.pop()
        ll.appendleft(element)
        current_sum = get_best_result(ll)
        if best_result < current_sum:
            best_result = current_sum
            best_rotation = rotation
    return f"Best pureness {best_result} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


