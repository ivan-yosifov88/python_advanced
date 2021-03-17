def range_one(range_first):
    list_first = []
    start, end = range_first.split(",")
    start = int(start)
    end = int(end) + 1
    for number in range(start, end):
        list_first.append(number)
    return list_first


def range_two(range_second):
    list_second = []
    start, end = range_second.split(",")
    start = int(start)
    end = int(end) + 1
    for number in range(start, end):
        list_second.append(number)
    return list_second


def set_intersection(list_one, list_two, list_of_intersections):
    result = set.intersection(set(list_one), set(list_two))
    list_of_intersections.append(result)


number_of_lines = int(input())

intersections = []

for _ in range(number_of_lines):
    first_range, second_range = input().split("-")
    list_first_range = range_one(first_range)
    list_second_range = range_two(second_range)
    set_intersection(list_first_range, list_second_range, intersections)

longest_intersection_len = 0
longest_intersection = []

for element in intersections:
    if len(element) > longest_intersection_len:
        longest_intersection_len = len(element)
        longest_intersection = list(element)

print(f"Longest intersection is {longest_intersection} with length {longest_intersection_len}")
