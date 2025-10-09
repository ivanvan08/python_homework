"""
Homework 1:
✈️ Synchronized Arrival: F-16 and Eurofighter Typhoon

📘 Scenario:
Two fighter jets — the F-16 Fighting Falcon and the Eurofighter Typhoon — are flying to the same
destination and must arrive at the exact same time. The F-16 is slower, so it takes off first at 10:00.
Both aircraft fly the same distance, but at different speeds and fuel consumption rates.

All input data in an `INIT DATA` section below is given in imperial units:
Distance: miles
Speed: mph
Fuel consumption: gallons per hour

Your tasks:
0. Read about Python's triple quotes, used for the text - https://realpython.com/ref/glossary/triple-quoted-string/
1. Convert all values from an `INIT DATA` section below into metric units (kilometers, km/h, liters/hour).
2. Calculate the flight time for each aircraft, expressed in full hours and minutes.
   Read about convertion to integer - https://www.w3schools.com/python/ref_func_int.asp
3. Determine the departure time of the Typhoon so it arrives at the same time as the F-16.
4. Calculate how much fuel was used by each aircraft.
5. Print all results in a formatted table.
6. Use input() to enter the distance value from a keyboard - https://www.w3schools.com/python/python_user_input.asp

Formatted table example

----------------------------------------------------------------------------------------------------------
| Aircraft               | Distance (km)  | Speed (km/h)   |  Flight Time  | Departure   | Fuel Used (L) |
----------------------------------------------------------------------------------------------------------
| F-16 Fighting Falcon   |         1932.0 |          929.0 |  2 h  4 min   | 10:00       |       23646.4 |
| Eurofighter Typhoon    |         1932.0 |         1853.1 |  1 h  2 min   | 10:00       |        9088.1 |
----------------------------------------------------------------------------------------------------------


"""

# Conversion constants
MILE_TO_KM = 1.61
GALLON_TO_LITER = 3.79

# INIT DATA
# Distance in miles
distance_miles = 1200

# F-16 data
speed_mph_f16 = 577
fuel_gph_f16 = 3000

# Typhoon data
speed_mph_typhoon = 1151
fuel_gph_typhoon = 2300


# YOUR CODE
# 5
q = input("Введіть вашу дистанцію в милях (якщо бажаєте використати класичну - натисніть Enter): ")
if not q:
    print("Використано звичайну відстань")
else: distance_miles=int(q)




# 1
distance_km = distance_miles*MILE_TO_KM

# F-16 data convert
speed_kph_f16 = speed_mph_f16*MILE_TO_KM
fuel_lph_f16 = fuel_gph_f16*GALLON_TO_LITER

# Typhoon data convert
speed_kph_typhoon = speed_mph_typhoon*MILE_TO_KM
fuel_lph_typhoon = fuel_gph_typhoon*GALLON_TO_LITER
# 2
# flight time for each aircraft

ft_f16_with_fractions = distance_km/speed_kph_f16 # дроби-fractions, не знаю як по іншому позначити
ft_typhoon_with_fractions = distance_km/speed_kph_typhoon

ft_f16_solid = distance_km//speed_kph_f16 # ціле значення
ft_typhoon_solid = distance_km//speed_kph_typhoon

ft_f16_only_fractions = (ft_f16_with_fractions-ft_f16_solid)*60        # в хвилинах    only_fractions=100    only_fractions_хв=60
ft_f16_only_fractions_min = round(ft_f16_only_fractions, 0)       # хотів заокруглити ft_f16_only_fractions до
# звичайних хвилин за допомогою int, але int() can't convert non-string with explicit base.
# Тому загуглив і знайшов функцію round()
ft_f16_time = f"{round(ft_f16_solid)} h {round(ft_f16_only_fractions_min)} min" # хвилини заокруглені до більшого (при 4.5+ буде 5 а не 4). Я вважаю це логічним
ft_f16_normal = ft_f16_solid+(ft_f16_only_fractions_min/100)

ft_typhoon_only_fractions = (ft_typhoon_with_fractions-ft_typhoon_solid)*60
ft_typhoon_only_fractions_min = round(ft_typhoon_only_fractions, 0)
ft_typhoon_time = f"{round(ft_typhoon_solid)} h {round(ft_typhoon_only_fractions_min)} min"
ft_typhoon_normal = ft_typhoon_solid+(ft_typhoon_only_fractions_min/100)

# 3
Departure_time_hours = ft_f16_solid-ft_typhoon_solid
Departure_time_min = ft_f16_only_fractions_min-ft_typhoon_only_fractions_min
Departure_default = 10.00
Departure_f16 = 0
Departure_typhoon = f"+ {round(Departure_time_hours)} h {round(Departure_time_min)} min" # час відправлення trphoon

# 4
#f f/h h
f_u_f16 = fuel_lph_f16*ft_f16_with_fractions
f_u_typhoon = fuel_lph_typhoon*ft_typhoon_with_fractions

# 5
a='-'*106
b="| Aircraft               | Distance (km)  | Speed (km/h)   |  Flight Time  | Departure   | Fuel Used (L) |"
c=f'''| F-16 Fighting Falcon   |         {round(distance_km, 0)} |         {round(speed_kph_f16, 0)}  | {ft_f16_time}     | {Departure_f16}           | {round(f_u_f16, 1)}       |'''
d=f'''| Eurofighter Typhoon    |         {round(distance_km, 0)}|         {round(speed_kph_typhoon, 0)}  | {ft_typhoon_time}     | {Departure_typhoon} | {round(f_u_typhoon, 1)}        |'''

print(a)
print(b)
print(a)
print(c)
print(d)
print(a)