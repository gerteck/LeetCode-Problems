/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        // Put it in  a stack ig
        Stack<ListNode> stack = new Stack();
        ListNode node = head;

        while (node != null) {
            stack.push(node);
            node = node.next;
        }

        ListNode newHead = stack.pop();
        node = newHead;

        while (!stack.empty()) {
            node.next = stack.pop();
            node = node.next;
        }

        node.next = null;
        return newHead;

    }
}