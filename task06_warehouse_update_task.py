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
