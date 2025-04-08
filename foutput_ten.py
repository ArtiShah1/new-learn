# chap -10
# functions - def my_function():....called ......my_function()
# functions with inputs - def my_function(something (perameter)): ......called...my_function(123)
# functions with outputs - def my_function(): .....result & return ----output


def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())


format_name("angela", "AnGela")


# ........OR.....
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name} {formated_l_name}")


format_name("artI", "SHAH")


# ................OR ..........
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name("aMy", "SHAH"))

# ------------task DOCSTRINGS-------------
"""DOCSTRINGS"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("what is your first number?:"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation:")
        num2 = float(input("what is your next number?:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation") == "Y":
            num1 = answer
        else:
            should_continue = False


calculator()

# operation_symbol = input("pick another operation:")
# num3 = int(input("what's the next number"))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function (first_answer,num3)
# print(f"{first_answer}{operation_symbol}{num3} = {second_answer}")
