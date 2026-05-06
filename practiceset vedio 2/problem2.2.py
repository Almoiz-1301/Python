
# Write a program using match case that simulates a simple calculator
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

num  = int(input("Enter first number:   "))
num2 = int(input("Enter second number:  "))
operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"{num} + {num2} = {num + num2}")
    case "-":
        print(f"{num} - {num2} = {num - num2}")
    case "*":
        print(f"{num} * {num2} = {num * num2}")
    case "/":
        if num2 != 0:
            print(f"{num} / {num2} = {num / num2}")
        else:
            print("Division by zero is not allowed.")
    case _:
        print("Invalid operation.")