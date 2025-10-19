inputs = input("input numbers, use space to write another one ")
number = []
sum = 0
counter = 0
for i in inputs.split(" "):
    number.append(int(i))
    sum += int(i)
    counter+=1
print(number)
def get_min():
    return min(number)
def get_max():
    return max(number)
def get_average():
    return sum/counter
# def sort():
#     sorted_list = []
#     counter = 0
#     sorted_number = number[counter]
#     for x in number:
#         while x > sorted_number:
#             counter += 1



def get_median():
    sort = sorted(number)
    indexed = round(counter / 2)
    if counter % 2 == 1:
        return sort[indexed // 2]
    else:
        medr = counter//2
        medl = counter//2 - 1
        return (sort[medr]+sort[medl])/2
print(f"""min {get_min()}
max {get_max()}
average {get_average()}
median {get_median()}""")