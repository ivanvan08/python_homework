# Введення номеру варіанту
k = int(input("Введіть номер варіанту (k): "))

# Розрахунок залишків згідно з фото
val1 = k % 11
val2 = k % 8
val3 = k % 12
val4 = k % 6
val5 = k % 5

# Функція обробки результату
# Якщо залишок 0 -> повертаємо саме число модуля (наприклад, 11 замість 0)
def get_task(value, modulus):
    if value == 0:
        return modulus
    return value

print("\nВаші завдання:")
print(f"1. (k mod 11): Завдання № {get_task(val1, 11)}")
print(f"2. (k mod 8):  Завдання № {get_task(val2, 8)}")
print(f"3. (k mod 12): Завдання № {get_task(val3, 12)}")
print(f"4. (k mod 6):  Завдання № {get_task(val4, 6)}")
print(f"5. (k mod 5):  Завдання № {get_task(val5, 5)}")