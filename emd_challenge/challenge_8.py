"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

"""
101 + 1 = 110
"""


def addBinary(a: str, b: str) -> str:
    # a = "11", b = "1"

    bin_a = len(a) - 1
    bin_b = len(b) - 1

    reminder = 0

    result = []

    while bin_a >= 0 or bin_b >= 0 or reminder:
        total = reminder

        if bin_a >= 0:
            total += int(a[bin_a])
            bin_a -= 1
        if bin_b >= 0:
            total += int(b[bin_b])
            bin_b -= 1

        # print(total)

        result.append(str(total % 2))
        # 0
        reminder = total // 2

    return "".join((reversed(result)))

    # decimal_a = int(a, 2)
    # decimal_b = int(b, 2)

    # decimal_sum = decimal_a + decimal_b

    # result = bin(decimal_sum)[2:]
    # return result
