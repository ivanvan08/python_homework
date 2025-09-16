"""
Homework 2:
⛵️ Sailing yacht cruise

📘 Scenario:
You are skippering a small cruising yacht on a short coastal hop between two marinas.
The boat maintains a steady speed through the water (STW), while the tidal stream may help, oppose,
or set at an angle to your course depending on the time. The auxiliary engine (or generator) runs at a
constant burn rate to keep batteries topped up, so fuel use is proportional to passage time.
Your aim is to compare several forecasted current situations, estimate arrival time, and check whether
your fuel plan (with reserve) is adequate for the leg.

Compute for each scenario (A, B1, B2, C):
  • Yacht absolute Speed (km/h) — ground speed magnitude
  • Time (h) and Time (H:MM) to target
  • Distance in km
  • Fuel (L) — constant burn rate [L/h]


OUTPUT EXAMPLE:
+-----------+----------------+------------------+--------------------+--------------+------------+------------+
| Scenario  |  Distance (km) |   Current (km/h) |   Current (km/h) |     Time (h) |  Time H:MM |   Fuel (L) |
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

distance_nm_i = input("distance in nm (nautical miles)")
stw_kt_i = input("yacht speed in knots (speed through water, STW)")
current_kt_i = input("current in knots")
angle_degrees_yacht_i = input("current angle in degrees (for Scenario C)")
burn_lph_i = input("fuel consumption in liters per hour")
if not distance_nm_i and stw_kt_i and current_kt_i and angle_degrees_yacht_i and burn_lph_i:
    print("Використано звичайну відстань")
else:
    print("задано ввідні данні")
    distance_nm = distance_nm_i
    stw_kt = stw_kt_i
    current_kt = current_kt_i
    angle_degrees_yacht = angle_degrees_yacht_i
    burn_lph = burn_lph_i

# =========================
# Scenario A — no current
# =========================
distance_nm = 12.4
distance_km = distance_nm*NM_TO_KM

stw_kt = 6.2
stw_km = stw_kt*KTS_TO_KMH


current_kt = 0.0  # no current per description
current_km = current_kt*KTS_TO_KMH

burn_lph = 2.4

if current_km >= 0: # для наочності
    Abs_speed_A = stw_km+current_km
    print("Current for scenario A - upstream")
elif current_km < 0:
    Abs_speed_A = stw_km+current_km
    print("Current for scenario A - adrift")


time_A = distance_km/Abs_speed_A
time_A_hours = round(time_A)
time_A_min = (time_A-time_A_hours)*60 # отримав дріб, перевів в хвилини

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
time_B1_hours = round(time_B1)
time_B1_min = (time_B1-time_B1_hours)*60 # отримав дріб, перевів в хвилини

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
time_B2_hours = round(time_B2)
time_B2_min = (time_B2-time_B2_hours)*60 # отримав дріб, перевів в хвилини

Fuel_B2 = time_B1*burn_lph
# ============================================
# Scenario C — angled current (2D vector sum)
# ============================================
distance_km_C = distance_km
stw_km_C = stw_km
current_mag_km_C = 1.3*KTS_TO_KMH  # magnitude (knots), >= 0
print("Current for scenario C - allways upstream")

burn_lph_C = burn_lph
if not angle_degrees_yacht:
    angle_deg_C = 30.0  # angle between current direction and course
else: angle_deg_C = angle_degrees_yacht

angle_deg_C_rad = math.radians(float(angle_deg_C))
current_along = current_mag_km_C * math.cos(angle_deg_C_rad)
current_across = current_mag_km_C * math.sin(angle_deg_C_rad)

gx = stw_km_C + current_along
gy = current_across
Speed_over_ground = math.hypot(gx, gy)

time_C = distance_km_C/Speed_over_ground
time_C_hours = round(time_C)
time_C_min = (time_C-time_C_hours)*60 # отримав дріб, перевів в хвилини

Fuel_C = time_C*burn_lph
# -------------type length----------------
distance_len = len("|  Distance (km) ")
distance_max = len(str((max(distance_km, distance_km_B1, distance_km_B2, distance_km_C))))
distance_max_1 = int(distance_max)
# не знайшов цієї функції в книзі,
# пробував методом перебору через math. - але не було. з типом float не працювало,
# поміняв на str (все одно потрібна довжина)

# ---------------------------
# Table output (no loops)
# ---------------------------

# Буду використовувати len() для надання таблиці презентабельного вигляду
print(f"""{distance_max_1} {distance_km}""")