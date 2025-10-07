"""
Task 6 — Warehouse Stock Update 🏭

Requirements:
  - inventory = [["laptops", 15], ["keyboards", 40], ["mice", 30]]
  - A customer buys 3 keyboards
  - Use a loop to find "keyboards" and decrease quantity (not below 0)
  - Print old and new quantity

Practice: lists of lists, searching, in-place mutation

OUTPUT EXAMPLE
--------------
Inventory: [['laptops', 15], ['keyboards', 37], ['mice', 30]]
keyboards: 40 -> 37
"""

inventory = [["laptops", 15], ["keyboards", 40], ["mice", 30]]
print("(Starter) Inventory:", inventory)
# TODO: find "keyboards" row and subtract 3 (min 0), then print before/after
whattobuy = input("what from the list do you want to buy ")
howmany = input("how many? ")
for i in inventory:
    if whattobuy in str(i) and whattobuy != "," and whattobuy != "":
        if int(howmany) <= i[1]:
            print(f"{whattobuy}: {i[1]}->{i[1]-int(howmany)}")
        else:
            print("we don't have that amount of product")
            wanttobuy = input("do you want to buy all what we have? (yes or no)")
            if wanttobuy.lower() == "yes":
                howmany = i[1]
                print(f"{whattobuy}: {i[1]}->{i[1] - int(howmany)}. Thanks for buying all!!!")
            elif wanttobuy.lower() == "no":
                print("change your product or amount")
                break
            else: print("input yes or no next time")
