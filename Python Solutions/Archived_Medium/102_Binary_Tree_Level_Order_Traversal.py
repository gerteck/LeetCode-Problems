from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        node_queue = []
        level_queue = []
        level_counter = -1
        result = []

        # Add root into queue.
        node_queue.append(root)
        level_queue.append(0)

        while len(node_queue) > 0:
            node = node_queue.pop(0)
            level = level_queue.pop(0)

            if level > level_counter:
                result.append([node.val])
                level_counter += 1
            else:
                result[level].append(node.val)

            # Check Left side
            if node.left is not None:
                node_queue.append(node.left)
                level_queue.append(level + 1)

            if node.right is not None:
                node_queue.append(node.right)
                level_queue.append(level + 1)

        return result



