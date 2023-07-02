# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

'''
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with 
val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency 
list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        # Possible can do recursion
        # Naive solution: put nodes in a list and connect them naively.
        nodes_list = [None] * 101
        nodes_list[node.val] = Node(node.val, [])

        root = nodes_list[node.val]

        def process_node(original_node):
            clone_node = nodes_list[original_node.val]
            for x in original_node.neighbors:
                # If new clone node does not exist, initialize and process it.
                if nodes_list[x.val] is None:
                    nodes_list[x.val] = Node(x.val, [])
                    process_node(x)
                # Add neighbour clone node to neighbour list
                clone_node.neighbors.append(nodes_list[x.val])

        process_node(node)
        return root


# Verified Accepted Submission on Leetcode.