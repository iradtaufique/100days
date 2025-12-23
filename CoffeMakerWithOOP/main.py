from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    user_choice = input(f"What would you like? (espresso/latte/cappuccino/):").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
    else:

        if coffee_maker.is_resource_sufficient(user_choice):
            print("Pass")


