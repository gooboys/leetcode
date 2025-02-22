'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        columns = len(matrix[0])
        length = rows*columns
        left = 0
        top = 1
        ret = [matrix[0][0]]
        state = 1
        row = 0
        column = 0
        while len(ret)<length:
            if state%4 == 1:
                column += 1
                if column == columns:
                    columns -= 1
                    column -= 1
                    state += 1
                    continue
                ret.append(matrix[row][column])
            elif state%4 == 2:
                row += 1
                if row == rows:
                    rows -= 1
                    row -= 1
                    state += 1
                    continue
                ret.append(matrix[row][column])
            elif state%4 == 3:
                column -= 1
                if column == left-1:
                    left += 1
                    column += 1
                    state += 1
                    continue
                ret.append(matrix[row][column])
            else:
                row -= 1
                if row == top-1:
                    top += 1
                    row += 1
                    state += 1
                    continue
                ret.append(matrix[row][column])
        return ret