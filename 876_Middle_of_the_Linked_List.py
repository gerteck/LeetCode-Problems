# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def middleNode(self, head: [ListNode]) -> Optional[ListNode]:
    # Approach: Have a fast and slow pointer.
    def middleNode(self, head: ListNode) -> ListNode:
        if (head.next is None):
            return head
        slow = head
        fast = head.next

        while (fast.next is not None):
            if (fast.next.next is None):
                return slow.next
            else:
                fast = fast.next.next
                slow = slow.next

        return slow.next