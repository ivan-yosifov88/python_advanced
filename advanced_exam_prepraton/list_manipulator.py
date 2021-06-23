def list_manipulator(number_list, *args):
    if args[0] == "add":
        if args[1] == "beginning":
            return [el for el in args[2:]] + number_list
        elif args[1] == "end":
            return number_list + [el for el in args[2:]]
    elif args[0] == "remove":
        if args[1] == "beginning":
            if args[2:]:
                return number_list[args[2]:]
            return number_list[1:]
        elif args[1] == "end":
            if args[2:]:
                return number_list[:-args[2]]
            return number_list[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
