import math

def authorsnotes():
    print("Current Version is under development, Work Continuation TBD.")

def welcome():
    print()
    print("Welcome To Number Cruncher V1.3")
    print("Current Version is Incomplete, Future Additions Coming")

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
root for Square Root
fact for factorial calculation
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
        #Power
    elif operation == '**':
        print('{} ** {} = '.format(num1, num2))
        print(num1 ** num2)

    elif operation == 'root':
        print('Square Root of {} = '.format(num1))
        print(math.sqrt(num1))

    elif operation == 'fact':
        print('The Factorial of {} = '.format(num1))
        print(math.factorial(num1))
        
    else:
        print("Not a Available Option, Try Again.")

    again()


def again():
    use_again = input('''
Do You Want to Use the Calculator Again?
Please type Y for Yes or N for No.
''')
    if use_again.upper() == 'Y':
        calculate()
    elif use_again.upper() == 'N':
        print("See You Later")
    else:
        again()
    
logo()    
welcome()
calculate()