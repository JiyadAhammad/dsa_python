"""
1. Python Basics ✅
    Python execution model,Variables,Dynamic typing,Type inference,Comments,
    print(),input(),Basic syntax,Indentation
2. Data Types ✅
    int,float,complex,bool,str,None,list,tuple,set,dict
3. Operators
    Arithmetic,Comparison,Logical,Assignment,Bitwise,Membership,
    Identity,is,is not,in,not in
4. Control Flow
    if,elif,else,for,while,break,continue,pass

Practice
Build:

✓ Calculator
✓ Number guessing game
✓ Prime number checker
✓ FizzBuzz
✓ Palindrome checker
✓ Frequency counter
"""

# Python Basics

# Read a data from input and print
# indentation defines the block — this is not optional
name = input("Enter your name -> ")  # input() always returns str
if name:
    print(f"name is {name}")  # 4-space block belongs to the if
else:
    print("Nothing entered")

# Operators
a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True  — same values
a is b  # False — two different list objects
2 in a  # True  — membership check

# Control Flow
# if / elif / else
score = 82
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"

# for
for ch in "abc":
    print(ch)
# a  b  c — one iteration per item

# while
n = 3
while n > 0:
    print(n)
    n -= 1
# runs until the condition is False

# break / continue / pass
for n in range(10):
    if n == 5:
        break  # exit loop
    if n % 2:
        continue  # skip odd
    pass  # placeholder, does nothing
