def combinations(text, index=0):
    if index == len(text):
        print(''.join(text))
        return
    for i in range(index, len(text)):
        text[index], text[i] = text[i], text[index]
        combinations(text, index + 1)
        text[index], text[i] = text[i], text[index]


string_as_list = list(input())

combinations(string_as_list)
