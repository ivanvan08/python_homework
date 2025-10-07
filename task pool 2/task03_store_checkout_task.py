
"""
🛒 TASK 3 — Store Checkout
Topic: dict lookup + loop over a list

Price list: {"apple": 30, "banana": 20, "orange": 25}
Basket:     ["apple", "apple", "banana", "orange"]
Compute total basket cost and print the result.

"""
# Starter:
prices = {"apple": 30, "banana": 20, "orange": 25}
basket = ["apple", "apple", "banana", "orange"]
# TODO: compute total using a loop; print total
a = 0
for i in basket:
    if i in prices:
        a += prices[i]
print(a)