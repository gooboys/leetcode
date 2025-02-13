'''
289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton 
devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: 
live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

1. Any live cell with fewer than two live neighbors dies (under-population).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (over-population).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

The next state of the board is determined by applying these rules simultaneously to every cell in the 
m x n grid. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note: You do not need to return anything.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        empty = [0] * (columns+2)
        track = [empty]
        for row in board:
            temp = row[:]
            track.append(temp)
            track[-1].append(0)
            track[-1].insert(0,0)
        track.append(empty)
        for row in range(rows):
            for column in range(columns):
                cur = board[row][column]
                nearby = self.death(track, row, column)
                if cur:
                    if nearby < 2 or nearby > 3:
                        board[row][column] = 0
                elif nearby == 3:
                    board[row][column] = 1
         
    def death(self, track, row, column):
        living = 0
        for i in range(3):
            for j in range(3):
                living += track[row+i][column+j]
        return living - track[row+1][column+1]
            
            