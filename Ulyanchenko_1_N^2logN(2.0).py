import random

n = int(input("Введіть кількість цілих чисел "))

solution_dict = dict.fromkeys(range(n))

negative_n = int(n)*(-1)
numbers_data = random.sample(range(negative_n, n+1), n*2)
numbers_data.sort()

def binary_search(numbers, target, low):
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

count = 0
for i in range(0, n*2):
    for j in range(i+1, n*2):
        if i > 0 and numbers_data[i] == numbers_data[i - 1]:
            continue
        c = -(numbers_data[i] + numbers_data[j])
        if binary_search(numbers_data, c, j + 1):
            count += 1
print(count)