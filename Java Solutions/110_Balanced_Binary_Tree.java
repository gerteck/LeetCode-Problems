/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean balanced = true;

    public boolean isBalanced(TreeNode root) {
        // first compute the height
        // then determine?
        height(root);
        return balanced;
    }

    int height(TreeNode root) {
        if (root == null) return -1;
        int leftH = height(root.left);
        int rightH = height(root.right);
        if (Math.abs(leftH - rightH) > 1) {
            balanced = false;
        }
        return Math.max(leftH, rightH) + 1;
    }



}