"""
Calculator
Take two numbers and an operator from input(),
branch on the operator with if/elif, print the result.
"""

import sys

try:
    num1 = int(input("Enter first number"))
except:
    print("Please Enter a number")
    sys.exit()
try:
    num2 = int(input("Enter second number"))
except:
    print("Please Enter a number")
    sys.exit()

try:
    choice = input("Enter your choice \n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choiceVal = int(choice)
except:
    print("Invalid choice select 1,2,3,4 any")
    sys.exit()

if choiceVal == 1:
    result = num1 + num2
    print(result)
elif choiceVal == 2:
    result = num1 - num2
    print(result)
elif choiceVal == 3:
    result = num1 * num2
    print(result)
elif choiceVal == 4:
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Can't divide bt zero")
else:
    print("Wrong choice selected")
