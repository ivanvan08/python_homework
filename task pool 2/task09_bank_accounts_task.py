
"""
🏦 TASK 9 — Bank Accounts Update
Topic: dict state update from a list of transactions

Accounts: {"Alex": 1000, "Bob": 500, "Cara": 200}
Transactions: [("Alex",-200), ("Bob",+300), ("Alex",+100), ("Cara",-50), ("Dan",+40)]
Apply transactions (add deltas). If name not in accounts, create with starting balance 0 before applying.
Finally, print balances sorted by name.

"""
from tkinter.font import names

# Starter:
accounts = {"Alex": 1000, "Bob": 500, "Cara": 200}
tx = [("Alex",-200), ("Bob",+300), ("Alex",+100), ("Cara",-50), ("Dan",+40), ("VAN",+21341234123)]
# TODO: apply tx to accounts; then print sorted balances
for user in tx:
    for obj in user:
        if type(obj) is str:
            if not obj in accounts:
                print()
                accounts.update({obj: user[1]})
            if not obj in accounts:
                accounts.update({obj: accounts[obj]+user[1]})
        elif type(obj) is int:
            break
        else:
            print("non valid object")
            tx.pop()
            break
print(sorted(accounts.items(), key=lambda item: item[0]))