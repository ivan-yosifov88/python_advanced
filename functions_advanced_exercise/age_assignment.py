def age_assignment(*args, **kwargs):
    result_dictionary = {}
    for name in args:
        if name[0] in kwargs:
            result_dictionary[name] = kwargs[name[0]]
    return result_dictionary

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))