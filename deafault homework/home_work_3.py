"""
Advanced Password Quality Meter — Strings Only

GOAL
----
Read a username and a password and classify the password.

INPUT with input() function
-----
Line 1: username
Line 2: password

MANDATORY RULES (all must pass or print EXACTLY "REJECT"):
  R1) length: 10..64 characters inclusive
  R2) contains at least one digit
  R3) contains at least one lowercase letter
  R4) contains at least one uppercase letter
  R5) contains at least one special from:
      ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \\ |
  R6) no spaces or tabs
  R7) must start with a LETTER (A–Z or a–z)
  R8) must NOT contain the username (case-insensitive)
  R9) must NOT contain the reversed username (case-insensitive)
  R10) must NOT contain these weak substrings (case-insensitive):
       "password", "qwerty", "12345", "admin", "god"

CLASSIFICATION (only if all R1..R10 pass):
  Score the following extras (each +1):
    E1) ends with a digit OR a special
    E2) contains BOTH '-' and '_' somewhere
    E3) contains at least one of '@' or '#'
    E4) contains at least two categories among {digit, upper, lower, special} at
        the BEGINNING 4 chars (first four chars contain at least two categories)
  Total extras: 0..4
  LABEL:
    0-1 -> OK
    2-3 -> STRONG
    4   -> ELITE

OUTPUT
------
If any mandatory rule fails: print 
  REJECT

Else print
  RESULT: <OK|STRONG|ELITE> (len=<n>, d=<0/1>, lo=<0/1>, up=<0/1>, sp=<0/1>)

NOTES / HINTS
-------------
- You may use: len, in, not in, strip, lower, upper, replace, startswith/endswith,
  slicing (e.g., s[:4], s[::-1]), comparisons, boolean ops, f-strings.
"""

username = input("Введіть логін")
password = input("Введіть пароль")

# -----------------MANDATORY RULES------------------------
R = 0
# R1
password_len = len(password)
if password_len >= 10 or password_len <= 64:
    R = R+1
else: print(f"REJECT error code R1")
# R2
if any(el.isdigit() for el in password): #el - просто змінна (елемент), щоб через цикл перевіряти чи є цифра в паролі,
    # в нього записується кожен символ змінної і прирівнюється (чи є він цифрою)
    R = R+1
else: print(f"REJECT error code R2")
# R3
if any(el.islower() for el in password):
    R = R+1
else: print(f"REJECT error code R3")
# R4
if any(el.isupper() for el in password):
    R = R+1
else: print(f"REJECT error code R4")
# R5
special =("!@#$%^&*()-_=+[]{};:,.?/\\|")# всюди де теоретично може бути знак \ додам r
if any(el in special for el in password):
    R = R+1
else: print(f"REJECT error code R5")
# R6
if not " " in password:
    R = R+1
else: print(f"REJECT error code R6")
# R7
if password[0:1].istitle() and password[0:1].isalpha():
    R = R+1
else: print(f"REJECT error code R7")
# R8
if not username.lower() in password.lower(): # можна через перевірку в циклі зробити порівняння декількох символів і тоді навіть схований збіг буде задетекчений, але це не необхідно
    R = R+1
else: print(f"REJECT error code R8")
# R9
if not username[::-1].lower() in password.lower():
    R = R+1
else: print(f"REJECT error code R9")
# R10
ban_word_list = {"password", "qwerty", "12345", "admin", "god"}
if any(el in password.lower() for el in ban_word_list):
    R = R+1
else: print(f"REJECT error code R10")
# CLASSIFICATION
print("R =", R)
if R == 10:
    print("you can apply your password")
else:
    print("you need to change your password")
    quit() # вирішив не імпортувати sys
E = 0
# E1
password_last_symbol = slice(password_len-1, password_len)
if password[password_last_symbol].isdigit() or any(el in special for el in password[password_last_symbol]):
    E = E+1
# E2
if "-" in password and "_" in password:
    E = E+1
# E3
if "@" in password or "#" in password:
    E = E+1
# E4
trueness = 0
if any(c.isdigit() for c in password[:4]):
    trueness = trueness+1
if any(c.isupper() for c in password[:4]):
    trueness = trueness + 1
if any(c.islower() for c in password[:4]):
    trueness = trueness + 1
if any(c in special for c in password[:4]):
    trueness = trueness + 1
if trueness >=2:
    E = E+1
# output
if E == 0 or E == 1:
    print("your password is OK")
if E == 2 or E == 3:
    print("your password is STRONG")
if E == 4:
    print("your password is ELITE")