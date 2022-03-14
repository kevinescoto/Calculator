def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num1 = int(input('Pick Your First Number: '))
    num2 = int(input('Pick Your Second Number: '))


    if operation == '+':
#Addition
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)
    elif operation == '-':
#Subraction
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)
    elif operation == '*':
#Multiply
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)
    elif operation == '/':
#Division
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print("No a Available Option, Try Again.")

calculate()