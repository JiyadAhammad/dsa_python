"""
Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12
"""


def alternative_element_app1(arr: list):
    final_list = []
    for i, val in enumerate(arr):
        if i % 2 == 0:
            final_list.append(val)

    print(final_list)

    # Time Complexity O(n)
    # Space Complexity O(1)


def alternative_element_app2(arr: list):
    final_list = []

    for i in range(0, len(arr), 2):
        final_list.append(arr[i])

    print(final_list)

    # Time Complexity O(n)
    # Space Complexity O(1)


# Recursive Approach
def recursive_arr_item(idx: int, arr: list, result: list):
    if idx < len(arr):
        result.append(arr[idx])
        recursive_arr_item(idx + 2, arr, result)


def alternative_element_app3(arr: list):
    result = []
    recursive_arr_item(0, arr, result)

    print(result)

    # Time Complexity O(n)
    # Space Complexity O(n)
