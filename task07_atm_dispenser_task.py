"""
Task 7 — ATM Cash Dispenser 🔢

Requirements:
  - bills = [100, 50, 20, 10]
  - For amount = 180, calculate greedy breakdown
  - Print like: "1x100, 1x50, 1x20, 1x10"
  - If not divisible by 10, print an error message

Practice: loops, integer division, modulo, conditional handling

OUTPUT EXAMPLE
--------------
1x100, 1x50, 1x20, 1x10
"""

amount = input("input your amount")
if amount == "":
    amount = 180
bills = [100, 50, 20, 10]
print(f"(Starter) Amount: {amount}, Bills: {bills}")
# TODO: implement greedy breakdown and print result (or error if remainder)
if type(int(amount)/10) != int:
    print("error, your amount not divisible by 10")
    quit()
hundred = 0
fifty = 0
twent = 0
ten = 0
if amount < bills[-1]: print("Your amount is less than", bills[-1])
while amount >= bills[0]:
    hundred = hundred+1
    amount = amount-bills[0]
while amount >= bills[1]:
    fifty = fifty+1
    amount = amount-bills[1]
while amount >= bills[2]:
    twent = twent+1
    amount = amount-bills[2]
while amount >= bills[3]:
    ten = ten+1
    amount = amount-bills[3]

print(f"{hundred}x100 {fifty}x50 {twent}x20 {ten}x10")
