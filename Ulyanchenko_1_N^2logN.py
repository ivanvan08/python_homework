import random

n = int(input("Введіть кількість цілих чисел "))

solution_dict = dict.fromkeys(range(n))

negative_n = int(n)*(-1)
numbers_data = random.sample(range(negative_n, n+1), n*2)
# print(numbers_data)
