closed_parentheses = []

parentheses = input()
if len(parentheses) % 2 == 0:
    for index in range(len(parentheses) - 1, - 1, - 1):
        if parentheses[index] == ")" or parentheses[index] == "}" or parentheses[index] == "]":
            closed_parentheses.append(parentheses[index])
        elif parentheses[index] == "{" and closed_parentheses[-1] == "}":
            closed_parentheses.pop(-1)
        elif parentheses[index] == "(" and closed_parentheses[-1] == ")":
            closed_parentheses.pop(-1)
        elif parentheses[index] == "[" and closed_parentheses[-1] == "]":
            closed_parentheses.pop(-1)
    if not closed_parentheses:
        print("YES")
    else:
        print("NO")
else:
    print("NO")