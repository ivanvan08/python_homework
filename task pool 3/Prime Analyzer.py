import math
first = input("input fist number of range")
second = input("input last number in your range")
primes = []
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return True
    dil = 3
    while dil <= math.sqrt(n):
        if n%dil == 0:
            return False
        dil += 2
    return True
for n in range(int(first), int(second)+1):
    if is_prime(n):
        primes.append(n)
counter = len(primes)
gaps = []
for i in range(len(primes) - 1):
    gap = primes[i + 1] - primes[i]
    gaps.append(gap)
if len(gaps) > 0:
    avg_gap = sum(gaps) / len(gaps)
else:
    avg_gap = 0
print(f"""Range:{first}-{second}
Primes: {primes}
Count: {counter}
Average gap: {avg_gap}""")