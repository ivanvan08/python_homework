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
for drink in coffee_recipes:
    price_per_ingredient = []
    ingredients = coffee_recipes[drink]["ingredients"]
    for ingredient in ingredients:
        price_per_ingredient.append(ingredients[ingredient] * ingredient_prices.get(ingredient))
        print(f"напій {drink} інгридієнт {ingredient} кількість {ingredients[ingredient]} ціна {ingredient_prices.get(ingredient)}")
    total_price = sum(price_per_ingredient)
    coffee_recipes[drink]["price"]=total_price
    print(coffee_recipes[drink]["price"])