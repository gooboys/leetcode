'''
74. Search a 2D Matrix

You are given an m x n integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `True` if `target` is in `matrix` or `False` otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: True

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: False

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target<matrix[0][0] or target>matrix[-1][-1]: return False
        rows = len(matrix)
        columns = len(matrix[0])
        lRow = 0
        rRow = rows
        while lRow<rRow:
            row = (lRow+rRow)//2
            if matrix[row][0]<=target and target<=matrix[row][-1]:
                lRow = rRow
            elif matrix[row][0]>target:
                rRow = row
            else:
                lRow = row+1
        left = 0
        right = columns
        if matrix[row][0] == target:
            return True
        while left<right:
            mid = (left+right)//2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid]<target: left = mid+1
            else: right = mid
        return False