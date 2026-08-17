"""
FizzBuzz
For 1–100,
print Fizz on multiples of 3,
Buzz on multiples of 5,
FizzBuzz on both.
"""

while True:
    try:
        num = int(input("Enter a number between 1 to 100 -> "))

        if num < 1 or num > 100:
            print('"Entered number is not in range of 1 to 100"')
            continue
        break
    except ValueError:
        print("Please Enter a number")

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Not a valid divisible")
