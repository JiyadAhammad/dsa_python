"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​.
After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2,
with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k
(hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5,
with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k
(hence they are underscores).
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # [0, 1,2,3,]

    if not nums:
        return 0

    n = len(nums)

    left = 1

    for right in range(1, n):
        if nums[right] != nums[left - 1]:
            nums[left] = nums[right]
            left += 1

    return left


# ===========================================

# if not nums:
#     return 0

# n = len(nums)

# left = 0

# for right in range(1, n):
#     count = 0
#     if nums[left] != nums[right]:
#         while count > 0:
#             print(count)
#             nums.pop(left + 1)
#             count -= 1
#         left += 1
#     else:
#         count += 1
# print(nums)
# return len(nums)

# ===========================================

# if not nums:
#     return 0

# n = len(nums)

# left, count = 0, 1

# for right in range(1, n):
#     if nums[left] != nums[right]:
#         temp = nums[left + 1]
#         nums[left + 1] = nums[right]
#         nums[right] = temp
#         left += 1
#         count += 1
# return count

# ===========================================

# unique = set(nums)
# nums[:] = list(unique)
# nums.sort()
# return len(nums)
