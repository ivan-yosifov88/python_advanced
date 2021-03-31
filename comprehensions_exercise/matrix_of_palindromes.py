alphabet = [chr(i) for i in range(97, 123)]
row_count, col_count = map(int, input().split())

for r in range(row_count):
    for c in range(col_count):
        palindrom = alphabet[r] + alphabet[r + c] + alphabet[r]
        print(palindrom, end=" ")
    print()
