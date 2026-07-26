"""
503. Next Greater Element II
Medium
Topics
premium lock icon
Companies
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.



Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""

from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)

    result = []
    # [1, 2, 1]
    # [1,5,3,6,8]
    for i in range(n):
        is_found = False

        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result.append(nums[j])
                is_found = True
                break
        if not is_found:
            for j in range(i - 1):
                if nums[j] > nums[i]:
                    result.append(nums[j])
                    is_found = True
                    break

        if not is_found:
            result.append(-1)

    return result


def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):
        num = nums[i % n]
        while stack and stack[-1] <= num:
            stack.pop()
        if i < n and stack:
            ans[i] = stack[-1]
        stack.append(num)
    return ans
