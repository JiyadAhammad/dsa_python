"""
Frequency counter
Walk a string or list, tally occurrences of each item into a dict.
"""

while True:
    try:
        word = input("Enter a String -> ")

        if not word.strip(" "):
            print("Please enter a valid string")
            continue
        break
    except ValueError:
        print("Value error")

frequency_map = {}
n = len(word)

for char in word:
    frequency_map[char] = frequency_map.get(char, 0) + 1

# for i in range(n):
#     if word[i] not in frequency_map:
#         frequency_map[word[i]] = 1
#     else:
#         frequency_map[word[i]] = frequency_map[word[i]] + 1


print(frequency_map)
