while True:
    print("Simple Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    action=input("Press the symbol of the operation you want to perform (+, -, *, /) or 'q' to quit: ")
    if action == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    elif action in ['+', '-', '*', '/']:
         if action == '+':
            print("Sum:", num1 + num2)
         elif action == '-':
            print("Difference:", num1 - num2)
         elif action == '*':
            print("Product:", num1 * num2)
         elif action == '/':
            if num2 != 0:
                print("Quotient:", num1 / num2)
            else:        
                print("Cannot divide by zero")