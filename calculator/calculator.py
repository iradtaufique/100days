import art

def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

""""
Adding functions in in a dictionary with its correspondence symbol value
"""
operations = {
    "+": add,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

def calculator():
    print(art.logo)
    # create a variable that will change according to the user input
    restart = True
    # getting the first number
    num1 = float(input('Enter the first number: '))
    while restart:
        # displaying available operators
        for operator in operations:
            print(operator)
        symbol = input('Choose one operator from the list above: ')
        num2 = float(input('Enter the next number: '))

        result = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        user_choice = input(f"type 'y' to continue calculating with {result}, or 'n' to start new calculation: ").lower()

        # check User Choice
        if user_choice == 'y':
            num1 = result
        else:
            restart = False
            # clear the screen
            print('\n' * 20)
            calculator()

calculator()



