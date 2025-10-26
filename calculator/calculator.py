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


# getting the first number
num1 = float(input('Enter the first number: '))
# displaying available operators
for operator in operations:
    print(operator)
symbol = input('Choose one operator from the list above: ')
num2 = float(input('Enter the next number: '))

result = operations[symbol](num1, num2)
print(f"{num1} {symbol} {num2} = {result}")
user_choice = input(f"type 'y' to continue calculating with {result} or 'n' to start new calculation: ").lower()





