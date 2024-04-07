#Calculator

from art import logo

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operation = {
    "+": add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    print(logo)
    num1 = int(input("Enter the a number: "))

    for symbols in operation:
        print(symbols)

    should_continue = True

    while should_continue:
        operator = input("Choose the operation from the above: ")
        num2 = int(input("Enter the next number: ")) 
        calculation_function = operation[operator]
        answer = calculation_function(num1,num2) 

        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Would you like to continue with {answer}.Type 'y' to continue or 'n' to start new calculation. ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator() 

