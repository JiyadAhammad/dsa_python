"""
Palindrome checker
Compare a string to its reverse (s[::-1])
to test if it reads the same both ways.
"""

while True:
    try:
        word = input("Enter a String")

        if not word.strip(" "):
            print("Please enter a valid string")
            continue
        break
    except ValueError:
        print("Value error")

## Use python inbuilt slice method
if word == word[::-1]:
    print("Entered is a palindrome")
else:
    print("Entered is not a palindrome")

# Use normal two pointer approach
# n = len(word)
# left, right = 0, n - 1
# is_palindrome = True
# while left <= right:
#     if word[left] != word[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1

# if is_palindrome:
#     print("Entered is a palindrome")
# else:
#     print("Entered is not a palindrome")
