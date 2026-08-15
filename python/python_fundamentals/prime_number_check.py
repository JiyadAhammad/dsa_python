"""
Prime number checker
Loop from 2 up to n, use modulo to test divisibility,
break as soon as a factor is found.
"""

# 1,3,5,7,11,13,17...

while True:
    try:
        num = int(input("Enter a number greater than 2 upto 100"))
        if num < 2:
            print("Number less than 2 not prime")
            continue
        elif num > 100:
            print("Number less than 100 is allowed")
            continue
        else:
            break
    except ValueError:
        print("Wrong input ")
        continue
isPrime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print("Not a prime")
        isPrime = False
        break
if isPrime:
    print("Entered prime number")
