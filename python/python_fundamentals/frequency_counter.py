"""
Frequency counter
Walk a string or list, tally occurrences of each item into a dict.
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

frequency_map = {}
n = len(word)

for i in range(n):
    pass
