from typing import List

# Given an m x n binary matrix mat, return the distance
# of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Do something similar to BFS:
# Just optimize the box with every run.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        new_matrix = [[m + n for j in range(n)] for i in range(m)]

        # # Initialize 0 values first
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    new_matrix[i][j] = 0

        def optimize_neighbours(i, j):
            value = new_matrix[i][j]
            if i > 0 :
                if new_matrix[i-1][j] - 1 > value:
                    new_matrix[i-1][j] = value + 1
                    optimize_neighbours(i-1, j)
            if i < m - 1 :
                if new_matrix[i + 1][j] - 1 > value:
                    new_matrix[i + 1][j] = value + 1
                    optimize_neighbours(i + 1, j)
            if j > 0 :
                if new_matrix[i][j - 1] - 1 > value:
                    new_matrix[i][j - 1] = value + 1
                    optimize_neighbours(i, j - 1)
            if j < n - 1 :
                if new_matrix[i][j + 1] - 1 > value:
                    new_matrix[i][j + 1] = value + 1
                    optimize_neighbours(i, j + 1)

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    optimize_neighbours(i,j)

        return new_matrix


a = Solution()
print(a.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))

# Notes: python is too slow to compute this. Leetcode time limit exceeded.
# See java solution.
