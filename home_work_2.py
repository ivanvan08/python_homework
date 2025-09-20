"""
Homework 2:
⛵️ Sailing yacht cruise

📘 Scenario:
You are skippering a small cruising yacht on a short coastal hop between two marinas.
The boat maintains a steady speed through the water (STW), while the tidal stream may help, oppose,
or set at an angle to your course depending on the time. The auxiliary engine (or generator) runs at a
constant burn rate to keep batteries topped up, so fuel use is proportional to passage time.
Your aim is to compare several forecasted current situations, estimate arrival time, or check whether
your fuel plan (with reserve) is adequate for the leg.

Compute for each scenario (A, B1, B2, C):
  • Yacht absolute Speed (km/h) — ground speed magnitude
  • Time (h) or Time (H:MM) to target
  • Distance in km
  • Fuel (L) — constant burn rate [L/h]


OUTPUT EXAMPLE:
+-----------+----------------+------------------+--------------------+--------------+------------+------------+
| Scenario  |  Distance (km) |   Current (km/h) |   Current (km/h)   |     Time (h) |  Time H:MM |   Fuel (L) |
+-----------+----------------+------------------+--------------------+--------------+------------+------------+
| A         |          22.96 |             0.00 |              11.48 |        2.000 | 02:00      |       4.80 |
| B1        |          22.96 |            -1.48 |              10.00 |        2.296 | 02:18      |       5.51 |
| B2        |          22.96 |             2.22 |              13.70 |        1.676 | 01:41      |       4.02 |
| C         |          22.96 |     2.41 (30.0°) |              13.62 |        1.686 | 01:41      |       4.05 |
+-----------+----------------+------------------+--------------------+--------------+------------+------------+
Input data:
- distance in nm (nautical miles)
- yacht speed in knots (speed through water, STW)
- current in knots
- current angle in degrees (for Scenario C)
- fuel consumption in liters per hour

Scenario A — simplest case: no current at all.
Scenario B1, B2 — alternative inputs for comparison (1D current helps/opposes).
Scenario C — current at angle β to the course:
  - β measured from ship’s course:
    β=0° tail (helps), β=180° head (opposes), 90° pure cross-current.
  - Decomposition (knots):
      current_along = current_mag * cos(β)
      current_across = current_mag * sin(β)
  - Vector sum (knots):
      gx = STW + current_along
      gy = current_across
      speed over ground (SOG) = hypot(gx, gy)
  - Use math.radians for degrees → radians.
  - For H:MM: convert hours → minutes, round, split; carry if minutes == 60.
"""

import math

# ---------------- Constants ----------------
NM_TO_KM = 1.852 # from Google
KTS_TO_KMH = NM_TO_KM # same
# ---------------- Input ----------------

distance_nm_i = input("distance in nm (nautical miles, no more than 9999)")
stw_kt_i = input("yacht speed in knots (speed through water, STW, no more than 999)")
current_kt_i = input("current in knots (no more than 99)")
angle_degrees_yacht = input("current angle in degrees (for Scenario C), 360 - max")
burn_lph_i = input("fuel consumption in liters per hour (no more than 9999)")
index_1 = 0 # задаю зачення індексу кожної змінної бо якщо його не буде при використанні звичайної відстані буде помилка
index_2 = 0
index_3 = 0
index_4 = 0
index_5 = 0
if not distance_nm_i:
    print("Використано звичайну відстань")
else:
    print("задано ввідні данні")
    index_1 = 1



if not stw_kt_i:
    print("Використано звичайну швидкість")
else:
    print("задано ввідні данні")
    index_2 = 1

if not current_kt_i:
    print("Використано звичайну швидкість потоку")
else:
    print("задано ввідні данні")
    index_3 = 1

if not burn_lph_i:
    print("Використано звичайну швидкість спалення топлива")
else:
    print("задано ввідні данні")
    index_4 = 1

# =========================
# Scenario A — no current
# =========================
distance_nm = 12.4
if index_1 == 1:
    distance_nm = float(distance_nm_i)
