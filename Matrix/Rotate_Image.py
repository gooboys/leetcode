'''
48. Rotate Image

Difficulty: Medium
Topics: Array, Matrix
Companies: Common in technical interviews

Problem Description:
You are given an `n x n` 2D matrix representing an image. Rotate the image **90 degrees clockwise**.

Task:
- Modify the input 2D matrix **in-place** (without allocating another matrix).
- The transformation should be performed directly on the given matrix.

Examples:

Example 1:
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
Output: [[7,4,1],
         [8,5,2],
         [9,6,3]]
Explanation:
- The first column `[7,4,1]` becomes the first row.
- The second column `[8,5,2]` becomes the second row.
- The third column `[9,6,3]` becomes the third row.

Example 2:
Input: matrix = [[5,1,9,11],
                 [2,4,8,10],
                 [13,3,6,7],
                 [15,14,12,16]]
Output: [[15,13,2,5],
         [14,3,4,1],
         [12,6,8,9],
         [16,7,10,11]]
Explanation:
- The first column `[15,14,12,16]` becomes the first row.
- The second column `[13,3,6,7]` becomes the second row, etc.

Constraints:
1. `n == matrix.length == matrix[i].length` (square matrix)
2. `1 <= n <= 20`
3. `-1000 <= matrix[i][j] <= 1000`
'''

class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        cp = []
        for i in range(length):
            cp.append([0]* length)
        for row in range(length):
            for val in range(length):
                cp[row][val] = matrix[row][val]
        for row in range(length):
            for val in range(length):
                matrix[val][length-row-1] = cp[row][val]
        return