from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(lower_bound, upper_bound, node):
            if node is None:
                return True

            if upper_bound is not None:
                if node.val >= upper_bound:
                    return False

            if lower_bound is not None:
                if node.val <= lower_bound:
                    return False

            # ## Left Subtree: Constrained by val as upperbound.
            # validate_left = helper(lower_bound, node.val, node.left)

            # ## Right Subtree: Constrained by val as lowerbound.
            # validate_right = helper(node.val, upper_bound, node.right)

            return helper(lower_bound, node.val, node.left) and helper(node.val, upper_bound, node.right)

        return helper(None, None, root)

# Verified Accepted Submission on LeetCode.
