"""
Refactored Calculator using OOP
"""
class Calculator:
    def __init__(self):
        self.is_a_calculator = True

    def add(self):
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number to add: "))
        add_total = int1 + int2
        add_result = f"{int1} % {int2} = {add_total}"
        print(add_result)
        return add_result
    def subtract(self):
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number to subtract: "))
        subtract_total = int1 - int2
        subtract_result = f"{int1} % {int2} = {subtract_total}"
        print(subtract_result)
        return subtract_result

    def multiply(self):
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number to multiply: "))
        multiply_total = int1 * int2
        multiply_result = f"{int1} % {int2} = {multiply_total}"
        print(multiply_result)
        return multiply_result
    def divide(self):
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number to divide: "))
        divide_total = int1 / int2
        divide_result = f"{int1} / {int2} = {divide_total}"
        print(divide_result)
        return divide_result

    def modu(self):
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number to modulo: "))
        modu_total = int1 % int2
        modu_result = f"{int1} % {int2} = {modu_total}"
        print(modu_result)
        return modu_result

first_sums = Calculator()
first_sums.add()
first_sums.subtract()
first_sums.multiply()
first_sums.divide()
first_sums.modu()


