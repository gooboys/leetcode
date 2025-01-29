'''
73. Set Matrix Zeroes

Difficulty: Medium
Topics: Array, Matrix
Companies: Common in technical interviews

Problem Description:
Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`'s. 
You must do this **in place** without using extra space for another matrix.

Examples:

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation:
- The element at (1,1) is 0.
- Set the entire 1st row and 1st column to 0's.

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Explanation:
- The element at (0,0) is 0, so set the 0th row and column to 0's.
- The element at (0,3) is 0, so set the 0th row and 3rd column to 0's.

Constraints:
1. `m == matrix.length`
2. `n == matrix[0].length`
3. 1 <= `m, n` <= 200
4. -2^31 <= matrix[i][j] <= 2^31 - 1

Follow-Up:
1. Could you devise a solution that uses O(m + n) space?
2. Could you devise a solution that uses O(1) space (in place)?
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        rowCount = len(matrix)
        colCount = len(matrix[0])
        for row in range(rowCount):
            for col in range(colCount):
                if matrix[row][col] == 0:
                    rows.append(row)
                    columns.append(col)
        for i in rows:
            matrix[i] = [0]*colCount
        for i in columns:
            for row in matrix:
                row[i] = 0
        return matrix