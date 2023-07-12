from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Make two pointers, with one n nodes in front of the other.
        if head.next is None:
            return None

        back_pointer = ListNode(0, head)
        ahead_pointer = head

        for i in range(n):
            ahead_pointer = ahead_pointer.next

        while ahead_pointer is not None:
            back_pointer = back_pointer.next
            ahead_pointer = ahead_pointer.next

        if back_pointer.next == head:
            return head.next

        back_pointer.next = back_pointer.next.next

        return head

    # Verified Leetcode