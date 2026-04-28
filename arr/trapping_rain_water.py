"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is
represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    water = 0
    # [0,1,0,2,1,0,1,3,2,1,2,1]
    for i in range(n):
        left_max = right_max = 0

        for j in range(i + 1):
            left_max = max(left_max, height[j])

        for j in range(i, n):
            right_max = max(right_max, height[j])

        water += min(left_max, right_max) - height[i]

    return water


def trap_app(height: List[int]) -> int:
    n = len(height)
    water = 0
    left, right = 0, n - 1

    left_max, right_max = height[left], height[right]

    while left < right:

        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water
