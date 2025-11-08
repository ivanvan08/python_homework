import datetime
def log_sale(order_list, amount):
    order_names = []
    for objkt in order_list:
        order_names.append(objkt["drink"])
    order_names_str = ", ".join(order_names)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{now}] | SALE | {amount:.2f} | {order_names_str}\n"
    with open("sales_log.txt", "a", encoding="utf-8") as file:
        file.write(log_entry)
def load_prices(filename):
    prices = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip().lower()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                name = None
                price = None
                for part in parts:
                    try:
                        value = float(part)
                        if name is not None:
                            price = value
                            break
                    except ValueError:
                        if name is None:
                            name = part
                if name is not None and price is not None:
                    prices[name] = price
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено. Переконайтеся, що він існує.")
    return prices
coffee_recipes = { # рецепти написані за допомогою ШІ, бо мені ліньки шукати скільки в якому напої міліграм й тд.
    "espresso": {
        "ingredients": {
            "coffee": 50
        },
        "price": 0
    },
    "americano": {
        "ingredients": {
            "coffee": 50,
            "water": 100
        },
        "price": 0
    },
    "latte": {
        "ingredients": {
            "coffee": 50,
            "milk": 150
        },
        "price": 0
    },
    "cappuccino": {
        "ingredients": {
            "coffee": 50,
            "milk": 100,
            "milk_foam": 50
        },
        "price": 0
    },
    "flat_white": {
        "ingredients": {
            "coffee": 60,
            "milk": 120
        },
        "price": 0
    },
    "macchiato": {
        "ingredients": {
            "coffee": 50,
            "milk_foam": 10
        },
        "price": 0
    },
    "mochaccino": {
        "ingredients": {
            "coffee": 50,
            "milk": 150,
            "chocolate_syrup": 30
        },
        "price": 0
    },
    "affogato": {
        "ingredients": {
            "coffee": 50,
            "ice_cream": 80
        },
        "price": 0
    },
    "frappe": {
        "ingredients": {
            "instant_coffee": 10,
            "water": 50,
            "milk": 120,
            "ice": 80
        },
        "price": 0
    },
    "cold_brew": {
        "ingredients": {
            "coffee": 60,
            "cold_water": 240
        },
        "price": 0
    },
    "irish_coffee": {
        "ingredients": {
            "coffee": 80,
            "whiskey": 30,
            "cream": 40,
            "sugar": 10
        },
        "price": 0
    },
    "turkish_coffee": {
        "ingredients": {
            "coffee": 50,
            "water": 60,
            "sugar": 10
        },
        "price": 0
    }
}
extra_ingredients = {
    "chocolate_syrup": 10,
    "vanilla_syrup": 10,
    "caramel_syrup": 10,
    "hazelnut_syrup": 10,
    "coconut_syrup": 10,
    "marshmallow": 5,
    "cinnamon": 2,
    "whipped_cream": 20,
    "chocolate_chips": 5
}
def mein():
    global ingredient_prices_dict
    global extra_ingredients_dict
    ingredient_prices_dict = load_prices("ingredient_prices.txt")
    extra_ingredients_dict = load_prices("extra_prices.txt")
    order_list = []
    while True:
        action = hello_and_menu()
        action_clean = action.strip().lower()
        if "exit" in action_clean:
            break
        elif action_clean == "1":
            menu_show()
            while True:
                drink_choice = drink_choose()
                drink_choice_clean = drink_choice.strip().lower()
                if drink_choice_clean == "exit":
                    return
                elif drink_choice_clean == "finish":
                    if len(order_list) == 0:
                        print("Ваше замовлення порожнє, додайте напій!")
                        break
                    total_amount = float(calculate_order(order_list))
                    tips = input(f"ось ціна вашого замовлення {total_amount}, бажаєте залишити чайові? (введіть Так або Ні) ")
                    if tips.lower().strip() == "так":
                        tips_amount = float(input("Введіть кількість чайових в відсотках"))
                        end_amount = total_amount+(total_amount*(tips_amount*0.01))
                    elif tips.lower().strip() == "ні":
                        end_amount = total_amount
                        print("Обов'язково напишіть відгук щоб ми могли стати краще")
                    else: end_amount = total_amount
                    print("Ви закінчили заповнювати замовлення")
                    cash_or_card = input(f"Ось ваше замовлення - {order_list}: {end_amount}грн. Бажаєте оплатити картою чи готівкою? (Введіть Картка або Готівка) ")
                    if cash_or_card.strip().lower() == "готівка":
                        cash_amount = float(input("Введіть внесену вами суму"))
                        remainder = cash_amount-end_amount
                        print(f"Ось ваша решта {remainder:.2f}")
                        log_sale(order_list, end_amount)
                    if cash_or_card.strip().lower() == "картка":
                        print("Дякую за користування нашою кавомашиною")
                        log_sale(order_list, end_amount)
                    break
                elif drink_choice_clean in coffee_recipes:
                    extras = add_extras(drink_choice_clean)
                    if extras == "exit":
                        return
                    order_list.append({"drink": drink_choice_clean, "extras": extras})
                    if extras:
                        print(f"Додано: {drink_choice_clean} + {', '.join(extras)}")
                    else:
                        print("без додатків до замовлення")
                else:
                    print("Спробуйте ще")
        else:
            print("Спробуйте ще")

