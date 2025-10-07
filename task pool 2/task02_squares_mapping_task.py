
"""
🔢 TASK 2 — Squares Mapping
Topic: loops → build dictionary

Given a list of numbers [1, 2, 3, 4, 5],
create a dictionary where key is the number and value is its square.

"""
# Starter:
nums = [1, 2, 3, 4, 5]
# TODO: create dict of squares; print it

square_dict = {num: num**2 for num in nums}
print(square_dict)