inputer = int(input("ввести ціле число n в діапазоні від -5 до 10 "))
if not -5 < inputer < 10:
    print("Error")
    quit()
for i in range(1, 10):
    print(f"{inputer} x {i} = {inputer*int(i)}")