distance_km = distance_nm*NM_TO_KM

stw_kt = 6.2
if index_2 == 1:
    stw_kt = float(stw_kt_i)


stw_km = stw_kt*KTS_TO_KMH


current_kt = 0.0  # no current per description
if index_3 == 1:
    current_kt = float(current_kt_i)
current_km = current_kt*KTS_TO_KMH

burn_lph = 2.4
if index_4 == 1:
    burn_lph = float(burn_lph_i)

if current_km >= 0: # для наочності
    Abs_speed_A = stw_km+current_km
    print("Current for scenario A - upstream")
elif current_km < 0:
    Abs_speed_A = stw_km+current_km
    print("Current for scenario A - adrift")


time_A = distance_km/Abs_speed_A
if time_A > 9999.99:   # технічна межа, вимушено через зїзд таблички
        print("Занадто великий час, обмежую до 9999")
        time_A = 9999
time_A_hours = int(time_A)
time_A_min = (time_A-time_A_hours)*60 # отримав дріб, перевів в хвилини

if time_A_min == 60: # про всяк випадок
    time_A_hours += 1
    time_A_min = 0


Fuel_A = time_A*burn_lph


# =========================
# Scenario B1 — opposing current
# =========================
distance_km_B1 = distance_km
stw_km_B1 = stw_km
current_km_B1 = -0.8*KTS_TO_KMH
burn_lph_B1 = burn_lph

if current_km >= 0: # для наочності
    Abs_speed_B1 = stw_km+current_km_B1
    print("Current for scenario B1 - upstream")
elif current_km < 0:
    Abs_speed_B1 = stw_km+current_km_B1
    print("Current for scenario B1 - adrift")


time_B1 = distance_km_B1/Abs_speed_B1
if time_B1 > 9999.99:   # технічна межа
        print("Занадто великий час, обмежую до 9999")
        time_B1 = 9999
time_B1_hours = int(time_B1)
time_B1_min = (time_B1-time_B1_hours)*60 # отримав дріб, перевів в хвилини

if time_B1_min == 60:
    time_B1_hours += 1
    time_B1_min = 0


Fuel_B1 = time_B1*burn_lph
# =========================
# Scenario B2 — helping current
# =========================
distance_km_B2 = distance_km
stw_km_B2 = stw_km
current_km_B2 = +1.2*KTS_TO_KMH
burn_lph_B2 = burn_lph

if current_km >= 0: # для наочності
    Abs_speed_B2 = stw_km+current_km_B2
    print("Current for scenario B2 - upstream")
elif current_km < 0:
    Abs_speed_B2 = stw_km+current_km_B2
    print("Current for scenario B2 - adrift")

time_B2 = distance_km_B2/Abs_speed_B2
if time_B2 > 9999.99:   # технічна межа
        print("Занадто великий час, обмежую до 9999")
        time_B2 = 9999
time_B2_hours = int(time_B2)
time_B2_min = (time_B2-time_B2_hours)*60 # отримав дріб, перевів в хвилини

if time_B2_min == 60:
    time_B2_hours += 1
    time_B2_min = 0


Fuel_B2 = time_B2*burn_lph
# ============================================
# Scenario C — angled current (2D vector sum)
# ============================================
distance_km_C = distance_km
stw_km_C = stw_km
current_mag_km_C = 1.3*KTS_TO_KMH  # magnitude (knots), >= 0
print("Current for scenario C - allways upstream")

burn_lph_C = burn_lph
if not angle_degrees_yacht:
    angle_deg_C = 30.0  # angle between current direction or course
else: angle_deg_C = angle_degrees_yacht

angle_deg_C_rad = math.radians(float(angle_deg_C))
current_along = current_mag_km_C * math.cos(angle_deg_C_rad)
current_across = current_mag_km_C * math.sin(angle_deg_C_rad)

gx = stw_km_C + current_along
gy = current_across
Speed_over_ground = math.hypot(gx, gy)

time_C = distance_km_C/Speed_over_ground
if time_C > 9999.99:   # технічна межа
        print("Занадто великий час, обмежую до 9999")
        time_C = 9999
