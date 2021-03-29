start_index = int(input())
end_index = int(input())

result_list = [number for number in range(start_index, end_index + 1) if any(number % x == 0 for x in range(2, 11))]
print(result_list)


# this is a solution from presentation, and I like how they define ranges !!!!!
# start = int(input())
# end = int(input())
# numbers = [num for num in range(start, end + 1)]
# numbers_one_to_ten = [num for num in range(2, 11)]
#
# filtered = [num for num in numbers if any([num % x == 0 for x in numbers_one_to_ten])]
# print(filtered)
