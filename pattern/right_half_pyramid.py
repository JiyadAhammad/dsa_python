"""
Print Right Half Pyramid Star Pattern

Given an integer N, print a right half pyramid star pattern with N rows.
The first row has 1 star, the second row has 2 stars,
and each next row has one more star than the previous row.
The Nth row has N stars, and all stars are left aligned.

Examples:

Input: N = 3
Output:
*
**
***

Input: N = 5
Output:
*
**
***
****
*****
"""


def right_half_pyramid_pattern(n: int):

    # for i in range(1, n + 1):
    #     for j in range(1, i + 1):
    #         print("*", end="")
    #     print()
    for i in range(n):
        print("*" * (i + 1))
