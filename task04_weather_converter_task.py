"""
Task 4 — Weather App Converter 🌡️

Requirements:
  - temps_c = [-2, 4, 12, 18, 25]
  - Convert to Fahrenheit using a loop (F = C * 9/5 + 32)
  - Print pairs like "-2°C = 28°F" and store in temps_f list

Practice: list iteration, arithmetic, building new list

OUTPUT EXAMPLE
--------------
-2°C = 28°F
4°C = 39°F
12°C = 54°F
18°C = 64°F
25°C = 77°F

Fahrenheit list: [28, 39, 54, 64, 77]
"""

temps_c = [-2, 4, 12, 18, 25]
print("(Starter) Celsius:", temps_c)
# TODO: loop over temps_c, compute F, print each pair, and append rounded F to temps_f
# F = C * (9/5) + 32
Fahrenheit_list = []
for cel in temps_c:
    fahrenheit = round(cel * (9/5) + 32)
    print(f"{cel}°C = {fahrenheit}°F")
    Fahrenheit_list.append(fahrenheit)
print(f"Fahrenheit list = {Fahrenheit_list}")