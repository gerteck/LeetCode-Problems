from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        rotting = []
        to_rot = []
        has_fresh_oranges = False

        m = len(grid)
        n = len(grid[0])

        # 0 is an empty cell, 1 is a fresh orange, 2 is a rotten orange.

        # First we iterate through the grid to find to rot oranges.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotting.append([i, j])
                if grid[i][j] == 1:
                    has_fresh_oranges = True

        if not has_fresh_oranges:
            return 0

        def rot_nearby(i, j):
            if i > 0:
                if grid[i-1][j] == 1:
                    grid[i - 1][j] = 2
                    to_rot.append([i-1, j])
            if j > 0:
                if grid[i][j-1] == 1:
                    grid[i][j - 1] = 2
                    to_rot.append([i, j-1])
            if i < m - 1:
                if grid[i+1][j] == 1:
                    grid[i + 1][j] = 2
                    to_rot.append([i+1, j])
            if j < n - 1:
                if grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    to_rot.append([i, j + 1])

        while len(rotting) > 0:
            # Fills up the to rot list.
            for position in rotting:
                rot_nearby(position[0], position[1])

            # Move it to rotting list
            count += 1
            rotting = to_rot
            to_rot = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return count - 1




