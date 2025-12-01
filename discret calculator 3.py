def fix_zero(value, modulus):
    """Якщо остача 0 — повертаємо останній номер (тобто modulus)."""
    return modulus if value == 0 else value


def calc_levels(k: int):
    lvl1_a = fix_zero(k % 37, 37)
    lvl1_b = fix_zero((k + 19) % 37, 37)

    lvl2_a = fix_zero(k % 17, 17)
    lvl2_b = fix_zero((k + 9) % 17, 17)

    lvl3_a = fix_zero(k % 11, 11)
    lvl3_b = fix_zero((k + 6) % 11, 11)

    lvl4 = fix_zero(k % 6, 6)

    result = {
        "Nivel 1": {
            "k mod 37": lvl1_a,
            "(k + 19) mod 37": lvl1_b
        },
        "Nivel 2": {
            "k mod 17": lvl2_a,
            "(k + 9) mod 17": lvl2_b
        },
        "Nivel 3": {
            "k mod 11": lvl3_a,
            "(k + 6) mod 11": lvl3_b
        },
        "Nivel 4": {
            "k mod 6": lvl4
        }
    }
    return result


# Приклад використання
variant = int(input("Введіть номер варіанту k: "))
output = calc_levels(variant)

for nivel, values in output.items():
    print(nivel + ":")
    for name, val in values.items():
        print(f"  {name} = {val}")
