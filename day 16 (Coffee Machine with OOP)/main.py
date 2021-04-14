from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menushka = Menu()
money = MoneyMachine()


def machine_in_operation():
    off = False

    while not off:
        options = menushka.get_items()
        user_input = input(f"What would you like to drink today? ({options}): ")
        try:
            if user_input == "off":
                off = True
            elif user_input == "report":
                coffee_machine.report()
                money.report()
            else:
                drink = menushka.find_drink(user_input)
                is_enough_resources = coffee_machine.is_resource_sufficient(drink)
                is_money_good = money.make_payment(drink.cost)
                if is_enough_resources and is_money_good:
                    coffee_machine.make_coffee(drink)
        except:
            print("ERROR! Try again")


machine_in_operation()
