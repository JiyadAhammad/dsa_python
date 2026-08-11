"""
Prime number checker
Loop from 2 up to n, use modulo to test divisibility,
break as soon as a factor is found.
"""

# 1,3,5,7,11,13,17...

while True:
    try:
        num = int(input("Enter a number greater than 1 upto 100"))
        if num < 0:
            print("Negative number not allowed")
            continue
        elif num < 2:
            print("Number less than 2 is prime")
            continue
        elif num > 100:
            print("Number less than 100 is allowed")
            continue
        else:
            break
    except ValueError:
        print("Wrong input ")
        continue
