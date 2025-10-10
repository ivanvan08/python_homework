
"""
🚗 TASK 7 — Group Car Colors by Brand
Topic: list of tuples → dict of lists

Cars: [("BMW","black"), ("Audi","red"), ("BMW","white"), ("Audi","blue")]
Build a dictionary where key is the brand and value is a list of colors for that brand.

"""
# Starter:
cars = [("BMW","black"), ("Audi","red"), ("BMW","white"), ("Audi","blue")]
# TODO: build brand -> list_of_colors dict and print it
brand_colors = {}
for element in cars:
    for i in element:
        if i is element[0]:
            a = i
        else: b = i
    brand_colors.update({a: b})
print(brand_colors)