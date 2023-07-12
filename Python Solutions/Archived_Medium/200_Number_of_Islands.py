from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_islands = 0

        # Use a stack and a helper function.
        # 1s represent land while 0 represents water
        # Return the number of islands

        def fill_island(i, j):
            grid[i][j] = 2
            if i > 0:
                if grid[i - 1][j] == "1":
                    grid[i - 1][j] = 2
                    fill_island(i-1, j)
            if j > 0:
                if grid[i][j - 1] == "1":
                    grid[i][j - 1] = 2
                    fill_island(i, j-1)
            if i < m - 1:
                if grid[i + 1][j] == "1":
                    grid[i + 1][j] = 2
                    fill_island(i + 1, j)
            if j < n - 1:
                if grid[i][j + 1] == "1":
                    grid[i][j + 1] = 2
                    fill_island(i, j + 1)

        # Let 2 be the number representing a filled island
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    no_of_islands += 1
                    fill_island(i, j)

        print("Number of islands: ", no_of_islands)
        return no_of_islands


a = Solution()
print(a.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

# Verified and Accepted Leetcode
