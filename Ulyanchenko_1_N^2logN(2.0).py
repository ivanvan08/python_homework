import random

n = int(input("Введіть кількість цілих чисел "))

solution_dict = dict.fromkeys(range(n))

negative_n = int(n)*(-1)
numbers_data = random.sample(range(negative_n, n+1), n*2)
count = 0
for i in range(0, n*2):
    for j in range(i+1, n*2):
        if numbers_data[i] + numbers_data[j] == 0:
            count += 1
print(count)