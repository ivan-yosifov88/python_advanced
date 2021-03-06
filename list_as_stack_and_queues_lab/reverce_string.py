text = input()

new_text = []

for letter in text:
    new_text.append(letter)
result = ""
while new_text:
    result += new_text.pop()
print(result)
