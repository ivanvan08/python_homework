n = input("ввести додатне ціле число n ")
sum = 0
for i in range(1, int(n) + 1):
    val = int(i)
    if val % 3 == 0 or val % 5 == 0:
        sum += val
print(sum)