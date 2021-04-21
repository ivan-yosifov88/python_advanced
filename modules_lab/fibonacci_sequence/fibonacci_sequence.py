seq = [0, 1]


def generate_sequence(n):
    global seq
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        seq = [0, 1]
        for num in range(2, n):
            seq.append(seq[num - 1] + seq[num - 2])
        return seq


def locate_number_in_sequence(number):
    if number in seq:
        current_index = seq.index(number)
        return f"The number - {number} is at index {current_index}"
    else:
        return f"The number {number} is not in the sequence"



