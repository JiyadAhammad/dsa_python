"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


def find_square(val: int) -> int:
    ans = 0
    while val:
        digit = val % 10
        ans += digit**2
        val = val // 10

    return ans


def happy_number(number: int) -> bool:
    slow = find_square(number)
    fast = find_square(find_square(number))

    while slow != fast:
        if fast == 1:
            return True
        slow = find_square(slow)
        fast = find_square(find_square(fast))

    return slow == 1
