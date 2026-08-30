"""
Program to Print Inverted Right Half Pyramid Pattern (Star Pattern)
Last Updated :
30 Jan, 2026
Given an integer N, print N rows of an inverted right half pyramid pattern.
In an inverted right half pattern of N rows,
the first row has N number of stars,
the second row has (N - 1) number of stars,
and so on till the Nth row, which has only 1 star.

Input: n = 5
Output:
*****
****
***
**
*

Input: n = 3
Output:
***
**
*
"""


def inverted_right_half_pyramid_pattern(n: int):

    # for i in range(n, 0, -1):
    #     for j in range(i):
    #         print("*", end="")
    #     print()

    for i in range(n, 0, -1):
        print("*" * (i))
