inputer = input("ввести речення ").strip().split()
def loop():
    new_list = []
    for word in inputer:
        if len(word) <= 3:
            new_list.append(word.upper())
    return print(new_list)
def comprehension():
    new_list = [word.upper() for word in inputer if len(word) <= 3]
    return print(new_list)
choose = input("loop (1) or list comp. (2) ")
if int(choose.strip()) == 1:
    print(inputer, "->")
    loop()
elif int(choose.strip()) == 2:
    print(inputer, "->")
    comprehension()