time_C_hours = int(time_C)
time_C_min = (time_C-time_C_hours)*60 # отримав дріб, перевів в хвилини

if time_C_min == 60:
    time_C_hours += 1
    time_C_min = 0

Fuel_C = time_C*burn_lph
# -------------type length----------------
scenario_len = len("| Scenario  ") + 1

# довжинни верхнього рядку таблиці
distance_max = max(
    len(f"{distance_km:.2f}"),
    len(f"{distance_km_B1:.2f}"),
    len(f"{distance_km_B2:.2f}"),
    len(f"{distance_km_C:.2f}"),
    len("|  Distance (km) ")
)
distance_max_1 = int(distance_max + 1) # переведення довжини в чисельне значення

# first current
current_max = max(
    len(f"{current_km:.2f}"),
    len(f"{current_km_B1:.2f}"),
    len(f"{current_km_B2:.2f}"),
    len(f"{current_mag_km_C:.2f}"),
    len("|   Current (km/h)   ")
)
current_max_1 = int(current_max + 1)

# second current
# зберігаємо ім'я stw_check, але обчислюємо через len форматованих рядків
stw_check = max(
    len(f"{stw_km:.2f}"),
    len(f"{stw_km_B1:.2f}"),
    len(f"{stw_km_B2:.2f}"),
    len(f"{stw_km_C:.2f}"),
    len("|   Current (km/h) ")
)
stw_max = stw_check
stw_max_1 = int(stw_max + 1)

time_max = max(
    len(f"{time_A:.3f}"),
    len(f"{time_B1:.3f}"),
    len(f"{time_B2:.3f}"),
    len(f"{time_C:.3f}"),
    len("|     Time (h) ")
)
time_max_1 = time_max + 1

time_HM_max = None
# Time H:MM — формуємо реальні рядки H:MM та вимірюємо їх довжину. Def був зроблений за допомогою GPT,
# я заплутався в моменті як проставили return і він мені допоміг
def hm_str(hours, minutes):
    m = int(round(minutes))
    if m == 60:
        hours = int(hours) + 1
        m = 0
    return f"{int(hours):02d}:{m:02d}"

hmA = hm_str(time_A_hours, time_A_min)
hmB1 = hm_str(time_B1_hours, time_B1_min)
hmB2 = hm_str(time_B2_hours, time_B2_min)
hmC = hm_str(time_C_hours, time_C_min)
time_HM_max = max(len(hmA), len(hmB1), len(hmB2), len(hmC), len("|  Time H:MM "))
time_HM_max_1 = int(time_HM_max) + 2 # + ще 1 бо є знак ":" (HM) розділяючий години та хвилини

# Fuel column
Fuel_max = max(
    len(f"{Fuel_A:.2f}"),
    len(f"{Fuel_B1:.2f}"),
    len(f"{Fuel_B2:.2f}"),
    len(f"{Fuel_C:.2f}"),
    len("|   Fuel (L) |")
)
Fuel_max_1 = int(Fuel_max + 1)
# ---------------------------
# Table output (no loops)
# ---------------------------

# Буду використовувати len() для надання таблиці презентабельного вигляду
frame = 1
print(f"""+{'-' * scenario_len}+{'-' * distance_max_1}+{'-' * current_max_1}+{'-' * stw_max_1}+{'-' * time_max_1}+{'-' * time_HM_max_1}+{'-' * Fuel_max_1}+""")
print(
    f"| {'Scenario':^{scenario_len-2}}  " # all in default, but -2 cause i puted spaces by my own
    f"|  {'Distance (km)':^{distance_max_1-2}} "
    f"|   {'Current (km/h)':^{current_max_1-2}} "
    f"|   {'Current (km/h)':^{stw_max_1-2}}   "
    f"|     {'Time (h)':^{time_max_1-2}} "
    f"|  {'Time H:MM':^{time_HM_max_1-2}} "
    f"|   {'Fuel (L)':^{Fuel_max_1-2}} |"
)