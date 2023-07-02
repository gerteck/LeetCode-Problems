from typing import List

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
# if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# [0,1] means [ 0 => 1 ]
'''
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''


# The question is asking in other words if there is any way to topologically sort the nodes!
# This also means the graph must be acyclic.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Do topological sort.

        # List to represent in degree of nodes.
        in_degree = [0]*numCourses

        # List to represent nodes pointing out
        nodes_fulfilled = [[] for i in range(numCourses)]

        # First, we process the data.
        for pair in prerequisites:
            preq = pair[0]
            post = pair[1]

            # We add one to the in degree of the post, and add the satisfied node to nodes_fufilled of the preq
            in_degree[post] = in_degree[post] + 1
            nodes_fulfilled[preq].append(post)

        # Now, we start our topological ordering.
        # We always want to start with an in_degree = 0, and slowly sort through.

        count = 0

        while count < numCourses:
            removed = False

            for i in range(numCourses):
                # Starting node: Go through all fulfilled nodes and minus off the in_degree of those nodes.
                if in_degree[i] == 0:
                    count += 1
                    removed = True
                    fulfilled_list = nodes_fulfilled[i]

                    # Decrement the in_degree
                    for node_int in fulfilled_list:
                        in_degree[node_int] = in_degree[node_int] - 1

                    in_degree[i] = -1

            if not removed:
                return False

        return True


a = Solution()
print(a.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
# Expected: True
# Verified answer accepted on Leetcode.
