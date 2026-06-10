"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    eg :[1,3,12,0,0]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Example 3:
    Input: nums = [1,0]
    Output: [1,0]
"""

from typing import List


def move_zeros_brute(nums: List[int]) -> List[int]:

    n = len(nums)
    left = 0

    for i in range(n):
        if nums[i] != 0:
            temp = nums[left]
            nums[left] = nums[i]
            nums[i] = temp
            left += 1
    return nums
