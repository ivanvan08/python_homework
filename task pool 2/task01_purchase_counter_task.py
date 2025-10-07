
"""
🧮 TASK 1 — Purchase Counter
Topic: lists → loops → dictionary (frequency map)

You have a shopping list: ["apple", "banana", "apple", "orange", "banana", "apple"].
Build a dictionary that counts how many times each item appears and print the result.

"""
# Starter:
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
# TODO: build a frequency dict using a loop; print it
apple_counter = 0
banana_counter = 0
orange_counter = 0
for i in items:
    if i == "apple":
        apple_counter += 1
    if i == "banana":
        banana_counter += 1
    if i == "orange":
        orange_counter += 1
print(f"apple X{apple_counter} banana X{banana_counter} orange X{orange_counter}")