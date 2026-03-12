import os
from quad import quadratic_formula

while True:
    print("Simple Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    action=input("Press the symbol of the operation you want to perform (+, -, *, /) or 'q' to quit: ")
    if action == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    elif action in ['+', '-', '*', '/', 'q']:
         if action == '+':
            print("Sum:", num1 + num2)
         elif action == '-':
            print("Difference:", num1 - num2)
         elif action == '*':
            print("Product:", num1 * num2)
         elif action == '/':
            if num2>num1:
                num1, num2 = num2, num1
            if num2 != 0:
                print("Quotient:", num1 / num2)
            else:        
                print("Cannot divide by zero")
         elif action == 'Q':
            num3=int(input("Enter the third number: "))
            quadratic_formula(num1, num2, num3)
    again=input("Do you want to perform another calculation? (y/n): ")
    if again.lower() != 'y':
        print("Exiting the calculator")
        break
    os.system('clear')