# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      #height = 0
      if root is None: # case 1: root is None
        return 0
      elif root.left is None and root.right is None: # case 2: root does not have children
        return 1
      elif root.left is None and root.right is not None:
        #height = height + 1 + self.maxDepth(root.right)
        return 1 + self.maxDepth(root.right)
      elif root.right is None and root.left is not None:
        #height = height + 1 + self.maxDepth(root.left)
        return 1 + self.maxDepth(root.left)
      else: # root has 2 children
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))