def price_calculator():
    for drink in coffee_recipes:
        price_per_ingredient = []
        ingredients = coffee_recipes[drink]["ingredients"]
        for ingredient in ingredients:
            price = ingredient_prices_dict.get(ingredient)
            if price is None:
                price = extra_ingredients_dict.get(ingredient, 0)
            price_per_ingredient.append(ingredients[ingredient] * price)
            # print(f"напій {drink} інгредієнт {ingredient} кількість {ingredients[ingredient]} ціна {ingredient_prices_dict.get(ingredient)}")
        total_price = sum(price_per_ingredient)
        coffee_recipes[drink]["price"]=total_price
        # print(coffee_recipes[drink]["price"])
def menu_show():
    price_calculator()
    counter = 0
    print("--- Наше меню ---")
    for drink in coffee_recipes:
        counter += 1
        print(f"{counter}) {drink} — {int(coffee_recipes[drink]["price"])}грн")

def hello_and_menu():
    first_step = input("Вітаю, дякую що вибрали нашу кавомашину. Для перегляду меню введіть 1, для виходу введіть exit ")
    return first_step
def drink_choose():
    while True:
        choose = input("Введіть вибраний вами напій, якщо наша вибірка вам не довподоби - введіть else. Щоб закінчити введіть finish ")
        choose_clean = choose.strip().lower()
        if "exit" in choose_clean:
            return "exit"
        elif "finish" in choose_clean:
            return "finish"
        elif choose_clean == "else":
            print("Цей функціонал ще не додано")
        elif choose_clean in coffee_recipes:
            print(choose_clean, "є в меню")
            return choose_clean
        else:
            print("цього немає в меню, спробуйте ще")
def calculate_order(orderlist):
    total_price = 0
    for item in orderlist:
        drink_name = item["drink"]
        base_price = coffee_recipes[drink_name]["price"]
        total_price += base_price
        extras_list = item["extras"]
        for extra in extras_list:
            price_per_serving = extra_ingredients[extra] * extra_ingredients_dict[extra]
            total_price += price_per_serving
    return total_price
def add_extras(drink_choice_clean):
    available_extras = list(extra_ingredients.keys())
    selected = []
    print(f"\n--- Додаткові інгредієнти для {drink_choice_clean} ---")
    counter = 1
    for extra in available_extras:
        price_per_serving = extra_ingredients[extra] * extra_ingredients_dict[extra]
        print(f"{counter}) {extra} — {price_per_serving:.2f} грн")
        counter += 1
    print("-" * 35)
    while True:
        choice_extras = input("Введіть вибрану вами добавку, або done для продовження без неї: ").strip().lower()
        if choice_extras == "done":
            return selected
        elif choice_extras == "exit":
            return "exit"
        elif choice_extras in extra_ingredients_dict:
            selected.append(choice_extras)
            print(f"Додано {choice_extras}")
        else: print("Невірний ввід. Сробуйде ще або введіть done для виходу")
mein()