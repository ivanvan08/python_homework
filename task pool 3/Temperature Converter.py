income  = [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]
fahrenheit = []
celsius = []
Far = None
C = None
def convert(C, Far, income):
    for C in income:
        Far = C*9/5+32
        fahrenheit.append(Far)
        celsius.append(C)
    return
convert(Far, C, income)
print(f"""Celsius: {celsius}
{"-" * sum(len(str(C))+3 for C in fahrenheit)}
Fahrenheit: {fahrenheit}""")
