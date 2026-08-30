"""
Program to Print Full Pyramid Pattern (Star Pattern)
s
Given an integer N, the task is to print a full pyramid pattern with N rows.
In this pattern, each row contains an odd number of stars,
ranging from 1 star in the first row to (2 * N - 1) stars in the Nth row.
All the stars are center-aligned.

Input: 3
Output:
  *
 ***
*****

Input: 5
Output:
    *
   ***
  *****
 *******
*********
"""


def full_pyramid(n: int):
    star = 1
    space = n - 1

    for i in range(n):
        print(" " * (space - i), end="")
        print("*" * star, end="")
        star += 2
        print()
