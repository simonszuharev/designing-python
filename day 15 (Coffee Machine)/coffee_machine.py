"""MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}"""


def latte(user_money):
    if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24

        if user_money >= 2.5:
            user_money -= 2.5
            print("Your latte is ready!")
            print("Your change is $", round(user_money, 2))
            return user_money
        else:
            print("Not enough money!!!!!")
            print("The whole amount of $", user_money, " is refunded.")
            return user_money
    else:
        if resources["water"] < 200:
            print("Not enough water to make your latte :( ")
        elif resources["milk"] < 150:
            print("Not enough milk to make your latte :( ")
        elif resources["coffee"] < 24:
            print("Not enough coffee to make your latte :( ")

        return resources


def cappuccino(user_money):
    if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24

        if user_money >= 3:
            user_money -= 3
            print("Your cappuccino is ready!")
            print("Your change is $", round(user_money, 2))
            return user_money
        else:
            print("Not enough money!!!!!")
            print("The whole amount of $", user_money, " is refunded.")
            return user_money
    else:
        if resources["water"] < 250:
            print("Not enough water to make your latte :( ")
        elif resources["milk"] < 100:
            print("Not enough milk to make your latte :( ")
        elif resources["coffee"] < 24:
            print("Not enough coffee to make your latte :( ")
        return resources


def espresso(user_money):
    if resources["water"] >= 50 and resources["coffee"] >= 18:
        resources["water"] -= 50
        resources["coffee"] -= 18
        print("Your espresso is ready!")

        if user_money >= 1.5:
            user_money -= 1.5
            print("Your espresso is ready!")
            print("Your change is $", round(user_money, 2))
            return user_money
        else:
            print("Not enough money!!!!!")
            print("The whole amount of $", user_money, " is refunded.")
            return user_money
    else:
        if resources["water"] < 50:
            print("Not enough water to make your latte :( ")
        elif resources["coffee"] < 18:
            print("Not enough coffee to make your latte :( ")
        return resources


def get_sum(user_quarter, user_dime, user_nickel, user_penny):
    return user_quarter + user_dime + user_nickel + user_penny


def get_change(cost, user_money):
    user_money -= cost
    return user_money


def report():
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])


def coffee_machine():
    off = False
    print("Welcome to the Coffee Machine")
    while not off:

        user_input = str(input("What would you like? (espresso/latte/cappuccino): "))
        if user_input != "report" and user_input != "off":
            user_quarter = int(input("Insert quarters: ")) * .25
            user_dime = int(input("Insert dimes: ")) * .1
            user_nickel = int(input("Insert nickels: ")) * .05
            user_pennies = int(input("Insert pennies: ")) * .01
            user_money = get_sum(user_quarter, user_dime, user_nickel, user_pennies)

            if user_input.lower() == "espresso":
                user_money = espresso(user_money)
            elif user_input.lower() == "latte":
                user_money = latte(user_money)
            elif user_input.lower() == "cappuccino":
                user_money = cappuccino(user_money)
            else:
                print("Type in something valid. Let's try again!")
        elif user_input.lower() == "report":
            report()
        elif user_input.lower() == "off":
            print("Good bye!")
            off = True


coffee_machine()
