vowels = {'a', 'o', 'u', 'e', 'i'}
vowels_upper = {el.upper() for el in vowels}
vowels.update(vowels_upper)

text = input()

result = [char for char in text if char not in vowels]

print(*result, sep="")