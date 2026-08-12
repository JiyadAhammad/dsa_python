"""
14. Longest Common Prefix

Write a function to find the longest common
prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


## Python
# Time Complexity = O(n)
# Space Complexity = O(m), m = length of the shortest string.
def longestCommonPrefix(strs: List[str]) -> str:
    result = ""

    for i in range(len(strs[0])):
        prefix = strs[0][i]

        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != prefix:
                return result

        result += prefix
    return prefix
