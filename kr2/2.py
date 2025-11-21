inputer = input("ввести цілі числа, розділені пробілами ").split()
def loop():
    new_list = []
    for i in inputer:
        if int(i) < 0:
            i = 0
        new_list.append(int(i))
    print(f"Ввід: {inputer} \nВивід: {new_list}")
def comprehension():
    comprehension = [0 if int(i) < 0 else int(i) for i in inputer]
    print(f"Ввід: {inputer} \nВивід: {comprehension}")
choose = input("loop (1) or list comp. (2) ")
if int(choose.strip()) == 1:
    loop()
elif int(choose.strip()) == 2:
    comprehension()