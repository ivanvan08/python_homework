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
ingredient_prices = {
    "coffee": 0.6,
    "water": 0.05,
    "cold_water": 0.05,
    "milk": 0.3,
    "milk_foam": 0.35,
    "instant_coffee": 0.5,
    "chocolate_syrup": 0.8,
    "ice_cream": 1.2,
    "ice": 0.1,
    "whiskey": 2.5,
    "cream": 0.9,
    "sugar": 0.15,
    "vanilla_syrup": 0.5,
    "caramel_syrup": 0.6,
    "hazelnut_syrup": 0.7,
    "coconut_syrup": 0.75,
    "marshmallow": 0.7,
    "cinnamon": 0.2,
    "whipped_cream": 1.0,
    "chocolate_chips": 0.8
}
extra_ingredients = {
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
                    total_amount = round(calculate_order(order_list))
                    print("Ви закінчили заповнювати замовлення")
                    cash_or_card = input(f"Ось ваше замовлення - {order_list}: {total_amount}грн. Бажаєте оплатити картою чи готівкою? (Введіть Картка або Готівка)")
                    if cash_or_card.strip().lower() == "Готівка":
                        cash_amount = int(input("Введіть внесену вами суму"))
                        remainder = cash_amount-total_amount
                        print("Ось ваша решта", remainder)
                    if cash_or_card.strip().lower() == "Картка":
                        print("Дякую за користування нашою кавомашиною")
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
            price_per_ingredient.append(ingredients[ingredient] * ingredient_prices.get(ingredient))
            # print(f"напій {drink} інгредієнт {ingredient} кількість {ingredients[ingredient]} ціна {ingredient_prices.get(ingredient)}")
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
            price_per_serving = extra_ingredients[extra] * ingredient_prices[extra]
            total_price += price_per_serving
    return total_price
def add_extras(drink_choice_clean):
    available_extras = list(extra_ingredients.keys())
    selected = []
    print(f"\n--- Додаткові інгредієнти для {drink_choice_clean} ---")
    counter = 1
    for extra in available_extras:
        price_per_serving = extra_ingredients[extra] * ingredient_prices[extra]
        print(f"{counter}) {extra} — {price_per_serving:.2f} грн")
        counter += 1
    print("-" * 35)
    while True:
        choice_exstras = input("Введіть вибрану вами добавку, або done для продовження без неї: ").strip().lower()
        if choice_exstras == "done":
            return selected
        elif choice_exstras == "exit":
            return "exit"
        elif choice_exstras in extra_ingredients:
            selected.append(choice_exstras)
            print(f"Додано {choice_exstras}")
        else: print("Невірний ввід. Сробуйде ще або введіть done для виходу")
mein()
