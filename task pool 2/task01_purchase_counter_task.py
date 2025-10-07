
"""
🧮 TASK 1 — Purchase Counter
Topic: lists → loops → dictionary (frequency map)

You have a shopping list: ["apple", "banana", "apple", "orange", "banana", "apple"].
Build a dictionary that counts how many times each item appears and print the result.

"""
# Starter:
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
# TODO: build a frequency dict using a loop; print it
counter = {}
for i in items:
    counter[i] = counter.get(i, 0)+1
print(counter)