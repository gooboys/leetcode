'''
200. Number of Islands

Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ret = 0
        rows = len(grid)
        columns = len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=='1':
                    ret += 1
                    self.makeZeros(grid, row, column)
        return ret

    def makeZeros(self, grid, row, column):
        if row < 0 or column < 0:
            return
        if row >= len(grid) or column >= len(grid[0]):
            return
        if grid[row][column] == '0':
            return
        grid[row][column] = '0'
        self.makeZeros(grid, row-1, column)
        self.makeZeros(grid, row+1, column)
        self.makeZeros(grid, row, column-1)
        self.makeZeros(grid, row, column+1)
        return