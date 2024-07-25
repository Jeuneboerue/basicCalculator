def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1*n2
    


def calculator():

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    shouldContinue = True
    num1 = float(input("What's the first number?"))


    for symbol in operations:
        print(symbol)

    while shouldContinue:

        operationSymbol = input("Pick an operation symbol from the line above.")
        num2 = float(input("What's the second number?"))

        calculationFunction = operations[operationSymbol]

        answer = calculationFunction(num1, num2)

        print(f"{num1} {operationSymbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with calculating {answer}, or type 'n' to start with new number.") == "y":
            num1 = answer
        else:
            shouldContinue = False
            calculator()

calculator()




