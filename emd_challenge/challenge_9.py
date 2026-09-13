"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:

    n = len(nums)
    result = []
    hash_set = set()

    nums.sort()
    # [1,0,-1,0,-2,2]
    # [-2, -1, 0, 0, 1, 2]
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if four_sum == target:

                    sort = (nums[i], nums[j], nums[left], nums[right])
                    left += 1
                    right -= 1

                    result.append(sort)
                elif four_sum > target:
                    right -= 1
                else:
                    left += 1

    return result

    # n = len(nums)
    # result = []

    # for i in range(n - 3):
    #     for j in range(i + 1, n - 2):
    #         for k in range(j + 1, n - 1):
    #             for x in range(k + 1, n):
    #                 if nums[i] + nums[j] + nums[k] + nums[x] == target:
    #                     sort = sorted([nums[i], nums[j], nums[k], nums[x]])
    #                     if sort not in result:
    #                         result.append(sort)

    # return result
