"""
11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by
array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section)
the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""

from typing import List

# 1 sec = 100M 1,000,000,000
# 10^4 = 10,000
# 10^5 = 100,000 (17) ==> n = 100,000; n log n = 1,700,000  ,n^2 =  10,000,000,000

"""
for i in range(n) -> n
    for j in range(n/2) -> log n
"""


def max_area(height: List[int]) -> int:
    # Area of rectangle = length * breadth
    n = len(height)
    # [1,8,6,2,5,4,8,3,7] 1,8
    maxi_area = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            breadth = min(height[i], height[j])
            length = j - i
            area = length * breadth
            maxi_area = max(area, maxi_area)
    return maxi_area


def max_area_optimal(height: List[int]) -> int:
    n = len(height)

    left, right = 0, n - 1
    maxi_area = 0

    while left < right:
        breadth = min(height[left], height[right])
        length = right - left
        area = length * breadth
        print(area)
        maxi_area = max(area, maxi_area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxi_area


# =======================================================


def maxArea(height: List[int]) -> int:

    # [1,8,6,2,5,4,8,3,7]
    n = len(height)
    max_area = 0
    for left in range(n - 1):
        for right in range(left + 1, n):
            h = min(height[left], height[right])
            width = right - left

            area = h * width

            max_area = max(area, max_area)

    return max_area


def maxArea_app(height: List[int]) -> int:
    # [1,8,6,2,5,4,8,3,7]
    n = len(height)
    max_area = 0

    left = 0
    right = n - 1

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        area = h * width
        max_area = max(area, max_area)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area
