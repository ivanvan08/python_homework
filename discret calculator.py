# Калькулятор завдань за номером варіанту

# Введення номера варіанту
k = int(input("Введіть номер варіанту (1–100): "))

# Розрахунки для кожного рівня
i1 = k % 23
i2 = (k + 12) % 23
ii1 = k % 9
ii2 = (k + 5) % 9
iii = k % 7
iv = k % 4

# Якщо залишок 0 — це останнє завдання рівня
def format_task(value, level_max):
    return f"{value} (остання задача)" if value == 0 else str(value)

# Вивід результатів
print("\nРезультати:")
print(f"I рівень: {format_task(i1, 23)}, {format_task(i2, 23)}")
print(f"II рівень: {format_task(ii1, 9)}, {format_task(ii2, 9)}")
print(f"III рівень: {format_task(iii, 7)}")
print(f"IV рівень: {format_task(iv, 4)}")
