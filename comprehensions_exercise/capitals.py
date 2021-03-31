country_list = input().split(", ")
capital_list = input().split(", ")
country_capital = zip(capital_list, country_list)
for el in country_capital:
    print(f"{el[1]} -> {el[0]}")
