"""
Task 1 — Shopping Cart Tracker 🛒

Real-world context:
  A POS app keeps a shopping cart as a Python list.

Requirements:
  1) Start with cart = ["milk", "bread", "eggs", "apples", "coffee"].
  2) Print each item for a receipt using a for-loop (numbered lines).
  3) Add two items: "cheese" and "butter".
  4) Print the updated cart on one line (comma-separated).

Practice: lists, for-loops, enumerate, str.join

OUTPUT EXAMPLE
--------------
Receipt items:
1. milk
2. bread
3. eggs
4. apples
5. coffee

Updated cart: milk, bread, eggs, apples, coffee, cheese, butter
"""

cart = ["milk", "bread", "eggs", "apples", "coffee"]

print("(Starter) Initial cart:", cart)
# TODO: print items as numbered receipt lines using a for-loop
n = 0
for ing in cart:
    n = n + 1
    print(f"{n}. {ing}")
# TODO: add "cheese" and "butter" to the list
another_cart = ["cheese", "butter"]
cart.extend(another_cart)
# TODO: print updated cart as one comma-separated line
for ing in range(len(cart)):
    print(cart[ing], end="")
    if ing < len(cart) - 1:
        print(", ", end= "")