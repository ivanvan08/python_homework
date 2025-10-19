income  = [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]
fahrenheit = []
celsius = []
for C in income:
    F = C*9/5+32
    fahrenheit.append(F)
    celsius.append(C)
print(f"""Celsius: {celsius}
{"-" * sum(len(str(C))+3 for C in fahrenheit)}
Fahrenheit: {fahrenheit}""")
