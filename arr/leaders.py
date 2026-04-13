"""
Leaders in an array

Given an array arr[] of size n,
the task is to find all the Leaders in the array.
An element is a Leader if it is greater than or equal to all
the elements to its right side.

Note: The rightmost element is always a leader.
Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e.,
[4, 3, 5, 2], therefore 17 is a leader.
5 is greater than all the elements to its right i.e.,
[2], therefore 5 is a leader. 2 has no element to its right,
therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e.,
[2], therefore 5 is a leader. 2 has no element to its right,
therefore 2 is a leader.
"""


def leaders_app1(arr: list):
    res = []
    for i in range(len(arr) - 1):
        is_leader = True
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                is_leader = False
                break

        if is_leader:
            res.append(arr[i])
    res.append(arr[len(arr) - 1])

    print(res)

    # Time Complexity O(n)
    # Space Complexity O(1)


def leaders_app2(arr: list):
    res = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                break
        else:
            res.append(arr[i])
    res.append(arr[len(arr) - 1])

    print(res)

    # Time Complexity O(n)
    # Space Complexity O(1)


def leaders_app3(arr: list):
    res = []
    n = len(arr)

    max_right = arr[-1]

    res.append(max_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            res.append(max_right)
    res.reverse()
    print(res)
