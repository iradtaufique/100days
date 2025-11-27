from data import resources, MENU

profit = 0

def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def is_transaction_successful(user_coins, drink_cost):
    if user_coins < drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink['cost']
        change = payment - drink['cost']
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True


def is_enough_coins():
    print('Insert Coins')
    total = int(input(f"How many Quarters: ")) * 0.25
    total += int( input(f"How many Cent: ")) * 0.10
    total += int( input(f"How many Dimes: ")) * 0.05
    total += int( input(f"How many Pennies: ")) *0.01
    return total

def make_coffee(drinks, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drinks}, Enjoy")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = is_enough_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


