"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without
duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"

Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n < 2:
        return n

    cur_len = max_len = 0
    unique = set()
    # "pwwkew"

    for i in range(n - 1):
        cur_len = 1
        for j in range(i + 1, n):
            if s[i] != s[j] and s[j] not in unique:
                cur_len += 1
                unique.add(s[j])
            else:
                break
        print(s[i], max_len, cur_len)
        max_len = max(max_len, cur_len)
    return max_len
