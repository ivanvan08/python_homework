"""
Task 9 — Music Festival Ticket Analyzer (No dicts, No functions) 🎤

Constraints: lists + loops + conditions + strings + numbers only (NO dicts, NO def).

Scenario:
  Entrance logs are noisy strings with three data points:
    - Ticket ID starting with 'T' + digits (e.g., T123)
    - Age (e.g., age=21, AGE:17)
    - Zone name containing 'zone' (zoneA, ZONE_B, ZONE_C)

Example logs:
  logs = [
    "id:T123 age=21 zoneA",
    "noise T045 AGE=17 ZONE_B",
    "ticket T222 age:35 zoneA",
    "id:T045 age=17 zoneB (duplicate)",
    "bad line missing fields",
    "T555 age=12 ZONE_C",
  ]

Requirements:
  1) Extract for each line:
     - ticket id (string starting with 'T' + digits)
     - age (int)
     - zone label ('A', 'B', 'C') derived from zone token (case-insensitive)
     Ignore lines missing any of these three fields.

  2) Compute and print:
     - Valid tickets count
     - Minors (<18) count
     - Average age (1 decimal)
     - Zone counts as: A=?, B=?, C=?
     - Duplicates list (IDs that appear more than once)

Practice: string normalization, token scanning, counters, averages, duplicate detection

OUTPUT EXAMPLE
--------------
Valid tickets: 5
Minors: 2
Average age: 21.2
Zone counts: A=2, B=2, C=1
Duplicates: T045
"""

import re

logs = [
    "id:T123 age=21 zoneA",
    "noise T045 AGE=17 ZONE_B",
    "ticket T222 age:35 zoneA",
    "id:T045 age=17 zoneB (duplicate)",
    "bad line missing fields",
    "T555 age=12 ZONE_C",
]

print("(Starter) Logs loaded:", len(logs))
# TODO: parse each line, extract id/age/zone using loops over tokens
# TODO: compute metrics with lists and counters only (no dicts, no def)
id = []
id_dup = []
age = []
zone = []
zone_count_a = 0
zone_count_b = 0
zone_count_c = 0
for line in logs:
    if re.findall(r"T\d+", line.upper()) != []: #з цифрами (\d) + - одна або більше цифра
        if re.findall(r"T\d+", line.upper()) in id:
            id_dup.append(re.findall(r"T\d+", line.upper()))
        id.append(re.findall(r"T\d+", line.upper()))


    if re.findall(r"age\D*(\d+)", line.lower()) != []: # \D* 0 або більше не цифр, але їх ігноруємо, бо беремо тільки кортеж
        age.append(re.findall(r"age\D*(\d+)", line.lower()))


    if re.findall(r"zone\D*(\w+)", line.lower()) != []:  # \D* 0 або більше не цифр, але їх ігноруємо, бо беремо тільки кортеж
        zone.append(re.findall(r"zone\D*(\w+)", line.lower())) # 4 стрічку видає як e, ймовірніше всього через те що [['b']] інтерпретується як ['е'] по ASCII

Valid_tickets = len(id)

Minors = 0
for i in age:
    if int(i[0]) < 18:
        Minors += 1

avarage = 0

for i in age:
    avarage += int(i[0])

for i in zone:
    if 'a' in i:
        zone_count_a += 1
    elif 'b' in i:
        zone_count_b += 1
    elif 'c' in i:
        zone_count_c += 1

print(id)
print(age)
print(zone)

print(f"""{"-"*35}
Valid tickets: {Valid_tickets}
Minors: {Minors}
Average age: {avarage/len(age)}
Zone counts: A={zone_count_a}, B={zone_count_b}, C={zone_count_c}
Duplicates: {id_dup}
{"-"*35}""")
