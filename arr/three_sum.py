"""
15. 3Sum

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


def threeSum_app(nums: list[int]) -> list[list[int]]:
    n = len(nums)

    result = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])

                    print(triplet)

                    if triplet not in result:
                        result.append(triplet)

    return result


def threeSum_app2(nums: list[int]) -> list[list[int]]:
    n = len(nums)

    result = []

    nums.sort()

    # [-1, 0, 1, 2, -1, -4]

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1

        while left < right:

            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                right -= 1
                left += 1

            elif sum > 0:
                right -= 1
            else:
                left += 1

    return result
