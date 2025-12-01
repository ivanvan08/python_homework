my_list = input("введіть числа через пробіли" ).strip().split()
new_list = []
for element in my_list:
    new_list.append(int(element))