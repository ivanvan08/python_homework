import random

n = int(input("Введіть кількість цілих чисел "))

solution_dict = dict.fromkeys(range(n))

negative_n = int(n)*(-1)
numbers_data = random.sample(range(negative_n, n+1), n*2)
count = None
numbers_data.sort()
for i in range(0, n*2):
    for j in range(0, n*2):
        if i > 0 and numbers_data[i] == numbers_data[i - 1]:
            continue
        c = -(numbers_data[i] + numbers_data[j])
        if numbers_data[i] + numbers_data[j] + c == 0:
            count += 1
print(count)