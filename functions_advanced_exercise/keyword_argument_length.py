def kwargs_length(**kwargs):
    return len(kwargs)

dictionary = {'name': 'Peter', 'age': 25, 'baba': 'Peter'}

print(kwargs_length(**dictionary))
