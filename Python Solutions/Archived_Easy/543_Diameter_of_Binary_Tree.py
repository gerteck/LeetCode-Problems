# Given the root of a binary tree,
# return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented
# by the number of edges between them.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Diameter will always be length of the longest path between two leaf nodes.
# May or may not pass through root


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_count = 0

        def helper(root):
            nonlocal max_count
            left_path = 0
            right_path = 0
            if root is None:
                return 0
            if root.left is not None:
                left_path = helper(root.left) + 1
            if root.right is not None:
                right_path = helper(root.right) + 1
            max_count = max(max_count, left_path + right_path)
            return max(left_path, right_path)

        root_path = helper(root)

        return max(root_path, max_count)


