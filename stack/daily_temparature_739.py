"""
739. Daily Temperatures

Hint
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List


def dailyTemperatures(nums: List[int]) -> List[int]:
    n = len(nums)

    ans = [0] * n

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = j - i
                break
    return ans


def dailyTemperatures_2(nums: List[int]) -> List[int]:
    n = len(nums)

    stack = []
    ans = [0] * n
    #  0, 1, 2, 3, 4, 5, 6, 7
    # [73,74,75,71,69,72,76,73]
    # [6,2,1,0]
    # [1,1,4,2,1,1,0,0]
    for i in range(n - 1, -1, -1):

        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1] - i

        stack.append(i)
        print(stack)

    return ans
