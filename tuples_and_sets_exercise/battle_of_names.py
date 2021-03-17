def line_letter_result(text, divider):
    result = 0
    for letter in text:
        result += ord(letter)
    return result // divider


def even_odd_add(even, odd, result):
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)


def final_result(even, odd):
    result = set()
    if sum(even) == sum(odd):
        result = set.union(even, odd)
    elif sum(odd) > sum(even):
        result = set.difference(odd, even)
    else:
        result = set.symmetric_difference(even, odd)
    return result


number_of_lines = int(input())
even_set = set()
odd_set = set()


for index in range(1, number_of_lines + 1):
    line = input()
    letter_result = line_letter_result(line, index)
    even_odd_add(even_set, odd_set, letter_result)

print(", ".join(map(str, final_result(even_set, odd_set))))



