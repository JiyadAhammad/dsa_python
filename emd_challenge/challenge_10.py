"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List

"""
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

00,01,02
10,11,12
20,21,22

"""


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    n = len(matrix)
    m = len(matrix[0])
    result = []
    top, bottom = 0, n - 1
    left, right = 0, m - 1

    """
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    """

    # left -> right -> bottom -> left -> top
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
