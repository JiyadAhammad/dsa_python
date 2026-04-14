"""
Given the head of a singly linked list,
return true if it is a palindrome or false otherwise.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def palindrome_linked_list_app1(self, head: Optional[ListNode]) -> bool:
    stack = []

    temp = head

    while temp:
        stack.append(temp.val)
        temp = temp.next

    temp = head

    while temp:
        if temp.val != stack[-1]:
            return False
        stack.pop()
        temp = temp.next

    return not stack

    # Time Complexity O(n)
    # Space Complexity O(1)


def reverse_ll(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def palindrome_linked_list_app2(self, head: Optional[ListNode]) -> bool:

    if not head:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next

    new_head = reverse_ll(mid)

    first = head
    second = new_head

    while second:
        if first.val != second.val:
            reverse_ll(new_head)
            return False
        second = second.next
        first = first.next

    reverse_ll(new_head)
    return True
