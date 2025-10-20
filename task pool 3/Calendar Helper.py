year = int(input("input year "))
month = input("input month name ")
month_number = int(input("input month number "))
def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
def days_in_month(month, year):
    months = {"september": 30, "april": 30, "june": 30, "november": 30, "january": 31,
    "march": 31, "may": 31, "july": 31, "august": 31, "october": 31, "december": 31}
    if is_leap(year):
        months["february"] = 29
    else: months["february"] = 28
    return months[month]
def next_month(month_number, year):
    if month_number == 12:
        next_m = 1
    else: next_m = int(month_number)+1
    next_y = year+1
    return next_m, next_y
def month_summary(month, year, month_number):
    return print(f"""month = {month}
days = {days_in_month(month, year)}
is year leap? {is_leap(year)}
next - {next_month(month_number, year)}""")
print(month_summary(month, year, month_number))


