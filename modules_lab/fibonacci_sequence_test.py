from fibonacci_sequence import fibonacci_sequence

sequence = []
while True:
    data = input()
    if data == "Stop":
        break
    data_info = data.split()
    command = data_info[0]
    number = int(data_info[-1])
    if command == "Create":
        sequence = fibonacci_sequence.generate_sequence(number)
        print(sequence)
    elif command == "Locate":
        print(fibonacci_sequence.locate_number_in_sequence(number))

    