"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the
color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

from typing import List


def sortColors(nums: List[int]) -> None:
    n = len(nums)
    count = 0
    sort_list = []
    for i in range(n):
        if nums[i] == 0:
            sort_list.insert(0, nums[i])
            count += 1
        elif nums[i] == 2:
            sort_list.insert(n - 1, nums[i])
        else:
            sort_list.insert(count, nums[i])

    nums = sort_list

    print(nums)


def sortColors_app(nums: List[int]) -> None:
    n = len(nums)

    count_zero = 0
    count_one = 0
    count_two = 0

    for i in range(n):
        if nums[i] == 0:
            count_zero += 1
        elif nums[i] == 1:
            count_one += 1
        else:
            count_two += 1

    count = 0

    while count_zero > 0:
        nums[count] = 0
        count_zero -= 1
        count += 1

    while count_one > 0:
        nums[count] = 1
        count_one -= 1
        count += 1

    while count_two > 0:
        nums[count] = 2
        count_two -= 1
        count += 1

    print(nums)


def sortColors_app2(nums: List[int]) -> None:
    # DNF Algo
    n = len(nums)

    low = mid = 0
    high = n - 1
    # [2,0,2,1,1,0]
    while mid <= high:
        if nums[mid] == 0:
            nums[mid] = nums[low]
            nums[low] = 0
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid] = nums[high]
            nums[high] = 2
            high -= 1
    print(nums)
