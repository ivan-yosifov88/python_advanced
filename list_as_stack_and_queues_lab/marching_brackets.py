expression = input()

sub_expression = []
for index in range(len(expression)):
    if expression[index] == "(":
        sub_expression.append(index)
    elif expression[index] == ")":
        element = sub_expression.pop()
        print(expression[element:index + 1])

