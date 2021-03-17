def parking(cars_in, cars):
    for _ in range(cars):
        direction, car_number = input().split(", ")
        if direction == "IN":
            cars_in.add(car_number)
        elif direction == "OUT":
            if car_number in cars_in:
                cars_in.remove(car_number)


def parking_lot(cars):
    for car in cars:
        print(car)


number_of_cars = int(input())

cars_in_parking = set()
parking(cars_in_parking, number_of_cars)
if cars_in_parking:
    parking_lot(cars_in_parking)
else:
    print("Parking Lot is Empty")