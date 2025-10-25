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
    "sugar": 0.15
}
def mein():
    while True:
        action = hello_and_menu()
        action_clean = action.strip().lower()
        if "exit" in action_clean:
            break
        elif action.strip().lower() == "1":
            menu_show()
            drink_choice = drink_choose()
            if drink_choice.strip().lower() == "exit":
                break
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
        choose = input("Введіть вибраний вами напій, якщо наша вибірка вам не довподоби - введіть else ")
        choose_clean = choose.strip().lower()
        if "exit" in choose_clean:
            return "exit"
        elif choose_clean in coffee_recipes:
            print(choose_clean, "є в меню")
            return choose_clean
        else:
            print("цього немає в меню, спробуйте ще")
mein()
