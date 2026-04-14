from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0

    temp = head

    while temp:
        count += 1
        temp = temp.next

    temp = head
    node_count = count - n

    if node_count == 0:
        return head.next

    while temp:
        node_count -= 1
        if node_count == 0:
            temp.next = temp.next.next

        temp = temp.next

    return head
