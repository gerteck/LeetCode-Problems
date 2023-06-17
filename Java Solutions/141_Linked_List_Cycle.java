/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {

        // Floyd Cycle Finding Algorithm Fast and Slow pointers:
        if (head == null) return false;
        ListNode fastPointer = head.next;
        ListNode slowPointer = head;

        while (fastPointer != null) {
            if (slowPointer == fastPointer) return true;
            fastPointer = fastPointer.next;
            if (fastPointer != null) fastPointer = fastPointer.next;
            slowPointer = slowPointer.next;
        }

        return false;

    }
}