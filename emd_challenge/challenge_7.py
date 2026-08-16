"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color
red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""

from typing import List


def sortColors(nums: List[int]) -> None:
    n = len(nums)
    # [2,0,2,1,1,0]

    left, mid, right = 0, 0, n - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1


# n = len(nums)

# count_zero = 0
# count_one = 0
# count_two = 0

# for i in range(n):
#     if nums[i] == 0:
#         count_zero += 1
#     elif nums[i] == 1:
#         count_one += 1
#     else:
#         count_two += 1
# count = 0
# for i in range(count_zero):
#     nums[count] = 0
#     count += 1
# for i in range(count_one):
#     nums[count] = 1
#     count += 1
# for i in range(count_two):
#     nums[count] = 2
#     count += 1
