from collections import deque


def delivery(list_of_boxes, *args):
    for el in args:
        list_of_boxes.append(el)


def sell(list_of_boxes, *args):
    if not args:
        return list_of_boxes.popleft()
    element = args[0]
    if type(element) == int:
        element = int(element)
        for _ in range(element):
            list_of_boxes.popleft()
        return list_of_boxes
    for el in args:
        while el in list_of_boxes:
            list_of_boxes.remove(el)
    return list_of_boxes


def stock_availability(list_of_boxes, command, *args):
    list_of_boxes = deque(list_of_boxes)
    if command == 'delivery':
        delivery(list_of_boxes, *args)
    elif command == 'sell':
        sell(list_of_boxes, *args)
    return list(list_of_boxes)







print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
